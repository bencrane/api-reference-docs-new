---
title: "getAudioDurationInSeconds()"
url: "https://www.remotion.dev/docs/get-audio-duration-in-seconds"
path: "/docs/get-audio-duration-in-seconds"
---

"---\nimage: /generated/articles-docs-get-audio-duration-in-seconds.png\ntitle: getAudioDurationInSeconds()\nid: get-audio-duration-in-seconds\ncrumb: '@remotion/media-utils'\n---\n\n:::warning[Deprecated]\nThis function has been deprecated. Use [`getMediaMetadata()`](/docs/mediabunny/metadata) instead, which is faster and supports more formats.\n:::\n\n_Part of the `@remotion/media-utils` package of helper functions._\n\n_Previously called `getAudioDuration()`._\n\nGets the duration in seconds of an audio source. Remotion will create an invisible `<audio>` tag, load the audio and return the duration.\n\n## Arguments\n\n### `src`\n\nA string pointing to an audio asset\n\n## Return value\n\n`Promise<number>` - the duration of the audio file.\n\n## Example\n\n```tsx twoslash\nimport {useCallback, useEffect} from 'react';\nimport {staticFile} from 'remotion';\n// ---cut---\nimport {getAudioDurationInSeconds} from '@remotion/media-utils';\nimport music from './music.mp3';\n\nconst MyComp: React.FC = () => {\n  const getDuration = useCallback(async () => {\n    const publicFile = await getAudioDurationInSeconds(staticFile('voiceover.wav')); // 33.221\n    const imported = await getAudioDurationInSeconds(music); // 127.452\n    const remote = await getAudioDurationInSeconds('https://example.com/remote-audio.aac'); // 50.24\n  }, []);\n\n  useEffect(() => {\n    getDuration();\n  }, []);\n\n  return null;\n};\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/get-audio-duration-in-seconds.ts)\n"
]()]()
]()
- ]()
- ]()
- ]()
- ]()