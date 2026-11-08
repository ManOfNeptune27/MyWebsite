export interface SiteLink {
  label: string;
  url: string;
  download?: string;
}

export interface SiteConfig {
  contactEmail: string;
  contactLinks: SiteLink[];
}

export const site: SiteConfig = {
  contactEmail: 'connerbrunner@gmail.com',
  contactLinks: [
    { label: 'GitHub', url: 'https://github.com/ManOfNeptune27' },
    { label: 'LinkedIn', url: 'https://www.linkedin.com/in/conner-brunner/' },
    { label: 'Resume', url: '/resume.docx', download: 'ConnerBrunner.docx' }
  ]
};
