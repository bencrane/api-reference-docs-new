---
title: "staticFile()"
url: "https://www.remotion.dev/docs/staticfile"
path: "/docs/staticfile"
---

"---\nimage: /generated/articles-docs-staticfile.png\nid: staticfile\ntitle: staticFile()\ncrumb: 'API'\n---\n\n<AvailableFrom v=\"2.5.7\" />\n\nTurns a file in your `public/` folder into an URL which you can then load into your project.\n\n```tsx twoslash\nimport {Img, staticFile} from 'remotion';\n\nconst myImage = staticFile(`/my-image.png`);\n\n// ...\n\n<Img src={myImage} />;\n```\n\n## Example\n\nStart by creating a `public/` folder in the root of your video project:\n\n```txt\nmy-video/\n├─ node_modules/\n├─ public/\n│  ├─ my-image.png\n│  ├─ font.woff2\n├─ src/\n│  ├─ Root.tsx\n│  ├─ index.ts\n├─ package.json\n```\n\n:::info\nThe `public/` folder should always be in the same folder as your `package.json` that contains the `remotion` dependency, even if your Remotion code lives in a subdirectory.\n:::\n\nGet an URL reference of your asset:\n\n```tsx twoslash\nimport {staticFile} from 'remotion';\n\nconst myImage = staticFile(`/my-image.png`); // \"/static-32e8nd/my-image.png\"\nconst font = staticFile(`/font.woff2`); // \"/static-32e8nd/font.woff2\"\n```\n\nYou can now load the asset via:\n\n- [`<Img>`](/docs/img), [`<Audio>`](/docs/media/audio), [`<Video>`](/docs/media/video), [`<OffthreadVideo>`](/docs/offthreadvideo), [`<Html5Audio>`](/docs/html5-audio), [`<Html5Video>`](/docs/html5-video) tags\n- Fetch API\n- [FontFace()](/docs/fonts)\n- Any other loader that supports data fetching via URL\n\n## Why can't I just pass a string?\n\nIf you are a Create React App or Next.JS user, you might be used to just to be able to reference the asset from a string: `<img src=\"/my-image.png\"/>`. Remotion chooses to be different in that you need to use the `staticFile()` API because:\n\n- It prevents breaking when deploying your site into a subdirectory of a domain: `https://example.com/my-folder/my-logo.png`\n- It avoids conflicts with composition names which might share the same name (for example `http://localhost:3000/conflicting-name` while running the studio)\n- It allows us to make paths framework-agnostic, so your code can work across Remotion, Create React App, Next.JS and potentially other frameworks.\n\n## Getting all files in the public folder\n\nUse the [`getStaticFiles()`](/docs/getstaticfiles) API to get a list of available options.\n\n## Handling URI-unsafe characters<AvailableFrom v=\"4.0.0\"/>\n\nSince `v4.0`, `staticFile()` encodes the filename using `encodeURIComponent`.  \nIf you encoded the path by yourself until now, make sure to drop your encoding before passing the path into `staticFile()` to avoid double encoding.\n\nBefore `v4.0`, `staticFile()` did not handle URI-unsafe characters contained in the provided path. This could lead to problems in some cases when filenames would contain characters such as `#`, `?` and or `&`.\n\n### Example\n\n```tsx title=\"Before v4\"\nstaticFile('my-image#portrait.png'); //output: \"/my-image#portrait.png\"\n```\n\nIf this URL is passed to a component accepting an URL, the part after `#` will be left out, leading\nto an error because the file can't be found.\n\n```tsx title=\"Since v4.0.0\"\nstaticFile('my-image#portrait.png'); // \"/my-image%23portrait.png\"\n```\n\nThe image will now be loaded properly, however, you must avoid to encode the filename yourself.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"Uses / as prefix\" bun=\"Uses / as prefix\" serverlessFunctions=\"Uses / as prefix\" clientSideRendering serverSideRendering player=\"Uses / as prefix\" studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/static-file.ts)\n- [Loading assets](/docs/assets)\n- [`getStaticFiles()`](/docs/getstaticfiles)\n- [`watchStaticFile()`](/docs/watchstaticfile)\n"
[v2.5.7](https://github.com/remotion-dev/remotion/releases/v2.5.7)

Turns a file in your `public/` folder into an URL which you can then load into your project.

```
import {Img, staticFile} from 'remotion';

const myImage = staticFile(`/my-image.png`);

// ...

<Img src={myImage} />;Copy
```

## Example[​](#example)

Start by creating a `public/` folder in the root of your video project:

```
my-video/
├─ node_modules/
├─ public/
│  ├─ my-image.png
│  ├─ font.woff2
├─ src/
│  ├─ Root.tsx
│  ├─ index.ts
├─ package.jsonCopy
```

](#example)](#example)
](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)