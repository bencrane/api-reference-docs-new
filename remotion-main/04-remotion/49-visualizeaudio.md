---
title: "visualizeAudio()"
url: "https://www.remotion.dev/docs/visualize-audio"
path: "/docs/visualize-audio"
---

"---\nimage: /generated/articles-docs-visualize-audio.png\ntitle: visualizeAudio()\nid: visualize-audio\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils` package of helper functions._\n\nThis function takes in `AudioData` (for example fetched by [`useAudioData()`](/docs/use-audio-data)) and processes it for displaying as bars.\n\n## Arguments\n\nTakes an object containing the following values:\n\n### `audioData`\n\n_`AudioData`_\n\nAn object containing audio data. You can fetch this object using [`useAudioData()`](/docs/use-audio-data) or [`getAudioData()`](/docs/get-audio-data).\n\n### `frame`\n\n_`number`_\n\nThe time of the track that you want to get the audio information for. The `frame` always refers to the position in the audio track - if you have shifted or trimmed the audio in your timeline, the frame returned by `useCurrentFrame` must also be tweaked before you pass it into this function.\n\n### `fps`\n\n_`number`_\n\nThe frame rate of the composition. This helps the function understand the meaning of the `frame` input.\n\n### `numberOfSamples`\n\n`number`\n\nMust be a power of two, such as `32`, `64`, `128`, etc. This parameter controls the length of the output array. A lower number will simplify the spectrum and is useful if you want to animate elements roughly based on the level of lows, mids and highs. A higher number will give the spectrum in more detail, which is useful for displaying a bar chart or waveform-style visualization of the audio.\n\n### `smoothing`\n\n`boolean`\n\nWhen set to `true` the returned values will be an average of the current, previous and next frames. The result is a smoother transition for quickly changing values. Default value is `true`.\n\n### `optimizeFor?`<AvailableFrom v=\"4.0.83\"/>\n\n_`\"accuracy\" | \"speed\"`_\n\nDefault `\"accuracy\"`. When set to `\"speed\"`, a faster Fast Fourier transform is used. Recommended for Remotion Lambda and when using a high number of samples. Read [user](https://discord.com/channels/809501355504959528/1189048518988550264/1190228606287360030) [experiences](https://discord.com/channels/809501355504959528/1155110845488046111/1155111360481480725) [here](https://github.com/remotion-dev/remotion/issues/2925).\n\n### `dataOffsetInSeconds`<AvailableFrom v=\"4.0.268\" />\n\nThe amount of seconds the audio is offset, pass this parameter if you are using [`useWindowedAudioData()`](/docs/use-windowed-audio-data).\n\n## Return value\n\n`number[]`\n\nAn array of values describing the amplitude of each frequency range. Each value is between 0 and 1. The array is of length defined by the `numberOfSamples` parameter.\n\nThe values on the left of the array are low frequencies (for example bass) and as we move towards the right, we go through the mid and high frequencies like drums and vocals.\n\nUsually the values on left side of the array can become much larger than the values on the right. This is not a mistake, but for some visualizations you might have to apply some postprocessing to it, you can flatten the curve by for example mapping each value to a logarithm of the original function.\n\n## Example\n\nIn this example, we render a bar chart visualizing the audio spectrum of an audio file we imported using [`useAudioData()`](/docs/use-audio-data) and `visualizeAudio()`.\n\n```tsx twoslash\nimport {useAudioData, visualizeAudio} from '@remotion/media-utils';\nimport {Html5Audio, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';\n\nexport const MyComponent: React.FC = () => {\n  const frame = useCurrentFrame();\n  const {width, height, fps} = useVideoConfig();\n  const audioData = useAudioData(staticFile('music.mp3'));\n\n  if (!audioData) {\n    return null;\n  }\n\n  const visualization = visualizeAudio({\n    fps,\n    frame,\n    audioData,\n    numberOfSamples: 16,\n  }); // [0.22, 0.1, 0.01, 0.01, 0.01, 0.02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\n\n  // Render a bar chart for each frequency, the higher the amplitude,\n  // the longer the bar\n  return (\n    <div>\n      <Html5Audio src={staticFile('music.mp3')} />\n      {visualization.map((v) => {\n        return <div style={{width: 1000 * v, height: 15, backgroundColor: 'blue'}} />;\n      })}\n    </div>\n  );\n};\n```\n\n## Postprocessing example\n\nA logarithmic representation of the audio will look more appealing than a linear one. Below is an example of a postprocessing step that looks prettier than the default one.\n\n```tsx twoslash\nimport {visualizeAudio} from '@remotion/media-utils';\nconst params = {\n  audioData: {\n    channelWaveforms: [],\n    sampleRate: 0,\n    durationInSeconds: 0,\n    numberOfChannels: 0,\n    resultId: '',\n    isRemote: true,\n  },\n  frame: 0,\n  fps: 0,\n  numberOfSamples: 0,\n};\n// ---cut---\n/**\n * This postprocessing step will match the values with what you'd\n * get from WebAudio's `AnalyserNode.getByteFrequencyData()`.\n *\n * MDN: https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/getByteFrequencyData\n * W3C Spec: https://www.w3.org/TR/webaudio/#AnalyserNode-methods\n */\n\n// get the frequency data\nconst frequencyData = visualizeAudio(params);\n\n// default scaling factors from the W3C spec for getByteFrequencyData\nconst minDb = -100;\nconst maxDb = -30;\n\nconst amplitudes = frequencyData.map((value) => {\n  // convert to decibels (will be in the range `-Infinity` to `0`)\n  const db = 20 * Math.log10(value);\n\n  // scale to fit between min and max\n  const scaled = (db - minDb) / (maxDb - minDb);\n\n  return scaled;\n});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/visualize-audio.ts)\n- [Audio visualization](/docs/audio/visualization)\n- [`useAudioData()`](/docs/use-audio-data)\n- [`getAudioData()`](/docs/get-audio-data)\n- [`<Html5Audio/>`](/docs/html5-audio)\n- [Using audio](/docs/using-audio)\n"

*Part of the `@remotion/media-utils` package of helper functions.*

This function takes in `AudioData` (for example fetched by [`useAudioData()`](/docs/use-audio-data)) and processes it for displaying as bars.

## Arguments[​](#arguments)

Takes an object containing the following values:

### `audioData`[​](#audiodata)

*`AudioData`*

An object containing audio data. You can fetch this object using [`useAudioData()`](/docs/use-audio-data) or [`getAudioData()`](/docs/get-audio-data).

### `frame`[​](#frame)

*`number`*

The time of the track that you want to get the audio information for. The `frame` always refers to the position in the audio track - if you have shifted or trimmed the audio in your timeline, the frame returned by `useCurrentFrame` must also be tweaked before you pass it into this function.

### `fps`[​](#fps)

*`number`*

The frame rate of the composition. This helps the function understand the meaning of the `frame` input.

### `numberOfSamples`[​](#numberofsamples)

`number`

Must be a power of two, such as `32`, `64`, `128`, etc. This parameter controls the length of the output array. A lower number will simplify the spectrum and is useful if you want to animate elements roughly based on the level of lows, mids and highs. A higher number will give the spectrum in more detail, which is useful for displaying a bar chart or waveform-style visualization of the audio.

### `smoothing`[​](#smoothing)

`boolean`

When set to `true` the returned values will be an average of the current, previous and next frames. The result is a smoother transition for quickly changing values. Default value is `true`.

### `optimizeFor?`[v4.0.83](https://github.com/remotion-dev/remotion/releases/v4.0.83)[​](#optimizefor)

*`"accuracy" | "speed"`*

Default `"accuracy"`. When set to `"speed"`, a faster Fast Fourier transform is used. Recommended for Remotion Lambda and when using a high number of samples. Read [user](https://discord.com/channels/809501355504959528/1189048518988550264/1190228606287360030) [experiences](https://discord.com/channels/809501355504959528/1155110845488046111/1155111360481480725) [here](https://github.com/remotion-dev/remotion/issues/2925).

### `dataOffsetInSeconds`[v4.0.268](https://github.com/remotion-dev/remotion/releases/v4.0.268)[​](#dataoffsetinseconds)

The amount of seconds the audio is offset, pass this parameter if you are using [`useWindowedAudioData()`](/docs/use-windowed-audio-data).

## Return value[​](#return-value)

`number[]`

An array of values describing the amplitude of each frequency range. Each value is between 0 and 1. The array is of length defined by the `numberOfSamples` parameter.

The values on the left of the array are low frequencies (for example bass) and as we move towards the right, we go through the mid and high frequencies like drums and vocals.

Usually the values on left side of the array can become much larger than the values on the right. This is not a mistake, but for some visualizations you might have to apply some postprocessing to it, you can flatten the curve by for example mapping each value to a logarithm of the original function.

## Example[​](#example)

In this example, we render a bar chart visualizing the audio spectrum of an audio file we imported using [`useAudioData()`](/docs/use-audio-data) and `visualizeAudio()`.

```
import {useAudioData, visualizeAudio} from '@remotion/media-utils';
import {Html5Audio, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';

export const MyComponent: React.FC = () => {
  const frame = useCurrentFrame();
  const {width, height, fps} = useVideoConfig();
  const audioData = useAudioData(staticFile('music.mp3'));

  if (!audioData) {
    return null;
  }

  const visualization = visualizeAudio({
    fps,
    frame,
    audioData,
    numberOfSamples: 16,
  }); // [0.22, 0.1, 0.01, 0.01, 0.01, 0.02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  // Render a bar chart for each frequency, the higher the amplitude,
  // the longer the bar
  return (
    <div>
      <Html5Audio src={staticFile('music.mp3')} />
      {visualization.map((v) => {
        return <div style={{width: 1000 * v, height: 15, backgroundColor: 'blue'}} />;
      })}
    </div>
  );
};Copy
```

## Postprocessing example[​](#postprocessing-example)

A logarithmic representation of the audio will look more appealing than a linear one. Below is an example of a postprocessing step that looks prettier than the default one.

```
/**
 * This postprocessing step will match the values with what you'd
 * get from WebAudio's `AnalyserNode.getByteFrequencyData()`.
 *
 * MDN: https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/getByteFrequencyData
 * W3C Spec: https://www.w3.org/TR/webaudio/#AnalyserNode-methods
 */

// get the frequency data
const frequencyData = visualizeAudio(params);

// default scaling factors from the W3C spec for getByteFrequencyData
const minDb = -100;
const maxDb = -30;

const amplitudes = frequencyData.map((value) => {
  // convert to decibels (will be in the range `-Infinity` to `0`)
  const db = 20 * Math.log10(value);

  // scale to fit between min and max
  const scaled = (db - minDb) / (maxDb - minDb);

  return scaled;
});Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/visualize-audio.ts)

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