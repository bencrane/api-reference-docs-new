---
title: "getUserPolicy()"
url: "https://www.remotion.dev/docs/lambda/getuserpolicy"
path: "/docs/lambda/getuserpolicy"
---

"---\nimage: /generated/articles-docs-lambda-getuserpolicy.png\nid: getuserpolicy\ntitle: getUserPolicy()\nslug: /lambda/getuserpolicy\ncrumb: 'Lambda API'\n---\n\nReturns an inline JSON policy to be assigned to the AWS user whose credentials are being used for excuting CLI commands or calling Node.JS functions.\n\nSee [Setup tutorial](/docs/lambda/setup) for setting up Lambda from scratch or [User permissions](/docs/lambda/permissions#user-permissions) to see a copy of the current policy file with explanations.\n\n## Example\n\n```ts twoslash\nimport {getUserPolicy} from '@remotion/lambda';\n\nconsole.log(getUserPolicy()); /* `\n{\n  \"Version\": \"2012-10-17\",\n  \"Statements\": [\n    // ...\n  ]\n}\n` */\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/iam-validation/suggested-policy.ts)\n- [getRolePolicy()](/docs/lambda/getrolepolicy)\n- [Permissions](/docs/lambda/permissions)\n"

Returns an inline JSON policy to be assigned to the AWS user whose credentials are being used for excuting CLI commands or calling Node.JS functions.

See [Setup tutorial](/docs/lambda/setup) for setting up Lambda from scratch or [User permissions](/docs/lambda/permissions#user-permissions) to see a copy of the current policy file with explanations.

## Example[​](#example)

```
import {getUserPolicy} from '@remotion/lambda';

console.log(getUserPolicy()); /* `
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

- [getRolePolicy()](/docs/lambda/getrolepolicy)

- [Permissions](/docs/lambda/permissions)
](/docs/lambda/permissions)](/docs/lambda/permissions)
](/docs/lambda/permissions)
- ](/docs/lambda/permissions)