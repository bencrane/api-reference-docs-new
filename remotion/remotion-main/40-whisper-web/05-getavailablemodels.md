---
title: "getAvailableModels()"
url: "https://www.remotion.dev/docs/whisper-web/get-available-models"
path: "/docs/whisper-web/get-available-models"
---

"---\nimage: /generated/articles-docs-whisper-web-get-available-models.png\ntitle: getAvailableModels()\ncrumb: '@remotion/whisper-web'\n---\n\n# getAvailableModels()\n\n:::warning\n**Unstable API**: This package is experimental for the moment. As we test it, we might make a few changes to the API and switch to a WebGPU-based backend in the future.\n:::\n\nReturns an array of all available Whisper models with their names and download sizes.\n\n```tsx twoslash title=\"app.ts\"\nimport {getAvailableModels} from '@remotion/whisper-web';\n\nconst availableModels = getAvailableModels();\nconsole.log(availableModels);\n// [\n//   { name: 'tiny', downloadSize: 77691713 },\n//   { name: 'tiny.en', downloadSize: 77704715 },\n//   { name: 'base', downloadSize: 147951465 },\n//   { name: 'base.en', downloadSize: 147964211 },\n//   { name: 'small', downloadSize: 487601967 },\n//   { name: 'small.en', downloadSize: 487614201 }\n// ]\n```\n\n## Return value\n\nReturns an array of `AvailableModel` objects. Each object contains:\n\n- `name`: A `WhisperWebModel` string representing the model name\n- `downloadSize`: A number representing the download size in bytes\n\n## See also\n\n- [Source code for `getAvailableModels()`](https://github.com/remotion-dev/remotion/blob/main/packages/whisper-web/src/get-available-models.ts)\n- [`@remotion/whisper-web`](/docs/whisper-web)\n- [`downloadWhisperModel()`](/docs/whisper-web/download-whisper-model)\n- [`getLoadedModels()`](/docs/whisper-web/get-loaded-models)\n"

]()]()
]()
- ]()