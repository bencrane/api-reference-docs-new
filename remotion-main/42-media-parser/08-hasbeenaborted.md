---
title: "hasBeenAborted()"
url: "https://www.remotion.dev/docs/media-parser/has-been-aborted"
path: "/docs/media-parser/has-been-aborted"
---

"---\nimage: /generated/articles-docs-media-parser-has-been-aborted.png\nid: has-been-aborted\ntitle: hasBeenAborted()\nslug: /media-parser/has-been-aborted\ncrumb: '@remotion/media-parser'\n---\n\n:::warning\n[We are phasing out Media Parser and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nPass an error to the `hasBeenAborted()` function to check if the error was thrown because you opted to abort the render.  \nIn this case, the error is intentional and you probably don't want to display it.\n\nCheck if a media file download has been aborted.\n\n```tsx twoslash title=\"Check if a download has been aborted\"\nimport {parseMedia, hasBeenAborted} from '@remotion/media-parser';\n\ntry {\n  await parseMedia({\n    src: 'https://www.w3schools.com/html/mov_bbb.mp4',\n  });\n} catch (e) {\n  if (hasBeenAborted(e)) {\n    console.log('Has been aborted by user / developer');\n  } else {\n    console.error('Download failed', e);\n  }\n}\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-parser/src/errors.ts)\n- [`parseMedia()`](/docs/media-parser/parse-media)\n"
]()]()
]()