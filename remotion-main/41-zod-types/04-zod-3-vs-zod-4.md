---
title: "Zod 3 vs. Zod 4"
url: "https://www.remotion.dev/docs/zod-types/v3"
path: "/docs/zod-types/v3"
---

"---\nimage: /generated/articles-docs-zod-types-v3.png\nsidebar_label: Zod 3 vs. Zod 4\ntitle: '@remotion/zod-types-v3'\ncrumb: '@remotion/zod-types'\n---\n\n# @remotion/zod-types-v3<AvailableFrom v=\"4.0.426\" />\n\n[`@remotion/zod-types`](/docs/zod-types) creates schemas using Zod v4 since Remotion v4.0.426.\n\nThis package is for if you are using Zod v3.22.3 and want to compose functions like [`zColor()`](/docs/zod-types/z-color) with Zod v3.22.3 schemas.\n\n## Installation\n\n<Installation pkg=\"@remotion/zod-types-v3\" />\n\n## Usage\n\n```tsx twoslash title=\"Using @remotion/zod-types-v3 with Zod v3\"\nimport {z} from 'zod'; // zod = 3.22.3\nimport {zColor} from '@remotion/zod-types-v3';\n\nexport const mySchema = z.object({\n  color: zColor(),\n});\n```\n\nThe package exports the same [`zColor()`](/docs/zod-types/z-color), [`zTextarea()`](/docs/zod-types/z-textarea), and [`zMatrix()`](/docs/zod-types/z-matrix) functions as [`@remotion/zod-types`](/docs/zod-types), but they return Zod v3.22.3 schema types.\n\n## When to use\n\nUse [`@remotion/zod-types`](/docs/zod-types) with Zod v4:\n\n```tsx twoslash\nimport {z} from 'zod'; // zod = 4.x.x\nimport {zColor} from '@remotion/zod-types';\n\nexport const mySchema = z.object({\n  color: zColor(),\n});\n```\n\nUse [`@remotion/zod-types`](/docs/zod-types) if you are not nesting schemas:\n\n```tsx twoslash\nimport {zColor} from '@remotion/zod-types';\nimport {visualControl} from '@remotion/studio';\n\nexport const myVisualControl = visualControl('my-color', '#fff', zColor());\n```\n\nUse `@remotion/zod-types-v3` with Zod v3.22.3:\n\n```tsx twoslash\nimport {z} from 'zod'; // zod = 3.22.3\nimport {zColor} from '@remotion/zod-types-v3';\n\nexport const mySchema = z.object({\n  color: zColor(),\n});\n```\n\nOther Zod 3.x.x versions are not officially supported.\n\n## See also\n\n- [`@remotion/zod-types`](/docs/zod-types)\n"

[`@remotion/zod-types`](/docs/zod-types) creates schemas using Zod v4 since Remotion v4.0.426.

This package is for if you are using Zod v3.22.3 and want to compose functions like [`zColor()`](/docs/zod-types/z-color) with Zod v3.22.3 schemas.

## Installation[​](#installation)

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/zod-types-v3Copy
```

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

## Usage[​](#usage)

```

Using @remotion/zod-types-v3 with Zod v3import {z} from 'zod'; // zod = 3.22.3
import {zColor} from '@remotion/zod-types-v3';

export const mySchema = z.object({
  color: zColor(),
});Copy
```

The package exports the same [`zColor()`](/docs/zod-types/z-color), [`zTextarea()`](/docs/zod-types/z-textarea), and [`zMatrix()`](/docs/zod-types/z-matrix) functions as [`@remotion/zod-types`](/docs/zod-types), but they return Zod v3.22.3 schema types.

## When to use[​](#when-to-use)

Use [`@remotion/zod-types`](/docs/zod-types) with Zod v4:

```
import {z} from 'zod'; // zod = 4.x.x
import {zColor} from '@remotion/zod-types';

export const mySchema = z.object({
  color: zColor(),
});Copy
```

Use [`@remotion/zod-types`](/docs/zod-types) if you are not nesting schemas:

```
import {zColor} from '@remotion/zod-types';
import {visualControl} from '@remotion/studio';

export const myVisualControl = visualControl('my-color', '#fff', zColor());Copy
```

Use `@remotion/zod-types-v3` with Zod v3.22.3:

```
import {z} from 'zod'; // zod = 3.22.3
import {zColor} from '@remotion/zod-types-v3';

export const mySchema = z.object({
  color: zColor(),
});Copy
```

Other Zod 3.x.x versions are not officially supported.

## See also[​](#see-also)

- [`@remotion/zod-types`](/docs/zod-types)
](/docs/zod-types)](/docs/zod-types)
](/docs/zod-types)
- ](/docs/zod-types)
- ](/docs/zod-types)
- ](/docs/zod-types)