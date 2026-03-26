---
title: "getFunctions()"
url: "https://www.remotion.dev/docs/lambda/getfunctions"
path: "/docs/lambda/getfunctions"
---

"---\nimage: /generated/articles-docs-lambda-getfunctions.png\ntitle: getFunctions()\nid: getfunctions\nslug: /lambda/getfunctions\ncrumb: 'Lambda API'\n---\n\nRetrieves a list of functions that Remotion deployed to AWS Lambda in a certain region.\n\nThe parameter `compatibleOnly` determines whether only functions that are compatible with the installed version of Remotion Lambda should be returned.\n\n:::note\nThe Lambda function is versioned and the version of the function must match the version of the `@remotion/lambda` package. So if you upgrade Remotion, you should deploy a new function or otherwise you might get an empty array from this function.\n:::\n\nTo get information about only a single function, use [`getFunctionInfo()`](/docs/lambda/getfunctioninfo).\n\nIf you are sure that a function exists, you can also guess the name of it using [`speculateFunctionName()`](/docs/lambda/speculatefunctionname) and save an API call to Lambda.\n\n## Example\n\n```ts twoslash\nimport {getFunctions} from '@remotion/lambda/client';\n\nconst info = await getFunctions({\n  region: 'eu-central-1',\n  compatibleOnly: true,\n});\n\nfor (const fn of info) {\n  console.log(fn.functionName); // \"remotion-render-d8a03x\"\n  console.log(fn.memorySizeInMb); // 1536\n  console.log(fn.timeoutInSeconds); // 120\n  console.log(fn.diskSizeInMb); // 2048\n  console.log(fn.version); // \"2021-07-25\"\n}\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n## Argument\n\nAn object containing the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) that you would like to query.\n\n### `logLevel?`<AvailableFrom v=\"4.0.115\"/>\n\n<Options id=\"log\" />\n\n### `compatibleOnly`\n\nIf `true`, only functions that match the version of the current Remotion Lambda package are returned. If `false`, all functions are returned.\n\n## Return value\n\nA promise resolving to an **array of objects** with the following properties:\n\n### `functionName`\n\nThe name of the function.\n\n### `memorySizeInMb`\n\nThe amount of memory allocated to the function.\n\n### `diskSizeInMb`\n\nThe amount of ephemereal disk storage allocated to the function.\n\n### `version`\n\nThe version of the function. Remotion is versioning the Lambda function and a render can only be triggered from a version of `@remotion/lambda` that is matching the one of the function.\n\n### `timeoutInSeconds`\n\nThe timeout that has been assigned to the Lambda function.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-functions.ts)\n- [`getFunctionInfo()`](/docs/lambda/getfunctioninfo)\n- [`deployFunction()`](/docs/lambda/deployfunction)\n- [`deleteFunction()`](/docs/lambda/deletefunction)\n"

Retrieves a list of functions that Remotion deployed to AWS Lambda in a certain region.

The parameter `compatibleOnly` determines whether only functions that are compatible with the installed version of Remotion Lambda should be returned.
]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()