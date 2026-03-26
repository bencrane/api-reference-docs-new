---
title: "@remotion/enable-scss"
url: "https://www.remotion.dev/docs/enable-scss/overview"
path: "/docs/enable-scss/overview"
---

"---\nimage: /generated/articles-docs-enable-scss-overview.png\nsidebar_label: Overview\ntitle: '@remotion/enable-scss'\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {ExperimentalBadge} from '../../components/Experimental';\nimport {TableOfContents} from './TableOfContents';\n\nThis package provides a Webpack override for enabling [SCSS/SASS](https://sass-lang.com/) with Remotion..\n\n## Installation\n\nInstall `@remotion/enable-scss` as well as TailwindCSS dependencies.\n\n<Installation pkg=\"@remotion/enable-scss sass@1.77.2 sass-loader@14.2.1 css-loader@5.2.7\" />\n\n<br />\n\n:::warning\nPay attention to install exactly these versions.  \nNewer versions may not work.\n:::\n\n## Usage\n\n[Override the Webpack config](/docs/webpack) by using [`enableScss()`](/docs/enable-scss/enable-scss).\n\n```ts twoslash title=\"remotion.config.ts\"\nimport {Config} from '@remotion/cli/config';\nimport {enableScss} from '@remotion/enable-scss';\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableScss(currentConfiguration);\n});\n```\n\n## APIs\n\n<TableOfContents />\n"

This package provides a Webpack override for enabling [SCSS/SASS](https://sass-lang.com/) with Remotion..

## Installation[​](#installation)

Install `@remotion/enable-scss` as well as TailwindCSS dependencies.

- npm
- bun
- pnpm
- yarn

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection) [[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

](/cdn-cgi/l/email-protection)](/cdn-cgi/l/email-protection)
](/cdn-cgi/l/email-protection)
- ](/cdn-cgi/l/email-protection)
- ](/cdn-cgi/l/email-protection)