---
title: "Best practices"
url: "https://www.remotion.dev/docs/layout-utils/best-practices"
path: "/docs/layout-utils/best-practices"
---

"---\nimage: /generated/articles-docs-layout-utils-best-practices.png\ntitle: Best practices for @remotion/layout-utils\nsidebar_label: Best practices\ncrumb: '@remotion/layout-utils'\n---\n\nTake note of the following points to ensure correct measurements when using the [`@remotion/layout-utils`](/docs/layout-utils) package.\n\nThese tips apply to all of [`measureText()`](/docs/layout-utils/measure-text), [`fitText()`](/docs/layout-utils/fit-text), and [`fillTextBox()`](/docs/layout-utils/fill-text-box).\n\n## Wait until the font is loaded\n\nOnly call [`measureText()`](/docs/layout-utils/measure-text) after the font is loaded. This applies to Google Fonts (example below) or any other font loading mechanism.\n\nIf you only need this in one component, using `waitUntilDone()` in a `useEffect()` is fine.\n\n### Example with `useEffect`\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {useState, useEffect} from 'react';\nimport {Dimensions, measureText} from '@remotion/layout-utils';\nimport {loadFont, fontFamily} from '@remotion/google-fonts/Inter';\n\nconst {waitUntilDone} = loadFont('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n\nconst MyComp: React.FC = () => {\n  const [dimensions, setDimensions] = useState<Dimensions | null>(null);\n\n  useEffect(() => {\n    // Wait until the font is loaded before measuring text\n    waitUntilDone().then(() => {\n      const measurement = measureText({\n        fontFamily: fontFamily,\n        fontSize: 14,\n        fontWeight: '400',\n        text: 'Hello world',\n      });\n\n      // We don't need to use delayRender() here, because\n      // font loading from @remotion/google-fonts is already wrapped in it\n      setDimensions(measurement);\n    });\n  }, []);\n\n  return null;\n};\n```\n\n### Example with high-order component\n\nFor larger projects, this pattern keeps the code clean by exposing a higher-order component that only mounts children once fonts are loaded.\n\nThe following logic is borrowed from the [Remotion Recorder](/docs/recorder).\n\nA file is defined which loads some fonts:\n\n```tsx twoslash title=\"fonts.ts\"\nimport {fontFamily as regularFont, loadFont as loadRegular} from '@remotion/google-fonts/Inter';\n\nimport {fontFamily as monospaceFont, loadFont as loadMonospace} from '@remotion/google-fonts/RobotoMono';\n\nimport {cancelRender, continueRender, delayRender} from 'remotion';\n\nconst regular = loadRegular('normal', {\n  weights: ['400', '700'],\n  subsets: ['latin'],\n});\nconst monospace = loadMonospace('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n\nexport const waitForFonts = async () => {\n  await regular.waitUntilDone();\n  await monospace.waitUntilDone();\n};\n\nconst delay = delayRender('Loading fonts');\n\nwaitForFonts()\n  .then(() => continueRender(delay))\n  .catch((err) => cancelRender(err));\n```\n\nThen a higher-order component is defined which only renders its children when the font is loaded:\n\n```tsx twoslash title=\"WaitForFonts.tsx\"\n// @filename: fonts.ts\nimport {fontFamily as regularFont, loadFont as loadRegular} from '@remotion/google-fonts/Inter';\n\nimport {fontFamily as monospaceFont, loadFont as loadMonospace} from '@remotion/google-fonts/RobotoMono';\n\nimport {cancelRender, continueRender, delayRender} from 'remotion';\n\nexport const regular = loadRegular('normal', {\n  weights: ['400', '700'],\n  subsets: ['latin'],\n});\nconst monospace = loadMonospace('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n\nexport const waitForFonts = async () => {\n  await regular.waitUntilDone();\n  await monospace.waitUntilDone();\n};\n\nconst delay = delayRender('Loading fonts');\n\nwaitForFonts()\n  .then(() => continueRender(delay))\n  .catch((err) => cancelRender(err));\n\n// @filename: WaitForFonts.tsx\n// ---cut---\nimport React, {useEffect, useState} from 'react';\nimport {cancelRender, continueRender, useDelayRender} from 'remotion';\nimport {waitForFonts} from './fonts';\n\nexport const WaitForFonts: React.FC<{\n  children: React.ReactNode;\n}> = ({children}) => {\n  const [fontsLoaded, setFontsLoaded] = useState(false);\n  const {delayRender, continueRender} = useDelayRender();\n  const [handle] = useState(() => delayRender('Waiting for fonts to be loaded'));\n\n  useEffect(() => {\n    if (fontsLoaded) {\n      return;\n    }\n\n    waitForFonts()\n      .then(() => {\n        setFontsLoaded(true);\n      })\n      .catch((err) => {\n        cancelRender(err);\n      });\n  }, [fontsLoaded, handle, continueRender, delayRender]);\n\n  useEffect(() => {\n    if (fontsLoaded) {\n      continueRender(handle);\n    }\n  }, [continueRender, fontsLoaded, handle]);\n\n  if (!fontsLoaded) {\n    return null;\n  }\n\n  return <>{children}</>;\n};\n```\n\nThen the component can wrap any other component that calls text measurement APIs:\n\n```tsx twoslash title=\"MyComp.tsx\"\n// @filename: fonts.ts\nexport const regular = 'Inter';\n\n// @filename: WaitForFonts.tsx\nexport const WaitForFonts: React.FC<{\n  children: React.ReactNode;\n}> = ({children}) => {\n  // ...\n  return children;\n};\n\n// @filename: MyComp.tsx\n// ---cut---\nimport React from 'react';\nimport {regular} from './fonts';\nimport {WaitForFonts} from './WaitForFonts';\nimport {measureText} from '@remotion/layout-utils';\n\nconst MyCompInner: React.FC = () => {\n  // Safe to call measureText() here\n  const measurement = measureText({\n    fontFamily: regular,\n    fontSize: 14,\n    fontWeight: '400',\n    text: 'Hello world',\n  });\n\n  return null;\n};\n\nexport const MyComp: React.FC = () => {\n  return (\n    <WaitForFonts>\n      <MyCompInner />\n    </WaitForFonts>\n  );\n};\n```\n\n### Use the `validateFontIsLoaded` option<AvailableFrom v=\"4.0.136\"/>\n\nPass `validateFontIsLoaded: true` to any of [`measureText()`](/docs/layout-utils/measure-text), [`fitText()`](/docs/layout-utils/fit-text), and [`fillTextBox()`](/docs/layout-utils/fill-text-box) to validate that the font family you passed is actually loaded.\n\nThis will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.\n\n:::note\nIn Remotion v5, this will become the default.\n:::\n\n## Match all font properties\n\nWhen measuring text, ensure that all font properties match the ones you are going to use in your video.  \nThis includes `fontFamily`, `fontSize`, and `fontWeight`, `letterSpacing` and `fontVariantNumeric`.\n\nYou could make reusable variables that you reference in both the measuring function and the actual component.\n\n```tsx twoslash title=\"Using variables for font properties\"\nimport {measureText} from '@remotion/layout-utils';\n\nconst text = 'Hello world';\nconst fontFamily = 'Inter';\nconst fontWeight = 'bold';\nconst fontSize = 16;\n\n// Use the variable in the measurement function:\nmeasureText({\n  text,\n  fontFamily,\n  fontWeight,\n  fontSize,\n});\n\n// As well as in markup\n<div style={{fontFamily, fontWeight, fontSize}}>{text}</div>;\n```\n\n## Be aware of borders and padding\n\nAdding a `padding` or a `border` to a word will skew the measurements.  \nAvoid using `padding` altogether and use the natural spacing between words.  \nInstead of `border`, use an `outline` to add a line outside the text without affecting its layout.\n\n## Whitespace\n\nWhen measuring, the Layout utils will wrap the text in a `<span>` with `display: inline-block` and `white-space: pre` applied.  \nThis will also measure the width of the whitespace characters.\n\nAdd those two CSS properties to your markup as well to match it with the measurements.\n\n## Server-side rendering\n\nThe layout utilities need to be run in a browser.  \nIf you are using them in a component that will be server-side rendered, then we recommend you call the functions in a `useEffect`, like on the first example on this page.\n"

Take note of the following points to ensure correct measurements when using the [`@remotion/layout-utils`](/docs/layout-utils) package.

These tips apply to all of [`measureText()`](/docs/layout-utils/measure-text), [`fitText()`](/docs/layout-utils/fit-text), and [`fillTextBox()`](/docs/layout-utils/fill-text-box).

## Wait until the font is loaded[​](#wait-until-the-font-is-loaded)

Only call [`measureText()`](/docs/layout-utils/measure-text) after the font is loaded. This applies to Google Fonts (example below) or any other font loading mechanism.

If you only need this in one component, using `waitUntilDone()` in a `useEffect()` is fine.

### Example with `useEffect`[​](#example-with-useeffect)

```

MyComp.tsximport {useState, useEffect} from 'react';
import {Dimensions, measureText} from '@remotion/layout-utils';
import {loadFont, fontFamily} from '@remotion/google-fonts/Inter';

const {waitUntilDone} = loadFont('normal', {
  weights: ['400'],
  subsets: ['latin'],
});

const MyComp: React.FC = () => {
  const [dimensions, setDimensions] = useState<Dimensions | null>(null);

  useEffect(() => {
    // Wait until the font is loaded before measuring text
    waitUntilDone().then(() => {
      const measurement = measureText({
        fontFamily: fontFamily,
        fontSize: 14,
        fontWeight: '400',
        text: 'Hello world',
      });

      // We don't need to use delayRender() here, because
      // font loading from @remotion/google-fonts is already wrapped in it
      setDimensions(measurement);
    });
  }, []);

  return null;
};Copy
```

### Example with high-order component[​](#example-with-high-order-component)

For larger projects, this pattern keeps the code clean by exposing a higher-order component that only mounts children once fonts are loaded.

The following logic is borrowed from the [Remotion Recorder](/docs/recorder).

A file is defined which loads some fonts:

```

fonts.tsimport {fontFamily as regularFont, loadFont as loadRegular} from '@remotion/google-fonts/Inter';

import {fontFamily as monospaceFont, loadFont as loadMonospace} from '@remotion/google-fonts/RobotoMono';

import {cancelRender, continueRender, delayRender} from 'remotion';

const regular = loadRegular('normal', {
  weights: ['400', '700'],
  subsets: ['latin'],
});
const monospace = loadMonospace('normal', {
  weights: ['400'],
  subsets: ['latin'],
});

export const waitForFonts = async () => {
  await regular.waitUntilDone();
  await monospace.waitUntilDone();
};

const delay = delayRender('Loading fonts');

waitForFonts()
  .then(() => continueRender(delay))
  .catch((err) => cancelRender(err));Copy
```

Then a higher-order component is defined which only renders its children when the font is loaded:

```

WaitForFonts.tsximport React, {useEffect, useState} from 'react';
import {cancelRender, continueRender, useDelayRender} from 'remotion';
import {waitForFonts} from './fonts';

export const WaitForFonts: React.FC<{
  children: React.ReactNode;
}> = ({children}) => {
  const [fontsLoaded, setFontsLoaded] = useState(false);
  const {delayRender, continueRender} = useDelayRender();
  const [handle] = useState(() => delayRender('Waiting for fonts to be loaded'));

  useEffect(() => {
    if (fontsLoaded) {
      return;
    }

    waitForFonts()
      .then(() => {
        setFontsLoaded(true);
      })
      .catch((err) => {
        cancelRender(err);
      });
  }, [fontsLoaded, handle, continueRender, delayRender]);

  useEffect(() => {
    if (fontsLoaded) {
      continueRender(handle);
    }
  }, [continueRender, fontsLoaded, handle]);

  if (!fontsLoaded) {
    return null;
  }

  return <>{children}</>;
};Copy
```

Then the component can wrap any other component that calls text measurement APIs:

```

MyComp.tsximport React from 'react';
import {regular} from './fonts';
import {WaitForFonts} from './WaitForFonts';
import {measureText} from '@remotion/layout-utils';

const MyCompInner: React.FC = () => {
  // Safe to call measureText() here
  const measurement = measureText({
    fontFamily: regular,
    fontSize: 14,
    fontWeight: '400',
    text: 'Hello world',
  });

  return null;
};

export const MyComp: React.FC = () => {
  return (
    <WaitForFonts>
      <MyCompInner />
    </WaitForFonts>
  );
};Copy
```

### Use the `validateFontIsLoaded` option[v4.0.136](https://github.com/remotion-dev/remotion/releases/v4.0.136)[​](#use-the-validatefontisloaded-option)

Pass `validateFontIsLoaded: true` to any of [`measureText()`](/docs/layout-utils/measure-text), [`fitText()`](/docs/layout-utils/fit-text), and [`fillTextBox()`](/docs/layout-utils/fill-text-box) to validate that the font family you passed is actually loaded.

This will take a second measurement with the fallback font and if it produces the same measurements, it assumes the fallback font was used and will throw an error.
](/docs/layout-utils/fill-text-box)](/docs/layout-utils/fill-text-box)
](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)
- ](/docs/layout-utils/fill-text-box)