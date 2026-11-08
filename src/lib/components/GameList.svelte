<script lang="ts">
  import type { Game } from '#lib/data/games';

  let { games }: { games: Game[] } = $props();
  let activeFilter = $state('all');

  const filteredGames = $derived(
    games.filter((game) => {
      if (activeFilter === 'all') return true;
      if (activeFilter === '100') return (game.completion ?? game.achievements_completion) === 100;
      return game.platform === activeFilter;
    })
  );
  const completedGames = $derived(
    filteredGames.filter((game) => (game.completion ?? game.achievements_completion) === 100).length
  );
</script>

<div class="games-container">
  <div class="filter-buttons" aria-label="Filter games">
    <button class:active={activeFilter === 'all'} class="filter-btn" onclick={() => (activeFilter = 'all')}>All Games</button>
    <button class:active={activeFilter === '100'} class="filter-btn" onclick={() => (activeFilter = '100')}>100% Completion</button>
    <button class:active={activeFilter === 'PlayStation'} class="filter-btn" onclick={() => (activeFilter = 'PlayStation')}>PlayStation</button>
    <button class:active={activeFilter === 'Steam'} class="filter-btn" onclick={() => (activeFilter = 'Steam')}>Steam</button>
  </div>

  <div class="completion-stats">
    <div class="stat-card">
      <div class="stat-number">{filteredGames.length}</div>
      <div class="stat-label">Games in Filter</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">{completedGames}</div>
      <div class="stat-label">100% Completed</div>
    </div>
  </div>

  <div class="games-list">
    {#each filteredGames as game (game.title)}
      {@const percentage = game.completion ?? game.achievements_completion}
      <div class="game-card">
        {#if percentage !== undefined}
          <div class="game-status">{percentage}%</div>
        {/if}
        <div class="game-info">
          <h3>{game.title}</h3>
          <div class="game-details">
            <span class="game-hours">{game.hours} hours</span>
            {#if game.completionDate}
              <span class="game-date">{game.completionDate}</span>
            {/if}
            <span class="game-platform">{game.platform}</span>
          </div>
          {#if game.achievements_total !== undefined}
            <div class="game-achievements">
              <span class="achievements-info">{game.achievements_unlocked}/{game.achievements_total} achievements</span>
            </div>
          {:else if game.completion !== undefined}
            <div class="game-achievements">
              <span class="achievements-info">{game.completion}% Complete</span>
            </div>
          {/if}
        </div>
        {#if percentage === 100}
          <div class="game-badge">MASTERED</div>
        {/if}
      </div>
    {/each}
  </div>
</div>
