---
title: "@remotion/lottie"
url: "https://www.remotion.dev/docs/lottie/"
path: "/docs/lottie/"
---

"---\nimage: /generated/articles-docs-lottie-index.png\nid: lottie-index\nsidebar_label: Overview\ntitle: \"@remotion/lottie\"\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {TableOfContents} from \"./table-of-contents\"\n\nThis package provides a component for displaying [Lottie](http://airbnb.io/lottie/) animations in Remotion.\n\n## Installation\n\nInstall, `@remotion/lottie` as well as `lottie-web`.\n\n<Tabs\ndefaultValue=\"npm\"\nvalues={[\n{ label: 'npm', value: 'npm', },\n{ label: 'yarn', value: 'yarn', },\n{ label: 'pnpm', value: 'pnpm', },\n]\n}>\n<TabItem value=\"npm\">\n\n```bash\nnpm i @remotion/lottie lottie-web\n```\n\n  </TabItem>\n\n  <TabItem value=\"yarn\">\n\n```bash\nyarn add @remotion/lottie lottie-web\n```\n\n  </TabItem>\n\n  <TabItem value=\"pnpm\">\n\n```bash\npnpm i @remotion/lottie lottie-web\n```\n\n  </TabItem>\n</Tabs>\n\nYou can now start using the [`<Lottie>`](/docs/lottie/lottie) component in your Remotion project.\n\n## Supported features\n\n- Playing Lottie animations using `lottie-web`\n- Change the speed of the animation\n- Playing animation forwards and backwards\n- Playing remote files\n- Determining dimensions and duration of a Lottie animation\n\n## Unsupported features\n\n- Rendering on other renderers as `svg`\n- `setSubFrame()`, `setLocationHref()`\n- Limited expression support: Remotion uses the `.goToAndStop()` method from `lottie-web` to seek through the Lottie file. Depending on the expression, the frame might not render deterministally, leading to [flickering](/docs/flickering) in the Remotion output. Remotion cannot fix this without a change in `lottie-web` upstream. You need to evaluate on a case-by-case basis whether the expression you are using is supported by Remotion.\n\n:::note\n[Open an issue](https://remotion.dev/issue) if you want to request a currently unsupported feature.\n:::\n\n## Table of contents\n\n<TableOfContents />\n\n## License\n\n[Remotion License](https://remotion.dev/license)\n"

This package provides a component for displaying [Lottie](http://airbnb.io/lottie/) animations in Remotion.

## Installation[​](#installation)

Install, `@remotion/lottie` as well as `lottie-web`.

- npm
- yarn
- pnpm

```
npm i @remotion/lottie lottie-webCopy
```

```
yarn add @remotion/lottie lottie-webCopy
```

```
pnpm i @remotion/lottie lottie-webCopy
```

You can now start using the [`<Lottie>`](/docs/lottie/lottie) component in your Remotion project.

## Supported features[​](#supported-features)

- Playing Lottie animations using `lottie-web`

- Change the speed of the animation

- Playing animation forwards and backwards

- Playing remote files

- Determining dimensions and duration of a Lottie animation

## Unsupported features[​](#unsupported-features)

- Rendering on other renderers as `svg`

- `setSubFrame()`, `setLocationHref()`

- Limited expression support: Remotion uses the `.goToAndStop()` method from `lottie-web` to seek through the Lottie file. Depending on the expression, the frame might not render deterministally, leading to [flickering](/docs/flickering) in the Remotion output. Remotion cannot fix this without a change in `lottie-web` upstream. You need to evaluate on a case-by-case basis whether the expression you are using is supported by Remotion.

](/docs/flickering)](/docs/flickering)
](/docs/flickering)
- ](/docs/flickering)
- ](/docs/flickering)
- ](/docs/flickering)
- ](/docs/flickering)