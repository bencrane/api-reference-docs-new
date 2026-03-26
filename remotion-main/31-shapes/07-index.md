---
title: "<Star />"
url: "https://www.remotion.dev/docs/shapes/star"
path: "/docs/shapes/star"
---

"---\nimage: /generated/articles-docs-shapes-star.png\ntitle: <Star />\ncrumb: '@remotion/shapes'\n---\n\nimport {ShapeSeeAlso, ShapeOptions} from '../../components/shapes/shapes-info';\n\n_Part of the [` @remotion/shapes`](/docs/shapes) package._\n\nRenders an SVG element containing a star.\n\n## Explorer\n\n<Demo type=\"star\" />\n\n## Example\n\n```tsx twoslash title=\"src/Star.tsx\"\nimport {Star} from '@remotion/shapes';\nimport {AbsoluteFill} from 'remotion';\n\nexport const MyComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: 'white',\n        justifyContent: 'center',\n        alignItems: 'center',\n      }}\n    >\n      <Star points={5} innerRadius={100} outerRadius={200} fill=\"red\" />\n    </AbsoluteFill>\n  );\n};\n```\n\n## Props\n\n<ShapeOptions shape=\"star\" all />\n\n## See also\n\n<ShapeSeeAlso shape=\"star\" />\n"

*Part of the [` @remotion/shapes`](/docs/shapes) package.*

Renders an SVG element containing a star.

## Explorer[​](#explorer)

innerRadius
`100`
outerRadius
`200`
edgeRoundness
``
points
`5`
cornerRadius
`0`

## Example[​](#example)

```

src/Star.tsximport {Star} from '@remotion/shapes';
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
      <Star points={5} innerRadius={100} outerRadius={200} fill="red" />
    </AbsoluteFill>
  );
};Copy
```

## Props[​](#props)

### `points`

*number*

The amount of points of the star.

### `innerRadius`

*number*

The inner radius of the star.

### `outerRadius`

*number*

The outer radius of the star.

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

- [makeStar()](/docs/shapes/star)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/star.tsx)