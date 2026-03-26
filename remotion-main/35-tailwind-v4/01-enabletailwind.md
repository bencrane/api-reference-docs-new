---
title: "enableTailwind()"
url: "https://www.remotion.dev/docs/tailwind-v4/enable-tailwind"
path: "/docs/tailwind-v4/enable-tailwind"
---

"---\nimage: /generated/articles-docs-tailwind-v4-enable-tailwind.png\ntitle: enableTailwind()\ncrumb: '@remotion/tailwind-v4'\n---\n\n_available from v4.0.256_\n\nA function that modifies the default Webpack configuration to make the necessary changes to support TailwindCSS.\nSee the [setup](/docs/tailwind) to see full instructions on how to setup TailwindCSS in Remotion.\n\n```ts twoslash title=\"remotion.config.ts\"\nimport {Config} from '@remotion/cli/config';\nimport {enableTailwind} from '@remotion/tailwind-v4';\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableTailwind(currentConfiguration);\n});\n```\n\n## Multiple Webpack changes\n\nIf you want to make other configuration changes, you can do so by doing them reducer-style:\n\n```ts twoslash title=\"remotion.config.ts\"\nimport {Config} from '@remotion/cli/config';\nimport {enableTailwind} from '@remotion/tailwind-v4';\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableTailwind({\n    ...currentConfiguration,\n\n    // Make other changes\n  });\n});\n```\n"

*available from v4.0.256*

A function that modifies the default Webpack configuration to make the necessary changes to support TailwindCSS.
See the [setup](/docs/tailwind) to see full instructions on how to setup TailwindCSS in Remotion.

```

remotion.config.tsimport {Config} from '@remotion/cli/config';
import {enableTailwind} from '@remotion/tailwind-v4';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind(currentConfiguration);
});Copy
```

## Multiple Webpack changes[​](#multiple-webpack-changes)

If you want to make other configuration changes, you can do so by doing them reducer-style:

```

remotion.config.tsimport {Config} from '@remotion/cli/config';
import {enableTailwind} from '@remotion/tailwind-v4';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind({
    ...currentConfiguration,

    // Make other changes
  });
});Copy
```
](#multiple-webpack-changes)](#multiple-webpack-changes)
](#multiple-webpack-changes)