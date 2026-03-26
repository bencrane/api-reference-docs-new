---
title: "@remotion/tailwind-v4"
url: "https://www.remotion.dev/docs/tailwind-v4/overview"
path: "/docs/tailwind-v4/overview"
---

"---\nimage: /generated/articles-docs-tailwind-v4-overview.png\nid: overview\nsidebar_label: Overview\ntitle: '@remotion/tailwind-v4'\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {ExperimentalBadge} from '../../components/Experimental';\nimport {TableOfContents} from './TableOfContents';\n\nThis package provides utilities useful for integrating [TailwindCSS v4](https://tailwindcss.com/) with Remotion, as documented on our [TailwindCSS](/docs/tailwind) page.\n\n## Installation\n\nInstall `@remotion/tailwind-v4` as well as TailwindCSS dependencies.\n\n<Installation pkg=\"@remotion/tailwind-v4\" />\n\n<br />\n\n[Override the Webpack config](/docs/webpack) by using [`enableTailwind()`](/docs/tailwind/enable-tailwind).\n\n```ts twoslash title=\"remotion.config.ts\"\nimport {Config} from '@remotion/cli/config';\nimport {enableTailwind} from '@remotion/tailwind-v4';\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableTailwind(currentConfiguration);\n});\n```\n\nThen follow the remaining set up steps from the [TailwindCSS](/docs/tailwind) page.\n\n## APIs\n\n<TableOfContents />\n"

This package provides utilities useful for integrating [TailwindCSS v4](https://tailwindcss.com/) with Remotion, as documented on our [TailwindCSS](/docs/tailwind) page.

## Installation[​](#installation)

Install `@remotion/tailwind-v4` as well as TailwindCSS dependencies.

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/tailwind-v4Copy
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

[Override the Webpack config](/docs/webpack) by using [`enableTailwind()`](/docs/tailwind/enable-tailwind).

```

remotion.config.tsimport {Config} from '@remotion/cli/config';
import {enableTailwind} from '@remotion/tailwind-v4';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind(currentConfiguration);
});Copy
```

Then follow the remaining set up steps from the [TailwindCSS](/docs/tailwind) page.

## APIs[​](#apis)

[
**enableTailwind()**
Override the Webpack config to enable TailwindCSS](/docs/tailwind-v4/enable-tailwind)](/docs/tailwind-v4/enable-tailwind)](/docs/tailwind-v4/enable-tailwind)
](/docs/tailwind-v4/enable-tailwind)
- ](/docs/tailwind-v4/enable-tailwind)