---
title: "convertMedia()"
url: "https://www.remotion.dev/docs/webcodecs/convert-media"
path: "/docs/webcodecs/convert-media"
---

"---\nimage: /generated/articles-docs-webcodecs-convert-media.png\nid: convert-media\ntitle: convertMedia()\nslug: /webcodecs/convert-media\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n# convertMedia()<AvailableFrom v=\"4.0.229\"/>\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\nimport {LicenseDisclaimer} from './LicenseDisclaimer';\nimport {UnstableDisclaimer} from './UnstableDisclaimer';\n\n<details>\n  <summary>💼 Important License Disclaimer</summary>\n  <LicenseDisclaimer />\n</details>\n<details>\n  <summary>🚧 Unstable API</summary>\n  <UnstableDisclaimer />\n</details>\n\nRe-encodes a video using [WebCodecs](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) and [`@remotion/media-parser`](/docs/media-parser).\n\n```tsx twoslash title=\"Converting a video\"\nimport {convertMedia} from '@remotion/webcodecs';\n\nconst result = await convertMedia({\n  src: 'https://remotion.media/BigBuckBunny.mp4',\n  container: 'webm',\n});\n\n// Save the converted video as a Blob\nconst blob = await result.save();\n```\n\n## Return value\n\n`convertMedia()` returns a Promise that resolves to a `ConvertMediaResult` object with the following properties:\n\n### `save()`\n\n_Function that returns `Promise<Blob>`_\n\nCall this function to get the converted video as a `Blob`. You can then use this blob to:\n\n- Create a download link\n- Upload to a server\n- Display in a video element\n- Store in IndexedDB\n\n```tsx twoslash title=\"Saving and downloading a converted video\"\nimport {convertMedia} from '@remotion/webcodecs';\n\nconst result = await convertMedia({\n  src: 'https://remotion.media/BigBuckBunny.mp4',\n  container: 'webm',\n});\n\nconst blob = await result.save();\n\n// Create a download link\nconst url = URL.createObjectURL(blob);\nconst a = document.createElement('a');\na.href = url;\na.download = 'converted-video.webm';\ndocument.body.appendChild(a);\na.click();\ndocument.body.removeChild(a);\nURL.revokeObjectURL(url);\n```\n\n### `remove()`\n\n_Function that returns `Promise<void>`_\n\nCall this function to clean up any temporary resources created during the conversion process.\n\n### `finalState`\n\n_object of type `ConvertMediaProgress`_\n\nContains the final state of the conversion process, including statistics about the conversion.\n\n## API\n\n### `src`\n\nA URL or `File`/`Blob`, or a local file path.\n\nIf passing a local file, tracks can only be copied, and the [`reader`](#reader) field must be set to [`nodeReader`](/docs/media-parser/node-reader).\n\n### `container`\n\n_string_ <TsType type=\"ConvertMediaContainer\" source=\"@remotion/webcodecs\"/>\n\nThe container format to convert to. Currently, `\"mp4\"`, `\"webm\"` and `\"wav\"` is supported.\n\n### `expectedDurationInSeconds?`\n\n_number_\n\nPass the expected duration of the output video in seconds, so that the size of the MP4 metadata section can be estimated well. If the value is not passed, 2MB will be allocated for the MP4 metadata section.\n\nIf the size is exceeded (for videos which are around 1 hour or longer), the render may fail in the end.\n\n### `expectedFrameRate?`\n\n_number_\n\nPass the expected frame rate of the output video, so that the size of the MP4 metadata section can be estimated well. If the value is not passed, 60 will be used as a conservative fallback.\n\n### `videoCodec?`\n\n_string_ <TsType type=\"ConvertMediaVideoCodec\" source=\"@remotion/webcodecs\"/>\n\nThe video codec to convert to. Currently, `\"h264\"`, `\"h265\"`, `\"vp8\"` and `\"vp9\"` are supported.  \nThe default is defined by [`getDefaultVideoCodec()`](/docs/webcodecs/get-default-video-codec).  \nIf a [`onVideoTrack`](#onvideotrack) handler is provided, it will override this setting.\n\n### `audioCodec?`\n\n_string_ <TsType type=\"ConvertMediaAudioCodec\" source=\"@remotion/webcodecs\"/>\n\nThe audio codec to convert to. Currently, only `\"opus\"` is supported.  \nThe default is defined by [`getDefaultAudioCodec()`](/docs/webcodecs/get-default-audio-codec).  \nIf an [`onAudioTrack`](#onaudiotrack) handler is provided, it will override this setting.\n\n### `controller?`\n\nA [controller](/docs/webcodecs/webcodecs-controller) object that allows you to pause, resume and abort the conversion process.\n\n### `reader?`\n\nA [reader](/docs/media-parser/readers) interface.\n\nDefault value: `webReader`, which allows URLs and `File` objects.\n\n### `rotate?`\n\n_number_\n\nThe number of degrees to rotate the video. See [Rotate a video](/docs/webcodecs/rotate-a-video) for more information.\n\n### `resize?`\n\n_object_ <TsType type=\"ResizeOperation\" source=\"@remotion/webcodecs\"/>\n\nResize the video. See [Resize a video](/docs/webcodecs/resize-a-video) for more information.\n\n### `logLevel?`\n\n_string_ <TsType type=\"LogLevel\" source=\"@remotion/media-parser\"/>\n\nOne of `\"error\"`, `\"warn\"`, `\"info\"`, `\"debug\"`, `\"trace\"`.  \nDefault value: `\"info\"`, which logs only important information.\n\n### `onProgress?`\n\n_Function_ <TsType type=\"ConvertMediaOnProgress\" source=\"@remotion/media-parser\"/>\n\nAllows receiving progress updates. The following fields are available:\n\n```tsx twoslash\nimport type {ConvertMediaOnProgress, ConvertMediaProgress} from '@remotion/webcodecs';\n\nexport const onProgress: ConvertMediaOnProgress = ({decodedVideoFrames, decodedAudioFrames, encodedVideoFrames, encodedAudioFrames, bytesWritten, millisecondsWritten, expectedOutputDurationInMs, overallProgress}: ConvertMediaProgress) => {\n  console.log(decodedVideoFrames);\n  //                   ^?\n  console.log(decodedAudioFrames);\n  //                   ^?\n  console.log(encodedVideoFrames);\n  //                   ^?\n  console.log(encodedAudioFrames);\n  //                   ^?\n  console.log(bytesWritten);\n  //                   ^?\n  console.log(millisecondsWritten);\n  //                   ^?\n  console.log(expectedOutputDurationInMs);\n  //                   ^?\n  console.log(overallProgress);\n  //                   ^?\n};\n```\n\n### `onVideoFrame?`\n\n_Function_ <TsType type=\"ConvertMediaOnVideoFrame\" source=\"@remotion/media-parser\"/>\n\nAllows you to hook into the video frames. The frames are [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) objects.\n\n```tsx twoslash\nimport type {ConvertMediaOnVideoFrame} from '@remotion/webcodecs';\n\nexport const onVideoFrame: ConvertMediaOnVideoFrame = ({frame}) => {\n  console.log(frame);\n  //           ^?\n\n  // Do something with the frame, for example:\n  // - Draw to a canvas\n  // - Modify the frame\n\n  // Then return the frame to be used for encoding.\n  return frame;\n};\n```\n\nThe callback function may be async.\n\nWhen the function returns, the returned frame is used for video encoding.  \nYou may return the same frame or replace it with a new `VideoFrame` object.\n\nAfter the function returns, `convertMedia()` will call [`.close()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame/close) on the input and output frames.  \nThis will destroy the frame and free up memory.\nIf you need a reference to the frame that lasts longer than the lifetime of this function, you must call [`.clone()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame/clone) on it.\n\nIf you return a different frame than the one you received, it must have the same values for `codedWidth`, `codedHeight`, `displayWidth` and `displayHeight`, `timestamp` and `duration` as the input frame.\n\n### `onAudioData?`\n\n_Function_ <TsType type=\"ConvertMediaOnAudioData\" source=\"@remotion/media-parser\"/>\n\nAllows you to hook into the audio data. The items are native [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) objects.\n\n```tsx twoslash\nimport type {ConvertMediaOnAudioData} from '@remotion/webcodecs';\n\nexport const onAudioData: ConvertMediaOnAudioData = ({audioData}) => {\n  console.log(audioData);\n  //           ^?\n\n  // Do something with the audiodata, for example:\n  // - Change the pitch\n  // - Lower the volume\n\n  // Then return the frame to be used for encoding.\n  return audioData;\n};\n```\n\nThe callback function may be async.\n\nWhen the function returns, the returned audio data is used for audio encoding.  \nYou may return the same audio data or replace it with a new [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object.\n\nAfter the function returns, `convertMedia()` will call [`.close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/close) on the input and output audio data.  \nThis will destroy the audio data and free up memory.\nIf you need a reference to the audio data that lasts longer than the lifetime of this function, you must call [`.clone()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/clone) on it.\n\nIf you return a different audio data than the one you received, it should have the same [`duration`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/duration), [`numberOfChannels`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/numberOfChannels), [`sampleRate`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/sampleRate), [`timestamp`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/format), [`numberOfChannels`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/timestamp), [`format`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/format) and [`numberOfChannels`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/numberOfChannels) as the input audio data.\n\n### `writer?`\n\n_object_ <TsType type=\"WriterInterface\" source=\"@remotion/webcodecs\" />\n\nA writer interface. The following interfaces are available:\n\n```tsx twoslash title=\"Buffer writer\"\nimport {bufferWriter} from '@remotion/webcodecs/buffer';\n//               ^?\n```\n\nWrite to a resizable Array Buffer.\n\n```tsx twoslash title=\"Web File System writer\"\nimport {canUseWebFsWriter, webFsWriter} from '@remotion/webcodecs/web-fs';\n//                          ^?\n\nawait canUseWebFsWriter(); // boolean\n```\n\nUse the Web File System API to write to a file.\n\nBy default the writer is `webFsWriter`.\n\n### `onAudioTrack?`\n\n_Function_ <TsType type=\"ConvertMediaOnAudioTrackHandler\" source=\"@remotion/webcodecs\"/>\n\nTake control of what to do for each audio track in the file: Re-encoding, copying, or dropping.  \nSee [Track Transformation](/docs/webcodecs/track-transformation) for a guide on how to use this callback.\n\n### `onVideoTrack?`\n\n_Function_ <TsType type=\"ConvertMediaOnVideoTrackHandler\" source=\"@remotion/webcodecs\"/>\n\nTake control of what to do for each video track in the file: Re-encoding, copying, or dropping.  \nSee [Track Transformation](/docs/webcodecs/track-transformation) for a guide on how to use this callback.\n\n### `selectM3uStream?`\n\n_Function_ <TsType type=\"SelectM3uStreamFn\" source=\"@remotion/media-parser\"/>\n\nA callback that is called when a `.m3u8` file is detected which has multiple streams.  \nSee [Stream selection](/docs/media-parser/stream-selection) for an example.\n\n### `progressIntervalInMs?`\n\n_number_\n\nThe interval in milliseconds at which the `onProgress` callback is called.  \nDefault `100`. Set to `0` for unthrottled updates.  \nNote that updates are fired very often and updating the DOM often may slow down the conversion process.\n\n### `seekingHints?`\n\nAn object that contains hints about the structure of the media file.\n\nSee [Seeking Hints](/docs/media-parser/seeking-hints) for more information.\n\n### `fields?` and Callbacks\n\nYou can obtain information about the video file while you are converting it.  \nThis feature is inherited from [`parseMedia()`](/docs/media-parser/parse-media), but only the callback-style API is available.\n\n```tsx twoslash title=\"Converting a video\"\nimport {convertMedia} from '@remotion/webcodecs';\n\nconst result = await convertMedia({\n  src: 'https://remotion.media/BigBuckBunny.mp4',\n  container: 'webm',\n  videoCodec: 'vp8',\n  audioCodec: 'opus',\n  fields: {\n    size: true,\n  },\n  onSize: (size) => {\n    console.log(size);\n    //           ^?\n  },\n});\n\nconst blob = await result.save();\n```\n\n## License\n\n[See notes about `@remotion/webcodecs`](/docs/webcodecs#-license-disclaimer).\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/convert-media.ts)\n- [`@remotion/webcodecs`](/docs/webcodecs)\n- [`parseMedia()`](/docs/media-parser/parse-media)\n"

*Part of the [`@remotion/webcodecs`](/docs/webcodecs) package.*

💼 Important License Disclaimer

This package is licensed under the [Remotion License](/docs/license).
We consider a team of 4 or more people a "company".

**For "companies"**: A Remotion Company license needs to be obtained to use this package.
 In a future version of [`@remotion/webcodecs`](), this package will also require the purchase of a newly created "WebCodecs Conversion Seat". [Get in touch](/contact) with us if you are planning to use this package.

**For individuals and teams up to 3:** You can use this package for free.

This is a short, non-binding explanation of our license. See the [License](/docs/license) itself for more details.
🚧 Unstable API

This package is experimental.
We might change the API at any time, until we remove this notice.

Re-encodes a video using [WebCodecs](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) and [`@remotion/media-parser`](/docs/media-parser).

```

Converting a videoimport {convertMedia} from '@remotion/webcodecs';

const result = await convertMedia({
  src: 'https://remotion.media/BigBuckBunny.mp4',
  container: 'webm',
});

// Save the converted video as a Blob
const blob = await result.save();Copy
```

## Return value[​](#return-value)

`convertMedia()` returns a Promise that resolves to a `ConvertMediaResult` object with the following properties:

### `save()`[​](#save)

*Function that returns `Promise<Blob>`*

Call this function to get the converted video as a `Blob`. You can then use this blob to:

- Create a download link

- Upload to a server

- Display in a video element

- Store in IndexedDB

```

Saving and downloading a converted videoimport {convertMedia} from '@remotion/webcodecs';

const result = await convertMedia({
  src: 'https://remotion.media/BigBuckBunny.mp4',
  container: 'webm',
});

const blob = await result.save();

// Create a download link
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'converted-video.webm';
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
URL.revokeObjectURL(url);Copy
```

### `remove()`[​](#remove)

*Function that returns `Promise<void>`*

Call this function to clean up any temporary resources created during the conversion process.

### `finalState`[​](#finalstate)

*object of type `ConvertMediaProgress`*

Contains the final state of the conversion process, including statistics about the conversion.

## API[​](#api)

### `src`[​](#src)

A URL or `File`/`Blob`, or a local file path.

If passing a local file, tracks can only be copied, and the [`reader`](#reader) field must be set to [`nodeReader`](/docs/media-parser/node-reader).

### `container`[​](#container)

*string* `ConvertMediaContainer`

The container format to convert to. Currently, `"mp4"`, `"webm"` and `"wav"` is supported.

### `expectedDurationInSeconds?`[​](#expecteddurationinseconds)

*number*

Pass the expected duration of the output video in seconds, so that the size of the MP4 metadata section can be estimated well. If the value is not passed, 2MB will be allocated for the MP4 metadata section.

If the size is exceeded (for videos which are around 1 hour or longer), the render may fail in the end.

### `expectedFrameRate?`[​](#expectedframerate)

*number*

Pass the expected frame rate of the output video, so that the size of the MP4 metadata section can be estimated well. If the value is not passed, 60 will be used as a conservative fallback.

### `videoCodec?`[​](#videocodec)

*string* `ConvertMediaVideoCodec`

The video codec to convert to. Currently, `"h264"`, `"h265"`, `"vp8"` and `"vp9"` are supported.

The default is defined by [`getDefaultVideoCodec()`](/docs/webcodecs/get-default-video-codec).

If a [`onVideoTrack`](#onvideotrack) handler is provided, it will override this setting.

### `audioCodec?`[​](#audiocodec)

*string* `ConvertMediaAudioCodec`

The audio codec to convert to. Currently, only `"opus"` is supported.

The default is defined by [`getDefaultAudioCodec()`](/docs/webcodecs/get-default-audio-codec).

If an [`onAudioTrack`](#onaudiotrack) handler is provided, it will override this setting.

### `controller?`[​](#controller)

A [controller](/docs/webcodecs/webcodecs-controller) object that allows you to pause, resume and abort the conversion process.

### `reader?`[​](#reader)

A [reader](/docs/media-parser/readers) interface.

Default value: `webReader`, which allows URLs and `File` objects.

### `rotate?`[​](#rotate)

*number*

The number of degrees to rotate the video. See [Rotate a video](/docs/webcodecs/rotate-a-video) for more information.

### `resize?`[​](#resize)

*object* `ResizeOperation`

Resize the video. See [Resize a video](/docs/webcodecs/resize-a-video) for more information.

### `logLevel?`[​](#loglevel)

*string* `LogLevel`

One of `"error"`, `"warn"`, `"info"`, `"debug"`, `"trace"`.

Default value: `"info"`, which logs only important information.

### `onProgress?`[​](#onprogress)

*Function* `ConvertMediaOnProgress`

Allows receiving progress updates. The following fields are available:

```
import type {ConvertMediaOnProgress, ConvertMediaProgress} from '@remotion/webcodecs';

export const onProgress: ConvertMediaOnProgress = ({decodedVideoFrames, decodedAudioFrames, encodedVideoFrames, encodedAudioFrames, bytesWritten, millisecondsWritten, expectedOutputDurationInMs, overallProgress}: ConvertMediaProgress) => {
  console.log(decodedVideoFrames);
                      
(parameter) decodedVideoFrames: number  console.log(decodedAudioFrames);
                      
(parameter) decodedAudioFrames: number  console.log(encodedVideoFrames);
                      
(parameter) encodedVideoFrames: number  console.log(encodedAudioFrames);
                      
(parameter) encodedAudioFrames: number  console.log(bytesWritten);
                   
(parameter) bytesWritten: number  console.log(millisecondsWritten);
                      
(parameter) millisecondsWritten: number  console.log(expectedOutputDurationInMs);
                          
(parameter) expectedOutputDurationInMs: number | null  console.log(overallProgress);
                    
(parameter) overallProgress: number | null};Copy
```

### `onVideoFrame?`[​](#onvideoframe)

*Function* `ConvertMediaOnVideoFrame`

Allows you to hook into the video frames. The frames are [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) objects.

```
import type {ConvertMediaOnVideoFrame} from '@remotion/webcodecs';

export const onVideoFrame: ConvertMediaOnVideoFrame = ({frame}) => {
  console.log(frame);
               
(parameter) frame: VideoFrame
  // Do something with the frame, for example:
  // - Draw to a canvas
  // - Modify the frame

  // Then return the frame to be used for encoding.
  return frame;
};Copy
```

The callback function may be async.

When the function returns, the returned frame is used for video encoding.

You may return the same frame or replace it with a new `VideoFrame` object.

After the function returns, `convertMedia()` will call [`.close()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame/close) on the input and output frames.

This will destroy the frame and free up memory.
If you need a reference to the frame that lasts longer than the lifetime of this function, you must call [`.clone()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame/clone) on it.

If you return a different frame than the one you received, it must have the same values for `codedWidth`, `codedHeight`, `displayWidth` and `displayHeight`, `timestamp` and `duration` as the input frame.

### `onAudioData?`[​](#onaudiodata)

*Function* `ConvertMediaOnAudioData`

Allows you to hook into the audio data. The items are native [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) objects.

```
import type {ConvertMediaOnAudioData} from '@remotion/webcodecs';

export const onAudioData: ConvertMediaOnAudioData = ({audioData}) => {
  console.log(audioData);
                 
(parameter) audioData: AudioData
  // Do something with the audiodata, for example:
  // - Change the pitch
  // - Lower the volume

  // Then return the frame to be used for encoding.
  return audioData;
};Copy
```

The callback function may be async.

When the function returns, the returned audio data is used for audio encoding.

You may return the same audio data or replace it with a new [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object.

After the function returns, `convertMedia()` will call [`.close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/close) on the input and output audio data.

This will destroy the audio data and free up memory.
If you need a reference to the audio data that lasts longer than the lifetime of this function, you must call [`.clone()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/clone) on it.

If you return a different audio data than the one you received, it should have the same [`duration`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/duration), [`numberOfChannels`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/numberOfChannels), [`sampleRate`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/sampleRate), [`timestamp`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/format), [`numberOfChannels`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/timestamp), [`format`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/format) and [`numberOfChannels`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData/numberOfChannels) as the input audio data.

### `writer?`[​](#writer)

*object* `WriterInterface`

A writer interface. The following interfaces are available:

```

Buffer writerimport {bufferWriter} from '@remotion/webcodecs/buffer';
             
(alias) const bufferWriter: WriterInterface
import bufferWriterCopy
```

Write to a resizable Array Buffer.

```

Web File System writerimport {canUseWebFsWriter, webFsWriter} from '@remotion/webcodecs/web-fs';
                               
(alias) const webFsWriter: WriterInterface
import webFsWriter
await canUseWebFsWriter(); // booleanCopy
```

Use the Web File System API to write to a file.

By default the writer is `webFsWriter`.

### `onAudioTrack?`[​](#onaudiotrack)

*Function* `ConvertMediaOnAudioTrackHandler`

Take control of what to do for each audio track in the file: Re-encoding, copying, or dropping.

See [Track Transformation](/docs/webcodecs/track-transformation) for a guide on how to use this callback.

### `onVideoTrack?`[​](#onvideotrack)

*Function* `ConvertMediaOnVideoTrackHandler`

Take control of what to do for each video track in the file: Re-encoding, copying, or dropping.

See [Track Transformation](/docs/webcodecs/track-transformation) for a guide on how to use this callback.

### `selectM3uStream?`[​](#selectm3ustream)

*Function* `SelectM3uStreamFn`

A callback that is called when a `.m3u8` file is detected which has multiple streams.

See [Stream selection](/docs/media-parser/stream-selection) for an example.

### `progressIntervalInMs?`[​](#progressintervalinms)

*number*

The interval in milliseconds at which the `onProgress` callback is called.

Default `100`. Set to `0` for unthrottled updates.

Note that updates are fired very often and updating the DOM often may slow down the conversion process.

### `seekingHints?`[​](#seekinghints)

An object that contains hints about the structure of the media file.

See [Seeking Hints](/docs/media-parser/seeking-hints) for more information.

### `fields?` and Callbacks[​](#fields-and-callbacks)

You can obtain information about the video file while you are converting it.

This feature is inherited from [`parseMedia()`](/docs/media-parser/parse-media), but only the callback-style API is available.

```

Converting a videoimport {convertMedia} from '@remotion/webcodecs';

const result = await convertMedia({
  src: 'https://remotion.media/BigBuckBunny.mp4',
  container: 'webm',
  videoCodec: 'vp8',
  audioCodec: 'opus',
  fields: {
    size: true,
  },
  onSize: (size) => {
    console.log(size);
                 
(parameter) size: number | null  },
});

const blob = await result.save();Copy
```

## License[​](#license)

[See notes about `@remotion/webcodecs`](/docs/webcodecs#-license-disclaimer).

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/convert-media.ts)

- [`@remotion/webcodecs`](/docs/webcodecs)

- [`parseMedia()`](/docs/media-parser/parse-media)
](/docs/media-parser/parse-media)](/docs/media-parser/parse-media)
](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)
- ](/docs/media-parser/parse-media)