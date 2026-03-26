---
title: "speculateFunctionName()"
url: "https://www.remotion.dev/docs/lambda/speculatefunctionname"
path: "/docs/lambda/speculatefunctionname"
---

"---\nimage: /generated/articles-docs-lambda-speculateFunctionName.png\nid: speculatefunctionname\ntitle: speculateFunctionName()\nslug: /lambda/speculatefunctionname\ncrumb: 'Lambda API'\n---\n\n_available from v3.3.75_\n\nSpeculate the name of the Lambda function that will be created by [`deployFunction()`](/docs/lambda/deployfunction) or its CLI equivalent, [`npx remotion lambda functions deploy`](/docs/lambda/cli/functions/deploy). This could be useful in cases when the configuration of the Lambda function is known in advance, and the name of the function is needed.\n\nIf you are not sure whether a function exists, use [`getFunctionInfo()`](/docs/lambda/getfunctioninfo) and catch the error that gets thrown if it does not exist.\n\nIf you want to get a list of deployed functions, use [`getFunctions()`](/docs/lambda/getfunctions) instead.\n\n## Function name pattern\n\nA Remotion Lambda function is always names like this:\n\n```txt\nremotion-render-3-3-63-mem2048mb-disk2048mb-240sec\n                ^^^^^^    ^^^^       ^^^    ^^^\n                  |         |         |      |-- Timeout in seconds\n                  |         |         |--------- Disk size in MB\n                  |         |------------------- Memory size in MB\n                  |----------------------------- Remotion version with dots replaced by dashes\n```\n\n[Learn more](/docs/lambda/naming-convention) about this convention.\n\n## Example\n\n```ts twoslash\nimport {speculateFunctionName} from '@remotion/lambda/client';\n\nconst speculatedFunctionName = speculateFunctionName({\n  memorySizeInMb: 2048,\n  diskSizeInMb: 2048,\n  timeoutInSeconds: 120,\n});\n\nconsole.log(speculatedFunctionName); // remotion-render-3-3-63-mem2048mb-disk2048mb-120sec\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `memorySizeInMb`\n\nThe amount of memory allocated to the function.\n\n### `diskSizeInMb`\n\nThe amount of disk space allocated to the function.\n\n### `timeoutInSeconds`\n\nThe timeout that has been assigned to the Lambda function.\n\n## Return value\n\nA string with the name of the function that will be created.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/speculate-function-name.ts)\n- [Function name convention](/docs/lambda/naming-convention)\n- [`deployFunction()`](/docs/lambda/deployfunction)\n- CLI version of `deployFunction()`: [`npx remotion lambda functions deploy`](/docs/lambda/cli/functions/deploy)\n"

*available from v3.3.75*

Speculate the name of the Lambda function that will be created by [`deployFunction()`](/docs/lambda/deployfunction) or its CLI equivalent, [`npx remotion lambda functions deploy`](/docs/lambda/cli/functions/deploy). This could be useful in cases when the configuration of the Lambda function is known in advance, and the name of the function is needed.

If you are not sure whether a function exists, use [`getFunctionInfo()`](/docs/lambda/getfunctioninfo) and catch the error that gets thrown if it does not exist.

If you want to get a list of deployed functions, use [`getFunctions()`](/docs/lambda/getfunctions) instead.

## Function name pattern[​](#function-name-pattern)

A Remotion Lambda function is always names like this:

```
remotion-render-3-3-63-mem2048mb-disk2048mb-240sec
                ^^^^^^    ^^^^       ^^^    ^^^
                  |         |         |      |-- Timeout in seconds
                  |         |         |--------- Disk size in MB
                  |         |------------------- Memory size in MB
                  |----------------------------- Remotion version with dots replaced by dashesCopy
```

[Learn more](/docs/lambda/naming-convention) about this convention.

## Example[​](#example)

```
import {speculateFunctionName} from '@remotion/lambda/client';

const speculatedFunctionName = speculateFunctionName({
  memorySizeInMb: 2048,
  diskSizeInMb: 2048,
  timeoutInSeconds: 120,
});

console.log(speculatedFunctionName); // remotion-render-3-3-63-mem2048mb-disk2048mb-120secCopy
```

## Arguments[​](#arguments)

An object with the following properties:

### `memorySizeInMb`[​](#memorysizeinmb)

The amount of memory allocated to the function.

### `diskSizeInMb`[​](#disksizeinmb)

The amount of disk space allocated to the function.

### `timeoutInSeconds`[​](#timeoutinseconds)

The timeout that has been assigned to the Lambda function.

## Return value[​](#return-value)

A string with the name of the function that will be created.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/speculate-function-name.ts)

- [Function name convention](/docs/lambda/naming-convention)

- [`deployFunction()`](/docs/lambda/deployfunction)

- CLI version of `deployFunction()`: [`npx remotion lambda functions deploy`](/docs/lambda/cli/functions/deploy)
](/docs/lambda/cli/functions/deploy)](/docs/lambda/cli/functions/deploy)
](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)
- ](/docs/lambda/cli/functions/deploy)