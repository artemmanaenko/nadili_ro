// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { repositoryName, repositoryUrl } from './repository.mjs';

// GitHub Pages project URL. When a custom domain is attached,
// set `site` to that domain and remove `base`.
export default defineConfig({
	site: 'https://artemmanaenko.github.io',
	base: `/${repositoryName}`,
	integrations: [
		starlight({
			title: 'Nadili',
			logo: { src: './src/assets/logo.svg', replacesTitle: true },
			customCss: ['./src/styles/theme.css'],
			// Right-hand navigation: sections, with subsections shown for the current one.
			tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
			routeMiddleware: './src/routeData.ts',
			// Guides stand alone: no previous/next links between them.
			pagination: false,
			components: {
				Head: './src/components/Head.astro',
				Header: './src/components/HomeHeader.astro',
				Footer: './src/components/SiteFooter.astro',
				ThemeProvider: './src/components/ThemeProvider.astro',
				ThemeSelect: './src/components/ThemeSelect.astro',
				PageTitle: './src/components/PageTitle.astro',
			},
			// Single locale: guides stay in the language they were written in.
			// The locale only sets the language of the interface strings.
			locales: {
				root: { label: 'Українська', lang: 'uk' },
			},
			editLink: {
				baseUrl: `${repositoryUrl}/edit/main/`,
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
