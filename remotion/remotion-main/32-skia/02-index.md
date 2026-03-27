---
title: "<SkiaCanvas />"
url: "https://www.remotion.dev/docs/skia/skia-canvas"
path: "/docs/skia/skia-canvas"
---

"---\nimage: /generated/articles-docs-skia-skia-canvas.png\ntitle: <SkiaCanvas />\ncrumb: \"@remotion/skia\"\n---\n\nA [React Native Skia `<Canvas />` component](https://shopify.github.io/react-native-skia/docs/canvas/overview) that wraps Remotion contexts.\n\nYou can place elements from `@shopify/react-native-skia` in it!\n\n```tsx twoslash\nimport { SkiaCanvas } from \"@remotion/skia\";\nimport { Fill } from \"@shopify/react-native-skia\";\nimport React from \"react\";\nimport { useVideoConfig } from \"remotion\";\n\nconst MySkiaVideo: React.FC = () => {\n  const { width, height } = useVideoConfig();\n  return (\n    <SkiaCanvas width={width} height={height}>\n      <Fill color=\"black\" />\n    </SkiaCanvas>\n  );\n};\n```\n\n## Props\n\n### `width`\n\nThe width of the canvas in pixels.\n\n### `height`\n\nThe height of the canvas in pixels.\n\n### Inherited props\n\nAll the props that are accepted by [`<Canvas>`](https://shopify.github.io/react-native-skia/docs/canvas/overview) are accepted as well.\n\n## See also\n\n- [Installation](/docs/skia)\n"

A [React Native Skia `<Canvas />` component](https://shopify.github.io/react-native-skia/docs/canvas/overview) that wraps Remotion contexts.

You can place elements from `@shopify/react-native-skia` in it!

```
import { SkiaCanvas } from "@remotion/skia";
import { Fill } from "@shopify/react-native-skia";
import React from "react";
import { useVideoConfig } from "remotion";

const MySkiaVideo: React.FC = () => {
  const { width, height } = useVideoConfig();
  return (
    <SkiaCanvas width={width} height={height}>
      <Fill color="black" />
    </SkiaCanvas>
  );
};Copy
```

## Props[​](#props)

### `width`[​](#width)

The width of the canvas in pixels.

### `height`[​](#height)

The height of the canvas in pixels.

### Inherited props[​](#inherited-props)

All the props that are accepted by [`<Canvas>`](https://shopify.github.io/react-native-skia/docs/canvas/overview) are accepted as well.

## See also[​](#see-also)

- [Installation](/docs/skia)
](/docs/skia)](/docs/skia)
](/docs/skia)
- ](/docs/skia)
- ](/docs/skia)
- ](/docs/skia)
- ](/docs/skia)