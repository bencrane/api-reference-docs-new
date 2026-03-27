---
title: "<Still>"
url: "https://www.remotion.dev/docs/still"
path: "/docs/still"
---

"---\nimage: /generated/articles-docs-still.png\nid: still\ntitle: <Still>\ncrumb: 'API'\n---\n\nA `<Still />` is a single-frame [`<Composition />`](/docs/composition). It is a convenient way to define a composition that renders an image rather than a video.\n\n## Example\n\nThe `<Still />` component has the same API as the [`<Composition />`](/docs/composition) component, except that it's not necessary to pass `durationInFrames` and `fps`.\n\n```tsx twoslash\n// @allowUmdGlobalAccess\n// @filename: ./MyComp.tsx\nexport const MyComp = () => <></>;\n\n// @filename: index.tsx\n// ---cut---\nimport {Composition, Still} from 'remotion';\nimport {MyComp} from './MyComp';\n\nexport const MyVideo = () => {\n  return (\n    <>\n      <Composition id=\"my-video\" component={MyComp} width={1080} height={1080} fps={30} durationInFrames={3 * 30} />\n      <Still id=\"my-image\" component={MyComp} width={1080} height={1080} />\n    </>\n  );\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={false} bun={false} serverlessFunctions={false} clientSideRendering={false} serverSideRendering player={false} studio />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Still.tsx)\n- [`<Composition />`](/docs/composition)\n"

A `<Still />` is a single-frame [`<Composition />`](/docs/composition). It is a convenient way to define a composition that renders an image rather than a video.

## Example[​](#example)

The `<Still />` component has the same API as the [`<Composition />`](/docs/composition) component, except that it's not necessary to pass `durationInFrames` and `fps`.

```
import {Composition, Still} from 'remotion';
import {MyComp} from './MyComp';

export const MyVideo = () => {
  return (
    <>
      <Composition id="my-video" component={MyComp} width={1080} height={1080} fps={30} durationInFrames={3 * 30} />
      <Still id="my-image" component={MyComp} width={1080} height={1080} />
    </>
  );
};Copy
```

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
 
 
 
 
 
 
 
 
 

## See also[​](#see-also)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Still.tsx)

- [`<Composition />`](/docs/composition)
](/docs/composition)](/docs/composition)
](/docs/composition)
- ](/docs/composition)
- ](/docs/composition)