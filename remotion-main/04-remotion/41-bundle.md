---
title: "bundle()"
url: "https://www.remotion.dev/docs/bundle"
path: "/docs/bundle"
---

"---\nimage: /generated/articles-docs-bundle.png\nid: bundle\ntitle: bundle()\ncrumb: '@remotion/bundler'\n---\n\n_Part of the `@remotion/bundler` package._\n\nBundles a Remotion project using Webpack and prepares it for rendering using [`renderMedia()`](/docs/renderer/render-media). [See a full server-side rendering example.](/docs/ssr-node)\n\nYou only need to call this function when the source code changes. You can render multiple videos from the same bundle and parametrize them using [input props](/docs/passing-props).\n\nCalling `bundle()` for every video that you render is an anti-pattern.  \n`bundle()` cannot be called in a serverless function, see: [Calling bundle() in bundled code](/docs/troubleshooting/bundling-bundle).\n\n## Example\n\n```tsx twoslash title=\"render.mjs\"\nimport path from 'path';\nimport {bundle} from '@remotion/bundler';\n\nconst serveUrl = await bundle({\n  entryPoint: path.join(process.cwd(), './src/index.ts'),\n  // If you have a webpack override in remotion.config.ts, pass it here as well.\n  webpackOverride: (config) => config,\n});\n```\n\n## Arguments\n\n### `entryPoint`\n\nA `string` containing an absolute path of the entry point of a Remotion project. [In most Remotion project created with the template, the entry point is located at `src/index.ts`](/docs/terminology/entry-point).\n\n### `onProgress?`\n\nA callback function that notifies about the progress of the Webpack bundling. Passes a number between `0` and `100`. Example function:\n\n```ts twoslash\nconst onProgress = (progress: number) => {\n  console.log(`Webpack bundling progress: ${progress}%`);\n};\n```\n\n### `webpackOverride?`\n\nA function to override the webpack config reducer-style. Takes a function which gives you the current webpack config which you can transform and return a modified version of it. For example:\n\n```ts twoslash\nimport {WebpackOverrideFn} from '@remotion/bundler';\n// ---cut---\nconst webpackOverride: WebpackOverrideFn = (webpackConfig) => {\n  return {\n    ...webpackConfig,\n    // Override properties\n  };\n};\n```\n\n### `outDir?`\n\nSpecify a desired output directory. If no passed, the webpack bundle will be created in a temp dir.\n\n### `askAIEnabled?`\n\n<Options id=\"disable-ask-ai\" />\n\n### `rspack?`\n\nWhether to use [Rspack](https://rspack.dev) instead of Webpack as the bundler. Default `false`.\n\n### `keyboardShortcutsEnabled?`\n\n<Options id=\"disable-keyboard-shortcuts\" />\n\n### `enableCaching?`\n\n<Options id=\"bundle-cache\" />\n\n### `publicPath?`\n\n<Options id=\"public-path\" />\n\n### `rootDir?`<AvailableFrom v=\"3.1.6\" />\n\nThe directory in which the Remotion project is rooted in. This should be set to the directory that contains the `package.json` which installs Remotion. By default, it is the current working directory.\n\n:::note\nThe current working directory is the directory from which your program gets executed from. It is not the same as the file where bundle() gets called.\n:::\n\n### `publicDir?`<AvailableFrom v=\"3.2.13\" />\n\n<Options id=\"public-dir\" />\n\n### `onPublicDirCopyProgress?`<AvailableFrom v=\"3.3.3\" />\n\nReports progress of how many bytes have been written while copying the `public/` directoy. Useful to warn the user if the directory is large that this operation is slow.\n\n### `onSymlinkDetected?`<AvailableFrom v=\"3.3.3\" />\n\nGets called when a symbolic link is detected in the `public/` directory. Since Remotion will forward the symbolic link, it might be useful to display a hint to the user that if the original symbolic link gets deleted, the bundle will also break.\n\n### `ignoreRegisterRootWarning?`<AvailableFrom v=\"3.3.46\" />\n\nIgnore an error that gets thrown if you pass an entry point file which does not contain `registerRoot`.\n\n## Legacy function signature\n\nRemotion versions earlier than v3.2.17 had the following function signature instead:\n\n```ts\nconst bundle: (\n  entryPoint: string,\n  onProgress?: (progress: number) => void,\n  options?: {\n    webpackOverride?: WebpackOverrideFn;\n    outDir?: string;\n    enableCaching?: boolean;\n    publicPath?: string;\n    rootDir?: string;\n    publicDir?: string | null;\n  },\n) => Promise<string>;\n```\n\nExample:\n\n```ts\nawait bundle('src/index.ts', () => console.log(progress * 100 + '% done'), {\n  webpackOverride,\n});\n```\n\nIt is still supported in Remotion v3, but we encourage to migrate to the new function signature.\n\n## Return value\n\nA promise which will resolve into a `string` specifying the output directory.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/bundler/src/bundle.ts)\n- [Server-Side rendering](/docs/ssr)\n- [getCompositions()](/docs/renderer/get-compositions)\n- [renderMedia()](/docs/renderer/render-media)\n- [stitchFramesToVideo()](/docs/renderer/stitch-frames-to-video)\n- [Calling bundle() in bundled code](/docs/troubleshooting/bundling-bundle)\n"

*Part of the `@remotion/bundler` package.*

Bundles a Remotion project using Webpack and prepares it for rendering using [`renderMedia()`](/docs/renderer/render-media). [See a full server-side rendering example.](/docs/ssr-node)

You only need to call this function when the source code changes. You can render multiple videos from the same bundle and parametrize them using [input props](/docs/passing-props).

Calling `bundle()` for every video that you render is an anti-pattern.

`bundle()` cannot be called in a serverless function, see: [Calling bundle() in bundled code](/docs/troubleshooting/bundling-bundle).

## Example[​](#example)

```

render.mjsimport path from 'path';
import {bundle} from '@remotion/bundler';

const serveUrl = await bundle({
  entryPoint: path.join(process.cwd(), './src/index.ts'),
  // If you have a webpack override in remotion.config.ts, pass it here as well.
  webpackOverride: (config) => config,
});Copy
```

## Arguments[​](#arguments)

### `entryPoint`[​](#entrypoint)

A `string` containing an absolute path of the entry point of a Remotion project. [In most Remotion project created with the template, the entry point is located at `src/index.ts`](/docs/terminology/entry-point).

### `onProgress?`[​](#onprogress)

A callback function that notifies about the progress of the Webpack bundling. Passes a number between `0` and `100`. Example function:

```
const onProgress = (progress: number) => {
  console.log(`Webpack bundling progress: ${progress}%`);
};Copy
```

### `webpackOverride?`[​](#webpackoverride)

A function to override the webpack config reducer-style. Takes a function which gives you the current webpack config which you can transform and return a modified version of it. For example:

```
const webpackOverride: WebpackOverrideFn = (webpackConfig) => {
  return {
    ...webpackConfig,
    // Override properties
  };
};Copy
```

### `outDir?`[​](#outdir)

Specify a desired output directory. If no passed, the webpack bundle will be created in a temp dir.

### `askAIEnabled?`[​](#askaienabled)

If the Cmd + I shortcut of the Ask AI modal conflicts with your Studio, you can disable it using this.

### `rspack?`[​](#rspack)

Whether to use [Rspack](https://rspack.dev) instead of Webpack as the bundler. Default `false`.

### `keyboardShortcutsEnabled?`[​](#keyboardshortcutsenabled)

Enable or disable keyboard shortcuts in the Remotion Studio.

### `enableCaching?`[​](#enablecaching)

Enable or disable Webpack caching. This flag is enabled by default, use `--bundle-cache=false` to disable caching.

### `publicPath?`[​](#publicpath)

The path of the URL where the bundle is going to be hosted. By default it is `/`, meaning that the bundle is going to be hosted at the root of the domain (e.g. `https://localhost:3000/`). If you are deploying to a subdirectory (e.g. `/sites/my-site/`), you should set this to the subdirectory.

### `rootDir?`[v3.1.6](https://github.com/remotion-dev/remotion/releases/v3.1.6)[​](#rootdir)

The directory in which the Remotion project is rooted in. This should be set to the directory that contains the `package.json` which installs Remotion. By default, it is the current working directory.
](#rootdir)](#rootdir)
](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)
- ](#rootdir)