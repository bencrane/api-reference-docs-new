---
title: "createSmoothSvgPath()"
url: "https://www.remotion.dev/docs/media-utils/create-smooth-svg-path"
path: "/docs/media-utils/create-smooth-svg-path"
---

"---\nimage: /generated/articles-docs-media-utils-create-smooth-svg-path.png\ntitle: createSmoothSvgPath()\nid: create-smooth-svg-path\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils`_ package of helper functions.\n\nThis function takes points, usually generated from [`visualizeAudioWaveform()`](/docs/media-utils/visualize-audio-waveform) or [`visualizeAudio()`](/docs/visualize-audio), and adds SVG `C` (curve) statements inbetween them to create a smooth path.\n\n## Example\n\n```tsx twoslash\nimport {createSmoothSvgPath} from '@remotion/media-utils';\nimport React from 'react';\n\nconst points = [\n  {x: 0, y: 0},\n  {x: 100, y: 100},\n  {x: 200, y: 50},\n  {x: 300, y: 150},\n];\n\nconst path = createSmoothSvgPath({points});\n```\n\nSee a practical example [here](/docs/media-utils/visualize-audio-waveform#examples).\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/create-smooth-svg-path.ts)\n- [Audio visualization](/docs/audio/visualization)\n"

*Part of the `@remotion/media-utils`* package of helper functions.

This function takes points, usually generated from [`visualizeAudioWaveform()`](/docs/media-utils/visualize-audio-waveform) or [`visualizeAudio()`](/docs/visualize-audio), and adds SVG `C` (curve) statements inbetween them to create a smooth path.

## Example[​](#example)

```
import {createSmoothSvgPath} from '@remotion/media-utils';
import React from 'react';

const points = [
  {x: 0, y: 0},
  {x: 100, y: 100},
  {x: 200, y: 50},
  {x: 300, y: 150},
];

const path = createSmoothSvgPath({points});Copy
```

See a practical example [here](/docs/media-utils/visualize-audio-waveform#examples).

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/create-smooth-svg-path.ts)

- [Audio visualization](/docs/audio/visualization)
](/docs/audio/visualization)](/docs/audio/visualization)
](/docs/audio/visualization)
- ](/docs/audio/visualization)