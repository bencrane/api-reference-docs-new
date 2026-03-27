---
title: "@remotion/skia"
url: "https://www.remotion.dev/docs/skia/"
path: "/docs/skia/"
---

"---\nimage: /generated/articles-docs-skia-skia.png\nid: skia\nsidebar_label: Overview\ntitle: '@remotion/skia'\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {ExperimentalBadge} from '../../components/Experimental';\nimport {TableOfContents} from './TableOfContents';\n\nThis package provides utilities useful for integrating [React Native Skia](https://github.com/Shopify/react-native-skia) with Remotion.\n\n## Installation\n\nInstall, `@remotion/skia` as well as `@shopify/react-native-skia`.\n\n<Installation pkg=\"@remotion/skia @shopify/react-native-skia\" />\n\n:::note\nSince Remotion `v3.3.93` and React Native Skia `0.1.191`, `react-native-web` is not a dependency anymore. You may remove it from your project.\n:::\n\nAlso update **all the other Remotion packages** to have the same version: `remotion`, `@remotion/cli` and others.\n\n:::note\nMake sure no package version number has a `^` character in front of it as it can lead to a version conflict.\n:::\n\n[Override the Webpack config](/docs/webpack) by using [`enableSkia()`](/docs/skia/enable-skia).\n\n```ts twoslash title=\"remotion.config.ts\"\nimport {Config} from '@remotion/cli/config';\nimport {enableSkia} from '@remotion/skia/enable';\n\nConfig.overrideWebpackConfig((currentConfiguration) => {\n  return enableSkia(currentConfiguration);\n});\n```\n\n:::note\nPrior to `v3.3.39`, the option was called `Config.Bundling.overrideWebpackConfig()`.\n:::\n\nNext, you need to refactor the [entry point](/docs/terminology/entry-point) file to first load the Skia WebAssembly binary before calling registerRoot():\n\n```ts twoslash title=\"src/index.ts\"\n// @filename: ./Root.tsx\nexport const RemotionRoot = () => <></>;\n\n// @filename: index.tsx\n// ---cut---\nimport { LoadSkia } from \"@shopify/react-native-skia/src/web\";\nimport { registerRoot } from \"remotion\";\n\n(async () => {\n  await LoadSkia();\n  const { RemotionRoot } = await import(\"./Root\");\n  registerRoot(RemotionRoot);\n})();\n```\n\nYou can now start using the [`<SkiaCanvas>`](/docs/skia/skia-canvas) in your Remotion project.\n\n## Templates\n\nYou can find the [starter template](https://github.com/remotion-dev/template-skia) here or install it using:\n\n<Tabs\ndefaultValue=\"npm\"\nvalues={[\n{ label: 'npm', value: 'npm', },\n{ label: 'bun', value: 'bun', },\n{ label: 'pnpm', value: 'pnpm', },\n{ label: 'yarn', value: 'yarn', },\n]\n}>\n<TabItem value=\"npm\">\n\n```bash\nnpx create-video --skia\n```\n\n  </TabItem>\n    <TabItem value=\"bun\">\n\n```bash\nbun create video --skia\n```\n\n  </TabItem>\n\n  <TabItem value=\"yarn\">\n\n```bash\nyarn create video --skia\n```\n\n  </TabItem>\n\n  <TabItem value=\"pnpm\">\n\n```bash\npnpm create video --skia\n```\n\n  </TabItem>\n</Tabs>\n\n## Rendering\n\nBy default Remotion rendering are done on the CPU. Some Skia effects rely on advanced GPU features, which may be slow to run on the CPU depending on the kind of effect you are using. If your Skia export is extremely slow, we found that enabling the GPU via the `--gl=angle` option improves things substantially. Please check out the documentation on [GPU rendering](/docs/gpu).\n\n```sh\nremotion render Main out/video.mp4 --gl=angle\n```\n\n## Resources\n\n- [Example project by William Candillon](https://github.com/wcandillon/remotion-skia-tutorial)\n- [Tutorial for the example project](https://www.youtube.com/watch?v=-7MOoWN2_nk)\n\n## APIs\n\n<TableOfContents />\n"

This package provides utilities useful for integrating [React Native Skia](https://github.com/Shopify/react-native-skia) with Remotion.

## Installation[​](#installation)

Install, `@remotion/skia` as well as `@shopify/react-native-skia`.

- npm
- bun
- pnpm
- yarn

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection) @shopify/react-native-skiaCopy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection) @shopify/react-native-skiaCopy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection) @shopify/react-native-skiaCopy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection) @shopify/react-native-skiaCopy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.
](/cdn-cgi/l/email-protection)](/cdn-cgi/l/email-protection)
](/cdn-cgi/l/email-protection)
- ](/cdn-cgi/l/email-protection)
- ](/cdn-cgi/l/email-protection)
- ](/cdn-cgi/l/email-protection)
- ](/cdn-cgi/l/email-protection)