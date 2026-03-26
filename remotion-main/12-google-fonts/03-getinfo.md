---
title: "getInfo()"
url: "https://www.remotion.dev/docs/google-fonts/get-info"
path: "/docs/google-fonts/get-info"
---

"---\nimage: /generated/articles-docs-google-fonts-get-info.png\ntitle: getInfo()\ncrumb: '@remotion/google-fonts'\n---\n\nimport {AvailableFonts} from '../../components/AvailableFonts';\n\n_Part of the [`@remotion/google-fonts`](/docs/google-fonts) package_\n\nEach font exports an `getInfo()` function that can be used to get various information about the font at runtime, such as which weights, styles and subsets are available.\n\n## Usage\n\nTo get information about a font, you can import the `info` property:\n\n```tsx twoslash title=\"Get info about the font\"\nimport {getInfo} from '@remotion/google-fonts/Montserrat';\nconsole.log(getInfo());\n```\n\n```json title=\"Example value of info object\"\n{\n  \"fontFamily\": \"Titan One\",\n  \"importName\": \"TitanOne\",\n  \"version\": \"v13\",\n  \"url\": \"https://fonts.googleapis.com/css2?family=Titan+One:ital,wght@0,400\",\n  \"unicodeRanges\": {\n    \"latin-ext\": \"U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF\",\n    \"latin\": \"U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD\"\n  },\n  \"fonts\": {\n    \"normal\": {\n      \"400\": {\n        \"latin-ext\": \"https://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjCmjgm6Es.woff2\",\n        \"latin\": \"https://fonts.gstatic.com/s/titanone/v13/mFTzWbsGxbbS_J5cQcjClDgm.woff2\"\n      }\n    }\n  },\n  \"subsets\": [\"latin\", \"latin-ext\"]\n}\n```\n\n## See also\n\n- [Fonts](/docs/fonts)\n- [`@remotion/google-fonts`](/docs/google-fonts)\n"

*Part of the [`@remotion/google-fonts`](/docs/google-fonts) package*

Each font exports an `getInfo()` function that can be used to get various information about the font at runtime, such as which weights, styles and subsets are available.

## Usage[​](#usage)

To get information about a font, you can import the `info` property:

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

## See also[​](#see-also)

- [Fonts](/docs/fonts)

- [`@remotion/google-fonts`](/docs/google-fonts)
](/docs/google-fonts)](/docs/google-fonts)
](/docs/google-fonts)
- ](/docs/google-fonts)