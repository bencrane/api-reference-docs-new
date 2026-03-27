---
title: "Loading from staticFile()"
url: "https://www.remotion.dev/docs/lottie/staticfile"
path: "/docs/lottie/staticfile"
---

"---\nimage: /generated/articles-docs-lottie-lottie-staticfile.png\nid: lottie-staticfile\nsidebar_label: \"Loading from staticFile()\"\ntitle: \"Loading Lottie animations from staticFile()\"\nslug: staticfile\ncrumb: \"@remotion/lottie\"\n---\n\nIn order to load a Lottie animation from a file that has been put into the `public/` folder, use [`staticFile()`](/docs/staticfile) in combination with [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and Remotion's [`delayRender()`](/docs/delay-render) function.\n\nUse the `LottieAnimationData` type to keep a state using React's `useState()` and only render the [`<Lottie>`](/docs/lottie/lottie) component once the data has been fetched.\n\n```tsx twoslash title=\"Animation.tsx\"\nimport { Lottie, LottieAnimationData } from \"@remotion/lottie\";\nimport { useEffect, useState } from \"react\";\nimport {\n  cancelRender,\n  continueRender,\n  delayRender,\n  staticFile,\n} from \"remotion\";\n\nconst Square = () => {\n  const [handle] = useState(() => delayRender(\"Loading Lottie animation\"));\n\n  const [animationData, setAnimationData] =\n    useState<LottieAnimationData | null>(null);\n\n  useEffect(() => {\n    fetch(staticFile(\"data.json\"))\n      .then((data) => data.json())\n      .then((json) => {\n        setAnimationData(json);\n        continueRender(handle);\n      })\n      .catch((err) => {\n        cancelRender(err);\n      });\n  }, [handle]);\n\n  if (!animationData) {\n    return null;\n  }\n\n  return <Lottie animationData={animationData} />;\n};\n```\n\n## See also\n\n- [`<Lottie>`](/docs/lottie/lottie)\n- [Loading from a URL](/docs/lottie/remote)\n"

In order to load a Lottie animation from a file that has been put into the `public/` folder, use [`staticFile()`](/docs/staticfile) in combination with [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and Remotion's [`delayRender()`](/docs/delay-render) function.

Use the `LottieAnimationData` type to keep a state using React's `useState()` and only render the [`<Lottie>`](/docs/lottie/lottie) component once the data has been fetched.

```

Animation.tsximport { Lottie, LottieAnimationData } from "@remotion/lottie";
import { useEffect, useState } from "react";
import {
  cancelRender,
  continueRender,
  delayRender,
  staticFile,
} from "remotion";

const Square = () => {
  const [handle] = useState(() => delayRender("Loading Lottie animation"));

  const [animationData, setAnimationData] =
    useState<LottieAnimationData | null>(null);

  useEffect(() => {
    fetch(staticFile("data.json"))
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

- [Loading from a URL](/docs/lottie/remote)
](/docs/lottie/remote)](/docs/lottie/remote)
](/docs/lottie/remote)