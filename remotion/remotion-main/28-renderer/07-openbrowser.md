---
title: "openBrowser()"
url: "https://www.remotion.dev/docs/renderer/open-browser"
path: "/docs/renderer/open-browser"
---

"---\nimage: /generated/articles-docs-renderer-open-browser.png\ntitle: openBrowser()\nid: open-browser\ncrumb: '@remotion/renderer'\n---\n\n_Available since v3.0 - Part of the `@remotion/renderer` package._\n\nOpens a Chrome or Chromium browser instance. By reusing an instance across [`renderFrames()`](/docs/renderer/render-frames), [`renderStill()`](/docs/renderer/render-still), [`renderMedia()`](/docs/renderer/render-media) and [`getCompositions()`](/docs/renderer/get-compositions) calls, you can save time by not opening and closing browsers for each call.\n\n```ts\nconst openBrowser: (\n  browser: Browser,\n  options: {\n    shouldDumpIo?: boolean;\n    browserExecutable?: string | null;\n    chromiumOptions?: ChromiumOptions;\n  },\n) => Promise<puppeteer.Browser>;\n```\n\n## Arguments\n\n### `browser`\n\nCurrently the only valid option is `\"chrome\"`. This field is reserved for future compatibility with other browsers.\n\n### `options?`\n\nAn object containing one or more of the following options:\n\n#### ~`shouldDumpIo?`~\n\nDeprecated since v4.0.189, scheduled for removal in v5.0.\n\nIf set to `true`, logs and other browser diagnostics are being printed to standard output. This setting is useful for debugging.  \n**Will be removed in 5.0:** Use `logLevel` instead.\n\n#### `logLevel?`<AvailableFrom v=\"4.0.189\"/>\n\n<Options id=\"log\" />\n\n#### `browserExecutable?`\n\nA string defining the absolute path on disk of the browser executable that should be used. By default Remotion will try to detect it automatically and download one if none is available. If `puppeteerInstance` is defined, it will take precedence over `browserExecutable`.\n\n#### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n:::note\nChromium flags need to be set at browser launch. If you pass an instance to SSR APIs like [`renderMedia()`](/docs/renderer/render-media), the `chromiumOptions` option of that API will not apply, but rather the flags that have been passed to `openBrowser()`.\n:::\n\n#### `forceDeviceScaleFactor?`\n\nSet a [scale](/docs/scaling). If you plan to use scaling, you already need to set it when opening the browser.\n\n#### `onBrowserDownload?`<AvailableFrom v=\"4.0.137\" />\n\n<Options id=\"on-browser-download\" />\n\n### `chromeMode?`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n## Closing the browser\n\nUse the `close()` method to cleanup a browser you are not using anymore:\n\n```ts\nconst browser = await openBrowser('chrome');\nbrowser.close({silent: true});\n```\n\nIf already closed or an operation is interrupted, an error is thrown.  \nSetting the `silent` option to `true` will close the browser without generating an error.\n\n## Compatibility\n\n<CompatibilityTable chrome={false} firefox={false} safari={false} nodejs={true} bun={true} serverlessFunctions={false} clientSideRendering={false} serverSideRendering={true} player={false} studio={false} />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/open-browser.ts)\n- [Server-Side rendering](/docs/ssr)\n"

*Available since v3.0 - Part of the `@remotion/renderer` package.*

Opens a Chrome or Chromium browser instance. By reusing an instance across [`renderFrames()`](/docs/renderer/render-frames), [`renderStill()`](/docs/renderer/render-still), [`renderMedia()`](/docs/renderer/render-media) and [`getCompositions()`](/docs/renderer/get-compositions) calls, you can save time by not opening and closing browsers for each call.

```
const openBrowser: (
  browser: Browser,
  options: {
    shouldDumpIo?: boolean;
    browserExecutable?: string | null;
    chromiumOptions?: ChromiumOptions;
  },
) => Promise<puppeteer.Browser>;Copy
```

## Arguments[​](#arguments)

### `browser`[​](#browser)

Currently the only valid option is `"chrome"`. This field is reserved for future compatibility with other browsers.

### `options?`[​](#options)

An object containing one or more of the following options:

#### `shouldDumpIo?`[​](#shoulddumpio)

Deprecated since v4.0.189, scheduled for removal in v5.0.

If set to `true`, logs and other browser diagnostics are being printed to standard output. This setting is useful for debugging.

**Will be removed in 5.0:** Use `logLevel` instead.

#### `logLevel?`[v4.0.189](https://github.com/remotion-dev/remotion/releases/v4.0.189)[​](#loglevel)

One of `trace`, `verbose`, `info`, `warn`, `error`.
 Determines how much info is being logged to the console.

 Default `info`.

#### `browserExecutable?`[​](#browserexecutable)

A string defining the absolute path on disk of the browser executable that should be used. By default Remotion will try to detect it automatically and download one if none is available. If `puppeteerInstance` is defined, it will take precedence over `browserExecutable`.

#### `chromiumOptions?`[​](#chromiumoptions)

Allows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).
](/docs/chromium-flags)](/docs/chromium-flags)
](/docs/chromium-flags)
- ](/docs/chromium-flags)
- ](/docs/chromium-flags)
- ](/docs/chromium-flags)
- ](/docs/chromium-flags)
- ](/docs/chromium-flags)
- ](/docs/chromium-flags)