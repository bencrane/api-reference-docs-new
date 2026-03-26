---
title: "<Series>"
url: "https://www.remotion.dev/docs/series"
path: "/docs/series"
---

"---\nimage: /generated/articles-docs-series.png\nid: series\ntitle: <Series>\ncrumb: 'API'\n---\n\n<AvailableFrom v=\"2.3.1\" />\n\nimport {SeriesExample} from '../components/SeriesExamples/SeriesExample';\n\nUsing this component, you can easily stitch together scenes that should play sequentially after another.\n\n## Example\n\n### Code\n\n```twoslash include example\nconst Square: React.FC<{color: string}> = () => <div></div>\n// - Square\n```\n\n```tsx twoslash title=\"src/Example.tsx\"\n// @include: example-Square\n// ---cut---\nimport {Series} from 'remotion';\n\nexport const Example: React.FC = () => {\n  return (\n    <Series>\n      <Series.Sequence durationInFrames={40}>\n        <Square color={'#3498db'} />\n      </Series.Sequence>\n      <Series.Sequence durationInFrames={20}>\n        <Square color={'#5ff332'} />\n      </Series.Sequence>\n      <Series.Sequence durationInFrames={70}>\n        <Square color={'#fdc321'} />\n      </Series.Sequence>\n    </Series>\n  );\n};\n```\n\n### Result\n\n<SeriesExample type=\"base\" />\n\n## API\n\nThe `<Series />` component takes no props. It may only contain a list of `<Series.Sequence />` instances.  \nA `<Series.Sequence />` component accepts the following props:\n\n### `durationInFrames?`\n\nFor how many frames the sequence should be displayed. Children are unmounted if they are not within the time range of display.\n\nOnly the last `<Series.Sequence />` instance is allowed to have `Infinity` as a duration, all previous one must have a positive integer.\n\n### `offset?`\n\nPass a positive number to delay the beginning of the sequence. Pass a negative number to start the sequence earlier, and to overlay the sequence with the one that comes before.\n\nThe offset does not apply to sequences that come before, but the sequences that come after it will also be shifted.\n\n**Example 1**: Pass `10` to delay the sequence by 10 frames and create a blank space of 10 frames before it.  \n**Example 2**: Pass `-10` to start the sequence earlier and overlay the sequence on top of the previous one for 10 frames.\n\n### `layout?`\n\nEither `\"absolute-fill\"` _(default)_ or `\"none\"` By default, your sequences will be absolutely positioned, so they will overlay each other. If you would like to opt out of it and handle layouting yourself, pass `layout=\"none\"`.\n\n### `style?`<AvailableFrom v=\"3.3.4\"/>\n\nCSS styles to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.\n\n### `className?`<AvailableFrom v=\"3.3.45\"/>\n\nA class name to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.\n\n### `premountFor?`<AvailableFrom v=\"4.0.140\"/>\n\n[Premount](/docs/player/premounting) the sequence for a set number of frames.\n\n### `ref?`<AvailableFrom v=\"3.3.4\" />\n\nYou can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to a `<Series.Sequence>`. If you use TypeScript, you need to type it with `HTMLDivElement`:\n\n```tsx twoslash title=\"src/Example.tsx\"\nconst Square: React.FC<{\n  color: string;\n}> = () => null;\n// ---cut---\nimport React, {useRef} from 'react';\nimport {Series} from 'remotion';\n\nexport const Example: React.FC = () => {\n  const first = useRef<HTMLDivElement>(null);\n  const second = useRef<HTMLDivElement>(null);\n\n  return (\n    <Series>\n      <Series.Sequence durationInFrames={40} ref={first}>\n        <Square color={'#3498db'} />\n      </Series.Sequence>\n      <Series.Sequence durationInFrames={20} ref={second}>\n        <Square color={'#5ff332'} />\n      </Series.Sequence>\n      <Series.Sequence durationInFrames={70}>\n        <Square color={'#fdc321'} />\n      </Series.Sequence>\n    </Series>\n  );\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/series/index.tsx)\n- [`<Sequence />`](/docs/sequence)\n"
[v2.3.1](https://github.com/remotion-dev/remotion/releases/v2.3.1)

Using this component, you can easily stitch together scenes that should play sequentially after another.

## Example[​](#example)

### Code[​](#code)

```

src/Example.tsximport {Series} from 'remotion';

export const Example: React.FC = () => {
  return (
    <Series>
      <Series.Sequence durationInFrames={40}>
        <Square color={'#3498db'} />
      </Series.Sequence>
      <Series.Sequence durationInFrames={20}>
        <Square color={'#5ff332'} />
      </Series.Sequence>
      <Series.Sequence durationInFrames={70}>
        <Square color={'#fdc321'} />
      </Series.Sequence>
    </Series>
  );
};Copy
```

### Result[​](#result)

## API[​](#api)

The `<Series />` component takes no props. It may only contain a list of `<Series.Sequence />` instances.

A `<Series.Sequence />` component accepts the following props:

### `durationInFrames?`[​](#durationinframes)

For how many frames the sequence should be displayed. Children are unmounted if they are not within the time range of display.

Only the last `<Series.Sequence />` instance is allowed to have `Infinity` as a duration, all previous one must have a positive integer.

### `offset?`[​](#offset)

Pass a positive number to delay the beginning of the sequence. Pass a negative number to start the sequence earlier, and to overlay the sequence with the one that comes before.

The offset does not apply to sequences that come before, but the sequences that come after it will also be shifted.

**Example 1**: Pass `10` to delay the sequence by 10 frames and create a blank space of 10 frames before it.

**Example 2**: Pass `-10` to start the sequence earlier and overlay the sequence on top of the previous one for 10 frames.

### `layout?`[​](#layout)

Either `"absolute-fill"` *(default)* or `"none"` By default, your sequences will be absolutely positioned, so they will overlay each other. If you would like to opt out of it and handle layouting yourself, pass `layout="none"`.

### `style?`[v3.3.4](https://github.com/remotion-dev/remotion/releases/v3.3.4)[​](#style)

CSS styles to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.

### `className?`[v3.3.45](https://github.com/remotion-dev/remotion/releases/v3.3.45)[​](#classname)

A class name to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.

### `premountFor?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#premountfor)

[Premount](/docs/player/premounting) the sequence for a set number of frames.

### `ref?`[v3.3.4](https://github.com/remotion-dev/remotion/releases/v3.3.4)[​](#ref)

You can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to a `<Series.Sequence>`. If you use TypeScript, you need to type it with `HTMLDivElement`:

```

src/Example.tsximport React, {useRef} from 'react';
import {Series} from 'remotion';

export const Example: React.FC = () => {
  const first = useRef<HTMLDivElement>(null);
  const second = useRef<HTMLDivElement>(null);

  return (
    <Series>
      <Series.Sequence durationInFrames={40} ref={first}>
        <Square color={'#3498db'} />
      </Series.Sequence>
      <Series.Sequence durationInFrames={20} ref={second}>
        <Square color={'#5ff332'} />
      </Series.Sequence>
      <Series.Sequence durationInFrames={70}>
        <Square color={'#fdc321'} />
      </Series.Sequence>
    </Series>
  );
};Copy
```

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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/series/index.tsx)

- [`<Sequence />`](/docs/sequence)
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
- ](/docs/sequence)
- ](/docs/sequence)