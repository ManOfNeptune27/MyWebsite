<script lang="ts">
  import PageHeader from '#lib/components/PageHeader.svelte';
  import GameList from '#lib/components/GameList.svelte';
  import { games } from '#lib/data/games';
</script>

<svelte:head>
  <title>Games | My Portfolio</title>
</svelte:head>

<PageHeader title="My Games & Achievements" description="Games I've played and completed" />
<GameList {games} />
