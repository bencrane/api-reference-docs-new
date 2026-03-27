---
title: "getStaticFiles()"
url: "https://www.remotion.dev/docs/getstaticfiles"
path: "/docs/getstaticfiles"
---

"---\nimage: /generated/articles-docs-get-static-files.png\nid: getstaticfiles\ntitle: getStaticFiles()\ncrumb: 'API'\n---\n\n<AvailableFrom v=\"3.3.26\" />\n\n:::note\nThis API is being moved to the `@remotion/studio` package. Prefer importing the API from [`@remotion/studio`](/docs/studio/get-static-files) instead of `remotion`.\n:::\n\nGets an array containing all files in the `public/` folder.  \nYou can reference them by using [`staticFile()`](/docs/staticfile).\n\n:::warning\nThis feature _only_ works in Remotion Studio and during rendering, otherwise it returns an empty array.  \n:::\n\n:::note\nOn Linux, watching for changes in subdirectories is only supported from Node.js v19.1.0. If you use a version earlier than that, you need to refresh the Remotion Studio browser tab manually.\n:::\n\n```tsx twoslash title=\"example.ts\"\nimport {getStaticFiles, StaticFile} from 'remotion';\nimport {Video} from '@remotion/media';\n\nconst files = getStaticFiles();\n/*\n[\n  {\n    \"name\": \"video.mp4\",\n    \"src\": \"/static-7n5spa/video.mp4\",\n    \"sizeInBytes\": 432944,\n    \"lastModified\": 1670170466865\n  },\n  {\n    \"name\": \"assets/data.json\",\n    \"src\": \"/static-7n5spa/assets/data.json\",\n    \"sizeInBytes\": 1311,\n    \"lastModified\": 1670170486089\n  },\n]\n*/\n\n// ❗ Don't pass the `name` directly to the `src` of a media element\nconst videoName = files[0].name;\n\n// ✅ Wrap it in staticFile() instead or use `src`\nconst videoSrc = files[0].src;\n\n// Find a file by it's name and import it\nconst data = files.find((f) => {\n  return f.name === 'video.mp4';\n}) as StaticFile; // Use `as StaticFile` to assert the file exists\n\n// Use the `src` property to get a src to pass to a media element\n<Video src={data.src} />;\n```\n\n## API\n\nTakes no arguments and returns an array of object, each of which have four entries:\n\n- `name`: The path relative to the public folder.\n  :::note\n  Contains forward slashes `/` even on Windows.\n  :::note\n\n- `src`: The path with a prefix. The prefix changes whenever the Studio server restarts.\n- `sizeInBytes`: The file size. If it is a symbolic link, the file size of the original is reported.\n- `lastModified`: Last modified date in Unix timestamp in milliseconds.\n\n## Maximum files\n\nFor performance, only the first 10000 items are fetched and displayed.\n\n**Changelog**\n\nBefore v4.0.64, only the first 1000 items were displayed.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={'Empty array'} bun={'Empty array'} serverlessFunctions={'Empty array'} clientSideRendering=\"If in Studio, otherwise empty array\" serverSideRendering player={'Empty array'} studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/get-static-files.ts)\n- [`staticFile()`](/docs/staticfile)\n- [`watchStaticFile()`](/docs/watchstaticfile)\n"
[v3.3.26](https://github.com/remotion-dev/remotion/releases/v3.3.26)

- 

`src`: The path with a prefix. The prefix changes whenever the Studio server restarts.

- 

`sizeInBytes`: The file size. If it is a symbolic link, the file size of the original is reported.

- 

`lastModified`: Last modified date in Unix timestamp in milliseconds.

## Maximum files[​](#maximum-files)

For performance, only the first 10000 items are fetched and displayed.

**Changelog**

Before v4.0.64, only the first 1000 items were displayed.

## Compatibility[​](#compatibility)

|  Browsers Servers Environments
|  
Chrome 
Firefox 
Safari 
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
Empty array 
Empty array 
Empty array 
If in Studio, otherwise empty array 
 
Empty array 

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/get-static-files.ts)

- [`staticFile()`](/docs/staticfile)

- [`watchStaticFile()`](/docs/watchstaticfile)
](/docs/watchstaticfile)](/docs/watchstaticfile)
](/docs/watchstaticfile)
- ](/docs/watchstaticfile)
- ](/docs/watchstaticfile)
- ](/docs/watchstaticfile)