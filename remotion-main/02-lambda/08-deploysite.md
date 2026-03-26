---
title: "deploySite()"
url: "https://www.remotion.dev/docs/lambda/deploysite"
path: "/docs/lambda/deploysite"
---

"---\nimage: /generated/articles-docs-lambda-deploysite.png\nid: deploysite\ntitle: deploySite()\nslug: /lambda/deploysite\ncrumb: 'Lambda API'\n---\n\nTakes a Remotion project, bundles it and uploads it to an S3 bucket. Once uploaded, a Lambda function can render any composition in the Remotion project by specifying the URL.\n\n- If you make changes locally, you need to redeploy the site. You can use [`siteName`](#sitename) to overwrite the previous site.\n- Note that the Remotion project will be deployed to a subdirectory, not the root of the domain. Therefore you must ensure that if you have specified paths in your Remotion project, they are able to handle this scenario.\n- Before calling this function, you should create a bucket, see [`getOrCreateBucket()`](/docs/lambda/getorcreatebucket).\n\n## Example\n\n```ts twoslash\nimport {deploySite} from '@remotion/lambda';\nimport path from 'path';\n\nconst {serveUrl} = await deploySite({\n  entryPoint: path.resolve(process.cwd(), 'src/index.ts'),\n  bucketName: 'remotionlambda-c7fsl3d',\n  region: 'us-east-1',\n  options: {\n    onBundleProgress: (progress) => {\n      // Progress is between 0 and 100\n      console.log(`Bundle progress: ${progress}%`);\n    },\n    onUploadProgress: ({totalFiles, filesUploaded, totalSize, sizeUploaded}) => {\n      console.log(`Upload progress: Total files ${totalFiles}, Files uploaded ${filesUploaded}, Total size ${totalSize}, Size uploaded ${sizeUploaded}`);\n    },\n  },\n});\nconsole.log(serveUrl);\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `entryPoint`\n\nAn absolute path pointing to the entry point of your Remotion project. [Usually the entry point in your Remotion project is stored at `src/entry.tsx`](/docs/terminology/entry-point).\n\n### `bucketName`\n\nThe bucket to where the website will be deployed. The bucket must have been created by Remotion Lambda.\n\n### `region`\n\nThe AWS region in which the bucket resides.\n\n### `siteName?`\n\nSpecify the subfolder in your S3 bucket that you want the site to deploy to. If you omit this property, a new subfolder with a random name will be created. If a site already exists with the name you passed, it will be overwritten. Can only contain the following characters: `0-9`, `a-z`, `A-Z`, `-`, `!`, `_`, `.`, `*`, `'`, `(`, `)`\n\n### `logLevel?`<AvailableFrom v=\"4.0.140\"/>\n\n<Options id=\"log\" />\n\n### `options?`\n\nAn object with the following properties:\n\n#### `onBundleProgress?`\n\nCallback from Webpack when the bundling has progressed. Passes a number between 0 and 100 to the callback, see example at the top of the page.\n\n#### `onUploadProgress?`\n\nCallback function that gets called when uploading of the assets has progressed. Passes an object with the following properties to the callback:\n\n- `totalFiles` (_number_): Total number of files in the bundle.\n- `filesUploaded` (_number_): Number of files that have been fully uploaded so far.\n- `totalSize` (_number_): Total size in bytes of all the files in the bundle.\n- `sizeUploaded` (_number_): Amount of bytes uploaded so far.\n\n#### `webpackOverride?`\n\nAllows to pass a custom webpack override. See [`bundle()` -> webpackOverride](/docs/bundle#webpackoverride) for more information.\n\n#### `enableCaching?`\n\n<Options id=\"bundle-cache\" />\n\n#### `publicDir?`\n\n_available from v3.2.17_\n\n<Options id=\"public-dir\" />\n\n#### `rootDir?`\n\n_available from v3.2.17_\n\nThe directory in which the Remotion project is rooted in. This should be set to the directory that contains the `package.json` which installs Remotion. By default, it is the current working directory.\n\n:::note\nThe current working directory is the directory from which your program gets executed from. It is not the same as the file where bundle() gets called.\n:::\n\n#### `ignoreRegisterRootWarning?`\n\n_available from v3.3.55_\n\nIgnore an error that gets thrown if you pass an entry point file which does not contain `registerRoot`.\n\n#### `keyboardShortcutsEnabled?`<AvailableFrom v=\"4.0.407\"/>\n\n<Options id=\"disable-keyboard-shortcuts\" />\n\n#### `askAIEnabled?`<AvailableFrom v=\"4.0.407\"/>\n\n<Options id=\"disable-ask-ai\" />\n\n#### `experimentalClientSideRenderingEnabled?`<AvailableFrom v=\"4.0.407\"/>\n\n<Options id=\"enable-experimental-client-side-rendering\" />\n\n#### `rspack?`<AvailableFrom v=\"4.0.426\"/>\n\n<Options id=\"experimental-rspack\" />\n\n### `privacy?`\n\n_available from v3.3.97_\n\nEither `public` (default) or `no-acl` if you are not using ACL. Sites must have a public URL to be able to be rendered on Lambda, since the headless browser opens that URL.\n\n### `throwIfSiteExists?`<AvailableFrom v=\"4.0.141\"/>\n\n<Options id=\"throw-if-site-exists\" />\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n## Return value\n\nAn object with the following values:\n\n- `serveUrl` _(string)_: An URL such as `https://remotionlambda-12345.s3.eu-central-1.amazonaws.com/sites/abcdef/index.html`.\n\n  You can use this \"Serve URL\" to render a video on Remotion Lambda using:\n  - The [`npx remotion lambda render`](/docs/lambda/cli/render) and [`npx remotion lambda still`](/docs/lambda/cli/still) commands\n  - The [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) and [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda) functions.\n  - Locally using the [`renderMedia()`](/docs/renderer/render-media) and [`renderStill()`](/docs/renderer/render-still) functions.\n  - Locally using the [`npx remotion render`](/docs/cli) and [`npx remotion still`](/docs/cli) commands\n\n  If you are rendering on Lambda, you can also pass the site name (in this case `abcdef`) as an abbreviation.\n\n- `siteName` _(string)_: The identifier of the site that was given. Is either the site name that you have passed into this function, or a random string that was generated if you didn't pass a site name.\n\n- `stats`: (_available from v3.3.7_) An object with 3 entries: `uploadedFiles`, `deletedFiles` and `untouchedFiles`. Each one is a `number`.\n\n## Changelog\n\nFrom `v3.3.7`, this function is incremental: It only compares the contents of the local files and the files on S3 and only executes the necessary operations.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/deploy-site.ts)\n- [CLI equivalent: `npx remotion lambda sites create`](/docs/lambda/cli/sites/create)\n- [getSites()](/docs/lambda/getsites)\n- [deleteSite()](/docs/lambda/deletesite)\n"

Takes a Remotion project, bundles it and uploads it to an S3 bucket. Once uploaded, a Lambda function can render any composition in the Remotion project by specifying the URL.

- If you make changes locally, you need to redeploy the site. You can use [`siteName`](#sitename) to overwrite the previous site.

- Note that the Remotion project will be deployed to a subdirectory, not the root of the domain. Therefore you must ensure that if you have specified paths in your Remotion project, they are able to handle this scenario.

- Before calling this function, you should create a bucket, see [`getOrCreateBucket()`](/docs/lambda/getorcreatebucket).

## Example[​](#example)

```
import {deploySite} from '@remotion/lambda';
import path from 'path';

const {serveUrl} = await deploySite({
  entryPoint: path.resolve(process.cwd(), 'src/index.ts'),
  bucketName: 'remotionlambda-c7fsl3d',
  region: 'us-east-1',
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

The bucket to where the website will be deployed. The bucket must have been created by Remotion Lambda.

### `region`[​](#region)

The AWS region in which the bucket resides.

### `siteName?`[​](#sitename)

Specify the subfolder in your S3 bucket that you want the site to deploy to. If you omit this property, a new subfolder with a random name will be created. If a site already exists with the name you passed, it will be overwritten. Can only contain the following characters: `0-9`, `a-z`, `A-Z`, `-`, `!`, `_`, `.`, `*`, `'`, `(`, `)`

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

*available from v3.2.17*
Define the location of the [`public/ directory`](/docs/terminology/public-dir). If not defined, Remotion will assume the location is the `public` folder in your Remotion root.

#### `rootDir?`[​](#rootdir)

*available from v3.2.17*

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