---
title: "uploadToVercelBlob()"
url: "https://www.remotion.dev/docs/vercel/upload-to-vercel-blob"
path: "/docs/vercel/upload-to-vercel-blob"
---

"---\nimage: /generated/articles-docs-vercel-upload-to-vercel-blob.png\ntitle: uploadToVercelBlob()\ncrumb: '@remotion/vercel'\n---\n\n# uploadToVercelBlob()<AvailableFrom v=\"4.0.426\" />\n\n:::warning\nExperimental package: We reserve the right to make breaking changes in order to correct bad design decisions until this notice is gone.\n:::\n\nUploads a file from the sandbox to [Vercel Blob](https://vercel.com/docs/storage/vercel-blob) storage. Typically used after [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel) or [`renderStillOnVercel()`](/docs/vercel/render-still-on-vercel) to make the output publicly accessible.\n\n## Example\n\n```ts twoslash title=\"route.ts\"\n// @module: es2022\n// @target: es2022\nimport {uploadToVercelBlob, addBundleToSandbox, createSandbox} from '@remotion/vercel';\nconst sandbox = await createSandbox();\nawait addBundleToSandbox({sandbox, bundleDir: '/path/to/bundle'});\n// ---cut---\nconst {url, size} = await uploadToVercelBlob({\n  sandbox,\n  sandboxFilePath: '/tmp/video.mp4',\n  contentType: 'video/mp4',\n  blobToken: process.env.BLOB_READ_WRITE_TOKEN!,\n  access: 'public',\n});\n\nconsole.log(`Uploaded ${size} bytes to ${url}`);\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `sandbox`\n\nA [`Sandbox`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class) instance.\n\n### `sandboxFilePath`\n\nThe path to the file inside the sandbox to upload, e.g. `\"/tmp/video.mp4\"`.\n\n### `blobPath?`\n\nThe destination path in Vercel Blob, e.g. `\"renders/abc.mp4\"`. If omitted, a random path is generated.\n\n### `contentType`\n\nThe MIME type of the file, e.g. `\"video/mp4\"` or `\"image/png\"`.\n\n### `blobToken`\n\nYour Vercel Blob read/write token. Typically `process.env.BLOB_READ_WRITE_TOKEN`.\n\n### `access`\n\n<TsType type=\"VercelBlobAccess\" source=\"@remotion/vercel\" href=\"/docs/vercel/types#vercelblobaccess\" />\n\nThe access level of the uploaded blob. Either `\"public\"` or `\"private\"`. Default: `\"private\"`.\n\n## Return value\n\nAn object containing:\n\n### `url`\n\nThe public download URL of the uploaded file.\n\n### `size`\n\nThe size of the uploaded file in bytes.\n\n## See also\n\n- [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel)\n- [`renderStillOnVercel()`](/docs/vercel/render-still-on-vercel)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/vercel/src/upload-to-vercel-blob.ts)\n"

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