---
title: "getCompositionsOnLambda()"
url: "https://www.remotion.dev/docs/lambda/getcompositionsonlambda"
path: "/docs/lambda/getcompositionsonlambda"
---

"---\nimage: /generated/articles-docs-lambda-getcompositionsonlambda.png\nid: getcompositionsonlambda\ntitle: getCompositionsOnLambda()\nslug: /lambda/getcompositionsonlambda\ncrumb: 'Lambda API'\n---\n\n<AvailableFrom v=\"3.3.2\" />\n\nGets the compositions inside a Lambda function.\n\nNote that you can also get the compositions of a site that is hosted on Lambda using [`getCompositions()`](/docs/renderer/get-compositions). Vice versa, you can also get the compositions from a serve URL that is not hosted on AWS Lambda using `getCompositionsOnLambda()`.\n\nYou should use `getCompositionsOnLambda()` if you cannot use [`getCompositions()`](/docs/renderer/get-compositions) because the machine cannot run Chrome.\n\n## Example\n\n```tsx twoslash\nimport {getCompositionsOnLambda} from '@remotion/lambda/client';\n\nconst compositions = await getCompositionsOnLambda({\n  region: 'us-east-1',\n  functionName: 'remotion-render-bds9aab',\n  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',\n  inputProps: {},\n});\n\nconsole.log(compositions); // See below for an example value\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `functionName`\n\nThe name of the deployed Lambda function that should be used to ge the list of compositions.\nUse [`deployFunction()`](/docs/lambda/deployfunction) to create a new function and [`getFunctions()`](/docs/lambda/getfunctions) to obtain currently deployed Lambdas.\n\n### `region`\n\nIn which region your Lambda function is deployed.\n\n### `serveUrl`\n\nA URL pointing to a Remotion project. Use [`deploySite()`](/docs/lambda/deploysite) to deploy a Remotion project.\n\n### `inputProps`\n\n[Input Props to pass to the selected composition of your video.](/docs/passing-props#passing-input-props-in-the-cli).  \nMust be a JSON object.  \nFrom the root component the props can be read using [`getInputProps()`](/docs/get-input-props).  \nYou may transform input props using [`calculateMetadata()`](/docs/calculate-metadata).\n\n### `envVariables?`\n\nSee [`renderMedia() -> envVariables`](/docs/renderer/render-media#envvariables). Default: `{}`.\n\n### `timeoutInMilliseconds?`\n\nA number describing how long the function may take in milliseconds to evaluate the list of compositions [before it times out](/docs/timeout). Default: `30000`\n\n### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n#### `disableWebSecurity`\n\n_boolean - default `false`_\n\nThis will most notably disable CORS among other security features.\n\n#### `ignoreCertificateErrors`\n\n_boolean - default `false`_\n\nResults in invalid SSL certificates, such as self-signed ones, being ignored.\n\n#### `gl`\n\n<Options id=\"gl\" />\n\n#### `userAgent`<AvailableFrom v=\"3.3.83\"/>\n\nLets you set a custom user agent that the headless Chrome browser assumes.\n\n#### `darkMode?`<AvailableFrom v=\"4.0.381\"/>\n\n<Options id=\"dark-mode\" />\n\n### `forceBucketName?`<AvailableFrom v=\"3.3.42\" />\n\nSpecify a specific bucket name to be used. [This is not recommended](/docs/lambda/multiple-buckets), instead let Remotion discover the right bucket automatically.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\nLogs can be read through the CloudWatch URL that this function returns.\n\n### `mediaCacheSizeInBytes?`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `offthreadVideoCacheSizeInBytes?`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `offthreadVideoThreads?`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### ~~`dumpBrowserLogs?`~~\n\nDeprecated in v4.0 in favor of [`logLevel`](#loglevel).\n\n## Return value\n\nReturns a promise that resolves to an array of available compositions. Example value:\n\n```ts twoslash\n[\n  {\n    id: 'HelloWorld',\n    width: 1920,\n    height: 1080,\n    fps: 30,\n    durationInFrames: 120,\n    defaultProps: {\n      title: 'Hello World',\n    },\n  },\n  {\n    id: 'Title',\n    width: 1080,\n    height: 1080,\n    fps: 30,\n    durationInFrames: 90,\n    defaultProps: undefined,\n  },\n];\n```\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-compositions-on-lambda.ts)\n- [getCompositions()](/docs/renderer/get-compositions)\n"
[v3.3.2](https://github.com/remotion-dev/remotion/releases/v3.3.2)

Gets the compositions inside a Lambda function.

Note that you can also get the compositions of a site that is hosted on Lambda using [`getCompositions()`](/docs/renderer/get-compositions). Vice versa, you can also get the compositions from a serve URL that is not hosted on AWS Lambda using `getCompositionsOnLambda()`.

You should use `getCompositionsOnLambda()` if you cannot use [`getCompositions()`](/docs/renderer/get-compositions) because the machine cannot run Chrome.

## Example[​](#example)

```
import {getCompositionsOnLambda} from '@remotion/lambda/client';

const compositions = await getCompositionsOnLambda({
  region: 'us-east-1',
  functionName: 'remotion-render-bds9aab',
  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',
  inputProps: {},
});

console.log(compositions); // See below for an example valueCopy
```

](#example)](#example)
](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)