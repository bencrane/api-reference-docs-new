---
title: "downloadWhisperModel()"
url: "https://www.remotion.dev/docs/install-whisper-cpp/download-whisper-model"
path: "/docs/install-whisper-cpp/download-whisper-model"
---

"---\nimage: /generated/articles-docs-install-whisper-cpp-download-whisper-model.png\ntitle: downloadWhisperModel()\ncrumb: '@remotion/install-whisper-cpp'\n---\n\n# downloadWhisperModel()<AvailableFrom v=\"4.0.115\"/>\n\nDownloads a Whisper.cpp model to a folder.  \nYou should first install Whisper.cpp, for example through [`installWhisperCpp()`](/docs/install-whisper-cpp/install-whisper-cpp).\n\n```tsx twoslash title=\"install-whisper.mjs\"\nimport path from 'path';\nimport {downloadWhisperModel} from '@remotion/install-whisper-cpp';\n\nconst {alreadyExisted} = await downloadWhisperModel({\n  model: 'medium.en',\n  folder: path.join(process.cwd(), 'whisper.cpp'),\n});\n```\n\n## Options\n\n### `folder`\n\nThe folder to download the model to. The model will be downloaded into this folder with the filename `ggml-${model}.bin`.\n\n### `model`\n\nThe model to download. Possible values: `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`, `medium`, `medium.en`, `large-v1`, `large-v2`, `large-v3`, `large-v3-turbo`.\n\n### `onProgress?`\n\nAct upon download progress. This is the function signature:\n\n```tsx twoslash\nimport type {OnProgress} from '@remotion/install-whisper-cpp';\n\nconst onProgress: OnProgress = (downloadedBytes: number, totalBytes: number) => {\n  const progress = downloadedBytes / totalBytes;\n};\n```\n\n### `printOutput?`\n\nPrint human-readable progress to the console. Default: `true`.\n\n### `signal?`<AvailableFrom v=\"4.0.156\" />\n\nA signal from an [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) to cancel the download process.\n\n## Return Value\n\nReturns an object with the following property:\n\n### `alreadyExisted`\n\nIndicates whether a file at the output path already existed. If it did, the function did not do anything and this property is set to `true`.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/install-whisper-cpp/src/download-whisper-model.ts)\n- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)\n- [`installWhisperCpp()`](/docs/install-whisper-cpp/install-whisper-cpp)\n"

Downloads a Whisper.cpp model to a folder.

You should first install Whisper.cpp, for example through [`installWhisperCpp()`](/docs/install-whisper-cpp/install-whisper-cpp).

```

install-whisper.mjsimport path from 'path';
import {downloadWhisperModel} from '@remotion/install-whisper-cpp';

const {alreadyExisted} = await downloadWhisperModel({
  model: 'medium.en',
  folder: path.join(process.cwd(), 'whisper.cpp'),
});Copy
```

## Options[​](#options)

### `folder`[​](#folder)

The folder to download the model to. The model will be downloaded into this folder with the filename `ggml-${model}.bin`.

### `model`[​](#model)

The model to download. Possible values: `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`, `medium`, `medium.en`, `large-v1`, `large-v2`, `large-v3`, `large-v3-turbo`.

### `onProgress?`[​](#onprogress)

Act upon download progress. This is the function signature:

```
import type {OnProgress} from '@remotion/install-whisper-cpp';

const onProgress: OnProgress = (downloadedBytes: number, totalBytes: number) => {
  const progress = downloadedBytes / totalBytes;
};Copy
```

### `printOutput?`[​](#printoutput)

Print human-readable progress to the console. Default: `true`.

### `signal?`[v4.0.156](https://github.com/remotion-dev/remotion/releases/v4.0.156)[​](#signal)

A signal from an [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) to cancel the download process.

## Return Value[​](#return-value)

Returns an object with the following property:

### `alreadyExisted`[​](#alreadyexisted)

Indicates whether a file at the output path already existed. If it did, the function did not do anything and this property is set to `true`.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/install-whisper-cpp/src/download-whisper-model.ts)

- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)

- [`installWhisperCpp()`](/docs/install-whisper-cpp/install-whisper-cpp)
](/docs/install-whisper-cpp/install-whisper-cpp)](/docs/install-whisper-cpp/install-whisper-cpp)
](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)
- ](/docs/install-whisper-cpp/install-whisper-cpp)