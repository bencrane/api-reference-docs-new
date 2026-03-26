---
title: "render"
url: "https://www.remotion.dev/docs/cli/render"
path: "/docs/cli/render"
---

"---\nimage: /generated/articles-docs-cli-render.png\ntitle: npx remotion render\nsidebar_label: render\ncrumb: CLI Reference\n---\n\nRender a video or audio based on the entry point, the composition ID and save it to the output location.\n\n```bash\nnpx remotion render <entry-point|serve-url>? <composition-id> <output-location>\n```\n\nYou may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).\n\nIf `composition-id` is not passed, Remotion will ask you to select a composition.  \nIf `output-location` is not passed, the media will be rendered into the `out` folder.\n\n## Flags\n\nBesides choosing a video and output location with the command line arguments, the following flags are supported:\n\n### `--props`\n\n<Options id=\"props\" />\n\n:::note\nInline JSON string isn't supported on Windows shells because it removes the `\"` character, use a file name instead.\n:::\n\n### `--height`<AvailableFrom v=\"3.2.40\" />\n\n<Options id=\"height\" cli />\n\n### `--width`<AvailableFrom v=\"3.2.40\" />\n\n<Options id=\"width\" cli />\n\n### `--fps`<AvailableFrom v=\"4.0.424\" />\n\n<Options id=\"fps\" cli />\n\n### `--duration`<AvailableFrom v=\"4.0.424\" />\n\n<Options id=\"duration\" cli />\n\n### `--concurrency`\n\n<Options id=\"concurrency\" />\n\n### `--pixel-format`\n\n<Options id=\"pixel-format\" />\n\n### `--image-format`<AvailableFrom v=\"1.4.0\" />\n\n<Options id=\"video-image-format\" />\n\n### `--image-sequence-pattern` <AvailableFrom v=\"4.0.313\" />\n\n<Options id=\"image-sequence-pattern\" />\n\n### `--config`<AvailableFrom v=\"1.2.0\" />\n\n<Options id=\"config\" />\n\n### `--env-file`<AvailableFrom v=\"2.2.0\" />\n\n<Options id=\"env-file\" />\n\n### `--jpeg-quality`<AvailableFrom v=\"4.0.0\" />\n\n[Value between 0 and 100 for JPEG rendering quality](/docs/config#setjpegquality). Doesn't work when PNG frames are rendered.\n\n### ~~`--quality`~~<AvailableFrom v=\"1.4.0\" />\n\nRenamed to `--jpeg-quality` in v4.0.0\n\n### `--output` <AvailableFrom v=\"4.0.0\" />\n\nSets the output file path, as an alternative to the `output-location` positional argument.\n\n### `--overwrite`\n\n[Write to output even if file already exists.](/docs/config#setoverwriteoutput). This flag is enabled by default, use `--overwrite=false` to disable it.\n\n### `--sequence`<AvailableFrom v=\"1.4.0\" />\n\n<Options id=\"sequence\" />\n\n### `--codec`<AvailableFrom v=\"1.4.0\" />\n\n[`h264` or `h265` or `av1` or `png` or `vp8` or `vp9` or `mp3` or `aac` or `wav` or `prores` or `h264-mkv`](/docs/config#setcodec). If you don't supply `--codec`, it will use the H.264 encoder.\n\nIf you are rendering on Linux ARM64 GNU, `av1` is not available.\n\n### `--audio-codec`<AvailableFrom v=\"3.3.42\" />\n\n<Options id=\"audio-codec\" />\n\n### `--audio-bitrate`<AvailableFrom v=\"3.2.32\" />\n\n<Options id=\"audio-bitrate\" />\n\n### `--video-bitrate`<AvailableFrom v=\"3.2.32\" />\n\n<Options id=\"video-bitrate\" />\n\n### `--buffer-size`<AvailableFrom v=\"4.0.78\" />\n\n<Options id=\"buffer-size\" />\n\n### `--max-rate`<AvailableFrom v=\"4.0.78\" />\n\n<Options id=\"max-rate\" />\n\n### `--prores-profile`<AvailableFrom v=\"2.1.6\" />\n\n<Options id=\"prores-profile\" />\n\n### `--x264-preset`<AvailableFrom v=\"4.2.2\" />\n\n<Options id=\"x264-preset\" />\n\n### `--crf`<AvailableFrom v=\"1.4.0\" />\n\n[To set Constant Rate Factor (CRF) of the output](/docs/config#setcrf). Minimum 0. Use this rate control mode if you want to keep the best quality and care less about the file size. This option cannot be set if `--video-bitrate` is set.\n\n:::note\nIf you enable [hardware acceleration](/docs/hardware-acceleration), you cannot set a `crf`. Use the [`--video-bitrate`](#--video-bitrate) option instead.\n:::\n\n### `--browser-executable`<AvailableFrom v=\"1.5.0\" />\n\n<Options id=\"browser-executable\" />\n\n### `--chrome-mode`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n### `--scale`\n\n[Scales the output frames by the factor you pass in.](/docs/scaling) For example, a 1280x720px frame will become a 1920x1080px frame with a scale factor of `1.5`. Vector elements like fonts and HTML markups will be rendered with extra details. `scale` must be greater than 0 and less than equal to 16. Default: `1`.\n\n### `--frames`<AvailableFrom v=\"2.0.0\" />\n\n<Options id=\"frames\" />\n\n### `--every-nth-frame`<AvailableFrom v=\"3.1.0\" />\n\n<Options id=\"every-nth-frame\" />\n\nFor example only every second frame, every third frame and so on. Only works for rendering GIFs. [See here for more details.](/docs/render-as-gif#reducing-frame-rate)\n\n### `--muted`<AvailableFrom v=\"3.2.1\" />\n\n[Disables audio output.](/docs/cli/render#--muted) This option may only be used when rendering a video.\n\n### `--enforce-audio-track`<AvailableFrom v=\"3.2.1\" />\n\n[Render a silent audio track if there wouldn't be one otherwise.](/docs/cli/render#--enforce-audio-track).\n\n### `--disallow-parallel-encoding`<AvailableFrom v=\"4.0.315\" />\n\nDisallows the renderer from doing rendering frames and encoding at the same time. This makes the rendering process more memory-efficient, but possibly slower.\n\n### `--number-of-gif-loops`<AvailableFrom v=\"3.1.0\" />\n\n<Options id=\"number-of-gif-loops\" />\n\n### `--color-space`<AvailableFrom v=\"4.0.28\"/>\n\n<Options cli id=\"color-space\" />\n\n### `--hardware-acceleration`<AvailableFrom v=\"4.0.228\" />\n\n<Options cli id=\"hardware-acceleration\" />\n\n### `--bundle-cache`<AvailableFrom v=\"2.0.0\" />\n\n<Options id=\"bundle-cache\" />\n\n### `--log`\n\n[Set the log level](/docs/config#setlevel). Increase or decrease the amount of output. Acceptable values: `error`, `warn`, `info` (_default_), `verbose`\n\n### `--port`\n\n<Options id=\"port\" />\n\n### `--public-dir`<AvailableFrom v=\"3.2.13\" />\n\n<Options id=\"public-path\" />\n\n### `--timeout`\n\nDefine how long a single frame may take to resolve all [`delayRender()`](/docs/delay-render) calls [before it times out](/docs/timeout) in milliseconds. Default: `30000`.\n\n:::info\nNot to be confused with the [`--timeout` flag when deploying a Lambda function](/docs/lambda/cli/functions/deploy#--timeout).\n:::\n\n### `--ignore-certificate-errors`<AvailableFrom v=\"2.6.5\" />\n\n<Options id=\"ignore-certificate-errors\" />\n\n### `--disable-web-security`<AvailableFrom v=\"2.6.5\" />\n\n<Options id=\"disable-web-security\" />\n\n### ~`--disable-headless`~<AvailableFrom v=\"2.6.5\" />\n\n<Options id=\"disable-headless\" />\n\n### `--dark-mode`<AvailableFrom v=\"4.0.381\"/>\n\n<Options id=\"dark-mode\" />\n\n### `--gl`\n\n<Options id=\"gl\" cli />\n\n### `--user-agent`<AvailableFrom v=\"3.3.83\"/>\n\n<Options id=\"user-agent\" />\n\n### `--media-cache-size-in-bytes`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `--offthreadvideo-cache-size-in-bytes`<AvailableFrom v=\"4.0.23\"/>\n\n<Options cli id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `--offthreadvideo-video-threads`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `--enable-multiprocess-on-linux`<AvailableFrom v=\"4.0.42\"/>\n\n<Options cli id=\"enable-multiprocess-on-linux\" />\n\n### `--repro`<AvailableFrom v=\"4.0.88\" />\n\n<Options id=\"repro\" />\n\n### `--binaries-directory`<AvailableFrom v=\"4.0.120\" />\n\n<Options cli id=\"binaries-directory\" />\n\n### `--experimental-rspack`<AvailableFrom v=\"4.0.426\" />\n\n<Options id=\"experimental-rspack\" />\n\n### `--for-seamless-aac-concatenation`<AvailableFrom v=\"4.0.123\" />\n\n<Options cli id=\"for-seamless-aac-concatenation\" />\n\n### `--separate-audio-to`<AvailableFrom v=\"4.0.123\" />\n\n<Options cli id=\"separate-audio-to\" />\n\n### `--metadata`<AvailableFrom v=\"4.0.216\" />\n\n<Options cli id=\"metadata\" />\n\n### ~~`--ffmpeg-executable`~~\n\n_removed in v4.0_\n\n[Set a custom `ffmpeg` executable](/docs/config#setffmpegexecutable). If not defined, a `ffmpeg` executable will be searched in `PATH`.\n\n### ~~`--ffprobe-executable`~~ <AvailableFrom v=\"3.0.17\" />\n\n_removed in v4.0_\n\n[Set a custom `ffprobe` executable](/docs/config#setffprobeexecutable). If not defined, a `ffprobe` executable will be searched in `PATH`.\n"

Render a video or audio based on the entry point, the composition ID and save it to the output location.

```
npx remotion render <entry-point|serve-url>? <composition-id> <output-location>Copy
```

You may pass a [Serve URL](/docs/terminology/serve-url) or an [entry point](/docs/terminology/entry-point) as the first argument, otherwise the entry point will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).

If `composition-id` is not passed, Remotion will ask you to select a composition.

If `output-location` is not passed, the media will be rendered into the `out` folder.

## Flags[​](#flags)

Besides choosing a video and output location with the command line arguments, the following flags are supported:

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