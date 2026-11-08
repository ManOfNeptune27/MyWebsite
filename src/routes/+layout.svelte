<script lang="ts">
  import { onMount } from 'svelte';
  import type { Snippet } from 'svelte';
  import { resolve } from '$app/paths';
  import { page } from '$app/state';

  let { children }: { children: Snippet } = $props();
  const rootHref = resolve('/');
  const navItems = [
    { label: 'Home', href: rootHref, route: '/' },
    { label: 'Projects', href: resolve('/projects'), route: '/projects' },
    { label: 'Skills', href: resolve('/skills'), route: '/skills' },
    { label: 'Contact', href: resolve('/contact'), route: '/contact' }
  ];

  onMount(() => {
    const updateActiveNavLink = () => {
      const currentPath = window.location.pathname;
      if (currentPath === rootHref) {
        const scrollPosition = window.scrollY + 160;
        const sections = document.querySelectorAll<HTMLElement>('main section[id]');
        let activeHash = '';

        sections.forEach((section) => {
          if (section.offsetTop <= scrollPosition) activeHash = `#${section.id}`;
        });

        document.querySelectorAll<HTMLAnchorElement>('.nav-links a').forEach((link) => {
          link.classList.toggle('active', activeHash ? link.hash === activeHash : link.href === window.location.origin + rootHref);
        });
        return;
      }

      document.querySelectorAll<HTMLAnchorElement>('.nav-links a').forEach((link) => {
        link.classList.toggle('active', link.pathname === currentPath);
      });
    };

    const handleAnchorClick = (event: MouseEvent) => {
      const target = event.target;
      if (!(target instanceof Element)) return;
      const anchor = target.closest<HTMLAnchorElement>('a[href*="#"]');
      if (!anchor) return;

      const url = new URL(anchor.href);
      if (url.origin !== window.location.origin) return;
      const isHomeAnchor = url.pathname === rootHref;
      const isHomePage = window.location.pathname === rootHref;
      if (isHomeAnchor && !isHomePage) return;

      const section = url.hash ? document.querySelector(url.hash) : null;
      if (!section) return;

      event.preventDefault();
      section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    const observer =
      typeof IntersectionObserver === 'undefined'
        ? undefined
        : new IntersectionObserver(
            (entries) => {
              entries.forEach((entry) => {
                if (entry.isIntersecting) {
                  (entry.target as HTMLElement).style.animationPlayState = 'running';
                }
              });
            },
            { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
          );

    document.querySelectorAll<HTMLElement>('.favorites-section, .card').forEach((element) => {
      element.style.animation = 'fadeIn 0.5s ease forwards';
      element.style.animationPlayState = 'paused';
      observer?.observe(element);
    });

    window.addEventListener('scroll', updateActiveNavLink);
    document.addEventListener('click', handleAnchorClick);
    updateActiveNavLink();

    return () => {
      window.removeEventListener('scroll', updateActiveNavLink);
      document.removeEventListener('click', handleAnchorClick);
      observer?.disconnect();
    };
  });
</script>

<svelte:head>
  <meta name="description" content="Conner Brunner's portfolio" />
  <link rel="stylesheet" href={`${rootHref}css/style.css`} />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" />
</svelte:head>

<nav class="navbar">
  <div class="nav-container">
    <div class="logo">
      <a href={rootHref}>Conner Brunner</a>
    </div>
    <ul class="nav-links">
      {#each navItems as item}
        <li><a href={item.href} class:active={page.route.id === item.route}>{item.label}</a></li>
      {/each}
    </ul>
  </div>
</nav>

<main class="main-container">
  {@render children()}
</main>

<footer class="footer">
  <p>&copy; 2026 Conner Brunner // Built with SvelteKit &amp; Pure Grit</p>
</footer>
