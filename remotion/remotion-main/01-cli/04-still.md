---
title: "still"
url: "https://www.remotion.dev/docs/cli/still"
path: "/docs/cli/still"
---

"---\nimage: /generated/articles-docs-cli-still.png\ntitle: npx remotion still\nsidebar_label: still\ncrumb: CLI Reference\n---\n\n<AvailableFrom v=\"2.3\" />\n\nRender a still frame based on the entry point, the composition ID and save it to the output location.\n\n```bash\nnpx remotion still <serve-url|entry-point>? [<composition-id>] [<output-location>]\n```\n\nYou may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).\n\nIf `output-location` is not passed, the still will be rendered into the `out` folder.  \nIf `composition-id` is also not passed, Remotion will let you select a composition.\n\n## Flags\n\n### `--props`\n\n<Options id=\"props\" />\n\n:::note\nInline JSON string isn't supported on Windows shells because it removes the `\"` character, use a file name instead.\n:::\n\n### `--image-format`\n\n<Options id=\"still-image-format\" />\n\n### `--config`\n\n<Options id=\"config\" />\n\n### `--env-file`\n\n<Options id=\"env-file\" />\n\n### `--jpeg-quality` <AvailableFrom v=\"4.0.0\" />\n\n[Value between 0 and 100 for JPEG rendering quality](/docs/config#setjpegquality). Doesn't work when PNG frames are rendered.\n\n### ~~`--quality`~~ <AvailableFrom v=\"1.4.0\" />\n\nRenamed to `--jpeg-quality` in v4.0.0\n\n### `--output` <AvailableFrom v=\"4.0.0\" />\n\nSets the output file path, as an alternative to the `output-location` positional argument.\n\n### `--overwrite`\n\n[Write to output even if file already exists.](/docs/config#setoverwriteoutput). This flag is enabled by default, use `--overwrite=false` to disable it.\n\n### `--browser-executable`\n\n<Options id=\"browser-executable\" />\n\n### `--scale`\n\n[Scales the output frames by the factor you pass in.](/docs/scaling) For example, a 1280x720px frame will become a 1920x1080px frame with a scale factor of `1.5`. Vector elements like fonts and HTML markups will be rendered with extra details. `scale` must be greater than 0 and less than equal to 16. Default: `1`.\n\n### `--frame`\n\n<Options id=\"frame\" />\n\n### `--bundle-cache`\n\n<Options id=\"bundle-cache\" />\n\n### `--log`\n\n[Set the log level](/docs/config#setlevel). Increase or decrease the amount of output. Acceptable values: `error`, `warn`, `info` (_default_), `verbose`\n\n### `--port`\n\n<Options id=\"port\" />\n\n### `--public-dir`<AvailableFrom v=\"3.2.13\" />\n\n<Options id=\"public-path\" />\n\n### `--timeout`\n\nDefine how long a single frame may take to resolve all [`delayRender()`](/docs/delay-render) calls [before it times out](/docs/timeout) in milliseconds. Default: `30000`.\n\n:::info\nNot to be confused with the [`--timeout` flag when deploying a Lambda function](/docs/lambda/cli/functions/deploy#--timeout).\n:::\n\n### `--ignore-certificate-errors`<AvailableFrom v=\"2.6.5\" />\n\n<Options id=\"ignore-certificate-errors\" />\n\n### `--disable-web-security`<AvailableFrom v=\"2.6.5\" />\n\n<Options id=\"disable-web-security\" />\n\n### ~`--disable-headless`~<AvailableFrom v=\"2.6.5\" />\n\n<Options id=\"disable-headless\" />\n\n### `--dark-mode`<AvailableFrom v=\"4.0.381\"/>\n\n<Options id=\"dark-mode\" />\n\n### `--chrome-mode`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n### `--gl`\n\n<Options id=\"gl\" cli />\n\n### `--user-agent`<AvailableFrom v=\"3.3.83\"/>\n\n<Options id=\"user-agent\" />\n\n### `--media-cache-size-in-bytes`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `--offthreadvideo-cache-size-in-bytes`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `--offthreadvideo-video-threads`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `--enable-multiprocess-on-linux`<AvailableFrom v=\"4.0.42\"/>\n\n<Options cli id=\"enable-multiprocess-on-linux\" />\n\n### `--binaries-directory`<AvailableFrom v=\"4.0.120\" />\n\n<Options cli id=\"binaries-directory\" />\n\n### `--experimental-rspack`<AvailableFrom v=\"4.0.426\" />\n\n<Options id=\"experimental-rspack\" />\n\n### ~~`--ffmpeg-executable`~~\n\n_removed in v4.0_\n\n[Set a custom `ffmpeg` executable](/docs/config#setffmpegexecutable). If not defined, a `ffmpeg` executable will be searched in `PATH`.\n\n### ~~`--ffprobe-executable`~~\n\n_removed in v4.0_\n\n[Set a custom `ffprobe` executable](/docs/config#setffprobeexecutable). If not defined, a `ffprobe` executable will be searched in `PATH`.\n"
[v2.3](https://github.com/remotion-dev/remotion/releases/v2.3)

Render a still frame based on the entry point, the composition ID and save it to the output location.

```
npx remotion still <serve-url|entry-point>? [<composition-id>] [<output-location>]Copy
```

You may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).

If `output-location` is not passed, the still will be rendered into the `out` folder.

If `composition-id` is also not passed, Remotion will let you select a composition.

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
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)
- ](#--props)