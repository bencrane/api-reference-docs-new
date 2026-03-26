---
title: "compositions"
url: "https://www.remotion.dev/docs/cli/compositions"
path: "/docs/cli/compositions"
---

"---\nimage: /generated/articles-docs-cli-compositions.png\ntitle: npx remotion compositions\nsidebar_label: compositions\ncrumb: CLI Reference\n---\n\n<AvailableFrom v=\"2.6.12\" />\n\nPrint list of composition IDs based on a path of an entry point.\n\n```bash\nnpx remotion compositions <serve-url|entry-file>?\n```\n\nYou may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).\n\n## Flags\n\n### `--props`\n\n<Options id=\"props\" />\n\n:::note\nInline JSON string isn't supported on Windows shells because it removes the `\"` character, use a file name instead.\n:::\n\n### `--config`\n\n<Options id=\"config\" />\n\n### `--env-file`<AvailableFrom v=\"2.2.0\" />\n\n<Options id=\"env-file\" />\n\n### `--bundle-cache`\n\n<Options id=\"bundle-cache\" />\n\n### `--log`\n\n[Set the log level](/docs/config#setlevel). Increase or decrease the amount of output. Acceptable values: `error`, `warn`, `info` (_default_), `verbose`\n\n:::info\nIf you don't feel like passing command line flags every time, consider creating a `remotion.config.ts` [config file](/docs/config).\n:::\n\n### `--port`\n\n<Options id=\"port\" />\n\n### `--public-dir`<AvailableFrom v=\"3.2.13\" />\n\n<Options id=\"public-path\" />\n\n### `--timeout`\n\nDefine how long it may take to resolve all [`delayRender()`](/docs/delay-render) calls before the composition fetching times out in milliseconds. Default: `30000`.\n\n:::info\nNot to be confused with the [`--timeout` flag when deploying a Lambda function](/docs/lambda/cli/functions/deploy#--timeout).\n:::\n\n### `--ignore-certificate-errors`\n\n<Options id=\"ignore-certificate-errors\" />\n\n### `--disable-web-security`\n\n<Options id=\"disable-web-security\" />\n\n### ~`--disable-headless`~\n\n<Options id=\"disable-headless\" />\n\n### `--dark-mode`<AvailableFrom v=\"4.0.381\"/>\n\n<Options id=\"dark-mode\" />\n\n### `--enable-multiprocess-on-linux`<AvailableFrom v=\"4.0.42\"/>\n\n<Options cli id=\"enable-multiprocess-on-linux\" />\n\n### `--user-agent`<AvailableFrom v=\"3.3.83\"/>\n\n<Options id=\"user-agent\" />\n\n### `--media-cache-size-in-bytes`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `--offthreadvideo-cache-size-in-bytes`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `--offthreadvideo-video-threads`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `--binaries-directory`<AvailableFrom v=\"4.0.120\" />\n\n<Options cli id=\"binaries-directory\" />\n\n### `--chrome-mode`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n### `--quiet`, `--q`\n\nOnly prints the composition IDs, separated by a space.\n\n### ~~`--ffmpeg-executable`~~\n\n_removed in v4.0_\n\n[Set a custom `ffmpeg` executable](/docs/config#setffmpegexecutable). If not defined, a `ffmpeg` executable will be searched in `PATH`.\n\n### ~~`--ffprobe-executable`~~\n\n_removed in v4.0_\n\n[Set a custom `ffprobe` executable](/docs/config#setffprobeexecutable). If not defined, a `ffprobe` executable will be searched in `PATH`.\n\n## See also\n\n- [`getCompositions()`](/docs/renderer/get-compositions)\n- [`getCompositionsOnLambda()`](/docs/lambda/getcompositionsonlambda)\n- [`npx remotion lambda compositions`](/docs/lambda/cli/compositions)\n"
[v2.6.12](https://github.com/remotion-dev/remotion/releases/v2.6.12)

Print list of composition IDs based on a path of an entry point.

```
npx remotion compositions <serve-url|entry-file>?Copy
```

You may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).

## Flags[​](#flags)

### `--props`[​](#--props)

Input Props to pass to the selected composition of your video. Must be a serialized JSON string (`--props='{"hello": "world"}'`) or a path to a JSON file (`./path/to/props.json`).
](#--props)](#--props)
](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)