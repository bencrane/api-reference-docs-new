---
title: "getStaticFiles()"
url: "https://www.remotion.dev/docs/studio/get-static-files"
path: "/docs/studio/get-static-files"
---

"---\nimage: /generated/articles-docs-studio-get-static-files.png\ntitle: getStaticFiles()\ncrumb: '@remotion/studio'\n---\n\n# getStaticFiles()<AvailableFrom v=\"4.0.144\"/>\n\nGets an array containing all files in the `public/` folder. You can reference them by using [`staticFile()`](/docs/staticfile).\n\n:::note\nThis API is being moved from the <code>remotion</code> package.  \nPrefer this API over the old one.\n:::\n\n:::note\nIn environments outside the Remotion Studio, this API returns an empty array.  \n:::\n\n:::note\nOn Linux, watching for changes in subdirectories is only supported from Node.js v19.1.0. If you use a version earlier than that, you need to refresh the Remotion Studio browser tab manually.\n:::\n\n```tsx twoslash title=\"example.ts\"\nimport {getStaticFiles, StaticFile} from '@remotion/studio';\nimport {Video} from '@remotion/media';\n\nconst files = getStaticFiles();\n/*\n[\n  {\n    \"name\": \"video.mp4\",\n    \"src\": \"/static-7n5spa/video.mp4\",\n    \"sizeInBytes\": 432944,\n    \"lastModified\": 1670170466865\n  },\n  {\n    \"name\": \"assets/data.json\",\n    \"src\": \"/static-7n5spa/assets/data.json\",\n    \"sizeInBytes\": 1311,\n    \"lastModified\": 1670170486089\n  },\n]\n*/\n\n// ❗ Don't pass the `name` directly to the `src` of a media element\nconst videoName = files[0].name;\n\n// ✅ Wrap it in staticFile() instead or use `src`\nconst videoSrc = files[0].src;\n\n// Find a file by it's name and import it\nconst data = files.find((f) => {\n  return f.name === 'video.mp4';\n}) as StaticFile; // Use `as StaticFile` to assert the file exists\n\n// Use the `src` property to get a src to pass to a media element\n<Video src={data.src} />;\n```\n\n## API\n\nTakes no arguments and returns an array of object, each of which have four entries:\n\n- `name`: The path relative to the public folder.\n  :::note\n  Contains forward slashes `/` even on Windows.\n  :::note\n\n- `src`: The path with a prefix. The prefix changes whenever the Studio server restarts.\n- `sizeInBytes`: The file size. If it is a symbolic link, the file size of the original is reported.\n- `lastModified`: Last modified date in Unix timestamp in milliseconds.\n\n## Maximum files\n\nFor performance, only the first 10000 items are fetched and displayed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/get-static-files.ts)\n- [`staticFile()`](/docs/staticfile)\n- [`watchStaticFile()`](/docs/studio/watch-static-file)\n"

Gets an array containing all files in the `public/` folder. You can reference them by using [`staticFile()`](/docs/staticfile).

- 

`src`: The path with a prefix. The prefix changes whenever the Studio server restarts.

- 

`sizeInBytes`: The file size. If it is a symbolic link, the file size of the original is reported.

- 

`lastModified`: Last modified date in Unix timestamp in milliseconds.

## Maximum files[​](#maximum-files)

For performance, only the first 10000 items are fetched and displayed.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/get-static-files.ts)

- [`staticFile()`](/docs/staticfile)

- [`watchStaticFile()`](/docs/studio/watch-static-file)
](/docs/studio/watch-static-file)](/docs/studio/watch-static-file)
](/docs/studio/watch-static-file)
- ](/docs/studio/watch-static-file)
- ](/docs/studio/watch-static-file)