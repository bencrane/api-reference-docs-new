---
title: "toCaptions()"
url: "https://www.remotion.dev/docs/install-whisper-cpp/to-captions"
path: "/docs/install-whisper-cpp/to-captions"
---

"---\nimage: /generated/articles-docs-install-whisper-cpp-to-captions.png\ntitle: toCaptions()\ncrumb: '@remotion/install-whisper-cpp'\n---\n\n# toCaptions()<AvailableFrom v=\"4.0.216\"/>\n\nConverts the output from [`transcribe()`](/docs/install-whisper-cpp/transcribe) into an array of [`Caption`](/docs/captions/caption) objects, so you can use the functions from [`@remotion/captions`](/docs/captions/api).\n\n```tsx twoslash title=\"generate-captions.mjs\"\nimport {toCaptions, transcribe} from '@remotion/install-whisper-cpp';\nimport path from 'path';\n\nconst whisperCppOutput = await transcribe({\n  inputPath: '/path/to/audio.wav',\n  whisperPath: path.join(process.cwd(), 'whisper.cpp'),\n  whisperCppVersion: '1.5.5',\n  model: 'medium.en',\n  tokenLevelTimestamps: true,\n});\n\nconst {captions} = toCaptions({\n  whisperCppOutput,\n});\n\nconsole.log(captions); /*\n [\n    {\n      text: \"William\",\n      startMs: 40,\n      endMs: 420,\n      timestampMs: 240,\n      confidence: 0.813602,\n    }, {\n      text: \" just\",\n      startMs: 420,\n      endMs: 650,\n      timestampMs: 480,\n      confidence: 0.990905,\n    }, {\n      text: \" hit\",\n      startMs: 650,\n      endMs: 810,\n      timestampMs: 700,\n      confidence: 0.981798,\n    }\n  ]\n*/\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/install-whisper-cpp/src/to-captions.ts)\n- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)\n- [`@remotion/captions`](/docs/captions/api)\n"

Converts the output from [`transcribe()`](/docs/install-whisper-cpp/transcribe) into an array of [`Caption`](/docs/captions/caption) objects, so you can use the functions from [`@remotion/captions`](/docs/captions/api).

```

generate-captions.mjsimport {toCaptions, transcribe} from '@remotion/install-whisper-cpp';
import path from 'path';

const whisperCppOutput = await transcribe({
  inputPath: '/path/to/audio.wav',
  whisperPath: path.join(process.cwd(), 'whisper.cpp'),
  whisperCppVersion: '1.5.5',
  model: 'medium.en',
  tokenLevelTimestamps: true,
});

const {captions} = toCaptions({
  whisperCppOutput,
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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/install-whisper-cpp/src/to-captions.ts)

- [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp)

- [`@remotion/captions`](/docs/captions/api)
](/docs/captions/api)](/docs/captions/api)
](/docs/captions/api)