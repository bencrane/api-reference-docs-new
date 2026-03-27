---
title: "watchPublicFolder()"
url: "https://www.remotion.dev/docs/studio/watch-public-folder"
path: "/docs/studio/watch-public-folder"
---

"---\nimage: /generated/articles-docs-studio-watch-public-folder.png\ntitle: watchPublicFolder()\ncrumb: \"@remotion/studio\"\n---\n\n# watchPublicFolder()<AvailableFrom v=\"4.0.154\"/>\n\nWatches for changes in the [public directory](/docs/terminology/public-dir) and calls a callback function when a file is added, removed or modified.\n\n:::note\nThis feature is only available within the Remotion Studio environment. In the Player, events will never fire.\n:::\n\n## Example\n\n```tsx twoslash title=\"example.tsx\"\nimport { StaticFile, watchPublicFolder } from \"@remotion/studio\";\n\n// Watch for changes in a specific static file\nconst { cancel } = watchPublicFolder((newFiles: StaticFile[]) => {\n  console.log(\"The public folder now contains:\", newFiles);\n});\n\n// To stop watching for changes, call the cancel function\ncancel();\n```\n\n## Arguments\n\nTakes one argument and returns a function that can be used to `cancel` the event listener.\n\n### `callback`\n\nA callback function that will be called when the directory is modified. As an argument, an array of [`StaticFile`](/docs/getstaticfiles#api)'s is passed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/watch-public-folder.ts)\n- [`watchStaticFile()`](/docs/studio/watch-static-file)\n- [`staticFile()`](/docs/staticfile)\n- [`getStaticFiles()`](/docs/studio/get-static-files)\n"

Watches for changes in the [public directory](/docs/terminology/public-dir) and calls a callback function when a file is added, removed or modified.
](/docs/terminology/public-dir)](/docs/terminology/public-dir)
](/docs/terminology/public-dir)
- ](/docs/terminology/public-dir)
- ](/docs/terminology/public-dir)
- ](/docs/terminology/public-dir)