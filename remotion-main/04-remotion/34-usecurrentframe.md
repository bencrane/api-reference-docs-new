---
title: "useCurrentFrame()"
url: "https://www.remotion.dev/docs/use-current-frame"
path: "/docs/use-current-frame"
---

"---\nimage: /generated/articles-docs-use-current-frame.png\ntitle: useCurrentFrame()\nid: use-current-frame\ncrumb: 'API'\n---\n\nWith this hook, you can retrieve the current frame of the video. Frames are 0-indexed, meaning the first frame is `0`, the last frame is the duration of the composition in frames minus one. To learn more about how Remotion works with time, read the page about [the fundamentals](/docs/the-fundamentals).\n\nIf the component you are writing is wrapped in a [`<Sequence>`](/docs/sequence), `useCurrentFrame` will return the frame relative to when the Sequence starts.\n\nSay the timeline marker is positioned at frame 25. In the example below, `useCurrentFrame()` will return `25`, except within the Subtitle component, where it will return `15` because it is within a sequence that starts at frame 10.\n\n```tsx twoslash\nimport {Sequence, useCurrentFrame} from 'remotion';\n\nconst Title = () => {\n  const frame = useCurrentFrame(); // 25\n  return <div>{frame}</div>;\n};\n\nconst Subtitle = () => {\n  const frame = useCurrentFrame(); // 15\n  return <div>{frame}</div>;\n};\n\nconst MyVideo = () => {\n  const frame = useCurrentFrame(); // 25\n\n  return (\n    <div>\n      <Title />\n      <Sequence from={10}>\n        <Subtitle />\n      </Sequence>\n    </div>\n  );\n};\n```\n\nUsing `<Sequence />`'s, you can compose multiple elements together and time-shift them independently from each other without changing their animation.\n\n### Getting the absolute frame of the timeline\n\nIn rare circumstances, you want access to the absolute frame of the timeline inside a sequence, use `useCurrentFrame()` at the top-level component and then pass it down as a prop to the children of the `<Sequence />`.\n\n```tsx twoslash\nimport {Sequence, useCurrentFrame} from 'remotion';\n\n// ---cut---\n\nconst Subtitle: React.FC<{absoluteFrame: number}> = ({absoluteFrame}) => {\n  console.log(useCurrentFrame()); // 15\n  console.log(absoluteFrame); // 25\n\n  return null;\n};\n\nconst MyVideo = () => {\n  const frame = useCurrentFrame(); // 25\n\n  return (\n    <Sequence from={10}>\n      <Subtitle absoluteFrame={frame} />\n    </Sequence>\n  );\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-current-frame.ts)\n- [useVideoConfig()](/docs/use-video-config)\n- [`<Sequence />`](/docs/sequence)\n"

With this hook, you can retrieve the current frame of the video. Frames are 0-indexed, meaning the first frame is `0`, the last frame is the duration of the composition in frames minus one. To learn more about how Remotion works with time, read the page about [the fundamentals](/docs/the-fundamentals).

If the component you are writing is wrapped in a [`<Sequence>`](/docs/sequence), `useCurrentFrame` will return the frame relative to when the Sequence starts.

Say the timeline marker is positioned at frame 25. In the example below, `useCurrentFrame()` will return `25`, except within the Subtitle component, where it will return `15` because it is within a sequence that starts at frame 10.

```
import {Sequence, useCurrentFrame} from 'remotion';

const Title = () => {
  const frame = useCurrentFrame(); // 25
  return <div>{frame}</div>;
};

const Subtitle = () => {
  const frame = useCurrentFrame(); // 15
  return <div>{frame}</div>;
};

const MyVideo = () => {
  const frame = useCurrentFrame(); // 25

  return (
    <div>
      <Title />
      <Sequence from={10}>
        <Subtitle />
      </Sequence>
    </div>
  );
};Copy
```

Using `<Sequence />`'s, you can compose multiple elements together and time-shift them independently from each other without changing their animation.

### Getting the absolute frame of the timeline[​](#getting-the-absolute-frame-of-the-timeline)

In rare circumstances, you want access to the absolute frame of the timeline inside a sequence, use `useCurrentFrame()` at the top-level component and then pass it down as a prop to the children of the `<Sequence />`.

```

const Subtitle: React.FC<{absoluteFrame: number}> = ({absoluteFrame}) => {
  console.log(useCurrentFrame()); // 15
  console.log(absoluteFrame); // 25

  return null;
};

const MyVideo = () => {
  const frame = useCurrentFrame(); // 25

  return (
    <Sequence from={10}>
      <Subtitle absoluteFrame={frame} />
    </Sequence>
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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/use-current-frame.ts)

- [useVideoConfig()](/docs/use-video-config)

- [`<Sequence />`](/docs/sequence)
](/docs/sequence)](/docs/sequence)
](/docs/sequence)
- ](/docs/sequence)
- ](/docs/sequence)