---
title: "createTikTokStyleCaptions()"
url: "https://www.remotion.dev/docs/captions/create-tiktok-style-captions"
path: "/docs/captions/create-tiktok-style-captions"
---

"---\nimage: /generated/articles-docs-captions-create-tiktok-style-captions.png\ntitle: createTikTokStyleCaptions()\ncrumb: '@remotion/captions'\n---\n\n# createTikTokStyleCaptions()<AvailableFrom v=\"4.0.216\"/>\n\nUsing this function, you can segment tokens to create \"pages\" of captions, as commonly seen on TikTok videos.\n\nYou may specify how often pages switch.\nA high value for `combineTokensWithinMilliseconds` will fit many words on 1 page, while a low value will lead to word-by-word animation.\n\nThis function is safe to use in the browser, Node.js and Bun.\n\n:::note\nThis API expects the whitespace to be included in the `text` field **before each word. Spaces are used as delimiters, and omitting them will cause the entire text to merge into a single line or page, resulting in poorly formatted captions.**.\n:::\n\n```tsx twoslash title=\"Create pages from captions\"\nimport {createTikTokStyleCaptions, Caption} from '@remotion/captions';\n\nconst captions: Caption[] = [\n  {\n    text: 'Using',\n    startMs: 40,\n    endMs: 300,\n    timestampMs: 200,\n    confidence: null,\n  },\n  {\n    text: \" Remotion's\",\n    startMs: 300,\n    endMs: 900,\n    timestampMs: 440,\n    confidence: null,\n  },\n  {\n    text: ' TikTok',\n    startMs: 900,\n    endMs: 1260,\n    timestampMs: 1080,\n    confidence: null,\n  },\n  {\n    text: ' template,',\n    startMs: 1260,\n    endMs: 1950,\n    timestampMs: 1600,\n    confidence: null,\n  },\n];\n\nconst {pages} = createTikTokStyleCaptions({\n  captions,\n  combineTokensWithinMilliseconds: 1200,\n});\n\n/* pages: [\n  {\n    text: \"Using Remotion's\",\n    startMs: 40,\n    durationMs: 860,\n    tokens: [\n      {\n        text: 'Using',\n        fromMs: 40,\n        toMs: 300,\n      },\n      {\n        text: \" Remotion's\",\n        fromMs: 300,\n        toMs: 900,\n      },\n    ],\n  },\n  {\n    text: 'TikTok template,',\n    startMs: 900,\n    durationMs: 1050,\n    tokens: [\n      {\n        text: 'TikTok',\n        fromMs: 900,\n        toMs: 1260,\n      },\n      {\n        text: ' template,',\n        fromMs: 1260,\n        toMs: 1950,\n      },\n    ],\n  }\n] */\n```\n\n## API\n\n### `captions`\n\nAn array of [`Caption`](/docs/captions/caption) objects.\n\n### `combineTokensWithinMilliseconds`\n\nWords that are closer than this value will be combined into a single page.\n\n## Return value\n\nAn object with the following properties:\n\n### `pages`\n\nAn array of `TikTokPage` objects.\n\nA page consists of:\n\n- `text`: The text of the page.\n- `startMs`: The start time of the page in milliseconds.\n- `durationMs`: The duration of the page in milliseconds (_from v4.0.261_).\n- `tokens`: An array of objects, if you want to animate word-per-word:\n  - `text`: The text of the token.\n  - `fromMs`: The absolute start time of the token in milliseconds.\n  - `toMs`: The absolute end time of the token in milliseconds.\n\n## Whitespace sensitivity\n\nThe [`text`](/docs/captions/caption#text) field is whitespace sensitive. You should include spaces in it, ideally before each word.\n\nWhile rendering, apply the [`white-space: pre`](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space) CSS property to the container of the caption to ensure that the spaces are preserved.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/create-tiktok-style-captions.ts)\n- [`@remotion/captions`](/docs/captions/api)\n"

Using this function, you can segment tokens to create "pages" of captions, as commonly seen on TikTok videos.

You may specify how often pages switch.
A high value for `combineTokensWithinMilliseconds` will fit many words on 1 page, while a low value will lead to word-by-word animation.

This function is safe to use in the browser, Node.js and Bun.
]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()