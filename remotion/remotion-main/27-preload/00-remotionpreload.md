---
title: "@remotion/preload"
url: "https://www.remotion.dev/docs/preload/"
path: "/docs/preload/"
---

"---\nimage: /generated/articles-docs-preload-preload.png\nid: preload\nsidebar_label: Overview\ntitle: \"@remotion/preload\"\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {TableOfContents} from './table-of-contents';\n\nThis package provides functions for preloading assets. While preload is not necessary for rendering, it can help with seamless playback in the [`<Player />`](/docs/player) and in the Studio. Currently, three functions are implemented:\n\n<TableOfContents />\n\nAn alternative to `@remotion/preload` is the [`prefetch()`](/docs/prefetch) API. See [`@remotion/preload` vs `prefetch()`](/docs/player/preloading#remotionpreload-vs-prefetch) to decide which one is better for your usecase.\n\n## Installation\n\n<Installation pkg=\"@remotion/preload\"/>\n"

This package provides functions for preloading assets. While preload is not necessary for rendering, it can help with seamless playback in the [`<Player />`](/docs/player) and in the Studio. Currently, three functions are implemented:

[
**preloadVideo()**
Preload a video source](/docs/preload/preload-video)[
**preloadAudio()**
Preload an audio source](/docs/preload/preload-audio)[
**preloadFont()**
Preload a font](/docs/preload/preload-font)[
**preloadImage()**
Preload an image](/docs/preload/preload-image)[
**resolveRedirect()**
Get the definitive URL after all redirects](/docs/preload/preload-audio)

An alternative to `@remotion/preload` is the [`prefetch()`](/docs/prefetch) API. See [`@remotion/preload` vs `prefetch()`](/docs/player/preloading#remotionpreload-vs-prefetch) to decide which one is better for your usecase.

## Installation[​](#installation)

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/preloadCopy
```

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.](/cdn-cgi/l/email-protection)](/cdn-cgi/l/email-protection)
](/cdn-cgi/l/email-protection)