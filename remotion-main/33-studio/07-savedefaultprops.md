---
title: "saveDefaultProps()"
url: "https://www.remotion.dev/docs/studio/save-default-props"
path: "/docs/studio/save-default-props"
---

"---\nimage: /generated/articles-docs-studio-save-default-props.png\ntitle: saveDefaultProps()\ncrumb: \"@remotion/studio\"\n---\n\n# saveDefaultProps()<AvailableFrom v=\"4.0.147\"/>\n\nSaves the [`defaultProps`](/docs/composition) for a [composition](/docs/terminology/composition) back to the [root file](/docs/terminology/root-file).\n[`updateDefaultProps()`](/docs/studio/update-default-props) is an alias for this function.\n\n## Examples\n\n```tsx twoslash title=\"Saving {color: 'green'} to Root.tsx\"\n// @target: esnext\nimport { saveDefaultProps } from \"@remotion/studio\";\n\nawait saveDefaultProps({\n  compositionId: \"my-composition\",\n  defaultProps: () => {\n    return {\n      color: \"green\",\n    };\n  },\n});\n```\n\nYou can access the saved default props to only override part of it (reducer-style):\n\n```tsx twoslash title=\"Accessing the saved default props\"\n// @target: esnext\nimport { saveDefaultProps } from \"@remotion/studio\";\n\nawait saveDefaultProps({\n  compositionId: \"my-composition\",\n  defaultProps: ({ savedDefaultProps }) => {\n    return {\n      ...savedDefaultProps,\n      color: \"green\",\n    };\n  },\n});\n```\n\nIf you have a Zod schema, you can also access its runtime value:\n\n```tsx twoslash title=\"Accessing the Zod schema\"\n// @target: esnext\nimport { saveDefaultProps } from \"@remotion/studio\";\n\nawait saveDefaultProps({\n  compositionId: \"my-composition\",\n  defaultProps: ({ schema, savedDefaultProps }) => {\n    // Do something with the Zod schema\n\n    return {\n      ...savedDefaultProps,\n      color: \"red\",\n    };\n  },\n});\n```\n\n## `unsavedDefaultProps`\n\n:::info\nBefore v4.0.437, the Props Editor had a concept of \"unsaved props\" that were not yet written back to the root file.\nStarting from v4.0.437, all prop changes are immediately saved, so `unsavedDefaultProps` is now always the same as `savedDefaultProps`.\n\nIt is still accepted for backwards compatibility, but you should use `savedDefaultProps` instead.\n:::\n\n## Requirements\n\nIn order to use this function:\n\n<Step>1</Step> You need to be inside the Remotion Studio.\n<br />\n<Step>2</Step> The Studio must be running (no static deployment)\n<br />\n<Step>3</Step> <code>zod</code> needs to be installed.\n<br />\n<br />\n\nOtherwise, the function will throw.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/save-default-props.ts)\n"

Saves the [`defaultProps`](/docs/composition) for a [composition](/docs/terminology/composition) back to the [root file](/docs/terminology/root-file).
[`updateDefaultProps()`](/docs/studio/update-default-props) is an alias for this function.

## Examples[​](#examples)

```

Saving {color: 'green'} to Root.tsximport { saveDefaultProps } from "@remotion/studio";

await saveDefaultProps({
  compositionId: "my-composition",
  defaultProps: () => {
    return {
      color: "green",
    };
  },
});Copy
```

You can access the saved default props to only override part of it (reducer-style):

```

Accessing the saved default propsimport { saveDefaultProps } from "@remotion/studio";

await saveDefaultProps({
  compositionId: "my-composition",
  defaultProps: ({ savedDefaultProps }) => {
    return {
      ...savedDefaultProps,
      color: "green",
    };
  },
});Copy
```

If you have a Zod schema, you can also access its runtime value:

```

Accessing the Zod schemaimport { saveDefaultProps } from "@remotion/studio";

await saveDefaultProps({
  compositionId: "my-composition",
  defaultProps: ({ schema, savedDefaultProps }) => {
    // Do something with the Zod schema

    return {
      ...savedDefaultProps,
      color: "red",
    };
  },
});Copy
```

## `unsavedDefaultProps`[​](#unsaveddefaultprops)

](#unsaveddefaultprops)](#unsaveddefaultprops)
](#unsaveddefaultprops)
- ](#unsaveddefaultprops)
- ](#unsaveddefaultprops)
- ](#unsaveddefaultprops)