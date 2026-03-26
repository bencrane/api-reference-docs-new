---
title: "delayRender()"
url: "https://www.remotion.dev/docs/delay-render"
path: "/docs/delay-render"
---

"---\nimage: /generated/articles-docs-delay-render.png\nid: delay-render\ntitle: delayRender() and continueRender()\nsidebar_label: delayRender()\ncrumb: 'How to'\n---\n\n`delayRender()` pauses the render to let an asynchronous task such as data fetching complete.  \nIt has no effect when you are in a preview environment (e.g. Studio or Player).\n\nThis API returns a handle. Once you have fetched data or finished the asynchronous task, you should call `continueRender(handle)` to let Remotion know that the render can continue.\n\nIf the asynchronous task fails and you cannot recover, call [`cancelRender()`](/docs/cancel-render) to cancel the render.\n\n`delayRender()` can be imported from the [`remotion`](/docs/remotion) package, but preferrably, you should use the [`useDelayRender()`](/docs/use-delay-render) hook instead, because it future-proofs your code for [browser rendering](/docs/miscellaneous/render-in-browser).\n\n## Example\n\n```tsx twoslash {2, 6,7,  15, 17}\nimport {useCallback, useEffect, useState} from 'react';\nimport {useDelayRender} from 'remotion';\n\nexport const MyVideo = () => {\n  const [data, setData] = useState(null);\n  const {delayRender, continueRender, cancelRender} = useDelayRender();\n  const [handle] = useState(() => delayRender());\n\n  const fetchData = useCallback(async () => {\n    try {\n      const response = await fetch('http://example.com/api');\n      const json = await response.json();\n      setData(json);\n\n      continueRender(handle);\n    } catch (err) {\n      cancelRender(err);\n    }\n  }, []);\n\n  useEffect(() => {\n    fetchData();\n  }, []);\n\n  return <div>{data ? <div>This video has data from an API! {JSON.stringify(data)}</div> : null}</div>;\n};\n```\n\n## Timeout\n\nAfter calling `delayRender()`, you need to call `continueRender()` within 30 seconds or the render will fail with a timeout error. You can [customize the timeout](/docs/timeout#increase-timeout).\n\nIf `continueRender()` is not called within the timeout frame, the render will fail with an exception similarly to this:\n\n```\nA delayRender() was called but not cleared after 28000ms. See https://remotion.dev/docs/timeout for help. The delayRender was called\n```\n\nSee the [Timeout](/docs/timeout) page to troubleshoot timeouts.\n\n## Adding a label<AvailableFrom v=\"2.6.13\"/>\n\nIf you encounter a timeout and don't know where it came from, you can add a label as a parameter:\n\n```tsx twoslash\nimport {delayRender} from 'remotion';\n\n// ---cut---\n\ndelayRender('Fetching data from API...');\n```\n\nIf the call times out, the label will be referenced in the error message:\n\n```\nUncaught Error: A delayRender() \"Fetching data from API...\" was called but not cleared after 28000ms. See https://remotion.dev/docs/timeout for help. The delayRender was called\n```\n\n## Multiple calls\n\nYou can call `delayRender()` multiple times. The render will be blocked for as long as at least one blocking handle exists that has not been cleared by `continueRender()`.\n\n```tsx twoslash\nimport {useEffect, useState} from 'react';\nimport {useDelayRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const {delayRender, continueRender} = useDelayRender();\n  const [handle1] = useState(() => delayRender());\n  const [handle2] = useState(() => delayRender());\n\n  useEffect(() => {\n    // You need to clear all handles before the render continues\n    continueRender(handle1);\n    continueRender(handle2);\n  }, []);\n\n  return null;\n};\n```\n\n## Encapsulation\n\nYou should put `delayRender()` calls inside your components rather than placing them as a top-level statement, to avoid blocking a render if a different composition is rendered.\n\n```tsx twoslash title=\"❌ Bug - Other compositions are blocked\" {4-7}\nimport {useEffect} from 'react';\nimport {continueRender, delayRender} from 'remotion';\n\n// Don't call a delayRender() call outside a component -\n// it will block the render if a different composition is rendered\n// as well as block the fetching of the list of compositions.\nconst handle = delayRender();\n\nconst MyComp: React.FC = () => {\n  useEffect(() => {\n    continueRender(handle);\n  }, []);\n\n  return null;\n};\n```\n\nAlso avoid creating a new handle on every [React render](https://react.dev/learn/render-and-commit):\n\n```tsx twoslash title=\"❌ Bug - New handle is create on every React re-render\" {4-7}\nimport {useEffect} from 'react';\nimport {continueRender, delayRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  // New handle is created on every React re-render\n  const handle = delayRender();\n\n  useEffect(() => {\n    continueRender(handle);\n  }, []);\n\n  return null;\n};\n```\n\nIt's best to always use [`useDelayRender()`](/docs/use-delay-render) in the first place since this mistake cannot happen and it enables [browser rendering](/docs/miscellaneous/render-in-browser) in the future.\n\n```tsx twoslash title=\"✅ Best practice - useDelayRender() + useState() \" {4-7}\nimport {useEffect, useState} from 'react';\nimport {useDelayRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const {delayRender, continueRender} = useDelayRender();\n  const [handle] = useState(() => delayRender());\n\n  useEffect(() => {\n    continueRender(handle);\n  }, []);\n\n  return null;\n};\n```\n\n## Data fetching\n\nNote that data fetching can also be performed in [`calculateMetadata()`](/docs/composition#calculatemetadata), which has 2 advantages:\n\n- It runs only once, rather than the amount of [concurrency](/docs/terminology/concurrency).\n- You don't need to call `continueRender()` or `cancelRender()` manually.\n\n## Failing with an error<AvailableFrom v=\"4.0.374\" />\n\nIf your code fails to do an asynchronous operation and you want to cancel the render, you can call [`cancelRender()`](/docs/cancel-render) with an error message. This will automatically cancel all `delayRender()` calls to not further delay the render.\n\n```tsx twoslash title=\"MyComposition.tsx\"\nimport React, {useEffect, useState} from 'react';\nimport {cancelRender, continueRender, delayRender} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const [handle] = useState(() => delayRender('Fetching data...'));\n\n  useEffect(() => {\n    fetch('https://example.com')\n      .then(() => {\n        continueRender(handle);\n      })\n      .catch((err) => cancelRender(err));\n  }, []);\n\n  return null;\n};\n```\n\n## Retrying<AvailableFrom v=\"4.0.140\"/>\n\nIf an operation is flaky (for example, if loading an asset from a CDN does sometimes give 5xx errors), you can pass an object with a `retries` value as a second argument.  \nIf a `delayRender()` call is not cleared within the timeout, the whole browser tab will be closed and the frame will be retried from scratch.\n\n```tsx twoslash title=\"Retrying a delayRender()\"\nimport {useDelayRender} from 'remotion';\n\nconst {delayRender} = useDelayRender();\n// ---cut---\ndelayRender('Loading asset...', {\n  retries: 1, // default: 0\n});\n```\n\nThe [`<Img>`](/docs/img#delayrenderretries), [`<Video>`](/docs/media/video#delayrenderretries), [`<Audio>`](/docs/media/audio#delayrenderretries), [`<Html5Audio>`](/docs/html5-audio#delayrenderretries), [`<Html5Video>`](/docs/html5-video#delayrenderretries) and [`<IFrame>`](/docs/iframe#delayrenderretries) tags support a `delayRenderRetries` prop to control the value of `retries` for the `delayRender()` call that those components make.\n\n## Modifying the timeout<AvailableFrom v=\"4.0.140\"/>\n\nIn addition to the [global timeout](/docs/timeout#increase-timeout) that can be set, the timeout can be modified on a per-`delayRender()` level.\n\n```tsx twoslash title=\"Modifying the timeout of a delayRender()\"\nimport {useDelayRender} from 'remotion';\nconst {delayRender} = useDelayRender();\n\n// ---cut---\ndelayRender('Loading asset...', {\n  timeoutInMilliseconds: 7000,\n});\n```\n\nThe [`<Img>`](/docs/img#delayrendertimeoutinmilliseconds), [`<Video>`](/docs/media/video#delayrendertimeoutinmilliseconds), [`<Audio>`](/docs/media/audio#delayrendertimeoutinmilliseconds), [`<Html5Audio>`](/docs/html5-audio#delayrendertimeoutinmilliseconds), [`<Html5Video>`](/docs/html5-video#delayrendertimeoutinmilliseconds) and [`<IFrame>`](/docs/iframe#delayrendertimeoutinmilliseconds) tags support a `delayRenderTimeoutInMilliseconds` prop to control the value of `timeoutInMilliseconds` for the `delayRender()` call that those components make.\n\n## Difference to `useBufferState().delayPlayback()`\n\n[`useBufferState()`](/docs/use-buffer-state) is a different API that allows pausing playback in the [Studio](/docs/terminology/studio) and in the [Player](/docs/terminology/player).  \n`delayRender()` only has an effect when a video is being rendered.\n\nIf you are loading data, you might want to both delay the screenshotting of your component during rendering and start a buffering state during Preview, in which case you need to use both APIs together.\n\n```tsx twoslash title=\"Using delayRender() and delayPlayback() together\"\nimport React from 'react';\nimport {useBufferState, useDelayRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const buffer = useBufferState();\n  const {delayRender, continueRender} = useDelayRender();\n  const [handle] = React.useState(() => delayRender());\n\n  React.useEffect(() => {\n    const delayHandle = buffer.delayPlayback();\n\n    setTimeout(() => {\n      delayHandle.unblock();\n      continueRender(handle);\n    }, 5000);\n\n    return () => {\n      delayHandle.unblock();\n    };\n  }, []);\n\n  return <></>;\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={'No-op'} bun={'No-op'} serverlessFunctions=\"No-op\" clientSideRendering=\"Use useDelayRender()\" serverSideRendering player=\"No-op\" studio=\"No-op\" hideServers />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/delay-render.ts)\n- [`useDelayRender()`](/docs/use-delay-render)\n- [`continueRender()`](/docs/continue-render)\n- [`cancelRender()`](/docs/cancel-render)\n- [Data fetching](/docs/data-fetching)\n"

`delayRender()` pauses the render to let an asynchronous task such as data fetching complete.

It has no effect when you are in a preview environment (e.g. Studio or Player).

This API returns a handle. Once you have fetched data or finished the asynchronous task, you should call `continueRender(handle)` to let Remotion know that the render can continue.

If the asynchronous task fails and you cannot recover, call [`cancelRender()`](/docs/cancel-render) to cancel the render.

`delayRender()` can be imported from the [`remotion`](/docs/remotion) package, but preferrably, you should use the [`useDelayRender()`](/docs/use-delay-render) hook instead, because it future-proofs your code for [browser rendering](/docs/miscellaneous/render-in-browser).

## Example[​](#example)

```
import {useCallback, useEffect, useState} from 'react';
import {useDelayRender} from 'remotion';

export const MyVideo = () => {
  const [data, setData] = useState(null);
  const {delayRender, continueRender, cancelRender} = useDelayRender();
  const [handle] = useState(() => delayRender());

  const fetchData = useCallback(async () => {
    try {
      const response = await fetch('http://example.com/api');
      const json = await response.json();
      setData(json);

      continueRender(handle);
    } catch (err) {
      cancelRender(err);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, []);

  return <div>{data ? <div>This video has data from an API! {JSON.stringify(data)}</div> : null}</div>;
};Copy
```

## Timeout[​](#timeout)

After calling `delayRender()`, you need to call `continueRender()` within 30 seconds or the render will fail with a timeout error. You can [customize the timeout](/docs/timeout#increase-timeout).

If `continueRender()` is not called within the timeout frame, the render will fail with an exception similarly to this:

```
A delayRender() was called but not cleared after 28000ms. See https://remotion.dev/docs/timeout for help. The delayRender was calledCopy
```

See the [Timeout](/docs/timeout) page to troubleshoot timeouts.

## Adding a label[v2.6.13](https://github.com/remotion-dev/remotion/releases/v2.6.13)[​](#adding-a-label)

If you encounter a timeout and don't know where it came from, you can add a label as a parameter:

```

delayRender('Fetching data from API...');Copy
```

If the call times out, the label will be referenced in the error message:

```
Uncaught Error: A delayRender() "Fetching data from API..." was called but not cleared after 28000ms. See https://remotion.dev/docs/timeout for help. The delayRender was calledCopy
```

## Multiple calls[​](#multiple-calls)

You can call `delayRender()` multiple times. The render will be blocked for as long as at least one blocking handle exists that has not been cleared by `continueRender()`.

```
import {useEffect, useState} from 'react';
import {useDelayRender} from 'remotion';

const MyComp: React.FC = () => {
  const {delayRender, continueRender} = useDelayRender();
  const [handle1] = useState(() => delayRender());
  const [handle2] = useState(() => delayRender());

  useEffect(() => {
    // You need to clear all handles before the render continues
    continueRender(handle1);
    continueRender(handle2);
  }, []);

  return null;
};Copy
```

## Encapsulation[​](#encapsulation)

You should put `delayRender()` calls inside your components rather than placing them as a top-level statement, to avoid blocking a render if a different composition is rendered.

```

❌ Bug - Other compositions are blockedimport {useEffect} from 'react';
import {continueRender, delayRender} from 'remotion';

// Don't call a delayRender() call outside a component -
// it will block the render if a different composition is rendered
// as well as block the fetching of the list of compositions.
const handle = delayRender();

const MyComp: React.FC = () => {
  useEffect(() => {
    continueRender(handle);
  }, []);

  return null;
};Copy
```

Also avoid creating a new handle on every [React render](https://react.dev/learn/render-and-commit):

```

❌ Bug - New handle is create on every React re-renderimport {useEffect} from 'react';
import {continueRender, delayRender} from 'remotion';

const MyComp: React.FC = () => {
  // New handle is created on every React re-render
  const handle = delayRender();

  useEffect(() => {
    continueRender(handle);
  }, []);

  return null;
};Copy
```

It's best to always use [`useDelayRender()`](/docs/use-delay-render) in the first place since this mistake cannot happen and it enables [browser rendering](/docs/miscellaneous/render-in-browser) in the future.

```

✅ Best practice - useDelayRender() + useState() import {useEffect, useState} from 'react';
import {useDelayRender} from 'remotion';

const MyComp: React.FC = () => {
  const {delayRender, continueRender} = useDelayRender();
  const [handle] = useState(() => delayRender());

  useEffect(() => {
    continueRender(handle);
  }, []);

  return null;
};Copy
```

## Data fetching[​](#data-fetching)

Note that data fetching can also be performed in [`calculateMetadata()`](/docs/composition#calculatemetadata), which has 2 advantages:

- It runs only once, rather than the amount of [concurrency](/docs/terminology/concurrency).

- You don't need to call `continueRender()` or `cancelRender()` manually.

## Failing with an error[v4.0.374](https://github.com/remotion-dev/remotion/releases/v4.0.374)[​](#failing-with-an-error)

If your code fails to do an asynchronous operation and you want to cancel the render, you can call [`cancelRender()`](/docs/cancel-render) with an error message. This will automatically cancel all `delayRender()` calls to not further delay the render.

```

MyComposition.tsximport React, {useEffect, useState} from 'react';
import {cancelRender, continueRender, delayRender} from 'remotion';

export const MyComp: React.FC = () => {
  const [handle] = useState(() => delayRender('Fetching data...'));

  useEffect(() => {
    fetch('https://example.com')
      .then(() => {
        continueRender(handle);
      })
      .catch((err) => cancelRender(err));
  }, []);

  return null;
};Copy
```

## Retrying[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#retrying)

If an operation is flaky (for example, if loading an asset from a CDN does sometimes give 5xx errors), you can pass an object with a `retries` value as a second argument.

If a `delayRender()` call is not cleared within the timeout, the whole browser tab will be closed and the frame will be retried from scratch.

```

Retrying a delayRender()delayRender('Loading asset...', {
  retries: 1, // default: 0
});Copy
```

The [`<Img>`](/docs/img#delayrenderretries), [`<Video>`](/docs/media/video#delayrenderretries), [`<Audio>`](/docs/media/audio#delayrenderretries), [`<Html5Audio>`](/docs/html5-audio#delayrenderretries), [`<Html5Video>`](/docs/html5-video#delayrenderretries) and [`<IFrame>`](/docs/iframe#delayrenderretries) tags support a `delayRenderRetries` prop to control the value of `retries` for the `delayRender()` call that those components make.

## Modifying the timeout[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#modifying-the-timeout)

In addition to the [global timeout](/docs/timeout#increase-timeout) that can be set, the timeout can be modified on a per-`delayRender()` level.

```

Modifying the timeout of a delayRender()delayRender('Loading asset...', {
  timeoutInMilliseconds: 7000,
});Copy
```

The [`<Img>`](/docs/img#delayrendertimeoutinmilliseconds), [`<Video>`](/docs/media/video#delayrendertimeoutinmilliseconds), [`<Audio>`](/docs/media/audio#delayrendertimeoutinmilliseconds), [`<Html5Audio>`](/docs/html5-audio#delayrendertimeoutinmilliseconds), [`<Html5Video>`](/docs/html5-video#delayrendertimeoutinmilliseconds) and [`<IFrame>`](/docs/iframe#delayrendertimeoutinmilliseconds) tags support a `delayRenderTimeoutInMilliseconds` prop to control the value of `timeoutInMilliseconds` for the `delayRender()` call that those components make.

## Difference to `useBufferState().delayPlayback()`[​](#difference-to-usebufferstatedelayplayback)

[`useBufferState()`](/docs/use-buffer-state) is a different API that allows pausing playback in the [Studio](/docs/terminology/studio) and in the [Player](/docs/terminology/player).

`delayRender()` only has an effect when a video is being rendered.

If you are loading data, you might want to both delay the screenshotting of your component during rendering and start a buffering state during Preview, in which case you need to use both APIs together.

```

Using delayRender() and delayPlayback() togetherimport React from 'react';
import {useBufferState, useDelayRender} from 'remotion';

const MyComp: React.FC = () => {
  const buffer = useBufferState();
  const {delayRender, continueRender} = useDelayRender();
  const [handle] = React.useState(() => delayRender());

  React.useEffect(() => {
    const delayHandle = buffer.delayPlayback();

    setTimeout(() => {
      delayHandle.unblock();
      continueRender(handle);
    }, 5000);

    return () => {
      delayHandle.unblock();
    };
  }, []);

  return <></>;
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
 
 
 
Use useDelayRender() 
 
No-op 
No-op

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/delay-render.ts)

- [`useDelayRender()`](/docs/use-delay-render)

- [`continueRender()`](/docs/continue-render)

- [`cancelRender()`](/docs/cancel-render)

- [Data fetching](/docs/data-fetching)
](/docs/data-fetching)](/docs/data-fetching)
](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)
- ](/docs/data-fetching)