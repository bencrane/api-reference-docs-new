---
title: "validateWebhookSignature()"
url: "https://www.remotion.dev/docs/lambda/validatewebhooksignature"
path: "/docs/lambda/validatewebhooksignature"
---

"---\nimage: /generated/articles-docs-lambda-validatewebhooksignature.png\nid: validatewebhooksignature\ntitle: validateWebhookSignature()\nslug: /lambda/validatewebhooksignature\ncrumb: 'Lambda API'\n---\n\n<AvailableFrom v=\"3.2.30\" />\n\nValidates that the signature that was received by a [webhook](/docs/lambda/webhooks) endpoint is authentic. If the validation fails, an error is thrown.\n\n## API\n\nThe function accepts an object with three key-value pairs:\n\n### `secret`\n\nThe same webhook secret that was passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda)'s webhook options.\n\n### `body`\n\nThe body that was received by the endpoint - takes a parsed JSON object, not a `string`.\n\n### `signatureHeader`\n\nThe `X-Remotion-Signature` header from the request that was received by the endpoint.\n\n## Example\n\nIn the following Next.JS webhook endpoint, an error gets thrown if the signature does not match the one expected one or is missing..\n\n```tsx twoslash title=\"pages/api/webhook.ts\"\ntype NextApiRequest = {\n  body: object;\n  headers: Record<string, string>;\n};\ntype NextApiResponse = {\n  status: (code: number) => {json: (body: object) => void};\n};\n// ---cut---\nimport {validateWebhookSignature, WebhookPayload} from '@remotion/lambda/client';\n\nexport default async function handler(req: NextApiRequest, res: NextApiResponse) {\n  validateWebhookSignature({\n    secret: process.env.WEBHOOK_SECRET as string,\n    body: req.body,\n    signatureHeader: req.headers['x-remotion-signature'] as string,\n  });\n\n  // If code reaches this path, the webhook is authentic.\n  const payload = req.body as WebhookPayload;\n  if (payload.type === 'success') {\n    // ...\n  } else if (payload.type === 'timeout') {\n    // ...\n  }\n\n  res.status(200).json({\n    success: true,\n  });\n}\n```\n\nSee [Webhooks](/docs/lambda/webhooks) for an Express example.\n\n## See also\n\n- [Webhooks](/docs/lambda/webhooks)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)\n"
[v3.2.30](https://github.com/remotion-dev/remotion/releases/v3.2.30)

Validates that the signature that was received by a [webhook](/docs/lambda/webhooks) endpoint is authentic. If the validation fails, an error is thrown.

## API[​](#api)

The function accepts an object with three key-value pairs:

### `secret`[​](#secret)

The same webhook secret that was passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda)'s webhook options.

### `body`[​](#body)

The body that was received by the endpoint - takes a parsed JSON object, not a `string`.

### `signatureHeader`[​](#signatureheader)

The `X-Remotion-Signature` header from the request that was received by the endpoint.

## Example[​](#example)

In the following Next.JS webhook endpoint, an error gets thrown if the signature does not match the one expected one or is missing..

```

pages/api/webhook.tsimport {validateWebhookSignature, WebhookPayload} from '@remotion/lambda/client';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  validateWebhookSignature({
    secret: process.env.WEBHOOK_SECRET as string,
    body: req.body,
    signatureHeader: req.headers['x-remotion-signature'] as string,
  });

  // If code reaches this path, the webhook is authentic.
  const payload = req.body as WebhookPayload;
  if (payload.type === 'success') {
    // ...
  } else if (payload.type === 'timeout') {
    // ...
  }

  res.status(200).json({
    success: true,
  });
}Copy
```

See [Webhooks](/docs/lambda/webhooks) for an Express example.

## See also[​](#see-also)

- [Webhooks](/docs/lambda/webhooks)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/validate-webhook-signature.ts)