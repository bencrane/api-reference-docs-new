---
title: "renderStillOnVercel()"
url: "https://www.remotion.dev/docs/vercel/render-still-on-vercel"
path: "/docs/vercel/render-still-on-vercel"
---

"---\nimage: /generated/articles-docs-vercel-render-still-on-vercel.png\ntitle: renderStillOnVercel()\ncrumb: '@remotion/vercel'\n---\n\n# renderStillOnVercel()<AvailableFrom v=\"4.0.426\" />\n\n:::warning\nExperimental package: We reserve the right to make breaking changes in order to correct bad design decisions until this notice is gone.\n:::\n\nRenders a still image inside a Vercel Sandbox.\n\nThe rendered file stays inside the sandbox. Use [`uploadToVercelBlob()`](/docs/vercel/upload-to-vercel-blob) to upload it to Vercel Blob.\n\n## Example\n\n```ts twoslash title=\"route.ts\"\n// @module: es2022\n// @target: es2022\nimport {renderStillOnVercel, addBundleToSandbox, createSandbox} from '@remotion/vercel';\nconst sandbox = await createSandbox();\n// ---cut---\nconst {sandboxFilePath} = await renderStillOnVercel({\n  sandbox,\n  compositionId: 'MyComp',\n  inputProps: {title: 'Hello World'},\n  imageFormat: 'png',\n});\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `sandbox`\n\nA [`Sandbox`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class) instance.\n\n### `compositionId`\n\nThe ID of the Remotion composition to render.\n\n### `inputProps`\n\nProps to pass to the composition.\n\n### `imageFormat?`\n\n<Options id=\"still-image-format\" />\n\n### `outputFile?`\n\nThe output file path inside the sandbox. Default: `\"/tmp/still.png\"`.\n\n### `frame?`\n\n<Options id=\"frame\" />\n\n### `jpegQuality?`\n\n<Options id=\"jpeg-quality\" />\n\n### `envVariables?`\n\nAn object containing key-value pairs of environment variables which will be injected into your Remotion project and which can be accessed by reading the global `process.env` object. Default: `{}`.\n\n### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n### `scale?`\n\n<Options id=\"scale\" />\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\n### `timeoutInMilliseconds?`\n\n<Options id=\"timeout\" />\n\n### `offthreadVideoCacheSizeInBytes?`\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `mediaCacheSizeInBytes?`\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `offthreadVideoThreads?`\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `licenseKey?`\n\n<Options id=\"license-key\" />\n\n### `onProgress?`\n\n_function_ <TsType type=\"RenderStillOnVercelProgress\" source=\"@remotion/vercel\" href=\"/docs/vercel/types#renderstillonvercelprogress\" />\n\nA callback that receives render progress updates. Every variant includes `overallProgress` (0–1).\n\n## Return value\n\nAn object containing:\n\n### `sandboxFilePath`\n\nThe path to the rendered still image inside the sandbox.\n\n### `contentType`\n\nThe MIME type of the rendered output (e.g. `\"image/png\"`, `\"image/jpeg\"`, `\"image/webp\"`).\n\n## See also\n\n- [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel)\n- [`uploadToVercelBlob()`](/docs/vercel/upload-to-vercel-blob)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/vercel/src/render-still-on-vercel.ts)\n"

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