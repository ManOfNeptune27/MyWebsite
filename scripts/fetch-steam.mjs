import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const projectRoot = fileURLToPath(new URL('../', import.meta.url));
const envPath = path.join(projectRoot, '.env');
const outputPath = path.join(projectRoot, 'src/lib/data/games.json');

/**
 * @typedef {{
 *   title: string;
 *   hours: number;
 *   platform: string;
 *   achievements_unlocked?: number;
 *   achievements_total?: number;
 *   achievements_completion?: number;
 * }} SnapshotGame
 */

async function readCredentials() {
  let envContents;
  try {
    envContents = await readFile(envPath, 'utf8');
  } catch (error) {
    if (error instanceof Error && 'code' in error && error.code === 'ENOENT') {
      throw new Error('Missing .env file. Add STEAM_API_KEY and STEAM_USER_ID before running this script.');
    }
    throw error;
  }

  const values = new Map(
    envContents
      .split(/\r?\n/)
      .map((line) => line.trim())
      .filter((line) => line && !line.startsWith('#') && line.includes('='))
      .map((line) => {
        const separator = line.indexOf('=');
        return [line.slice(0, separator).trim(), line.slice(separator + 1).trim().replace(/^(['"])(.*)\1$/, '$2')];
      })
  );
  const apiKey = values.get('STEAM_API_KEY');
  const steamUserId = values.get('STEAM_USER_ID');
  if (!apiKey || !steamUserId) {
    throw new Error('.env must define both STEAM_API_KEY and STEAM_USER_ID.');
  }
  return { apiKey, steamUserId };
}

/**
 * @param {string} url
 * @param {Record<string, string>} params
 */
async function requestJson(url, params) {
  const requestUrl = new URL(url);
  for (const [key, value] of Object.entries(params)) requestUrl.searchParams.set(key, value);

  let response;
  try {
    response = await fetch(requestUrl, { signal: AbortSignal.timeout(15000) });
  } catch {
    throw new Error('Steam API request could not be completed.');
  }
  if (!response.ok) throw new Error(`Steam API request failed with HTTP ${response.status}.`);
  return response.json();
}

async function fetchSnapshot() {
  const { apiKey, steamUserId } = await readCredentials();
  const owned = await requestJson('https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/', {
    key: apiKey,
    steamid: steamUserId,
    include_appinfo: 'true',
    include_played_free_games: 'true',
    format: 'json'
  });
  const steamGames = owned?.response?.games;
  if (!Array.isArray(steamGames)) {
    throw new Error('Steam returned no owned-games list; the existing snapshot was left unchanged.');
  }

  /** @type {SnapshotGame[]} */
  const snapshot = [];
  for (const game of steamGames) {
    const hours = Math.round(((game.playtime_forever ?? 0) / 60) * 10) / 10;
    if (hours <= 0) continue;

    const item = /** @type {SnapshotGame} */ ({
      title: game.name ?? 'Unknown Game',
      hours,
      platform: 'Steam'
    });

    try {
      const stats = await requestJson('https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/', {
        key: apiKey,
        steamid: steamUserId,
        appid: game.appid,
        format: 'json'
      });
      const achievements = stats?.playerstats?.achievements;
      if (Array.isArray(achievements) && achievements.length > 0) {
        const unlocked = achievements.filter((achievement) => achievement.achieved === 1).length;
        item.achievements_unlocked = unlocked;
        item.achievements_total = achievements.length;
        item.achievements_completion = Math.round((unlocked / achievements.length) * 1000) / 10;
      }
    } catch (error) {
      console.warn(`Could not fetch achievements for app ${game.appid}; keeping playtime only.`);
    }
    snapshot.push(item);
  }

  snapshot.sort((first, second) => second.hours - first.hours);
  await writeFile(outputPath, `${JSON.stringify(snapshot, null, 2)}\n`, 'utf8');
  console.log(`Wrote ${snapshot.length} games to src/lib/data/games.json.`);
}

fetchSnapshot().catch((error) => {
  console.error(error instanceof Error ? error.message : 'Steam snapshot failed with an unknown error.');
  process.exitCode = 1;
});
