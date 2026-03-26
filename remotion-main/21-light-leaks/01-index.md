---
title: "<LightLeak>"
url: "https://www.remotion.dev/docs/light-leaks/light-leak"
path: "/docs/light-leaks/light-leak"
---

"---\nimage: /generated/articles-docs-light-leaks-light-leak.png\ntitle: '<LightLeak>'\ncrumb: '@remotion/light-leaks'\n---\n\n# &lt;LightLeak&gt;<AvailableFrom v=\"4.0.415\" />\n\nRenders a WebGL-based light leak effect.  \nThe effect reveals during the first half of the duration and retracts during the second half.  \nIs a [`<Sequence>`](/docs/sequence) component under the hood and accepts it's props.\n\n## Example\n\n<Demo type=\"light-leak\" />\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {LightLeak} from '@remotion/light-leaks';\nimport {AbsoluteFill} from 'remotion';\n\nconst MyVideo = () => {\n  return (\n    <AbsoluteFill style={{backgroundColor: 'black'}}>\n      <LightLeak durationInFrames={60} seed={3} hueShift={30} />\n    </AbsoluteFill>\n  );\n};\n```\n\n## API\n\nApart from the props listed below, all props from [`<Sequence>`](/docs/sequence) except `children` and `layout` are accepted.\n\n### `durationInFrames?`\n\nThe duration of the light leak effect in frames. The effect reveals during the first half and retracts during the second half.  \nDuring the midpoint, the light leak will cover most of the canvas.\n\nIf not specified, defaults to the duration of the composition or sequence, reading from [`useVideoConfig()`](/docs/use-video-config).\n\n### `seed?`\n\nDetermines the shape of the light leak pattern. Different seeds produce different patterns. Default: `0`.\n\n### `hueShift?`\n\nRotates the hue of the light leak in degrees (`0`-`360`).\n\n- `0` (default) yellow-to-orange\n- `120` shifts toward green\n- `240` shifts toward blue\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/light-leaks/src/LightLeak.tsx)\n- [`<Sequence>`](/docs/sequence)\n"

Renders a WebGL-based light leak effect.

The effect reveals during the first half of the duration and retracts during the second half.

Is a [`<Sequence>`](/docs/sequence) component under the hood and accepts it's props.

## Example[​](#example)

seed
`0`
hueShift
`0`

```

MyComp.tsximport {LightLeak} from '@remotion/light-leaks';
import {AbsoluteFill} from 'remotion';

const MyVideo = () => {
  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      <LightLeak durationInFrames={60} seed={3} hueShift={30} />
    </AbsoluteFill>
  );
};Copy
```

## API[​](#api)

Apart from the props listed below, all props from [`<Sequence>`](/docs/sequence) except `children` and `layout` are accepted.

### `durationInFrames?`[​](#durationinframes)

The duration of the light leak effect in frames. The effect reveals during the first half and retracts during the second half.

During the midpoint, the light leak will cover most of the canvas.

If not specified, defaults to the duration of the composition or sequence, reading from [`useVideoConfig()`](/docs/use-video-config).

### `seed?`[​](#seed)

Determines the shape of the light leak pattern. Different seeds produce different patterns. Default: `0`.

### `hueShift?`[​](#hueshift)

Rotates the hue of the light leak in degrees (`0`-`360`).

- `0` (default) yellow-to-orange

- `120` shifts toward green

- `240` shifts toward blue

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

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/light-leaks/src/LightLeak.tsx)

- [`<Sequence>`](/docs/sequence)
](/docs/sequence)](/docs/sequence)
](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)