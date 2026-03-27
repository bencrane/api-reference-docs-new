---
title: "simulatePermissions()"
url: "https://www.remotion.dev/docs/lambda/simulatepermissions"
path: "/docs/lambda/simulatepermissions"
---

"---\nimage: /generated/articles-docs-lambda-simulatepermissions.png\nid: simulatepermissions\ntitle: simulatePermissions()\nslug: /lambda/simulatepermissions\ncrumb: 'Lambda API'\n---\n\nRuns tests through the AWS Simulator ensuring that all the necessary permissions are set for the authenticated user.\n\nThe CLI equivalent is `npx remotion lambda policies validate`.\n\nThe function does not reject with an error if a permission is missing, rather the missing permission is indicated in the return value.\n\nThis function does only validate the validity of the **user policy**, not the **role policy**.\n\n## Example\n\n```ts twoslash\nimport {simulatePermissions} from '@remotion/lambda';\n\nconst {results} = await simulatePermissions({\n  region: 'us-east-1',\n});\n\nfor (const result of results) {\n  console.log(result.decision); // \"allowed\"\n  console.log(result.name); // \"iam:SimulatePrincipalPolicy\"\n}\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) that you would like to query.\n\n### `onSimulation?`\n\nA callback function that gets called every time a new simulation has been executed. This allows you to react to new simulation results coming in much faster than waiting for the return value of the function. Example:\n\n```ts twoslash\nimport {simulatePermissions} from '@remotion/lambda';\n\nconst {results} = await simulatePermissions({\n  region: 'us-east-1',\n  onSimulation: (result) => {\n    console.log(result.decision); // \"allowed\"\n    console.log(result.name); // \"iam:SimulatePrincipalPolicy\"\n  },\n});\n```\n\n## Return value\n\n**An array of objects** containing simulation results of each necessary permission. The objects contain the following keys:\n\n### `decision`\n\nEither `\"allowed\"`, `\"implicitDeny\"` or `\"explicitDeny\"`.\n\n### `name`\n\nThe identifier of the required permission. See the [Permissions page](/docs/lambda/permissions) to see a list of required permissions.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/iam-validation/simulate.ts)\n- [getUserPolicy()](/docs/lambda/getuserpolicy)\n- [getRolePolicy()](/docs/lambda/getrolepolicy)\n- [Permissions](/docs/lambda/permissions)\n"

Runs tests through the AWS Simulator ensuring that all the necessary permissions are set for the authenticated user.

The CLI equivalent is `npx remotion lambda policies validate`.

The function does not reject with an error if a permission is missing, rather the missing permission is indicated in the return value.

This function does only validate the validity of the **user policy**, not the **role policy**.

## Example[​](#example)

```
import {simulatePermissions} from '@remotion/lambda';

const {results} = await simulatePermissions({
  region: 'us-east-1',
});

for (const result of results) {
  console.log(result.decision); // "allowed"
  console.log(result.name); // "iam:SimulatePrincipalPolicy"
}Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) that you would like to query.

### `onSimulation?`[​](#onsimulation)

A callback function that gets called every time a new simulation has been executed. This allows you to react to new simulation results coming in much faster than waiting for the return value of the function. Example:

```
import {simulatePermissions} from '@remotion/lambda';

const {results} = await simulatePermissions({
  region: 'us-east-1',
  onSimulation: (result) => {
    console.log(result.decision); // "allowed"
    console.log(result.name); // "iam:SimulatePrincipalPolicy"
  },
});Copy
```

## Return value[​](#return-value)

**An array of objects** containing simulation results of each necessary permission. The objects contain the following keys:

### `decision`[​](#decision)

Either `"allowed"`, `"implicitDeny"` or `"explicitDeny"`.

### `name`[​](#name)

The identifier of the required permission. See the [Permissions page](/docs/lambda/permissions) to see a list of required permissions.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/iam-validation/simulate.ts)

- [getUserPolicy()](/docs/lambda/getuserpolicy)

- [getRolePolicy()](/docs/lambda/getrolepolicy)

- [Permissions](/docs/lambda/permissions)
](/docs/lambda/permissions)](/docs/lambda/permissions)
](/docs/lambda/permissions)
- ](/docs/lambda/permissions)
- ](/docs/lambda/permissions)
- ](/docs/lambda/permissions)
- ](/docs/lambda/permissions)
- ](/docs/lambda/permissions)
- ](/docs/lambda/permissions)
- ](/docs/lambda/permissions)