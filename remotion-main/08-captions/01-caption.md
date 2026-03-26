---
title: "Caption"
url: "https://www.remotion.dev/docs/captions/caption"
path: "/docs/captions/caption"
---

"---\nimage: /generated/articles-docs-captions-caption.png\ntitle: Caption\ncrumb: '@remotion/captions'\nno_ai: true\n---\n\n# Caption<AvailableFrom v=\"4.0.216\"/>\n\nThis is a simple data structure for a caption.\n\n```tsx twoslash\nimport type {Caption} from '@remotion/captions';\n//            ^?\n```\n\nBy establishing a standard data structure, we allow many operations that involve captions to be interoperable:\n\n- **Transcribing**: Using the [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp) or [`@remotion/openai-whisper`](/docs/openai-whisper) packages\n- **Formatting**: For example, creating pages using [`createTikTokStyleCaptions()`](/docs/captions/create-tiktok-style-captions)\n- **Parsing**: Using the [`parseSrt()`](/docs/captions/parse-srt) function\n- **Serializing**: For example to a `.srt` file using [`serializeSrt()`](/docs/captions/serialize-srt)\n\n## Fields\n\n### `text`\n\nThe text of the caption.\n\n### `startMs`\n\nThe start time of the caption in milliseconds.\n\n### `endMs`\n\nThe end time of the caption in milliseconds.\n\n### `timestampMs`\n\nThe timestamp of the caption as a singular timestamp in milliseconds.  \nWhen using [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp), this the `t_dtw` value.  \nOtherwise, it is not defined, but may be the average of the start and end timestamps.\n\n### `confidence`\n\nA number between 0 and 1 that indicates how confident the transcription is.\n\n## Whitespace sensitivity\n\nThe [`text`](#text) field is whitespace sensitive. You should include spaces in it, ideally before each word.\n\nWhile rendering, apply the [`white-space: pre`](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space) CSS property to the container of the caption to ensure that the spaces are preserved.\n\n## See also\n\n- [Source code for this type](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/caption.ts)\n- [`@remotion/captions`](/docs/captions/api)\n"

This is a simple data structure for a caption.

```
import type {Caption} from '@remotion/captions';
               
(alias) type Caption = {
    text: string;
    startMs: number;
    endMs: number;
    timestampMs: number | null;
    confidence: number | null;
}
import CaptionCopy
```

By establishing a standard data structure, we allow many operations that involve captions to be interoperable:

- **Transcribing**: Using the [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp) or [`@remotion/openai-whisper`](/docs/openai-whisper) packages

- **Formatting**: For example, creating pages using [`createTikTokStyleCaptions()`](/docs/captions/create-tiktok-style-captions)

- **Parsing**: Using the [`parseSrt()`](/docs/captions/parse-srt) function

- **Serializing**: For example to a `.srt` file using [`serializeSrt()`](/docs/captions/serialize-srt)

## Fields[​](#fields)

### `text`[​](#text)

The text of the caption.

### `startMs`[​](#startms)

The start time of the caption in milliseconds.

### `endMs`[​](#endms)

The end time of the caption in milliseconds.

### `timestampMs`[​](#timestampms)

The timestamp of the caption as a singular timestamp in milliseconds.

When using [`@remotion/install-whisper-cpp`](/docs/install-whisper-cpp), this the `t_dtw` value.

Otherwise, it is not defined, but may be the average of the start and end timestamps.

### `confidence`[​](#confidence)

A number between 0 and 1 that indicates how confident the transcription is.

## Whitespace sensitivity[​](#whitespace-sensitivity)

The [`text`](#text) field is whitespace sensitive. You should include spaces in it, ideally before each word.

While rendering, apply the [`white-space: pre`](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space) CSS property to the container of the caption to ensure that the spaces are preserved.

## See also[​](#see-also)

- [Source code for this type](https://github.com/remotion-dev/remotion/blob/main/packages/captions/src/caption.ts)

- [`@remotion/captions`](/docs/captions/api)
](/docs/captions/api)](/docs/captions/api)
](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)
- ](/docs/captions/api)