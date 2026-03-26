---
title: "reduceInstructions()"
url: "https://www.remotion.dev/docs/paths/reduce-instructions"
path: "/docs/paths/reduce-instructions"
---

"---\nimage: /generated/articles-docs-paths-reduce-instructions.png\ntitle: reduceInstructions()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40_\n\nTakes an array of [`Instruction`](/docs/paths/parse-path)'s and reduces the amount of instruction types them so the path only consists of `M`, `L`, `C` and `Z` instructions.\n\n:::note\nIn versions before v4.0.168, `Q` instructions were reduced away.\n:::\n\nIn reverse logic, this function will eliminate all `H`, `V`, `S`, `T`, `A`, `Q` `m`, `l`, `h`, `v`, `c`, `s`, `q`, `t`, `a`, `q` and `z` instructions.\n\nThis is useful if you want to manually edit a path and want to make sure it's as simple as possible.\n\nNote that this may result in a longer path.\n\n```ts twoslash\nimport { reduceInstructions, ReducedInstruction } from \"@remotion/paths\";\n\nconst simplified: ReducedInstruction[] = reduceInstructions([\n  { type: \"m\", dx: 10, dy: 10 },\n  { type: \"h\", dx: 100 },\n]);\n\n/*\n  [\n    {type: 'M', x: 10, y: 10},\n    {type: 'L', x: 110, y: 10},\n  ]\n*/\n```\n\n## `ReducedInstruction` type\n\nIf you want a type which includes only reduced instructions, you can import the `ReducedInstruction` type.\n\n```ts twoslash\nimport { ReducedInstruction } from \"@remotion/paths\";\n```\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [`parsePath()`](/docs/paths/parse-path)\n- [`normalizePath()`](/docs/paths/normalize-path)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/reduce-instructions.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40*

Takes an array of [`Instruction`](/docs/paths/parse-path)'s and reduces the amount of instruction types them so the path only consists of `M`, `L`, `C` and `Z` instructions.
](/docs/paths/parse-path)](/docs/paths/parse-path)
](/docs/paths/parse-path)
- ](/docs/paths/parse-path)