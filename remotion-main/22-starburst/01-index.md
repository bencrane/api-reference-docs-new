---
title: "<Starburst>"
url: "https://www.remotion.dev/docs/starburst/starburst"
path: "/docs/starburst/starburst"
---

"---\nimage: /generated/articles-docs-starburst-starburst.png\nid: starburst-component\nslug: /starburst/starburst\ntitle: '<Starburst>'\ncrumb: '@remotion/starburst'\n---\n\n# &lt;Starburst><AvailableFrom v=\"4.0.435\" />\n\nRenders a static WebGL-based retro starburst ray pattern.  \nIs a [`<Sequence>`](/docs/sequence) component under the hood and accepts its props.\n\n<Demo type=\"starburst\" />\n\n## Example\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {Starburst} from '@remotion/starburst';\nimport {AbsoluteFill} from 'remotion';\n\nconst MyVideo = () => {\n  return (\n    <AbsoluteFill style={{backgroundColor: 'black'}}>\n      <Starburst\n        durationInFrames={60}\n        rays={16}\n        colors={['#ffdd00', '#ff8800', '#ff4400']}\n        rotation={15}\n        width={1080}\n        height={1080}\n      />\n    </AbsoluteFill>\n  );\n};\n```\n\n## API\n\nApart from the props listed below, all props from [`<Sequence>`](/docs/sequence) except `children` and `layout` are accepted.\n\n### `rays`\n\nThe number of rays in the starburst pattern. Must be between `2` and `100`.\n\n### `colors`\n\nAn array of hex color strings for the rays. Colors are assigned to rays cyclically. Must contain at least 2 colors.\n\n```tsx\n<Starburst rays={12} colors={['#ff0066', '#6600ff', '#00ccff']} />\n```\n\n### `rotation?`\n\nRotates the starburst pattern in degrees (`0`-`360`). Default: `0`.\n\n### `smoothness?`\n\nControls the softness of the ray edges. `0` gives hard edges, `1` gives very soft edges. Default: `0`.\n\n### `vignette?`\n\nControls the radial transparency falloff from the center. `1` (default) means no vignette — the starburst is fully opaque. `0` makes the entire canvas transparent. Values in between create a circular fade from opaque at the center to transparent at the edges.\n\n### `originOffsetX?`\n\nShifts the origin of the starburst pattern horizontally. `-1` moves the origin to the left edge, `1` to the right edge. Default: `0` (centered).\n\n### `originOffsetY?`\n\nShifts the origin of the starburst pattern vertically. `-1` moves the origin to the top edge, `1` to the bottom edge. Default: `0` (centered).\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/starburst/src/Starburst.tsx)\n- [`<Sequence>`](/docs/sequence)\n"

Renders a static WebGL-based retro starburst ray pattern.

Is a [`<Sequence>`](/docs/sequence) component under the hood and accepts its props.

rays
`12`
rotation
`0`
smoothness
`0`
vignette
`1`
originOffsetX
`0`
originOffsetY
`0`

## Example[​](#example)

```

MyComp.tsximport {Starburst} from '@remotion/starburst';
import {AbsoluteFill} from 'remotion';

const MyVideo = () => {
  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      <Starburst
        durationInFrames={60}
        rays={16}
        colors={['#ffdd00', '#ff8800', '#ff4400']}
        rotation={15}
        width={1080}
        height={1080}
      />
    </AbsoluteFill>
  );
};Copy
```

## API[​](#api)

Apart from the props listed below, all props from [`<Sequence>`](/docs/sequence) except `children` and `layout` are accepted.

### `rays`[​](#rays)

The number of rays in the starburst pattern. Must be between `2` and `100`.

### `colors`[​](#colors)

An array of hex color strings for the rays. Colors are assigned to rays cyclically. Must contain at least 2 colors.

```
<Starburst rays={12} colors={['#ff0066', '#6600ff', '#00ccff']} />Copy
```

### `rotation?`[​](#rotation)

Rotates the starburst pattern in degrees (`0`-`360`). Default: `0`.

### `smoothness?`[​](#smoothness)

Controls the softness of the ray edges. `0` gives hard edges, `1` gives very soft edges. Default: `0`.

### `vignette?`[​](#vignette)

Controls the radial transparency falloff from the center. `1` (default) means no vignette — the starburst is fully opaque. `0` makes the entire canvas transparent. Values in between create a circular fade from opaque at the center to transparent at the edges.

### `originOffsetX?`[​](#originoffsetx)

Shifts the origin of the starburst pattern horizontally. `-1` moves the origin to the left edge, `1` to the right edge. Default: `0` (centered).

### `originOffsetY?`[​](#originoffsety)

Shifts the origin of the starburst pattern vertically. `-1` moves the origin to the top edge, `1` to the bottom edge. Default: `0` (centered).

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

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/starburst/src/Starburst.tsx)

- [`<Sequence>`](/docs/sequence)
](/docs/sequence)](/docs/sequence)
](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)