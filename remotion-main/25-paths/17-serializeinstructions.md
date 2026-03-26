---
title: "serializeInstructions()"
url: "https://www.remotion.dev/docs/paths/serialize-instructions"
path: "/docs/paths/serialize-instructions"
---

"---\nimage: /generated/articles-docs-paths-serialize-instructions.png\ntitle: serializeInstructions()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40_\n\nTakes an array of [`Instruction`](/docs/paths/parse-path)'s and serializes it into an SVG path string.\n\n```tsx twoslash title=\"serialize-instructions.ts\"\nimport { serializeInstructions } from \"@remotion/paths\";\n\nconst newPath = serializeInstructions([\n  {\n    type: \"M\",\n    x: 10,\n    y: 10,\n  },\n  {\n    type: \"L\",\n    x: 20,\n    y: 20,\n  },\n]); // M 10 10 L 20 20\n```\n\nThis function may throw if the instructions don't match the [`Instruction`](/docs/paths/parse-path) type, but it does not explicitly check for invalid input.\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [`parsePath()`](/docs/paths/parse-path)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/serialize-instructions.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40*

Takes an array of [`Instruction`](/docs/paths/parse-path)'s and serializes it into an SVG path string.

```

serialize-instructions.tsimport { serializeInstructions } from "@remotion/paths";

const newPath = serializeInstructions([
  {
    type: "M",
    x: 10,
    y: 10,
  },
  {
    type: "L",
    x: 20,
    y: 20,
  },
]); // M 10 10 L 20 20Copy
```

This function may throw if the instructions don't match the [`Instruction`](/docs/paths/parse-path) type, but it does not explicitly check for invalid input.

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [`parsePath()`](/docs/paths/parse-path)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/serialize-instructions.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/serialize-instructions.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/serialize-instructions.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/serialize-instructions.ts)