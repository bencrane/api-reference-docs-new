---
title: "calculateMetadata()"
url: "https://www.remotion.dev/docs/calculate-metadata"
path: "/docs/calculate-metadata"
---

"---\nimage: /generated/articles-docs-calculate-metadata.png\nid: calculate-metadata\ntitle: calculateMetadata()\ncrumb: 'API'\n---\n\n# calculateMetadata()<AvailableFrom v=\"4.0.0\" />\n\n`calculateMetadata` is a prop that gets passed to [`<Composition>`](/docs/composition) and takes a callback function which may transform metadata.\n\nUse it if you:\n\n<div>\n  <Step>1</Step> need to make the `durationInFrames`, `width`, `height`, or `fps` <a href=\"/docs/dynamic-metadata\">dynamic based on some data</a>\n</div>\n<div>\n\n<Step>2</Step> want to transform the props passed to the composition, for example to do <a href=\"/docs/data-fetching\">data fetching</a>\n</div>\n<div>\n<Step>3</Step> want to add a per-composition default codec\n</div>\n<div>\n<Step>4</Step> want to add per-composition default video image format, pixel format, or ProRes profile\n</div>\n<div>\n<Step>5</Step> want to run code once, before the actual render starts.\n</div>\n\nThe `calculateMetadata()` function is called a single time, independently from the concurrency of the render.  \nIt runs in a separate tab, as part of the render process calling [`selectComposition()`](/docs/renderer/select-composition).\n\n## Usage / API\n\nDefine a function, you may type it using `CalculateMetadataFunction` - the generic argument takes the props of the component of your composition:\n\n```tsx twoslash title=\"src/Root.tsx\"\n// @filename: MyComp.tsx\nimport React from 'react';\nexport type MyComponentProps = {\n  text: string;\n  duration: number;\n};\n\nexport const MyComponent: React.FC<MyComponentProps> = ({text}) => {\n  return <div>{text}</div>;\n};\n\n// @filename: Vid.tsx\n// ---cut---\nimport React from 'react';\nimport {CalculateMetadataFunction, Composition} from 'remotion';\nimport {MyComponent, MyComponentProps} from './MyComp';\n\nconst calculateMetadata: CalculateMetadataFunction<MyComponentProps> = ({props, defaultProps, abortSignal, isRendering}) => {\n  return {\n    // Change the metadata\n    durationInFrames: props.duration,\n    // or transform some props\n    props,\n    // or add per-composition default codec\n    defaultCodec: 'h264',\n    // or add per-composition default video image format\n    defaultVideoImageFormat: 'png',\n    // or add per-composition default pixel format\n    defaultPixelFormat: 'yuv420p',\n    // or add per-composition default ProRes profile\n    defaultProResProfile: 'hq',\n  };\n};\n\nexport const Root: React.FC = () => {\n  return (\n    <Composition\n      id=\"MyComp\"\n      component={MyComponent}\n      durationInFrames={300}\n      fps={30}\n      width={1920}\n      height={1080}\n      defaultProps={{\n        text: 'Hello World',\n        duration: 1,\n      }}\n      calculateMetadata={calculateMetadata}\n    />\n  );\n};\n```\n\nAs argument, you get an object with the following properties:\n\n- `defaultProps`: Only the default props, taken from the [`defaultProps`](/docs/composition#defaultprops) prop or the Remotion Studio Data sidebar.\n- `props`: The [resolved props](/docs/props-resolution), taking input props into account.\n- `abortSignal`: An [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) which you can use to abort network requests if [the default props have been changed](/docs/data-fetching#aborting-stale-requests) in the meanwhile.\n- `compositionId` (_available from v4.0.98_): The ID of the current composition\n- `isRendering` (_available from v4.0.342_): A boolean indicating whether the function is being called during rendering (`true`) or in other contexts like the Studio (`false`)\n\nThe function must return an pure JSON-serializable object, which can contain the following properties:\n\n- `props`: The [final props](/docs/props-resolution) the component receives. It must have the [same shape](/docs/data-fetching#usage) as the `props` received by this function. The props must be a plain object and must not contain any non-JSON-serializable values, except `Date`, `Map`, `Set` and [`staticFile()`](/docs/staticfile). Optional.\n- `durationInFrames`: The duration of the composition in frames. Optional.\n- `width`: The width of the composition in pixels. Optional.\n- `height`: The height of the composition in pixels. Optional.\n- `fps`: The frames per second of the composition. Optional.\n- `defaultCodec`: The default codec to use for the composition. Optional.\n- `defaultOutName`: The default output name when rendering (without file extension). Optional. <AvailableFrom v=\"4.0.268\" />\n- `defaultVideoImageFormat`: The default video image format (`'png'`, `'jpeg'`, or `'none'`). Optional. <AvailableFrom v=\"4.0.316\" />\n- `defaultPixelFormat`: The default pixel format (`'yuv420p'`, `'yuva420p'`, `'yuv422p'`, `'yuv444p'`, `'yuv420p10le'`, `'yuv422p10le'`, `'yuv444p10le'`, or `'yuva444p10le'`). Optional. <AvailableFrom v=\"4.0.316\" />\n- `defaultProResProfile`: The default ProRes profile (`'4444-xq'`, `'4444'`, `'hq'`, `'standard'`, `'light'`, or `'proxy'`). Optional. <AvailableFrom v=\"4.0.367\" />\n\nIf you return a field, it will take precendence over the props directly passed to the composition. The defaultCodec returned will have a higher priority than the config file, but less priority than explicitly passing the option to renderMedia() i.e. the composition will be rendered with this codec if nothing with higher priority was specified.\n\nThe function may be `async`.\n\nThe function must resolve within the [timeout](/docs/delay-render#timeout).\n\nThe function will get executed every time the props in the [Remotion Studio](/docs/visual-editing) changes.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs bun serverlessFunctions clientSideRendering serverSideRendering player={false} studio />\n\n## See also\n\n- [`<Composition>`](/docs/composition)\n- [Data fetching](/docs/data-fetching)\n- [Dynamic metadata](/docs/dynamic-metadata)\n"

`calculateMetadata` is a prop that gets passed to [`<Composition>`](/docs/composition) and takes a callback function which may transform metadata.

Use it if you:

[](#1)
[1](#1)[ ](#1) need to make the `durationInFrames`, `width`, `height`, or `fps` [dynamic based on some data](/docs/dynamic-metadata)

[](#2)
[2](#2)[ ](#2) want to transform the props passed to the composition, for example to do [data fetching](/docs/data-fetching)

[](#3)
[3](#3)[ ](#3) want to add a per-composition default codec

[](#4)
[4](#4)[ ](#4) want to add per-composition default video image format, pixel format, or ProRes profile

[](#5)
[5](#5)[ ](#5) want to run code once, before the actual render starts.

The `calculateMetadata()` function is called a single time, independently from the concurrency of the render.

It runs in a separate tab, as part of the render process calling [`selectComposition()`](/docs/renderer/select-composition).

## Usage / API[​](#usage--api)

Define a function, you may type it using `CalculateMetadataFunction` - the generic argument takes the props of the component of your composition:

```

src/Root.tsximport React from 'react';
import {CalculateMetadataFunction, Composition} from 'remotion';
import {MyComponent, MyComponentProps} from './MyComp';

const calculateMetadata: CalculateMetadataFunction<MyComponentProps> = ({props, defaultProps, abortSignal, isRendering}) => {
  return {
    // Change the metadata
    durationInFrames: props.duration,
    // or transform some props
    props,
    // or add per-composition default codec
    defaultCodec: 'h264',
    // or add per-composition default video image format
    defaultVideoImageFormat: 'png',
    // or add per-composition default pixel format
    defaultPixelFormat: 'yuv420p',
    // or add per-composition default ProRes profile
    defaultProResProfile: 'hq',
  };
};

export const Root: React.FC = () => {
  return (
    <Composition
      id="MyComp"
      component={MyComponent}
      durationInFrames={300}
      fps={30}
      width={1920}
      height={1080}
      defaultProps={{
        text: 'Hello World',
        duration: 1,
      }}
      calculateMetadata={calculateMetadata}
    />
  );
};Copy
```

As argument, you get an object with the following properties:

- `defaultProps`: Only the default props, taken from the [`defaultProps`](/docs/composition#defaultprops) prop or the Remotion Studio Data sidebar.

- `props`: The [resolved props](/docs/props-resolution), taking input props into account.

- `abortSignal`: An [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) which you can use to abort network requests if [the default props have been changed](/docs/data-fetching#aborting-stale-requests) in the meanwhile.

- `compositionId` (*available from v4.0.98*): The ID of the current composition

- `isRendering` (*available from v4.0.342*): A boolean indicating whether the function is being called during rendering (`true`) or in other contexts like the Studio (`false`)

The function must return an pure JSON-serializable object, which can contain the following properties:

- `props`: The [final props](/docs/props-resolution) the component receives. It must have the [same shape](/docs/data-fetching#usage) as the `props` received by this function. The props must be a plain object and must not contain any non-JSON-serializable values, except `Date`, `Map`, `Set` and [`staticFile()`](/docs/staticfile). Optional.

- `durationInFrames`: The duration of the composition in frames. Optional.

- `width`: The width of the composition in pixels. Optional.

- `height`: The height of the composition in pixels. Optional.

- `fps`: The frames per second of the composition. Optional.

- `defaultCodec`: The default codec to use for the composition. Optional.

- `defaultOutName`: The default output name when rendering (without file extension). Optional. [v4.0.268](https://github.com/remotion-dev/remotion/releases/v4.0.268)

- `defaultVideoImageFormat`: The default video image format (`'png'`, `'jpeg'`, or `'none'`). Optional. [v4.0.316](https://github.com/remotion-dev/remotion/releases/v4.0.316)

- `defaultPixelFormat`: The default pixel format (`'yuv420p'`, `'yuva420p'`, `'yuv422p'`, `'yuv444p'`, `'yuv420p10le'`, `'yuv422p10le'`, `'yuv444p10le'`, or `'yuva444p10le'`). Optional. [v4.0.316](https://github.com/remotion-dev/remotion/releases/v4.0.316)

- `defaultProResProfile`: The default ProRes profile (`'4444-xq'`, `'4444'`, `'hq'`, `'standard'`, `'light'`, or `'proxy'`). Optional. [v4.0.367](https://github.com/remotion-dev/remotion/releases/v4.0.367)

If you return a field, it will take precendence over the props directly passed to the composition. The defaultCodec returned will have a higher priority than the config file, but less priority than explicitly passing the option to renderMedia() i.e. the composition will be rendered with this codec if nothing with higher priority was specified.

The function may be `async`.

The function must resolve within the [timeout](/docs/delay-render#timeout).

The function will get executed every time the props in the [Remotion Studio](/docs/visual-editing) changes.

## Compatibility[​](#compatibility)

|  Browsers Servers Environments
|  
Chrome 
Firefox 
Safari 
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
 
 
 
 

## See also[​](#see-also)

- [`<Composition>`](/docs/composition)

- [Data fetching](/docs/data-fetching)

- [Dynamic metadata](/docs/dynamic-metadata)
](/docs/dynamic-metadata)](/docs/dynamic-metadata)
](/docs/dynamic-metadata)
- ](/docs/dynamic-metadata)
- ](/docs/dynamic-metadata)