export interface ProjectLink {
  label: string;
  url: string;
}

export interface Project {
  title: string;
  summary: string;
  stack: string[];
  links: ProjectLink[];
}

export const projects: Project[] = [
  {
    title: 'ASL Department Dictionary',
    summary: 'Personal full-stack project for the ASL department. Stores signs in a database and displays them as GIFs, with multi-teacher cookie-based authentication, admin tools for managing signs and storage, and presigned-URL uploads to Cloudflare R2. Deployed to Vercel.',
    stack: ['SvelteKit', 'Svelte', 'TypeScript', 'Bootstrap', 'Turso (libSQL)', 'Cloudflare R2'],
    links: [
      { label: 'GitHub', url: 'https://github.com/ManOfNeptune27/ASLDepartmentDictionary' },
      { label: 'Live Site', url: 'https://asldepartmentdictionary.org' }
    ]
  },
  {
    title: 'ASL Translate — First-Place Hackathon Project',
    summary: 'Built a web app that translates American Sign Language into English, using a five-parameter filter system and database-backed GIF results. Won first place at Kent Hack Enough.',
    stack: ['Svelte', 'JavaScript', 'HTML', 'CSS'],
    links: [
      { label: 'GitHub', url: 'https://github.com/HappyCoderHackathons/aslTranslate' },
      { label: 'Devpost', url: 'https://devpost.com/software/asl-translator-6shtz4' }
    ]
  },
  {
    title: 'Dependency Domino',
    summary: 'Software supply-chain visualization tool that imports dependency lockfiles, explores package relationships, simulates hypothetical compromise impact, and checks known advisories through OSV.dev.',
    stack: ['Svelte', 'TypeScript', 'JavaScript'],
    links: [{ label: 'GitHub', url: 'https://github.com/HappyCoderHackathons/Dependency-Domino' }]
  },
  {
    title: 'iTrace-Toolkit Research',
    summary: 'Collaborated with a research team to implement saccade detection for eye-tracking data, helping researchers analyze how programmers read code.',
    stack: ['C++', 'SQL', 'Qt Creator'],
    links: []
  },
  {
    title: 'Kent Hack It CTF — Two-Time First-Place Winner',
    summary: 'Won first place with a team in 2025 and 2026. Wrote Python scripts to brute-force cryptographic ciphers and solved steganography and web-based challenges using command-line tools.',
    stack: ['Python', 'zsteg', 'gobuster'],
    links: []
  },
  {
    title: 'FindMe',
    summary: 'A local OSINT tool available as a terminal CLI or Flask GUI.',
    stack: ['Python', 'Flask', 'Playwright'],
    links: [{ label: 'GitHub', url: 'https://github.com/UnDefinedCS/findme' }]
  },
  {
    title: 'The Cattery',
    summary: 'A Unity game made by Team A about creating cats by baking them from dough.',
    stack: ['C#'],
    links: [{ label: 'GitHub', url: 'https://github.com/knotpil/GDP-TeamA' }]
  }
];
