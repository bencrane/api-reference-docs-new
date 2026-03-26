---
title: "<Sequence>"
url: "https://www.remotion.dev/docs/sequence"
path: "/docs/sequence"
---

"---\nimage: /generated/articles-docs-sequence.png\nid: sequence\ntitle: <Sequence>\ncrumb: 'API'\n---\n\nimport {SequenceForwardExample} from '../components/SequenceExamples/SequenceForward';\n\n```twoslash include example\nconst BlueSquare: React.FC = () => <div></div>\n// - BlueSquare\n```\n\nBy using a sequence, you can time-shift the display of your components or parts of your animation in the video.\n\n```tsx twoslash title=\"MyTrailer.tsx\"\nimport {Sequence} from 'remotion';\n\nexport const Intro = () => <></>;\nexport const Clip = () => <></>;\nexport const Outro = () => <></>;\n\n// ---cut---\n\nconst MyTrailer = () => {\n  return (\n    <>\n      <Sequence durationInFrames={30}>\n        <Intro />\n      </Sequence>\n      <Sequence from={30} durationInFrames={30}>\n        <Clip />\n      </Sequence>\n      <Sequence from={60}>\n        <Outro />\n      </Sequence>\n    </>\n  );\n};\n```\n\n- `<Intro>` will show from frame 0–29.\n- `<Clip>` will show from frame 30 until frame 59.\n- `<Outro>` will show from frame 60 until the end of the composition.\n\nAll children of a `<Sequence>` that call [`useCurrentFrame()`](/docs/use-current-frame) will receive a value that is shifted by [`from`](#from).\n\n```tsx twoslash title=\"MyTrailer.tsx\"\nimport {Sequence, useCurrentFrame} from 'remotion';\n\nconst Intro = () => <div>{useCurrentFrame()}</div>;\n\nconst MyTrailer = () => {\n  return (\n    <>\n      <Intro />\n      <Sequence from={30}>\n        <Intro />\n      </Sequence>\n    </>\n  );\n};\n```\n\n- At frame `0`, this would render `<div>0</div>`.\n- At frame `30`, this would render `<div>30</div><div>0</div>`.\n\nUsing the [`durationInFrames`](#durationinframes) prop, you can define for how long the children of a `<Sequence>` should be mounted.\n\nBy default, the children of a `<Sequence>` are wrapped in an [`<AbsoluteFill>`](/docs/absolute-fill) component. If you don't want this behavior, add [`layout=\"none\"`](#layout) as a prop.\n\n## Cascading\n\nYou can nest sequences within each other and they will cascade.  \nFor example, a sequence that starts at frame 60 which is inside a sequence that starts at frame 30 will have it's children start at frame 90.\n\n## Examples\n\nAll the examples below are based on the following animation of a blue square:\n\n<SequenceForwardExample type=\"base\" />\n\n<br />\n\n```tsx twoslash title=\"MyVideo.tsx\"\n// @include: example-BlueSquare\n// ---cut---\nconst MyVideo = () => {\n  return <BlueSquare />;\n};\n```\n\n### Delay\n\nIf you would like to delay the content by say 30 frames, you can wrap it in <br/> `<Sequence from={30}>`.\n\n<SequenceForwardExample type=\"delay\" />\n<br />\n\n```tsx twoslash title=\"delay.tsx\"\n// @include: example-BlueSquare\nimport {Sequence} from 'remotion';\n// ---cut---\nconst MyVideo = () => {\n  return (\n    <Sequence from={30}>\n      <BlueSquare />\n    </Sequence>\n  );\n};\n```\n\n### Trim end\n\nWrap your component in a `<Sequence>` with a finite `durationInFrames` prop to make it unmount after the duration has passed.\n\n<SequenceForwardExample type=\"clip\" />\n<br />\n\n```tsx twoslash title=\"trim-end.tsx\"\n// @include: example-BlueSquare\nimport {Sequence} from 'remotion';\n// ---cut---\nconst ClipExample: React.FC = () => {\n  return (\n    <Sequence durationInFrames={45}>\n      <BlueSquare />\n    </Sequence>\n  );\n};\n```\n\n### Trim start\n\nWrap the square in `<Sequence>` with a negative `from` value to trim the beginning of the content.  \nBy shifting the time backwards, the animation has already progressed by 15 frames when the content appears.\n\n<SequenceForwardExample type=\"trim-start\" />\n<br />\n\n```tsx title=\"trim-start.tsx\"\nconst TrimStartExample: React.FC = () => {\n  return (\n    <Sequence from={-15}>\n      <BlueSquare />\n    </Sequence>\n  );\n};\n```\n\n### Trim and delay\n\nWrap the content in two `<Sequence>`'s.  \nTo the inner one, pass a negative start value `from={-15}` to trim away the first 15 frames of the content.  \nTo the outer one we pass a positive value `from={30}` to then shift it forwards by 30 frames.\n\n<SequenceForwardExample type=\"trim-and-delay\" />\n<br />\n\n```tsx twoslash title=\"trim-and-delay.tsx\"\n// @include: example-BlueSquare\nimport {Sequence} from 'remotion';\n// ---cut---\nconst TrimAndDelayExample: React.FC = () => {\n  return (\n    <Sequence from={30}>\n      <Sequence from={-15}>\n        <BlueSquare />\n      </Sequence>\n    </Sequence>\n  );\n};\n```\n\n## Play Sequences sequentially\n\nSee the [`<Series />`](/docs/series) helper component, which helps you calculate markup that makes sequences play after each other.\n\n## Props\n\nThe Sequence component is a high order component and accepts, besides children, the following props:\n\n### `from?`\n\n(optional from v3.2.36, _required_ in previous versions)\n\nAt which frame it's children should assume the video starts. When the sequence is at `frame`, it's children are at frame `0`.\nFrom v3.2.36 onwards, this prop will be optional; by default, it will be 0.\n\n### `durationInFrames?`\n\nFor how many frames the sequence should be displayed. Children are unmounted if they are not within the time range of display. By default it will be `Infinity` to avoid limit the duration of the sequence.\n\n### `height?`<AvailableFrom v=\"4.0.80\"/>\n\nGives the sequence a specific `style={{height: height}}` style and overrides `height` that is returned by the [`useVideoConfig()`](/docs/use-video-config) hook in child components. Useful for including a component that was designed for a specific height.\n\n### `width?`<AvailableFrom v=\"4.0.80\"/>\n\nGives the sequence a specific `style={{width: width}}` style and overrides `width` that is returned by the [`useVideoConfig()`](/docs/use-video-config) hook in child components. Useful for including a component that was designed for a specific width.\n\n### `name?`\n\nYou can give your sequence a name and it will be shown as the label of the sequence in the timeline of the Remotion Studio. This property is purely for helping you keep track of sequences in the timeline.\n\n### `layout?`\n\nEither `\"absolute-fill\"` _(default)_ or `\"none\"`. By default, your sequences will be absolutely positioned, so they will overlay each other. If you would like to opt out of it and handle layouting yourself, pass `layout=\"none\"`. Available since v1.4.\n\n### `style?`<AvailableFrom v=\"3.0.27\"/>\n\nCSS styles to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.\n\n### `className?`<AvailableFrom v=\"3.3.45\"/>\n\nA class name to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.\n\n### `premountFor?`<AvailableFrom v=\"4.0.140\" />\n\n[Premount](/docs/player/premounting) the sequence for a set number of frames.\nFrom [v5.0](/docs/5-0-migration), the default value changes from `0` to `fps` (1 second).\n\n### `postmountFor?`<AvailableFrom v=\"4.0.340\" />\n\nSame as `premountFor`, but for after the sequence has ended.  \nUse this only if you expect the user to frequently seek backwards in the timeline and you want to avoid flickers for this behavior.\n\n### `styleWhilePremounted?`<AvailableFrom v=\"4.0.252\" />\n\nCSS styles to be applied to the container while the sequence is premounted.  \nThe `style` is still applied, but `styleWhilePremounted` can override properties.\n\n### `showInTimeline?`<AvailableFrom v=\"4.0.110\" />\n\nIf set to `false`, the track will not be shown in the Studio's timeline.  \nChild `<Sequence>`'s will show by default, unless `showInTimeline` is also set to false.  \nThis behavior is stable as of v4.0.110, previously the behavior was different, but this prop not documented.\n\n## Adding a ref\n\nYou can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to an `<Sequence>` from version `v3.2.13` on. If you use TypeScript, you need to type it with `HTMLDivElement`:\n\n```tsx twoslash\nimport {useRef} from 'react';\nimport {Sequence} from 'remotion';\n\nconst content = <div>Hello, World</div>;\n// ---cut---\nconst MyComp = () => {\n  const ref = useRef<HTMLDivElement>(null);\n  return (\n    <Sequence from={10} ref={ref}>\n      {content}\n    </Sequence>\n  );\n};\n```\n\n## Note for `@remotion/three`\n\nA `<Sequence>` by default will return a `<div>` component which is not allowed inside a [`<ThreeCanvas>`](/docs/three-canvas).  \nAvoid an error by passing `layout=\"none\"` to `<Sequence>`. Example: `<Sequence layout=\"none\">`.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Sequence.tsx)\n- [Reuse components using Sequences](/docs/reusability)\n- [`<Composition />`](/docs/composition)\n- [`<Series />`](/docs/series)\n"

By using a sequence, you can time-shift the display of your components or parts of your animation in the video.

```

MyTrailer.tsx
const MyTrailer = () => {
  return (
    <>
      <Sequence durationInFrames={30}>
        <Intro />
      </Sequence>
      <Sequence from={30} durationInFrames={30}>
        <Clip />
      </Sequence>
      <Sequence from={60}>
        <Outro />
      </Sequence>
    </>
  );
};Copy
```

- `<Intro>` will show from frame 0–29.

- `<Clip>` will show from frame 30 until frame 59.

- `<Outro>` will show from frame 60 until the end of the composition.

All children of a `<Sequence>` that call [`useCurrentFrame()`](/docs/use-current-frame) will receive a value that is shifted by [`from`](#from).

```

MyTrailer.tsximport {Sequence, useCurrentFrame} from 'remotion';

const Intro = () => <div>{useCurrentFrame()}</div>;

const MyTrailer = () => {
  return (
    <>
      <Intro />
      <Sequence from={30}>
        <Intro />
      </Sequence>
    </>
  );
};Copy
```

- At frame `0`, this would render `<div>0</div>`.

- At frame `30`, this would render `<div>30</div><div>0</div>`.

Using the [`durationInFrames`](#durationinframes) prop, you can define for how long the children of a `<Sequence>` should be mounted.

By default, the children of a `<Sequence>` are wrapped in an [`<AbsoluteFill>`](/docs/absolute-fill) component. If you don't want this behavior, add [`layout="none"`](#layout) as a prop.

## Cascading[​](#cascading)

You can nest sequences within each other and they will cascade.

For example, a sequence that starts at frame 60 which is inside a sequence that starts at frame 30 will have it's children start at frame 90.

## Examples[​](#examples)

All the examples below are based on the following animation of a blue square:

```

MyVideo.tsxconst MyVideo = () => {
  return <BlueSquare />;
};Copy
```

### Delay[​](#delay)

If you would like to delay the content by say 30 frames, you can wrap it in 
 `<Sequence from={30}>`.

```

delay.tsxconst MyVideo = () => {
  return (
    <Sequence from={30}>
      <BlueSquare />
    </Sequence>
  );
};Copy
```

### Trim end[​](#trim-end)

Wrap your component in a `<Sequence>` with a finite `durationInFrames` prop to make it unmount after the duration has passed.

```

trim-end.tsxconst ClipExample: React.FC = () => {
  return (
    <Sequence durationInFrames={45}>
      <BlueSquare />
    </Sequence>
  );
};Copy
```

### Trim start[​](#trim-start)

Wrap the square in `<Sequence>` with a negative `from` value to trim the beginning of the content.

By shifting the time backwards, the animation has already progressed by 15 frames when the content appears.

```

trim-start.tsxconst TrimStartExample: React.FC = () => {
  return (
    <Sequence from={-15}>
      <BlueSquare />
    </Sequence>
  );
};Copy
```

### Trim and delay[​](#trim-and-delay)

Wrap the content in two `<Sequence>`'s.

To the inner one, pass a negative start value `from={-15}` to trim away the first 15 frames of the content.

To the outer one we pass a positive value `from={30}` to then shift it forwards by 30 frames.

```

trim-and-delay.tsxconst TrimAndDelayExample: React.FC = () => {
  return (
    <Sequence from={30}>
      <Sequence from={-15}>
        <BlueSquare />
      </Sequence>
    </Sequence>
  );
};Copy
```

## Play Sequences sequentially[​](#play-sequences-sequentially)

See the [`<Series />`](/docs/series) helper component, which helps you calculate markup that makes sequences play after each other.

## Props[​](#props)

The Sequence component is a high order component and accepts, besides children, the following props:

### `from?`[​](#from)

(optional from v3.2.36, *required* in previous versions)

At which frame it's children should assume the video starts. When the sequence is at `frame`, it's children are at frame `0`.
From v3.2.36 onwards, this prop will be optional; by default, it will be 0.

### `durationInFrames?`[​](#durationinframes)

For how many frames the sequence should be displayed. Children are unmounted if they are not within the time range of display. By default it will be `Infinity` to avoid limit the duration of the sequence.

### `height?`[v4.0.80](https://github.com/remotion-dev/remotion/releases/v4.0.80)[​](#height)

Gives the sequence a specific `style={{height: height}}` style and overrides `height` that is returned by the [`useVideoConfig()`](/docs/use-video-config) hook in child components. Useful for including a component that was designed for a specific height.

### `width?`[v4.0.80](https://github.com/remotion-dev/remotion/releases/v4.0.80)[​](#width)

Gives the sequence a specific `style={{width: width}}` style and overrides `width` that is returned by the [`useVideoConfig()`](/docs/use-video-config) hook in child components. Useful for including a component that was designed for a specific width.

### `name?`[​](#name)

You can give your sequence a name and it will be shown as the label of the sequence in the timeline of the Remotion Studio. This property is purely for helping you keep track of sequences in the timeline.

### `layout?`[​](#layout)

Either `"absolute-fill"` *(default)* or `"none"`. By default, your sequences will be absolutely positioned, so they will overlay each other. If you would like to opt out of it and handle layouting yourself, pass `layout="none"`. Available since v1.4.

### `style?`[v3.0.27](https://github.com/remotion-dev/remotion/releases/v3.0.27)[​](#style)

CSS styles to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.

### `className?`[v3.3.45](https://github.com/remotion-dev/remotion/releases/v3.3.45)[​](#classname)

A class name to be applied to the container. If `layout` is set to `none`, there is no container and setting this style is not allowed.

### `premountFor?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#premountfor)

[Premount](/docs/player/premounting) the sequence for a set number of frames.
From [v5.0](/docs/5-0-migration), the default value changes from `0` to `fps` (1 second).

### `postmountFor?`[v4.0.340](https://github.com/remotion-dev/remotion/releases/v4.0.340)[​](#postmountfor)

Same as `premountFor`, but for after the sequence has ended.

Use this only if you expect the user to frequently seek backwards in the timeline and you want to avoid flickers for this behavior.

### `styleWhilePremounted?`[v4.0.252](https://github.com/remotion-dev/remotion/releases/v4.0.252)[​](#stylewhilepremounted)

CSS styles to be applied to the container while the sequence is premounted.

The `style` is still applied, but `styleWhilePremounted` can override properties.

### `showInTimeline?`[v4.0.110](https://github.com/remotion-dev/remotion/releases/v4.0.110)[​](#showintimeline)

If set to `false`, the track will not be shown in the Studio's timeline.

Child `<Sequence>`'s will show by default, unless `showInTimeline` is also set to false.

This behavior is stable as of v4.0.110, previously the behavior was different, but this prop not documented.

## Adding a ref[​](#adding-a-ref)

You can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to an `<Sequence>` from version `v3.2.13` on. If you use TypeScript, you need to type it with `HTMLDivElement`:

```
const MyComp = () => {
  const ref = useRef<HTMLDivElement>(null);
  return (
    <Sequence from={10} ref={ref}>
      {content}
    </Sequence>
  );
};Copy
```

## Note for `@remotion/three`[​](#note-for-remotionthree)

A `<Sequence>` by default will return a `<div>` component which is not allowed inside a [`<ThreeCanvas>`](/docs/three-canvas).

Avoid an error by passing `layout="none"` to `<Sequence>`. Example: `<Sequence layout="none">`.

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

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Sequence.tsx)

- [Reuse components using Sequences](/docs/reusability)

- [`<Composition />`](/docs/composition)

- [`<Series />`](/docs/series)
](/docs/series)](/docs/series)
](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)