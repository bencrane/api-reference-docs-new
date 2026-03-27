---
title: "seek()"
url: "https://www.remotion.dev/docs/studio/seek"
path: "/docs/studio/seek"
---

"---\nimage: /generated/articles-docs-studio-seek.png\ntitle: seek()\ncrumb: '@remotion/studio'\n---\n\n# seek()<AvailableFrom v=\"4.0.259\"/>\n\nJump to a position in time in the Remotion Studio.\n\nIf a number smaller than 0 is passed, the value will be automatically clamped to 0.  \nIf a number greater than or equal to the duration of the composition is passed, the value will be automatically clamped to `durationInFrames - 1`.\n\nUse [`useVideoConfig()`](/docs/use-video-config) to get the duration of the composition.\n\n## Examples\n\n```tsx twoslash title=\"Saving {color: 'green'} to Root.tsx\"\nimport {seek} from '@remotion/studio';\n\nseek(100);\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/seek.ts)\n"

Jump to a position in time in the Remotion Studio.

If a number smaller than 0 is passed, the value will be automatically clamped to 0.

If a number greater than or equal to the duration of the composition is passed, the value will be automatically clamped to `durationInFrames - 1`.

Use [`useVideoConfig()`](/docs/use-video-config) to get the duration of the composition.

## Examples[​](#examples)

```

Saving {color: 'green'} to Root.tsximport {seek} from '@remotion/studio';

seek(100);Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/seek.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/seek.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/seek.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/seek.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/seek.ts)