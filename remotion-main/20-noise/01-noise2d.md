---
title: "noise2D()"
url: "https://www.remotion.dev/docs/noise/noise-2d"
path: "/docs/noise/noise-2d"
---

"---\nimage: /generated/articles-docs-noise-noise-2d.png\ntitle: noise2D()\ncrumb: \"Make some\"\n---\n\n_Part of the [`@remotion/noise`](/docs/noise) package._\n\nCreates 2D noise.\n\n## API\n\nThe function takes three arguments:\n\n### `seed`\n\nPass any _string_ or _number_. If the seed is the same, you will get the same result for same `x` and `y` values. Change the seed to get different results for your `x` and `y` values.\n\n### `x`\n\n_number_\n\nThe first dimensional value.\n\n### `y`\n\n_number_\n\nThe second dimensional value.\n\n## Return value\n\nA value between `-1` and `1`, swinging as your `x` and `y` values change.\n\n## Example\n\n```tsx twoslash\nimport { noise2D } from \"@remotion/noise\";\n\nconst x = 32;\nconst y = 40;\nconsole.log(noise2D(\"my-seed\", x, y)); // a number in the interval [-1, 1] which corresponds to (x, y) coord.\n```\n\n## Credits\n\nUses the [simplex-noise](https://www.npmjs.com/package/simplex-noise) dependency\n\n## See also\n\n- [Example: Noise visualization](/docs/noise-visualization)\n- [noise3D()](/docs/noise/noise-3d)\n- [noise4D()](/docs/noise/noise-4d)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/noise/src/index.ts)\n- [`@remotion/noise`](/docs/noise)\n"

*Part of the [`@remotion/noise`](/docs/noise) package.*

Creates 2D noise.

## API[​](#api)

The function takes three arguments:

### `seed`[​](#seed)

Pass any *string* or *number*. If the seed is the same, you will get the same result for same `x` and `y` values. Change the seed to get different results for your `x` and `y` values.

### `x`[​](#x)

*number*

The first dimensional value.

### `y`[​](#y)

*number*

The second dimensional value.

## Return value[​](#return-value)

A value between `-1` and `1`, swinging as your `x` and `y` values change.

## Example[​](#example)

```
import { noise2D } from "@remotion/noise";

const x = 32;
const y = 40;
console.log(noise2D("my-seed", x, y)); // a number in the interval [-1, 1] which corresponds to (x, y) coord.Copy
```

## Credits[​](#credits)

Uses the [simplex-noise](https://www.npmjs.com/package/simplex-noise) dependency

## See also[​](#see-also)

- [Example: Noise visualization](/docs/noise-visualization)

- [noise3D()](/docs/noise/noise-3d)

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