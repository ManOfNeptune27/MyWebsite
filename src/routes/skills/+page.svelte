<script lang="ts">
  import PageHeader from '#lib/components/PageHeader.svelte';

  const skillGroups = [
    { title: 'Programming Languages', items: ['C++', 'C#', 'Python', 'Java', 'JavaScript', 'TypeScript', 'SQL'] },
    { title: 'Web Development', items: ['SvelteKit', 'Svelte', 'Bootstrap', 'HTML', 'CSS'] },
    { title: 'Data & Storage', items: ['MySQL', 'Turso (libSQL)', 'Cloudflare R2'] },
    { title: 'Development Tools', items: ['Git', 'SVN', 'Linux', 'Bash', 'Visual Studio Code', 'Qt Creator'] },
    { title: 'Security & CTF', items: ['Python cryptography scripts', 'zsteg', 'gobuster'] },
    { title: 'Platforms', items: ['Unity', 'Vercel'] }
  ];
</script>

<svelte:head>
  <title>Skills | My Portfolio</title>
</svelte:head>

<PageHeader title="Skills" description="Technical skills demonstrated across my projects, research, and CTF competitions" />

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
