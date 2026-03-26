---
title: "makeCircle()"
url: "https://www.remotion.dev/docs/shapes/make-circle"
path: "/docs/shapes/make-circle"
---

"---\nimage: /generated/articles-docs-shapes-make-circle.png\ntitle: makeCircle()\ncrumb: \"@remotion/shapes\"\n---\n\nimport {MakeShapeSeeAlso, ShapeOptions, MakeShapeReturnType} from \"../../components/shapes/shapes-info\"\n\n_Part of the [`@remotion/shapes`](/docs/shapes) package._\n\nGenerates a circle SVG path.\n\n## Example\n\n```tsx twoslash title=\"circle.ts\"\nimport { makeCircle } from \"@remotion/shapes\";\n\nconst { path, width, height, transformOrigin } = makeCircle({ radius: 50 });\n\nconsole.log(path); // M 0 0 m -50, 0 a 50,50 0 1,0 100,0  50,50 0 1,0 -100,0\nconsole.log(width); // 100\nconsole.log(height); // 100\nconsole.log(transformOrigin); // '50 50'\n```\n\n## Arguments\n\n<ShapeOptions shape=\"circle\"/>\n\n## Return type\n\n<MakeShapeReturnType shape=\"circle\"/>\n\n## See also\n\n<MakeShapeSeeAlso shape=\"circle\"/>\n"

*Part of the [`@remotion/shapes`](/docs/shapes) package.*

Generates a circle SVG path.

## Example[​](#example)

```

circle.tsimport { makeCircle } from "@remotion/shapes";

const { path, width, height, transformOrigin } = makeCircle({ radius: 50 });

console.log(path); // M 0 0 m -50, 0 a 50,50 0 1,0 100,0  50,50 0 1,0 -100,0
console.log(width); // 100
console.log(height); // 100
console.log(transformOrigin); // '50 50'Copy
```

## Arguments[​](#arguments)

### `radius`

*number*

The radius of the circle.

## Return type[​](#return-type)

### `path`

A string that is suitable as an argument for `d` in a `<path>` element.

### `width`

The width of the circle. Suitable for defining the `viewBox` of an `<svg>` tag.

### `height`

The height of the circle. Suitable for defining the `viewBox` of an `<svg>` tag.

### `instructions`

An array with SVG instructions. The type for a instruction can be seen by importing `Instruction` from `@remotion/shapes`.

### `transformOrigin`

A string representing the point of origin if a shape should be rotated around itself.

If you want to rotate the shape around its center, use the `transform-origin` CSS property and pass this value, and also add `transform-box: fill-box`. This is the default for [`<Circle />`](/docs/shapes/circle).

## See also[​](#see-also)

- [<Circle />](/docs/shapes/circle)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-circle.ts)