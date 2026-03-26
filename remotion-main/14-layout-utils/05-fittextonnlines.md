---
title: "fitTextOnNLines()"
url: "https://www.remotion.dev/docs/layout-utils/fit-text-on-n-lines"
path: "/docs/layout-utils/fit-text-on-n-lines"
---

"---\nimage: /generated/articles-docs-layout-utils-fit-text-on-n-lines.png\ntitle: fitTextOnNLines()\ncrumb: '@remotion/layout-utils'\n---\n\n_Part of the [`@remotion/layout-utils`](/docs/layout-utils) package. Available from v4.0.313_\n\nCalculates the `fontSize` needed to fit a text into a given width while respecting a maximum number of lines. Optionally, you can specify a maximum font size, and see how the text is split into lines.\n\n```tsx twoslash title=\"FitTextOnNLines.tsx\"\nimport {fitTextOnNLines} from '@remotion/layout-utils';\n\nconst text = 'Hello World';\nconst width = 100;\nconst maxLines = 2;\nconst fontFamily = 'Arial';\nconst fontWeight = 'bold';\n\nconst {fontSize, lines} = fitTextOnNLines({\n  text,\n  maxBoxWidth: width,\n  maxLines,\n  fontFamily: fontFamily,\n  fontWeight: fontWeight,\n  textTransform: 'uppercase',\n  maxFontSize: 80,\n});\n\n// Example markup:\n<div\n  style={{\n    fontSize,\n    width,\n    fontFamily,\n    fontWeight,\n    textTransform: 'uppercase',\n  }}\n>\n  {text}\n</div>;\n```\n\n## API\n\nAccepts an object with the following properties:\n\n### `text`\n\n_string_\n\nThe text to fit.\n\n### `maxBoxWidth`\n\n_number_\n\nThe maximum width the text should fit into.\n\n:::info\nIn the default Remotion stylesheet, borders shrink the container due to `box-sizing: border-box`.  \nSubtract any borders, or use `outline` instead of `border`.\n:::\n\n### `maxLines`\n\n_number_\n\nThe maximum number of lines the text should be distributed across.\n\n### `fontFamily`\n\n_string_\n\nThe `font-family` CSS property you are going to assign to the text.\n\n:::info\nThe font needs to be loaded before this API is being called.  \nIf you use [`@remotion/google-fonts`](/docs/google-fonts), wait until [`waitUntilDone()`](/docs/google-fonts/load-font#waituntildone) resolves first.\n:::\n\n### `fontWeight?`\n\n_string | number_\n\nPass this option if you are going to assign a `font-weight` CSS property to the text.\n\n### `letterSpacing?`\n\n_string_\n\nPass this option if you are going to assign a `letter-spacing` CSS property to the text.\n\n### `fontVariantNumeric?`\n\n_string_\n\nPass this option if you are going to assign a `font-variant-numeric` CSS property to the text.\n\n### `textTransform`\n\n_string_\n\nSame as CSS style `text-transform`.\n\n### `validateFontIsLoaded?`\n\n_boolean_\n\nIf set to `true`, will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.\n\n### `additionalStyles?`\n\n_object_\n\nAdditional CSS properties that affect the layout of the text.\n\n### `maxFontSize?`\n\n_number_\n\nThe maximum font size (in pixels) that the text is allowed to reach. If not specified, defaults to 2000.\n\n## Return value\n\nAn object with the following properties:\n\n### `fontSize`\n\n_number_\n\nThe calculated font size in pixels. Assign this to the `style` prop of your text element.\n\n### `lines`\n\n_string[]_\n\nAn array of strings, each representing a line of text at the calculated font size. Useful for rendering or debugging how the text is split.\n\n## Example\n\n```tsx twoslash\nimport {fitTextOnNLines} from '@remotion/layout-utils';\nimport React from 'react';\nimport {AbsoluteFill} from 'remotion';\n\nconst boxWidth = 600;\nconst maxLines = 2;\n// Must be loaded before calling fitTextOnNLines()\nconst fontFamily = 'Helvetica';\nconst fontWeight = 'bold';\n\nexport const FitTextOnNLines: React.FC<{text: string}> = ({text}) => {\n  const {fontSize, lines} = fitTextOnNLines({\n    fontFamily,\n    text,\n    maxBoxWidth: boxWidth,\n    maxLines,\n    fontWeight,\n    maxFontSize: 80,\n  });\n\n  return (\n    <AbsoluteFill\n      style={{\n        justifyContent: 'center',\n        alignItems: 'center',\n        backgroundColor: 'white',\n      }}\n    >\n      <div\n        style={{\n          width: boxWidth,\n          outline: '1px dashed rgba(0, 0, 0, 0.5)',\n          height: 100,\n          fontSize,\n          fontWeight,\n          fontFamily,\n          display: 'flex',\n          alignItems: 'center',\n        }}\n      >\n        {text}\n      </div>\n    </AbsoluteFill>\n  );\n};\n```\n\nNotes:\n\n- A maximum font size of `80` was specified to prevent the text from becoming too large.\n- The `fontFamily` and `fontWeight` were passed to the `div` element to ensure that the text is rendered with the same font as the one used by `fitTextOnNLines()`.\n- The `outline` CSS property was used instead of `border`.  \n  This is because in Remotion, the border is inside by default and shrinks the container, due to `box-sizing: border-box` being in the default stylesheet.\n- The `lines` property in the return value shows how the text is split into lines at the calculated font size. This can be useful for rendering or debugging.\n- The `maxFontSize` property allows you to limit the font size if you don't want the text to become too large.\n\n## Important considerations\n\nSee [Best practices](/docs/layout-utils/best-practices) to ensure you get correct measurements.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/layout-utils/src/layouts/fit-text-on-n-lines.ts)\n- [`@remotion/layout-utils`](/docs/layout-utils)\n"

*Part of the [`@remotion/layout-utils`](/docs/layout-utils) package. Available from v4.0.313*

Calculates the `fontSize` needed to fit a text into a given width while respecting a maximum number of lines. Optionally, you can specify a maximum font size, and see how the text is split into lines.

```

FitTextOnNLines.tsximport {fitTextOnNLines} from '@remotion/layout-utils';

const text = 'Hello World';
const width = 100;
const maxLines = 2;
const fontFamily = 'Arial';
const fontWeight = 'bold';

const {fontSize, lines} = fitTextOnNLines({
  text,
  maxBoxWidth: width,
  maxLines,
  fontFamily: fontFamily,
  fontWeight: fontWeight,
  textTransform: 'uppercase',
  maxFontSize: 80,
});

// Example markup:
<div
  style={{
    fontSize,
    width,
    fontFamily,
    fontWeight,
    textTransform: 'uppercase',
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

### `maxBoxWidth`[​](#maxboxwidth)

*number*

The maximum width the text should fit into.
](#maxboxwidth)](#maxboxwidth)
](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)
- ](#maxboxwidth)