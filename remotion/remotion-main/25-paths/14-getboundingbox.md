---
title: "getBoundingBox()"
url: "https://www.remotion.dev/docs/paths/get-bounding-box"
path: "/docs/paths/get-bounding-box"
---

"---\nimage: /generated/articles-docs-paths-get-bounding-box.png\ntitle: getBoundingBox()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40_\n\nReturns the bounding box of the given path, suitable for calculating the `viewBox` value that you need to pass to an SVG.\n\nThe bounding box is the smallest rectangle which can contain the shape in full.\n\n```tsx twoslash title=\"get-bounding-box.ts\"\nimport { getBoundingBox } from \"@remotion/paths\";\n\nconst boundingBox = getBoundingBox(\n  \"M 35,50 a 25,25,0,1,1,50,0 a 25,25,0,1,1,-50,0\"\n);\n// { x1: 35, x2: 85, y1: 24.999999999999993, y2: 75 };\n```\n\nThis function will throw if the SVG path is invalid.\n\n## Return type\n\nIncludes the following properties:\n\n- `x1`: The leftmost x coordinate of the bounding box\n- `x2`: The rightmost x coordinate of the bounding box\n- `y1`: The topmost y coordinate of the bounding box\n- `y2`: The bottommost y coordinate of the bounding box\n- `width`: The width of the bounding box, _returned from v3.3.97_\n- `height`: The height of the bounding box, _returned from v3.3.97_\n- `viewBox`: The `viewBox` value that you can pass to an SVG, _returned from v3.3.97_\n\n## `BoundingBox` type\n\nIn TypeScript, you can get the shape of the return value by importing the `BoundingBox` type:\n\n```ts twoslash\nimport type { BoundingBox } from \"@remotion/paths\";\n```\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40*

Returns the bounding box of the given path, suitable for calculating the `viewBox` value that you need to pass to an SVG.

The bounding box is the smallest rectangle which can contain the shape in full.

```

get-bounding-box.tsimport { getBoundingBox } from "@remotion/paths";

const boundingBox = getBoundingBox(
  "M 35,50 a 25,25,0,1,1,50,0 a 25,25,0,1,1,-50,0"
);
// { x1: 35, x2: 85, y1: 24.999999999999993, y2: 75 };Copy
```

This function will throw if the SVG path is invalid.

## Return type[​](#return-type)

Includes the following properties:

- `x1`: The leftmost x coordinate of the bounding box

- `x2`: The rightmost x coordinate of the bounding box

- `y1`: The topmost y coordinate of the bounding box

- `y2`: The bottommost y coordinate of the bounding box

- `width`: The width of the bounding box, *returned from v3.3.97*

- `height`: The height of the bounding box, *returned from v3.3.97*

- `viewBox`: The `viewBox` value that you can pass to an SVG, *returned from v3.3.97*

## `BoundingBox` type[​](#boundingbox-type)

In TypeScript, you can get the shape of the return value by importing the `BoundingBox` type:

```
import type { BoundingBox } from "@remotion/paths";Copy
```

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-bounding-box.ts)