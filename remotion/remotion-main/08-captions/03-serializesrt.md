---
title: "serializeSrt()"
url: "https://www.remotion.dev/docs/captions/serialize-srt"
path: "/docs/captions/serialize-srt"
---

"---\nimage: /generated/articles-docs-captions-serialize-srt.png\ntitle: serializeSrt()\ncrumb: '@remotion/captions'\n---\n\n# serializeSrt()<AvailableFrom v=\"4.0.216\"/>\n\nConverts a two-dimensional array of [`Caption`](/docs/captions/caption) items into a string in the SubRip format (`.srt`).\n\n```tsx twoslash title=\"Example usage\"\nimport {serializeSrt, Caption} from '@remotion/captions';\n\nconst captions: Caption[] = [\n  {\n    text: 'Welcome to the Example Subtitle File!',\n    startMs: 0,\n    endMs: 2500,\n    timestampMs: 1250,\n    confidence: 1,\n  },\n  {\n    text: 'This is a demonstration of SRT subtitles.',\n    startMs: 3000,\n    endMs: 6000,\n    timestampMs: 4500,\n    confidence: 1,\n  },\n  {\n    text: 'You can use SRT files to add subtitles to your videos.',\n    startMs: 7000,\n    endMs: 10500,\n    timestampMs: 8750,\n    confidence: 1,\n  },\n];\n\nconst lines = captions.map((caption) => [caption]);\n\nconst serialized = serializeSrt({lines});\n\n/* serialized = `1\n00:00:00,000 --> 00:00:02,500\nWelcome to the Example Subtitle File!\n\n2\n00:00:03,000 --> 00:00:06,000\nThis is a demonstration of SRT subtitles.\n\n3\n00:00:07,000 --> 00:00:10,500\nYou can use SRT files to add subtitles to your videos.\n`\n*/\n```\n\n## API\n\n### `lines`\n\nAn two-dimensional array of [`Caption`](/docs/captions/caption) items.\n\nEach top-level item represents a line in the SubRip file.\n\nThe second-level items represent the words in that line.  \nWords get concatenated together during serialization. No spaces are added between the words.  \nThe start timestamp is determined from the `startMs` value of the first word in the line.  \nThe end timestamp is determined from the `endMs` value of the last word in the line.\n\nArrays with no items will be ignored.\n\n## Return value\n\nA string in the SubRip format (`.srt`).\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/serialize-srt.ts)\n- [`@remotion/captions`](/docs/captions/api)\n"

Converts a two-dimensional array of [`Caption`](/docs/captions/caption) items into a string in the SubRip format (`.srt`).

```

Example usageimport {serializeSrt, Caption} from '@remotion/captions';

const captions: Caption[] = [
  {
    text: 'Welcome to the Example Subtitle File!',
    startMs: 0,
    endMs: 2500,
    timestampMs: 1250,
    confidence: 1,
  },
  {
    text: 'This is a demonstration of SRT subtitles.',
    startMs: 3000,
    endMs: 6000,
    timestampMs: 4500,
    confidence: 1,
  },
  {
    text: 'You can use SRT files to add subtitles to your videos.',
    startMs: 7000,
    endMs: 10500,
    timestampMs: 8750,
    confidence: 1,
  },
];

const lines = captions.map((caption) => [caption]);

const serialized = serializeSrt({lines});

/* serialized = `1
00:00:00,000 --> 00:00:02,500
Welcome to the Example Subtitle File!

2
00:00:03,000 --> 00:00:06,000
This is a demonstration of SRT subtitles.

3
00:00:07,000 --> 00:00:10,500
You can use SRT files to add subtitles to your videos.
`
*/Copy
```

## API[​](#api)

### `lines`[​](#lines)

An two-dimensional array of [`Caption`](/docs/captions/caption) items.

Each top-level item represents a line in the SubRip file.

The second-level items represent the words in that line.

Words get concatenated together during serialization. No spaces are added between the words.

The start timestamp is determined from the `startMs` value of the first word in the line.

The end timestamp is determined from the `endMs` value of the last word in the line.

Arrays with no items will be ignored.

## Return value[​](#return-value)

A string in the SubRip format (`.srt`).

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/serialize-srt.ts)

- [`@remotion/captions`](/docs/captions/api)
](/docs/captions/api)](/docs/captions/api)
](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)