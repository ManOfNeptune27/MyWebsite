<script lang="ts">
  import type { Project } from '#lib/data/projects';

  let { project }: { project: Project } = $props();
</script>

<article class="project-card card">
  <div class="project-card-inner">
    <h3>{project.title}</h3>
    <p>{project.summary}</p>
    <div class="tech-list">
      {#each project.stack as tech}
        <span class="tech-pill">{tech}</span>
      {/each}
    </div>
    <div class="project-links">
      {#each project.links as link}
        <a href={link.url} class="btn btn-primary project-button">{link.label}</a>
      {/each}
    </div>
  </div>
</article>
