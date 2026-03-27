---
title: "nodeReader"
url: "https://www.remotion.dev/docs/media-parser/node-reader"
path: "/docs/media-parser/node-reader"
---

"---\nimage: /generated/articles-docs-media-parser-node-reader.png\nid: node-reader\ntitle: nodeReader\nslug: /media-parser/node-reader\ncrumb: '@remotion/media-parser'\n---\n\n:::warning\n[We are phasing out Media Parser and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nA [reader](/docs/media-parser/readers) for `@remotion/media-parser` that reads from the local file system using Node.js `fs` module.  \nIt also works with Bun.\n\n## Example\n\n```tsx twoslash title=\"Reading a local file\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {nodeReader} from '@remotion/media-parser/node';\n\nconst result = await parseMedia({\n  src: '/Users/jonnyburger/Downloads/my-video.mp4',\n  fields: {\n    durationInSeconds: true,\n    dimensions: true,\n  },\n  reader: nodeReader,\n});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-parser/src/node.ts)\n- [Readers](/docs/media-parser/readers)\n"
]()]()
]()
- ]()