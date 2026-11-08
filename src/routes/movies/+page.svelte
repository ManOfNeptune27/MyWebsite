<script lang="ts">
  import PageHeader from '#lib/components/PageHeader.svelte';
  import { movieFavorites } from '#lib/data/favorites';
</script>

<svelte:head>
  <title>Movies | My Portfolio</title>
</svelte:head>

<PageHeader title="Movies" description="My favorite movies with ratings and reviews" />

<div class="favorites-container">
  <div class="items-grid">
    {#each movieFavorites as item (item.id)}
      <div class="favorite-item" data-id={item.id}>
        <div class="item-header">
          <h3>{item.name}</h3>
          <div class="rating">
            <span class="stars">{'⭐'.repeat(Math.floor(item.rating))}</span>
            <span class="rating-value">{item.rating}/10</span>
          </div>
        </div>
        <p>{item.details}</p>
      </div>
    {/each}
  </div>
</div>
