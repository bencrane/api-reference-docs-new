---
title: "resolveRedirect()"
url: "https://www.remotion.dev/docs/preload/resolve-redirect"
path: "/docs/preload/resolve-redirect"
---

"---\nid: resolve-redirect\ntitle: resolveRedirect()\ncrumb: '@remotion/player'\n---\n\nFollows the redirects of a URL (most commonly a remote video or audio) until the final URL is resolved and returns that.\n\nIf the resource does not support CORS, the function will throw. **If the resource redirects, and does not support CORS, you cannot preload the asset.**\n\n```tsx twoslash\nimport {resolveRedirect} from '@remotion/preload';\n\nresolveRedirect('https://player.vimeo.com/external/291648067.hd.mp4?s=94998971682c6a3267e4cbd19d16a7b6c720f345&profile_id=175&oauth2_token_id=57447761')\n  .then((src) => {\n    console.log(src); // \"https://vod-progressive.akamaized.net/...\"\n  })\n  .catch((err) => {\n    console.log('Could not resolve redirect', err);\n  });\n```\n\n## Example: Resolve and preload a video\n\nThis snippet tries to preload a video on a best-effort basis. If the redirect cannot be resolved, it tries to preload the original URL.\n\n```tsx twoslash\nimport {preloadVideo, resolveRedirect} from '@remotion/preload';\nimport {OffthreadVideo} from 'remotion';\n\n// This code gets executed immediately once the page loads\nlet urlToLoad = 'https://player.vimeo.com/external/291648067.hd.mp4?s=94998971682c6a3267e4cbd19d16a7b6c720f345&profile_id=175&oauth2_token_id=57447761';\n\nresolveRedirect(urlToLoad)\n  .then((resolved) => {\n    // Was able to resolve a redirect, setting this as the video to load\n    urlToLoad = resolved;\n  })\n  .catch((err) => {\n    // Was unable to resolve redirect e.g. due to no CORS support\n    console.log('Could not resolve redirect', err);\n  })\n  .finally(() => {\n    // In either case, we try to preload the original or resolved URL\n    preloadVideo(urlToLoad);\n  });\n\n// This code only executes once the component gets mounted\nconst MyComp: React.FC = () => {\n  // If the component did not mount immediately, this will be the resolved URL.\n\n  // If the component mounted immediately, this will be the original URL.\n  // In that case preloading is ineffective anyway.\n  return <OffthreadVideo src={urlToLoad}></OffthreadVideo>;\n};\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/resolve-redirect.ts)\n- [Installing `@remotion/preload`](/docs/preload)\n- [preloadAudio()](/docs/preload/preload-audio)\n- [preloadVideo()](/docs/preload/preload-video)\n"

Follows the redirects of a URL (most commonly a remote video or audio) until the final URL is resolved and returns that.

If the resource does not support CORS, the function will throw. **If the resource redirects, and does not support CORS, you cannot preload the asset.**

```
import {resolveRedirect} from '@remotion/preload';

resolveRedirect('https://player.vimeo.com/external/291648067.hd.mp4?s=94998971682c6a3267e4cbd19d16a7b6c720f345&profile_id=175&oauth2_token_id=57447761')
  .then((src) => {
    console.log(src); // "https://vod-progressive.akamaized.net/..."
  })
  .catch((err) => {
    console.log('Could not resolve redirect', err);
  });Copy
```

## Example: Resolve and preload a video[​](#example-resolve-and-preload-a-video)

This snippet tries to preload a video on a best-effort basis. If the redirect cannot be resolved, it tries to preload the original URL.

```
import {preloadVideo, resolveRedirect} from '@remotion/preload';
import {OffthreadVideo} from 'remotion';

// This code gets executed immediately once the page loads
let urlToLoad = 'https://player.vimeo.com/external/291648067.hd.mp4?s=94998971682c6a3267e4cbd19d16a7b6c720f345&profile_id=175&oauth2_token_id=57447761';

resolveRedirect(urlToLoad)
  .then((resolved) => {
    // Was able to resolve a redirect, setting this as the video to load
    urlToLoad = resolved;
  })
  .catch((err) => {
    // Was unable to resolve redirect e.g. due to no CORS support
    console.log('Could not resolve redirect', err);
  })
  .finally(() => {
    // In either case, we try to preload the original or resolved URL
    preloadVideo(urlToLoad);
  });

// This code only executes once the component gets mounted
const MyComp: React.FC = () => {
  // If the component did not mount immediately, this will be the resolved URL.

  // If the component mounted immediately, this will be the original URL.
  // In that case preloading is ineffective anyway.
  return <OffthreadVideo src={urlToLoad}></OffthreadVideo>;
};Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/preload/src/resolve-redirect.ts)

- [Installing `@remotion/preload`](/docs/preload)

- [preloadAudio()](/docs/preload/preload-audio)

- [preloadVideo()](/docs/preload/preload-video)
](/docs/preload/preload-video)](/docs/preload/preload-video)
](/docs/preload/preload-video)
- ](/docs/preload/preload-video)