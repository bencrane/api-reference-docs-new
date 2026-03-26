---
title: "useVideoConfig()"
url: "https://www.remotion.dev/docs/use-video-config"
path: "/docs/use-video-config"
---

"---\nimage: /generated/articles-docs-use-video-config.png\ntitle: useVideoConfig()\nid: use-video-config\ncrumb: 'API'\n---\n\nWith this hook, you can retrieve some info about the composition you are in.\n\n## Example\n\n```tsx twoslash\nimport React from 'react';\nimport {useVideoConfig} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const {width, height, fps, durationInFrames} = useVideoConfig();\n  console.log(width); // 1920\n  console.log(height); // 1080\n  console.log(fps); // 30;\n  console.log(durationInFrames); // 300\n\n  return <div>Hello World!</div>;\n};\n```\n\n## Return value\n\nA object with the following properties:\n\n### `width`\n\nThe width of the composition in pixels, or the `width` of a [`<Sequence>`](/docs/sequence) if the component that calls `useVideoConfig()` is a child of a [`<Sequence>`](/docs/sequence) that defines a width.\n\n### `height`\n\nThe height of the composition in pixels, or the `height` of a [`<Sequence>`](/docs/sequence) if the component that calls `useVideoConfig()` is a child of a [`<Sequence>`](/docs/sequence) that defines a height.\n\n### `fps`\n\nThe frame rate of the composition, in frames per seconds.\n\n### `durationInFrames`\n\nIf inside a [`<Sequence>`](/docs/sequence), the duration of the sequence in frames.  \nIf not inside a [`<Sequence>`](/docs/sequence), the duration of the composition in frames.\n\n### `id`\n\nThe ID of the composition. This is the same as the `id` prop of the [`<Composition>`](/docs/composition) component.\n\n### `defaultProps`\n\nThe object that you have defined as the `defaultProps` in your composition.\n\n### `props`<AvailableFrom v=\"4.0.0\" />\n\nThe props that were passed to the composition, after [all transformations](/docs/props-resolution).\n\n### `defaultCodec`<AvailableFrom v=\"4.0.54\" />\n\nThe default codec that is used for rendering this composition. Use [`calculateMetadata()`](/docs/calculate-metadata) to modify it.\n\nThese properties are controlled by passing them as props to [`<Composition>`](/docs/composition). Read the page about [the fundamentals](/docs/the-fundamentals) to read how to setup a Remotion project.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-video-config.ts)\n- [`useCurrentFrame()`](/docs/use-current-frame)\n"

With this hook, you can retrieve some info about the composition you are in.

## Example[​](#example)

```
import React from 'react';
import {useVideoConfig} from 'remotion';

export const MyComp: React.FC = () => {
  const {width, height, fps, durationInFrames} = useVideoConfig();
  console.log(width); // 1920
  console.log(height); // 1080
  console.log(fps); // 30;
  console.log(durationInFrames); // 300

  return <div>Hello World!</div>;
};Copy
```

## Return value[​](#return-value)

A object with the following properties:

### `width`[​](#width)

The width of the composition in pixels, or the `width` of a [`<Sequence>`](/docs/sequence) if the component that calls `useVideoConfig()` is a child of a [`<Sequence>`](/docs/sequence) that defines a width.

### `height`[​](#height)

The height of the composition in pixels, or the `height` of a [`<Sequence>`](/docs/sequence) if the component that calls `useVideoConfig()` is a child of a [`<Sequence>`](/docs/sequence) that defines a height.

### `fps`[​](#fps)

The frame rate of the composition, in frames per seconds.

### `durationInFrames`[​](#durationinframes)

If inside a [`<Sequence>`](/docs/sequence), the duration of the sequence in frames.

If not inside a [`<Sequence>`](/docs/sequence), the duration of the composition in frames.

### `id`[​](#id)

The ID of the composition. This is the same as the `id` prop of the [`<Composition>`](/docs/composition) component.

### `defaultProps`[​](#defaultprops)

The object that you have defined as the `defaultProps` in your composition.

### `props`[v4.0.0](https://github.com/remotion-dev/remotion/releases/v4.0.0)[​](#props)

The props that were passed to the composition, after [all transformations](/docs/props-resolution).

### `defaultCodec`[v4.0.54](https://github.com/remotion-dev/remotion/releases/v4.0.54)[​](#defaultcodec)

The default codec that is used for rendering this composition. Use [`calculateMetadata()`](/docs/calculate-metadata) to modify it.

These properties are controlled by passing them as props to [`<Composition>`](/docs/composition). Read the page about [the fundamentals](/docs/the-fundamentals) to read how to setup a Remotion project.

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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-video-config.ts)

- [`useCurrentFrame()`](/docs/use-current-frame)
](/docs/use-current-frame)](/docs/use-current-frame)
](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)
- ](/docs/use-current-frame)