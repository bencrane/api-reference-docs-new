---
title: "mediaParserController()"
url: "https://www.remotion.dev/docs/media-parser/media-parser-controller"
path: "/docs/media-parser/media-parser-controller"
---

"---\nimage: /generated/articles-docs-media-parser-media-parser-controller.png\nid: media-parser-controller\ntitle: mediaParserController()\nslug: /media-parser/media-parser-controller\ncrumb: '@remotion/media-parser'\n---\n\n:::warning\n[We are phasing out Media Parser and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nPass `mediaParserController()` to [`controller`](/docs/media-parser/parse-media#controller) to steer the `parseMedia()` function.\n\nEach `mediaParserController` can only be attached to 1 [`parseMedia()`](/docs/media-parser/parse-media) call.\n\n```tsx twoslash title=\"Use mediaParserController()\"\nimport {mediaParserController, parseMedia} from '@remotion/media-parser';\n\nconst controller = mediaParserController();\n\nparseMedia({\n  src: 'https://www.w3schools.com/html/mov_bbb.mp4',\n  controller,\n});\n\n// Pause\ncontroller.pause();\n\n// Resume\ncontroller.resume();\n\n// Abort\ncontroller.abort();\n```\n\n## API\n\nThis function returns an object that can be passed to [`parseMedia({controller})`](/docs/media-parser/parse-media#controller).\n\nIt has the following methods:\n\n### `pause()`\n\nPauses the download and parsing process.\n\n### `resume()`\n\nResumes the download and parsing process.\n\n### `abort()`\n\nAborts the download and parsing process.\n\n### `seek(timeInSeconds: number)`\n\n[Seeks to the best keyframe](/docs/media-parser/seeking) that comes before the time you specified.\n\n### `getSeekingHints()`\n\nReturns a promise that resolves to the [seeking hints](/docs/media-parser/seeking-hints).\n\n### `addEventListener()`\n\nSee events below.\n\n### `removeEventListener()`\n\nSee events below.\n\n## Events\n\nYou can attach event listeners to the object returned by `mediaParserController()`.\n\n```tsx twoslash title=\"Use events\"\nimport {mediaParserController, parseMedia} from '@remotion/media-parser';\n\nconst controller = mediaParserController();\n\nconst onPause = () => {\n  console.log('Paused');\n};\n\nconst onResume = () => {\n  console.log('Resumed');\n};\n\ncontroller.addEventListener('pause', onPause);\ncontroller.addEventListener('resume', onResume);\n\n// Make sure to cleanup later:\ncontroller.removeEventListener('pause', onPause);\ncontroller.removeEventListener('resume', onResume);\n```\n\nIt also emits the following events:\n\n### `pause`\n\nEmitted when the download and parsing process is paused.\n\n### `resume`\n\nEmitted when the download and parsing process is resumed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-parser/src/media-parser-controller.ts)\n- [Pause, resume and abort parsing](/docs/media-parser/pause-resume-abort)\n- [`parseMedia()`](/docs/media-parser/parse-media)\n"
]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()