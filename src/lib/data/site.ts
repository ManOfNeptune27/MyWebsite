export interface SiteLink {
  label: string;
  url: string;
}

export interface SiteConfig {
  contactEmail: string;
  contactLinks: SiteLink[];
}

export const site: SiteConfig = {
  contactEmail: '', // TODO: Add a public contact email address.
  contactLinks: [
    { label: 'GitHub', url: '' }, // TODO: Add the GitHub profile URL.
    { label: 'LinkedIn', url: '' }, // TODO: Add the LinkedIn profile URL.
    { label: 'Resume', url: '' } // TODO: Add a public resume URL.
  ]
};
