---
title: "scalePath()"
url: "https://www.remotion.dev/docs/paths/scale-path"
path: "/docs/paths/scale-path"
---

"---\nimage: /generated/articles-docs-paths-scale-path.png\ntitle: scalePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.43_\n\nAllows you to grow or shrink the size of a path.\n\n```tsx twoslash title=\"scale-path.ts\"\nimport { scalePath } from \"@remotion/paths\";\n\nconst newPath = scalePath(\"M 0 0 L 100 100\", 1, 2); // \"M 0 0 L 100 200\";\n```\n\nThe origin of the transform is the top left corner of the path. To use a different origin, first use [`translatePath()`](/docs/paths/translate-path) to move the path to the desired origin, then scale it, and finally move it back to the original origin.\n\n## Arguments\n\n### `path`\n\n_string_\n\nA valid SVG Path string.\n\n### `xScale`\n\n_number_\n\nThe factor of which to scale the path horizontally. `1` will leave the path unchanged.\n\n### `yScale`\n\n_number_\n\nThe factor of which to scale the path vertically. `1` will leave the path unchanged.\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.43*

Allows you to grow or shrink the size of a path.

```

scale-path.tsimport { scalePath } from "@remotion/paths";

const newPath = scalePath("M 0 0 L 100 100", 1, 2); // "M 0 0 L 100 200";Copy
```

The origin of the transform is the top left corner of the path. To use a different origin, first use [`translatePath()`](/docs/paths/translate-path) to move the path to the desired origin, then scale it, and finally move it back to the original origin.

## Arguments[​](#arguments)

### `path`[​](#path)

*string*

A valid SVG Path string.

### `xScale`[​](#xscale)

*number*

The factor of which to scale the path horizontally. `1` will leave the path unchanged.

### `yScale`[​](#yscale)

*number*

The factor of which to scale the path vertically. `1` will leave the path unchanged.

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/scale-path.ts)