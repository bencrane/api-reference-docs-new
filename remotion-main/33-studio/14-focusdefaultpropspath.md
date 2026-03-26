---
title: "focusDefaultPropsPath()"
url: "https://www.remotion.dev/docs/studio/focus-default-props-path"
path: "/docs/studio/focus-default-props-path"
---

"---\nimage: /generated/articles-docs-studio-focus-default-props-path.png\ntitle: focusDefaultPropsPath()\ncrumb: \"@remotion/studio\"\n---\n\n# focusDefaultPropsPath()<AvailableFrom v=\"4.0.165\"/>\n\nScrolls to a specific field in the default props editor.\n\n## Example\n\nFor the following Zod schema:\n\n```tsx twoslash title=\"schema.ts\"\nimport { z } from \"zod\";\n\nconst MySchema = z.object({\n  array: z.array(\n    z.object({\n      subfield: z.string(),\n    }),\n  ),\n});\n```\n\nCall `focusDefaultPropsPath()` with the path to the field you want to focus on:\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport { focusDefaultPropsPath } from \"@remotion/studio\";\n\nfocusDefaultPropsPath({\n  path: [\"array\", 0, \"subfield\"],\n});\n```\n\n## API\n\n### `path`\n\nThe path to the field you want to focus on. An array containing numbers and strings.\n\n### `scrollBehavior`\n\nThe behavior of the scrolling.  \nOne of `\"auto\" | \"instant\" | \"smooth\"`.  \nDefaults to the [default scroll behavior](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView).\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/focus-default-props-path.ts)\n- [Visual editing](/docs/visual-editing)\n"

Scrolls to a specific field in the default props editor.

## Example[​](#example)

For the following Zod schema:

```

schema.tsimport { z } from "zod";

const MySchema = z.object({
  array: z.array(
    z.object({
      subfield: z.string(),
    }),
  ),
});Copy
```

Call `focusDefaultPropsPath()` with the path to the field you want to focus on:

```

MyComp.tsximport { focusDefaultPropsPath } from "@remotion/studio";

focusDefaultPropsPath({
  path: ["array", 0, "subfield"],
});Copy
```

## API[​](#api)

### `path`[​](#path)

The path to the field you want to focus on. An array containing numbers and strings.

### `scrollBehavior`[​](#scrollbehavior)

The behavior of the scrolling.

One of `"auto" | "instant" | "smooth"`.

Defaults to the [default scroll behavior](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView).

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/focus-default-props-path.ts)

- [Visual editing](/docs/visual-editing)
](/docs/visual-editing)](/docs/visual-editing)
](/docs/visual-editing)
- ](/docs/visual-editing)
- ](/docs/visual-editing)
- ](/docs/visual-editing)
- ](/docs/visual-editing)