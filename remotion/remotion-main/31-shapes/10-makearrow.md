---
title: "makeArrow()"
url: "https://www.remotion.dev/docs/shapes/make-arrow"
path: "/docs/shapes/make-arrow"
---

"---\nimage: /generated/articles-docs-shapes-make-arrow.png\ntitle: makeArrow()\ncrumb: '@remotion/shapes'\n---\n\nimport {MakeShapeSeeAlso, ShapeOptions, MakeShapeReturnType} from '../../components/shapes/shapes-info';\n\n_Part of the [`@remotion/shapes`](/docs/shapes) package._\n\nGenerates an SVG path for an arrow shape.\n\n## Example\n\n```tsx twoslash title=\"arrow.ts\"\nimport {makeArrow} from '@remotion/shapes';\n\nconst {path, width, height, transformOrigin} = makeArrow({\n  length: 300,\n  headWidth: 185,\n  headLength: 120,\n  shaftWidth: 80,\n  direction: 'right',\n});\n```\n\n## Arguments\n\n<ShapeOptions shape=\"arrow\" />\n\n## Return type\n\n<MakeShapeReturnType shape=\"arrow\" />\n\n## See also\n\n<MakeShapeSeeAlso shape=\"arrow\" />\n"

*Part of the [`@remotion/shapes`](/docs/shapes) package.*

Generates an SVG path for an arrow shape.

## Example[​](#example)

```

arrow.tsimport {makeArrow} from '@remotion/shapes';

const {path, width, height, transformOrigin} = makeArrow({
  length: 300,
  headWidth: 185,
  headLength: 120,
  shaftWidth: 80,
  direction: 'right',
});Copy
```

## Arguments[​](#arguments)

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

## Return type[​](#return-type)

### `path`

A string that is suitable as an argument for `d` in a `<path>` element.

### `width`

The width of the arrow. Suitable for defining the `viewBox` of an `<svg>` tag.

### `height`

The height of the arrow. Suitable for defining the `viewBox` of an `<svg>` tag.

### `instructions`

An array with SVG instructions. The type for a instruction can be seen by importing `Instruction` from `@remotion/shapes`.

### `transformOrigin`

A string representing the point of origin if a shape should be rotated around itself.

If you want to rotate the shape around its center, use the `transform-origin` CSS property and pass this value, and also add `transform-box: fill-box`. This is the default for [`<Arrow />`](/docs/shapes/arrow).

## See also[​](#see-also)

- [<Arrow />](/docs/shapes/arrow)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-arrow.ts)