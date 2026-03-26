---
title: "<Ellipse />"
url: "https://www.remotion.dev/docs/shapes/ellipse"
path: "/docs/shapes/ellipse"
---

"---\nimage: /generated/articles-docs-shapes-ellipse.png\ntitle: <Ellipse />\ncrumb: \"@remotion/shapes\"\n---\n\nimport {ShapeSeeAlso, ShapeOptions} from \"../../components/shapes/shapes-info\"\n\n_Part of the [` @remotion/shapes`](/docs/shapes) package._\n\nRenders an SVG element drawing an ellipse.\n\n## Explorer\n\n<Demo type=\"ellipse\" />\n\n## Example\n\n```tsx twoslash title=\"src/Ellipse.tsx\"\nimport { Ellipse } from \"@remotion/shapes\";\nimport { AbsoluteFill } from \"remotion\";\n\nexport const MyComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: \"white\",\n        justifyContent: \"center\",\n        alignItems: \"center\",\n      }}\n    >\n      <Ellipse rx={100} ry={50} fill=\"green\" stroke=\"red\" strokeWidth={1} />\n    </AbsoluteFill>\n  );\n};\n```\n\n## Props\n\n<ShapeOptions shape=\"ellipse\" all />\n\n## See also\n\n<ShapeSeeAlso shape=\"ellipse\"/>\n"

*Part of the [` @remotion/shapes`](/docs/shapes) package.*

Renders an SVG element drawing an ellipse.

## Explorer[​](#explorer)

rx
`150`
ry
`200`

## Example[​](#example)

```

src/Ellipse.tsximport { Ellipse } from "@remotion/shapes";
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
      <Ellipse rx={100} ry={50} fill="green" stroke="red" strokeWidth={1} />
    </AbsoluteFill>
  );
};Copy
```

## Props[​](#props)

### `rx`

*number*

The radius of the ellipse on the X axis.

### `ry`

*number*

The radius of the ellipse on the Y axis.

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

- [makeEllipse()](/docs/shapes/ellipse)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/components/ellipse.tsx)