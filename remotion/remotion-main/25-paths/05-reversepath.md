---
title: "reversePath()"
url: "https://www.remotion.dev/docs/paths/reverse-path"
path: "/docs/paths/reverse-path"
---

"---\nimage: /generated/articles-docs-paths-reverse-path.png\ntitle: reversePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nReverses a path so the end and start are switched.\n\n```tsx twoslash\nimport { reversePath } from \"@remotion/paths\";\n\nconst reversedPath = reversePath(\"M 0 0 L 100 0\");\nconsole.log(reversedPath); // \"L 100 0 M 0 0\"\n```\n\nThe function will throw if the path is invalid:\n\n```tsx twoslash\nimport { reversePath } from \"@remotion/paths\";\n// ---cut---\nreversePath(\"remotion\"); // Error: Malformed path data: ...\n```\n\n## Credits\n\nSource code stems mostly from [svg-path-reverse](https://www.npmjs.com/package/svg-path-reverse).\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reverse-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Reverses a path so the end and start are switched.

```
import { reversePath } from "@remotion/paths";

const reversedPath = reversePath("M 0 0 L 100 0");
console.log(reversedPath); // "L 100 0 M 0 0"Copy
```

The function will throw if the path is invalid:

```
reversePath("remotion"); // Error: Malformed path data: ...Copy
```

## Credits[​](#credits)

Source code stems mostly from [svg-path-reverse](https://www.npmjs.com/package/svg-path-reverse).

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reverse-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reverse-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reverse-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reverse-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reverse-path.ts)