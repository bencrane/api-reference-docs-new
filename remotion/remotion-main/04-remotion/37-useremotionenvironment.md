---
title: "useRemotionEnvironment()"
url: "https://www.remotion.dev/docs/use-remotion-environment"
path: "/docs/use-remotion-environment"
---

"---\nimage: /generated/articles-docs-use-remotion-environment.png\ntitle: useRemotionEnvironment()\nid: use-remotion-environment\ncrumb: 'API'\n---\n\n# useRemotionEnvironment()<AvailableFrom v=\"4.0.342\" />\n\nA React hook that provides information about the current Remotion Environment. This is the preferred way to access environment information.\n\nIt returns an object with the following properties:\n\n- `isStudio`: Whether the hook got called in the [Remotion Studio](/docs/cli/studio).\n- `isRendering`: Whether the hook got called in a render.\n- `isPlayer`: Whether a [`<Player>`](/docs/player) is mounted on the current page.\n- `isReadOnlyStudio`: Whether in a [statically deployed studio](https://www.remotion.dev/docs/studio/deploy-static), where the [`@remotion/studio`](/docs/studio/api) APIs cannot be used\n- `isClientSideRendering`: Whether the function [got called in a client-side rendering context](/docs/miscellaneous/render-in-browser) (_available from v4.0.344_)\n\nThis can be useful if you want components to behave differently depending on the environment.\n\n### Example\n\n```tsx twoslash\nimport React from 'react';\nimport {useRemotionEnvironment} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const {isStudio, isPlayer, isRendering} = useRemotionEnvironment();\n\n  if (isStudio) {\n    return <div>I'm in the Studio!</div>;\n  }\n\n  if (isPlayer) {\n    return <div>I'm in the Player!</div>;\n  }\n\n  if (isRendering) {\n    return <div>I'm Rendering</div>;\n  }\n\n  return <div>Hello World!</div>;\n};\n```\n\n## Why use this hook instead of `getRemotionEnvironment()`?\n\nWhile `getRemotionEnvironment()` works for the current use cases, `useRemotionEnvironment()` is future-proof for browser rendering scenarios where preview and render might happen on the same page simultaneously.\n\nThe hook helps to scope the environment information to the context of component that calls it, rather than globally.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-remotion-environment.ts)\n- [getRemotionEnvironment()](/docs/get-remotion-environment)\n- [useVideoConfig()](/docs/use-video-config)\n- [`<OffthreadVideo/> while rendering`](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)\n"

A React hook that provides information about the current Remotion Environment. This is the preferred way to access environment information.

It returns an object with the following properties:

- `isStudio`: Whether the hook got called in the [Remotion Studio](/docs/cli/studio).

- `isRendering`: Whether the hook got called in a render.

- `isPlayer`: Whether a [`<Player>`](/docs/player) is mounted on the current page.

- `isReadOnlyStudio`: Whether in a [statically deployed studio](https://www.remotion.dev/docs/studio/deploy-static), where the [`@remotion/studio`](/docs/studio/api) APIs cannot be used

- `isClientSideRendering`: Whether the function [got called in a client-side rendering context](/docs/miscellaneous/render-in-browser) (*available from v4.0.344*)

This can be useful if you want components to behave differently depending on the environment.

### Example[​](#example)

```
import React from 'react';
import {useRemotionEnvironment} from 'remotion';

export const MyComp: React.FC = () => {
  const {isStudio, isPlayer, isRendering} = useRemotionEnvironment();

  if (isStudio) {
    return <div>I'm in the Studio!</div>;
  }

  if (isPlayer) {
    return <div>I'm in the Player!</div>;
  }

  if (isRendering) {
    return <div>I'm Rendering</div>;
  }

  return <div>Hello World!</div>;
};Copy
```

## Why use this hook instead of `getRemotionEnvironment()`?[​](#why-use-this-hook-instead-of-getremotionenvironment)

While `getRemotionEnvironment()` works for the current use cases, `useRemotionEnvironment()` is future-proof for browser rendering scenarios where preview and render might happen on the same page simultaneously.

The hook helps to scope the environment information to the context of component that calls it, rather than globally.

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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-remotion-environment.ts)

- [getRemotionEnvironment()](/docs/get-remotion-environment)

- [useVideoConfig()](/docs/use-video-config)

- [`<OffthreadVideo/> while rendering`](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)
](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)
](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)
- ](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)
- ](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)
- ](/docs/video-tags#using-a-different-tag-in-preview-and-rendering)