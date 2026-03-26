---
title: "normalizePath()"
url: "https://www.remotion.dev/docs/paths/normalize-path"
path: "/docs/paths/normalize-path"
---

"---\nimage: /generated/articles-docs-paths-normalize-path.png\ntitle: normalizePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nRemoves all relative coordinates from a path and converts them into absolute coordinates.\n\nReturns a string if the path is valid:\n\n```tsx twoslash\nimport { normalizePath } from \"@remotion/paths\";\n\nconst normalizedPath = normalizePath(\"M 50 50 l 100 0\");\nconsole.log(normalizedPath); // \"M 50 50 L 150 50\"\n```\n\nThe function will throw if the path is invalid:\n\n```tsx twoslash\nimport { normalizePath } from \"@remotion/paths\";\n// ---cut---\nnormalizePath(\"remotion\"); // Error: Malformed path data: ...\n```\n\n## Credits\n\nSource code stems mostly from [svg-path-reverse](https://www.npmjs.com/package/svg-path-reverse).\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [`reduceInstructions()`](/docs/paths/reduce-instructions)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/normalize-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Removes all relative coordinates from a path and converts them into absolute coordinates.

Returns a string if the path is valid:

```
import { normalizePath } from "@remotion/paths";

const normalizedPath = normalizePath("M 50 50 l 100 0");
console.log(normalizedPath); // "M 50 50 L 150 50"Copy
```

The function will throw if the path is invalid:

```
normalizePath("remotion"); // Error: Malformed path data: ...Copy
```

## Credits[​](#credits)

Source code stems mostly from [svg-path-reverse](https://www.npmjs.com/package/svg-path-reverse).

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [`reduceInstructions()`](/docs/paths/reduce-instructions)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/normalize-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/normalize-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/normalize-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/normalize-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/normalize-path.ts)