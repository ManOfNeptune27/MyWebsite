<script lang="ts">
  import PageHeader from '#lib/components/PageHeader.svelte';
  import ProjectCard from '#lib/components/ProjectCard.svelte';
  import { projects } from '#lib/data/projects';
</script>

<svelte:head>
  <title>Projects | My Portfolio</title>
</svelte:head>

<PageHeader title="Projects" description="Featured builds and selected work" />

<section class="content-section">
  <div class="project-grid">
    {#each projects as project (project.title)}
      <ProjectCard {project} />
    {/each}
  </div>
</section>
