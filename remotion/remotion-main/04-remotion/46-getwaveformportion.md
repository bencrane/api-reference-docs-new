---
title: "getWaveformPortion()"
url: "https://www.remotion.dev/docs/get-waveform-portion"
path: "/docs/get-waveform-portion"
---

"---\nimage: /generated/articles-docs-get-waveform-portion.png\ntitle: getWaveformPortion()\nid: get-waveform-portion\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils` package of helper functions._\n\nTakes bulky waveform data (for example fetched by [`getAudioData()`](/docs/get-audio-data)) and returns a trimmed and simplified version of it, for simpler visualization. This function is suitable if you only need volume data, if you need more detailed data about each frequency range, use [`visualizeAudio()`](/docs/visualize-audio).\n\n## Arguments\n\nAn object with the following arguments:\n\n### `audioData`\n\n_AudioData_\n\nInformation about the audio. Use [`getAudioData()`](/docs/get-audio-data) to fetch it.\n\n### `startTimeInSeconds`\n\n_number_\n\nTrim the waveform to exclude all data before `startTimeInSeconds`.\n\n### `durationInSeconds`\n\n_number_\n\ntrim the waveform to exclude all data after `startTimeInSeconds + durationInSeconds`.\n\n### `numberOfSamples`\n\n_number_\n\nHow big you want the result array to be. The function will compress the waveform to fit in `numberOfSamples` data points.\n\n### `channel`\n\n_number_\n\nWhich channel to use. Defaults to 0.\n\n### `outputRange`\n\n_number_\n\nThe range of the output values. Either `minus-one-to-one` or `zero-to-one`. Defaults to `zero-to-one`.\n\n### `normalize?`<AvailableFrom v=\"4.0.280\" />\n\n_boolean_\n\nDefault `true`. If set to `true`, then the data gets scaled so that the biggest value is `1`.\n\n:::note\nFrom v4.0.267 to v4.0.279, `normalize` was mistakenly changed to `false`. We have restored the original behavior from v4.0.280.\n:::\n\n## Return value\n\n`Bar[]` - An array of objects with the following properties:\n\n### `index`\n\n_number_\n\nThe index of the datapoint, starting at 0. Useful for specifying as React `key` attribute without getting a warning.\n\n### `amplitude`\n\n_number_\n\nA value describing the amplitude / volume / loudness of the audio. Values range between 0 and 1.\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {getAudioData, getWaveformPortion} from '@remotion/media-utils';\nimport {staticFile} from 'remotion';\n\nconst audioData = await getAudioData(staticFile('music.mp3')); /* {\n  channelWaveforms: [Float32Array(4410000), Float32Array(4410000)],\n  sampleRate: 44100,\n  durationInSeconds: 100.0000,\n  numberOfChannels: 2,\n  resultId: \"0.432878981\",\n  isRemote: false\n} */\n\nconst waveformPortion = await getWaveformPortion({\n  audioData,\n  // Will select time range of 20-40 seconds\n  startTimeInSeconds: 20,\n  durationInSeconds: 20,\n  numberOfSamples: 10,\n}); // [{index: 0, amplitude: 0.14}, ... {index: 9, amplitude: 0.79}]\n\nconsole.log(waveformPortion.length); // 10\n```\n\n## Alternatives\n\nThe [`visualizeAudio()`](/docs/visualize-audio) function is more suitable for visualizing audio based on frequency properties of the audio (bass, mids, highs, etc).\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/get-waveform-portion.ts)\n- [Using audio](/docs/using-audio)\n- [`<Html5Audio/>`](/docs/html5-audio)\n"

*Part of the `@remotion/media-utils` package of helper functions.*

Takes bulky waveform data (for example fetched by [`getAudioData()`](/docs/get-audio-data)) and returns a trimmed and simplified version of it, for simpler visualization. This function is suitable if you only need volume data, if you need more detailed data about each frequency range, use [`visualizeAudio()`](/docs/visualize-audio).

## Arguments[​](#arguments)

An object with the following arguments:

### `audioData`[​](#audiodata)

*AudioData*

Information about the audio. Use [`getAudioData()`](/docs/get-audio-data) to fetch it.

### `startTimeInSeconds`[​](#starttimeinseconds)

*number*

Trim the waveform to exclude all data before `startTimeInSeconds`.

### `durationInSeconds`[​](#durationinseconds)

*number*

trim the waveform to exclude all data after `startTimeInSeconds + durationInSeconds`.

### `numberOfSamples`[​](#numberofsamples)

*number*

How big you want the result array to be. The function will compress the waveform to fit in `numberOfSamples` data points.

### `channel`[​](#channel)

*number*

Which channel to use. Defaults to 0.

### `outputRange`[​](#outputrange)

*number*

The range of the output values. Either `minus-one-to-one` or `zero-to-one`. Defaults to `zero-to-one`.

### `normalize?`[v4.0.280](https://github.com/remotion-dev/remotion/releases/v4.0.280)[​](#normalize)

*boolean*

Default `true`. If set to `true`, then the data gets scaled so that the biggest value is `1`.
](#normalize)](#normalize)
](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)
- ](#normalize)