---
title: "<Loop>"
url: "https://www.remotion.dev/docs/loop"
path: "/docs/loop"
---

"---\nimage: /generated/articles-docs-loop.png\nid: loop\ntitle: <Loop>\ncrumb: 'API'\n---\n\nimport {LoopExamples, BlueSquare} from '../components/LoopExamples/LoopExamples';\n\n```twoslash include example\nconst BlueSquare: React.FC = () => <div></div>\n// - BlueSquare\n```\n\n<AvailableFrom v=\"2.5.0\" />\n\nThe `<Loop />` component allows you to quickly lay out an animation so it repeats itself.\n\n```tsx twoslash title=\"MyComp.tsx\"\n// @include: example-BlueSquare\nimport {Loop} from 'remotion';\n// ---cut---\nconst MyComp = () => {\n  return (\n    <Loop durationInFrames={50} times={2}>\n      <BlueSquare />\n    </Loop>\n  );\n};\n```\n\n:::note\nGood to know: You can nest loops within each other and they will cascade.\n:::\n\n## API\n\nThe Loop component is a high order component and accepts, besides it's children, the following props:\n\n### `durationInFrames`\n\nHow many frames one iteration of the loop should be long.\n\n### `times?`\n\nHow many times to loop the content. Default: `Infinity`.\n\n### `layout?`\n\nEither `\"absolute-fill\"` or `\"none\"`. Default: `\"absolute-fill\"`.  \nBy default, your content will be absolutely positioned.  \nIf you would like to disable layout side effects, pass `layout=\"none\"`.\n\n### `style?`<AvailableFrom v=\"3.3.4\"/>\n\nCSS styles to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.\n\n## Examples\n\nAll the examples below are based on the following animation of a blue square:\n\n<LoopExamples />\n<br />\n\n```tsx twoslash\n// @include: example-BlueSquare\n// ---cut---\nconst MyComp = () => {\n  return <BlueSquare />;\n};\n```\n\n### Continuous loop\n\n<LoopExamples type=\"base\" />\n<br />\n\n```tsx twoslash\n// @include: example-BlueSquare\nimport {Loop} from 'remotion';\n// ---cut---\nconst MyComp = () => {\n  return (\n    <Loop durationInFrames={50}>\n      <BlueSquare />\n    </Loop>\n  );\n};\n```\n\n### Fixed count loop\n\n<LoopExamples type=\"times\" />\n<br />\n\n```tsx twoslash\n// @include: example-BlueSquare\nimport {Loop} from 'remotion';\n// ---cut---\nconst MyComp = () => {\n  return (\n    <Loop durationInFrames={50} times={2}>\n      <BlueSquare />\n    </Loop>\n  );\n};\n```\n\n### Nested loop\n\n<LoopExamples type=\"nested\" />\n<br />\n\n```tsx twoslash\n// @include: example-BlueSquare\nimport {Loop} from 'remotion';\n// ---cut---\nconst MyComp = () => {\n  return (\n    <Loop durationInFrames={75}>\n      <Loop durationInFrames={30}>\n        <BlueSquare />\n      </Loop>\n    </Loop>\n  );\n};\n```\n\n## `useLoop()`<AvailableFrom v=\"4.0.142\" />\n\nA child component can use the `Loop.useLoop()` hook to get information about the current loop.  \nYou should check for `null`, which is the case if the component is not inside a loop.\n\nIf inside a loop, an object with two properties is returned:\n\n- `durationInFrames`: The duration of the loop in frames as passed to the `<Loop />` component.\n- `iteration`: The current iteration of the loop, starting at 0.\n\n```tsx twoslash\nimport React from 'react';\nimport {Loop, useCurrentFrame} from 'remotion';\n\nconst LoopedVideo: React.FC = () => {\n  return (\n    <Loop durationInFrames={50} times={3} name=\"MyLoop\">\n      <Child />\n    </Loop>\n  );\n};\n\nconst Child = () => {\n  const frame = useCurrentFrame(); // 75\n  const loop = Loop.useLoop();\n\n  if (loop === null) {\n    // Not inside a loop\n  } else {\n    console.log(loop.durationInFrames); // 50\n    console.log(loop.iteration); // 1\n  }\n\n  return <div>{frame}</div>;\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/loop/index.tsx)\n- [`<Sequence>`](/docs/sequence)\n"

[v2.5.0](https://github.com/remotion-dev/remotion/releases/v2.5.0)

The `<Loop />` component allows you to quickly lay out an animation so it repeats itself.

```

MyComp.tsxconst MyComp = () => {
  return (
    <Loop durationInFrames={50} times={2}>
      <BlueSquare />
    </Loop>
  );
};Copy
```

](https://github.com/remotion-dev/remotion/releases/v2.5.0)](https://github.com/remotion-dev/remotion/releases/v2.5.0)
](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)
- ](https://github.com/remotion-dev/remotion/releases/v2.5.0)