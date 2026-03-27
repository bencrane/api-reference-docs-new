---
title: "interpolatePath()"
url: "https://www.remotion.dev/docs/paths/interpolate-path"
path: "/docs/paths/interpolate-path"
---

"---\nimage: /generated/articles-docs-paths-interpolate-path.png\ntitle: interpolatePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nInterpolates between two SVG paths. The function takes three arguments:\n\n- `value`, which is a number.\n  - If it is `0`, the first path is returned.\n  - If it is `1`, the second path is returned.\n  - If it is inbetween or outside the range, the path is interpolated.\n- `firstPath`, which must be a valid SVG path.\n- `secondPath`, which must be a valid SVG path.\n\n```tsx twoslash\nimport { interpolatePath } from \"@remotion/paths\";\n\nconst interpolated = interpolatePath(0.5, \"M 0 0 L 100 0\", \"M 100 0 L 0 0\");\nconsole.log(interpolated); // \"M 50 0 L 50 0\"\n```\n\n## Credits\n\nSource code stems mostly from [d3-interpolate-path](https://github.com/pbeshai/d3-interpolate-path).\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/interpolate-path/interpolate-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Interpolates between two SVG paths. The function takes three arguments:

- `value`, which is a number.

- If it is `0`, the first path is returned.

- If it is `1`, the second path is returned.

- If it is inbetween or outside the range, the path is interpolated.

- `firstPath`, which must be a valid SVG path.

- `secondPath`, which must be a valid SVG path.

```
import { interpolatePath } from "@remotion/paths";

const interpolated = interpolatePath(0.5, "M 0 0 L 100 0", "M 100 0 L 0 0");
console.log(interpolated); // "M 50 0 L 50 0"Copy
```

## Credits[​](#credits)

Source code stems mostly from [d3-interpolate-path](https://github.com/pbeshai/d3-interpolate-path).

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/interpolate-path/interpolate-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/interpolate-path/interpolate-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/interpolate-path/interpolate-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/interpolate-path/interpolate-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/interpolate-path/interpolate-path.ts)