---
title: "getVideoMetadata()"
url: "https://www.remotion.dev/docs/get-video-metadata"
path: "/docs/get-video-metadata"
---

"---\nimage: /generated/articles-docs-get-video-metadata.png\ntitle: getVideoMetadata()\nid: get-video-metadata\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils` package of helper functions._\n\n:::note\nDeprecated: Does not support H.265 videos on Linux and also fails on some other formats.  \nBetter solution: [Get metadata using Mediabunny](/docs/mediabunny/metadata)\n:::\n\n:::note\nOnly works in the browser.\n:::\n\nTakes a `src` to a video, loads it and returns metadata for the specified source.\n\n## Arguments\n\n### `src`\n\nA string pointing to an asset.\n\n## Return value\n\n`Promise<VideoMetadata>` - object with information about the video data:\n\n- `durationInSeconds`: `number` The duration of the video in seconds.\n- `width`: `number` The width of the video in pixels.\n- `height`: `number` The height of the video in pixels.\n- `aspectRatio`: `number` Video width divided by video height.\n- `isRemote`: `boolean` Whether the video was imported locally or from a different origin.\n\n:::warning\n`durationInSeconds` may return `Infinity`. This happens if the duration of the video is not stored in the beginning of the file.  \nThis is for example the case for videos that are recorded with a webcam and being encoded while the recording is still in progress.  \nEnsure handling for `Infinity` for user-provided videos and re-encode videos with FFmpeg to move the duration to the beginning of the file.\n:::\n\n## Example\n\n```tsx twoslash\nimport {staticFile} from 'remotion';\n// ---cut---\nimport {getVideoMetadata} from '@remotion/media-utils';\n\nawait getVideoMetadata(staticFile('video.mp4')); /* {\n  durationInSeconds: 100.00,\n  width: 1280,\n  height: 720,\n  aspectRatio: 1.77777778,\n  isRemote: false\n} */\nawait getVideoMetadata('https://example.com/remote-audio.webm'); /* {\n  durationInSeconds: 40.213,\n  width: 1920,\n  height: 1080,\n  aspectRatio: 1.77777778,\n  isRemote: true\n} */\n```\n\n## Caching behavior\n\nThis function is memoizing the results it returns.\nIf you pass in the same argument to `src` multiple times, it will return a cached version from the second time on, regardless of if the file has changed. To clear the cache, you have to reload the page.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/get-video-metadata.ts)\n- [Using videos](/docs/assets#using-videos)\n"

*Part of the `@remotion/media-utils` package of helper functions.*
]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()