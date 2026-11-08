<script lang="ts">
  import { resolve } from '$app/paths';

  const projectsHref = resolve('/projects');
  const contactHref = resolve('/contact');
</script>

<svelte:head>
  <title>Home | My Portfolio</title>
</svelte:head>

<div class="hero">
  <div class="hero-content">
    <p class="hero-kicker">&gt; PORTFOLIO_v2.0 // LOADED</p>
    <h1 class="hero-title"><span class="highlight">Conner Brunner</span></h1>
    <p class="hero-subtitle">Computer science student building accessible web apps, creative systems, and games-inspired experiences.</p>
    <div class="hero-actions">
      <a href={projectsHref} class="btn btn-primary">See Projects</a>
      <a href={contactHref} class="btn btn-secondary">Contact Me</a>
    </div>
  </div>
</div>

<section class="about-section" id="about">
  <div class="about-content">
    <h2>// ABOUT</h2>
    <p>I’m a computer science student focused on building polished, useful things with a creative edge. I like turning ideas into websites, tools, and systems that feel intentional.</p>
    <p>Alongside CS, I study American Sign Language and stay involved with the ASL community at Kent State. That interest shows up in projects like my <a href="https://devpost.com/software/asl-translator-6shtz4">2025 hackathon project</a>.</p>
    <p>This portfolio pulls together the work I’ve built, the technologies I’m using, and the areas I’m still pushing forward in.</p>
  </div>
</section>
