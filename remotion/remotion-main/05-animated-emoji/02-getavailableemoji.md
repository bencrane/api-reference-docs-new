---
title: "getAvailableEmoji()"
url: "https://www.remotion.dev/docs/animated-emoji/get-available-emoji"
path: "/docs/animated-emoji/get-available-emoji"
---

"---\nimage: /generated/articles-docs-animated-emoji-get-available-emoji.png\nid: get-available-emoji\nsidebar_label: \"getAvailableEmoji()\"\ntitle: \"getAvailableEmoji()\"\nslug: /animated-emoji/get-available-emoji\ncrumb: \"@remotion/animated-emoji\"\n---\n\n_available from v4.0.187_\n\nGets a list of available emoji that you can use with [`<AnimatedEmoji>`](/docs/animated-emoji/animated-emoji).\n\n```tsx twoslash title=\"get-emoji.ts\"\nimport {getAvailableEmojis} from \"@remotion/animated-emoji\";\n\nconst emojiList = getAvailableEmojis();\n\nconsole.log(emojiList);\n```\n\n## Return value\n\nAn array of objects with the following properties:\n\n### `name`\n\nThe name of the emoji. You can pass the name to the [`emoji`](/docs/animated-emoji/animated-emoji#emoji) prop.\n\n### `categories`\n\nAn array of categories that the emoji belongs to.\n\n### `tags`\n\nAn array of tags that the emoji has.\n\n### `durationInSeconds`\n\nThe duration of the emoji in seconds.\n\n### `codepoint`\n\nThe Unicode codepoint of the emoji.\n\n## See also\n\n- [`<AnimatedEmoji>`](/docs/animated-emoji/animated-emoji)\n"

*available from v4.0.187*

Gets a list of available emoji that you can use with [`<AnimatedEmoji>`](/docs/animated-emoji/animated-emoji).

```

get-emoji.tsimport {getAvailableEmojis} from "@remotion/animated-emoji";

const emojiList = getAvailableEmojis();

console.log(emojiList);Copy
```

## Return value[​](#return-value)

An array of objects with the following properties:

### `name`[​](#name)

The name of the emoji. You can pass the name to the [`emoji`](/docs/animated-emoji/animated-emoji#emoji) prop.

### `categories`[​](#categories)

An array of categories that the emoji belongs to.

### `tags`[​](#tags)

An array of tags that the emoji has.

### `durationInSeconds`[​](#durationinseconds)

The duration of the emoji in seconds.

### `codepoint`[​](#codepoint)

The Unicode codepoint of the emoji.

## See also[​](#see-also)

- [`<AnimatedEmoji>`](/docs/animated-emoji/animated-emoji)
](/docs/animated-emoji/animated-emoji)](/docs/animated-emoji/animated-emoji)
](/docs/animated-emoji/animated-emoji)
- ](/docs/animated-emoji/animated-emoji)
- ](/docs/animated-emoji/animated-emoji)
- ](/docs/animated-emoji/animated-emoji)
- ](/docs/animated-emoji/animated-emoji)
- ](/docs/animated-emoji/animated-emoji)
- ](/docs/animated-emoji/animated-emoji)