---
title: "useAudioData()"
url: "https://www.remotion.dev/docs/use-audio-data"
path: "/docs/use-audio-data"
---

"---\nimage: /generated/articles-docs-use-audio-data.png\ntitle: useAudioData()\nid: use-audio-data\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils` package of helper functions._\n\nThis convenience function wraps the [`getAudioData()`](/docs/get-audio-data) function into a hook and does 3 things:\n\n- Keeps the audio data in a state\n- Wraps the function in a [`delayRender()` / `continueRender()`](/docs/data-fetching) pattern.\n- Handles the case where the component gets unmounted while the fetching is in progress and a React error is thrown.\n\nUsing this function, you can elegantly render a component based on audio properties, for example together with the [`visualizeAudio()`](/docs/visualize-audio) function.\n\n:::info\nRemote audio files need to support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).\n\n<details>\n  <summary>More info</summary>\n  <ul>\n    <li>\n      Remotion's origin is usually <code>http://localhost:3000</code>, but it may be different if rendering on Lambda or the port is busy.\n    </li>\n    <li>\n      You can use{' '}\n      <a href=\"/docs/get-audio-duration-in-seconds\">\n        <code>getAudioDurationInSeconds()</code>\n      </a>{' '}\n      without the audio needing CORS.\n    </li>\n    <li>\n      You can <a href=\"/docs/chromium-flags#--disable-web-security\">disable CORS</a> during renders.\n    </li>\n  </ul>\n</details>\n:::\n\n## Arguments\n\n### `src`\n\nA string pointing to an audio asset.\n\n## Return value\n\n`AudioData | null` - An object containing audio data (see documentation of [`getAudioData()`](/docs/get-audio-data)) or `null` if the data has not been loaded.\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {useAudioData} from '@remotion/media-utils';\nimport {staticFile} from 'remotion';\n\nexport const MyComponent: React.FC = () => {\n  const audioData = useAudioData(staticFile('music.mp3'));\n\n  if (!audioData) {\n    return null;\n  }\n\n  return <div>This file has a {audioData.sampleRate} sampleRate.</div>;\n};\n```\n\n## Errors\n\nIf you pass in a file that has no audio track, this hook will throw an error (_from v4.0.75_) or lead to an unhandled rejection (_until v4.0.74_).\n\nTo determine if a file has an audio track, you may use the [`getVideoMetadata()`](/docs/renderer/get-video-metadata#audiocodec) function on the server to reject a file if it has no audio track. To do so, check if the `audioCodec` field is `null`.\n\nIf you want to catch the error in the component, you need to make your own inline hook by taking the source code from the bottom of this page.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/use-audio-data.ts)\n- [`getAudioData()`](/docs/get-audio-data)\n- [`visualizeAudio()`](/docs/visualize-audio)\n- [Audio visualization](/docs/audio/visualization)\n"

*Part of the `@remotion/media-utils` package of helper functions.*

This convenience function wraps the [`getAudioData()`](/docs/get-audio-data) function into a hook and does 3 things:

- Keeps the audio data in a state

- Wraps the function in a [`delayRender()` / `continueRender()`](/docs/data-fetching) pattern.

- Handles the case where the component gets unmounted while the fetching is in progress and a React error is thrown.

Using this function, you can elegantly render a component based on audio properties, for example together with the [`visualizeAudio()`](/docs/visualize-audio) function.
](/docs/visualize-audio)](/docs/visualize-audio)
](/docs/visualize-audio)
- ](/docs/visualize-audio)
- ](/docs/visualize-audio)
- ](/docs/visualize-audio)
- ](/docs/visualize-audio)
- ](/docs/visualize-audio)