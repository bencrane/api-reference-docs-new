---
title: "measureSpring()"
url: "https://www.remotion.dev/docs/measure-spring"
path: "/docs/measure-spring"
---

"---\nimage: /generated/articles-docs-measure-spring.png\ntitle: measureSpring()\nid: measure-spring\ncrumb: 'API'\n---\n\n<AvailableFrom v=\"2.0.8\" />\n\nBased on a [spring()](/docs/spring) configuration and the frame rate, return how long it takes for a spring animation to settle.\n\n```tsx twoslash\nimport {measureSpring, SpringConfig} from 'remotion';\n\nconst config: Partial<SpringConfig> = {\n  damping: 200,\n};\n\nmeasureSpring({\n  fps: 30,\n  config: {\n    damping: 200,\n  },\n}); // => 23\n```\n\n:::info\nTheoretically, a spring animation never ends. There is always a miniscule amount or energy left in the spring that causes tiny movements. Instead, we set a threshold to define when the spring animation is considered done.\n:::\n\n## Arguments\n\nAn object with these keys:\n\n### `fps`\n\nThe frame rate on which the spring animation is based on.\n\n### `threshold?`\n\nDefines when the animation should be considered finished. Default: `0.005`. `0.01` means that the animation is finished when it always stays within 1% of the `to` value. For example an animation that goes from 0 to 1 is considered finished when the value never leaves the range [0.99, 1.01] after the end point.\n\nLower values mean the spring duration is longer, higher values result in the spring duration being shorter.\n\n### `config?`\n\nThe spring configuration that you pass to [spring()](/docs/spring#config).\n\n### `from?`\n\nThe initial value of the animation. Default: `0`.\n\n### `to?`\n\nThe end value of the animation. Default: `1`. Note that depending on the parameters, spring animations may overshoot the target a bit, before they bounce back to their final target.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs bun serverlessFunctions clientSideRendering serverSideRendering player studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/spring/measure-spring.ts)\n- [spring()](/docs/spring)\n"
[v2.0.8](https://github.com/remotion-dev/remotion/releases/v2.0.8)

Based on a [spring()](/docs/spring) configuration and the frame rate, return how long it takes for a spring animation to settle.

```
import {measureSpring, SpringConfig} from 'remotion';

const config: Partial<SpringConfig> = {
  damping: 200,
};

measureSpring({
  fps: 30,
  config: {
    damping: 200,
  },
}); // => 23Copy
```

](/docs/spring)](/docs/spring)
](/docs/spring)
- ](/docs/spring)
- ](/docs/spring)
- ](/docs/spring)
- ](/docs/spring)
- ](/docs/spring)
- ](/docs/spring)
- ](/docs/spring)