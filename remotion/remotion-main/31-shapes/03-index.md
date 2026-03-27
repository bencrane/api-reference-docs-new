---
title: "<Triangle />"
url: "https://www.remotion.dev/docs/shapes/triangle"
path: "/docs/shapes/triangle"
---

"---\nimage: /generated/articles-docs-shapes-triangle.png\ntitle: <Triangle />\ncrumb: \"@remotion/shapes\"\n---\n\nimport {ShapeSeeAlso, ShapeOptions} from \"../../components/shapes/shapes-info\"\n\n_Part of the [` @remotion/shapes`](/docs/shapes) package._\n\nRenders an SVG element containing a triangle with same length on all sides.\n\n## Explorer\n\n<Demo type=\"triangle\" />\n\n## Example\n\n```tsx twoslash title=\"src/Triangle.tsx\"\nimport { Triangle } from \"@remotion/shapes\";\nimport { AbsoluteFill } from \"remotion\";\n\nexport const MyComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: \"white\",\n        justifyContent: \"center\",\n        alignItems: \"center\",\n      }}\n    >\n      <Triangle length={100} fill=\"red\" direction=\"left\" />\n    </AbsoluteFill>\n  );\n};\n```\n\n## Props\n\n<ShapeOptions shape=\"triangle\" all />\n\n## See also\n\n<ShapeSeeAlso shape=\"triangle\"/>\n"

*Part of the [` @remotion/shapes`](/docs/shapes) package.*

Renders an SVG element containing a triangle with same length on all sides.

## Explorer[​](#explorer)

length
`200`
edgeRoundness
``
cornerRadius
`0`
direction
updownleftright
debug

## Example[​](#example)

```

src/Triangle.tsximport { Triangle } from "@remotion/shapes";
import { AbsoluteFill } from "remotion";

export const MyComposition = () => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "white",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Triangle length={100} fill="red" direction="left" />
    </AbsoluteFill>
  );
};Copy
```

## Props[​](#props)

### `length`

*number*

The length of one triangle side.

### `direction`

*"left" | "right" | "up" | "down"*

The direction of the triangle.

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

### `cornerRadius`

*number*

Rounds the corner using an arc. Similar to CSS's `border-radius`. Cannot be used together with `edgeRoundness`.

### `edgeRoundness`

*null | number*

Allows to modify the shape by rounding the edges using bezier curves. Default `null`.

|   `0` will lead to a rotated triangle being drawn inside the natural dimensions of the triangle.
|   `Math.sqrt(2) - 1` will [draw a circle]().
|   `1` will draw a shape similar to a "squircle" but as a triangle.
|   Values below `0` and above `1` may result in other interesting shapes. Pictured: `2`. 

Cannot be used together with `cornerRadius`.

### `debug`

*boolean*

If enabled, draws the lines for Bézier curves. This is meant for debugging, note that the visuals may change in any version.

### Other props
 

All other props that can be passed to a `<path>` are accepted and will be forwarded.

## See also[​](#see-also)

- [makeTriangle()](/docs/shapes/triangle)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/triangle.tsx)