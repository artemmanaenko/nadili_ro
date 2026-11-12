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
			title: 'Українське IT у Румунії',
			customCss: ['./src/styles/theme.css'],
			components: {
				ThemeProvider: './src/components/ThemeProvider.astro',
				ThemeSelect: './src/components/ThemeSelect.astro',
			},
			// Single locale: guides stay in the language they were written in.
			// The locale only sets the language of the interface strings.
			locales: {
				root: { label: 'Українська', lang: 'uk' },
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
					items: [{ autogenerate: { directory: 'guides' } }],
				},
			],
		}),
	],
});
