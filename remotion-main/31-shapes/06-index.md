---
title: "<Heart />"
url: "https://www.remotion.dev/docs/shapes/heart"
path: "/docs/shapes/heart"
---

"---\nimage: /generated/articles-docs-shapes-heart.png\ntitle: <Heart />\ncrumb: '@remotion/shapes'\n---\n\nimport {ShapeSeeAlso, ShapeOptions} from '../../components/shapes/shapes-info';\n\n_available from v4.0.315_\n\nRenders an SVG element containing a heart.\n\n## Explorer\n\n<Demo type=\"heart\" />\n\n## Example\n\n```tsx twoslash title=\"src/Heart.tsx\"\nimport {Heart} from '@remotion/shapes';\nimport {AbsoluteFill} from 'remotion';\n\nexport const MyComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: 'white',\n        justifyContent: 'center',\n        alignItems: 'center',\n      }}\n    >\n      <Heart height={100} fill=\"red\" stroke=\"black\" strokeWidth={2} />\n    </AbsoluteFill>\n  );\n};\n```\n\n## Props\n\n<ShapeOptions shape=\"heart\" all />\n\n## See also\n\n<ShapeSeeAlso shape=\"heart\" />\n"

*available from v4.0.315*

Renders an SVG element containing a heart.

## Explorer[​](#explorer)

height
`300`
aspectRatio
`1.1`
depthAdjustment
`0`
bottomRoundnessAdjustment
`0`
debug
showStrokeInsteadPlaygroundOnly

## Example[​](#example)

```

src/Heart.tsximport {Heart} from '@remotion/shapes';
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
      <Heart height={100} fill="red" stroke="black" strokeWidth={2} />
    </AbsoluteFill>
  );
};Copy
```

## Props[​](#props)

### `height`

*number*

The height of the heart.

### `aspectRatio`

*number*

The aspect ratio of the heart. Default 1.1.

### `bottomRoundnessAdjustment`

*number*

The amount of bottom roundness deviation from the default. Negative values make the bottom point sharper, positive values make it rounder.

### `depthAdjustment`

*number*

The deviation of the default depth (how deep the top of the heart is). Negative values make the heart deeper, positive values make it shallower.

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

- [makeHeart()](/docs/shapes/heart)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/heart.tsx)