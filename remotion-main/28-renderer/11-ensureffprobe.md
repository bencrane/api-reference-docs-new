---
title: "ensureFfprobe()"
url: "https://www.remotion.dev/docs/renderer/ensure-ffprobe"
path: "/docs/renderer/ensure-ffprobe"
---

"---\nimage: /generated/articles-docs-renderer-ensure-ffprobe.png\nid: ensure-ffprobe\ntitle: ensureFfprobe()\ncrumb: '@remotion/renderer'\n---\n\n# ensureFfprobe()<AvailableFrom v=\"3.3\" />\n\n_Part of the `@remotion/renderer` package._\n_Removed from v4.0_\n\n:::warning\nThis API has been removed in v4.0 and is not necessary to call anymore. This page remains for archival purposes.\n:::\n\nChecks if the `ffprobe` binary is installed and if it is not, [downloads it and puts it into your `node_modules` folder](/docs/ffmpeg).\n\n```ts title=\"ensure.mjs\"\nimport {ensureFfprobe} from '@remotion/renderer';\n\nawait ensureFfprobe();\n```\n\nYou might not need to call this function. Remotion will automatically download `ffprobe` if a render is attempted, and no binary was found.\n\nThis function is useful if you need `ffprobe` to be ready before the first render is started.\n\nAlso call [`ensureFfmpeg()`](/docs/renderer/ensure-ffmpeg) to get both binaries that Remotion requires.\n\n## Options\n\nOptionally, you can pass an object and pass the following options:\n\n### `remotionRoot`\n\n_string_\n\nThe directory in which your `node_modules` is located.\n\n## Return value\n\nA promise which resolves an object with the following properties:\n\n- `wasAlreadyInstalled`: Boolean whether the binary was downloaded because of this function call.\n- `result`: A string, either `found-in-path`, `found-in-node-modules` or `installed`.\n\n## Exceptions\n\nThis function throws if no binary was found, the download fails or no binaries are available for your platform.\n\n## See also\n\n- CLI equivalent: [`npx remotion install ffprobe`](/docs/cli/install)\n- [`ensureFfmpeg()`](/docs/renderer/ensure-ffmpeg)\n- [Installing FFmpeg](/docs/ffmpeg)\n"

*Part of the `@remotion/renderer` package.*
*Removed from v4.0*
]()]()
]()
- ]()
- ]()
- ]()
- ]()