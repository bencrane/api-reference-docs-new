---
title: "@remotion/install-whisper-cpp"
url: "https://www.remotion.dev/docs/install-whisper-cpp/"
path: "/docs/install-whisper-cpp/"
---

"---\nimage: /generated/articles-docs-install-whisper-cpp-index.png\ntitle: '@remotion/install-whisper-cpp'\ncrumb: 'Transcribe audio locally'\n---\n\n# @remotion/install-whisper-cpp<AvailableFrom v=\"4.0.115\" />\n\nWith [Whisper.cpp](https://github.com/ggerganov/whisper.cpp), you can transcribe audio locally on your machine.  \nThis package provides easy to use cross-platform functions to install Whisper.cpp and a model.\n\nimport {TableOfContents} from './install-whisper-cpp';\n\n<Installation pkg=\"@remotion/install-whisper-cpp\" />\n\n## Example usage\n\nInstall Whisper `1.5.5` (the latest version at the time of writing that we find works well and supports token-level timestamps) and the `medium.en` model to the `whisper.cpp` folder.\n\n```tsx twoslash title=\"install-whisper.cpp\"\nimport path from 'path';\nimport {downloadWhisperModel, installWhisperCpp, transcribe, toCaptions} from '@remotion/install-whisper-cpp';\nimport fs from 'fs';\n\nconst to = path.join(process.cwd(), 'whisper.cpp');\n\nawait installWhisperCpp({\n  to,\n  version: '1.5.5',\n});\n\nawait downloadWhisperModel({\n  model: 'medium.en',\n  folder: to,\n});\n\n// Convert the audio to a 16KHz wav file first if needed:\n// import {execSync} from 'child_process';\n// execSync('ffmpeg -i /path/to/audio.mp4 -ar 16000 /path/to/audio.wav -y');\n\nconst whisperCppOutput = await transcribe({\n  model: 'medium.en',\n  whisperPath: to,\n  whisperCppVersion: '1.5.5',\n  inputPath: '/path/to/audio.wav',\n  tokenLevelTimestamps: true,\n});\n\n// Optional: Apply our recommended postprocessing\nconst {captions} = toCaptions({\n  whisperCppOutput,\n});\n\nfs.writeFileSync('captions.json', JSON.stringify(captions, null, 2));\n```\n\n## Functions\n\n<TableOfContents />\n\n## License\n\nMIT\n\n## See also\n\n- [`@remotion/openai-whisper`](/docs/openai-whisper)\n"

With [Whisper.cpp](https://github.com/ggerganov/whisper.cpp), you can transcribe audio locally on your machine.

This package provides easy to use cross-platform functions to install Whisper.cpp and a model.

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/install-whisper-cppCopy
```

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

## Example usage[​](#example-usage)

Install Whisper `1.5.5` (the latest version at the time of writing that we find works well and supports token-level timestamps) and the `medium.en` model to the `whisper.cpp` folder.

```

install-whisper.cppimport path from 'path';
import {downloadWhisperModel, installWhisperCpp, transcribe, toCaptions} from '@remotion/install-whisper-cpp';
import fs from 'fs';

const to = path.join(process.cwd(), 'whisper.cpp');

await installWhisperCpp({
  to,
  version: '1.5.5',
});

await downloadWhisperModel({
  model: 'medium.en',
  folder: to,
});

// Convert the audio to a 16KHz wav file first if needed:
// import {execSync} from 'child_process';
// execSync('ffmpeg -i /path/to/audio.mp4 -ar 16000 /path/to/audio.wav -y');

const whisperCppOutput = await transcribe({
  model: 'medium.en',
  whisperPath: to,
  whisperCppVersion: '1.5.5',
  inputPath: '/path/to/audio.wav',
  tokenLevelTimestamps: true,
});

// Optional: Apply our recommended postprocessing
const {captions} = toCaptions({
  whisperCppOutput,
});

fs.writeFileSync('captions.json', JSON.stringify(captions, null, 2));Copy
```

## Functions[​](#functions)

[
**installWhisperCpp()**
Install the whisper.cpp software](/docs/install-whisper-cpp/install-whisper-cpp)[
**downloadWhisperModel()**
Download a Whisper model](/docs/install-whisper-cpp/download-whisper-model)[
**transcribe()**
Transcribe an audio file](/docs/install-whisper-cpp/transcribe)[
**toCaptions()**
Converts the output from `transcribe()` into an array of `Caption` objects](/docs/install-whisper-cpp/to-captions)

## License[​](#license)

MIT

## See also[​](#see-also)

- [`@remotion/openai-whisper`](/docs/openai-whisper)
](/docs/openai-whisper)](/docs/openai-whisper)
](/docs/openai-whisper)
- ](/docs/openai-whisper)
- ](/docs/openai-whisper)
- ](/docs/openai-whisper)