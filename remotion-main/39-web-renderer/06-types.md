---
title: "Types"
url: "https://www.remotion.dev/docs/web-renderer/types"
path: "/docs/web-renderer/types"
---

"---\nimage: /generated/articles-docs-web-renderer-types.png\nid: types\nsidebar_label: Types\ntitle: TypeScript Types Reference\nslug: /web-renderer/types\ncrumb: '@remotion/web-renderer'\n---\n\n:::warning\nExperimental feature - expect bugs and breaking changes at any time.\n[Track progress on GitHub](https://github.com/remotion-dev/remotion/issues/5913) and discuss in the [`#web-renderer`](https://remotion.dev/discord) channel on Discord.\n:::\n\nThe following types are part of the API of `@remotion/web-renderer`:\n\n## `WebRendererContainer`\n\n```tsx twoslash\nimport type {WebRendererContainer} from '@remotion/web-renderer';\n//               ^?\n```\n\nMore values may be added in the future, this would not be considered a breaking change.\n\n## `WebRendererVideoCodec`\n\n```tsx twoslash\nimport type {WebRendererVideoCodec} from '@remotion/web-renderer';\n//                ^?\n```\n\nMore values may be added in the future, this would not be considered a breaking change.\n\n## `WebRendererAudioCodec`\n\n```tsx twoslash\nimport type {WebRendererAudioCodec} from '@remotion/web-renderer';\n//                ^?\n```\n\nMore values may be added in the future, this would not be considered a breaking change.\n\n## `WebRendererQuality`\n\n```tsx twoslash\nimport type {WebRendererQuality} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `WebRendererOutputTarget`\n\n```tsx twoslash\nimport type {WebRendererOutputTarget} from '@remotion/web-renderer';\n//                ^?\n```\n\n- `'arraybuffer'`: Returns the output as a `Blob` in memory\n- `'web-fs'`: Uses the [File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API) to write to a file\n\n## `FrameRange`\n\n```tsx twoslash\nimport type {FrameRange} from '@remotion/web-renderer';\n//                ^?\n```\n\n- A single number renders only that frame\n- A tuple `[start, end]` renders frames from `start` to `end` (inclusive)\n- A tuple `[start, null]` renders frames from `start` to the end of the composition<AvailableFrom v=\"4.0.421\" inline />\n\n## `RenderStillOnWebImageFormat`\n\n```tsx twoslash\nimport type {RenderStillOnWebImageFormat} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `RenderMediaOnWebProgress`\n\n```tsx twoslash\nimport type {RenderMediaOnWebProgress} from '@remotion/web-renderer';\n//                ^?\n```\n\n### `renderedFrames`\n\nDeprecated and kept for backward compatibility. The number of frames that have been rendered.\nPrefer `progress` for overall status updates.\n\n### `encodedFrames`\n\nThe number of frames that have been encoded.\n\n### `doneIn`\n\nThe total time in milliseconds from render start until all frames were encoded, or `null` while encoding is still in progress.\n\n### `renderEstimatedTime`\n\nEstimated time remaining in milliseconds until rendering is done.\n\n### `progress`\n\nOverall progress as a number between `0` and `1`.\n\n## `RenderMediaOnWebProgressCallback`\n\n```tsx twoslash\nimport type {RenderMediaOnWebProgressCallback} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `RenderMediaOnWebResult`\n\n```tsx twoslash\nimport type {RenderMediaOnWebResult} from '@remotion/web-renderer';\n//                ^?\n```\n\n- `getBlob()`: Returns a `Promise<Blob>` containing the rendered video\n- `internalState`: Internal state object (not for public use)\n\n## `RenderMediaOnWebOptions`\n\n```tsx twoslash\nimport type {RenderMediaOnWebOptions} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `RenderStillOnWebOptions`\n\n```tsx twoslash\nimport type {RenderStillOnWebOptions} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `CanRenderMediaOnWebOptions`\n\n```tsx twoslash\nimport type {CanRenderMediaOnWebOptions} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `CanRenderMediaOnWebResult`\n\n```tsx twoslash\nimport type {CanRenderMediaOnWebResult} from '@remotion/web-renderer';\n//                ^?\n```\n\n- `canRender`: Whether the render can be performed\n- `issues`: An array of [`CanRenderIssue`](#canrenderissue) objects\n- `videoCodec`: The resolved video codec\n- `audioCodec`: The resolved audio codec\n- `outputTarget`: The resolved output target\n\n## `CanRenderIssue`\n\n```tsx twoslash\nimport type {CanRenderIssue} from '@remotion/web-renderer';\n//                ^?\n```\n\n- `type`: The type of issue (e.g., `'video-codec-unsupported'`, `'webcodecs-unavailable'`)\n- `message`: A human-readable description of the issue\n- `severity`: Either `'error'` or `'warning'`\n\n## `EmittedArtifact`\n\n```tsx twoslash\nimport type {EmittedArtifact} from '@remotion/web-renderer';\n//                ^?\n```\n\n- `filename`: The name of the artifact file\n- `content`: The content of the artifact as a `string` or `Uint8Array`\n- `frame`: The frame number at which the artifact was emitted\n- `downloadBehavior`: How the artifact should be handled for download\n\n## `WebRendererOnArtifact`\n\n```tsx twoslash\nimport type {WebRendererOnArtifact} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `OnFrameCallback`\n\n```tsx twoslash\nimport type {OnFrameCallback} from '@remotion/web-renderer';\n//                ^?\n```\n\nA callback that receives each rendered `VideoFrame` and can transform it before encoding.\n\n## `GetEncodableVideoCodecsOptions`\n\n```tsx twoslash\nimport type {GetEncodableVideoCodecsOptions} from '@remotion/web-renderer';\n//                ^?\n```\n\n## `GetEncodableAudioCodecsOptions`\n\n```tsx twoslash\nimport type {GetEncodableAudioCodecsOptions} from '@remotion/web-renderer';\n//                ^?\n```\n"
]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()