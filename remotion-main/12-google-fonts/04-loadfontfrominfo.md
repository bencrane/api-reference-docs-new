---
title: "loadFontFromInfo()"
url: "https://www.remotion.dev/docs/google-fonts/load-font-from-info"
path: "/docs/google-fonts/load-font-from-info"
---

"---\nimage: /generated/articles-docs-google-fonts-load-font-from-info.png\ntitle: loadFontFromInfo()\ncrumb: '@remotion/google-fonts'\n---\n\n# loadFontFromInfo()<AvailableFrom v=\"4.0.279\"/>\n\nLoads a Google Font based on some metadata that was obtained using [`getInfo()`](/docs/google-fonts/get-info).\n\n[`getInfo()`](/docs/google-fonts/get-info) returns just a pure JSON object, so the metadata of a font may be loaded from a server, which can avoid having a heavy client-side bundle.\n\n```tsx twoslash title=\"On the server\"\nimport {getInfo} from '@remotion/google-fonts/InterTight';\n\n// Return `info` to the client using an endpoint\nconst info = getInfo();\n```\n\n```tsx twoslash title=\"On the client\"\nimport {getInfo} from '@remotion/google-fonts/InterTight';\nimport {loadFontFromInfo} from '@remotion/google-fonts/from-info';\n\nconst loadInfoFromServer = () => {\n  return Promise.resolve(getInfo());\n};\n\n// ---cut---\nconst info = await loadInfoFromServer();\n\nconst {fontFamily, waitUntilDone} = loadFontFromInfo(info, 'italic');\n\nconsole.log(fontFamily);\nwaitUntilDone();\n```\n\n## API\n\nThe API is the same as [`loadFont()`](/docs/google-fonts/load-font), except that another argument needs to be passed in first position, that being font metadata loaded using [`getInfo()`](/docs/google-fonts/get-info).\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {getInfo} from '@remotion/google-fonts/InterTight';\nimport {loadFontFromInfo} from '@remotion/google-fonts/from-info';\n\nconst {waitUntilDone} = loadFontFromInfo(getInfo(), 'normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n```\n\nUnlike [`loadFont()`](/docs/google-fonts/load-font), there is no autocomplete\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/google-fonts/src/from-info.ts)\n- [`loadFont()`](/docs/google-fonts/load-font)\n- [`getInfo()`](/docs/google-fonts/get-info)\n- [Building a Font Picker](/docs/font-picker)\n"

Loads a Google Font based on some metadata that was obtained using [`getInfo()`](/docs/google-fonts/get-info).

[`getInfo()`](/docs/google-fonts/get-info) returns just a pure JSON object, so the metadata of a font may be loaded from a server, which can avoid having a heavy client-side bundle.

```

On the serverimport {getInfo} from '@remotion/google-fonts/InterTight';

// Return `info` to the client using an endpoint
const info = getInfo();Copy
```

```

On the clientconst info = await loadInfoFromServer();

const {fontFamily, waitUntilDone} = loadFontFromInfo(info, 'italic');

console.log(fontFamily);
waitUntilDone();Copy
```

## API[​](#api)

The API is the same as [`loadFont()`](/docs/google-fonts/load-font), except that another argument needs to be passed in first position, that being font metadata loaded using [`getInfo()`](/docs/google-fonts/get-info).

```

MyComp.tsximport {getInfo} from '@remotion/google-fonts/InterTight';
import {loadFontFromInfo} from '@remotion/google-fonts/from-info';

const {waitUntilDone} = loadFontFromInfo(getInfo(), 'normal', {
  weights: ['400'],
  subsets: ['latin'],
});Copy
```

Unlike [`loadFont()`](/docs/google-fonts/load-font), there is no autocomplete

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/google-fonts/src/from-info.ts)

- [`loadFont()`](/docs/google-fonts/load-font)

- [`getInfo()`](/docs/google-fonts/get-info)

- [Building a Font Picker](/docs/font-picker)
](/docs/font-picker)](/docs/font-picker)
](/docs/font-picker)
- ](/docs/font-picker)