---
title: "ensureBrowser()"
url: "https://www.remotion.dev/docs/renderer/ensure-browser"
path: "/docs/renderer/ensure-browser"
---

"---\nimage: /generated/articles-docs-renderer-ensure-browser.png\ntitle: ensureBrowser()\nid: ensure-browser\ncrumb: '@remotion/renderer'\n---\n\n# ensureBrowser()<AvailableFrom v=\"4.0.137\" />\n\nEnsures a browser is locally installed so a Remotion render can be executed.\n\n```tsx twoslash title=\"Simple usage\"\nimport {ensureBrowser} from '@remotion/renderer';\n\nawait ensureBrowser();\n```\n\n```tsx twoslash title=\"Setting a specific Chrome version and listening to progress\"\nimport {ensureBrowser} from '@remotion/renderer';\n\nawait ensureBrowser({\n  onBrowserDownload: () => {\n    console.log('Downloading browser');\n\n    return {\n      version: '144.0.7559.20',\n      onProgress: ({percent}) => {\n        console.log(`${Math.round(percent * 100)}% downloaded`);\n      },\n    };\n  },\n});\n```\n\n## API\n\nAn object with the following properties, all of which are optional:\n\n### `chromeMode?`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n### `browserExecutable?`\n\nPass a path to a browser executable that you want to use instead of downloading.  \nIf the path does not exist, this function will throw.  \nPass the same path to any other API that supports the `browserExecutable` option.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\n### `onBrowserDownload`\n\nSpecify a specific version of Chrome that should be used and hook into the download progress.  \nSee the example below for the function signature.\n\n```tsx twoslash title=\"init.ts\"\nimport {ensureBrowser, OnBrowserDownload, DownloadBrowserProgressFn} from '@remotion/renderer';\n\nconst onProgress: DownloadBrowserProgressFn = ({percent, downloadedBytes, totalSizeInBytes}) => {\n  console.log(`${Math.round(percent * 100)}% downloaded`);\n};\n\nconst onBrowserDownload: OnBrowserDownload = () => {\n  console.log('Downloading browser');\n\n  return {\n    // Pass `null` to use Remotion's recommendation.\n    version: '144.0.7559.20',\n    onProgress,\n  };\n};\n\nawait ensureBrowser({\n  onBrowserDownload,\n});\n```\n\n## Return value\n\nA promise with no value.\n\n## Compatibility\n\n<CompatibilityTable chrome={false} firefox={false} safari={false} nodejs={true} bun={true} serverlessFunctions={false} clientSideRendering={false} serverSideRendering={true} player={false} studio={false} />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/ensure-browser.ts)\n- [Chrome Headless Shell](/docs/miscellaneous/chrome-headless-shell)\n- [Server-Side rendering](/docs/ssr)\n"

Ensures a browser is locally installed so a Remotion render can be executed.

```

Simple usageimport {ensureBrowser} from '@remotion/renderer';

await ensureBrowser();Copy
```

```

Setting a specific Chrome version and listening to progressimport {ensureBrowser} from '@remotion/renderer';

await ensureBrowser({
  onBrowserDownload: () => {
    console.log('Downloading browser');

    return {
      version: '144.0.7559.20',
      onProgress: ({percent}) => {
        console.log(`${Math.round(percent * 100)}% downloaded`);
      },
    };
  },
});Copy
```

## API[​](#api)

An object with the following properties, all of which are optional:

### `chromeMode?`[v4.0.248](https://github.com/remotion-dev/remotion/releases/v4.0.248)[​](#chromemode)

One of `headless-shell, ``chrome-for-testing`. Default `headless-shell`. [Use `chrome-for-testing` to take advantage of GPU drivers on Linux.](https://remotion.dev/docs/miscellaneous/chrome-headless-shell)

### `browserExecutable?`[​](#browserexecutable)

Pass a path to a browser executable that you want to use instead of downloading.

If the path does not exist, this function will throw.

Pass the same path to any other API that supports the `browserExecutable` option.

### `logLevel?`[​](#loglevel)

One of `trace`, `verbose`, `info`, `warn`, `error`.
 Determines how much info is being logged to the console.

 Default `info`.

### `onBrowserDownload`[​](#onbrowserdownload)

Specify a specific version of Chrome that should be used and hook into the download progress.

See the example below for the function signature.

```

init.tsimport {ensureBrowser, OnBrowserDownload, DownloadBrowserProgressFn} from '@remotion/renderer';

const onProgress: DownloadBrowserProgressFn = ({percent, downloadedBytes, totalSizeInBytes}) => {
  console.log(`${Math.round(percent * 100)}% downloaded`);
};

const onBrowserDownload: OnBrowserDownload = () => {
  console.log('Downloading browser');

  return {
    // Pass `null` to use Remotion's recommendation.
    version: '144.0.7559.20',
    onProgress,
  };
};

await ensureBrowser({
  onBrowserDownload,
});Copy
```

## Return value[​](#return-value)

A promise with no value.

## Compatibility[​](#compatibility)

|  Browsers Servers Environments
|  
Chrome 
Firefox 
Safari 
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
 
 
 
 

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/ensure-browser.ts)

- [Chrome Headless Shell](/docs/miscellaneous/chrome-headless-shell)

- [Server-Side rendering](/docs/ssr)
](/docs/ssr)](/docs/ssr)
](/docs/ssr)
- ](/docs/ssr)
- ](/docs/ssr)
- ](/docs/ssr)
- ](/docs/ssr)
- ](/docs/ssr)
- ](/docs/ssr)
- ](/docs/ssr)