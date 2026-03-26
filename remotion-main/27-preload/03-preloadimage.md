---
title: "preloadImage()"
url: "https://www.remotion.dev/docs/preload/preload-image"
path: "/docs/preload/preload-image"
---

"---\nimage: /generated/articles-docs-preload-preload-image.png\nid: preload-image\nslug: preload-image\ntitle: \"preloadImage()\"\ncrumb: \"@remotion/preload\"\n---\n\n_This function is part of the [`@remotion/preload`](/docs/preload) package._\n\nThis function preloads an image so that when an [`<Img>`](/docs/img) tag is mounted, it can display immediately.\n\nWhile preload is not necessary for rendering, it can help with seamless playback in the [`<Player />`](/docs/player) and in the Studio.\n\nAn alternative to `preloadImage()` is the [`prefetch()`](/docs/prefetch) API. See [`@remotion/preload` vs `prefetch()`](/docs/player/preloading#remotionpreload-vs-prefetch) to decide which one is better for your usecase.\n\n## Usage\n\n```tsx twoslash\nimport { preloadImage } from \"@remotion/preload\";\n\nconst unpreload = preloadImage(\n  \"https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80\"\n);\n\n// If you want to un-preload the image later\nunpreload();\n```\n\n## How it works\n\nA `<link rel=\"preload\" as=\"image\">` tag gets added to the head element of the document.\n\n## Handle redirects\n\nIf the image URL redirects to another URL, preloading the original URL does not work.\n\nIf the URL you include is unknown, use [`resolveRedirect()`](/docs/preload/resolve-redirect) to programmatically obtain the final URL following potential redirects.\n\nIf the resource does not support CORS, `resolveRedirect()` will fail. If the resource redirects, and does not support CORS, you cannot preload the asset.\n\nThis snippet tries to preload a image on a best-effort basis. If the redirect cannot be resolved, it tries to preload the original URL.\n\n```tsx twoslash\nimport { preloadImage, resolveRedirect } from \"@remotion/preload\";\nimport { Img } from \"remotion\";\n\n// This code gets executed immediately once the page loads\nlet urlToLoad =\n  \"https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80\";\n\nresolveRedirect(urlToLoad)\n  .then((resolved) => {\n    // Was able to resolve a redirect, setting this as the image to load\n    urlToLoad = resolved;\n  })\n  .catch((err) => {\n    // Was unable to resolve redirect e.g. due to no CORS support\n    console.log(\"Could not resolve redirect\", err);\n  })\n  .finally(() => {\n    // In either case, we try to preload the original or resolved URL\n    preloadImage(urlToLoad);\n  });\n\n// This code only executes once the component gets mounted\nconst MyComp: React.FC = () => {\n  // If the component did not mount immediately, this will be the resolved URL.\n\n  // If the component mounted immediately, this will be the original URL.\n  // In that case preloading is ineffective anyway.\n  return <Img src={urlToLoad}></Img>;\n};\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)\n"

*This function is part of the [`@remotion/preload`](/docs/preload) package.*

This function preloads an image so that when an [`<Img>`](/docs/img) tag is mounted, it can display immediately.

While preload is not necessary for rendering, it can help with seamless playback in the [`<Player />`](/docs/player) and in the Studio.

An alternative to `preloadImage()` is the [`prefetch()`](/docs/prefetch) API. See [`@remotion/preload` vs `prefetch()`](/docs/player/preloading#remotionpreload-vs-prefetch) to decide which one is better for your usecase.

## Usage[​](#usage)

```
import { preloadImage } from "@remotion/preload";

const unpreload = preloadImage(
  "https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"
);

// If you want to un-preload the image later
unpreload();Copy
```

## How it works[​](#how-it-works)

A `<link rel="preload" as="image">` tag gets added to the head element of the document.

## Handle redirects[​](#handle-redirects)

If the image URL redirects to another URL, preloading the original URL does not work.

If the URL you include is unknown, use [`resolveRedirect()`](/docs/preload/resolve-redirect) to programmatically obtain the final URL following potential redirects.

If the resource does not support CORS, `resolveRedirect()` will fail. If the resource redirects, and does not support CORS, you cannot preload the asset.

This snippet tries to preload a image on a best-effort basis. If the redirect cannot be resolved, it tries to preload the original URL.

```
import { preloadImage, resolveRedirect } from "@remotion/preload";
import { Img } from "remotion";

// This code gets executed immediately once the page loads
let urlToLoad =
  "https://images.unsplash.com/photo-1561336313-0bd5e0b27ec8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80";

resolveRedirect(urlToLoad)
  .then((resolved) => {
    // Was able to resolve a redirect, setting this as the image to load
    urlToLoad = resolved;
  })
  .catch((err) => {
    // Was unable to resolve redirect e.g. due to no CORS support
    console.log("Could not resolve redirect", err);
  })
  .finally(() => {
    // In either case, we try to preload the original or resolved URL
    preloadImage(urlToLoad);
  });

// This code only executes once the component gets mounted
const MyComp: React.FC = () => {
  // If the component did not mount immediately, this will be the resolved URL.

  // If the component mounted immediately, this will be the original URL.
  // In that case preloading is ineffective anyway.
  return <Img src={urlToLoad}></Img>;
};Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-image.ts)