---
title: "useDelayRender()"
url: "https://www.remotion.dev/docs/use-delay-render"
path: "/docs/use-delay-render"
---

"---\nimage: /generated/articles-docs-use-delay-render.png\nid: use-delay-render\ntitle: useDelayRender()\nsidebar_label: useDelayRender()\ncrumb: 'API'\n---\n\n# useDelayRender()<AvailableFrom v=\"4.0.342\" />\n\nA React hook that provides scoped `delayRender()`, `continueRender()` and `cancelRender()` (from v4.0.374) functions for React components.\n\nThis is the recommended approach instead of using the global [`delayRender()`](/docs/delay-render), [`continueRender()`](/docs/continue-render) and [`cancelRender()`](/docs/cancel-render) functions directly.\n\n```tsx twoslash title=\"✅ Preferred - use useDelayRender()\" {4}\nimport {useDelayRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const {delayRender, continueRender, cancelRender} = useDelayRender();\n\n  return <div>My component</div>;\n};\n```\n\n```tsx twoslash title=\"⚠️ Discouraged - global APIs\"\nimport {useDelayRender, continueRender, delayRender} from 'remotion';\n```\n\n## Why use `useDelayRender()` over global `delayRender()`?\n\nWith this hook, we can scope the delays to a specific render.  \nThis makes it future-proof for [browser rendering](/docs/miscellaneous/render-in-browser).<br /> It is recommended to use this hook instead of the global `delayRender()` function.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={''} bun={''} serverlessFunctions=\"\" clientSideRendering serverSideRendering player=\"No-op\" studio=\"No-op\" hideServers />\n\n## See also\n\n- [`delayRender()`](/docs/delay-render) - The underlying API\n- [`continueRender()`](/docs/continue-render) - Manual render continuation\n- [`cancelRender()`](/docs/cancel-render) - Cancel render on error\n- [Data fetching guide](/docs/data-fetching)\n"

A React hook that provides scoped `delayRender()`, `continueRender()` and `cancelRender()` (from v4.0.374) functions for React components.

This is the recommended approach instead of using the global [`delayRender()`](/docs/delay-render), [`continueRender()`](/docs/continue-render) and [`cancelRender()`](/docs/cancel-render) functions directly.

```

✅ Preferred - use useDelayRender()import {useDelayRender} from 'remotion';

const MyComp: React.FC = () => {
  const {delayRender, continueRender, cancelRender} = useDelayRender();

  return <div>My component</div>;
};Copy
```

```

⚠️ Discouraged - global APIsimport {useDelayRender, continueRender, delayRender} from 'remotion';Copy
```

## Why use `useDelayRender()` over global `delayRender()`?[​](#why-use-usedelayrender-over-global-delayrender)

With this hook, we can scope the delays to a specific render.

This makes it future-proof for [browser rendering](/docs/miscellaneous/render-in-browser).
 It is recommended to use this hook instead of the global `delayRender()` function.

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
 
 
 
 
 
No-op 
No-op

## See also[​](#see-also)

- [`delayRender()`](/docs/delay-render) - The underlying API

- [`continueRender()`](/docs/continue-render) - Manual render continuation

- [`cancelRender()`](/docs/cancel-render) - Cancel render on error

- [Data fetching guide](/docs/data-fetching)
](/docs/data-fetching)](/docs/data-fetching)
](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)