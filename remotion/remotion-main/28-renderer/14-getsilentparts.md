---
title: "getSilentParts()"
url: "https://www.remotion.dev/docs/renderer/get-silent-parts"
path: "/docs/renderer/get-silent-parts"
---

"---\nimage: /generated/articles-docs-renderer-get-silent-parts.png\nid: get-silent-parts\ntitle: getSilentParts()\ncrumb: '@remotion/renderer'\n---\n\n<YouTube minutes={2} href=\"https://www.youtube.com/watch?v=OHrvTMgiXWc\" thumb=\"https://i.ytimg.com/vi/OHrvTMgiXWc/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLC35vhR28KkxA7Bxr5XRqbIsMxe3g\" title=\"Remove silence from videos programmatically\" />\n\n# getSilentParts()<AvailableFrom v=\"4.0.18\" />\n\nGets the silent parts of a video or audio in Node.js. Useful for cutting out silence from a video.\n\n## Example\n\n```ts twoslash title=\"silent-parts.mjs\"\nimport {getSilentParts} from '@remotion/renderer';\n\nconst {silentParts, durationInSeconds} = await getSilentParts({\n  src: '/Users/john/Documents/bunny.mp4',\n  noiseThresholdInDecibels: -20,\n  minDurationInSeconds: 1,\n});\n\nconsole.log(silentParts); // [{startInSeconds: 0, endInSeconds: 1.5}]\n```\n\n:::info\nPass an absolute path to `getSilentParts()`. URLs are not supported.\n:::\n\n## Arguments\n\nAn object which takes the following properties:\n\n### `source`\n\n_string_\n\nA local video or audio file path.\n\n### `noiseThresholdInDecibels?`\n\n_number_\n\nThe threshold in decibels. If the audio is below this threshold, it is considered silent. The default is `-20`. Must be less than `30`.\n\n### `minDurationInSeconds?`\n\n_number_\n\nThe minimum duration of a silent part in seconds. The default is `1`.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\n### `binariesDirectory?`<AvailableFrom v=\"4.0.120\" />\n\n<Options id=\"binaries-directory\" />\n\n## Return Value\n\nThe return value is an object with the following properties:\n\n### `silentParts`\n\nAn array of objects with the following properties:\n\n- `startInSeconds`: The start time of the silent part in seconds.\n- `endInSeconds`: The end time of the silent part in seconds.\n\n### `audibleParts`\n\nThe inverse of the `silentParts` array.  \nAn array of objects with the following properties:\n\n- `startInSeconds`: The start time of the audible part in seconds.\n- `endInSeconds`: The end time of the audible part in seconds.\n\n### `durationInSeconds`\n\nThe time length of the media in seconds.\n\n## Compatibility\n\n<CompatibilityTable chrome={false} firefox={false} safari={false} nodejs={true} bun={true} serverlessFunctions={false} clientSideRendering={false} serverSideRendering={true} player={false} studio={false} />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/get-silent-parts.ts)\n- [`getVideoMetadata()`](/docs/renderer/get-video-metadata)\n"
[

Also available as a 2min video 
**Remove silence from videos programmatically**](https://www.youtube.com/watch?v=OHrvTMgiXWc)

Gets the silent parts of a video or audio in Node.js. Useful for cutting out silence from a video.

## Example[​](#example)

```

silent-parts.mjsimport {getSilentParts} from '@remotion/renderer';

const {silentParts, durationInSeconds} = await getSilentParts({
  src: '/Users/john/Documents/bunny.mp4',
  noiseThresholdInDecibels: -20,
  minDurationInSeconds: 1,
});

console.log(silentParts); // [{startInSeconds: 0, endInSeconds: 1.5}]Copy
```

](#example)](#example)
](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)