---
title: "getLength()"
url: "https://www.remotion.dev/docs/paths/get-length"
path: "/docs/paths/get-length"
---

"---\nimage: /generated/articles-docs-paths-get-length.png\ntitle: getLength()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nGets the length of an SVG path. The argument must be a valid SVG path property.\n\nA number is returned if the path is valid:\n\n```tsx twoslash\nimport { getLength } from \"@remotion/paths\";\n\nconst length = getLength(\"M 0 0 L 100 0\");\nconsole.log(length); // 100\n```\n\nThe function will throw if the path is invalid:\n\n```tsx twoslash\nimport { getLength } from \"@remotion/paths\";\n// ---cut---\ngetLength(\"remotion\"); // Error: Malformed path data: ...\n```\n\n## Credits\n\nSource code stems mostly from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).\n\n## See also\n\n- [getPointAtLength()](/docs/paths/get-point-at-length)\n- [getTangentAtLength()](/docs/paths/get-point-at-length)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-length.ts)\n- [`@remotion/paths`](/docs/paths)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Gets the length of an SVG path. The argument must be a valid SVG path property.

A number is returned if the path is valid:

```
import { getLength } from "@remotion/paths";

const length = getLength("M 0 0 L 100 0");
console.log(length); // 100Copy
```

The function will throw if the path is invalid:

```
getLength("remotion"); // Error: Malformed path data: ...Copy
```

## Credits[​](#credits)

Source code stems mostly from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).

## See also[​](#see-also)

- [getPointAtLength()](/docs/paths/get-point-at-length)

- [getTangentAtLength()](/docs/paths/get-point-at-length)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-length.ts)

- [`@remotion/paths`](/docs/paths)
](/docs/paths)](/docs/paths)
](/docs/paths)
- ](/docs/paths)