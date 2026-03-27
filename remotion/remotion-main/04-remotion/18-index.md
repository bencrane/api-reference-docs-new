---
title: "<Img>"
url: "https://www.remotion.dev/docs/img"
path: "/docs/img"
---

"---\nimage: /generated/articles-docs-img.png\ntitle: <Img>\nid: img\ncrumb: 'API'\n---\n\nThe `<Img>` tag can be used like a regular `<img>` HTML tag.\n\nIf you use `<Img>`, Remotion will ensure that the image is loaded before rendering the frame. That way you can avoid flickers if the image does not load immediately during rendering.\n\n## API\n\n### `src`\n\n[Put an image into the `public/` folder](/docs/assets) and use [`staticFile()`](/docs/staticfile) to reference it.\n\n```tsx twoslash\nimport {AbsoluteFill, Img, staticFile} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  return (\n    <AbsoluteFill>\n      <Img src={staticFile('hi.png')} />\n    </AbsoluteFill>\n  );\n};\n```\n\nYou can also load a remote image:\n\n```tsx twoslash\nimport {AbsoluteFill, Img} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  return (\n    <AbsoluteFill>\n      <Img src={'https://picsum.photos/200/300'} />\n    </AbsoluteFill>\n  );\n};\n```\n\n### `onError`\n\nTo use the `<Img>` tag in a resilient way, handle the error that occurs when an image can not be loaded:\n\n```tsx twoslash\nimport {AbsoluteFill, Img, staticFile} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  return (\n    <AbsoluteFill>\n      <Img\n        src={staticFile('hi.png')}\n        onError={(event) => {\n          // Handle image loading error here\n        }}\n      />\n    </AbsoluteFill>\n  );\n};\n```\n\nIf an error occurs, the component must be unmounted or the `src` must be replaced, otherwise the render will time out.\n\nFrom `v3.3.82`, the image load will first be retried before `onError` is thrown.\n\n### `maxRetries`<AvailableFrom v=\"3.3.82\"/>\n\nIf an image fails to load, it will be retried from `v3.3.82`. The default value is `2`.  \nAn exponential backoff is being used, with 1000ms delay between the first and second attempt, then 2000ms, then 4000ms and so on.\n\n### `pauseWhenLoading?`<AvailableFrom v=\"4.0.111\"/>\n\nIf set to `true`, pause the Player when the image is loading. See: [Buffer state](/docs/player/buffer-state).\n\n### `delayRenderTimeoutInMilliseconds?`<AvailableFrom v=\"4.0.140\" />\n\nCustomize the [timeout](/docs/delay-render#modifying-the-timeout) of the [`delayRender()`](/docs/delay-render) call that this component makes.\n\n### `delayRenderRetries?`<AvailableFrom v=\"4.0.140\" />\n\nCustomize the [number of retries](/docs/delay-render#retrying) of the [`delayRender()`](/docs/delay-render) call that this component makes.  \nPrefer the [`maxRetries`](#maxretries) prop over this.\n\n## Other props\n\nRemotion inherits the props of the regular `<img>` tag, like for example `style`.\n\n## GIFs\n\nDon't use the `<Img>` tag for GIFs, use [`@remotion/gif`](/docs/gif) instead.\n\n## Error behavior\n\nFrom v4.0.0: If the image fails to load and no retries are left, then [`cancelRender`](/docs/cancel-render) will be called to throw an error, unless you handle the error using `onError()`.\n\nFrom v3.3.82: If an image fails to load, it will be retried up to two times.\n\nIn earlier versions, failing to load an image would lead to an error message in the console and an eventual timeout.\n\n## Restrictions\n\n- The maximum resolution that Chrome can display is `2^29` pixels (539 megapixels) <sup><a href=\"https://stackoverflow.com/questions/57223559/what-is-the-maximum-image-dimensions-supported-in-desktop-chrome#:~:text=than%202%5E29-,(539MP)\">[source]</a></sup>. Remotion inherits this restriction.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Img.tsx)\n- [Use `<Img>` and `<IFrame>` tags](/docs/use-img-and-iframe)\n"

The `<Img>` tag can be used like a regular `<img>` HTML tag.

If you use `<Img>`, Remotion will ensure that the image is loaded before rendering the frame. That way you can avoid flickers if the image does not load immediately during rendering.

## API[​](#api)

### `src`[​](#src)

[Put an image into the `public/` folder](/docs/assets) and use [`staticFile()`](/docs/staticfile) to reference it.

```
import {AbsoluteFill, Img, staticFile} from 'remotion';

export const MyComp: React.FC = () => {
  return (
    <AbsoluteFill>
      <Img src={staticFile('hi.png')} />
    </AbsoluteFill>
  );
};Copy
```

You can also load a remote image:

```
import {AbsoluteFill, Img} from 'remotion';

export const MyComp: React.FC = () => {
  return (
    <AbsoluteFill>
      <Img src={'https://picsum.photos/200/300'} />
    </AbsoluteFill>
  );
};Copy
```

### `onError`[​](#onerror)

To use the `<Img>` tag in a resilient way, handle the error that occurs when an image can not be loaded:

```
import {AbsoluteFill, Img, staticFile} from 'remotion';

export const MyComp: React.FC = () => {
  return (
    <AbsoluteFill>
      <Img
        src={staticFile('hi.png')}
        onError={(event) => {
          // Handle image loading error here
        }}
      />
    </AbsoluteFill>
  );
};Copy
```

If an error occurs, the component must be unmounted or the `src` must be replaced, otherwise the render will time out.

From `v3.3.82`, the image load will first be retried before `onError` is thrown.

### `maxRetries`[v3.3.82](https://github.com/remotion-dev/remotion/releases/v3.3.82)[​](#maxretries)

If an image fails to load, it will be retried from `v3.3.82`. The default value is `2`.

An exponential backoff is being used, with 1000ms delay between the first and second attempt, then 2000ms, then 4000ms and so on.

### `pauseWhenLoading?`[v4.0.111](https://github.com/remotion-dev/remotion/releases/v4.0.111)[​](#pausewhenloading)

If set to `true`, pause the Player when the image is loading. See: [Buffer state](/docs/player/buffer-state).

### `delayRenderTimeoutInMilliseconds?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#delayrendertimeoutinmilliseconds)

Customize the [timeout](/docs/delay-render#modifying-the-timeout) of the [`delayRender()`](/docs/delay-render) call that this component makes.

### `delayRenderRetries?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#delayrenderretries)

Customize the [number of retries](/docs/delay-render#retrying) of the [`delayRender()`](/docs/delay-render) call that this component makes.

Prefer the [`maxRetries`](#maxretries) prop over this.

## Other props[​](#other-props)

Remotion inherits the props of the regular `<img>` tag, like for example `style`.

## GIFs[​](#gifs)

Don't use the `<Img>` tag for GIFs, use [`@remotion/gif`](/docs/gif) instead.

## Error behavior[​](#error-behavior)

From v4.0.0: If the image fails to load and no retries are left, then [`cancelRender`](/docs/cancel-render) will be called to throw an error, unless you handle the error using `onError()`.

From v3.3.82: If an image fails to load, it will be retried up to two times.

In earlier versions, failing to load an image would lead to an error message in the console and an eventual timeout.

## Restrictions[​](#restrictions)

- The maximum resolution that Chrome can display is `2^29` pixels (539 megapixels) [[source]](https://stackoverflow.com/questions/57223559/what-is-the-maximum-image-dimensions-supported-in-desktop-chrome#:~:text=than%202%5E29-,(539MP)). Remotion inherits this restriction.

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

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Img.tsx)

- [Use `<Img>` and `<IFrame>` tags](/docs/use-img-and-iframe)
](/docs/use-img-and-iframe)](/docs/use-img-and-iframe)
](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)
- ](/docs/use-img-and-iframe)