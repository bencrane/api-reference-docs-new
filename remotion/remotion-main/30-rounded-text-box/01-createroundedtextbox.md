---
title: "createRoundedTextBox()"
url: "https://www.remotion.dev/docs/rounded-text-box/create-rounded-text-box"
path: "/docs/rounded-text-box/create-rounded-text-box"
---

"---\nimage: /generated/articles-docs-rounded-text-box-create-rounded-text-box.png\ntitle: 'createRoundedTextBox()'\ncrumb: '@remotion/rounded-text-box'\n---\n\n_Part of the [`@remotion/rounded-text-box`](/docs/rounded-text-box) package._\n\nCreates a SVG path for rendering a text box with rounded corners, as pioneered by TikTok and Instagram.\n\n<Demo type=\"rounded-text-box\" />\n\nThe above example combines [`fitTextOnNLines()`](/docs/layout-utils/fit-text-on-n-lines) and [`measureText()`](/docs/layout-utils/measure-text) to get the text measurements, and then creates a rounded text box.  \n[View the source code here.](https://github.com/remotion-dev/remotion/blob/main/packages/docs/components/demos/RoundedTextBox.tsx)\n\n## Usage Example\n\n```tsx twoslash title=\"Simple usage example\"\nimport {fitTextOnNLines, measureText} from '@remotion/layout-utils';\nimport {createRoundedTextBox} from '@remotion/rounded-text-box';\n\nconst maxLines = 3;\nconst fontFamily = 'Figtree';\nconst fontWeight = '700';\nconst horizontalPadding = 20;\nconst borderRadius = 20;\nconst fontSize = 36;\nconst lineHeight = 1.5;\nconst textAlign = 'center';\n\nconst lines = ['Hello World', 'This is a test', 'This is another test'];\n\nconst textMeasurements = lines.map((t) =>\n  measureText({\n    text: t,\n    fontFamily,\n    fontSize,\n    additionalStyles: {\n      lineHeight,\n    },\n    fontVariantNumeric: 'normal',\n    fontWeight,\n    letterSpacing: 'normal',\n    textTransform: 'none',\n    validateFontIsLoaded: true,\n  }),\n);\n\nconst {d, boundingBox} = createRoundedTextBox({\n  textMeasurements,\n  textAlign,\n  horizontalPadding,\n  borderRadius,\n});\n\nconst markup = (\n  <div\n    style={{\n      width: boundingBox.width,\n      height: boundingBox.height,\n    }}\n  >\n    <svg\n      viewBox={boundingBox.viewBox}\n      style={{\n        position: 'absolute',\n        width: boundingBox.width,\n        height: boundingBox.height,\n        overflow: 'visible',\n      }}\n    >\n      <path fill=\"white\" d={d} />\n    </svg>\n    <div style={{position: 'relative'}}>\n      {lines.map((line, i) => (\n        <div\n          key={i}\n          style={{\n            fontSize,\n            fontWeight,\n            fontFamily,\n            lineHeight,\n            textAlign,\n            paddingLeft: horizontalPadding,\n            paddingRight: horizontalPadding,\n            color: 'black',\n          }}\n        >\n          {line}\n        </div>\n      ))}\n    </div>\n  </div>\n);\n```\n\n## API\n\n_object_ <TsType type=\"CreateRoundedTextBoxProps\" source=\"@remotion/rounded-text-box\" />\n\nAccepts an object with the following properties:\n\n### `textMeasurements`\n\n_array_ <TsType type=\"Dimensions[]\" source=\"@remotion/layout-utils\" />\n\nAn array of text measurements, each containing the `width` and `height` of a line of text.  \nShould be obtained using the [`measureText()`](/docs/layout-utils/measure-text) function.\n\n### `textAlign`\n\n_string_ <TsType type=\"TextAlign\" source=\"@remotion/rounded-text-box\" />\n\nThe alignment of the text.  \nCan be `'left'`, `'center'`, or `'right'`.\n\n### `horizontalPadding`\n\n_number_\n\nThe horizontal padding of the text box.\n\n### `borderRadius`\n\n_number_\n\nThe border radius of the text box.\n\n## Return value\n\n_object_ <TsType type=\"CreateRoundedTextBoxResult\" source=\"@remotion/rounded-text-box\" />\n\nAn object containing the following properties:\n\n### `d`\n\n_string_\n\nThe SVG path.\n\n### `boundingBox`\n\n_object_ <TsType type=\"BoundingBox\" source=\"@remotion/paths\" />\n\nThe bounding box of the text box. See [`getBoundingBox()`](/docs/paths/get-bounding-box) for the shape.\n\n### `instructions`\n\n_array_ <TsType type=\"ReducedInstruction[]\" source=\"@remotion/paths\" />\n\nThe SVG path instructions as an array, for use with the [`@remotion/paths`](/docs/paths) package.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/rounded-text-box/src/create-rounded-text-box.ts)\n- [`@remotion/rounded-text-box`](/docs/rounded-text-box)\n- [`@remotion/paths`](/docs/paths)\n- [`fitTextOnNLines()`](/docs/layout-utils/fit-text-on-n-lines)\n- [`measureText()`](/docs/layout-utils/measure-text)\n- [`getBoundingBox()`](/docs/paths/get-bounding-box)\n"

*Part of the [`@remotion/rounded-text-box`](/docs/rounded-text-box) package.*

Creates a SVG path for rendering a text box with rounded corners, as pioneered by TikTok and Instagram.

textAlign
leftcenterright
maxLines
`3`
borderRadius
`20`
horizontalPadding
`20`
text

The above example combines [`fitTextOnNLines()`](/docs/layout-utils/fit-text-on-n-lines) and [`measureText()`](/docs/layout-utils/measure-text) to get the text measurements, and then creates a rounded text box.

[View the source code here.](https://github.com/remotion-dev/remotion/blob/main/packages/docs/components/demos/RoundedTextBox.tsx)

## Usage Example[​](#usage-example)

```

Simple usage exampleimport {fitTextOnNLines, measureText} from '@remotion/layout-utils';
import {createRoundedTextBox} from '@remotion/rounded-text-box';

const maxLines = 3;
const fontFamily = 'Figtree';
const fontWeight = '700';
const horizontalPadding = 20;
const borderRadius = 20;
const fontSize = 36;
const lineHeight = 1.5;
const textAlign = 'center';

const lines = ['Hello World', 'This is a test', 'This is another test'];

const textMeasurements = lines.map((t) =>
  measureText({
    text: t,
    fontFamily,
    fontSize,
    additionalStyles: {
      lineHeight,
    },
    fontVariantNumeric: 'normal',
    fontWeight,
    letterSpacing: 'normal',
    textTransform: 'none',
    validateFontIsLoaded: true,
  }),
);

const {d, boundingBox} = createRoundedTextBox({
  textMeasurements,
  textAlign,
  horizontalPadding,
  borderRadius,
});

const markup = (
  <div
    style={{
      width: boundingBox.width,
      height: boundingBox.height,
    }}
  >
    <svg
      viewBox={boundingBox.viewBox}
      style={{
        position: 'absolute',
        width: boundingBox.width,
        height: boundingBox.height,
        overflow: 'visible',
      }}
    >
      <path fill="white" d={d} />
    </svg>
    <div style={{position: 'relative'}}>
      {lines.map((line, i) => (
        <div
          key={i}
          style={{
            fontSize,
            fontWeight,
            fontFamily,
            lineHeight,
            textAlign,
            paddingLeft: horizontalPadding,
            paddingRight: horizontalPadding,
            color: 'black',
          }}
        >
          {line}
        </div>
      ))}
    </div>
  </div>
);Copy
```

## API[​](#api)

*object* `CreateRoundedTextBoxProps`

Accepts an object with the following properties:

### `textMeasurements`[​](#textmeasurements)

*array* `Dimensions[]`

An array of text measurements, each containing the `width` and `height` of a line of text.

Should be obtained using the [`measureText()`](/docs/layout-utils/measure-text) function.

### `textAlign`[​](#textalign)

*string* `TextAlign`

The alignment of the text.

Can be `'left'`, `'center'`, or `'right'`.

### `horizontalPadding`[​](#horizontalpadding)

*number*

The horizontal padding of the text box.

### `borderRadius`[​](#borderradius)

*number*

The border radius of the text box.

## Return value[​](#return-value)

*object* `CreateRoundedTextBoxResult`

An object containing the following properties:

### `d`[​](#d)

*string*

The SVG path.

### `boundingBox`[​](#boundingbox)

*object* `BoundingBox`

The bounding box of the text box. See [`getBoundingBox()`](/docs/paths/get-bounding-box) for the shape.

### `instructions`[​](#instructions)

*array* `ReducedInstruction[]`

The SVG path instructions as an array, for use with the [`@remotion/paths`](/docs/paths) package.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/rounded-text-box/src/create-rounded-text-box.ts)

- [`@remotion/rounded-text-box`](/docs/rounded-text-box)

- [`@remotion/paths`](/docs/paths)

- [`fitTextOnNLines()`](/docs/layout-utils/fit-text-on-n-lines)

- [`measureText()`](/docs/layout-utils/measure-text)

- [`getBoundingBox()`](/docs/paths/get-bounding-box)
](/docs/paths/get-bounding-box)](/docs/paths/get-bounding-box)
](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)
- ](/docs/paths/get-bounding-box)