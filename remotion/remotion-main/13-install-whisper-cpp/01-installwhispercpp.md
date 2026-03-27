---
title: "installWhisperCpp()"
url: "https://www.remotion.dev/docs/install-whisper-cpp/install-whisper-cpp"
path: "/docs/install-whisper-cpp/install-whisper-cpp"
---

"---\nimage: /generated/articles-docs-install-whisper-cpp-install-whisper-cpp.png\nslug: install-whisper-cpp\ntitle: installWhisperCpp()\ncrumb: '@remotion/install-whisper-cpp'\n---\n\n# installWhisperCpp()<AvailableFrom v=\"4.0.115\"/>\n\nInstalls a Whisper.cpp version into a folder.\n\n```tsx twoslash title=\"install-whisper.mjs\"\nimport path from 'path';\nimport {installWhisperCpp} from '@remotion/install-whisper-cpp';\n\nconst {alreadyExisted} = await installWhisperCpp({\n  to: path.join(process.cwd(), 'whisper.cpp'),\n  version: '1.5.5', // A Whisper.cpp semver or git tag\n});\n```\n\n## Which Whisper.cpp version to select?\n\n- Generally, the source is cloned from Whisper.cpp GitHub and built.\n- On Windows, a binary is downloaded. Only semantic version format (e.g. `1.5.4` is supported).\n- On Windows, there are no binaries newer than `1.6.0` available.\n- From `1.7.3` and later, `cmake` is required for Whisper.cpp to be built.\n\n## Note this\n\n- You should add the folder you install Whisper.cpp into to the `.gitignore` file.\n- If the output folder already exists, the function will not do anything and return `{ alreadyExisted: true }`.\n- You also need to download a model for Whisper.cpp to work. You can do this with the [`downloadWhisperModel()`](/docs/install-whisper-cpp/download-whisper-model) function.\n\n## Options\n\n### `to`\n\nThe folder to install Whisper.cpp into.\n\n### `version`\n\nThe version of Whisper.cpp to install. Don't include the `v` prefix.\nThis can be either a hash of a Whisper.cpp commit or a semantic version of an official release.\n\n:::info\nOn Windows, currently only release tags of Whisper.cpp are supported (e.g `1.5.4`).\n:::\n\n### `printOutput?`\n\nWhether to print the output of the installation process to the console. Defaults to `true`.\n\n### `signal?`<AvailableFrom v=\"4.0.156\" />\n\nA signal from an [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) to cancel the installation process.\n\n## Return value\n\nReturns a `Promise` that resolves to an object with the following property:\n\n### `alreadyExisted`\n\nWhether the folder already existed. If it did, and contains the necessary executable, the function did not perform any installation and returned `true`. If the executable is missing in the existing folder, the function expects manual deletion of the folder before attempting another installation.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/install-whisper-cpp/src/install-whisper-cpp.ts)\n- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)\n- [`@remotion/openai-whisper`](/docs/openai-whisper)\n- [`downloadWhisperModel()`](/docs/install-whisper-cpp/download-whisper-model)\n"

Installs a Whisper.cpp version into a folder.

```

install-whisper.mjsimport path from 'path';
import {installWhisperCpp} from '@remotion/install-whisper-cpp';

const {alreadyExisted} = await installWhisperCpp({
  to: path.join(process.cwd(), 'whisper.cpp'),
  version: '1.5.5', // A Whisper.cpp semver or git tag
});Copy
```

## Which Whisper.cpp version to select?[​](#which-whispercpp-version-to-select)

- Generally, the source is cloned from Whisper.cpp GitHub and built.

- On Windows, a binary is downloaded. Only semantic version format (e.g. `1.5.4` is supported).

- On Windows, there are no binaries newer than `1.6.0` available.

- From `1.7.3` and later, `cmake` is required for Whisper.cpp to be built.

## Note this[​](#note-this)

- You should add the folder you install Whisper.cpp into to the `.gitignore` file.

- If the output folder already exists, the function will not do anything and return `{ alreadyExisted: true }`.

- You also need to download a model for Whisper.cpp to work. You can do this with the [`downloadWhisperModel()`](/docs/install-whisper-cpp/download-whisper-model) function.

## Options[​](#options)

### `to`[​](#to)

The folder to install Whisper.cpp into.

### `version`[​](#version)

The version of Whisper.cpp to install. Don't include the `v` prefix.
This can be either a hash of a Whisper.cpp commit or a semantic version of an official release.
](#version)](#version)
](#version)
- ](#version)
- ](#version)
- ](#version)
- ](#version)
- ](#version)
- ](#version)
- ](#version)
- ](#version)
- ](#version)