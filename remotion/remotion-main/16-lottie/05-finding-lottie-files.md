---
title: "Finding Lottie files"
url: "https://www.remotion.dev/docs/lottie/lottiefiles"
path: "/docs/lottie/lottiefiles"
---

"---\nimage: /generated/articles-docs-lottie-lottie-lottiefiles.png\nid: lottie-lottiefiles\nsidebar_label: 'Finding Lottie files'\ntitle: 'Finding Lottie files to use'\nslug: lottiefiles\ncrumb: 'Resources'\n---\n\nimport {InlineStep} from '../../components/InlineStep';\n\n[LottieFiles](https://lottiefiles.com) is a website where people can share and download Lottie files.\n\n<img src=\"https://pub-646d808d9cb240cea53bedc76dd3cd0c.r2.dev/lottiefiles.png\" />\n\n<br />\n<br />\n\nIf you find a file that you like, click on it, then click `Download` <InlineStep>1</InlineStep> and choose `Lottie JSON` <InlineStep>2</InlineStep> as the format.\n\n<img src=\"https://pub-646d808d9cb240cea53bedc76dd3cd0c.r2.dev/lottiefiles-instructions.png\" />\n\n### Import the file into Remotion\n\nCopy the file into the Remotion project. The recommended way is to put the JSON inside the `public/` folder of Remotion (create it if necessary) and then load it using [`staticFile()`](/docs/staticfile):\n\n```tsx twoslash title=\"Animation.tsx\"\nimport {Lottie, LottieAnimationData} from '@remotion/lottie';\nimport {useEffect, useState} from 'react';\nimport {cancelRender, continueRender, delayRender, staticFile} from 'remotion';\n\nconst Balloons = () => {\n  const [handle] = useState(() => delayRender('Loading Lottie animation'));\n\n  const [animationData, setAnimationData] = useState<LottieAnimationData | null>(null);\n\n  useEffect(() => {\n    fetch(staticFile('animation.json'))\n      .then((data) => data.json())\n      .then((json) => {\n        setAnimationData(json);\n        continueRender(handle);\n      })\n      .catch((err) => {\n        cancelRender(err);\n      });\n  }, [handle]);\n\n  if (!animationData) {\n    return null;\n  }\n\n  return <Lottie animationData={animationData} />;\n};\n```\n\n## See also\n\n- [Import from After Effects](/docs/after-effects)\n"

[LottieFiles](https://lottiefiles.com) is a website where people can share and download Lottie files.

If you find a file that you like, click on it, then click `Download` 
1 and choose `Lottie JSON` 
2 as the format.

### Import the file into Remotion[​](#import-the-file-into-remotion)

Copy the file into the Remotion project. The recommended way is to put the JSON inside the `public/` folder of Remotion (create it if necessary) and then load it using [`staticFile()`](/docs/staticfile):

```

Animation.tsximport {Lottie, LottieAnimationData} from '@remotion/lottie';
import {useEffect, useState} from 'react';
import {cancelRender, continueRender, delayRender, staticFile} from 'remotion';

const Balloons = () => {
  const [handle] = useState(() => delayRender('Loading Lottie animation'));

  const [animationData, setAnimationData] = useState<LottieAnimationData | null>(null);

  useEffect(() => {
    fetch(staticFile('animation.json'))
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

- [Import from After Effects](/docs/after-effects)
](/docs/after-effects)](/docs/after-effects)
](/docs/after-effects)
- ](/docs/after-effects)