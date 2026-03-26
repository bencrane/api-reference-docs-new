---
title: "universalReader"
url: "https://www.remotion.dev/docs/media-parser/universal-reader"
path: "/docs/media-parser/universal-reader"
---

"---\nimage: /generated/articles-docs-media-parser-universal-reader.png\nid: universal-reader\ntitle: universalReader\nslug: /media-parser/universal-reader\ncrumb: '@remotion/media-parser'\n---\n\n:::warning\n[We are phasing out Media Parser and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nA [reader](/docs/media-parser/readers) for [`@remotion/media-parser`](/docs/media-parser) that reads either from a URL, from a [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File) or from a local file path.\n\nIt is the combination of [`nodeReader`](/docs/media-parser/node-reader) and [`webReader`](/docs/media-parser/web-reader).\n\nBecause of the dependency on the `fs` module, it cannot be used in the browser.\n\n## Example\n\n```tsx twoslash title=\"Reading from any source\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {universalReader} from '@remotion/media-parser/universal';\n\nconst result = await parseMedia({\n  // Or a File, or a URL\n  src: '/Users/jonnyburger/Downloads/my-video.mp4',\n  fields: {\n    durationInSeconds: true,\n    dimensions: true,\n  },\n  reader: universalReader,\n});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-parser/src/universal.ts)\n- [`parseMedia()`](/docs/media-parser/parse-media)\n"
]()]()
]()
- ]()