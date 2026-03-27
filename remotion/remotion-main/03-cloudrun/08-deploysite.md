---
title: "deploySite()"
url: "https://www.remotion.dev/docs/cloudrun/deploysite"
path: "/docs/cloudrun/deploysite"
---

"---\nimage: /generated/articles-docs-cloudrun-deploysite.png\nid: deploysite\ntitle: deploySite()\nslug: /cloudrun/deploysite\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nTakes a Remotion project, bundles it and uploads it to an Cloud Storage bucket. Once uploaded, a Cloud Run service can render any composition in the Remotion project by specifying the URL.\n\n- If you make changes locally, you need to redeploy the site. You can use [`siteName`](#sitename) to overwrite the previous site.\n- Note that the Remotion project will be deployed to a subdirectory, not the root of the domain. Therefore you must ensure that if you have specified paths in your Remotion project, they are able to handle this scenario.\n- Before calling this function, you should create a bucket, see [`getOrCreateBucket()`](/docs/cloudrun/getorcreatebucket).\n\n## Example\n\n```ts twoslash\nimport {deploySite} from '@remotion/cloudrun';\nimport path from 'path';\n\nconst {serveUrl} = await deploySite({\n  entryPoint: path.resolve(process.cwd(), 'src/index.ts'),\n  bucketName: 'remotioncloudrun-c7fsl3d',\n  options: {\n    onBundleProgress: (progress) => {\n      // Progress is between 0 and 100\n      console.log(`Bundle progress: ${progress}%`);\n    },\n    onUploadProgress: ({totalFiles, filesUploaded, totalSize, sizeUploaded}) => {\n      console.log(`Upload progress: Total files ${totalFiles}, Files uploaded ${filesUploaded}, Total size ${totalSize}, Size uploaded ${sizeUploaded}`);\n    },\n  },\n});\nconsole.log(serveUrl);\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `entryPoint`\n\nAn absolute path pointing to the entry point of your Remotion project. [Usually the entry point in your Remotion project is stored at `src/entry.tsx`](/docs/terminology/entry-point).\n\n### `bucketName`\n\nThe bucket to where the website will be deployed. The bucket must have been created by Remotion Cloud Run.\n\n### `siteName?`\n\nSpecify the subfolder in your Cloud Storage bucket that you want the site to deploy to. If you omit this property, a new subfolder with a random name will be created. If a site already exists with the name you passed, it will be overwritten. Can only contain the following characters: `0-9`, `a-z`, `A-Z`, `-`, `!`, `_`, `.`, `*`, `'`, `(`, `)`\n\n### `logLevel?`<AvailableFrom v=\"4.0.140\"/>\n\n<Options id=\"log\" />\n\n### `options?`\n\nAn object with the following properties:\n\n#### `onBundleProgress?`\n\nCallback from Webpack when the bundling has progressed. Passes a number between 0 and 100 to the callback, see example at the top of the page.\n\n#### `onUploadProgress?`\n\nCallback function that gets called when uploading of the assets has progressed. Passes an object with the following properties to the callback:\n\n- `totalFiles` (_number_): Total number of files in the bundle.\n- `filesUploaded` (_number_): Number of files that have been fully uploaded so far.\n- `totalSize` (_number_): Total size in bytes of all the files in the bundle.\n- `sizeUploaded` (_number_): Amount of bytes uploaded so far.\n\n#### `webpackOverride?`\n\nAllows to pass a custom webpack override. See [`bundle()` -> webpackOverride](/docs/bundle#webpackoverride) for more information.\n\n#### `enableCaching?`\n\n<Options id=\"bundle-cache\" />\n\n#### `publicDir?`\n\n<Options id=\"public-dir\" />\n\n#### `rootDir?`\n\nThe directory in which the Remotion project is rooted in. This should be set to the directory that contains the `package.json` which installs Remotion. By default, it is the current working directory.\n\n:::note\nThe current working directory is the directory from which your program gets executed from. It is not the same as the file where bundle() gets called.\n:::\n\n#### `ignoreRegisterRootWarning?`\n\nIgnore an error that gets thrown if you pass an entry point file which does not contain `registerRoot`.\n\n#### `keyboardShortcutsEnabled?`<AvailableFrom v=\"4.0.407\"/>\n\n<Options id=\"disable-keyboard-shortcuts\" />\n\n#### `askAIEnabled?`<AvailableFrom v=\"4.0.407\"/>\n\n<Options id=\"disable-ask-ai\" />\n\n#### `experimentalClientSideRenderingEnabled?`<AvailableFrom v=\"4.0.407\"/>\n\n<Options id=\"enable-experimental-client-side-rendering\" />\n\n#### `rspack?`<AvailableFrom v=\"4.0.426\"/>\n\n<Options id=\"experimental-rspack\" />\n\n## Return value\n\nAn object with the following values:\n\n### `serveUrl`\n\n_string_\n\nAn URL such as `https://storage.googleapis.com/remotioncloudrun-123asd321/sites/abcdefgh/index.html`.\n\nYou can use this \"Serve URL\" to render a video on Remotion Cloud Run using:\n\n- The [`npx remotion cloudrun render`](/docs/cloudrun/cli/render) command\n- The [`renderMediaOnCloudrun()`](/docs/cloudrun/rendermediaoncloudrun) and [`renderStillOnCloudrun()`](/docs/cloudrun/renderstilloncloudrun) functions.\n- Locally using the [`renderMedia()`](/docs/renderer/render-media) and [`renderStill()`](/docs/renderer/render-still) functions.\n- Locally using the [`npx remotion render`](/docs/cli) and [`npx remotion still`](/docs/cli) commands\n\nIf you are rendering on Cloud Run, you can also pass the site name (in this case `abcdefgh`) as an abbreviation.\n\n### `siteName`\n\n_string_\n\nThe identifier of the site that was given. Is either the site name that you have passed into this function, or a random string that was generated if you didn't pass a site name.\n\n### `stats`\n\nAn object with 3 entries:\n\n- `uploadedFiles`\n- `deletedFiles`\n- `untouchedFiles`\n\nEach one is a `number`.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/deploy-site.ts)\n- [CLI equivalent: `npx remotion cloudrun sites create`](/docs/cloudrun/cli/sites/create)\n- [getSites()](/docs/cloudrun/getsites)\n- [deleteSite()](/docs/cloudrun/deletesite)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Takes a Remotion project, bundles it and uploads it to an Cloud Storage bucket. Once uploaded, a Cloud Run service can render any composition in the Remotion project by specifying the URL.

- If you make changes locally, you need to redeploy the site. You can use [`siteName`](#sitename) to overwrite the previous site.

- Note that the Remotion project will be deployed to a subdirectory, not the root of the domain. Therefore you must ensure that if you have specified paths in your Remotion project, they are able to handle this scenario.

- Before calling this function, you should create a bucket, see [`getOrCreateBucket()`](/docs/cloudrun/getorcreatebucket).

## Example[​](#example)

```
import {deploySite} from '@remotion/cloudrun';
import path from 'path';

const {serveUrl} = await deploySite({
  entryPoint: path.resolve(process.cwd(), 'src/index.ts'),
  bucketName: 'remotioncloudrun-c7fsl3d',
  options: {
    onBundleProgress: (progress) => {
      // Progress is between 0 and 100
      console.log(`Bundle progress: ${progress}%`);
    },
    onUploadProgress: ({totalFiles, filesUploaded, totalSize, sizeUploaded}) => {
      console.log(`Upload progress: Total files ${totalFiles}, Files uploaded ${filesUploaded}, Total size ${totalSize}, Size uploaded ${sizeUploaded}`);
    },
  },
});
console.log(serveUrl);Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `entryPoint`[​](#entrypoint)

An absolute path pointing to the entry point of your Remotion project. [Usually the entry point in your Remotion project is stored at `src/entry.tsx`](/docs/terminology/entry-point).

### `bucketName`[​](#bucketname)

The bucket to where the website will be deployed. The bucket must have been created by Remotion Cloud Run.

### `siteName?`[​](#sitename)

Specify the subfolder in your Cloud Storage bucket that you want the site to deploy to. If you omit this property, a new subfolder with a random name will be created. If a site already exists with the name you passed, it will be overwritten. Can only contain the following characters: `0-9`, `a-z`, `A-Z`, `-`, `!`, `_`, `.`, `*`, `'`, `(`, `)`

### `logLevel?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#loglevel)

One of `trace`, `verbose`, `info`, `warn`, `error`.
 Determines how much info is being logged to the console.

 Default `info`.

### `options?`[​](#options)

An object with the following properties:

#### `onBundleProgress?`[​](#onbundleprogress)

Callback from Webpack when the bundling has progressed. Passes a number between 0 and 100 to the callback, see example at the top of the page.

#### `onUploadProgress?`[​](#onuploadprogress)

Callback function that gets called when uploading of the assets has progressed. Passes an object with the following properties to the callback:

- `totalFiles` (*number*): Total number of files in the bundle.

- `filesUploaded` (*number*): Number of files that have been fully uploaded so far.

- `totalSize` (*number*): Total size in bytes of all the files in the bundle.

- `sizeUploaded` (*number*): Amount of bytes uploaded so far.

#### `webpackOverride?`[​](#webpackoverride)

Allows to pass a custom webpack override. See [`bundle()` -> webpackOverride](/docs/bundle#webpackoverride) for more information.

#### `enableCaching?`[​](#enablecaching)

Enable or disable Webpack caching. This flag is enabled by default, use `--bundle-cache=false` to disable caching.

#### `publicDir?`[​](#publicdir)

Define the location of the [`public/ directory`](/docs/terminology/public-dir). If not defined, Remotion will assume the location is the `public` folder in your Remotion root.

#### `rootDir?`[​](#rootdir)

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