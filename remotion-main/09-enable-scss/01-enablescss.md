---
title: "enableScss()"
url: "https://www.remotion.dev/docs/enable-scss/enable-scss"
path: "/docs/enable-scss/enable-scss"
---

"---\nimage: /generated/articles-docs-enable-scss-enable-scss.png\ntitle: enableScss()\nslug: /enable-scss/enable-scss\ncrumb: \"@remotion/enable-scss\"\n---\n\n_available from v4.0.162_\n\nA function that modifies the default Webpack configuration to make the necessary changes to support SASS/SCSS.\n\n```ts twoslash title=\"remotion.config.ts\"\nimport { Config } from \"@remotion/cli/config\";\nimport { enableScss } from \"@remotion/enable-scss\";\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableScss(currentConfiguration);\n});\n```\n\nIf you want to make other configuration changes, you can do so by doing them reducer-style:\n\n```ts twoslash title=\"remotion.config.ts\"\nimport { Config } from \"@remotion/cli/config\";\nimport { enableScss } from \"@remotion/enable-scss\";\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableScss({\n    ...currentConfiguration,\n    // Make other changes\n  });\n});\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/enable-scss/src/enable-scss.ts)\n"

*available from v4.0.162*

A function that modifies the default Webpack configuration to make the necessary changes to support SASS/SCSS.

```

remotion.config.tsimport { Config } from "@remotion/cli/config";
import { enableScss } from "@remotion/enable-scss";

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableScss(currentConfiguration);
});Copy
```

If you want to make other configuration changes, you can do so by doing them reducer-style:

```

remotion.config.tsimport { Config } from "@remotion/cli/config";
import { enableScss } from "@remotion/enable-scss";

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableScss({
    ...currentConfiguration,
    // Make other changes
  });
});Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/enable-scss/src/enable-scss.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/enable-scss/src/enable-scss.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/enable-scss/src/enable-scss.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/enable-scss/src/enable-scss.ts)