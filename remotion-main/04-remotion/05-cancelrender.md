---
title: "cancelRender()"
url: "https://www.remotion.dev/docs/cancel-render"
path: "/docs/cancel-render"
---

"---\nimage: /generated/articles-docs-cancel-render.png\nid: cancel-render\ntitle: cancelRender()\nsidebar_label: cancelRender()\ncrumb: 'How to'\n---\n\n# cancelRender()<AvailableFrom v=\"3.3.44\" />\n\nBy invoking this function, Remotion will stop the current render, and not perform any retries.\n\nPass a `string` or an `Error` (for best stack traces) to `cancelRender()` so you can identify the error when your render failed.  \nIf a `string` is passed, it will be turned into an `Error` object.\n\n[It `throw`s the error](#cancelrender-throws-an-error), so any code after it will not be executed.  \nYou might have to catch it to avoid unhandled errors.\n\n`cancelRender()` can be imported from the [`remotion`](/docs/remotion) package, but preferrably, you should use the [`useDelayRender()`](/docs/use-delay-render) (from v3.0.374) hook instead, because it future-proofs your code for [browser rendering](/docs/miscellaneous/render-in-browser).\n\n## Example\n\n```tsx twoslash title=\"MyComposition.tsx\"\nimport React, {useEffect, useState} from 'react';\nimport {useDelayRender} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const {delayRender, continueRender, cancelRender} = useDelayRender();\n  const [handle] = useState(() => delayRender('Fetching data...'));\n\n  useEffect(() => {\n    fetch('https://example.com')\n      .then(() => {\n        continueRender(handle);\n      })\n      .catch((err) => {\n        cancelRender(err);\n      });\n  }, []);\n\n  return null;\n};\n```\n\n```tsx twoslash title=\"⚠️ Discouraged - global APIs\"\nimport {useEffect, useState} from 'react';\nimport {delayRender, continueRender, cancelRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const [handle] = useState(() => delayRender('Fetching data...'));\n\n  useEffect(() => {\n    fetch('https://example.com')\n      .then(() => {\n        continueRender(handle);\n      })\n      .catch((err) => {\n        cancelRender(err);\n      });\n  }, []);\n\n  return <div>My component</div>;\n};\n```\n\n## `cancelRender()` throws an error\n\n`cancelRender()` also throws an error, so any code after it will not be executed.\n\nIn [client-side rendering](/docs/miscellaneous/render-in-browser), this is not caught by [`renderMediaOnWeb()`](/docs/web-renderer/render-media-on-web) or [`renderStillOnWeb()`](/docs/web-renderer/render-still-on-web) and is an unhandled error.  \nWrap `cancelRender()` in a `try`/`catch` block to avoid this:\n\n```tsx twoslash title=\"✅ Best practice - wrap cancelRender() in a try/catch block\" {4-7}\nimport {useDelayRender} from 'remotion';\n\nconst {cancelRender} = useDelayRender();\n\ntry {\n  cancelRender(new Error('This throws an error'));\n} catch {\n  // Ignore the resulting error\n}\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={false} bun={false} serverlessFunctions={false} clientSideRendering serverSideRendering player=\"Throws error\" studio=\"Throws error\" hideBrowsers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/cancel-render.ts)\n- [delayRender()](/docs/delay-render)\n- [continueRender()](/docs/continue-render)\n"

By invoking this function, Remotion will stop the current render, and not perform any retries.

Pass a `string` or an `Error` (for best stack traces) to `cancelRender()` so you can identify the error when your render failed.

If a `string` is passed, it will be turned into an `Error` object.

[It `throw`s the error](#cancelrender-throws-an-error), so any code after it will not be executed.

You might have to catch it to avoid unhandled errors.

`cancelRender()` can be imported from the [`remotion`](/docs/remotion) package, but preferrably, you should use the [`useDelayRender()`](/docs/use-delay-render) (from v3.0.374) hook instead, because it future-proofs your code for [browser rendering](/docs/miscellaneous/render-in-browser).

## Example[​](#example)

```

MyComposition.tsximport React, {useEffect, useState} from 'react';
import {useDelayRender} from 'remotion';

export const MyComp: React.FC = () => {
  const {delayRender, continueRender, cancelRender} = useDelayRender();
  const [handle] = useState(() => delayRender('Fetching data...'));

  useEffect(() => {
    fetch('https://example.com')
      .then(() => {
        continueRender(handle);
      })
      .catch((err) => {
        cancelRender(err);
      });
  }, []);

  return null;
};Copy
```

```

⚠️ Discouraged - global APIsimport {useEffect, useState} from 'react';
import {delayRender, continueRender, cancelRender} from 'remotion';

const MyComp: React.FC = () => {
  const [handle] = useState(() => delayRender('Fetching data...'));

  useEffect(() => {
    fetch('https://example.com')
      .then(() => {
        continueRender(handle);
      })
      .catch((err) => {
        cancelRender(err);
      });
  }, []);

  return <div>My component</div>;
};Copy
```

## `cancelRender()` throws an error[​](#cancelrender-throws-an-error)

`cancelRender()` also throws an error, so any code after it will not be executed.

In [client-side rendering](/docs/miscellaneous/render-in-browser), this is not caught by [`renderMediaOnWeb()`](/docs/web-renderer/render-media-on-web) or [`renderStillOnWeb()`](/docs/web-renderer/render-still-on-web) and is an unhandled error.

Wrap `cancelRender()` in a `try`/`catch` block to avoid this:

```

✅ Best practice - wrap cancelRender() in a try/catch blockimport {useDelayRender} from 'remotion';

const {cancelRender} = useDelayRender();

try {
  cancelRender(new Error('This throws an error'));
} catch {
  // Ignore the resulting error
}Copy
```

## Compatibility[​](#compatibility)

|  Servers Environments
|  
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
Throws error 
Throws error

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/cancel-render.ts)

- [delayRender()](/docs/delay-render)

- [continueRender()](/docs/continue-render)
](/docs/continue-render)](/docs/continue-render)
](/docs/continue-render)
- ](/docs/continue-render)
- ](/docs/continue-render)
- ](/docs/continue-render)