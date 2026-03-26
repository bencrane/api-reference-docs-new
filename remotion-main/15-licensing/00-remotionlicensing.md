---
title: "@remotion/licensing"
url: "https://www.remotion.dev/docs/licensing/"
path: "/docs/licensing/"
---

"---\nimage: /generated/articles-docs-licensing-index.png\nsidebar_label: Overview\ntitle: '@remotion/licensing'\ncrumb: API\n---\n\n_available from v4.0.237_\n\nThis package allows holders of the [Company License](https://remotion.pro/license) to send events to Remotion to track the usage of renders.  \nAlso, it offers an API to programmatically check the usage in order to implement spend controls.\n\n### How do I use this package?\n\nNot directly - pass the `licenseKey` option in the renderer package you use.\n\n**Supported packages**\n\n- [`@remotion/lambda`](/docs/lambda): Pass `licenseKey` to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#licensekey) and [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#licensekey) to trigger an event.\n- [`@remotion/vercel`](/docs/vercel/api): Pass `licenseKey` to [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel#licensekey) and [`renderStillOnVercel()`](/docs/vercel/render-still-on-vercel#licensekey) to trigger an event.\n- [`@remotion/renderer`](/docs/renderer): Pass `licenseKey` to [`renderMedia()`](/docs/renderer/render-media#licensekey) and [`renderStill()`](/docs/renderer/render-still#licensekey) to trigger an event.\n- [`@remotion/web-renderer`](/docs/client-side-rendering/telemetry): An event is always sent. Pass a real `licenseKey`, or declare eligibility for the free license with `licenseKey: \"free-license\"`. See [Telemetry in client-side rendering](/docs/client-side-rendering/telemetry#setting-a-license-key).\n\n<details>\n  <summary>Deprecated packages</summary>\n\n- [`@remotion/cloudrun`](/docs/cloudrun): No telemetry is implemented. Use [`@remotion/licensing`](/docs/licensing) directly to track usage.\n- [`@remotion/webcodecs`](/docs/webcodecs): Telemetry was removed in v4.0.399 because this package is no longer monetized.\n</details>\n\nOn your Company License dashboard on [remotion.pro](https://remotion.pro), you can find your license keys under the \"Usage\" tab.\n\n### Do I need to use this package?\n\nFor all versions below Remotion 5.0, it is **voluntary** to use this package.  \nAn exception is [`@remotion/web-renderer`](/docs/client-side-rendering/telemetry), which will always send telemetry events.\n\nIf you are not eligible for the Free License, you need to get a Company License and are required to keep your allowance up to date.\n\nFrom Remotion 5.0, telemetry reporting using the `licenseKey` option is **mandatory** for Remotion for Automators (render-based licensing).\n\nFor Remotion for Creators (seat-based licensing), telemetry reporting is optional. Remotion for Creators is meant for low-volume rendering within and for your own company, not to serve (personalized) videos to your end users.\n\n### Can I use this package to count renders if I am eligible for the Free License?\n\nYes, you may still create a project on [remotion.pro](https://remotion.pro) and use this package to count renders.  \nYou do not have to pay anything for the renders.  \nThis package is only used to count the number of renders, not for billing.\n\n### Will I get charged based on the usage?\n\nThis package currently only counts renders, it does not bill you based on them.  \nIf you are a Company License holder, you need to manually adjust your seat count on [remotion.pro](https://remotion.pro) to cover all your renders.\n\nHowever, the plan is to introduce a system that automatically bills you based on the usage, eliminating the need for you to manually adjust the seat count.\n\n## Installation\n\n<Installation pkg=\"@remotion/licensing\" />\n\n## API\n\nimport {TableOfContents} from './TableOfContents';\n\n<TableOfContents />\n\n## License\n\n[Remotion License](https://remotion.dev/license)\n"

*available from v4.0.237*

This package allows holders of the [Company License](https://remotion.pro/license) to send events to Remotion to track the usage of renders.

Also, it offers an API to programmatically check the usage in order to implement spend controls.

### How do I use this package?[​](#how-do-i-use-this-package)

Not directly - pass the `licenseKey` option in the renderer package you use.

**Supported packages**

- [`@remotion/lambda`](/docs/lambda): Pass `licenseKey` to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#licensekey) and [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#licensekey) to trigger an event.

- [`@remotion/vercel`](/docs/vercel/api): Pass `licenseKey` to [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel#licensekey) and [`renderStillOnVercel()`](/docs/vercel/render-still-on-vercel#licensekey) to trigger an event.

- [`@remotion/renderer`](/docs/renderer): Pass `licenseKey` to [`renderMedia()`](/docs/renderer/render-media#licensekey) and [`renderStill()`](/docs/renderer/render-still#licensekey) to trigger an event.

- [`@remotion/web-renderer`](/docs/client-side-rendering/telemetry): An event is always sent. Pass a real `licenseKey`, or declare eligibility for the free license with `licenseKey: "free-license"`. See [Telemetry in client-side rendering](/docs/client-side-rendering/telemetry#setting-a-license-key).

Deprecated packages

- [`@remotion/cloudrun`](/docs/cloudrun): No telemetry is implemented. Use [`@remotion/licensing`](/docs/licensing) directly to track usage.

- [`@remotion/webcodecs`](/docs/webcodecs): Telemetry was removed in v4.0.399 because this package is no longer monetized.

On your Company License dashboard on [remotion.pro](https://remotion.pro), you can find your license keys under the "Usage" tab.

### Do I need to use this package?[​](#do-i-need-to-use-this-package)

For all versions below Remotion 5.0, it is **voluntary** to use this package.

An exception is [`@remotion/web-renderer`](/docs/client-side-rendering/telemetry), which will always send telemetry events.

If you are not eligible for the Free License, you need to get a Company License and are required to keep your allowance up to date.

From Remotion 5.0, telemetry reporting using the `licenseKey` option is **mandatory** for Remotion for Automators (render-based licensing).

For Remotion for Creators (seat-based licensing), telemetry reporting is optional. Remotion for Creators is meant for low-volume rendering within and for your own company, not to serve (personalized) videos to your end users.

### Can I use this package to count renders if I am eligible for the Free License?[​](#can-i-use-this-package-to-count-renders-if-i-am-eligible-for-the-free-license)

Yes, you may still create a project on [remotion.pro](https://remotion.pro) and use this package to count renders.

You do not have to pay anything for the renders.

This package is only used to count the number of renders, not for billing.

### Will I get charged based on the usage?[​](#will-i-get-charged-based-on-the-usage)

This package currently only counts renders, it does not bill you based on them.

If you are a Company License holder, you need to manually adjust your seat count on [remotion.pro](https://remotion.pro) to cover all your renders.

However, the plan is to introduce a system that automatically bills you based on the usage, eliminating the need for you to manually adjust the seat count.

## Installation[​](#installation)

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/licensingCopy
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

## API[​](#api)

[
**registerUsageEvent()**
Register a render](/docs/licensing/register-usage-event)[
**getUsage()**
Query usage of company license](/docs/licensing/get-usage)

## License[​](#license)

[Remotion License](https://remotion.dev/license)](https://remotion.dev/license)](https://remotion.dev/license)
](https://remotion.dev/license)
- ](https://remotion.dev/license)
- ](https://remotion.dev/license)
- ](https://remotion.dev/license)
- ](https://remotion.dev/license)
- ](https://remotion.dev/license)
- ](https://remotion.dev/license)