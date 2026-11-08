# Conner Brunner Portfolio

A static SvelteKit portfolio with project, skills, contact, movie, and games pages. Steam game data is stored as a build-time JSON snapshot; the site does not make server-side API requests.

## Run locally

```sh
npm install
npm run dev
```

The local development site uses no base path. To refresh the games snapshot, add `STEAM_API_KEY` and `STEAM_USER_ID` to your ignored `.env` file and run:

```sh
npm run fetch:steam
```

The script writes the result to `src/lib/data/games.json`. The existing hardcoded game list is used if that snapshot file is absent.

Update the public email, GitHub, LinkedIn, and resume URLs in `src/lib/data/site.ts`; these are intentionally left as TODOs.

## Build

```sh
npm run build
```

The static site is generated in `build/`. To test the generated site locally, run `npm run preview`.

## Deploy

The GitHub Actions workflow builds and deploys on pushes to `main`. It derives the GitHub Pages base path from the repository name, and uses no base path for `ManOfNeptune27.github.io`.

For the first deployment, open **Settings > Pages** and set **Source** to **GitHub Actions**.
