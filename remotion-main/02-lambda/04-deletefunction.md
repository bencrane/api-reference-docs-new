---
title: "deleteFunction()"
url: "https://www.remotion.dev/docs/lambda/deletefunction"
path: "/docs/lambda/deletefunction"
---

"---\nimage: /generated/articles-docs-lambda-deletefunction.png\nid: deletefunction\ntitle: deleteFunction()\nslug: /lambda/deletefunction\ncrumb: 'Lambda API'\n---\n\nDeletes a deployed Lambda function based on its name.\n\nTo retrieve a list of functions, call [`getFunctions()`](/docs/lambda/getfunctions) first.\n\n## Example\n\n```ts twoslash\nimport {deleteFunction, getFunctions} from '@remotion/lambda';\n\nconst functions = await getFunctions({\n  region: 'us-east-1',\n  compatibleOnly: false,\n});\nfor (const fn of functions) {\n  await deleteFunction({\n    region: 'us-east-1',\n    functionName: fn.functionName,\n  });\n}\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) to which the function was deployed to.\n\n### `functionName`\n\nThe name of the function to be deleted.\n\n## Return value\n\nNothing. If the deletion failed, the function rejects with an error.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-function.ts)\n- [deployFunction()](/docs/lambda/deployfunction)\n- [getFunctions()](/docs/lambda/getfunctions)\n"

Deletes a deployed Lambda function based on its name.

To retrieve a list of functions, call [`getFunctions()`](/docs/lambda/getfunctions) first.

## Example[​](#example)

```
import {deleteFunction, getFunctions} from '@remotion/lambda';

const functions = await getFunctions({
  region: 'us-east-1',
  compatibleOnly: false,
});
for (const fn of functions) {
  await deleteFunction({
    region: 'us-east-1',
    functionName: fn.functionName,
  });
}Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) to which the function was deployed to.

### `functionName`[​](#functionname)

The name of the function to be deleted.

## Return value[​](#return-value)

Nothing. If the deletion failed, the function rejects with an error.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-function.ts)

- [deployFunction()](/docs/lambda/deployfunction)

- [getFunctions()](/docs/lambda/getfunctions)
](/docs/lambda/getfunctions)](/docs/lambda/getfunctions)
](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)