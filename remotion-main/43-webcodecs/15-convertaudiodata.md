---
title: "convertAudioData()"
url: "https://www.remotion.dev/docs/webcodecs/convert-audiodata"
path: "/docs/webcodecs/convert-audiodata"
---

"---\nimage: /generated/articles-docs-webcodecs-convert-audiodata.png\nid: convert-audiodata\ntitle: convertAudioData()\nslug: /webcodecs/convert-audiodata\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n# convertAudioData()<AvailableFrom v=\"4.0.288\"/>\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\nimport {LicenseDisclaimer} from './LicenseDisclaimer';\n\n<details>\n  <summary>💼 Important License Disclaimer</summary>\n  <LicenseDisclaimer />\n</details>\n\nConverts an [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object to a new [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object with a different sample rate or format, or both.\n\n```tsx twoslash title=\"Converting an audio data\"\nimport {convertAudioData} from '@remotion/webcodecs';\n\nconst audioData = new AudioData({\n  data: new Int32Array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),\n  format: 's32',\n  numberOfChannels: 1,\n  numberOfFrames: 10,\n  sampleRate: 44100,\n  timestamp: 0,\n});\n\nconst newAudioData = convertAudioData({audioData, newSampleRate: 22050});\n\n/*\n{\n  data: [0, 2, 4, 6, 8],\n  format: 's32',\n  numberOfChannels: 1,\n  numberOfFrames: 5,\n  sampleRate: 22050,\n  timestamp: 0,\n}\n*/\n```\n\n## Behavior\n\n- Rounding may occur.\n- The new sample rate must be between 3000 and 768000.\n- If no conversion is needed (same sample rate and format), the original `AudioData` is cloned.\n- No cleanup is done on either the input or output `AudioData` (call [`close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/close) on them yourself).\n\n## API\n\nTakes an object with the following properties:\n\n### `audioData`\n\nThe [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object to convert.\n\n### `newSampleRate?`\n\nThe new sample rate. Must be between 3000 and 768000 (only Chrome enforces this technically, but Remotion will throw an error always).\n\n### `newFormat?`\n\nThe new format.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/convert-audiodata.ts)\n- [convertMedia()](/docs/webcodecs/convert-media)\n"

*Part of the [`@remotion/webcodecs`](/docs/webcodecs) package.*

💼 Important License Disclaimer

This package is licensed under the [Remotion License](/docs/license).
We consider a team of 4 or more people a "company".

**For "companies"**: A Remotion Company license needs to be obtained to use this package.
 In a future version of [`@remotion/webcodecs`](), this package will also require the purchase of a newly created "WebCodecs Conversion Seat". [Get in touch](/contact) with us if you are planning to use this package.

**For individuals and teams up to 3:** You can use this package for free.

This is a short, non-binding explanation of our license. See the [License](/docs/license) itself for more details.

Converts an [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object to a new [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object with a different sample rate or format, or both.

```

Converting an audio dataimport {convertAudioData} from '@remotion/webcodecs';

const audioData = new AudioData({
  data: new Int32Array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
  format: 's32',
  numberOfChannels: 1,
  numberOfFrames: 10,
  sampleRate: 44100,
  timestamp: 0,
});

const newAudioData = convertAudioData({audioData, newSampleRate: 22050});

/*
{
  data: [0, 2, 4, 6, 8],
  format: 's32',
  numberOfChannels: 1,
  numberOfFrames: 5,
  sampleRate: 22050,
  timestamp: 0,
}
*/Copy
```

## Behavior[​](#behavior)

- Rounding may occur.

- The new sample rate must be between 3000 and 768000.

- If no conversion is needed (same sample rate and format), the original `AudioData` is cloned.

- No cleanup is done on either the input or output `AudioData` (call [`close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/close) on them yourself).

## API[​](#api)

Takes an object with the following properties:

### `audioData`[​](#audiodata)

The [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object to convert.

### `newSampleRate?`[​](#newsamplerate)

The new sample rate. Must be between 3000 and 768000 (only Chrome enforces this technically, but Remotion will throw an error always).

### `newFormat?`[​](#newformat)

The new format.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/convert-audiodata.ts)

- [convertMedia()](/docs/webcodecs/convert-media)
](/docs/webcodecs/convert-media)](/docs/webcodecs/convert-media)
](/docs/webcodecs/convert-media)
- ](/docs/webcodecs/convert-media)
- ](/docs/webcodecs/convert-media)
- ](/docs/webcodecs/convert-media)
- ](/docs/webcodecs/convert-media)
- ](/docs/webcodecs/convert-media)