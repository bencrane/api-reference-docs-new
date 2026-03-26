---
title: "extractFramesOnWebWorker()"
url: "https://www.remotion.dev/docs/webcodecs/extract-frames-on-web-worker"
path: "/docs/webcodecs/extract-frames-on-web-worker"
---

"---\nimage: /generated/articles-docs-webcodecs-extract-frames-on-web-worker.png\nid: extract-frames-on-web-worker\ntitle: extractFramesOnWebWorker()\nslug: /webcodecs/extract-frames-on-web-worker\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!  \n**We recommend using [Mediabunny for extracting frames](/docs/mediabunny/extract-frames) instead.**\n:::\n\n# extractFramesOnWebWorker()<AvailableFrom v=\"4.0.330\"/>\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\nExtracts frames from a video at specific timestamps using [`parseMediaOnWebWorker()`](/docs/media-parser/parse-media-on-web-worker).\n\nSince Remotion is migrating to [Mediabunny](https://mediabunny.dev), we recommend using the [Mediabunny-based frame extraction implementation](/docs/mediabunny/extract-frames) for new projects.\n\n```tsx twoslash title=\"Extracting frames\"\nimport {extractFramesOnWebWorker} from '@remotion/webcodecs/worker';\n\nawait extractFramesOnWebWorker({\n  src: 'https://remotion.media/video.mp4',\n  timestampsInSeconds: [0, 1, 2, 3, 4],\n  onFrame: (frame) => {\n    console.log(frame);\n    //           ^?\n  },\n});\n```\n\n## API\n\n### `src`\n\nA URL or `File`/`Blob`.\n\nIf it is a remote URL, it must support CORS.\n\n### `timestampsInSeconds`\n\nAn array of timestamps in seconds, or a function that returns a promise resolving to an array of timestamps in seconds based on the video track.\n\nConsider you wanting you to create a filmstrip of a video. You can do this by extracting as many frames as fit in a canvas.\n\n```tsx twoslash title=\"Extracting as many frames as fit in a canvas\"\nimport type {ExtractFramesTimestampsInSecondsFn} from '@remotion/webcodecs';\n\nconst toSeconds = 10;\nconst fromSeconds = 0;\nconst canvasWidth = 500;\nconst canvasHeight = 80;\n\nconst timestamps: ExtractFramesTimestampsInSecondsFn = async ({track}) => {\n  const aspectRatio = track.width / track.height;\n  const amountOfFramesFit = Math.ceil(canvasWidth / (canvasHeight * aspectRatio));\n  const timestampsInSeconds: number[] = [];\n  const segmentDuration = toSeconds - fromSeconds;\n\n  for (let i = 0; i < amountOfFramesFit; i++) {\n    timestampsInSeconds.push(fromSeconds + (segmentDuration / amountOfFramesFit) * (i + 0.5));\n  }\n\n  return timestampsInSeconds;\n};\n```\n\nNote that currently, you can not get the duration of the video in seconds before the extraction.  \nFor this you need currently to make another [`parseMedia()`](/docs/media-parser/parse-media) call beforehand.\n\n### `onFrame`\n\nA callback that will be called with the frame at the given timestamp.  \nEach frame is a [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object that can for example be drawn to a canvas.\n\n### `acknowledgeRemotionLicense?`\n\nAcknowledge the [Remotion License](/docs/license) to make the console message disappear.\n\n### `signal?`\n\nAn optional [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to abort the extraction.\n\n### `logLevel?`\n\n_string_ <TsType type=\"LogLevel\" source=\"@remotion/media-parser\"/>\n\nOne of `\"error\"`, `\"warn\"`, `\"info\"`, `\"debug\"`, `\"trace\"`.  \nDefault value: `\"info\"`, which logs only important information.\n\n## See also\n\n- **[Extracting frames with Mediabunny](/docs/mediabunny/extract-frames)** (recommended)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/extract-frames.ts)\n- [`@remotion/webcodecs`](/docs/webcodecs)\n- [`parseMedia()`](/docs/media-parser/parse-media)\n- [`parseMediaOnWebWorker()`](/docs/media-parser/parse-media-on-web-worker)\n"

*Part of the [`@remotion/webcodecs`](/docs/webcodecs) package.*

Extracts frames from a video at specific timestamps using [`parseMediaOnWebWorker()`](/docs/media-parser/parse-media-on-web-worker).

Since Remotion is migrating to [Mediabunny](https://mediabunny.dev), we recommend using the [Mediabunny-based frame extraction implementation](/docs/mediabunny/extract-frames) for new projects.

```

Extracting framesimport {extractFramesOnWebWorker} from '@remotion/webcodecs/worker';

await extractFramesOnWebWorker({
  src: 'https://remotion.media/video.mp4',
  timestampsInSeconds: [0, 1, 2, 3, 4],
  onFrame: (frame) => {
    console.log(frame);
                 
(parameter) frame: VideoFrame  },
});Copy
```

## API[​](#api)

### `src`[​](#src)

A URL or `File`/`Blob`.

If it is a remote URL, it must support CORS.

### `timestampsInSeconds`[​](#timestampsinseconds)

An array of timestamps in seconds, or a function that returns a promise resolving to an array of timestamps in seconds based on the video track.

Consider you wanting you to create a filmstrip of a video. You can do this by extracting as many frames as fit in a canvas.

```

Extracting as many frames as fit in a canvasimport type {ExtractFramesTimestampsInSecondsFn} from '@remotion/webcodecs';

const toSeconds = 10;
const fromSeconds = 0;
const canvasWidth = 500;
const canvasHeight = 80;

const timestamps: ExtractFramesTimestampsInSecondsFn = async ({track}) => {
  const aspectRatio = track.width / track.height;
  const amountOfFramesFit = Math.ceil(canvasWidth / (canvasHeight * aspectRatio));
  const timestampsInSeconds: number[] = [];
  const segmentDuration = toSeconds - fromSeconds;

  for (let i = 0; i < amountOfFramesFit; i++) {
    timestampsInSeconds.push(fromSeconds + (segmentDuration / amountOfFramesFit) * (i + 0.5));
  }

  return timestampsInSeconds;
};Copy
```

Note that currently, you can not get the duration of the video in seconds before the extraction.

For this you need currently to make another [`parseMedia()`](/docs/media-parser/parse-media) call beforehand.

### `onFrame`[​](#onframe)

A callback that will be called with the frame at the given timestamp.

Each frame is a [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object that can for example be drawn to a canvas.

### `acknowledgeRemotionLicense?`[​](#acknowledgeremotionlicense)

Acknowledge the [Remotion License](/docs/license) to make the console message disappear.

### `signal?`[​](#signal)

An optional [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) to abort the extraction.

### `logLevel?`[​](#loglevel)

*string* `LogLevel`

One of `"error"`, `"warn"`, `"info"`, `"debug"`, `"trace"`.

Default value: `"info"`, which logs only important information.

## See also[​](#see-also)

- **[Extracting frames with Mediabunny](/docs/mediabunny/extract-frames)** (recommended)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/extract-frames.ts)

- [`@remotion/webcodecs`](/docs/webcodecs)

- [`parseMedia()`](/docs/media-parser/parse-media)

- [`parseMediaOnWebWorker()`](/docs/media-parser/parse-media-on-web-worker)
](/docs/media-parser/parse-media-on-web-worker)](/docs/media-parser/parse-media-on-web-worker)
](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)
- ](/docs/media-parser/parse-media-on-web-worker)