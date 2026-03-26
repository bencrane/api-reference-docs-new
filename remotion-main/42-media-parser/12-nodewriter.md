---
title: "nodeWriter"
url: "https://www.remotion.dev/docs/media-parser/node-writer"
path: "/docs/media-parser/node-writer"
---

"---\nimage: /generated/articles-docs-media-parser-node-writer.png\nid: node-writer\ntitle: nodeWriter\nslug: /media-parser/node-writer\ncrumb: '@remotion/media-parser'\n---\n\n:::warning\n[We are phasing out Media Parser and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n:::warning\n**Unstable API**: The writer interface is experimental. The API may change in the future.\n:::\n\nA writer for `@remotion/media-parser` that writes to the local file system using Node.js `fs` module.\n\nCan be used for [`downloadAndParseMedia()`](/docs/media-parser/download-and-parse-media) and [`convertMedia()`](/docs/webcodecs/convert-media) (for remuxing only, since Node.js does not implement WebCodecs).\n\n## Example\n\n```tsx twoslash title=\"Writing to a local file\"\nimport {downloadAndParseMedia} from '@remotion/media-parser';\nimport {nodeWriter} from '@remotion/media-parser/node-writer';\n\nawait downloadAndParseMedia({\n  src: 'https://www.w3schools.com/html/mov_bbb.mp4',\n  writer: nodeWriter('output.mp4'),\n});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-parser/src/writers/node.ts)\n"
]()]()
]()
- ]()