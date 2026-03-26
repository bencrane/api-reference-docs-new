---
title: "Loading from a URL"
url: "https://www.remotion.dev/docs/lottie/remote"
path: "/docs/lottie/remote"
---

"---\nimage: /generated/articles-docs-lottie-lottie-remote.png\nid: lottie-remote\nsidebar_label: \"Loading from a URL\"\ntitle: \"Loading Lottie animations from a URL\"\nslug: remote\ncrumb: \"@remotion/lottie\"\n---\n\nIn order to load a Lottie animation from a URL that has been put into the `public/` folder, use [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and Remotion's [`delayRender()`](/docs/delay-render) function.\n\nThe resource must support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).\n\nUse the `LottieAnimationData` type to keep a state using React's `useState()` and only render the [`<Lottie>`](/docs/lottie/lottie) component once the data has been fetched.\n\n```tsx twoslash title=\"Animation.tsx\"\nimport { Lottie, LottieAnimationData } from \"@remotion/lottie\";\nimport { useEffect, useState } from \"react\";\nimport { cancelRender, continueRender, delayRender } from \"remotion\";\n\nconst Balloons = () => {\n  const [handle] = useState(() => delayRender(\"Loading Lottie animation\"));\n\n  const [animationData, setAnimationData] =\n    useState<LottieAnimationData | null>(null);\n\n  useEffect(() => {\n    fetch(\"https://assets4.lottiefiles.com/packages/lf20_zyquagfl.json\")\n      .then((data) => data.json())\n      .then((json) => {\n        setAnimationData(json);\n        continueRender(handle);\n      })\n      .catch((err) => {\n        cancelRender(err);\n      });\n  }, [handle]);\n\n  if (!animationData) {\n    return null;\n  }\n\n  return <Lottie animationData={animationData} />;\n};\n```\n\n## See also\n\n- [`<Lottie>`](/docs/lottie/lottie)\n- [Loading from `staticFile()`](/docs/staticfile)\n"

In order to load a Lottie animation from a URL that has been put into the `public/` folder, use [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and Remotion's [`delayRender()`](/docs/delay-render) function.

The resource must support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

Use the `LottieAnimationData` type to keep a state using React's `useState()` and only render the [`<Lottie>`](/docs/lottie/lottie) component once the data has been fetched.

```

Animation.tsximport { Lottie, LottieAnimationData } from "@remotion/lottie";
import { useEffect, useState } from "react";
import { cancelRender, continueRender, delayRender } from "remotion";

const Balloons = () => {
  const [handle] = useState(() => delayRender("Loading Lottie animation"));

  const [animationData, setAnimationData] =
    useState<LottieAnimationData | null>(null);

  useEffect(() => {
    fetch("https://assets4.lottiefiles.com/packages/lf20_zyquagfl.json")
      .then((data) => data.json())
      .then((json) => {
        setAnimationData(json);
        continueRender(handle);
      })
      .catch((err) => {
        cancelRender(err);
      });
  }, [handle]);

  if (!animationData) {
    return null;
  }

  return <Lottie animationData={animationData} />;
};Copy
```

## See also[​](#see-also)

- [`<Lottie>`](/docs/lottie/lottie)

- [Loading from `staticFile()`](/docs/staticfile)
](/docs/staticfile)](/docs/staticfile)
](/docs/staticfile)