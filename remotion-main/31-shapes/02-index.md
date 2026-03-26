---
title: "<Rect />"
url: "https://www.remotion.dev/docs/shapes/rect"
path: "/docs/shapes/rect"
---

"---\nimage: /generated/articles-docs-shapes-rect.png\ntitle: <Rect />\ncrumb: \"@remotion/shapes\"\n---\n\nimport {ShapeSeeAlso, ShapeOptions} from \"../../components/shapes/shapes-info\"\n\n_Part of the [` @remotion/shapes`](/docs/shapes) package._\n\nRenders an SVG element containing a rectangle.\n\n## Explorer\n\n<Demo type=\"rect\"/>\n\n## Example\n\n```tsx twoslash title=\"src/Rect.tsx\"\nimport { Rect } from \"@remotion/shapes\";\nimport { AbsoluteFill } from \"remotion\";\n\nexport const MyComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: \"white\",\n        justifyContent: \"center\",\n        alignItems: \"center\",\n      }}\n    >\n      <Rect width={200} height={200} fill=\"red\" />\n    </AbsoluteFill>\n  );\n};\n```\n\n## Props\n\n<ShapeOptions shape=\"rect\" all />\n\n## See also\n\n<ShapeSeeAlso shape=\"rect\"/>\n"

*Part of the [` @remotion/shapes`](/docs/shapes) package.*

Renders an SVG element containing a rectangle.

## Explorer[​](#explorer)

width
`200`
height
`200`
cornerRadius
`0`
edgeRoundness
``
debug

## Example[​](#example)

```

src/Rect.tsximport { Rect } from "@remotion/shapes";
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
      <Rect width={200} height={200} fill="red" />
    </AbsoluteFill>
  );
};Copy
```

## Props[​](#props)

### `width`

*number*

The width of the rectangle.

### `height`

*number*

The height of the rectangle.

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

|   `0` will lead to a rotated rectangle being drawn inside the natural dimensions of the rectangle.
|   `(4 * (Math.sqrt(2) - 1)) / 3` will [draw a circle]().
|   `1` will draw a squircle.
|   Values below `0` and above `1` are possible and may result in interesting shapes. Pictured: `2` 

Cannot be used together with `cornerRadius`.

### `debug`

*boolean*

If enabled, draws the lines for Bézier curves. This is meant for debugging, note that the visuals may change in any version.

### Other props
 

All other props that can be passed to a `<path>` are accepted and will be forwarded.

## See also[​](#see-also)

- [makeRect()](/docs/shapes/rect)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/rect.tsx)