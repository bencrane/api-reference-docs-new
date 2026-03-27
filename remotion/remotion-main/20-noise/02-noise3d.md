---
title: "noise3D()"
url: "https://www.remotion.dev/docs/noise/noise-3d"
path: "/docs/noise/noise-3d"
---

"---\nimage: /generated/articles-docs-noise-noise-3d.png\ntitle: noise3D()\ncrumb: \"Make some\"\n---\n\n_Part of the [`@remotion/noise`](/docs/noise) package._\n\nCreates 3D noise.\n\n## API\n\nThe function takes four arguments:\n\n### `seed`\n\nPass any _string_ or _number_. If the seed is the same, you will get the same result for same `x`, `y` and `z` values. Change the seed to get different results for your `x`, `y` and `z` values.\n\n### `x`\n\n_number_\n\nThe first dimensional value.\n\n### `y`\n\n_number_\n\nThe second dimensional value.\n\n### `z`\n\n_number_\n\nThe third dimensional value.\n\n## Return value\n\nA value between `-1` and `1`, swinging as your `x`, `y` and `z` values change.\n\n## Example\n\n```tsx twoslash\nimport { noise3D } from \"@remotion/noise\";\n\nconst x = 32;\nconst y = 40;\nconst z = 50;\nconsole.log(noise3D(\"my-seed\", x, y, z));\n```\n\n## Credits\n\nUses the [simplex-noise](https://www.npmjs.com/package/simplex-noise) dependency\n\n## See also\n\n- [Example: Noise visualization](/docs/noise-visualization)\n- [noise2D()](/docs/noise/noise-2d)\n- [noise4D()](/docs/noise/noise-4d)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/noise/src/index.ts)\n- [`@remotion/noise`](/docs/noise)\n"

*Part of the [`@remotion/noise`](/docs/noise) package.*

Creates 3D noise.

## API[​](#api)

The function takes four arguments:

### `seed`[​](#seed)

Pass any *string* or *number*. If the seed is the same, you will get the same result for same `x`, `y` and `z` values. Change the seed to get different results for your `x`, `y` and `z` values.

### `x`[​](#x)

*number*

The first dimensional value.

### `y`[​](#y)

*number*

The second dimensional value.

### `z`[​](#z)

*number*

The third dimensional value.

## Return value[​](#return-value)

A value between `-1` and `1`, swinging as your `x`, `y` and `z` values change.

## Example[​](#example)

```
import { noise3D } from "@remotion/noise";

const x = 32;
const y = 40;
const z = 50;
console.log(noise3D("my-seed", x, y, z));Copy
```

## Credits[​](#credits)

Uses the [simplex-noise](https://www.npmjs.com/package/simplex-noise) dependency

## See also[​](#see-also)

- [Example: Noise visualization](/docs/noise-visualization)

- [noise2D()](/docs/noise/noise-2d)

- [noise4D()](/docs/noise/noise-4d)

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