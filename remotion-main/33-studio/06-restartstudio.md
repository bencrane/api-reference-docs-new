---
title: "restartStudio()"
url: "https://www.remotion.dev/docs/studio/restart-studio"
path: "/docs/studio/restart-studio"
---

"---\nimage: /generated/articles-docs-studio-restart-studio.png\ntitle: restartStudio()\ncrumb: \"@remotion/studio\"\n---\n\n# restartStudio()<AvailableFrom v=\"4.0.162\"/>\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport { restartStudio } from \"@remotion/studio\";\nimport { useCallback } from \"react\";\n\nconst MyComp: React.FC = () => {\n  const onClick = useCallback(async () => {\n    try {\n      await restartStudio();\n      console.log(\"Studio will restart now\");\n    } catch (err) {\n      console.error(err);\n    }\n  }, []);\n\n  return (\n    <button type=\"button\" onClick={onClick}>\n      Hello World\n    </button>\n  );\n};\n```\n\n## Requirements\n\nIn order to use this function:\n\n<Step>1</Step> You need to be inside the Remotion Studio.\n<br />\n<Step>2</Step> The Studio must be running (no static deployment)\n<br />\n<br />\n\nOtherwise, the function will throw.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/restart-studio.ts)\n"

```

MyComp.tsximport { restartStudio } from "@remotion/studio";
import { useCallback } from "react";

const MyComp: React.FC = () => {
  const onClick = useCallback(async () => {
    try {
      await restartStudio();
      console.log("Studio will restart now");
    } catch (err) {
      console.error(err);
    }
  }, []);

  return (
    <button type="button" onClick={onClick}>
      Hello World
    </button>
  );
};Copy
```

## Requirements[​](#requirements)

In order to use this function:

[](#1)
[1](#1)[ ](#1) You need to be inside the Remotion Studio.

[](#2)
[2](#2)[ ](#2) The Studio must be running (no static deployment)

Otherwise, the function will throw.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/restart-studio.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/restart-studio.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/restart-studio.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/restart-studio.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/restart-studio.ts)