---
title: "makePie()"
url: "https://www.remotion.dev/docs/shapes/make-pie"
path: "/docs/shapes/make-pie"
---

"---\nimage: /generated/articles-docs-shapes-make-pie.png\ntitle: makePie()\ncrumb: \"@remotion/shapes\"\n---\n\nimport {MakeShapeSeeAlso, ShapeOptions, MakeShapeReturnType} from \"../../components/shapes/shapes-info\"\n\n_Part of the [`@remotion/shapes`](/docs/shapes) package._\n\nGenerates a piece of pie SVG path.\n\n## Example\n\n```tsx twoslash title=\"pie.ts\"\nimport { makePie } from \"@remotion/shapes\";\n\nconst { path, width, height, transformOrigin } = makePie({\n  radius: 100,\n  progress: 0.5,\n});\n\nconsole.log(path); // M 100 0 A 100 100 0 0 1 100 200 L 100 100 z\nconsole.log(width); // 200\nconsole.log(height); // 200\nconsole.log(transformOrigin); // '100 100'\n```\n\n## Arguments\n\n<ShapeOptions shape=\"pie\"/>\n\n## Return type\n\n<MakeShapeReturnType shape=\"pie\"/>\n\n## See also\n\n<MakeShapeSeeAlso shape=\"pie\"/>\n"

*Part of the [`@remotion/shapes`](/docs/shapes) package.*

Generates a piece of pie SVG path.

## Example[​](#example)

```

pie.tsimport { makePie } from "@remotion/shapes";

const { path, width, height, transformOrigin } = makePie({
  radius: 100,
  progress: 0.5,
});

console.log(path); // M 100 0 A 100 100 0 0 1 100 200 L 100 100 z
console.log(width); // 200
console.log(height); // 200
console.log(transformOrigin); // '100 100'Copy
```

## Arguments[​](#arguments)

### `radius`

*number*

The radius of the circle.

### `progress`

*number*

The percentage of the circle that is filled. `0` means fully empty, `1` means fully filled.

### `counterClockwise`

*boolean*

If set, the circle gets filled counterclockwise instead of clockwise. Default false.

### `closePath`

*boolean*

If set to `false`, no path to the middle of the circle will be drawn, leading to an open arc. Default `true`.

### `rotation`

*number*

Add rotation to the path. `0` means no rotation, `Math.PI * 2` means 1 full clockwise rotation 

## Return type[​](#return-type)

### `path`

A string that is suitable as an argument for `d` in a `<path>` element.

### `width`

The width of the pie. Suitable for defining the `viewBox` of an `<svg>` tag.

### `height`

The height of the pie. Suitable for defining the `viewBox` of an `<svg>` tag.

### `instructions`

An array with SVG instructions. The type for a instruction can be seen by importing `Instruction` from `@remotion/shapes`.

### `transformOrigin`

A string representing the point of origin if a shape should be rotated around itself.

If you want to rotate the shape around its center, use the `transform-origin` CSS property and pass this value, and also add `transform-box: fill-box`. This is the default for [`<Pie />`](/docs/shapes/pie).

## See also[​](#see-also)

- [<Pie />](/docs/shapes/pie)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-pie.ts)