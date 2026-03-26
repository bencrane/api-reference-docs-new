---
title: "testPermissions()"
url: "https://www.remotion.dev/docs/cloudrun/testpermissions"
path: "/docs/cloudrun/testpermissions"
---

"---\nimage: /generated/articles-docs-cloudrun-testpermissions.png\nid: testpermissions\ntitle: testPermissions()\nslug: /cloudrun/testpermissions\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nMakes a call to the [Test Iam Permissions](https://cloud.google.com/resource-manager/reference/rest/v3/projects/testIamPermissions) method of the Resource Manager API in GCP, which returns the list of permissions the Service Account has on the GCP Project. This is then validated against the list of permissions required for the version of Remotion.\n\nThe CLI equivalent is `npx remotion cloudrun permissions`.\n\nThe function does not reject with an error if a permission is missing, rather the missing permission is indicated in the return value.\n\n## Example\n\n```ts twoslash\nimport {testPermissions} from '@remotion/cloudrun';\n\nconst {results} = await testPermissions();\n\nfor (const result of results) {\n  console.log(result.decision); // \"allowed\"\n  console.log(result.permissionName); // \"iam.serviceAccounts.actAs\"\n}\n```\n\n## Arguments\n\nAn object with the following property:\n\n### `onTest?`\n\nA callback function that gets called every time a new test has been executed. This allows you to react to new test results coming in much faster than waiting for the return value of the function. Example:\n\n```ts twoslash\nimport {testPermissions} from '@remotion/cloudrun';\n\nconst {results} = await testPermissions({\n  onTest: (result) => {\n    console.log(result.decision); // \"allowed\"\n    console.log(result.permissionName); // \"iam.serviceAccounts.actAs\"\n  },\n});\n```\n\n## Return value\n\n**An array of objects** containing simulation results of each necessary permission. The objects contain the following keys:\n\n### `decision`\n\nEither `true` or `false`.\n\n### `permissionName`\n\nThe identifier of the required permission. See the [Permissions page](/docs/cloudrun/permissions) to see a list of required permissions.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/iam-validation/testPermissions.ts)\n- [Permissions](/docs/cloudrun/permissions)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Makes a call to the [Test Iam Permissions](https://cloud.google.com/resource-manager/reference/rest/v3/projects/testIamPermissions) method of the Resource Manager API in GCP, which returns the list of permissions the Service Account has on the GCP Project. This is then validated against the list of permissions required for the version of Remotion.

The CLI equivalent is `npx remotion cloudrun permissions`.

The function does not reject with an error if a permission is missing, rather the missing permission is indicated in the return value.

## Example[​](#example)

```
import {testPermissions} from '@remotion/cloudrun';

const {results} = await testPermissions();

for (const result of results) {
  console.log(result.decision); // "allowed"
  console.log(result.permissionName); // "iam.serviceAccounts.actAs"
}Copy
```

## Arguments[​](#arguments)

An object with the following property:

### `onTest?`[​](#ontest)

A callback function that gets called every time a new test has been executed. This allows you to react to new test results coming in much faster than waiting for the return value of the function. Example:

```
import {testPermissions} from '@remotion/cloudrun';

const {results} = await testPermissions({
  onTest: (result) => {
    console.log(result.decision); // "allowed"
    console.log(result.permissionName); // "iam.serviceAccounts.actAs"
  },
});Copy
```

## Return value[​](#return-value)

**An array of objects** containing simulation results of each necessary permission. The objects contain the following keys:

### `decision`[​](#decision)

Either `true` or `false`.

### `permissionName`[​](#permissionname)

The identifier of the required permission. See the [Permissions page](/docs/cloudrun/permissions) to see a list of required permissions.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/iam-validation/testPermissions.ts)

- [Permissions](/docs/cloudrun/permissions)
](/docs/cloudrun/permissions)](/docs/cloudrun/permissions)
](/docs/cloudrun/permissions)
- ](/docs/cloudrun/permissions)
- ](/docs/cloudrun/permissions)
- ](/docs/cloudrun/permissions)
- ](/docs/cloudrun/permissions)
- ](/docs/cloudrun/permissions)
- ](/docs/cloudrun/permissions)