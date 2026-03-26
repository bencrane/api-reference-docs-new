---
title: "registerUsageEvent()"
url: "https://www.remotion.dev/docs/licensing/register-usage-event"
path: "/docs/licensing/register-usage-event"
---

"---\nimage: /generated/articles-docs-licensing-register-usage-event.png\nid: register-usage-event\ntitle: registerUsageEvent()\nslug: /licensing/register-usage-event\ncrumb: '@remotion/licensing'\n---\n\nRegisters a usage point for your Remotion license.  \nAllows for accurate and up to date reporting and to track your usage on the Remotion dashboard.\n\n```tsx twoslash title=\"Register a usage point\"\nimport {registerUsageEvent} from '@remotion/licensing';\n\nawait registerUsageEvent({\n  licenseKey: 'rm_pub_xxxxx',\n  event: 'cloud-render',\n  host: 'https://myapp.com',\n  succeeded: true,\n});\n```\n\n## API\n\nAn object with the following properties:\n\n### `licenseKey`<AvailableFrom v=\"4.0.409\"/>\n\nType: `string`\n\nYour Remotion public API key. You can get it from your Remotion.pro dashboard.\n\n### `event`\n\nType: `string`\n\nThe event you want to register. This can be one of the following:\n\n- `web-render`\n- `cloud-render`\n- `webcodec-conversion` _(deprecated, use `web-render` instead)_\n\n### `host`\n\nThe domain at here you host your app.  \nThis should be the value of what `window.location.origin` evaluates to on your frontend.  \nIf the host is `localhost` or similar, it will be registered as non-billable.\n\n### `succeeded`\n\nWhether the event was successful or not.  \nIf the event was not successful, it will be registered as a non-billable event.\n\n## Return value\n\nA promise that resolves when the event was successfully registered.\n\nThe resolved object contains two properties:\n\n### `billable`\n\nWhether this was an event that should be billed.\n\n### `classification`\n\nEither, `\"billable\"`, `\"development\"` or `\"failed\"`.  \nYou do not have to pay for failed renders or renders doing development.\n\n## See also\n\n- [`@remotion/licensing`](/docs/licensing)\n- [`getUsage()`](/docs/licensing/get-usage)\n"

Registers a usage point for your Remotion license.

Allows for accurate and up to date reporting and to track your usage on the Remotion dashboard.

```

Register a usage pointimport {registerUsageEvent} from '@remotion/licensing';

await registerUsageEvent({
  licenseKey: 'rm_pub_xxxxx',
  event: 'cloud-render',
  host: 'https://myapp.com',
  succeeded: true,
});Copy
```

## API[​](#api)

An object with the following properties:

### `licenseKey`[v4.0.409](https://github.com/remotion-dev/remotion/releases/v4.0.409)[​](#licensekey)

Type: `string`

Your Remotion public API key. You can get it from your Remotion.pro dashboard.

### `event`[​](#event)

Type: `string`

The event you want to register. This can be one of the following:

- `web-render`

- `cloud-render`

- `webcodec-conversion` *(deprecated, use `web-render` instead)*

### `host`[​](#host)

The domain at here you host your app.

This should be the value of what `window.location.origin` evaluates to on your frontend.

If the host is `localhost` or similar, it will be registered as non-billable.

### `succeeded`[​](#succeeded)

Whether the event was successful or not.

If the event was not successful, it will be registered as a non-billable event.

## Return value[​](#return-value)

A promise that resolves when the event was successfully registered.

The resolved object contains two properties:

### `billable`[​](#billable)

Whether this was an event that should be billed.

### `classification`[​](#classification)

Either, `"billable"`, `"development"` or `"failed"`.

You do not have to pay for failed renders or renders doing development.

## See also[​](#see-also)

- [`@remotion/licensing`](/docs/licensing)

- [`getUsage()`](/docs/licensing/get-usage)
](/docs/licensing/get-usage)](/docs/licensing/get-usage)
](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)
- ](/docs/licensing/get-usage)