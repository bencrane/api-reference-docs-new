---
title: "preloadAudio()"
url: "https://www.remotion.dev/docs/preload/preload-audio"
path: "/docs/preload/preload-audio"
---

"---\nimage: /generated/articles-docs-preload-preload-audio.png\nid: preload-audio\nslug: preload-audio\ntitle: 'preloadAudio()'\ncrumb: '@remotion/preload'\n---\n\n_This function is part of the [`@remotion/preload`](/docs/preload) package._\n\nThis function preloads audio in the DOM so that when a audio tag is mounted, it can play immediately.\n\nWhile preload is not necessary for rendering, it can help with seamless playback in the [`<Player />`](/docs/player) and in the Studio.\n\nAn alternative to `preloadAudio()` is the [`prefetch()`](/docs/prefetch) API. See [`@remotion/preload` vs `prefetch()`](/docs/player/preloading#remotionpreload-vs-prefetch) to decide which one is better for your usecase.\n\n## Usage\n\n```tsx twoslash\nimport {preloadAudio} from '@remotion/preload';\n\nconst unpreload = preloadAudio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');\n\n// If you want to un-preload the audio later\nunpreload();\n```\n\n## How it works\n\n- On Firefox, it appends a `<link rel=\"preload\" as=\"audio\">` tag in the head element of the document.\n- In other browsers, it appends a `<audio preload=\"auto\">` tag in the body element of the document.\n\n## Handle redirects\n\nIf the audio URL redirects to another URL, preloading the original URL does not work.\n\nIf the URL you include is unknown, use [`resolveRedirect()`](/docs/preload/resolve-redirect) to programmatically obtain the final URL following potential redirects.\n\nIf the resource does not support CORS, `resolveRedirect()` will fail. If the resource redirects, and does not support CORS, you cannot preload the asset.\n\nThis snippet tries to preload a audio on a best-effort basis. If the redirect cannot be resolved, it tries to preload the original URL.\n\n```tsx twoslash\nimport {preloadAudio, resolveRedirect} from '@remotion/preload';\nimport {Html5Audio} from 'remotion';\n\n// This code gets executed immediately once the page loads\nlet urlToLoad = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3';\n\nresolveRedirect(urlToLoad)\n  .then((resolved) => {\n    // Was able to resolve a redirect, setting this as the audio to load\n    urlToLoad = resolved;\n  })\n  .catch((err) => {\n    // Was unable to resolve redirect e.g. due to no CORS support\n    console.log('Could not resolve redirect', err);\n  })\n  .finally(() => {\n    // In either case, we try to preload the original or resolved URL\n    preloadAudio(urlToLoad);\n  });\n\n// This code only executes once the component gets mounted\nconst MyComp: React.FC = () => {\n  // If the component did not mount immediately, this will be the resolved URL.\n\n  // If the component mounted immediately, this will be the original URL.\n  // In that case preloading is ineffective anyway.\n  return <Html5Audio src={urlToLoad} />;\n};\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)\n"

*This function is part of the [`@remotion/preload`](/docs/preload) package.*

This function preloads audio in the DOM so that when a audio tag is mounted, it can play immediately.

While preload is not necessary for rendering, it can help with seamless playback in the [`<Player />`](/docs/player) and in the Studio.

An alternative to `preloadAudio()` is the [`prefetch()`](/docs/prefetch) API. See [`@remotion/preload` vs `prefetch()`](/docs/player/preloading#remotionpreload-vs-prefetch) to decide which one is better for your usecase.

## Usage[​](#usage)

```
import {preloadAudio} from '@remotion/preload';

const unpreload = preloadAudio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');

// If you want to un-preload the audio later
unpreload();Copy
```

## How it works[​](#how-it-works)

- On Firefox, it appends a `<link rel="preload" as="audio">` tag in the head element of the document.

- In other browsers, it appends a `<audio preload="auto">` tag in the body element of the document.

## Handle redirects[​](#handle-redirects)

If the audio URL redirects to another URL, preloading the original URL does not work.

If the URL you include is unknown, use [`resolveRedirect()`](/docs/preload/resolve-redirect) to programmatically obtain the final URL following potential redirects.

If the resource does not support CORS, `resolveRedirect()` will fail. If the resource redirects, and does not support CORS, you cannot preload the asset.

This snippet tries to preload a audio on a best-effort basis. If the redirect cannot be resolved, it tries to preload the original URL.

```
import {preloadAudio, resolveRedirect} from '@remotion/preload';
import {Html5Audio} from 'remotion';

// This code gets executed immediately once the page loads
let urlToLoad = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3';

resolveRedirect(urlToLoad)
  .then((resolved) => {
    // Was able to resolve a redirect, setting this as the audio to load
    urlToLoad = resolved;
  })
  .catch((err) => {
    // Was unable to resolve redirect e.g. due to no CORS support
    console.log('Could not resolve redirect', err);
  })
  .finally(() => {
    // In either case, we try to preload the original or resolved URL
    preloadAudio(urlToLoad);
  });

// This code only executes once the component gets mounted
const MyComp: React.FC = () => {
  // If the component did not mount immediately, this will be the resolved URL.

  // If the component mounted immediately, this will be the original URL.
  // In that case preloading is ineffective anyway.
  return <Html5Audio src={urlToLoad} />;
};Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/preload-audio.ts)