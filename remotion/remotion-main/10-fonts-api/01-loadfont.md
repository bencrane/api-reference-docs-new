---
title: "loadFont()"
url: "https://www.remotion.dev/docs/fonts-api/load-font"
path: "/docs/fonts-api/load-font"
---

"---\nimage: /generated/articles-docs-fonts-api-load-font.png\ntitle: loadFont()\ncrumb: \"@remotion/fonts\"\n---\n\n# loadFont()<AvailableFrom v=\"4.0.165\" />\n\n_Part of the [`@remotion/fonts`](/docs/fonts) package_\n\nLoad a local font for use in Remotion.  \nAutomatically blocks the render until the font is ready.\n\n## Usage\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport { loadFont } from \"@remotion/fonts\";\nimport { AbsoluteFill, staticFile } from \"remotion\";\n\nloadFont({\n  family: \"Bangers\",\n  url: staticFile(\"bangers.ttf\"),\n}).then(() => console.log(\"Font loaded!\"));\n\nexport const GoogleFontsExample: React.FC = () => {\n  return (\n    <AbsoluteFill\n      style={{\n        fontFamily: \"Bangers\",\n      }}\n    >\n      <h1>Local Font</h1>\n    </AbsoluteFill>\n  );\n};\n```\n\n## Options\n\n### family\n\nGive the family a name.  \nYou can then reference that name in your CSS using `fontFamily`.\n\n### url\n\nWhere to load the font from. Can be a local file using [`staticFile()`](/docs/staticfile) or a URL.\n\n### format?\n\nDefines the format of the font file. By default gets derived from the file extension of the URL.  \nOverride with one of the following values explicitly: `woff2`, `woff`, `opentype`, `truetype`.\n\n### ascentOverride?\n\nDefines the ascent metric for the font.\n\n### descentOverride?\n\nDefines the descent metric for the font.\n\n### display?\n\nEquivalent to the CSS [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) property.  \nDetermines how a font face is displayed based on whether and when it is downloaded and ready to use.\n\n### featureSettings?\n\nEquivalent to the CSS [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-feature-settings) property.\nAllows control over advanced typographic features in OpenType fonts.\n\n### lineGapOverride?\n\nDefines the line gap metric for the font.\n\n### stretch?\n\nEquivalent to the CSS [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-stretch) property.\nSpecify what kind of stretch the loaded font has.\n\n### style?\n\nEquivalent to the CSS [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-style) property.\nSpecify what kind of style the loaded font has.\n\n### weight?\n\nEquivalent to the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-weight) property.\nSpecify what kind of weight the loaded font has.\n\n### unicodeRange?\n\nThe range of Unicode code points to be used from the font.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/fonts/src/load-font.ts)\n- [Fonts](/docs/fonts)\n"

*Part of the [`@remotion/fonts`](/docs/fonts) package*

Load a local font for use in Remotion.

Automatically blocks the render until the font is ready.

## Usage[​](#usage)

```

MyComp.tsximport { loadFont } from "@remotion/fonts";
import { AbsoluteFill, staticFile } from "remotion";

loadFont({
  family: "Bangers",
  url: staticFile("bangers.ttf"),
}).then(() => console.log("Font loaded!"));

export const GoogleFontsExample: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        fontFamily: "Bangers",
      }}
    >
      <h1>Local Font</h1>
    </AbsoluteFill>
  );
};Copy
```

## Options[​](#options)

### family[​](#family)

Give the family a name.

You can then reference that name in your CSS using `fontFamily`.

### url[​](#url)

Where to load the font from. Can be a local file using [`staticFile()`](/docs/staticfile) or a URL.

### format?[​](#format)

Defines the format of the font file. By default gets derived from the file extension of the URL.

Override with one of the following values explicitly: `woff2`, `woff`, `opentype`, `truetype`.

### ascentOverride?[​](#ascentoverride)

Defines the ascent metric for the font.

### descentOverride?[​](#descentoverride)

Defines the descent metric for the font.

### display?[​](#display)

Equivalent to the CSS [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) property.

Determines how a font face is displayed based on whether and when it is downloaded and ready to use.

### featureSettings?[​](#featuresettings)

Equivalent to the CSS [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-feature-settings) property.
Allows control over advanced typographic features in OpenType fonts.

### lineGapOverride?[​](#linegapoverride)

Defines the line gap metric for the font.

### stretch?[​](#stretch)

Equivalent to the CSS [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-stretch) property.
Specify what kind of stretch the loaded font has.

### style?[​](#style)

Equivalent to the CSS [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-style) property.
Specify what kind of style the loaded font has.

### weight?[​](#weight)

Equivalent to the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-weight) property.
Specify what kind of weight the loaded font has.

### unicodeRange?[​](#unicoderange)

The range of Unicode code points to be used from the font.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/fonts/src/load-font.ts)

- [Fonts](/docs/fonts)
](/docs/fonts)](/docs/fonts)
](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)
- ](/docs/fonts)