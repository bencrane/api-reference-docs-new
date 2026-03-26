---
title: "measureText()"
url: "https://www.remotion.dev/docs/layout-utils/measure-text"
path: "/docs/layout-utils/measure-text"
---

"---\nimage: /generated/articles-docs-layout-utils-measure-text.png\ntitle: measureText()\ncrumb: '@remotion/layout-utils'\n---\n\n_Part of the [`@remotion/layout-utils`](/docs/layout-utils) package._\n\nCalculates the width and height of specified text to be used for layout calculations. Only works in the browser, not in Node.js or Bun.\n\n## Example\n\n```tsx twoslash\nimport {measureText} from '@remotion/layout-utils';\n\nconst text = 'remotion';\nconst fontFamily = 'Arial';\nconst fontWeight = '500';\nconst fontSize = 12;\nconst letterSpacing = '1px';\n\nmeasureText({\n  text,\n  fontFamily,\n  fontWeight,\n  fontSize,\n  letterSpacing,\n}); // { height: 14, width: 20 }\n```\n\n## API\n\nThis function has a cache. If there are two duplicate arguments inputs, the second one will return the first result without repeating the calculation.\n\nThe function takes the following options:\n\n### `text`\n\n_string_\n\nAny string.\n\n### `fontFamily`\n\n_string_\n\nSame as CSS style `font-family`\n\n### `fontSize`\n\n_number_ / _string_\n\nSame as CSS style `font-size`. Since v4.0.125, strings are allowed too, before only numbers.\n\n### `fontWeight`\n\n_string_\n\nSame as CSS style `font-weight`\n\n### `letterSpacing`\n\n_string_\n\nSame as CSS style `letter-spacing`.\n\n### `fontVariantNumeric`<AvailableFrom v=\"4.0.57\"/>\n\n_string_\n\nSame as CSS style `font-variant-numeric`.\n\n### `textTransform`<AvailableFrom v=\"4.0.140\"/>\n\n_string_\n\nSame as CSS style `text-transform`.\n\n### `validateFontIsLoaded?`<AvailableFrom v=\"4.0.136\"/>\n\n_boolean_\n\nIf set to `true`, will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.\n\n### `additionalStyles?`<AvailableFrom v=\"4.0.140\"/>\n\n_object_\n\nAdditional CSS properties that affect the layout of the text.\n\n## Return value\n\nAn object with `height` and `width`\n\n## Important considerations\n\nSee [Best practices](/docs/layout-utils/best-practices) to ensure you get correct measurements.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/layout-utils/src/layouts/measure-text.ts)\n- [`@remotion/layout-utils`](/docs/layout-utils)\n"

*Part of the [`@remotion/layout-utils`](/docs/layout-utils) package.*

Calculates the width and height of specified text to be used for layout calculations. Only works in the browser, not in Node.js or Bun.

## Example[​](#example)

```
import {measureText} from '@remotion/layout-utils';

const text = 'remotion';
const fontFamily = 'Arial';
const fontWeight = '500';
const fontSize = 12;
const letterSpacing = '1px';

measureText({
  text,
  fontFamily,
  fontWeight,
  fontSize,
  letterSpacing,
}); // { height: 14, width: 20 }Copy
```

## API[​](#api)

This function has a cache. If there are two duplicate arguments inputs, the second one will return the first result without repeating the calculation.

The function takes the following options:

### `text`[​](#text)

*string*

Any string.

### `fontFamily`[​](#fontfamily)

*string*

Same as CSS style `font-family`

### `fontSize`[​](#fontsize)

*number* / *string*

Same as CSS style `font-size`. Since v4.0.125, strings are allowed too, before only numbers.

### `fontWeight`[​](#fontweight)

*string*

Same as CSS style `font-weight`

### `letterSpacing`[​](#letterspacing)

*string*

Same as CSS style `letter-spacing`.

### `fontVariantNumeric`[v4.0.57](https://github.com/remotion-dev/remotion/releases/v4.0.57)[​](#fontvariantnumeric)

*string*

Same as CSS style `font-variant-numeric`.

### `textTransform`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#texttransform)

*string*

Same as CSS style `text-transform`.

### `validateFontIsLoaded?`[v4.0.136](https://github.com/remotion-dev/remotion/releases/v4.0.136)[​](#validatefontisloaded)

*boolean*

If set to `true`, will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.

### `additionalStyles?`[v4.0.140](https://github.com/remotion-dev/remotion/releases/v4.0.140)[​](#additionalstyles)

*object*

Additional CSS properties that affect the layout of the text.

## Return value[​](#return-value)

An object with `height` and `width`

## Important considerations[​](#important-considerations)

See [Best practices](/docs/layout-utils/best-practices) to ensure you get correct measurements.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/layout-utils/src/layouts/measure-text.ts)

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
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)
- ](/docs/layout-utils)