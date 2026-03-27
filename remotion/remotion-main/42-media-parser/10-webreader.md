---
title: "webReader"
url: "https://www.remotion.dev/docs/media-parser/web-reader"
path: "/docs/media-parser/web-reader"
---

"---\nimage: /generated/articles-docs-media-parser-web-reader.png\nid: web-reader\ntitle: webReader\nslug: /media-parser/web-reader\ncrumb: '@remotion/media-parser'\n---\n\n:::warning\n[We are phasing out Media Parser and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nA [reader](/docs/media-parser/readers) for [`@remotion/media-parser`](/docs/media-parser) that reads either from a URL or from a [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File).\n\nIt is the default reader, and therefore does not have to be specified.\n\n## Example\n\n```tsx twoslash title=\"Reading from any source\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {webReader} from '@remotion/media-parser/web';\n\nconst result = await parseMedia({\n  // Or a `File`\n  src: 'https://remotion.media/video.mp4',\n  fields: {\n    durationInSeconds: true,\n    dimensions: true,\n  },\n  reader: webReader,\n});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-parser/src/web.ts)\n- [`parseMedia()`](/docs/media-parser/parse-media)\n"
]()]()
]()
- ]()