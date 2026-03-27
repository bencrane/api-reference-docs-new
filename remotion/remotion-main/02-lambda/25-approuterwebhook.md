---
title: "appRouterWebhook()"
url: "https://www.remotion.dev/docs/lambda/approuterwebhook"
path: "/docs/lambda/approuterwebhook"
---

"---\nimage: /generated/articles-docs-lambda-approuterwebhook.png\nid: approuterwebhook\ntitle: appRouterWebhook()\nslug: /lambda/approuterwebhook\ncrumb: 'Lambda API'\n---\n\nSimplifies the process of setting up a [Lambda Webhook](/docs/lambda/webhooks) in your Next.js app which is using App Router. Refer to [`pagesRouterWebhook()`](/docs/lambda/pagesrouterwebhook) for doing the same in apps using Pages Router.\n\n## API\n\nThe function accepts an object with six key-value pairs:\n\n### `secret`\n\nYour webhook secret, must be a `string`\n\n### `testing`\n\nWhether or not to allow requests intending to test the endpoint, useful while using Webhook endpoint tester on [Webhooks Page](/docs/lambda/webhooks). Should be a `boolean`.\n\n### `extraHeaders`\n\nAdd your own custom headers to the outgoing response. Provide key-value pairs where both the key and value are strings.\n\n### `onSuccess()`\n\nA function that is called with a [`WebhookSuccessPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates a successful event.\n\n### `onError()`\n\nA function that is called with a [`WebhookErrorPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates an error.\n\n### `onTimeout()`\n\nA function that is called with a [`WebhookTimeoutPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates a timeout.\n\n## Example\n\nSetting up a webhook endpoint in a Next.js app which uses App Router. This will listen on the endpoint: `mydomain.com/api`\n\n```tsx twoslash title=\"app/api/route.ts\"\nimport {appRouterWebhook} from '@remotion/lambda/client';\n\nexport const POST = appRouterWebhook({\n  secret: 'mysecret',\n  testing: true,\n  extraHeaders: {\n    region: 'south-asia',\n  },\n  onSuccess: () => console.log('Rendering Completed Successfully'),\n  onError: () => console.log('Something went wrong while rendering'),\n  onTimeout: () => console.log('Timeout occured while rendering'),\n});\n\nexport const OPTIONS = POST;\n```\n\nSee [Webhooks](/docs/lambda/webhooks) for an Express example.\n\n## See also\n\n- [Webhooks](/docs/lambda/webhooks)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)\n"

Simplifies the process of setting up a [Lambda Webhook](/docs/lambda/webhooks) in your Next.js app which is using App Router. Refer to [`pagesRouterWebhook()`](/docs/lambda/pagesrouterwebhook) for doing the same in apps using Pages Router.

## API[​](#api)

The function accepts an object with six key-value pairs:

### `secret`[​](#secret)

Your webhook secret, must be a `string`

### `testing`[​](#testing)

Whether or not to allow requests intending to test the endpoint, useful while using Webhook endpoint tester on [Webhooks Page](/docs/lambda/webhooks). Should be a `boolean`.

### `extraHeaders`[​](#extraheaders)

Add your own custom headers to the outgoing response. Provide key-value pairs where both the key and value are strings.

### `onSuccess()`[​](#onsuccess)

A function that is called with a [`WebhookSuccessPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates a successful event.

### `onError()`[​](#onerror)

A function that is called with a [`WebhookErrorPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates an error.

### `onTimeout()`[​](#ontimeout)

A function that is called with a [`WebhookTimeoutPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates a timeout.

## Example[​](#example)

Setting up a webhook endpoint in a Next.js app which uses App Router. This will listen on the endpoint: `mydomain.com/api`

```

app/api/route.tsimport {appRouterWebhook} from '@remotion/lambda/client';

export const POST = appRouterWebhook({
  secret: 'mysecret',
  testing: true,
  extraHeaders: {
    region: 'south-asia',
  },
  onSuccess: () => console.log('Rendering Completed Successfully'),
  onError: () => console.log('Something went wrong while rendering'),
  onTimeout: () => console.log('Timeout occured while rendering'),
});

export const OPTIONS = POST;Copy
```

See [Webhooks](/docs/lambda/webhooks) for an Express example.

## See also[​](#see-also)

- [Webhooks](/docs/lambda/webhooks)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/app-router-webhook.ts)