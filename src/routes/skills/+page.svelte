<script lang="ts">
  import PageHeader from '#lib/components/PageHeader.svelte';

  const skillGroups = [
    { title: 'Languages', items: ['Python', 'JavaScript', 'HTML', 'CSS'] },
    { title: 'Frameworks', items: ['Flask', 'Jinja2', 'APIs', 'Responsive UI'] },
    { title: 'Interests', items: ['Game Dev', 'Accessibility', 'ASL', 'Web Design'] }
  ];
</script>

<svelte:head>
  <title>Skills | My Portfolio</title>
</svelte:head>

<PageHeader title="Skills" description="Tools, languages, and areas I’m growing in" />

<section class="content-section">
  <div class="skill-grid">
    {#each skillGroups as group (group.title)}
      <div class="skill-card card">
        <h3>{group.title}</h3>
        <div class="tag-list">
          {#each group.items as item}
            <span class="tech-pill">{item}</span>
          {/each}
        </div>
      </div>
    {/each}
  </div>
</section>
