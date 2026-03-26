---
title: "<IFrame>"
url: "https://www.remotion.dev/docs/iframe"
path: "/docs/iframe"
---

"---\nimage: /generated/articles-docs-iframe.png\ntitle: <IFrame>\nid: iframe\ncrumb: 'API'\n---\n\nThe `<IFrame />` can be used like the regular `<iframe>` HTML tag.\n\nRemotion automatically wraps the `<iframe>` in a [`delayRender()`](/docs/delay-render) call\nand ensures that the iframe is loaded before rendering the frame.\n\nIdeally, the website should not have any animations, since only animations using [`useCurrentFrame()`](/docs/use-current-frame) are supported by Remotion. See [Flickering](/docs/flickering) for an explanation.\n\n## Example\n\n```tsx twoslash\nimport {IFrame} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  return <IFrame src=\"https://remotion.dev\" />;\n};\n```\n\n## Props\n\n### `src`\n\nThe URL to load.\n\n### `delayRenderTimeoutInMilliseconds`<AvailableFrom v=\"4.0.140\" />\n\nCustomize the [timeout](/docs/delay-render#modifying-the-timeout) of the [`delayRender()`](/docs/delay-render) call that this component makes.\n\n### `delayRenderRetries`<AvailableFrom v=\"4.0.140\" />\n\nCustomize the [number of retries](/docs/delay-render#retrying) of the [`delayRender()`](/docs/delay-render) call that this component makes.  \nPrefer the [`maxRetries`](/docs/img#maxretries) prop over this.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering={false} serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/IFrame.tsx)\n- [Use `<Img>` and `<IFrame>` tags](/docs/use-img-and-iframe)\n"

The `<IFrame />` can be used like the regular `<iframe>` HTML tag.

Remotion automatically wraps the `<iframe>` in a [`delayRender()`](/docs/delay-render) call
and ensures that the iframe is loaded before rendering the frame.

Ideally, the website should not have any animations, since only animations using [`useCurrentFrame()`](/docs/use-current-frame) are supported by Remotion. See [Flickering](/docs/flickering) for an explanation.

## Example[​](#example)

```
import {IFrame} from 'remotion';

export const MyComp: React.FC = () => {
  return <IFrame src="https://remotion.dev" />;
};Copy
```

## Props[​](#props)

### `src`[​](#src)

The URL to load.

### `delayRenderTimeoutInMilliseconds`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#delayrendertimeoutinmilliseconds)

Customize the [timeout](/docs/delay-render#modifying-the-timeout) of the [`delayRender()`](/docs/delay-render) call that this component makes.

### `delayRenderRetries`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#delayrenderretries)

Customize the [number of retries](/docs/delay-render#retrying) of the [`delayRender()`](/docs/delay-render) call that this component makes.

Prefer the [`maxRetries`](/docs/img#maxretries) prop over this.

## Compatibility[​](#compatibility)

|  Browsers Environments
|  
Chrome 
Firefox 
Safari 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
 

## See also[​](#see-also)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/IFrame.tsx)

- [Use `<Img>` and `<IFrame>` tags](/docs/use-img-and-iframe)
](/docs/use-img-and-iframe)](/docs/use-img-and-iframe)
](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)