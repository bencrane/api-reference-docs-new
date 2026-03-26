---
title: "watchStaticFile()"
url: "https://www.remotion.dev/docs/studio/watch-static-file"
path: "/docs/studio/watch-static-file"
---

"---\nimage: /generated/articles-docs-studio-watch-static-file.png\ntitle: watchStaticFile()\ncrumb: \"@remotion/studio\"\n---\n\n# watchStaticFile()<AvailableFrom v=\"4.0.144\"/>\n\nWatches for changes in a specific [static file](/docs/staticfile) and invokes a callback function when the file changes, enabling dynamic updates in your Remotion projects.\n\n:::note\nThis API is being moved from the <code>remotion</code> package.  \nPrefer this API over the old one.\n:::\n\n:::note\nThis feature is only available within the Remotion Studio environment. In the Player, events will never fire.\n:::\n\n## Example\n\n```tsx twoslash title=\"example.tsx\"\nimport { StaticFile, watchStaticFile } from \"@remotion/studio\";\n\n// Watch for changes in a specific static file\nconst { cancel } = watchStaticFile(\n  \"your-static-file.jpg\",\n  (newData: StaticFile | null) => {\n    if (newData) {\n      console.log(`File ${newData.name} has been added or modified.`);\n    } else {\n      console.log(\"File has been deleted.\");\n    }\n  },\n);\n\n// To stop watching for changes, call the cancel function\ncancel();\n```\n\n## Arguments\n\nTakes two arguments and returns a function that can be used to `cancel` the event listener.\n\n### `filename`\n\nA name of the file in `/public` folder to watch for changes.\n\n### `callback`\n\nA callback function that will be called when the file is modified. As an argument, a [`StaticFile`](/docs/getstaticfiles#api) or `null` is passed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/watch-static-file.ts)\n- [`watchPublicFolder()`](/docs/studio/watch-public-folder)\n- [`staticFile()`](/docs/staticfile)\n- [`getStaticFiles()`](/docs/studio/get-static-files)\n"

Watches for changes in a specific [static file](/docs/staticfile) and invokes a callback function when the file changes, enabling dynamic updates in your Remotion projects.
](/docs/staticfile)](/docs/staticfile)
](/docs/staticfile)
- ](/docs/staticfile)
- ](/docs/staticfile)
- ](/docs/staticfile)
- ](/docs/staticfile)