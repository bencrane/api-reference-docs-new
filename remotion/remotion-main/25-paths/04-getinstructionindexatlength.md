---
title: "getInstructionIndexAtLength()"
url: "https://www.remotion.dev/docs/paths/get-instruction-index-at-length"
path: "/docs/paths/get-instruction-index-at-length"
---

"---\nimage: /generated/articles-docs-paths-get-instruction-index-at-length.png\ntitle: getInstructionIndexAtLength()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\n_available from v4.0.84_\n\nGets the index of the instruction that is at the length of the path.  \nThe first argument is an SVG path, the second one is the length at which the point should be sampled.  \nIt must be between `0` and the return value of [`getLength()`](/docs/paths/get-length).\n\nAn object containing `index` and `lengthIntoInstruction` is returned if the path is valid:\n\n```tsx twoslash title=\"Example\"\nimport { getInstructionIndexAtLength } from \"@remotion/paths\";\n\nconst { index, lengthIntoInstruction } = getInstructionIndexAtLength(\n  \"M 0 0 L 100 0 L 200 0\",\n  105,\n);\nconsole.log(index); // 1\nconsole.log(lengthIntoInstruction); // 5\n```\n\nTo get the instruction at a specific index, you can use [`parsePath()`](/docs/paths/parse-path):\n\n```tsx twoslash title=\"Get instruction\"\nimport { getInstructionIndexAtLength, parsePath } from \"@remotion/paths\";\n\nconst path = \"M 0 0 L 100 0 L 200 0\";\nconst { index } = getInstructionIndexAtLength(path, 105);\n\nconst parsed = parsePath(path);\nconst instruction = parsed[index]; // {type: 'L', x: 100, y: 0}\n```\n\nThe function **will throw** if the path is invalid:\n\n```tsx twoslash\nimport { getInstructionIndexAtLength } from \"@remotion/paths\";\n// ---cut---\ngetInstructionIndexAtLength(\"remotion\", 50); // Error: Malformed path data: ...\n```\n\nThe function **will throw** if the sample length is bigger than the [length](/docs/paths/get-length) of the path:\n\n```tsx twoslash\nimport { getInstructionIndexAtLength } from \"@remotion/paths\";\n// ---cut---\ngetInstructionIndexAtLength(\"M 0 0 L 100 0\", 105); // Error: A length of 105 was passed to getInstructionIndexAtLength() but the total length of the path is only 100;\n```\n\n## Credits\n\nThis function was adapted from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).\n\n## See also\n\n- [`getLength()`](/docs/paths/get-length)\n- [`parsePath()`](/docs/paths/parse-path)\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-instruction-index-at-length.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

*available from v4.0.84*

Gets the index of the instruction that is at the length of the path.

The first argument is an SVG path, the second one is the length at which the point should be sampled.

It must be between `0` and the return value of [`getLength()`](/docs/paths/get-length).

An object containing `index` and `lengthIntoInstruction` is returned if the path is valid:

```

Exampleimport { getInstructionIndexAtLength } from "@remotion/paths";

const { index, lengthIntoInstruction } = getInstructionIndexAtLength(
  "M 0 0 L 100 0 L 200 0",
  105,
);
console.log(index); // 1
console.log(lengthIntoInstruction); // 5Copy
```

To get the instruction at a specific index, you can use [`parsePath()`](/docs/paths/parse-path):

```

Get instructionimport { getInstructionIndexAtLength, parsePath } from "@remotion/paths";

const path = "M 0 0 L 100 0 L 200 0";
const { index } = getInstructionIndexAtLength(path, 105);

const parsed = parsePath(path);
const instruction = parsed[index]; // {type: 'L', x: 100, y: 0}Copy
```

The function **will throw** if the path is invalid:

```
getInstructionIndexAtLength("remotion", 50); // Error: Malformed path data: ...Copy
```

The function **will throw** if the sample length is bigger than the [length](/docs/paths/get-length) of the path:

```
getInstructionIndexAtLength("M 0 0 L 100 0", 105); // Error: A length of 105 was passed to getInstructionIndexAtLength() but the total length of the path is only 100;Copy
```

## Credits[​](#credits)

This function was adapted from [svg-path-properties](https://www.npmjs.com/package/svg-path-properties).

## See also[​](#see-also)

- [`getLength()`](/docs/paths/get-length)

- [`parsePath()`](/docs/paths/parse-path)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-instruction-index-at-length.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-instruction-index-at-length.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-instruction-index-at-length.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-instruction-index-at-length.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/get-instruction-index-at-length.ts)