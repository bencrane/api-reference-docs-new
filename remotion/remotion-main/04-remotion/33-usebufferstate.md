---
title: "useBufferState()"
url: "https://www.remotion.dev/docs/use-buffer-state"
path: "/docs/use-buffer-state"
---

"---\nimage: /generated/articles-docs-use-buffer-state.png\ntitle: useBufferState()\nid: use-buffer-state\ncrumb: 'API'\n---\n\n_available from 4.0.111_\n\nYou can use this hook inside your [composition](/docs/terminology/composition) to retrieve functions that can inform the Player that your component is currently loading data.\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport React from 'react';\nimport {useBufferState} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const buffer = useBufferState();\n\n  React.useEffect(() => {\n    const delayHandle = buffer.delayPlayback();\n\n    setTimeout(() => {\n      delayHandle.unblock();\n    }, 5000);\n\n    return () => {\n      delayHandle.unblock();\n    };\n  }, []);\n\n  return <></>;\n};\n```\n\n## API\n\nReturns an object with one method:\n\n### `delayPlayback()`\n\nTells the Player to delay playback until you call `unblock()`.\n\n## Usage notes\n\n### Handle unmounting\n\nThe user might seek to a different portion of the video which is immediately available.  \nUse the cleanup function of <code>useEffect()</code> to clear the handle when your component is unmounted.\n\n```tsx twoslash title=\"❌ Causes problems with React strict mode\"\nimport React, {useState} from 'react';\nimport {useBufferState} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const buffer = useBufferState();\n  const [delayHandle] = useState(() => buffer.delayPlayback()); // 💥\n\n  React.useEffect(() => {\n    return () => {\n      delayHandle.unblock();\n    };\n  }, []);\n\n  return <></>;\n};\n```\n\n### Avoid calling inside `useState()`\n\nWhile the following implementation works in production, it fails in development if you are inside React Strict mode, because the `useState()` hook is called twice, which causes the first invocation of the buffer to never be cleared and the video to buffer forever.\n\n```tsx twoslash title=\"❌ Doesn't clear the buffer handle when seeking to a different portion of a video\"\nimport React, {useState} from 'react';\nimport {useBufferState} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const buffer = useBufferState();\n  const [delayHandle] = useState(() => buffer.delayPlayback()); // 💥\n\n  React.useEffect(() => {\n    setTimeout(() => {\n      delayHandle.unblock();\n    }, 5000);\n\n    return () => {\n      delayHandle.unblock();\n    };\n  }, []);\n\n  return <></>;\n};\n```\n\n### Together with `delayRender()`\n\n[`delayRender()`](/docs/delay-render) is a different API that comes into play during rendering.\n\nIf you are loading data, you might want to both delay the screenshotting of your component during rendering and start a buffering state during Preview, in which case you need to use both APIs together.\n\n```tsx twoslash title=\"Using delayRender() and delayPlayback() together\"\nimport React from 'react';\nimport {useBufferState, delayRender, continueRender} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const buffer = useBufferState();\n  const [handle] = React.useState(() => delayRender());\n\n  React.useEffect(() => {\n    const delayHandle = buffer.delayPlayback();\n\n    setTimeout(() => {\n      delayHandle.unblock();\n      continueRender(handle);\n    }, 5000);\n\n    return () => {\n      delayHandle.unblock();\n    };\n  }, []);\n\n  return <></>;\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={''} bun={''} serverlessFunctions=\"\" clientSideRendering={'No-op'} serverSideRendering={'No-op'} player studio hideServers />\n\n## See also\n\n- [Buffer state](/docs/player/buffer-state)\n"

*available from 4.0.111*

You can use this hook inside your [composition](/docs/terminology/composition) to retrieve functions that can inform the Player that your component is currently loading data.

```

MyComp.tsximport React from 'react';
import {useBufferState} from 'remotion';

const MyComp: React.FC = () => {
  const buffer = useBufferState();

  React.useEffect(() => {
    const delayHandle = buffer.delayPlayback();

    setTimeout(() => {
      delayHandle.unblock();
    }, 5000);

    return () => {
      delayHandle.unblock();
    };
  }, []);

  return <></>;
};Copy
```

## API[​](#api)

Returns an object with one method:

### `delayPlayback()`[​](#delayplayback)

Tells the Player to delay playback until you call `unblock()`.

## Usage notes[​](#usage-notes)

### Handle unmounting[​](#handle-unmounting)

The user might seek to a different portion of the video which is immediately available.

Use the cleanup function of `useEffect()` to clear the handle when your component is unmounted.

```

❌ Causes problems with React strict modeimport React, {useState} from 'react';
import {useBufferState} from 'remotion';

const MyComp: React.FC = () => {
  const buffer = useBufferState();
  const [delayHandle] = useState(() => buffer.delayPlayback()); // 💥

  React.useEffect(() => {
    return () => {
      delayHandle.unblock();
    };
  }, []);

  return <></>;
};Copy
```

### Avoid calling inside `useState()`[​](#avoid-calling-inside-usestate)

While the following implementation works in production, it fails in development if you are inside React Strict mode, because the `useState()` hook is called twice, which causes the first invocation of the buffer to never be cleared and the video to buffer forever.

```

❌ Doesn't clear the buffer handle when seeking to a different portion of a videoimport React, {useState} from 'react';
import {useBufferState} from 'remotion';

const MyComp: React.FC = () => {
  const buffer = useBufferState();
  const [delayHandle] = useState(() => buffer.delayPlayback()); // 💥

  React.useEffect(() => {
    setTimeout(() => {
      delayHandle.unblock();
    }, 5000);

    return () => {
      delayHandle.unblock();
    };
  }, []);

  return <></>;
};Copy
```

### Together with `delayRender()`[​](#together-with-delayrender)

[`delayRender()`](/docs/delay-render) is a different API that comes into play during rendering.

If you are loading data, you might want to both delay the screenshotting of your component during rendering and start a buffering state during Preview, in which case you need to use both APIs together.

```

Using delayRender() and delayPlayback() togetherimport React from 'react';
import {useBufferState, delayRender, continueRender} from 'remotion';

const MyComp: React.FC = () => {
  const buffer = useBufferState();
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
 
 
 
No-op 
No-op 
 

## See also[​](#see-also)

- [Buffer state](/docs/player/buffer-state)
](/docs/player/buffer-state)](/docs/player/buffer-state)
](/docs/player/buffer-state)
- ](/docs/player/buffer-state)
- ](/docs/player/buffer-state)
- ](/docs/player/buffer-state)
- ](/docs/player/buffer-state)
- ](/docs/player/buffer-state)
- ](/docs/player/buffer-state)
- ](/docs/player/buffer-state)