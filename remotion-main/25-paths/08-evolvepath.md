---
title: "evolvePath()"
url: "https://www.remotion.dev/docs/paths/evolve-path"
path: "/docs/paths/evolve-path"
---

"---\nimage: /generated/articles-docs-paths-evolve-path.png\ntitle: evolvePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nAnimates an SVG path from being invisible to it's full length. The function takes two arguments:\n\n- `progress` is the progress towards full evolution, where `0` means the path being invisible, and `1` meaning the path being fully drawn out.\n  :::note\n  Passing in a value above 1 will result in the start of the path getting devolved. Passing in a value below 0 will result in the path getting evolved from the end.\n  :::\n\n- `path` must be a valid SVG path.\n\nThe return value will be an object containing [`strokeDasharray`](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dasharray) and [`strokeDashoffset`](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dashoffset) values, which should be passed to the `<path>` element.\n\n```tsx twoslash\nimport { evolvePath } from \"@remotion/paths\";\n\nconst path = \"M 0 0 L 100 0\";\nconst evolution = evolvePath(0.5, path);\nconsole.log(evolution); // { strokeDasharray: '100 100',  strokeDashoffset: 50 }\n\nconst element = (\n  <path\n    d={path}\n    strokeDasharray={evolution.strokeDasharray}\n    strokeDashoffset={evolution.strokeDashoffset}\n  />\n);\n```\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [reversePath()](/docs/paths/reverse-path)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/evolve-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Animates an SVG path from being invisible to it's full length. The function takes two arguments:

- 

`progress` is the progress towards full evolution, where `0` means the path being invisible, and `1` meaning the path being fully drawn out.

- 

`path` must be a valid SVG path.

The return value will be an object containing [`strokeDasharray`](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dasharray) and [`strokeDashoffset`](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-dashoffset) values, which should be passed to the `<path>` element.

```
import { evolvePath } from "@remotion/paths";

const path = "M 0 0 L 100 0";
const evolution = evolvePath(0.5, path);
console.log(evolution); // { strokeDasharray: '100 100',  strokeDashoffset: 50 }

const element = (
  <path
    d={path}
    strokeDasharray={evolution.strokeDasharray}
    strokeDashoffset={evolution.strokeDashoffset}
  />
);Copy
```

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [reversePath()](/docs/paths/reverse-path)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/evolve-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/evolve-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/evolve-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/evolve-path.ts)