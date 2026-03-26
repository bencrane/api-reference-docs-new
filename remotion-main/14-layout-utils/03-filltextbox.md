---
title: "fillTextBox()"
url: "https://www.remotion.dev/docs/layout-utils/fill-text-box"
path: "/docs/layout-utils/fill-text-box"
---

"---\nimage: /generated/articles-docs-layout-utils-fill-text-box.png\ntitle: fillTextBox()\ncrumb: '@remotion/layout-utils'\n---\n\n# fillTextBox()<AvailableFrom v=\"4.0.57\"/>\n\n_Part of the [`@remotion/layout-utils`](/docs/layout-utils) package._\n\nCalculate whether the text exceeds the box and wraps within the container. Only works in the browser, not in Node.js or Bun.\n\n## Example\n\n```tsx twoslash\nimport {fillTextBox} from '@remotion/layout-utils';\n\nconst fontFamily = 'Arial';\nconst fontSize = 12;\n\nconst box = fillTextBox({maxLines: 4, maxBoxWidth: 100});\nbox.add({text: 'Hello', fontFamily, fontSize}); // {exceedsBox: false, newLine: false}\nbox.add({text: 'World!', fontFamily, fontSize}); // {exceedsBox: false, newLine: false}\n// Doesn't fit on the previous line anymore\nbox.add({text: 'How', fontFamily, fontSize}); // {exceedsBox: false, newLine: true}\n// ...\n// Doesn't fix in the box anymore\nbox.add({text: 'the end', fontFamily, fontSize}); // {exceedsBox: true, newLine: false}\n```\n\n## API\n\nThe function takes the following options:\n\n### `maxBoxWidth`\n\n_number_\n\nThe max box width, unit `px`.\n\n### `maxLines`\n\n_number_\n\nThe max lines of the box.\n\n## Return value\n\nAn object with an `add()` method, which can be used to add words to the text box.\n\n### Arguments\n\n#### `text`\n\n_string_\n\nAny string.\n\n#### `fontFamily`\n\n_string_\n\nSame as CSS style `font-family`.\n\n#### `fontSize`\n\n_number_\n\nSame as CSS style `font-size`. Only _numbers_ allowed, unit `px`.\n\n#### `fontWeight`\n\n_string_\n\nSame as CSS style `font-weight`.\n\n#### `fontVariantNumeric`\n\n_string_\n\nSame as CSS style `font-variant-numeric`.\n\n#### `textTransform`<AvailableFrom v=\"4.0.140\"/>\n\n_string_\n\nSame as CSS style `text-transform`.\n\n#### `validateFontIsLoaded?`<AvailableFrom v=\"4.0.136\"/>\n\n_boolean_\n\nIf set to `true`, will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.\n\n#### `additionalStyles?`<AvailableFrom v=\"4.0.140\"/>\n\n_object_\n\nAdditional CSS properties that affect the layout of the text.\n\n### Return value\n\nThe add method returns an object with two properties:\n\n- `exceedsBox`:\n  _Boolean_, whether adding the word would cause the text to exceed the maximum lines of the box.\n- `newLine`:\n  _Boolean_, whether adding the word would require starting a new line in the text box.\n\n## Important considerations\n\nSee [Best practices](/docs/layout-utils/best-practices) to ensure you get correct measurements.\n\n## See also\n\n- [measureText()](/docs/layout-utils/measure-text)\n- [`@remotion/layout-utils`](/docs/layout-utils)\n"

*Part of the [`@remotion/layout-utils`](/docs/layout-utils) package.*

Calculate whether the text exceeds the box and wraps within the container. Only works in the browser, not in Node.js or Bun.

## Example[​](#example)

```
import {fillTextBox} from '@remotion/layout-utils';

const fontFamily = 'Arial';
const fontSize = 12;

const box = fillTextBox({maxLines: 4, maxBoxWidth: 100});
box.add({text: 'Hello', fontFamily, fontSize}); // {exceedsBox: false, newLine: false}
box.add({text: 'World!', fontFamily, fontSize}); // {exceedsBox: false, newLine: false}
// Doesn't fit on the previous line anymore
box.add({text: 'How', fontFamily, fontSize}); // {exceedsBox: false, newLine: true}
// ...
// Doesn't fix in the box anymore
box.add({text: 'the end', fontFamily, fontSize}); // {exceedsBox: true, newLine: false}Copy
```

## API[​](#api)

The function takes the following options:

### `maxBoxWidth`[​](#maxboxwidth)

*number*

The max box width, unit `px`.

### `maxLines`[​](#maxlines)

*number*

The max lines of the box.

## Return value[​](#return-value)

An object with an `add()` method, which can be used to add words to the text box.

### Arguments[​](#arguments)

#### `text`[​](#text)

*string*

Any string.

#### `fontFamily`[​](#fontfamily)

*string*

Same as CSS style `font-family`.

#### `fontSize`[​](#fontsize)

*number*

Same as CSS style `font-size`. Only *numbers* allowed, unit `px`.

#### `fontWeight`[​](#fontweight)

*string*

Same as CSS style `font-weight`.

#### `fontVariantNumeric`[​](#fontvariantnumeric)

*string*

Same as CSS style `font-variant-numeric`.

#### `textTransform`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#texttransform)

*string*

Same as CSS style `text-transform`.

#### `validateFontIsLoaded?`[v4.0.136](https://github.com/remotion-dev/remotion/releases/v4.0.136)[​](#validatefontisloaded)

*boolean*

If set to `true`, will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.

#### `additionalStyles?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#additionalstyles)

*object*

Additional CSS properties that affect the layout of the text.

### Return value[​](#return-value-1)

The add method returns an object with two properties:

- `exceedsBox`:
*Boolean*, whether adding the word would cause the text to exceed the maximum lines of the box.

- `newLine`:
*Boolean*, whether adding the word would require starting a new line in the text box.

## Important considerations[​](#important-considerations)

See [Best practices](/docs/layout-utils/best-practices) to ensure you get correct measurements.

## See also[​](#see-also)

- [measureText()](/docs/layout-utils/measure-text)

- [`@remotion/layout-utils`](/docs/layout-utils)
](/docs/layout-utils)](/docs/layout-utils)
](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)