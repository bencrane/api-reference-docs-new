---
title: "<Arrow />"
url: "https://www.remotion.dev/docs/shapes/arrow"
path: "/docs/shapes/arrow"
---

"---\nimage: /generated/articles-docs-shapes-arrow.png\ntitle: <Arrow />\ncrumb: '@remotion/shapes'\n---\n\nimport {ShapeSeeAlso, ShapeOptions} from '../../components/shapes/shapes-info';\n\n_Part of the [`@remotion/shapes`](/docs/shapes) package._\n\nRenders an SVG element containing an arrow shape.\n\n## Explorer\n\n<Demo type=\"arrow\" />\n\n## Example\n\n```tsx twoslash title=\"src/Arrow.tsx\"\nimport {Arrow} from '@remotion/shapes';\nimport {AbsoluteFill} from 'remotion';\n\nexport const MyComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: 'white',\n        justifyContent: 'center',\n        alignItems: 'center',\n      }}\n    >\n      <Arrow length={300} headWidth={185} headLength={120} shaftWidth={80} fill=\"red\" direction=\"right\" />\n    </AbsoluteFill>\n  );\n};\n```\n\n## Props\n\n<ShapeOptions shape=\"arrow\" all />\n\n## See also\n\n<ShapeSeeAlso shape=\"arrow\" />\n"

*Part of the [`@remotion/shapes`](/docs/shapes) package.*

Renders an SVG element containing an arrow shape.

## Explorer[​](#explorer)

length
`300`
headWidth
`185`
headLength
`120`
shaftWidth
`80`
direction
updownleftright
cornerRadius
`0`

## Example[​](#example)

```

src/Arrow.tsximport {Arrow} from '@remotion/shapes';
import {AbsoluteFill} from 'remotion';

export const MyComposition = () => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <Arrow length={300} headWidth={185} headLength={120} shaftWidth={80} fill="red" direction="right" />
    </AbsoluteFill>
  );
};Copy
```

## Props[​](#props)

### `length`

*number*

The total length of the arrow along its direction axis. Default 300.

### `headWidth`

*number*

The width of the arrowhead at its widest point. Default 185.

### `headLength`

*number*

The length of the arrowhead portion. Default 120.

### `shaftWidth`

*number*

The width of the arrow shaft. Default 80.

### `direction`

*"left" | "right" | "up" | "down"*

The direction the arrow points. Default right.

### `cornerRadius`

*number*

Rounds the corner using an arc. Similar to CSS's border-radius.

### `fill`

*string*

The color of the shape.

### `stroke`

*string*

The color of the stroke. Should be used together with `strokeWidth`.

### `strokeWidth`

*string*

The width of the stroke. Should be used together with `stroke`.

### `style`

*string*

CSS properties that will be applied to the `<svg>` tag. Default style: `overflow: 'visible'`

### `pathStyle`

*string*

CSS properties that will be applied to the `<path>` tag. Default style: `transform-box: 'fill-box'` and a dynamically calculated `transform-origin` which is the center of the shape, so that the shape rotates around its center by default.

### `strokeDasharray`

*string*

Allows to animate a path. See [evolvePath()](/docs/paths/evolve-path) for an example.

### `strokeDashoffset`

*string*

Allows to animate a path. See [evolvePath()](/docs/paths/evolve-path) for an example.

### Other props
 

All other props that can be passed to a `<path>` are accepted and will be forwarded.

## See also[​](#see-also)

- [makeArrow()](/docs/shapes/arrow)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/arrow.tsx)