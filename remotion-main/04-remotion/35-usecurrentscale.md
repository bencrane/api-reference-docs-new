---
title: "useCurrentScale()"
url: "https://www.remotion.dev/docs/use-current-scale"
path: "/docs/use-current-scale"
---

"---\nimage: /generated/articles-docs-use-current-scale.png\ntitle: useCurrentScale()\nid: use-current-scale\ncrumb: 'API'\n---\n\n# useCurrentScale()<AvailableFrom v=\"4.0.125\" />\n\nWith this hook, you can retrieve the scale factor of the canvas.  \nUseful for if you want to [measure DOM nodes](/docs/measuring).\n\nIn the [Studio](/docs/terminology/studio), it will correspond to the zoom level - the value is `1` if the zoom is at 100%.  \nIn the [Player](/docs/terminology/player), it will correspond to the scale that is needed to fit the video canvas in the Player.\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {Sequence, useCurrentScale} from 'remotion';\n\nconst MyVideo = () => {\n  const scale = useCurrentScale();\n\n  return <div>The current scale is {scale}</div>;\n};\n```\n\nIf you are outside of a Remotion context, the hook will throw an error.  \nIf you want to avoid this error and return a default scale, you can pass an options object with the property `dontThrowIfOutsideOfRemotion` set to `true`.  \nIn this case, the hook will return `1`.\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {useCurrentScale} from 'remotion';\n\nconst MyRegularReactComponent = () => {\n  const scale = useCurrentScale({dontThrowIfOutsideOfRemotion: true});\n\n  return <div>The current scale is {scale}</div>;\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"Returns 1\" bun=\"Returns 1\" serverlessFunctions=\"Returns 1\" clientSideRendering=\"Returns 1\" serverSideRendering=\"Returns 1\" player studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-current-scale.ts)\n- [Measuring DOM nodes](/docs/measuring)\n"

With this hook, you can retrieve the scale factor of the canvas.

Useful for if you want to [measure DOM nodes](/docs/measuring).

In the [Studio](/docs/terminology/studio), it will correspond to the zoom level - the value is `1` if the zoom is at 100%.

In the [Player](/docs/terminology/player), it will correspond to the scale that is needed to fit the video canvas in the Player.

```

MyComp.tsximport {Sequence, useCurrentScale} from 'remotion';

const MyVideo = () => {
  const scale = useCurrentScale();

  return <div>The current scale is {scale}</div>;
};Copy
```

If you are outside of a Remotion context, the hook will throw an error.

If you want to avoid this error and return a default scale, you can pass an options object with the property `dontThrowIfOutsideOfRemotion` set to `true`.

In this case, the hook will return `1`.

```

MyComp.tsximport {useCurrentScale} from 'remotion';

const MyRegularReactComponent = () => {
  const scale = useCurrentScale({dontThrowIfOutsideOfRemotion: true});

  return <div>The current scale is {scale}</div>;
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
 
 
 
Returns 1 
Returns 1 
Returns 1 
Returns 1 
Returns 1 
 

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-current-scale.ts)

- [Measuring DOM nodes](/docs/measuring)
](/docs/measuring)](/docs/measuring)
](/docs/measuring)
- ](/docs/measuring)