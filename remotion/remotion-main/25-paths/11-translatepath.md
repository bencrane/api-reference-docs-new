---
title: "translatePath()"
url: "https://www.remotion.dev/docs/paths/translate-path"
path: "/docs/paths/translate-path"
---

"---\nimage: /generated/articles-docs-paths-translate-path.png\ntitle: translatePath()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package._\n\nTranslates the path by the given `x` and `y` coordinates.\n\n## Arguments\n\nThe function takes three arguments:\n\n- `path`, the original SVG path.\n- `x`, the amount of horizontal translation.\n- `y` the amount of vertical translation.\n\n## Return value\n\nReturns a new `string` containing a path if it is valid:\n\n```tsx twoslash title='translate-x.ts'\nimport { translatePath } from \"@remotion/paths\";\n\nconst translatedPath = translatePath(\"M 50 50 L 150 50\", 10, 0);\nconsole.log(translatedPath); // \"M 50 50 L 150 50\"\n```\n\n```tsx twoslash title='translate-y.ts'\nimport { translatePath } from \"@remotion/paths\";\n\nconst translatedPath = translatePath(\"M10 10 L15 15\", 10, 10);\nconsole.log(translatedPath); // \"M 20 20 L 25 25\"\n```\n\n```tsx twoslash title='translate-x-and-y.ts'\nimport { translatePath } from \"@remotion/paths\";\n\nconst translatedPath = translatePath(\n  \"M 35,50 a 25,25,0,1,1,50,0 a 25,25,0,1,1,-50,0\",\n  10,\n  20\n);\nconsole.log(translatedPath); // \"M 45 70 a 25 25 0 1 1 50 0 a 25, 5 0 1 1 -50 0\"\n```\n\nThe function will throw if the path is invalid:\n\n```tsx twoslash\nimport { translatePath } from \"@remotion/paths\";\n// ---cut---\ntranslatePath(\"remotion\", 10, 0); // Malformed path data: \"m\" ...\n```\n\n## Credits\n\nSource code stems mostly from [translate-svg-path](https://github.com/michaelrhodes/translate-svg-path) and [serialize-svg-path](https://github.com/jkroso/serialize-svg-path).\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package.*

Translates the path by the given `x` and `y` coordinates.

## Arguments[​](#arguments)

The function takes three arguments:

- `path`, the original SVG path.

- `x`, the amount of horizontal translation.

- `y` the amount of vertical translation.

## Return value[​](#return-value)

Returns a new `string` containing a path if it is valid:

```

translate-x.tsimport { translatePath } from "@remotion/paths";

const translatedPath = translatePath("M 50 50 L 150 50", 10, 0);
console.log(translatedPath); // "M 50 50 L 150 50"Copy
```

```

translate-y.tsimport { translatePath } from "@remotion/paths";

const translatedPath = translatePath("M10 10 L15 15", 10, 10);
console.log(translatedPath); // "M 20 20 L 25 25"Copy
```

```

translate-x-and-y.tsimport { translatePath } from "@remotion/paths";

const translatedPath = translatePath(
  "M 35,50 a 25,25,0,1,1,50,0 a 25,25,0,1,1,-50,0",
  10,
  20
);
console.log(translatedPath); // "M 45 70 a 25 25 0 1 1 50 0 a 25, 5 0 1 1 -50 0"Copy
```

The function will throw if the path is invalid:

```
translatePath("remotion", 10, 0); // Malformed path data: "m" ...Copy
```

## Credits[​](#credits)

Source code stems mostly from [translate-svg-path](https://github.com/michaelrhodes/translate-svg-path) and [serialize-svg-path](https://github.com/jkroso/serialize-svg-path).

## See also[​](#see-also)

- [`@remotion/paths`](/docs/paths)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/translate-path.ts)