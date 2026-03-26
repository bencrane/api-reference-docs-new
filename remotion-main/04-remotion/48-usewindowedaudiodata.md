---
title: "useWindowedAudioData()"
url: "https://www.remotion.dev/docs/use-windowed-audio-data"
path: "/docs/use-windowed-audio-data"
---

"---\nimage: /generated/articles-docs-use-windowed-audio-data.png\ntitle: useWindowedAudioData()\nid: use-windowed-audio-data\ncrumb: '@remotion/media-utils'\n---\n\n# useWindowedAudioData()<AvailableFrom v=\"4.0.240\" />\n\n_Part of the `@remotion/media-utils` package of helper functions._\n\nThis is an alternative to [`useAudioData()`](/docs/use-audio-data) that only loads a portion of the audio around the current frame.  \nIt supports all [Mediabunny-supported formats.](/docs/mediabunny/formats)\n\nBefore v4.0.383, only WAV files were supported.\n\nUnlike [`useAudioData()`](/docs/use-audio-data), which keeps all of the audio data in memory, this function makes HTTP Range requests to only load the audio data around the current frame.  \nWe recommend using this function for visualizing audio with a long duration.\n\n:::info\nRemote audio files need to support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).\n\n<details>\n  <summary>More info</summary>\n  <ul>\n    <li>\n      Remotion's origin is usually <code>http://localhost:3000</code>, but it may be different if rendering on Lambda or the port is busy.\n    </li>\n    <li>\n      You can use{' '}\n      <a href=\"/docs/get-audio-duration-in-seconds\">\n        <code>getAudioDurationInSeconds()</code>\n      </a>{' '}\n      without the audio needing CORS.\n    </li>\n    <li>\n      You can <a href=\"/docs/chromium-flags#--disable-web-security\">disable CORS</a> during renders.\n    </li>\n  </ul>\n</details>\n:::\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {useWindowedAudioData, visualizeAudio} from '@remotion/media-utils';\nimport {staticFile, useCurrentFrame, useVideoConfig} from 'remotion';\n\nexport const MyComponent: React.FC = () => {\n  const {fps} = useVideoConfig();\n  const frame = useCurrentFrame();\n  const {audioData, dataOffsetInSeconds} = useWindowedAudioData({\n    src: staticFile('podcast.wav'),\n    frame,\n    fps,\n    windowInSeconds: 10,\n  });\n\n  if (!audioData) {\n    return null;\n  }\n\n  const visualization = visualizeAudio({\n    fps,\n    frame,\n    audioData,\n    numberOfSamples: 16,\n    dataOffsetInSeconds,\n  });\n\n  return null;\n};\n```\n\n## Arguments\n\nAn object with:\n\n### `src`\n\nA string pointing to an audio asset.\n\n### `frame`\n\n_`number`_\n\nThe current frame of the composition.\n\n### `fps`\n\n_`number`_\n\nThe frames per second of the composition. Should be taken from [`useVideoConfig()`](/docs/use-video-config).\n\n### `windowInSeconds`\n\n_`number`_\n\nThe audio will be segmented into windows of this length.  \nThe function will load the audio data around the current frame and the windows before and after.\n\nIn this example, the window is 10 seconds long, so the function will load the current window as well as the previous and next one, leading to up to 30 seconds of audio being loaded at a time.\n\n## Return value\n\nAn object with:\n\n### `audioData`\n\n_`AudioData | null`_\n\nAn object containing audio data (see documentation of [`getAudioData()`](/docs/get-audio-data)) or `null` if the data has not been loaded.\n\n### `dataOffsetInSeconds`\n\n_`number`_\n\nThe offset in seconds of the audio data that is currently loaded.  \nYou should pass it through to [`visualizeAudio()`](/docs/visualize-audio).\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/use-windowed-audio-data.ts)\n- [`getAudioData()`](/docs/get-audio-data)\n- [`visualizeAudio()`](/docs/visualize-audio)\n- [Audio visualization](/docs/audio/visualization)\n"

*Part of the `@remotion/media-utils` package of helper functions.*

This is an alternative to [`useAudioData()`](/docs/use-audio-data) that only loads a portion of the audio around the current frame.

It supports all [Mediabunny-supported formats.](/docs/mediabunny/formats)

Before v4.0.383, only WAV files were supported.

Unlike [`useAudioData()`](/docs/use-audio-data), which keeps all of the audio data in memory, this function makes HTTP Range requests to only load the audio data around the current frame.

We recommend using this function for visualizing audio with a long duration.
](/docs/use-audio-data)](/docs/use-audio-data)
](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)
- ](/docs/use-audio-data)