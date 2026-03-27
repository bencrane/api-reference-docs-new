---
title: "@remotion/google-fonts"
url: "https://www.remotion.dev/docs/google-fonts/"
path: "/docs/google-fonts/"
---

"---\nimage: /generated/articles-docs-google-fonts-index.png\nid: google-fonts\nsidebar_label: Overview\ntitle: '@remotion/google-fonts'\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {TableOfContents} from './TableOfContents';\n\nThe `@remotion/google-fonts` package provides APIs for easily integrating [Google Fonts](https://fonts.google.com/) into Remotion.\n\n## Installation\n\n<Tabs\ndefaultValue=\"npm\"\nvalues={[\n{ label: 'npm', value: 'npm', },\n{ label: 'yarn', value: 'yarn', },\n{ label: 'pnpm', value: 'pnpm', },\n]\n}>\n<TabItem value=\"npm\">\n\n```bash\nnpm i @remotion/google-fonts\n```\n\n  </TabItem>\n\n  <TabItem value=\"yarn\">\n\n```bash\nyarn add @remotion/google-fonts\n```\n\n  </TabItem>\n\n  <TabItem value=\"pnpm\">\n\n```bash\npnpm i @remotion/google-fonts\n```\n\n  </TabItem>\n</Tabs>\n\n## Usage\n\nTo load a font, import the package `@remotion/google-fonts/<FontName>` and call [`loadFont()`](/docs/google-fonts/load-font).\n\nFor production, start with these defaults:\n\n- Pass a style and usually `weights` + `subsets` to avoid loading unnecessary variants.\n- Load your fonts in one module and reuse the exports.\n- If you use text measurement APIs, gate rendering until fonts are ready using a higher-order component.\n\n```tsx twoslash title=\"Load one style, weight and subset\"\nimport {loadFont} from '@remotion/google-fonts/TitanOne';\n\nconst {fontFamily} = loadFont('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n}); // \"Titan One\"\n```\n\nIf you want to import multiple fonts and want to avoid a variable name collision, you can import the fonts using an `import * as` statement.\n\n```tsx twoslash title=\"Scope loadFont() variable\"\nimport * as Montserrat from '@remotion/google-fonts/Montserrat';\nMontserrat.loadFont('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n```\n\nCall [`loadFont()`](/docs/google-fonts/load-font) to start the loading process. Calling it without arguments loads every style, weight and subset, which can cause unnecessary requests.\n\nUse TypeScript autocomplete to see the available styles. To further narrow down what's being loaded, specify `weights` and `subsets`. If you need multiple styles, call `loadFont()` multiple times.\n\n```tsx twoslash title=\"Load multiple styles explicitly\"\nimport * as Montserrat from '@remotion/google-fonts/Montserrat';\n\nMontserrat.loadFont('normal', {\n  weights: ['400', '700'],\n  subsets: ['latin'],\n});\nMontserrat.loadFont('italic', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n```\n\n[`loadFont()`](/docs/google-fonts/load-font) returns an object with a `fontFamily` property. You can use the `style` attribute to render text in the font you loaded.\n\n```tsx twoslash title=\"Use the fontFamily property\"\nimport {loadFont} from '@remotion/google-fonts/TitanOne';\nimport {AbsoluteFill} from 'remotion';\n\nconst {fontFamily} = loadFont('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n\nexport const GoogleFontsDemoComposition = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        fontFamily,\n      }}\n    >\n      <div>Hallo Google Fonts</div>\n    </AbsoluteFill>\n  );\n};\n```\n\nIf your project uses multiple fonts, define them in one file and export a `waitForFonts()` helper:\n\n```tsx twoslash title=\"fonts.ts\"\nimport {loadFont as loadInter} from '@remotion/google-fonts/Inter';\nimport {loadFont as loadRobotoMono} from '@remotion/google-fonts/RobotoMono';\n\nconst inter = loadInter('normal', {\n  weights: ['400', '700'],\n  subsets: ['latin'],\n});\nconst mono = loadRobotoMono('normal', {\n  weights: ['400'],\n  subsets: ['latin'],\n});\n\nexport const waitForFonts = async () => {\n  await Promise.all([inter.waitUntilDone(), mono.waitUntilDone()]);\n};\n```\n\nIf you use text measurement APIs, wrap your content in a component that waits for your fonts before rendering. See the [higher-order component example](/docs/layout-utils/best-practices#example-with-high-order-component) and [font loading troubleshooting](/docs/troubleshooting/font-loading-errors).\n\nTo get information about a font, you can import the `getInfo()` function:\n\n```tsx twoslash title=\"Get info about the font\"\nimport {getInfo} from '@remotion/google-fonts/Montserrat';\nconsole.log(getInfo());\n```\n\n```json title=\"Example value of info object\"\n{\n  \"fontFamily\": \"Titan One\",\n  \"importName\": \"TitanOne\",\n  \"version\": \"v13\",\n  \"url\": \"https://fonts.googleapis.com/css2?family=Titan+One:ital,wght@0,400\",\n  \"unicodeRanges\": {\n    \"latin-ext\": \"U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF\",\n    \"latin\": \"U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD\"\n  },\n  \"fonts\": {\n    \"normal\": {\n      \"400\": {\n        \"latin-ext\": \"https://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjCmjgm6Es.woff2\",\n        \"latin\": \"https://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjClDgm.woff2\"\n      }\n    }\n  },\n  \"subsets\": [\"latin\", \"latin-ext\"]\n}\n```\n\nTo get a list of all available fonts, you can call [`getAvailableFonts()`](/docs/google-fonts/get-available-fonts) imported from `@remotion/google-fonts`:\n\n```ts twoslash\nimport {getAvailableFonts} from '@remotion/google-fonts';\n\nconsole.log(getAvailableFonts());\n```\n\n## APIs\n\n<TableOfContents />\n\n## Troubleshooting\n\nKnown issues:\n\n- [delayRender timeout when fetching fonts](/docs/troubleshooting/font-loading-errors#render-timeout-when-loading-google-fonts)\n\n## Credits\n\nImplemented by [Hidayatullah](https://github.com/ayatkyo).\n\n## License\n\nMIT\n\n## See also\n\n- [Fonts](/docs/fonts)\n- [`loadFont()`](/docs/google-fonts/load-font)\n"

The `@remotion/google-fonts` package provides APIs for easily integrating [Google Fonts](https://fonts.google.com/) into Remotion.

## Installation[​](#installation)

- npm
- yarn
- pnpm

```
npm i @remotion/google-fontsCopy
```

```
yarn add @remotion/google-fontsCopy
```

```
pnpm i @remotion/google-fontsCopy
```

## Usage[​](#usage)

To load a font, import the package `@remotion/google-fonts/<FontName>` and call [`loadFont()`](/docs/google-fonts/load-font).

For production, start with these defaults:

- Pass a style and usually `weights` + `subsets` to avoid loading unnecessary variants.

- Load your fonts in one module and reuse the exports.

- If you use text measurement APIs, gate rendering until fonts are ready using a higher-order component.

```

Load one style, weight and subsetimport {loadFont} from '@remotion/google-fonts/TitanOne';

const {fontFamily} = loadFont('normal', {
  weights: ['400'],
  subsets: ['latin'],
}); // "Titan One"Copy
```

If you want to import multiple fonts and want to avoid a variable name collision, you can import the fonts using an `import * as` statement.

```

Scope loadFont() variableimport * as Montserrat from '@remotion/google-fonts/Montserrat';
Montserrat.loadFont('normal', {
  weights: ['400'],
  subsets: ['latin'],
});Copy
```

Call [`loadFont()`](/docs/google-fonts/load-font) to start the loading process. Calling it without arguments loads every style, weight and subset, which can cause unnecessary requests.

Use TypeScript autocomplete to see the available styles. To further narrow down what's being loaded, specify `weights` and `subsets`. If you need multiple styles, call `loadFont()` multiple times.

```

Load multiple styles explicitlyimport * as Montserrat from '@remotion/google-fonts/Montserrat';

Montserrat.loadFont('normal', {
  weights: ['400', '700'],
  subsets: ['latin'],
});
Montserrat.loadFont('italic', {
  weights: ['400'],
  subsets: ['latin'],
});Copy
```

[`loadFont()`](/docs/google-fonts/load-font) returns an object with a `fontFamily` property. You can use the `style` attribute to render text in the font you loaded.

```

Use the fontFamily propertyimport {loadFont} from '@remotion/google-fonts/TitanOne';
import {AbsoluteFill} from 'remotion';

const {fontFamily} = loadFont('normal', {
  weights: ['400'],
  subsets: ['latin'],
});

export const GoogleFontsDemoComposition = () => {
  return (
    <AbsoluteFill
      style={{
        fontFamily,
      }}
    >
      <div>Hallo Google Fonts</div>
    </AbsoluteFill>
  );
};Copy
```

If your project uses multiple fonts, define them in one file and export a `waitForFonts()` helper:

```

fonts.tsimport {loadFont as loadInter} from '@remotion/google-fonts/Inter';
import {loadFont as loadRobotoMono} from '@remotion/google-fonts/RobotoMono';

const inter = loadInter('normal', {
  weights: ['400', '700'],
  subsets: ['latin'],
});
const mono = loadRobotoMono('normal', {
  weights: ['400'],
  subsets: ['latin'],
});

export const waitForFonts = async () => {
  await Promise.all([inter.waitUntilDone(), mono.waitUntilDone()]);
};Copy
```

If you use text measurement APIs, wrap your content in a component that waits for your fonts before rendering. See the [higher-order component example](/docs/layout-utils/best-practices#example-with-high-order-component) and [font loading troubleshooting](/docs/troubleshooting/font-loading-errors).

To get information about a font, you can import the `getInfo()` function:

```

Get info about the fontimport {getInfo} from '@remotion/google-fonts/Montserrat';
console.log(getInfo());Copy
```

```

Example value of info object{
  "fontFamily": "Titan One",
  "importName": "TitanOne",
  "version": "v13",
  "url": "https://fonts.googleapis.com/css2?family=Titan+One:ital,wght@0,400",
  "unicodeRanges": {
    "latin-ext": "U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF",
    "latin": "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
  },
  "fonts": {
    "normal": {
      "400": {
        "latin-ext": "https://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjCmjgm6Es.woff2",
        "latin": "https://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjClDgm.woff2"
      }
    }
  },
  "subsets": ["latin", "latin-ext"]
}Copy
```

To get a list of all available fonts, you can call [`getAvailableFonts()`](/docs/google-fonts/get-available-fonts) imported from `@remotion/google-fonts`:

```
import {getAvailableFonts} from '@remotion/google-fonts';

console.log(getAvailableFonts());Copy
```

## APIs[​](#apis)

[
**loadFont()**
Load a Google Font](/docs/google-fonts/load-font)[
**getAvailableFonts()**
Static list of available fonts](/docs/google-fonts/get-available-fonts)[
**getInfo()**
Metadata about a specific font](/docs/google-fonts/get-info)[
**loadFontFromInfo()**
Load a Google Font based on metadata](/docs/google-fonts/load-font-from-info)

## Troubleshooting[​](#troubleshooting)

Known issues:

- [delayRender timeout when fetching fonts](/docs/troubleshooting/font-loading-errors#render-timeout-when-loading-google-fonts)

## Credits[​](#credits)

Implemented by [Hidayatullah](https://github.com/ayatkyo).

## License[​](#license)

MIT

## See also[​](#see-also)

- [Fonts](/docs/fonts)

- [`loadFont()`](/docs/google-fonts/load-font)
](/docs/google-fonts/load-font)](/docs/google-fonts/load-font)
](/docs/google-fonts/load-font)
- ](/docs/google-fonts/load-font)
- ](/docs/google-fonts/load-font)
- ](/docs/google-fonts/load-font)
- ](/docs/google-fonts/load-font)
- ](/docs/google-fonts/load-font)
- ](/docs/google-fonts/load-font)