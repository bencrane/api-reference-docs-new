---
title: "visualizeAudioWaveform()"
url: "https://www.remotion.dev/docs/media-utils/visualize-audio-waveform"
path: "/docs/media-utils/visualize-audio-waveform"
---

"---\nimage: /generated/articles-docs-media-utils-visualize-audio-waveform.png\ntitle: visualizeAudioWaveform()\nid: visualize-audio-waveform\ncrumb: '@remotion/media-utils'\n---\n\nimport {AudioWaveFormExample} from '../../components/AudioWaveformExamples.tsx';\n\n_Part of the `@remotion/media-utils`_ package of helper functions.\n\nThis function takes in `AudioData` (for example fetched by [`useAudioData()`](/docs/use-audio-data)) and processes it for displaying as a waveform.\n\nThis function is suitable for visualizing voice. For visualizing music, use [`visualizeAudio()`](/docs/visualize-audio)\n\n```tsx twoslash title=\"Usage\"\nimport {createSmoothSvgPath, useAudioData, visualizeAudioWaveform, AudioData} from '@remotion/media-utils';\nimport React from 'react';\nimport {AbsoluteFill, Audio, useCurrentFrame, useVideoConfig, staticFile} from 'remotion';\n\nconst frame = useCurrentFrame();\nconst audioData = useAudioData(staticFile('podcast.wav')) as AudioData;\nconst {fps} = useVideoConfig();\n\n// ---cut---\nconst waveform = visualizeAudioWaveform({\n  fps,\n  frame,\n  audioData,\n  numberOfSamples: 16,\n  windowInSeconds: 1 / fps,\n});\n```\n\nSee [Examples](#examples) below.\n\n## Arguments\n\nThe only argument for this function is an object containing the following values:\n\n### `audioData`\n\n`AudioData`\n\nAn object containing audio data. You can fetch this object using [`useAudioData()`](/docs/use-audio-data) or [`getAudioData()`](/docs/get-audio-data).\n\n### `frame`\n\n`number`\n\nThe time of the track that you want to get the audio information for. The `frame` always refers to the position in the audio track - if you have shifted or trimmed the audio in your timeline, the frame returned by `useCurrentFrame` must also be tweaked before you pass it into this function.\n\n### `fps`\n\n`number`\n\nThe frame rate of the composition. This helps the function understand the meaning of the `frame` input.\n\n### `numberOfSamples`\n\n`number`\n\nMust be a power of two, such as `32`, `64`, `128`, etc. This parameter controls the length of the output array. A lower number will simplify the spectrum and is useful if you want to animate elements roughly based on the level of lows, mids and highs. A higher number will give the spectrum in more detail, which is useful for displaying a bar chart or waveform-style visualization of the audio.\n\n### `windowInSeconds`\n\n`number`\n\nTime in seconds (can be float) which represents the duration for which you want to see the audio waveform.  \nExample: Your video has an `fps` of 30, and you pass 15 as the `frame` on `visualizeAudioWaveform` and 0.25 as `windowInSeconds` then output will have audio waveform data from (15/30) - .125 = 0.375 sec to (15/30) +0.125 = 0.625 sec.\n\n### `dataOffsetInSeconds`<AvailableFrom v=\"4.0.268\" />\n\nThe amount of seconds the audio is offset, pass this parameter if you are using [`useWindowedAudioData()`](/docs/use-windowed-audio-data).\n\n### `normalize?`<AvailableFrom v=\"4.0.280\" />\n\n_boolean_\n\nDefault `false`. If set to `true`, then the wave data gets scaled so that the biggest value is `1`.\n\n## Return value\n\n`number[]`\n\nAn array of values describing the amplitude of each frequency range.  \nEach value is between -1 and 1.  \nThe array is of length defined by the `numberOfSamples` parameter.\n\n## Examples\n\n### Basic example\n\n```tsx twoslash\nimport {createSmoothSvgPath, useAudioData, visualizeAudioWaveform} from '@remotion/media-utils';\nimport React from 'react';\nimport {AbsoluteFill, Html5Audio, useCurrentFrame, useVideoConfig, staticFile} from 'remotion';\n\nconst height = 300;\n\nconst BaseExample: React.FC = () => {\n  const frame = useCurrentFrame();\n  const audioDataVoice = useAudioData(staticFile('podcast.wav'));\n  const {width, fps} = useVideoConfig();\n\n  if (!audioDataVoice) {\n    return null;\n  }\n\n  const waveform = visualizeAudioWaveform({\n    fps,\n    frame,\n    audioData: audioDataVoice,\n    numberOfSamples: 32,\n    windowInSeconds: 1 / fps,\n  });\n\n  const p = createSmoothSvgPath({\n    points: waveform.map((x, i) => {\n      return {\n        x: (i / (waveform.length - 1)) * width,\n        y: (x - 0.5) * height + height / 2,\n      };\n    }),\n  });\n\n  return (\n    <div style={{flex: 1}}>\n      <Html5Audio src={staticFile('podcast.wav')} />\n      <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center'}}>\n        <svg style={{backgroundColor: ' #0B84F3'}} viewBox={`0 0 ${width} ${height}`} width={width} height={height}>\n          <path stroke=\"white\" fill=\"none\" strokeWidth={10} d={p as string} />\n        </svg>\n      </AbsoluteFill>\n    </div>\n  );\n};\n```\n\n<AudioWaveFormExample type=\"base\" />\n<br />\n\n### Sliding effect\n\nBy increasing the `windowInSeconds` by tenfold, the audiogram starts moving to the right:\n\n```tsx twoslash {6}\nimport {createSmoothSvgPath, useAudioData, visualizeAudioWaveform, AudioData} from '@remotion/media-utils';\nimport React from 'react';\nimport {AbsoluteFill, Html5Audio, useCurrentFrame, useVideoConfig, staticFile} from 'remotion';\n\nconst frame = useCurrentFrame();\nconst audioDataVoice = useAudioData(staticFile('podcast.wav')) as AudioData;\nconst {fps} = useVideoConfig();\n\n// ---cut---\nconst waveform = visualizeAudioWaveform({\n  fps,\n  frame,\n  audioData: audioDataVoice,\n  numberOfSamples: 32,\n  windowInSeconds: 10 / fps,\n});\n```\n\n<AudioWaveFormExample type=\"moving\" />\n<br />\n\n### Posterizing\n\nBy only calculating the waveform every third frame, we make the waveform calmer and generate a cool effect:\n\n```tsx twoslash {3}\nimport {createSmoothSvgPath, useAudioData, visualizeAudioWaveform, AudioData} from '@remotion/media-utils';\nimport React from 'react';\nimport {AbsoluteFill, Html5Audio, useCurrentFrame, useVideoConfig, staticFile} from 'remotion';\n\nconst frame = useCurrentFrame();\nconst audioDataVoice = useAudioData(staticFile('podcast.wav')) as AudioData;\nconst {fps} = useVideoConfig();\n\n// ---cut---\nconst waveform = visualizeAudioWaveform({\n  fps,\n  frame: Math.round(frame / 3) * 3,\n  audioData: audioDataVoice,\n  numberOfSamples: 32,\n  windowInSeconds: 10 / fps,\n});\n```\n\n<AudioWaveFormExample type=\"posterized\" />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/visualize-audio-waveform.ts)\n- [Audio visualization](/docs/audio/visualization)\n- [`useAudioData()`](/docs/use-audio-data)\n- [`getAudioData()`](/docs/get-audio-data)\n- [`<Html5Audio/>`](/docs/html5-audio)\n- [Using audio](/docs/using-audio)\n"

*Part of the `@remotion/media-utils`* package of helper functions.

This function takes in `AudioData` (for example fetched by [`useAudioData()`](/docs/use-audio-data)) and processes it for displaying as a waveform.

This function is suitable for visualizing voice. For visualizing music, use [`visualizeAudio()`](/docs/visualize-audio)

```

Usageconst waveform = visualizeAudioWaveform({
  fps,
  frame,
  audioData,
  numberOfSamples: 16,
  windowInSeconds: 1 / fps,
});Copy
```

See [Examples](#examples) below.

## Arguments[​](#arguments)

The only argument for this function is an object containing the following values:

### `audioData`[​](#audiodata)

`AudioData`

An object containing audio data. You can fetch this object using [`useAudioData()`](/docs/use-audio-data) or [`getAudioData()`](/docs/get-audio-data).

### `frame`[​](#frame)

`number`

The time of the track that you want to get the audio information for. The `frame` always refers to the position in the audio track - if you have shifted or trimmed the audio in your timeline, the frame returned by `useCurrentFrame` must also be tweaked before you pass it into this function.

### `fps`[​](#fps)

`number`

The frame rate of the composition. This helps the function understand the meaning of the `frame` input.

### `numberOfSamples`[​](#numberofsamples)

`number`

Must be a power of two, such as `32`, `64`, `128`, etc. This parameter controls the length of the output array. A lower number will simplify the spectrum and is useful if you want to animate elements roughly based on the level of lows, mids and highs. A higher number will give the spectrum in more detail, which is useful for displaying a bar chart or waveform-style visualization of the audio.

### `windowInSeconds`[​](#windowinseconds)

`number`

Time in seconds (can be float) which represents the duration for which you want to see the audio waveform.

Example: Your video has an `fps` of 30, and you pass 15 as the `frame` on `visualizeAudioWaveform` and 0.25 as `windowInSeconds` then output will have audio waveform data from (15/30) - .125 = 0.375 sec to (15/30) +0.125 = 0.625 sec.

### `dataOffsetInSeconds`[v4.0.268](https://github.com/remotion-dev/remotion/releases/v4.0.268)[​](#dataoffsetinseconds)

The amount of seconds the audio is offset, pass this parameter if you are using [`useWindowedAudioData()`](/docs/use-windowed-audio-data).

### `normalize?`[v4.0.280](https://github.com/remotion-dev/remotion/releases/v4.0.280)[​](#normalize)

*boolean*

Default `false`. If set to `true`, then the wave data gets scaled so that the biggest value is `1`.

## Return value[​](#return-value)

`number[]`

An array of values describing the amplitude of each frequency range.

Each value is between -1 and 1.

The array is of length defined by the `numberOfSamples` parameter.

## Examples[​](#examples)

### Basic example[​](#basic-example)

```
import {createSmoothSvgPath, useAudioData, visualizeAudioWaveform} from '@remotion/media-utils';
import React from 'react';
import {AbsoluteFill, Html5Audio, useCurrentFrame, useVideoConfig, staticFile} from 'remotion';

const height = 300;

const BaseExample: React.FC = () => {
  const frame = useCurrentFrame();
  const audioDataVoice = useAudioData(staticFile('podcast.wav'));
  const {width, fps} = useVideoConfig();

  if (!audioDataVoice) {
    return null;
  }

  const waveform = visualizeAudioWaveform({
    fps,
    frame,
    audioData: audioDataVoice,
    numberOfSamples: 32,
    windowInSeconds: 1 / fps,
  });

  const p = createSmoothSvgPath({
    points: waveform.map((x, i) => {
      return {
        x: (i / (waveform.length - 1)) * width,
        y: (x - 0.5) * height + height / 2,
      };
    }),
  });

  return (
    <div style={{flex: 1}}>
      <Html5Audio src={staticFile('podcast.wav')} />
      <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center'}}>
        <svg style={{backgroundColor: ' #0B84F3'}} viewBox={`0 0 ${width} ${height}`} width={width} height={height}>
          <path stroke="white" fill="none" strokeWidth={10} d={p as string} />
        </svg>
      </AbsoluteFill>
    </div>
  );
};Copy
```

### Sliding effect[​](#sliding-effect)

By increasing the `windowInSeconds` by tenfold, the audiogram starts moving to the right:

```
const waveform = visualizeAudioWaveform({
  fps,
  frame,
  audioData: audioDataVoice,
  numberOfSamples: 32,
  windowInSeconds: 10 / fps,
});Copy
```

### Posterizing[​](#posterizing)

By only calculating the waveform every third frame, we make the waveform calmer and generate a cool effect:

```
const waveform = visualizeAudioWaveform({
  fps,
  frame: Math.round(frame / 3) * 3,
  audioData: audioDataVoice,
  numberOfSamples: 32,
  windowInSeconds: 10 / fps,
});Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/visualize-audio-waveform.ts)

- [Audio visualization](/docs/audio/visualization)

- [`useAudioData()`](/docs/use-audio-data)

- [`getAudioData()`](/docs/get-audio-data)

- [`<Html5Audio/>`](/docs/html5-audio)

- [Using audio](/docs/using-audio)
](/docs/using-audio)](/docs/using-audio)
](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)
- ](/docs/using-audio)