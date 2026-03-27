---
title: "fitText()"
url: "https://www.remotion.dev/docs/layout-utils/fit-text"
path: "/docs/layout-utils/fit-text"
---

"---\nimage: /generated/articles-docs-layout-utils-fit-text.png\ntitle: fitText()\ncrumb: \"@remotion/layout-utils\"\n---\n\n_Part of the [`@remotion/layout-utils`](/docs/layout-utils) package. Available from v4.0.88_\n\nCalculates the `font-size` needed to fit a text into a given width.\n\n```tsx twoslash title=\"FitText.tsx\"\nimport { fitText } from \"@remotion/layout-utils\";\n\nconst text = \"Hello World\";\nconst width = 100;\nconst fontFamily = \"Arial\";\nconst fontWeight = \"bold\";\n\nconst { fontSize } = fitText({\n  text,\n  withinWidth: width,\n  fontFamily: fontFamily,\n  fontWeight: fontWeight,\n  textTransform: \"uppercase\",\n});\n\n// Example markup:\n<div\n  style={{\n    fontSize,\n    width,\n    fontFamily,\n    fontWeight,\n    textTransform: \"uppercase\",\n  }}\n>\n  {text}\n</div>;\n```\n\n## API\n\nAccepts an object with the following properties:\n\n### `text`\n\n_string_\n\nThe text to fit.\n\n### `withinWidth`\n\n_number_\n\nThe width to fit the text into.\n\n:::info\nIn the default Remotion stylesheet, borders shrink the container due to `box-sizing: border-box`.  \nSubtract any borders, or use `outline` instead of `border`.\n:::\n\n### `fontFamily`\n\n_string_\n\nThe `font-family` CSS property you are going to assign to the text.\n\n:::info\nThe font needs to be loaded before this API is being called.  \nIf you use [`@remotion/google-fonts`](/docs/google-fonts), wait until [`waitUntilDone()`](/docs/google-fonts/load-font#waituntildone) resolves first.\n:::\n\n### `fontWeight?`\n\n_string | number_\n\nPass this option if you are going to assign a `font-weight` CSS property to the text.\n\n### `letterSpacing?`\n\n_string_\n\nPass this option if you are going to assign a `letter-spacing` CSS property to the text.\n\n### `fontVariantNumeric?`\n\n_string_\n\nPass this option if you are going to assign a `font-variant-numeric` CSS property to the text.\n\n### `textTransform`<AvailableFrom v=\"4.0.140\"/>\n\n_string_\n\nSame as CSS style `text-transform`.\n\n### `validateFontIsLoaded?`<AvailableFrom v=\"4.0.136\"/>\n\n_boolean_\n\nIf set to `true`, will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.\n\n### `additionalStyles?`<AvailableFrom v=\"4.0.140\"/>\n\n_object_\n\nAdditional CSS properties that affect the layout of the text.\n\n## Return value\n\nAn object with `fontSize` in pixels. Assign this to the `style` prop of your text element.\n\n## Example\n\n```tsx twoslash\nimport { fitText } from \"@remotion/layout-utils\";\nimport React from \"react\";\nimport { AbsoluteFill } from \"remotion\";\n\nconst boxWidth = 600;\n// Must be loaded before calling fitText()\nconst fontFamily = \"Helvetica\";\nconst fontWeight = \"bold\";\n\nexport const FitText: React.FC<{ text: string }> = ({ text }) => {\n  const fontSize = Math.min(\n    80,\n    fitText({\n      fontFamily,\n      text,\n      withinWidth: boxWidth,\n      fontWeight,\n    }).fontSize,\n  );\n\n  return (\n    <AbsoluteFill\n      style={{\n        justifyContent: \"center\",\n        alignItems: \"center\",\n        backgroundColor: \"white\",\n      }}\n    >\n      <div\n        style={{\n          width: boxWidth,\n          outline: \"1px dashed rgba(0, 0, 0, 0.5)\",\n          height: 100,\n          fontSize,\n          fontWeight,\n          fontFamily,\n          display: \"flex\",\n          alignItems: \"center\",\n        }}\n      >\n        {text}\n      </div>\n    </AbsoluteFill>\n  );\n};\n```\n\nNotes:\n\n- A maximum font size of `80` was specified to prevent the text from becoming too large.\n- The `fontFamily` and `fontWeight` were passed to the `div` element to ensure that the text is rendered with the same font as the one used by `fitText()`.\n- The `outline` CSS property was used instead of `border`.  \n  This is because in Remotion, the border is inside by default and shrinks the container, due to `box-sizing: border-box` being in the default stylesheet.\n\n## Important considerations\n\nSee [Best practices](/docs/layout-utils/best-practices) to ensure you get correct measurements.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/layout-utils/src/layouts/fit-text.ts)\n- [`@remotion/layout-utils`](/docs/layout-utils)\n- [`@remotion/google-fonts`](/docs/google-fonts)\n"

*Part of the [`@remotion/layout-utils`](/docs/layout-utils) package. Available from v4.0.88*

Calculates the `font-size` needed to fit a text into a given width.

```

FitText.tsximport { fitText } from "@remotion/layout-utils";

const text = "Hello World";
const width = 100;
const fontFamily = "Arial";
const fontWeight = "bold";

const { fontSize } = fitText({
  text,
  withinWidth: width,
  fontFamily: fontFamily,
  fontWeight: fontWeight,
  textTransform: "uppercase",
});

// Example markup:
<div
  style={{
    fontSize,
    width,
    fontFamily,
    fontWeight,
    textTransform: "uppercase",
  }}
>
  {text}
</div>;Copy
```

## API[​](#api)

Accepts an object with the following properties:

### `text`[​](#text)

*string*

The text to fit.

### `withinWidth`[​](#withinwidth)

*number*

The width to fit the text into.
](#withinwidth)](#withinwidth)
](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)
- ](#withinwidth)