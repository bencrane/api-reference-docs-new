---
title: "<Folder>"
url: "https://www.remotion.dev/docs/folder"
path: "/docs/folder"
---

"---\nimage: /generated/articles-docs-folder.png\ntitle: <Folder>\nid: folder\ncrumb: 'API'\n---\n\n<AvailableFrom v=\"3.0.1\" />\n\nBy wrapping a [`<Composition />`](/docs/composition) inside a `<Folder />`, you can visually categorize it in your sidebar, should you have many compositions.\n\n## Example\n\n```tsx twoslash\nimport React from 'react';\nconst Component: React.FC = () => null;\n// ---cut---\nimport {Composition, Folder} from 'remotion';\n\nexport const Video = () => {\n  return (\n    <>\n      <Folder name=\"Visuals\">\n        <Composition id=\"CompInFolder\" durationInFrames={100} fps={30} width={1080} height={1080} component={Component} />\n      </Folder>\n      <Composition id=\"CompOutsideFolder\" durationInFrames={100} fps={30} width={1080} height={1080} component={Component} />\n    </>\n  );\n};\n```\n\nwill create a tree structure in the sidebar that looks like this:\n\n<img src=\"/img/folders.png\" />\n\n## Folder behavior\n\n- They only visually change the sidebar in the Remotion Studio and have no further behavior.\n- Folder names can only contain `a-z`, `A-Z`, `0-9` and `-`.\n- Folders can be nested.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={false} bun={false} serverlessFunctions={false} clientSideRendering={false} serverSideRendering player={false} studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Folder.tsx)\n- [`<Composition />`](/docs/composition)\n"
[v3.0.1](https://github.com/remotion-dev/remotion/releases/v3.0.1)

By wrapping a [`<Composition />`](/docs/composition) inside a `<Folder />`, you can visually categorize it in your sidebar, should you have many compositions.

## Example[​](#example)

```
import {Composition, Folder} from 'remotion';

export const Video = () => {
  return (
    <>
      <Folder name="Visuals">
        <Composition id="CompInFolder" durationInFrames={100} fps={30} width={1080} height={1080} component={Component} />
      </Folder>
      <Composition id="CompOutsideFolder" durationInFrames={100} fps={30} width={1080} height={1080} component={Component} />
    </>
  );
};Copy
```

will create a tree structure in the sidebar that looks like this:

## Folder behavior[​](#folder-behavior)

- They only visually change the sidebar in the Remotion Studio and have no further behavior.

- Folder names can only contain `a-z`, `A-Z`, `0-9` and `-`.

- Folders can be nested.

## Compatibility[​](#compatibility)

|  Browsers Environments
|  
Chrome 
Firefox 
Safari 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
 

## See also[​](#see-also)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Folder.tsx)

- [`<Composition />`](/docs/composition)
](/docs/composition)](/docs/composition)
](/docs/composition)
- ](/docs/composition)
- ](/docs/composition)
- ](/docs/composition)