---
title: "getSubpaths()"
url: "https://www.remotion.dev/docs/paths/get-subpaths"
path: "/docs/paths/get-subpaths"
---

"---\nimage: /generated/articles-docs-paths-get-subpaths.png\ntitle: getSubpaths()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.6_\n\nTakes an SVG path and returns an array of subpaths.\n\nEach `M` and `m` statement in a path creates a new subpath.\n\nExample of a path that has two straight lines:\n\n```tsx twoslash\nimport { getSubpaths } from \"@remotion/paths\";\n\nconst parts = getSubpaths(`\n  M 0 0 L 100 0\n  M 0 100 L 200 100\n`);\n```\n\nAn array is returned containing two parts.\n\n```tsx twoslash\nimport { getSubpaths } from \"@remotion/paths\";\n\nconst parts = getSubpaths(`\n  M 0 0 L 100 0\n  M 0 100 L 200 100\n`);\n\n// ---cut---\n\nconsole.log(parts[0]); // \"M 0 0 L 100 0\"\nconsole.log(parts[1]); // \"M 0 100 L 200 100\"\n```\n\nPaths containing relative `m` elements will be converted into `M` elements.\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-subpaths.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.6*

Takes an SVG path and returns an array of subpaths.

Each `M` and `m` statement in a path creates a new subpath.

Example of a path that has two straight lines:

```
import { getSubpaths } from "@remotion/paths";

const parts = getSubpaths(`
  M 0 0 L 100 0
  M 0 100 L 200 100
`);Copy
```

An array is returned containing two parts.

```

console.log(parts[0]); // "M 0 0 L 100 0"
console.log(parts[1]); // "M 0 100 L 200 100"Copy
```

Paths containing relative `m` elements will be converted into `M` elements.

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-subpaths.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-subpaths.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-subpaths.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-subpaths.ts)