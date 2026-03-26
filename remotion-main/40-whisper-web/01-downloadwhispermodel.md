---
title: "downloadWhisperModel()"
url: "https://www.remotion.dev/docs/whisper-web/download-whisper-model"
path: "/docs/whisper-web/download-whisper-model"
---

"---\nimage: /generated/articles-docs-whisper-web-download-whisper-model.png\ntitle: downloadWhisperModel()\ncrumb: '@remotion/whisper-web'\n---\n\n# downloadWhisperModel()\n\n:::warning\n**Unstable API**: This package is experimental for the moment. As we test it, we might make a few changes to the API and switch to a WebGPU-based backend in the future.\n:::\n\nDownloads a Whisper model into IndexedDB.\n\n```tsx twoslash title=\"app.ts\"\nimport {downloadWhisperModel} from '@remotion/whisper-web';\n\nconst {alreadyDownloaded} = await downloadWhisperModel({\n  model: 'tiny.en',\n  onProgress: (progress) => {\n    console.log(progress);\n  },\n});\n```\n\n## Options\n\n### `model`\n\nThe model to download. Possible values: `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`.\n\n### `onProgress?`\n\nAct upon download progress. This is the function signature:\n\n```tsx twoslash\nimport {DownloadWhisperModelOnProgress, DownloadWhisperModelProgress} from '@remotion/whisper-web';\n\nconst onProgress: DownloadWhisperModelOnProgress = ({progress, totalBytes, downloadedBytes}: DownloadWhisperModelProgress) => {\n  console.log({progress, totalBytes, downloadedBytes});\n};\n```\n\n## Return Value\n\nReturns an object with the following properties:\n\n- `alreadyDownloaded`: Whether the model has already been downloaded.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/whisper-web/src/download-whisper-model.ts)\n- [`@remotion/whisper-web`](/docs/whisper-web)\n- [`transcribe()`](/docs/whisper-web/transcribe)\n"

]()]()
]()
- ]()
- ]()
- ]()
- ]()