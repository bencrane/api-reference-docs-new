---
title: "noise4D()"
url: "https://www.remotion.dev/docs/noise/noise-4d"
path: "/docs/noise/noise-4d"
---

"---\nimage: /generated/articles-docs-noise-noise-4d.png\ntitle: noise4D()\ncrumb: \"Make some\"\n---\n\n_Part of the [`@remotion/noise`](/docs/noise) package._\n\nCreates 4D noise.\n\n## API\n\nThe function takes five arguments:\n\n### `seed`\n\nPass any _string_ or _number_. If the seed is the same, you will get the same result for same `x`, `y`, `z` and `w` values. Change the seed to get different results for your `x`, `y`, `z`, `w` values.\n\n### `x`\n\n_number_\n\nThe first dimensional value.\n\n### `y`\n\n_number_\n\nThe second dimensional value.\n\n### `z`\n\n_number_\n\nThe third dimensional value.\n\n### `w`\n\n_number_\n\nThe fourth dimensional value.\n\n## Return value\n\nA value between `-1` and `1`, swinging as your `x`, `y`, `z` and `w` values change.\n\n## Example\n\n```tsx twoslash\nimport { noise4D } from \"@remotion/noise\";\n\nconst x = 32;\nconst y = 40;\nconst z = 50;\nconst w = 64;\nconsole.log(noise4D(\"my-seed\", x, y, z, w));\n```\n\n## Credits\n\nDependency: [simplex-noise](https://www.npmjs.com/package/simplex-noise)\n\n## See also\n\n- [Example: Noise visualization](/docs/noise-visualization)\n- [noise2D()](/docs/noise/noise-2d)\n- [noise3D()](/docs/noise/noise-3d)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/noise/src/index.ts)\n- [`@remotion/noise`](/docs/noise)\n"

*Part of the [`@remotion/noise`](/docs/noise) package.*

Creates 4D noise.

## API[​](#api)

The function takes five arguments:

### `seed`[​](#seed)

Pass any *string* or *number*. If the seed is the same, you will get the same result for same `x`, `y`, `z` and `w` values. Change the seed to get different results for your `x`, `y`, `z`, `w` values.

### `x`[​](#x)

*number*

The first dimensional value.

### `y`[​](#y)

*number*

The second dimensional value.

### `z`[​](#z)

*number*

The third dimensional value.

### `w`[​](#w)

*number*

The fourth dimensional value.

## Return value[​](#return-value)

A value between `-1` and `1`, swinging as your `x`, `y`, `z` and `w` values change.

## Example[​](#example)

```
import { noise4D } from "@remotion/noise";

const x = 32;
const y = 40;
const z = 50;
const w = 64;
console.log(noise4D("my-seed", x, y, z, w));Copy
```

## Credits[​](#credits)

Dependency: [simplex-noise](https://www.npmjs.com/package/simplex-noise)

## See also[​](#see-also)

- [Example: Noise visualization](/docs/noise-visualization)

- [noise2D()](/docs/noise/noise-2d)

- [noise3D()](/docs/noise/noise-3d)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/noise/src/index.ts)

- [`@remotion/noise`](/docs/noise)
](/docs/noise)](/docs/noise)
](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)
- ](/docs/noise)