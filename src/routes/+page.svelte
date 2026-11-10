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
    <p class="hero-subtitle">I enjoy building software, creating fun, useful tools and websites, and helping others.</p>
    <div class="hero-actions">
      <a href={projectsHref} class="btn btn-primary">See Projects</a>
      <a href={contactHref} class="btn btn-secondary">Contact Me</a>
    </div>
  </div>
</div>

<section class="about-section" id="about">
  <div class="about-content">
    <h2>// ABOUT</h2>
    <p>I graduated from Kent State University with a Bachelor of Science in Computer Science in May 2026, with a minor in American Sign Language. I’m currently pursuing a master’s degree in Computer Science.</p>
    <p>I enjoy building practical software, from a full-stack ASL dictionary for teachers to tools that explore software dependencies. I also write Python scripts for cryptography challenges and collaborate on eye-tracking research.</p>
    <p>As a HacKSU organizer and lesson coordinator and an academic tutor, I help plan technical learning events and explain computer science concepts to others.</p>
    <p>Explore my <a class="asl-hackathon-link" href="https://devpost.com/software/asl-translator-6shtz4">ASL hackathon project</a> and selected work, or contact me about junior developer, solutions engineer, and internship opportunities.</p>
  </div>
</section>

<section class="achievement-highlights" aria-labelledby="achievement-title">
  <h2 id="achievement-title">// ACHIEVEMENTS &amp; HIGHLIGHTS</h2>
  <ul class="achievement-list">
    <li><strong>1st place</strong> — <a href="https://devpost.com/software/asl-translator-6shtz4">Kent Hack Enough ASL Translate</a></li>
    <li><strong>2× 1st place</strong> — Kent Hack It CTF (2025 &amp; 2026)</li>
    <li><strong>Organizer &amp; lesson coordinator</strong> — HacKSU</li>
    <li><strong>Research contributor</strong> — eye-tracking tools for analyzing how programmers read code</li>
    <li><strong>ASL Department Dictionary</strong> — <a href="https://www.asldepartmentdictionary.org/">live website</a></li>
    <li><a href="https://devpost.com/ManOfNeptune27">View all hackathon projects on Devpost</a></li>
  </ul>
</section>
