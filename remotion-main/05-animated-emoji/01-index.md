---
title: "<AnimatedEmoji>"
url: "https://www.remotion.dev/docs/animated-emoji/animated-emoji"
path: "/docs/animated-emoji/animated-emoji"
---

"---\nimage: /generated/articles-docs-animated-emoji-animated-emoji.png\nid: animated-emoji\nsidebar_label: \"<AnimatedEmoji>\"\ntitle: \"<AnimatedEmoji>\"\nslug: /animated-emoji/animated-emoji\ncrumb: \"@remotion/animated-emoji\"\n---\n\nimport {AvailableEmoji} from \"./AvailableEmoji\";\n\n_Part of the [`@remotion/animated-emoji`](/docs/animated-emoji) package._\n_available from v4.0.187_\n\nDisplays an animated emoji from [Google Fonts Animated Emoji](https://googlefonts.github.io/noto-emoji-animation/).\n\n:::note\n**Self-hosting**: To load the assets, you need to copy the videos from the `public` folder of [`remotion-dev/animated-emoji`](https://github.com/remotion-dev/animated-emoji) into the `public` folder of your Remotion project.\n:::\n\n## Example\n\n```tsx title=\"Animation.tsx\"\nimport {AnimatedEmoji} from \"@remotion/animated-emoji\";\n\nexport const MyAnimation: React.FC = () => {\n  return <AnimatedEmoji emoji=\"blush\" />;\n};\n```\n\n## Props\n\n### `emoji`\n\nSee animated versions [here](https://googlefonts.github.io/noto-emoji-animation/).  \nBy default, no emoji assets are included. Copy them from the `public` folder of [`@remotion/animated-emoji`](/docs/animated-emoji) into the `public` folder of your Remotion project.\n\n<AvailableEmoji />\n\n### `scale?`\n\nChange the resolution of the videos to load.  \nBy default `1`.\n\n<table>\n  <tr>\n    <td>\n      <code>0.5</code>\n    </td>\n    <td>512x512px</td>\n  </tr>\n  <tr>\n    <td>\n      <code>1</code>\n    </td>\n    <td>1024x1024px</td>\n  </tr>\n  <tr>\n    <td>\n      <code>2</code>\n    </td>\n    <td>2048x2048px</td>\n  </tr>\n</table>\n\n### `calculateSrc?`\n\nCustomize the location where the videos are loaded.  \nThis is the default function:\n\n```tsx twoslash title=\"calculate-src.ts\"\nimport {staticFile} from \"remotion\";\nimport type {CalculateEmojiSrc} from \"@remotion/animated-emoji\";\n\nexport const defaultCalculateEmojiSrc: CalculateEmojiSrc = ({\n  emoji,\n  scale,\n  format,\n}) => {\n  const extension = format === \"hevc\" ? \"mp4\" : \"webm\";\n\n  return staticFile(`${emoji}-${scale}x.${extension}`);\n};\n```\n\n## See also\n\n- [`@remotion/animated-emoji`](/docs/animated-emoji)\n- [`getAvailableEmojis()`](/docs/animated-emoji/get-available-emoji)\n"

*Part of the [`@remotion/animated-emoji`](/docs/animated-emoji) package.*
*available from v4.0.187*

Displays an animated emoji from [Google Fonts Animated Emoji](https://googlefonts.github.io/noto-emoji-animation/).
](https://googlefonts.github.io/noto-emoji-animation/)](https://googlefonts.github.io/noto-emoji-animation/)
](https://googlefonts.github.io/noto-emoji-animation/)
- ](https://googlefonts.github.io/noto-emoji-animation/)
- ](https://googlefonts.github.io/noto-emoji-animation/)
- ](https://googlefonts.github.io/noto-emoji-animation/)
- ](https://googlefonts.github.io/noto-emoji-animation/)
- ](https://googlefonts.github.io/noto-emoji-animation/)