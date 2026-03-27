---
title: "play()"
url: "https://www.remotion.dev/docs/studio/play"
path: "/docs/studio/play"
---

"---\nimage: /generated/articles-docs-studio-play.png\ntitle: play()\ncrumb: '@remotion/studio'\n---\n\n# play()<AvailableFrom v=\"4.0.287\"/>\n\nStarts playback in the Remotion Studio.\n\nThe function accepts an optional event parameter which can be a `React.SyntheticEvent` or a [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent). This allows the function to be used directly as an event handler.\n\n## Examples\n\n```tsx twoslash title=\"Start playing on button click\"\nimport {play} from '@remotion/studio';\n\nconst PlayButton = () => {\n  // Call with the event parameter for better browser audio autoplay\n  return <button onClick={(e) => play(e)}>Play</button>;\n};\n```\n\n```tsx twoslash title=\"Start playing programmatically\"\nimport {play} from '@remotion/studio';\n\n// Call without event parameter\nplay();\n```\n\n## See also\n\n- [pause()](/docs/studio/pause)\n- [toggle()](/docs/studio/toggle)\n- [seek()](/docs/studio/seek)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/play.ts)\n"

Starts playback in the Remotion Studio.

The function accepts an optional event parameter which can be a `React.SyntheticEvent` or a [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent). This allows the function to be used directly as an event handler.

## Examples[​](#examples)

```

Start playing on button clickimport {play} from '@remotion/studio';

const PlayButton = () => {
  // Call with the event parameter for better browser audio autoplay
  return <button onClick={(e) => play(e)}>Play</button>;
};Copy
```

```

Start playing programmaticallyimport {play} from '@remotion/studio';

// Call without event parameter
play();Copy
```

## See also[​](#see-also)

- [pause()](/docs/studio/pause)

- [toggle()](/docs/studio/toggle)

- [seek()](/docs/studio/seek)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/play.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/play.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/play.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/play.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/play.ts)