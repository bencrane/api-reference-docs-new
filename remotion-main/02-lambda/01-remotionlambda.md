---
title: "@remotion/lambda"
url: "https://www.remotion.dev/docs/lambda/api"
path: "/docs/lambda/api"
---

"---\nimage: /generated/articles-docs-lambda-api.png\ntitle: \"@remotion/lambda\"\ncrumb: \"Render videos without servers on AWS\"\n---\n\nimport {TableOfContents} from './table-of-contents';\n\n<Installation pkg=\"@remotion/lambda\"/>\n<br/>\n\n**See the [setup guide](/docs/lambda/setup) for complete instructions on how to get started.**\n\n## APIs\n\nThe following Node.JS are available:\n\n<TableOfContents />\n\n## CLI\n\nSee [here](/docs/lambda/cli) for a list of CLI commands.\n"

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/lambdaCopy
```

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

**See the [setup guide](/docs/lambda/setup) for complete instructions on how to get started.**

## APIs[​](#apis)

The following Node.JS are available:

[
**estimatePrice()**
Estimate the price of a render](/docs/lambda/estimateprice)[
**deployFunction()**
Create a new function in AWS Lambda](/docs/lambda/deployfunction)[
**deleteFunction()**
Delete a function in AWS Lambda](/docs/lambda/deletefunction)[
**getFunctionInfo()**
Gets information about a function](/docs/lambda/getfunctioninfo)[
**getFunctions()**
Lists available Remotion Lambda functions](/docs/lambda/getfunctions)[
**getCompositionsOnLambda()**
Gets list of compositions inside a Lambda function](/docs/lambda/getcompositionsonlambda)[
**deleteSite()**
Delete a bundle from S3](/docs/lambda/deletesite)[
**deploySite()**
Bundle and upload a site to S3](/docs/lambda/deploysite)[
**getAwsClient()**
Access the AWS SDK directly](/docs/lambda/getawsclient)[
**getRegions()**
Get all available regions](/docs/lambda/getregions)[
**getSites()**
Get all available sites](/docs/lambda/getsites)[
**downloadMedia()**
Download a render artifact from S3](/docs/lambda/downloadmedia)[
**getUserPolicy()**
Get the policy JSON for your AWS user](/docs/lambda/getuserpolicy)[
**getRolePolicy()**
Get the policy JSON for your AWS role](/docs/lambda/getrolepolicy)[
**getOrCreateBucket()**
Ensure a Remotion S3 bucket exists](/docs/lambda/getorcreatebucket)[
**getRenderProgress()**
Query the progress of a render](/docs/lambda/getrenderprogress)[
**presignUrl()**
Make a private file public to those with the link](/docs/lambda/presignurl)[
**renderMediaOnLambda()**
Trigger a video or audio render](/docs/lambda/rendermediaonlambda)[
**renderStillOnLambda()**
Trigger a still render](/docs/lambda/renderstillonlambda)[
**simulatePermissions()**
Ensure permissions are correctly set up](/docs/lambda/simulatepermissions)[
**speculateFunctionName()**
Get the lambda function name based on its configuration](/docs/lambda/speculatefunctionname)[
**validateWebhookSignature()**
Validate an incoming webhook request is authentic](/docs/lambda/validatewebhooksignature)[
**appRouterWebhook()**
Handle incoming webhooks specifically for the Next.js app router](/docs/lambda/approuterwebhook)[
**pagesRouterWebhook()**
Handle incoming webhooks specifically for the Next.js pages router](/docs/lambda/pagesrouterwebhook)[
**expressWebhook()**
Handle incoming webhooks specifically for Express.js](/docs/lambda/expresswebhook)

## CLI[​](#cli)

See [here](/docs/lambda/cli) for a list of CLI commands.](/docs/lambda/cli)](/docs/lambda/cli)
](/docs/lambda/cli)
- ](/docs/lambda/cli)