---
title: "makeEllipse()"
url: "https://www.remotion.dev/docs/shapes/make-ellipse"
path: "/docs/shapes/make-ellipse"
---

"---\nimage: /generated/articles-docs-shapes-make-ellipse.png\ntitle: makeEllipse()\ncrumb: \"@remotion/shapes\"\n---\n\nimport {MakeShapeSeeAlso, ShapeOptions, MakeShapeReturnType} from \"../../components/shapes/shapes-info\"\n\n_Part of the [`@remotion/shapes`](/docs/shapes) package._\n\nGenerates an ellipse SVG path.\n\n## Example\n\n```tsx twoslash title=\"ellipse.ts\"\nimport { makeEllipse } from \"@remotion/shapes\";\n\nconst { path, width, height, transformOrigin } = makeEllipse({\n  rx: 100,\n  ry: 50,\n});\n\nconsole.log(path); // M 100 0 a 100 100 0 1 0 1 0\nconsole.log(width); // 200\nconsole.log(height); // 100\nconsole.log(transformOrigin); // '100 50'\n```\n\n## Arguments\n\n<ShapeOptions shape=\"ellipse\"/>\n\n## Return type\n\n<MakeShapeReturnType shape=\"ellipse\"/>\n\n## See also\n\n<MakeShapeSeeAlso shape=\"ellipse\"/>\n"

*Part of the [`@remotion/shapes`](/docs/shapes) package.*

Generates an ellipse SVG path.

## Example[​](#example)

```

ellipse.tsimport { makeEllipse } from "@remotion/shapes";

const { path, width, height, transformOrigin } = makeEllipse({
  rx: 100,
  ry: 50,
});

console.log(path); // M 100 0 a 100 100 0 1 0 1 0
console.log(width); // 200
console.log(height); // 100
console.log(transformOrigin); // '100 50'Copy
```

## Arguments[​](#arguments)

### `rx`

*number*

The radius of the ellipse on the X axis.

### `ry`

*number*

The radius of the ellipse on the Y axis.

## Return type[​](#return-type)

### `path`

A string that is suitable as an argument for `d` in a `<path>` element.

### `width`

The width of the ellipse. Suitable for defining the `viewBox` of an `<svg>` tag.

### `height`

The height of the ellipse. Suitable for defining the `viewBox` of an `<svg>` tag.

### `instructions`

An array with SVG instructions. The type for a instruction can be seen by importing `Instruction` from `@remotion/shapes`.

### `transformOrigin`

A string representing the point of origin if a shape should be rotated around itself.

If you want to rotate the shape around its center, use the `transform-origin` CSS property and pass this value, and also add `transform-box: fill-box`. This is the default for [`<Ellipse />`](/docs/shapes/ellipse).

## See also[​](#see-also)

- [<Ellipse />](/docs/shapes/ellipse)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-ellipse.ts)