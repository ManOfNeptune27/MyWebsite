<script lang="ts">
  import PageHeader from '#lib/components/PageHeader.svelte';
  import { site } from '#lib/data/site';
</script>

<svelte:head>
  <title>Contact | My Portfolio</title>
</svelte:head>

<PageHeader title="Contact" description="Ways to reach me and where to find my work" />

<section class="content-section">
  <div class="contact-panel card">
    <p>I’m open to internships, collaboration, and projects that need a clean front end.</p>
    {#if site.contactEmail}
      <p class="contact-email">Email: <a href={`mailto:${site.contactEmail}`}>{site.contactEmail}</a></p>
    {:else}
      <p class="todo-note">TODO: Add a public contact email in src/lib/data/site.ts.</p>
    {/if}
    <div class="contact-links">
      {#each site.contactLinks as link}
        {#if link.url}
          <a href={link.url} class="btn btn-primary">{link.label}</a>
        {:else}
          <span class="btn btn-secondary is-muted">{link.label} soon</span>
        {/if}
      {/each}
    </div>
  </div>
</section>
