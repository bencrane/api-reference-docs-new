---
title: "enableSkia()"
url: "https://www.remotion.dev/docs/skia/enable-skia"
path: "/docs/skia/enable-skia"
---

"---\nimage: /generated/articles-docs-skia-enable-skia.png\ntitle: enableSkia()\ncrumb: \"@remotion/skia\"\n---\n\nA function that modifies the default Webpack configuration to make the necessary changes to support Skia.\n\n```ts twoslash title=\"remotion.config.ts\"\nimport { Config } from \"@remotion/cli/config\";\nimport { enableSkia } from \"@remotion/skia/enable\";\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableSkia(currentConfiguration);\n});\n```\n\n:::note\nPrior to `v3.3.39`, the option was called `Config.Bundling.overrideWebpackConfig()`.\n:::\n\nIf you want to make other configuration changes, you can do so by doing them reducer-style:\n\n```ts twoslash title=\"remotion.config.ts\"\nimport { Config } from \"@remotion/cli/config\";\nimport { enableSkia } from \"@remotion/skia/enable\";\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableSkia({\n    ...currentConfiguration,\n\n    // Make other changes\n  });\n});\n```\n\n:::note\nPrior to `v3.3.39`, the option was called `Config.Bundling.overrideWebpackConfig()`.\n:::\n\nSee the [setup](/docs/skia) to see full instructions on how to setup React Native Skia in Remotion.\n"

A function that modifies the default Webpack configuration to make the necessary changes to support Skia.

```

remotion.config.tsimport { Config } from "@remotion/cli/config";
import { enableSkia } from "@remotion/skia/enable";

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableSkia(currentConfiguration);
});Copy
```

]()]()