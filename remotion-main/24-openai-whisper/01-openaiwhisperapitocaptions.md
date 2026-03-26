---
title: "openAiWhisperApiToCaptions()"
url: "https://www.remotion.dev/docs/openai-whisper/openai-whisper-api-to-captions"
path: "/docs/openai-whisper/openai-whisper-api-to-captions"
---

"---\nimage: /generated/articles-docs-openai-whisper-openai-whisper-api-to-captions.png\ntitle: openAiWhisperApiToCaptions()\ncrumb: '@remotion/openai-whisper'\n---\n\n# openAiWhisperApiToCaptions()<AvailableFrom v=\"4.0.217\"/>\n\nTurns the output from [`openai.audio.transcriptions.create`](https://platform.openai.com/docs/guides/speech-to-text/transcriptions) from the [openai](https://npm.im/openai) package into an array of [`Caption`](/docs/captions/caption) objects.\n\nThis package performs processing on the captions in order to retain the punctuation in the words, which is not by default included in the OpenAI response.\n\nThis function can be used in any JavaScript environment, but you should not use the OpenAI API in the browser because your API key will be exposed to the browser.\n\n```tsx twoslash title=\"Example usage\"\nimport fs from 'fs';\nimport {OpenAI} from 'openai';\nimport {openAiWhisperApiToCaptions} from '@remotion/openai-whisper';\n\nconst openai = new OpenAI();\n\nconst transcription = await openai.audio.transcriptions.create({\n  file: fs.createReadStream('audio.mp3'),\n  model: 'whisper-1',\n  response_format: 'verbose_json',\n  prompt: 'Hello, welcome to my lecture.',\n  timestamp_granularities: ['word'],\n});\n\nconst {captions} = openAiWhisperApiToCaptions({transcription});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/openai-whisper/src/openai-whisper-api-to-captions.ts)\n- [`@remotion/openai-whisper`](/docs/openai-whisper)\n- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)\n- [`@remotion/captions`](/docs/captions/api)\n"

Turns the output from [`openai.audio.transcriptions.create`](https://platform.openai.com/docs/guides/speech-to-text/transcriptions) from the [openai](https://npm.im/openai) package into an array of [`Caption`](/docs/captions/caption) objects.

This package performs processing on the captions in order to retain the punctuation in the words, which is not by default included in the OpenAI response.

This function can be used in any JavaScript environment, but you should not use the OpenAI API in the browser because your API key will be exposed to the browser.

```

Example usageimport fs from 'fs';
import {OpenAI} from 'openai';
import {openAiWhisperApiToCaptions} from '@remotion/openai-whisper';

const openai = new OpenAI();

const transcription = await openai.audio.transcriptions.create({
  file: fs.createReadStream('audio.mp3'),
  model: 'whisper-1',
  response_format: 'verbose_json',
  prompt: 'Hello, welcome to my lecture.',
  timestamp_granularities: ['word'],
});

const {captions} = openAiWhisperApiToCaptions({transcription});Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/openai-whisper/src/openai-whisper-api-to-captions.ts)

- [`@remotion/openai-whisper`](/docs/openai-whisper)

- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)

- [`@remotion/captions`](/docs/captions/api)
](/docs/captions/api)](/docs/captions/api)
](/docs/captions/api)