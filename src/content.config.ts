import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: ({ image }) => z.object({
				contributors: z.array(z.string().trim().min(1)).optional(),
				socialImage: z.object({ src: image(), alt: z.string() }).optional(),
			}),
		}),
	}),
};
