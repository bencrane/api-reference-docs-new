---
title: "reevaluateComposition()"
url: "https://www.remotion.dev/docs/studio/reevaluate-composition"
path: "/docs/studio/reevaluate-composition"
---

"---\nimage: /generated/articles-docs-studio-reevaluate-composition.png\ntitle: reevaluateComposition()\ncrumb: \"@remotion/studio\"\n---\n\n# reevaluateComposition()<AvailableFrom v=\"4.0.167\"/>\n\nRe-runs [`calculateMetadata()`](/docs/calculate-metadata) on the currently selected composition.  \nThis is useful if the function relies on:\n\n- The `public/` folder\n- Randomness\n- Changing network resources\n- Time\n\n## Example\n\n```tsx twoslash title=\"Re-run calculateMetadata() on the currently selected composition\"\nimport React, { useCallback } from \"react\";\nimport { reevaluateComposition } from \"@remotion/studio\";\n\nexport const ReevaluateCompositionComp: React.FC = () => {\n  const reevaluate = useCallback(async () => {\n    reevaluateComposition();\n\n    console.log(\"Re-evaluated!\");\n  }, []);\n\n  return <button onClick={reevaluate}>Re-evaluate</button>;\n};\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/reevaluate-composition.ts)\n- [`calculateMetadata()`](/docs/calculate-metadata)\n"

Re-runs [`calculateMetadata()`](/docs/calculate-metadata) on the currently selected composition.

This is useful if the function relies on:

- The `public/` folder

- Randomness

- Changing network resources

- Time

## Example[​](#example)

```

Re-run calculateMetadata() on the currently selected compositionimport React, { useCallback } from "react";
import { reevaluateComposition } from "@remotion/studio";

export const ReevaluateCompositionComp: React.FC = () => {
  const reevaluate = useCallback(async () => {
    reevaluateComposition();

    console.log("Re-evaluated!");
  }, []);

  return <button onClick={reevaluate}>Re-evaluate</button>;
};Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/reevaluate-composition.ts)

- [`calculateMetadata()`](/docs/calculate-metadata)
](/docs/calculate-metadata)](/docs/calculate-metadata)
](/docs/calculate-metadata)
- ](/docs/calculate-metadata)