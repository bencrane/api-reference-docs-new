---
title: "parsePath()"
url: "https://www.remotion.dev/docs/paths/parse-path"
path: "/docs/paths/parse-path"
---

"---\nimage: /generated/articles-docs-paths-parse-path.png\ntitle: parsePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40_\n\nParses an SVG string path into an array of `Instruction`'s.\n\n```tsx twoslash title=\"reset-path.ts\"\nimport { parsePath } from \"@remotion/paths\";\n\nconst newPath = parsePath(\"M 10 10 L 20 20\");\n\n/*\n  [\n    { type: \"M\", x: 10, y: 10 },\n    { type: \"L\", x: 20, y: 20 },\n  ]\n*/\n```\n\nThis function will throw if the SVG path is invalid.\n\n## Return type type\n\nAn array of `Instruction`'s. The `Instruction` type can also be imported from `@remotion/paths`:\n\n```ts twoslash\nimport type { Instruction } from \"@remotion/paths\";\n```\n\nThe type has the following shape:\n\n```ts twoslash\nexport type Instruction =\n  | {\n      type: \"M\";\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"L\";\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"H\";\n      x: number;\n    }\n  | {\n      type: \"V\";\n      y: number;\n    }\n  | {\n      type: \"C\";\n      cp1x: number;\n      cp1y: number;\n      cp2x: number;\n      cp2y: number;\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"S\";\n      cpx: number;\n      cpy: number;\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"Q\";\n      cpx: number;\n      cpy: number;\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"T\";\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"A\";\n      rx: number;\n      ry: number;\n      xAxisRotation: number;\n      largeArcFlag: boolean;\n      sweepFlag: boolean;\n      x: number;\n      y: number;\n    }\n  | {\n      type: \"m\";\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"l\";\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"h\";\n      dx: number;\n    }\n  | {\n      type: \"v\";\n      dy: number;\n    }\n  | {\n      type: \"c\";\n      cp1dx: number;\n      cp1dy: number;\n      cp2dx: number;\n      cp2dy: number;\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"s\";\n      cpdx: number;\n      cpdy: number;\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"q\";\n      cpdx: number;\n      cpdy: number;\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"t\";\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"a\";\n      rx: number;\n      ry: number;\n      xAxisRotation: number;\n      largeArcFlag: boolean;\n      sweepFlag: boolean;\n      dx: number;\n      dy: number;\n    }\n  | {\n      type: \"Z\";\n    }\n  | {\n      type: \"z\";\n    };\n```\n\n## See also\n\n- [`serializeInstructions()`](/docs/paths/serialize-instructions)\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/parse-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available from v3.3.40*

Parses an SVG string path into an array of `Instruction`'s.

```

reset-path.tsimport { parsePath } from "@remotion/paths";

const newPath = parsePath("M 10 10 L 20 20");

/*
  [
    { type: "M", x: 10, y: 10 },
    { type: "L", x: 20, y: 20 },
  ]
*/Copy
```

This function will throw if the SVG path is invalid.

## Return type type[​](#return-type-type)

An array of `Instruction`'s. The `Instruction` type can also be imported from `@remotion/paths`:

```
import type { Instruction } from "@remotion/paths";Copy
```

The type has the following shape:

```
export type Instruction =
  | {
      type: "M";
      x: number;
      y: number;
    }
  | {
      type: "L";
      x: number;
      y: number;
    }
  | {
      type: "H";
      x: number;
    }
  | {
      type: "V";
      y: number;
    }
  | {
      type: "C";
      cp1x: number;
      cp1y: number;
      cp2x: number;
      cp2y: number;
      x: number;
      y: number;
    }
  | {
      type: "S";
      cpx: number;
      cpy: number;
      x: number;
      y: number;
    }
  | {
      type: "Q";
      cpx: number;
      cpy: number;
      x: number;
      y: number;
    }
  | {
      type: "T";
      x: number;
      y: number;
    }
  | {
      type: "A";
      rx: number;
      ry: number;
      xAxisRotation: number;
      largeArcFlag: boolean;
      sweepFlag: boolean;
      x: number;
      y: number;
    }
  | {
      type: "m";
      dx: number;
      dy: number;
    }
  | {
      type: "l";
      dx: number;
      dy: number;
    }
  | {
      type: "h";
      dx: number;
    }
  | {
      type: "v";
      dy: number;
    }
  | {
      type: "c";
      cp1dx: number;
      cp1dy: number;
      cp2dx: number;
      cp2dy: number;
      dx: number;
      dy: number;
    }
  | {
      type: "s";
      cpdx: number;
      cpdy: number;
      dx: number;
      dy: number;
    }
  | {
      type: "q";
      cpdx: number;
      cpdy: number;
      dx: number;
      dy: number;
    }
  | {
      type: "t";
      dx: number;
      dy: number;
    }
  | {
      type: "a";
      rx: number;
      ry: number;
      xAxisRotation: number;
      largeArcFlag: boolean;
      sweepFlag: boolean;
      dx: number;
      dy: number;
    }
  | {
      type: "Z";
    }
  | {
      type: "z";
    };Copy
```

## See also[​](#see-also)

- [`serializeInstructions()`](/docs/paths/serialize-instructions)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/parse-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/parse-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/parse-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/parse-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/parse-path.ts)