---
title: "getTangentAtLength()"
url: "https://www.remotion.dev/docs/paths/get-tangent-at-length"
path: "/docs/paths/get-tangent-at-length"
---

"---\nimage: /generated/articles-docs-paths-get-tangent-at-length.png\ntitle: getTangentAtLength()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nGets tangent values `x` and `y` of a point which is on an SVG path. The first argument is an SVG path, the second one is the length at which the point should be sampled. It must be between 0 and the return value of [`getLength()`](/docs/paths/get-length).\n\nReturns a point if the path is valid:\n\n```tsx twoslash\nimport { getTangentAtLength } from \"@remotion/paths\";\n\nconst tangent = getTangentAtLength(\"M 50 50 L 150 50\", 50);\nconsole.log(tangent); // { x: 1, y: 0}\n```\n\nThe function will throw if the path is invalid:\n\n```tsx twoslash\nimport { getTangentAtLength } from \"@remotion/paths\";\n// ---cut---\ngetTangentAtLength(\"remotion\", 50); // Error: Malformed path data: ...\n```\n\n## Credits\n\nSource code stems mostly from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).\n\n## See also\n\n- [getLength()](/docs/paths/get-length)\n- [getPointAtLength()](/docs/paths/get-point-at-length)\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-tangent-at-length.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Gets tangent values `x` and `y` of a point which is on an SVG path. The first argument is an SVG path, the second one is the length at which the point should be sampled. It must be between 0 and the return value of [`getLength()`](/docs/paths/get-length).

Returns a point if the path is valid:

```
import { getTangentAtLength } from "@remotion/paths";

const tangent = getTangentAtLength("M 50 50 L 150 50", 50);
console.log(tangent); // { x: 1, y: 0}Copy
```

The function will throw if the path is invalid:

```
getTangentAtLength("remotion", 50); // Error: Malformed path data: ...Copy
```

## Credits[​](#credits)

Source code stems mostly from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).

## See also[​](#see-also)

- [getLength()](/docs/paths/get-length)

- [getPointAtLength()](/docs/paths/get-point-at-length)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-tangent-at-length.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-tangent-at-length.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-tangent-at-length.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-tangent-at-length.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-tangent-at-length.ts)