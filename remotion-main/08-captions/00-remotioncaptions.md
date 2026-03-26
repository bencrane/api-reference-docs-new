---
title: "@remotion/captions"
url: "https://www.remotion.dev/docs/captions/api"
path: "/docs/captions/api"
---

"---\nimage: /generated/articles-docs-captions-api.png\ntitle: '@remotion/captions'\ncrumb: 'Subtitle videos'\n---\n\n_Available from v4.0.216_\n\nThe `@remotion/captions` package provides utilities for dealing with subtitles.\n\nAt the centre of this caption is the [`Caption`](/docs/captions/caption) type, which defines a standard shape for captions from different sources.\n\nCaptions generated from [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp) [can be converted](/docs/install-whisper-cpp/to-captions) into the `Caption` type.\n\nimport {TableOfContents} from './TableOfContents';\n\n<Installation pkg=\"@remotion/captions\" />\n\n## APIs\n\n<TableOfContents />\n\n## License\n\nMIT\n"

*Available from v4.0.216*

The `@remotion/captions` package provides utilities for dealing with subtitles.

At the centre of this caption is the [`Caption`](/docs/captions/caption) type, which defines a standard shape for captions from different sources.

Captions generated from [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp) [can be converted](/docs/install-whisper-cpp/to-captions) into the `Caption` type.

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/captionsCopy
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
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

## APIs[​](#apis)

[
**Caption**
An object shape for captions](/docs/captions/caption)[
**parseSrt()**
Parse a .srt file into a `Caption` array](/docs/captions/parse-srt)[
**serializeSrt()**
Serialize a .srt file into a `Caption` array](/docs/captions/serialize-srt)[
**createTikTokStyleCaptions()**
Structure the captions for TikTok-style display](/docs/captions/create-tiktok-style-captions)

## License[​](#license)

MIT](#license)](#license)
](#license)
- ](#license)