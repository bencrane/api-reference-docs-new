---
title: "Timings"
url: "https://www.remotion.dev/docs/transitions/timings/"
path: "/docs/transitions/timings/"
---

"---\nimage: /generated/articles-docs-transitions-timings-index.png\ntitle: Timings\ncrumb: \"@remotion/transitions\"\n---\n\nA **timing** together with a presentation forms a transition.  \nRemotion provides certain timings out of the box, but you can also [create your own](/docs/transitions/timings/custom).\n\n## Available timings\n\nimport { Timings } from \"../../../components/TableOfContents/transitions/timings\";\n\n<Timings />\n\n## Getting the duration of a timing\n\nYou can get the duration of a transition by calling `getDurationInFrames()` on the timing:\n\n```tsx twoslash title=\"Assuming a framerate of 30fps\"\nimport { springTiming } from \"@remotion/transitions\";\n\nspringTiming({ config: { damping: 200 } }).getDurationInFrames({ fps: 30 }); // 23\n```\n"

A **timing** together with a presentation forms a transition.

Remotion provides certain timings out of the box, but you can also [create your own](/docs/transitions/timings/custom).

## Available timings[​](#available-timings)

[
**`springTiming()`**
Transition with a `spring()`](/docs/transitions/timings/springtiming)[
**`linearTiming()`**
Transition linearly with optional Easing](/docs/transitions/timings/lineartiming)[
**Custom timings**
Implement your own timing](/docs/transitions/timings/custom)

## Getting the duration of a timing[​](#getting-the-duration-of-a-timing)

You can get the duration of a transition by calling `getDurationInFrames()` on the timing:

```

Assuming a framerate of 30fpsimport { springTiming } from "@remotion/transitions";

springTiming({ config: { damping: 200 } }).getDurationInFrames({ fps: 30 }); // 23Copy
```
](#getting-the-duration-of-a-timing)](#getting-the-duration-of-a-timing)
](#getting-the-duration-of-a-timing)
- ](#getting-the-duration-of-a-timing)