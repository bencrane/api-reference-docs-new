---
title: "makePolygon()"
url: "https://www.remotion.dev/docs/shapes/make-polygon"
path: "/docs/shapes/make-polygon"
---

"---\nimage: /generated/articles-docs-shapes-make-polygon.png\ntitle: makePolygon()\ncrumb: \"@remotion/shapes\"\n---\n\nimport {MakeShapeSeeAlso, ShapeOptions, MakeShapeReturnType} from \"../../components/shapes/shapes-info\"\n\n_Part of the [`@remotion/shapes`](/docs/shapes) package._\n\nGenerates a polygon SVG path.\n\n## Example\n\n```tsx twoslash title=\"polygon.ts\"\nimport { makePolygon } from \"@remotion/shapes\";\n\nconst { path, width, height, transformOrigin, instructions } = makePolygon({\n  points: 5,\n  radius: 80,\n});\n\nconsole.log(path); // M 76.08452130361228 0 L 152.16904260722458 55.278640450004204 L 123.10734148701013 144.72135954999578 L 29.061701120214437 144.72135954999578 L 0 55.27864045000418\nconsole.log(width); // 160\nconsole.log(height); // 160\nconsole.log(transformOrigin); // '80 80'\nconsole.log(instructions); // '[{type: \"M\"}, ...]'\n```\n\n## Arguments\n\n<ShapeOptions shape=\"polygon\"/>\n\n## Return type\n\n<MakeShapeReturnType shape=\"polygon\"/>\n\n## See also\n\n<MakeShapeSeeAlso shape=\"polygon\"/>\n"

*Part of the [`@remotion/shapes`](/docs/shapes) package.*

Generates a polygon SVG path.

## Example[​](#example)

```

polygon.tsimport { makePolygon } from "@remotion/shapes";

const { path, width, height, transformOrigin, instructions } = makePolygon({
  points: 5,
  radius: 80,
});

console.log(path); // M 76.08452130361228 0 L 152.16904260722458 55.278640450004204 L 123.10734148701013 144.72135954999578 L 29.061701120214437 144.72135954999578 L 0 55.27864045000418
console.log(width); // 160
console.log(height); // 160
console.log(transformOrigin); // '80 80'
console.log(instructions); // '[{type: "M"}, ...]'Copy
```

## Arguments[​](#arguments)

### `points`

*number*

The number of points in the polygon.

### `radius`

*number*

The radius of the polygon.

### `edgeRoundness`

*number | null*

Allows to modify the shape by rounding the edges using bezier curves. Default null.

### `cornerRadius`

*number*

Rounds the corner using an arc. Similar to CSS's border-radius. Cannot be used together with edgeRoundness.

## Return type[​](#return-type)

### `path`

A string that is suitable as an argument for `d` in a `<path>` element.

### `width`

The width of the polygon. Suitable for defining the `viewBox` of an `<svg>` tag.

### `height`

The height of the polygon. Suitable for defining the `viewBox` of an `<svg>` tag.

### `instructions`

An array with SVG instructions. The type for a instruction can be seen by importing `Instruction` from `@remotion/shapes`.

### `transformOrigin`

A string representing the point of origin if a shape should be rotated around itself.

If you want to rotate the shape around its center, use the `transform-origin` CSS property and pass this value, and also add `transform-box: fill-box`. This is the default for [`<Polygon />`](/docs/shapes/polygon).

## See also[​](#see-also)

- [<Polygon />](/docs/shapes/polygon)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-polygon.ts)