---
title: "getPartialAudioData()"
url: "https://www.remotion.dev/docs/webcodecs/get-partial-audio-data"
path: "/docs/webcodecs/get-partial-audio-data"
---

"---\nimage: /generated/articles-docs-webcodecs-get-partial-audio-data.png\nsidebar_label: getPartialAudioData()\ntitle: getPartialAudioData()\nslug: /webcodecs/get-partial-audio-data\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nimport {UnstableDisclaimer} from './UnstableDisclaimer';\n\n:::warning\n\n<UnstableDisclaimer />\n:::\n\n# getPartialAudioData()<AvailableFrom v=\"4.0.328\" />\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\nExtracts audio data from a specific time window of a media file and returns it as a Float32Array.\n\n```tsx twoslash title=\"Extract audio data from 10-20 seconds\"\nimport {getPartialAudioData} from '@remotion/webcodecs';\n\nconst audioData = await getPartialAudioData({\n  src: 'https://remotion.media/audio.wav',\n  fromSeconds: 10,\n  toSeconds: 20,\n  channelIndex: 0, // Left channel for stereo audio\n  signal: new AbortController().signal,\n});\n\nconsole.log('Audio samples:', audioData.length);\nconsole.log('First sample value:', audioData[0]);\n```\n\n## API\n\n### `src`\n\n**string**\n\nA URL pointing to a media file, or a `File`/`Blob` object.\n\nIf it is a remote URL, it must support CORS and the server must support byte-range requests for efficient seeking.\n\n### `fromSeconds`\n\n**number**\n\nThe start time in seconds from which to extract audio data.\n\n### `toSeconds`\n\n**number**\n\nThe end time in seconds until which to extract audio data.\n\n### `channelIndex`\n\n**number**\n\nThe audio channel index to extract. For stereo audio:\n\n- `0` = Left channel\n- `1` = Right channel\n\nFor mono audio, use `0`.\n\n### `signal`\n\n**AbortSignal**\n\nAn [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation.\n\n```tsx twoslash title=\"Using AbortController\"\nimport {getPartialAudioData} from '@remotion/webcodecs';\nimport {hasBeenAborted} from '@remotion/media-parser';\n\nconst controller = new AbortController();\n\n// Cancel after 5 seconds\nsetTimeout(() => controller.abort(), 5000);\n\ntry {\n  const audioData = await getPartialAudioData({\n    src: 'https://remotion.media/audio.wav',\n    fromSeconds: 0,\n    toSeconds: 30,\n    channelIndex: 0,\n    signal: controller.signal,\n  });\n} catch (err) {\n  if (hasBeenAborted(err)) {\n    console.log('Operation was cancelled');\n  }\n}\n```\n\n## Return value\n\nReturns a `Promise<Float32Array>` containing the audio samples for the requested time window and channel.\n\nThe sample values are normalized floating-point numbers typically in the range of -1.0 to 1.0.\n\n## Notes\n\n- The function uses a small buffer (0.1 seconds) around the requested time window to ensure accurate extraction of chunks that span across boundaries\n- For multi-channel audio, samples are de-interleaved to extract the specific channel\n- The function leverages [`@remotion/media-parser`](/docs/media-parser) for parsing and WebCodecs for efficient audio decoding\n- Sample rate and other audio characteristics depend on the source media file\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-partial-audio-data.ts)\n- [`createAudioDecoder()`](/docs/webcodecs/create-audio-decoder)\n- [`@remotion/media-parser`](/docs/media-parser)\n- [`@remotion/webcodecs`](/docs/webcodecs)\n"

*Part of the [`@remotion/webcodecs`](/docs/webcodecs) package.*

Extracts audio data from a specific time window of a media file and returns it as a Float32Array.

```

Extract audio data from 10-20 secondsimport {getPartialAudioData} from '@remotion/webcodecs';

const audioData = await getPartialAudioData({
  src: 'https://remotion.media/audio.wav',
  fromSeconds: 10,
  toSeconds: 20,
  channelIndex: 0, // Left channel for stereo audio
  signal: new AbortController().signal,
});

console.log('Audio samples:', audioData.length);
console.log('First sample value:', audioData[0]);Copy
```

## API[​](#api)

### `src`[​](#src)

**string**

A URL pointing to a media file, or a `File`/`Blob` object.

If it is a remote URL, it must support CORS and the server must support byte-range requests for efficient seeking.

### `fromSeconds`[​](#fromseconds)

**number**

The start time in seconds from which to extract audio data.

### `toSeconds`[​](#toseconds)

**number**

The end time in seconds until which to extract audio data.

### `channelIndex`[​](#channelindex)

**number**

The audio channel index to extract. For stereo audio:

- `0` = Left channel

- `1` = Right channel

For mono audio, use `0`.

### `signal`[​](#signal)

**AbortSignal**

An [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to cancel the operation.

```

Using AbortControllerimport {getPartialAudioData} from '@remotion/webcodecs';
import {hasBeenAborted} from '@remotion/media-parser';

const controller = new AbortController();

// Cancel after 5 seconds
setTimeout(() => controller.abort(), 5000);

try {
  const audioData = await getPartialAudioData({
    src: 'https://remotion.media/audio.wav',
    fromSeconds: 0,
    toSeconds: 30,
    channelIndex: 0,
    signal: controller.signal,
  });
} catch (err) {
  if (hasBeenAborted(err)) {
    console.log('Operation was cancelled');
  }
}Copy
```

## Return value[​](#return-value)

Returns a `Promise<Float32Array>` containing the audio samples for the requested time window and channel.

The sample values are normalized floating-point numbers typically in the range of -1.0 to 1.0.

## Notes[​](#notes)

- The function uses a small buffer (0.1 seconds) around the requested time window to ensure accurate extraction of chunks that span across boundaries

- For multi-channel audio, samples are de-interleaved to extract the specific channel

- The function leverages [`@remotion/media-parser`](/docs/media-parser) for parsing and WebCodecs for efficient audio decoding

- Sample rate and other audio characteristics depend on the source media file

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-partial-audio-data.ts)

- [`createAudioDecoder()`](/docs/webcodecs/create-audio-decoder)

- [`@remotion/media-parser`](/docs/media-parser)

- [`@remotion/webcodecs`](/docs/webcodecs)
](/docs/webcodecs)](/docs/webcodecs)
](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)