---
title: "Debugging"
url: "https://www.remotion.dev/docs/layout-utils/debug"
path: "/docs/layout-utils/debug"
---

"---\nimage: /generated/articles-docs-layout-utils-debug.png\ntitle: Debugging font measurement bugs\nsidebar_label: Debugging\ncrumb: '@remotion/layout-utils'\nno_ai: true\n---\n\nWhen you find that the measurements that you are getting from [`measureText()`](/docs/layout-utils/measure-text), [`fillTextBox()`](/docs/layout-utils/fill-text-box) or [`fitText()`](/docs/layout-utils/fit-text) are off and are causing layout issues, follow the debugging instructions on this page.\n\n<Step>1</Step> Open your project in the Remotion Studio and select the\ncomposition in which you observe the issue.<br/>\n<Step>2</Step> Set the zoom to 100% to rule out any issues that arise from the\nzoom level.<br/>\n<Step>3</Step>Render at the bottom of your component a `<div>` that contains the string and all the properties that you passed to [`measureText()`](/docs/layout-utils/measure-text).\n\n```tsx twoslash title=\"Sample markup\"\nimport {AbsoluteFill} from 'remotion';\n\nconst MyComp: React.FC = () => {\n  const fontSize = 100;\n  const fontWeight = 'bold';\n  const fontFamily = 'Roboto';\n  const text = 'Hello World ';\n  const letterSpacing = undefined;\n  const fontVariantNumeric = undefined;\n  const textTransform = undefined;\n\n  return (\n    <AbsoluteFill>\n      <div\n        id=\"remotion-measurer\"\n        style={{\n          display: 'inline-block',\n          whiteSpace: 'pre',\n          fontSize,\n          fontWeight,\n          fontFamily,\n          letterSpacing,\n          fontVariantNumeric,\n          textTransform,\n        }}\n      >\n        {text}\n      </div>\n    </AbsoluteFill>\n  );\n};\n```\n\n<Step>4</Step> Open the Chrome DevTools and select the `<div id=\"remotion-measurer\">` node in the \"Elements\" tab.<br/>\n<Step>5</Step> The node lights up, and you can see its measurements. See if there are any unexpected deviations.<br/>\n<Step>6</Step> Use the \"Computed\" tabs and go through all properties that may affect the layout, and compare them with the node in your composition that is causing issue. If the measurements are different, there will be at least 1 computed proeprty that has a different value.<br/>\n<Step>7</Step> Align your markup so that it has the same computed properties as the node in your composition.<br/>\n\n## Remember\n\n- The text gets measured with `whiteSpace: \"pre\"`, which includes whitespace.\n  - If you don't want to measure whitespace. call `.trim()` on your string.\n  - Make sure `whiteSpace: \"pre\"` is applied to your whole container, not just the individual words.\n  - Make sure you don't remove any whitespace while splitting your text that you leave in while measuring.\n- Make sure the font is loaded when you are calling `measureText()`.\n  - Use the `validateFontIsLoaded` option to ensure the font is loaded.\n- External styles may apply. See if you have CSS Resets, TailwindCSS stylesheets or other external resources messing up your layout.\n  - If this is the case, you can see it in the Computed Properties panel in the Chrome Dev Tools.\n- Don't use `padding` or `border` on your text. Use `outline` instead of `border`.\n- Don't multiply the font size with [`useCurrentScale()`](/docs/use-current-scale). It will lead to a broken layout.\n\n## See also\n\nYou can also check out the source code of `measureText()`, paste and customize it in your project to aid debugging.\n\n- [Source code for `measureText()`](https://github.com/remotion-dev/remotion/blob/main/packages/layout-utils/src/layouts/measure-text.ts)\n- [Best practices](/docs/layout-utils/best-practices)\n"

When you find that the measurements that you are getting from [`measureText()`](/docs/layout-utils/measure-text), [`fillTextBox()`](/docs/layout-utils/fill-text-box) or [`fitText()`](/docs/layout-utils/fit-text) are off and are causing layout issues, follow the debugging instructions on this page.

[](#1)
[1](#1)[ ](#1) Open your project in the Remotion Studio and select the
composition in which you observe the issue.

[
2 ](#2) Set the zoom to 100% to rule out any issues that arise from the
zoom level.

[
3 ](#3)Render at the bottom of your component a `<div>` that contains the string and all the properties that you passed to [`measureText()`](/docs/layout-utils/measure-text).

```

Sample markupimport {AbsoluteFill} from 'remotion';

const MyComp: React.FC = () => {
  const fontSize = 100;
  const fontWeight = 'bold';
  const fontFamily = 'Roboto';
  const text = 'Hello World ';
  const letterSpacing = undefined;
  const fontVariantNumeric = undefined;
  const textTransform = undefined;

  return (
    <AbsoluteFill>
      <div
        id="remotion-measurer"
        style={{
          display: 'inline-block',
          whiteSpace: 'pre',
          fontSize,
          fontWeight,
          fontFamily,
          letterSpacing,
          fontVariantNumeric,
          textTransform,
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};Copy
```

[](#4)
[4](#4)[ ](#4) Open the Chrome DevTools and select the `<div id="remotion-measurer">` node in the "Elements" tab.

[
5 ](#5) The node lights up, and you can see its measurements. See if there are any unexpected deviations.

[
6 ](#6) Use the "Computed" tabs and go through all properties that may affect the layout, and compare them with the node in your composition that is causing issue. If the measurements are different, there will be at least 1 computed proeprty that has a different value.

[
7 ](#7) Align your markup so that it has the same computed properties as the node in your composition.

## Remember[​](#remember)

- The text gets measured with `whiteSpace: "pre"`, which includes whitespace.

- If you don't want to measure whitespace. call `.trim()` on your string.

- Make sure `whiteSpace: "pre"` is applied to your whole container, not just the individual words.

- Make sure you don't remove any whitespace while splitting your text that you leave in while measuring.

- Make sure the font is loaded when you are calling `measureText()`.

- Use the `validateFontIsLoaded` option to ensure the font is loaded.

- External styles may apply. See if you have CSS Resets, TailwindCSS stylesheets or other external resources messing up your layout.

- If this is the case, you can see it in the Computed Properties panel in the Chrome Dev Tools.

- Don't use `padding` or `border` on your text. Use `outline` instead of `border`.

- Don't multiply the font size with [`useCurrentScale()`](/docs/use-current-scale). It will lead to a broken layout.

## See also[​](#see-also)

You can also check out the source code of `measureText()`, paste and customize it in your project to aid debugging.

- [Source code for `measureText()`](https://github.com/remotion-dev/remotion/blob/main/packages/layout-utils/src/layouts/measure-text.ts)

- [Best practices](/docs/layout-utils/best-practices)
](/docs/layout-utils/best-practices)](/docs/layout-utils/best-practices)
](/docs/layout-utils/best-practices)
- ](/docs/layout-utils/best-practices)