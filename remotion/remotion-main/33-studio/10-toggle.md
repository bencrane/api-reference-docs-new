---
title: "toggle()"
url: "https://www.remotion.dev/docs/studio/toggle"
path: "/docs/studio/toggle"
---

"---\nimage: /generated/articles-docs-studio-toggle.png\ntitle: toggle()\ncrumb: '@remotion/studio'\n---\n\n# toggle()<AvailableFrom v=\"4.0.287\"/>\n\nToggles playback in the Remotion Studio. If the composition is currently playing, it will pause. If it's paused, it will start playing.\n\nThe function accepts an optional event parameter which can be a `React.SyntheticEvent` or a [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent). This allows the function to be used directly as an event handler.\n\n## Examples\n\n```tsx twoslash title=\"Toggle playback on button click\"\nimport {toggle} from '@remotion/studio';\n\nconst ToggleButton = () => {\n  // Call with the event parameter for better browser audio autoplay\n\n  return <button onClick={(e) => toggle(e)}>Play/Pause</button>;\n};\n```\n\n```tsx twoslash title=\"Toggle playback programmatically\"\nimport {toggle} from '@remotion/studio';\n\n// Call without event parameter\ntoggle();\n```\n\n## See also\n\n- [play()](/docs/studio/play)\n- [pause()](/docs/studio/pause)\n- [seek()](/docs/studio/seek)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/toggle.ts)\n"

Toggles playback in the Remotion Studio. If the composition is currently playing, it will pause. If it's paused, it will start playing.

The function accepts an optional event parameter which can be a `React.SyntheticEvent` or a [`PointerEvent`](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent). This allows the function to be used directly as an event handler.

## Examples[​](#examples)

```

Toggle playback on button clickimport {toggle} from '@remotion/studio';

const ToggleButton = () => {
  // Call with the event parameter for better browser audio autoplay

  return <button onClick={(e) => toggle(e)}>Play/Pause</button>;
};Copy
```

```

Toggle playback programmaticallyimport {toggle} from '@remotion/studio';

// Call without event parameter
toggle();Copy
```

## See also[​](#see-also)

- [play()](/docs/studio/play)

- [pause()](/docs/studio/pause)

- [seek()](/docs/studio/seek)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/toggle.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/toggle.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/toggle.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/toggle.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/toggle.ts)