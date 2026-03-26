---
title: "getFunctionInfo()"
url: "https://www.remotion.dev/docs/lambda/getfunctioninfo"
path: "/docs/lambda/getfunctioninfo"
---

"---\nimage: /generated/articles-docs-lambda-getfunctioninfo.png\nid: getfunctioninfo\ntitle: getFunctionInfo()\nslug: /lambda/getfunctioninfo\ncrumb: 'Lambda API'\n---\n\nGets information about a function given its name and region.\n\nTo get a list of deployed functions, use [`getFunctions()`](/docs/lambda/getfunctions).\n\nTo deploy a function, use [`deployFunction()`](/docs/lambda/deployfunction).\n\n## Example\n\n```ts twoslash\nimport {getFunctionInfo} from '@remotion/lambda';\n\nconst info = await getFunctionInfo({\n  functionName: 'remotion-render-d7nd2a9f',\n  region: 'eu-central-1',\n});\nconsole.log(info.functionName); // remotion-render-d7nd2a9f\nconsole.log(info.memorySizeInMb); // 1500\nconsole.log(info.diskSizeInMb); // 2048\nconsole.log(info.version); // '2021-07-14'\nconsole.log(info.timeoutInSeconds); // 120\n```\n\n## Arguments\n\nAn object containing the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) the function resides in.\n\n### `functionName`\n\nThe name of the function.\n\n### `logLevel?`<AvailableFrom v=\"4.0.115\"/>\n\n<Options id=\"log\" />\n\n## Return value\n\nIf the function does not exist, an error is thrown by the AWS SDK.\nIf the function exists, promise resolving to an object with the following properties is returned:\n\n### `memorySizeInMb`\n\nThe amount of memory allocated to the function.\n\n### `diskSizeInMb`\n\nThe amount of disk space allocated to the function.\n\n### `functionName`\n\nThe name of the function.\n\n### `version`\n\nThe version of the function. Remotion is versioning the Lambda function and a render can only be triggered from a version of `@remotion/lambda` that is matching the one of the function.\n\n### `timeoutInSeconds`\n\nThe timeout that has been assigned to the Lambda function.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-function-info.ts)\n- [`getFunctions()`](/docs/lambda/getfunctions)\n- [`deployFunction()`](/docs/lambda/deployfunction)\n- [`deleteFunction()`](/docs/lambda/deletefunction)\n"

Gets information about a function given its name and region.

To get a list of deployed functions, use [`getFunctions()`](/docs/lambda/getfunctions).

To deploy a function, use [`deployFunction()`](/docs/lambda/deployfunction).

## Example[​](#example)

```
import {getFunctionInfo} from '@remotion/lambda';

const info = await getFunctionInfo({
  functionName: 'remotion-render-d7nd2a9f',
  region: 'eu-central-1',
});
console.log(info.functionName); // remotion-render-d7nd2a9f
console.log(info.memorySizeInMb); // 1500
console.log(info.diskSizeInMb); // 2048
console.log(info.version); // '2021-07-14'
console.log(info.timeoutInSeconds); // 120Copy
```

## Arguments[​](#arguments)

An object containing the following properties:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) the function resides in.

### `functionName`[​](#functionname)

The name of the function.

### `logLevel?`[v4.0.115](https://github.com/remotion-dev/remotion/releases/v4.0.115)[​](#loglevel)

One of `trace`, `verbose`, `info`, `warn`, `error`.
 Determines how much info is being logged to the console.

 Default `info`.

## Return value[​](#return-value)

If the function does not exist, an error is thrown by the AWS SDK.
If the function exists, promise resolving to an object with the following properties is returned:

### `memorySizeInMb`[​](#memorysizeinmb)

The amount of memory allocated to the function.

### `diskSizeInMb`[​](#disksizeinmb)

The amount of disk space allocated to the function.

### `functionName`[​](#functionname-1)

The name of the function.

### `version`[​](#version)

The version of the function. Remotion is versioning the Lambda function and a render can only be triggered from a version of `@remotion/lambda` that is matching the one of the function.

### `timeoutInSeconds`[​](#timeoutinseconds)

The timeout that has been assigned to the Lambda function.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-function-info.ts)

- [`getFunctions()`](/docs/lambda/getfunctions)

- [`deployFunction()`](/docs/lambda/deployfunction)

- [`deleteFunction()`](/docs/lambda/deletefunction)
](/docs/lambda/deletefunction)](/docs/lambda/deletefunction)
](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)
- ](/docs/lambda/deletefunction)