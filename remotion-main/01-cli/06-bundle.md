---
title: "bundle"
url: "https://www.remotion.dev/docs/cli/bundle"
path: "/docs/cli/bundle"
---

"---\nimage: /generated/articles-docs-cli-bundle.png\ntitle: npx remotion bundle\nsidebar_label: bundle\ncrumb: CLI Reference\n---\n\n_available from v4.0.89_\n\nCreates a [Remotion Bundle](/docs/terminology/bundle) on the command line.  \nEquivalent to the [`bundle()`](/docs/bundle) Node.JS API.\n\n```bash\nnpx remotion bundle <serve-url|entry-file>?\n```\n\nYou may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).\n\n## Flags\n\n### `--config`\n\n<Options id=\"config\" />\n\n### `--log`\n\n<Options id=\"log\" />\n\n### `--public-dir`\n\n<Options id=\"public-dir\" />\n\n### `--out-dir`\n\n<Options id=\"out-dir\" />\n\n### `--public-path`<AvailableFrom v=\"4.0.127\"/>\n\n<Options id=\"public-path\" />\n\n### `--disable-git-source`<AvailableFrom v=\"4.0.182\" />\n\n<Options id=\"disable-git-source\" />\n\n### `--experimental-rspack`<AvailableFrom v=\"4.0.426\" />\n\n<Options id=\"experimental-rspack\" />\n"

*available from v4.0.89*

Creates a [Remotion Bundle](/docs/terminology/bundle) on the command line.

Equivalent to the [`bundle()`](/docs/bundle) Node.JS API.

```
npx remotion bundle <serve-url|entry-file>?Copy
```

You may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).

## Flags[​](#flags)

### `--config`[​](#--config)

Specify a location for the Remotion config file.

### `--log`[​](#--log)

One of `trace`, `verbose`, `info`, `warn`, `error`.
 Determines how much info is being logged to the console.

 Default `info`.

### `--public-dir`[​](#--public-dir)

Define the location of the [`public/ directory`](/docs/terminology/public-dir). If not defined, Remotion will assume the location is the `public` folder in your Remotion root.

### `--out-dir`[​](#--out-dir)

Define the location of the resulting bundle. By default it is a folder called `build`, adjacent to the [Remotion Root](/docs/terminology/remotion-root).

### `--public-path`[v4.0.127](https://github.com/remotion-dev/remotion/releases/v4.0.127)[​](#--public-path)

The path of the URL where the bundle is going to be hosted. By default it is `/`, meaning that the bundle is going to be hosted at the root of the domain (e.g. `https://localhost:3000/`). If you are deploying to a subdirectory (e.g. `/sites/my-site/`), you should set this to the subdirectory.

### `--disable-git-source`[v4.0.182](https://github.com/remotion-dev/remotion/releases/v4.0.182)[​](#--disable-git-source)

Disables the Git Source being connected to the Remotion Studio. Clicking on stack traces and certain menu items will be disabled.

### `--experimental-rspack`[v4.0.426](https://github.com/remotion-dev/remotion/releases/v4.0.426)[​](#--experimental-rspack)

Uses Rspack instead of Webpack as the bundler for the Studio or bundle.](#--experimental-rspack)](#--experimental-rspack)
](#--experimental-rspack)
- ](#--experimental-rspack)
- ](#--experimental-rspack)
- ](#--experimental-rspack)
- ](#--experimental-rspack)
- ](#--experimental-rspack)
- ](#--experimental-rspack)
- ](#--experimental-rspack)