---
title: "resetPath()"
url: "https://www.remotion.dev/docs/paths/reset-path"
path: "/docs/paths/reset-path"
---

"---\nimage: /generated/articles-docs-paths-reset-path.png\ntitle: resetPath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40_\n\nTranslates an SVG path so that the top-left corner of the [bounding box](/docs/paths/get-bounding-box) is at `0, 0`. Useful for simplifying the math when transforming the coordinates of an SVG path.\n\n```tsx twoslash title=\"reset-path.ts\"\nimport { resetPath } from \"@remotion/paths\";\n\nconst newPath = resetPath(\"M 10 10 L 20 20\"); // M 0 0 L 10 10\n```\n\nThis function will throw if the SVG path is invalid.\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reset-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40*

Translates an SVG path so that the top-left corner of the [bounding box](/docs/paths/get-bounding-box) is at `0, 0`. Useful for simplifying the math when transforming the coordinates of an SVG path.

```

reset-path.tsimport { resetPath } from "@remotion/paths";

const newPath = resetPath("M 10 10 L 20 20"); // M 0 0 L 10 10Copy
```

This function will throw if the SVG path is invalid.

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reset-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reset-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reset-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reset-path.ts)