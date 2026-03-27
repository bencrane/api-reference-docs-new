---
title: "<AbsoluteFill>"
url: "https://www.remotion.dev/docs/absolute-fill"
path: "/docs/absolute-fill"
---

"---\nimage: /generated/articles-docs-absolute-fill.png\nid: absolute-fill\ntitle: <AbsoluteFill>\ncrumb: 'API'\n---\n\nA helper component - it is an absolutely positioned `<div>` with the following styles:\n\n```ts twoslash title=\"Styles of AbsoluteFill\"\nimport React from 'react';\n// ---cut---\nconst style: React.CSSProperties = {\n  position: 'absolute',\n  top: 0,\n  left: 0,\n  right: 0,\n  bottom: 0,\n  width: '100%',\n  height: '100%',\n  display: 'flex',\n  flexDirection: 'column',\n};\n```\n\nThis component is useful for layering content on top of each other. For example, you can use it to create a full-screen video background:\n\n```tsx twoslash title=\"Layer example\"\nimport {AbsoluteFill, OffthreadVideo} from 'remotion';\n\nconst MyComp = () => {\n  return (\n    <AbsoluteFill>\n      <AbsoluteFill>\n        <OffthreadVideo src=\"https://example.com/video.mp4\" />\n      </AbsoluteFill>\n      <AbsoluteFill>\n        <h1>This text is written on top!</h1>\n      </AbsoluteFill>\n    </AbsoluteFill>\n  );\n};\n```\n\nThe layers that get rendered last appear on top - this is because of how HTML works.\n\n## Adding a ref\n\nYou can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to an `<AbsoluteFill>` from version `v3.2.13` on. If you use TypeScript, you need to type it with `HTMLDivElement`:\n\n```tsx twoslash\nimport {useRef} from 'react';\nimport {AbsoluteFill} from 'remotion';\n\nconst content = <div>Hello, World</div>;\n// ---cut---\nconst MyComp = () => {\n  const ref = useRef<HTMLDivElement>(null);\n  return <AbsoluteFill ref={ref}>{content}</AbsoluteFill>;\n};\n```\n\n## TailwindCSS class detection<AvailableFrom v=\"4.0.249\" />\n\nThis component has a `style` object, which has higher importance than `className`'s.\n\nIn order to make this behave like you expect (row layout):\n\n```tsx\n<AbsoluteFill className=\"flex flex-row\" />\n```\n\nWe detect conflicting Tailwind classes and disable the corresponding inline styles if they are present from Remotion v4.0.249.  \nReview the source code below to see how we detect Tailwind classes.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers/>\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)\n"

A helper component - it is an absolutely positioned `<div>` with the following styles:

```

Styles of AbsoluteFillconst style: React.CSSProperties = {
  position: 'absolute',
  top: 0,
  left: 0,
  right: 0,
  bottom: 0,
  width: '100%',
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
};Copy
```

This component is useful for layering content on top of each other. For example, you can use it to create a full-screen video background:

```

Layer exampleimport {AbsoluteFill, OffthreadVideo} from 'remotion';

const MyComp = () => {
  return (
    <AbsoluteFill>
      <AbsoluteFill>
        <OffthreadVideo src="https://example.com/video.mp4" />
      </AbsoluteFill>
      <AbsoluteFill>
        <h1>This text is written on top!</h1>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};Copy
```

The layers that get rendered last appear on top - this is because of how HTML works.

## Adding a ref[​](#adding-a-ref)

You can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to an `<AbsoluteFill>` from version `v3.2.13` on. If you use TypeScript, you need to type it with `HTMLDivElement`:

```
const MyComp = () => {
  const ref = useRef<HTMLDivElement>(null);
  return <AbsoluteFill ref={ref}>{content}</AbsoluteFill>;
};Copy
```

## TailwindCSS class detection[v4.0.249](https://github.com/remotion-dev/remotion/releases/v4.0.249)[​](#tailwindcss-class-detection)

This component has a `style` object, which has higher importance than `className`'s.

In order to make this behave like you expect (row layout):

```
<AbsoluteFill className="flex flex-row" />Copy
```

We detect conflicting Tailwind classes and disable the corresponding inline styles if they are present from Remotion v4.0.249.

Review the source code below to see how we detect Tailwind classes.

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

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/AbsoluteFill.tsx)