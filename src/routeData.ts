import { defineRouteMiddleware } from '@astrojs/starlight/route-data';

// Guides are read one at a time: no left-hand list of guides. Navigation
// within a page lives in the right-hand table of contents.
export const onRequest = defineRouteMiddleware((context) => {
	context.locals.starlightRoute.hasSidebar = false;
});
