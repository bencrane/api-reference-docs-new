---
title: "toCaptions()"
url: "https://www.remotion.dev/docs/whisper-web/to-captions"
path: "/docs/whisper-web/to-captions"
---

"---\nimage: /generated/articles-docs-whisper-web-to-captions.png\ntitle: toCaptions()\ncrumb: '@remotion/whisper-web'\n---\n\n# toCaptions()\n\nConverts the output from [`transcribe()`](/docs/whisper-web/transcribe) into an array of [`Caption`](/docs/captions/caption) objects, so you can use the functions from [`@remotion/captions`](/docs/captions/api).\n\n```tsx twoslash\nimport {toCaptions, transcribe, resampleTo16Khz} from '@remotion/whisper-web';\n\nconst file = new File([], 'audio.wav');\n\nconst channelWaveform = await resampleTo16Khz({\n  file,\n});\n\nconst whisperWebOutput = await transcribe({\n  channelWaveform,\n  model: 'tiny.en',\n});\n\nconst {captions} = toCaptions({\n  whisperWebOutput,\n});\n\nconsole.log(captions); /*\n [\n    {\n      text: \"William\",\n      startMs: 40,\n      endMs: 420,\n      timestampMs: 240,\n      confidence: 0.813602,\n    }, {\n      text: \" just\",\n      startMs: 420,\n      endMs: 650,\n      timestampMs: 480,\n      confidence: 0.990905,\n    }, {\n      text: \" hit\",\n      startMs: 650,\n      endMs: 810,\n      timestampMs: 700,\n      confidence: 0.981798,\n    }\n  ]\n*/\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/whisper-web/src/to-captions.ts)\n- [`@remotion/whisper-web`](/docs/whisper-web)\n- [`@remotion/captions`](/docs/captions/api)\n"

Converts the output from [`transcribe()`](/docs/whisper-web/transcribe) into an array of [`Caption`](/docs/captions/caption) objects, so you can use the functions from [`@remotion/captions`](/docs/captions/api).

```
import {toCaptions, transcribe, resampleTo16Khz} from '@remotion/whisper-web';

const file = new File([], 'audio.wav');

const channelWaveform = await resampleTo16Khz({
  file,
});

const whisperWebOutput = await transcribe({
  channelWaveform,
  model: 'tiny.en',
});

const {captions} = toCaptions({
  whisperWebOutput,
});

console.log(captions); /*
 [
    {
      text: "William",
      startMs: 40,
      endMs: 420,
      timestampMs: 240,
      confidence: 0.813602,
    }, {
      text: " just",
      startMs: 420,
      endMs: 650,
      timestampMs: 480,
      confidence: 0.990905,
    }, {
      text: " hit",
      startMs: 650,
      endMs: 810,
      timestampMs: 700,
      confidence: 0.981798,
    }
  ]
*/Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/whisper-web/src/to-captions.ts)

- [`@remotion/whisper-web`](/docs/whisper-web)

- [`@remotion/captions`](/docs/captions/api)
](/docs/captions/api)](/docs/captions/api)
](/docs/captions/api)