---
title: "watchStaticFile()"
url: "https://www.remotion.dev/docs/watchstaticfile"
path: "/docs/watchstaticfile"
---

"---\nimage: /generated/articles-docs-watch-static-file.png\nid: watchstaticfile\ntitle: watchStaticFile()\ncrumb: \"API\"\n---\n\n# watchStaticFile()<AvailableFrom v=\"4.0.61\"/>\n\n:::note\nThis API is being moved to the `@remotion/studio` package. Prefer importing the API from [`@remotion/studio`](/docs/studio/watch-static-file) instead of `remotion`.\n:::\n\nWatches for changes in a specific [static file](/docs/staticfile) and invokes a callback function when the file changes, enabling dynamic updates in your Remotion projects.\n\n:::warning\nThis feature is only available within the Remotion Studio environment. In the Player, events will never fire.\n:::\n\n## Example\n\n```tsx twoslash title=\"example.tsx\"\nimport { StaticFile, watchStaticFile } from \"remotion\";\n\n// Watch for changes in a specific static file\nconst { cancel } = watchStaticFile(\n  \"your-static-file.jpg\",\n  (newData: StaticFile | null) => {\n    if (newData) {\n      console.log(`File ${newData.name} has been added or modified.`);\n    } else {\n      console.log(\"File has been deleted.\");\n    }\n  },\n);\n\n// To stop watching for changes, call the cancel function\ncancel();\n```\n\n## Arguments\n\nTakes two arguments and returns a function that can be used to `cancel` the event listener.\n\n### `filename`\n\nA name of the file in `/public` folder to watch for changes.\n\n### `callback`\n\nA callback function that will be called when the file is modified. As an argument, a [`StaticFile`](/docs/getstaticfiles#api) or `null` is passed.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={\"\"} bun={\"\"} serverlessFunctions=\"\" clientSideRendering={false} serverSideRendering={false} player={false} studio hideBrowsers hideServers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/watch-static-file.ts)\n- [`staticFile()`](/docs/staticfile)\n- [`getStaticFiles()`](/docs/getstaticfiles)\n"

]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()