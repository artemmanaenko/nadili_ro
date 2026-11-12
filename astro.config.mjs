// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// GitHub Pages project URL. When a custom domain is attached,
// set `site` to that domain and remove `base`.
export default defineConfig({
	site: 'https://artemmanaenko.github.io',
	base: '/ua_it_in_ro',
	integrations: [
		starlight({
			title: {
				uk: 'Українське IT у Румунії',
				en: 'Ukrainian IT in Romania',
			},
			defaultLocale: 'root',
			locales: {
				root: { label: 'Українська', lang: 'uk' },
				en: { label: 'English', lang: 'en' },
			},
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/artemmanaenko/ua_it_in_ro' },
			],
			editLink: {
				baseUrl: 'https://github.com/artemmanaenko/ua_it_in_ro/edit/main/',
			},
			sidebar: [
				{
					label: 'Інструкції',
					translations: { en: 'Guides' },
					items: [{ autogenerate: { directory: 'guides' } }],
				},
			],
		}),
	],
});
