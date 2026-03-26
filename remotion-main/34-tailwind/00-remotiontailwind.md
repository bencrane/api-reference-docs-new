---
title: "@remotion/tailwind"
url: "https://www.remotion.dev/docs/tailwind/tailwind"
path: "/docs/tailwind/tailwind"
---

"---\nimage: /generated/articles-docs-tailwind-overview.png\nid: tailwind\nsidebar_label: Overview\ntitle: '@remotion/tailwind'\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {ExperimentalBadge} from '../../components/Experimental';\nimport {TableOfContents} from './TableOfContents';\n\n:::note\nThis is documentation for enabling Tailwind v3.  \nFor the Tailwind v4 version of this site, see the [Tailwind v4 documentation](/docs/tailwind-v4/overview).\n:::\n\nThis package provides utilities useful for integrating [TailwindCSS](https://tailwindcss.com/) with Remotion, as documented on our [TailwindCSS](/docs/tailwind) page.\n\n## Installation\n\nInstall `@remotion/tailwind` as well as TailwindCSS dependencies.\n\n<Installation pkg=\"@remotion/tailwind\" />\n\n<br />\n\n[Override the Webpack config](/docs/webpack) by using [`enableTailwind()`](/docs/tailwind/enable-tailwind).\n\n```ts twoslash title=\"remotion.config.ts\"\nimport {Config} from '@remotion/cli/config';\nimport {enableTailwind} from '@remotion/tailwind';\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableTailwind(currentConfiguration);\n});\n```\n\nThen follow the remaining set up steps from the [TailwindCSS](/docs/tailwind) page.\n\n## APIs\n\n<TableOfContents />\n"

]()]()
]()
- ]()