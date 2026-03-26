---
title: "<Freeze>"
url: "https://www.remotion.dev/docs/freeze"
path: "/docs/freeze"
---

"---\nimage: /generated/articles-docs-freeze.png\nid: freeze\ntitle: <Freeze>\ncrumb: 'API'\n---\n\nimport {FreezeExample} from '../components/FreezeExample/FreezeExample';\n\n```twoslash include example\nconst BlueSquare: React.FC = () => <div></div>\n// - BlueSquare\n```\n\n<AvailableFrom v=\"2.2.0\" />\n\nWhen using the `<Freeze/>` component, all of its children will freeze to the frame that you specify as a prop.\n\nIf a component is a child of `<Freeze/>`, calling the [`useCurrentFrame()`](/docs/use-current-frame) hook will always return the frame number you specify, irrespective of any [`<Sequence>`](/docs/sequence).\n\n[`<Html5Video />`](/docs/html5-video), [`<Video>`](/docs/media/video) and [`<OffthreadVideo />`](/docs/offthreadvideo) elements will be paused and [`<Html5Audio />`](/docs/html5-audio) and [`<Audio>`](/docs/media/audio) elements will render muted.\n\n## Example\n\n```tsx twoslash title=\"MyComp.tsx\"\n// @include: example-BlueSquare\n// ---cut---\nimport {Freeze} from 'remotion';\n\nconst MyVideo = () => {\n  return (\n    <Freeze frame={30}>\n      <BlueSquare />\n    </Freeze>\n  );\n};\n```\n\n## API\n\nThe Freeze component is a high order component and accepts, besides it's children, the following props:\n\n### `frame`\n\nAt which frame it's children should freeze.\n\n### `active`<AvailableFrom v=\"4.0.127\"/>\n\nDeactivate freezing component by passing `false`.  \nYou may also pass a callback function and accept the current frame and return a boolean.\n\n```tsx twoslash title=\"From frame 30 on\"\n// @include: example-BlueSquare\n// ---cut---\nimport {Freeze} from 'remotion';\n\nconst MyVideo = () => {\n  return (\n    <Freeze frame={30} active={(f) => f < 30}>\n      <BlueSquare />\n    </Freeze>\n  );\n};\n```\n\n## Demo\n\n<FreezeExample />\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/freeze.tsx)\n- [`useCurrentFrame()`](/docs/use-current-frame)\n"

[v2.2.0](https://github.com/remotion-dev/remotion/releases/v2.2.0)

When using the `<Freeze/>` component, all of its children will freeze to the frame that you specify as a prop.

If a component is a child of `<Freeze/>`, calling the [`useCurrentFrame()`](/docs/use-current-frame) hook will always return the frame number you specify, irrespective of any [`<Sequence>`](/docs/sequence).

[`<Html5Video />`](/docs/html5-video), [`<Video>`](/docs/media/video) and [`<OffthreadVideo />`](/docs/offthreadvideo) elements will be paused and [`<Html5Audio />`](/docs/html5-audio) and [`<Audio>`](/docs/media/audio) elements will render muted.

## Example[​](#example)

```

MyComp.tsximport {Freeze} from 'remotion';

const MyVideo = () => {
  return (
    <Freeze frame={30}>
      <BlueSquare />
    </Freeze>
  );
};Copy
```

## API[​](#api)

The Freeze component is a high order component and accepts, besides it's children, the following props:

### `frame`[​](#frame)

At which frame it's children should freeze.

### `active`[v4.0.127](https://github.com/remotion-dev/remotion/releases/v4.0.127)[​](#active)

Deactivate freezing component by passing `false`.

You may also pass a callback function and accept the current frame and return a boolean.

```

From frame 30 onimport {Freeze} from 'remotion';

const MyVideo = () => {
  return (
    <Freeze frame={30} active={(f) => f < 30}>
      <BlueSquare />
    </Freeze>
  );
};Copy
```

## Demo[​](#demo)

Use Freeze component

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

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/freeze.tsx)

- [`useCurrentFrame()`](/docs/use-current-frame)
](/docs/use-current-frame)](/docs/use-current-frame)
](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)