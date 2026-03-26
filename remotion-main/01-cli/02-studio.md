---
title: "studio"
url: "https://www.remotion.dev/docs/cli/studio"
path: "/docs/cli/studio"
---

"---\nimage: /generated/articles-docs-cli-studio.png\ntitle: npx remotion studio\nsidebar_label: studio\ncrumb: CLI Reference\n---\n\n_Alias: npx remotion preview_\n\nStart the [Remotion Studio](/docs/studio).\n\n```bash\nnpx remotion studio <entry-point>?\n```\n\nYou may pass an [entry point](/docs/terminology/entry-point) as an argument, otherwise it will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).\n\n## Flags\n\n### `--props`\n\n<Options id=\"props\" />\n\n:::note\nInline JSON string isn't supported on Windows shells because it removes the `\"` character, use a file name instead.\n:::\n\n### `--config`<AvailableFrom v=\"1.2.0\" />\n\n<Options id=\"config\" />\n\n### `--env-file`<AvailableFrom v=\"2.2.0\" />\n\n<Options id=\"env-file\" />\n\n### `--log`\n\n[Set the log level](/docs/config#setlevel). Increase or decrease the amount of output. Acceptable values: `error`, `warn`, `info` (_default_), `verbose`\n\n### `--port`\n\n<Options id=\"port\" />\n\n### `--public-dir`<AvailableFrom v=\"3.2.13\" />\n\n<Options id=\"public-path\" />\n\n### `--disable-keyboard-shortcuts`<AvailableFrom v=\"3.2.11\" />\n\n<Options id=\"disable-keyboard-shortcuts\" />\n\n### `--enable-experimental-client-side-rendering`<AvailableFrom v=\"4.0.387\" />\n\n<Options id=\"enable-experimental-client-side-rendering\" />\n\n### `--experimental-rspack`<AvailableFrom v=\"4.0.426\" />\n\n<Options id=\"experimental-rspack\" />\n\n### `--webpack-poll`<AvailableFrom v=\"3.3.11\" />\n\n<Options id=\"webpack-poll\" />\n\n### `--no-open`<AvailableFrom v=\"3.3.19\" />\n\n<Options id=\"no-open\" />\n\n### `--browser`<AvailableFrom v=\"3.3.79\" />\n\n<Options id=\"browser\" />\n\nYou can also configure the browser via environment variables for backwards compatibility:\n\n- `BROWSER` behaves like the `--browser` flag.\n- `BROWSER_ARGS` behaves like the `--browser-args` flag.\n- Setting `BROWSER=none` disables auto-opening of the browser (equivalent to `--no-open`).\n\n### `--browser-args`<AvailableFrom v=\"3.3.79\" />\n\nA set of command line flags that should be passed to the browser. Pass them like this:\n\n```sh\nnpx remotion studio --browser-args=\"--disable-web-security\"\n```\n\n### `--beep-on-finish`<AvailableFrom v=\"4.0.84\" />\n\n[Plays a beep sound when the video is finished rendering](/docs/config#setbeeponfinish). This is useful if you are rendering a video in the background and want to be notified when it is finished.\n\n```sh\nnpx remotion studio --beep-on-finish\n```\n\n### `--ipv4`<AvailableFrom v=\"4.0.125\" />\n\n<Options id=\"ipv4\" />\n\n```sh\nnpx remotion studio --ipv4\n```\n\n### `--number-of-shared-audio-tags`<AvailableFrom v=\"3.3.2\" />\n\n<Options id=\"number-of-shared-audio-tags\" />\n\n```sh\nnpx remotion studio --number-of-shared-audio-tags=5\n```\n\n### `--cross-site-isolation`<AvailableFrom v=\"4.0.364\" />\n\n[Enable Cross-Site Isolation in the Studio](/docs/config#setenablecrosssiteisolation).\n\n```sh\nnpx remotion studio --enable-cross-site-isolation\n```\n\n### `--disable-ask-ai`<AvailableFrom v=\"4.0.407\" />\n\n[Disable the Ask AI modal in the Studio](/docs/config#setaskaienabled).\n\n```sh\nnpx remotion studio --disable-ask-ai\n```\n\n### `--force-new`<AvailableFrom v=\"4.0.421\" />\n\n<Options id=\"force-new\" />\n\n```sh\nnpx remotion studio --force-new\n```\n\n### `--public-license-key`<AvailableFrom v=\"4.0.398\" />\n\n<Options id=\"public-license-key\" />\n\n```sh\nnpx remotion studio --public-license-key=\"your-license-key\"\n```\n"

*Alias: npx remotion preview*

Start the [Remotion Studio](/docs/studio).

```
npx remotion studio <entry-point>?Copy
```

You may pass an [entry point](/docs/terminology/entry-point) as an argument, otherwise it will be [determined](/docs/terminology/entry-point#which-entry-point-is-being-used).

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