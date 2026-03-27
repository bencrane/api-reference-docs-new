---
title: "combineChunks()"
url: "https://www.remotion.dev/docs/renderer/combine-chunks"
path: "/docs/renderer/combine-chunks"
---

"---\nimage: /generated/articles-docs-renderer-combine-chunks.png\nid: combine-chunks\ntitle: combineChunks()\ncrumb: '@remotion/renderer'\n---\n\n# combineChunks()<AvailableFrom v=\"4.0.279\" />\n\nCombine multiple video or audio chunks into a single output file. This function is useful for decentralized rendering workflows where different parts of a video are rendered separately and need to be combined.\n\n[Remotion Lambda](/docs/lambda) uses this API under the hood to combine chunks that were rendered on individual Lambda functions.\n\n:::note\n**Advanced API:** This is a hard-to-use API that most people should not use directly. Misusage of this API might lead to unpredictable behavior and potential audio and video artifacts. If you want a distributed rendering solution, use [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda). If you just want to render a video with multithreading enabled, use [`renderMedia()`](/docs/renderer/render-media).\n:::\n\n## Example\n\n```tsx twoslash title=\"combine.mjs\"\nimport {combineChunks} from '@remotion/renderer';\n\n// Video files rendered as separate chunks\nconst videoFiles = ['/path/to/chunk1.mp4', '/path/to/chunk2.mp4', '/path/to/chunk3.mp4'];\n\n// Optional audio files corresponding to each video chunk\nconst audioFiles = ['/path/to/chunk1.aac', '/path/to/chunk2.aac', '/path/to/chunk3.aac'];\n\nawait combineChunks({\n  outputLocation: '/path/to/final-video.mp4',\n  videoFiles,\n  audioFiles,\n  codec: 'h264',\n  fps: 30,\n  framesPerChunk: 100,\n  audioCodec: 'aac',\n  preferLossless: false,\n  compositionDurationInFrames: 300,\n});\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `outputLocation`\n\n_string_\n\nWhere to save the output media file. Must be an absolute path.\n\n### `videoFiles`\n\n_string[]_\n\nAn array of absolute file paths pointing to the video chunks to be combined. These should be in the correct order for combining.\n\n### `audioFiles`\n\n_string[]_\n\nAn array of absolute file paths pointing to the audio chunks to be combined. These should be in the correct order for combining.\n\n### `codec`\n\n_\"h264\" | \"h265\" | \"av1\" | \"vp8\" | \"vp9\" | \"mp3\" | \"aac\" | \"wav\" | \"prores\" | \"h264-mkv\" | \"gif\"_\n\nThe codec to use for the output file. See the distributed rendering guide to see which parameter to set.\n\n### `fps`\n\n_number_\n\nThe frames per second of the video. Must be set to the `fps` value returned by [`selectComposition()`](/docs/renderer/select-composition).\n\n### `framesPerChunk`\n\n_number_\n\nThe number of frames in each chunk. All chunks must have the same number of frames, except the last one.\n\n### `audioCodec?`\n\n_\"pcm-16\" | \"aac\" | \"mp3\" | \"opus\" | null_\n\nAudio codec to use for the output file. If not specified, it will be determined based on the video codec.\n\n### `preferLossless`\n\n_boolean_\n\nMust be the same value that you passed to each [`renderMedia()`](/docs/renderer/render-media) call.\n\n### `compositionDurationInFrames`\n\n_number_\n\nThe total duration of the composition. Must be set to the `durationInFrames` value returned by [`selectComposition()`](/docs/renderer/select-composition).  \nDo not change the value, even if you use the `frameRange` or `everyNthFrame` options.\n\n### `frameRange?`\n\n_number | [number, number] | [number, null] | null_\n\nLike [`frameRange`](/docs/renderer/render-media#framerange) that you would pass to [`renderMedia()`](/docs/renderer/render-media) or [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda). The range of frames of which the video exists once all chunks are combined. Pass `[number, null]` to render from a frame to the end of the composition.<AvailableFrom v=\"4.0.421\" inline />\n\n### `everyNthFrame?`\n\n_number_\n\nLike [`everyNthFrame`](/docs/renderer/render-media#everynthframe) that you would pass to [`renderMedia()`](/docs/renderer/render-media) or [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda).\n\nMust be the same value that you passed to each [`renderMedia()`](/docs/renderer/render-media) call.\n\n### `onProgress?`\n\n_function_\n\nCallback function to track the progress of the combining operation.\n\n```tsx twoslash\nimport {CombineChunksOnProgress} from '@remotion/renderer';\n\nconst onProgress: CombineChunksOnProgress = ({totalProgress, frames}) => {\n  console.log(`Combining is ${totalProgress * 100}% complete`);\n  console.log(`Processed ${frames} frames`);\n};\n```\n\n### `audioBitrate?`\n\n_string | null_\n\nMust be the same value that you passed to each [`renderMedia()`](/docs/renderer/render-media) call.\n\n### `numberOfGifLoops?`\n\n_number | null_\n\nMust be the same value that you passed to each [`renderMedia()`](/docs/renderer/render-media) call.\n\n### `logLevel?`\n\n_\"verbose\" | \"info\" | \"warn\" | \"error\"_\n\nControls the verbosity of logging. Default is `\"info\"`.\n\n### `binariesDirectory?`\n\n_string | null_\n\nA directory containing FFmpeg binaries to use instead of the bundled or system-installed ones.\n\n### `cancelSignal?`\n\n_CancelSignal_\n\nA token that allows the combining process to be cancelled. See: [`makeCancelSignal()`](/docs/renderer/make-cancel-signal)\n\n### `metadata?`\n\nMetadata to add to the output file, in the format of key-value pairs.\n\n## Return Value\n\nThe function returns a Promise that resolves when the combining process is complete.\n\n## Compatibility\n\n<CompatibilityTable chrome={false} firefox={false} safari={false} nodejs={true} bun={true} serverlessFunctions={false} clientSideRendering={false} serverSideRendering={true} player={false} studio={false} />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/combine-chunks.ts)\n- [`renderMedia()`](/docs/renderer/render-media)\n"

Combine multiple video or audio chunks into a single output file. This function is useful for decentralized rendering workflows where different parts of a video are rendered separately and need to be combined.

[Remotion Lambda](/docs/lambda) uses this API under the hood to combine chunks that were rendered on individual Lambda functions.
](/docs/lambda)](/docs/lambda)
](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)
- ](/docs/lambda)