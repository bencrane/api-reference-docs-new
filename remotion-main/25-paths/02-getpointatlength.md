---
title: "getPointAtLength()"
url: "https://www.remotion.dev/docs/paths/get-point-at-length"
path: "/docs/paths/get-point-at-length"
---

"---\nimage: /generated/articles-docs-paths-get-point-at-length.png\ntitle: getPointAtLength()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nGets the coordinates of a point which is on an SVG path.\nThe first argument is an SVG path, the second one is the length at which the point should be sampled. It must be between `0` and the return value of [`getLength()`](/docs/paths/get-length).\n\nAn object containing `x` and `y` is returned if the path is valid:\n\n```tsx twoslash\nimport { getPointAtLength } from \"@remotion/paths\";\n\nconst point = getPointAtLength(\"M 0 0 L 100 0\", 50);\nconsole.log(point); // { x: 50, y: 0 }\n```\n\nThe function will throw if the path is invalid:\n\n```tsx twoslash\nimport { getPointAtLength } from \"@remotion/paths\";\n// ---cut---\ngetPointAtLength(\"remotion\", 50); // Error: Malformed path data: ...\n```\n\n## Example: Getting the middle point of a path\n\nUse [`getLength()`](/docs/paths/get-length) to get the total length of a path and then multiply it with a number between 0 and 1 to get any point on the path. For example, `length * 0.5` to get the coordinates in the middle of the path.\n\n```tsx twoslash\nimport { getLength, getPointAtLength } from \"@remotion/paths\";\n\nconst path = \"M 0 0 L 100 0\";\nconst length = getLength(path);\nconst point = getPointAtLength(path, length * 0.5);\n\nconsole.log(point); // { x: 50, y: 0 }\n```\n\n## Credits\n\nSource code stems mostly from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).\n\n## See also\n\n- [getLength()](/docs/paths/get-length)\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Gets the coordinates of a point which is on an SVG path.
The first argument is an SVG path, the second one is the length at which the point should be sampled. It must be between `0` and the return value of [`getLength()`](/docs/paths/get-length).

An object containing `x` and `y` is returned if the path is valid:

```
import { getPointAtLength } from "@remotion/paths";

const point = getPointAtLength("M 0 0 L 100 0", 50);
console.log(point); // { x: 50, y: 0 }Copy
```

The function will throw if the path is invalid:

```
getPointAtLength("remotion", 50); // Error: Malformed path data: ...Copy
```

## Example: Getting the middle point of a path[​](#example-getting-the-middle-point-of-a-path)

Use [`getLength()`](/docs/paths/get-length) to get the total length of a path and then multiply it with a number between 0 and 1 to get any point on the path. For example, `length * 0.5` to get the coordinates in the middle of the path.

```
import { getLength, getPointAtLength } from "@remotion/paths";

const path = "M 0 0 L 100 0";
const length = getLength(path);
const point = getPointAtLength(path, length * 0.5);

console.log(point); // { x: 50, y: 0 }Copy
```

## Credits[​](#credits)

Source code stems mostly from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).

## See also[​](#see-also)

- [getLength()](/docs/paths/get-length)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-point-at-length.ts)