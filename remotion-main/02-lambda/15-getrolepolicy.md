---
title: "getRolePolicy()"
url: "https://www.remotion.dev/docs/lambda/getrolepolicy"
path: "/docs/lambda/getrolepolicy"
---

"---\nimage: /generated/articles-docs-lambda-getrolepolicy.png\nid: getrolepolicy\ntitle: getRolePolicy()\nslug: /lambda/getrolepolicy\ncrumb: 'Lambda API'\n---\n\nReturns an inline JSON policy to be assigned to the 'remotion-lambda-role' role that needs to be created in your AWS account.\n\nThese permissions will be given to the Lambda function itself.\n\nSee [Setup tutorial](/docs/lambda/setup) for setting up Lambda from scratch or [Role permissions](/docs/lambda/permissions#role-permissions) to see a copy of the current policy file with explanations.\n\n## Example\n\n```ts twoslash\nimport {getRolePolicy} from '@remotion/lambda';\n\nconsole.log(getRolePolicy()); /* `\n{\n  \"Version\": \"2012-10-17\",\n  \"Statements\": [\n    // ...\n  ]\n}\n` */\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/iam-validation/suggested-policy.ts)\n- [getUserPolicy()](/docs/lambda/getuserpolicy)\n- [Permissions](/docs/lambda/permissions)\n"

Returns an inline JSON policy to be assigned to the 'remotion-lambda-role' role that needs to be created in your AWS account.

These permissions will be given to the Lambda function itself.

See [Setup tutorial](/docs/lambda/setup) for setting up Lambda from scratch or [Role permissions](/docs/lambda/permissions#role-permissions) to see a copy of the current policy file with explanations.

## Example[​](#example)

```
import {getRolePolicy} from '@remotion/lambda';

console.log(getRolePolicy()); /* `
{
  "Version": "2012-10-17",
  "Statements": [
    // ...
  ]
}
` */Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/iam-validation/suggested-policy.ts)

- [getUserPolicy()](/docs/lambda/getuserpolicy)

- [Permissions](/docs/lambda/permissions)
](/docs/lambda/permissions)](/docs/lambda/permissions)
](/docs/lambda/permissions)
- ](/docs/lambda/permissions)