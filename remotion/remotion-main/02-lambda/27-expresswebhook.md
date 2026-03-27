---
title: "expressWebhook()"
url: "https://www.remotion.dev/docs/lambda/expresswebhook"
path: "/docs/lambda/expresswebhook"
---

"---\nimage: /generated/articles-docs-lambda-expresswebhook.png\nid: expresswebhook\ntitle: expressWebhook()\nslug: /lambda/expresswebhook\ncrumb: 'Lambda API'\n---\n\nSimplifies the process of setting up a [Lambda Webhook](/docs/lambda/webhooks) in your Express.js server. See [`pagesRouterWebhook()`](/docs/lambda/pagesrouterwebhook) and [`appRouterWebhook()`](/docs/lambda/approuterwebhook) for doing the same with Next.js apps.\n\n## API\n\nThe function accepts an object with six key-value pairs:\n\n### `secret`\n\nYour webhook secret, must be a `string`\n\n### `testing`\n\nWhether or not to allow requests intending to test the endpoint, useful while using Webhook endpoint tester on [Webhooks Page](/docs/lambda/webhooks). Should be a `boolean`.\n\n### `extraHeaders`\n\nAdd your own custom headers to the outgoing response. Provide key-value pairs where both the key and value are strings.\n\n### `onSuccess()`\n\nA function that is called with a [`WebhookSuccessPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates a successful event.\n\n### `onError()`\n\nA function that is called with a [`WebhookErrorPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates an error.\n\n### `onTimeout()`\n\nA function that is called with a [`WebhookTimeoutPayload`](/docs/lambda/webhooks#response) object as an argument when the incoming request indicates a timeout.\n\n## Example\n\nSetting up a webhook endpoint in an Express.js server.\n\n```jsx twoslash title=\"server.js\"\nimport {expressWebhook} from '@remotion/lambda/client';\n\nconst handler = expressWebhook({\n  secret: 'mysecret',\n  testing: true,\n  extraHeaders: {\n    region: \"south-asia\"\n  },\n  onSuccess: () => console.log('Rendering Completed Successfully'),\n  onError: () => console.log('Something went wrong while rendering'),\n  onTimeout: () => console.log('Timeout occured while rendering'),\n})\n\nrouter.post(\"/webhook\", jsonParser, handler);\n\nrouter.options(\"/webhook\", jsonParser, handler);\n```\n\nSee [Webhooks](/docs/lambda/webhooks) for a detailed example.\n\n## See also\n\n- [Webhooks](/docs/lambda/webhooks)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)\n"

Simplifies the process of setting up a [Lambda Webhook](/docs/lambda/webhooks) in your Express.js server. See [`pagesRouterWebhook()`](/docs/lambda/pagesrouterwebhook) and [`appRouterWebhook()`](/docs/lambda/approuterwebhook) for doing the same with Next.js apps.

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

Setting up a webhook endpoint in an Express.js server.

```

server.jsimport {expressWebhook} from '@remotion/lambda/client';

const handler = expressWebhook({
  secret: 'mysecret',
  testing: true,
  extraHeaders: {
    region: "south-asia"
  },
  onSuccess: () => console.log('Rendering Completed Successfully'),
  onError: () => console.log('Something went wrong while rendering'),
  onTimeout: () => console.log('Timeout occured while rendering'),
})

router.post("/webhook", jsonParser, handler);

router.options("/webhook", jsonParser, handler);Copy
```

See [Webhooks](/docs/lambda/webhooks) for a detailed example.

## See also[​](#see-also)

- [Webhooks](/docs/lambda/webhooks)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/express-webhook.ts)