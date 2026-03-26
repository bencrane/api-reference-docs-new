---
title: "webcodecsController()"
url: "https://www.remotion.dev/docs/webcodecs/webcodecs-controller"
path: "/docs/webcodecs/webcodecs-controller"
---

"---\nimage: /generated/articles-docs-webcodecs-webcodecs-controller.png\nid: webcodecs-controller\ntitle: webcodecsController()\nslug: /webcodecs/webcodecs-controller\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nPass `webcodecsController()` to [`controller`](/docs/webcodecs/convert-media#controller) to steer the `convertMedia()` function.\n\n```tsx twoslash title=\"Use webcodecsController()\"\nimport {webcodecsController, convertMedia} from '@remotion/webcodecs';\n\nconst controller = webcodecsController();\n\nconvertMedia({\n  src: 'https://www.w3schools.com/html/mov_bbb.mp4',\n  container: 'webm',\n  controller,\n});\n\n// Pause\ncontroller.pause();\n\n// Resume\ncontroller.resume();\n\n// Abort\ncontroller.abort();\n```\n\n## API\n\nThis function returns an object that can be passed to [`convertMedia({controller})`](/docs/webcodecs/convert-media#controller).\n\nIt has the following methods:\n\n### `pause()`\n\nPauses the conversion.\n\n### `resume()`\n\nResumes the conversion.\n\n### `abort()`\n\nAborts the conversion.\n\n### `addEventListener()`\n\nSee events below.\n\n### `removeEventListener()`\n\nSee events below.\n\n## Events\n\nYou can attach event listeners to the `webcodecsController` object.\n\n```tsx twoslash title=\"Use events\"\nimport {webcodecsController, convertMedia} from '@remotion/webcodecs';\n\nconst controller = webcodecsController();\n\nconst onPause = () => {\n  console.log('Paused');\n};\n\nconst onResume = () => {\n  console.log('Resumed');\n};\n\ncontroller.addEventListener('pause', onPause);\ncontroller.addEventListener('resume', onResume);\n\n// Make sure to cleanup later:\ncontroller.removeEventListener('pause', onPause);\ncontroller.removeEventListener('resume', onResume);\n```\n\nThe `webcodecsController` object emits the following events:\n\n### `pause`\n\nEmitted when the conversion is paused.\n\n### `resume`\n\nEmitted when the conversion is resumed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/webcodecs-controller.ts)\n- [Pause, resume and abort conversion](/docs/webcodecs/pause-resume-abort)\n- [`convertMedia()`](/docs/webcodecs/convert-media)\n"
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