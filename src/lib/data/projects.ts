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
  { title: 'ASL Dictionary Website', summary: 'A website built with Svelte, TypeScript, HTML, and JavaScript to help people learn ASL. It won first place at the 2024 Kent State Hackathon.', stack: ['Svelte', 'TypeScript', 'HTML', 'JavaScript'], links: [{ label: 'GitHub', url: 'https://github.com/ManOfNeptune27/asl-dictionary' }] },
  { title: 'ASL Department Dictionary', summary: "A school project for organizing and storing teachers' ASL vocabulary in one consolidated dictionary for day-to-day use.", stack: ['Web App', 'Dictionary'], links: [{ label: 'GitHub', url: 'https://github.com/ManOfNeptune27/ASLDepartmentDictionary' }] },
  { title: 'The Cattery', summary: 'A Unity game made by Team A about creating cats by baking them from dough.', stack: ['C#'], links: [{ label: 'GitHub', url: 'https://github.com/knotpil/GDP-TeamA' }] }
];
