---
title: "parseSrt()"
url: "https://www.remotion.dev/docs/captions/parse-srt"
path: "/docs/captions/parse-srt"
---

"---\nimage: /generated/articles-docs-captions-parse-srt.png\ntitle: parseSrt()\ncrumb: '@remotion/captions'\n---\n\n# parseSrt()<AvailableFrom v=\"4.0.216\"/>\n\nParses the contents of a SubRip file (`.srt`) and returns an array of [`Caption`](/docs/captions/caption) items.\n\n```tsx twoslash title=\"Example usage\"\nimport {parseSrt} from '@remotion/captions';\n\nconst input = `\n1\n00:00:00,000 --> 00:00:02,500\nWelcome to the Example Subtitle File!\n\n2\n00:00:03,000 --> 00:00:06,000\nThis is a demonstration of SRT subtitles.\n\n3\n00:00:07,000 --> 00:00:10,500\nYou can use SRT files to add subtitles to your videos.\n`.trim();\n\nconst {captions} = parseSrt({input});\n\n/* captions = [\n  {\n    confidence: 1,\n    endMs: 2500,\n    startMs: 0,\n    text: 'Welcome to the Example Subtitle File!',\n    timestampMs: 1250,\n  },\n  {\n    confidence: 1,\n    endMs: 6000,\n    startMs: 3000,\n    text: 'This is a demonstration of SRT subtitles.',\n    timestampMs: 4500,\n  },\n  {\n    confidence: 1,\n    endMs: 10500,\n    startMs: 7000,\n    text: 'You can use SRT files to add subtitles to your videos.',\n    timestampMs: 8750,\n  },\n]\n*/\n```\n\n## API\n\n### `input`\n\nThe contents of a `.srt` file as a `string`.\n\n## Return value\n\nAn object with the following properties:\n\n### `captions`\n\nAn array of [`Caption`](/docs/captions/caption) items.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/parse-srt.ts)\n- [`@remotion/captions`](/docs/captions/api)\n"

Parses the contents of a SubRip file (`.srt`) and returns an array of [`Caption`](/docs/captions/caption) items.

```

Example usageimport {parseSrt} from '@remotion/captions';

const input = `
1
00:00:00,000 --> 00:00:02,500
Welcome to the Example Subtitle File!

2
00:00:03,000 --> 00:00:06,000
This is a demonstration of SRT subtitles.

3
00:00:07,000 --> 00:00:10,500
You can use SRT files to add subtitles to your videos.
`.trim();

const {captions} = parseSrt({input});

/* captions = [
  {
    confidence: 1,
    endMs: 2500,
    startMs: 0,
    text: 'Welcome to the Example Subtitle File!',
    timestampMs: 1250,
  },
  {
    confidence: 1,
    endMs: 6000,
    startMs: 3000,
    text: 'This is a demonstration of SRT subtitles.',
    timestampMs: 4500,
  },
  {
    confidence: 1,
    endMs: 10500,
    startMs: 7000,
    text: 'You can use SRT files to add subtitles to your videos.',
    timestampMs: 8750,
  },
]
*/Copy
```

## API[​](#api)

### `input`[​](#input)

The contents of a `.srt` file as a `string`.

## Return value[​](#return-value)

An object with the following properties:

### `captions`[​](#captions)

An array of [`Caption`](/docs/captions/caption) items.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/parse-srt.ts)

- [`@remotion/captions`](/docs/captions/api)
](/docs/captions/api)](/docs/captions/api)
](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)