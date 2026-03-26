---
title: "getGifDurationInSeconds()"
url: "https://www.remotion.dev/docs/gif/get-gif-duration-in-seconds"
path: "/docs/gif/get-gif-duration-in-seconds"
---

"---\nimage: /generated/articles-docs-gif-get-gif-duration-in-seconds.png\ntitle: getGifDurationInSeconds()\nid: get-gif-duration-in-seconds\ncrumb: '@remotion/gif'\n---\n\n_Part of the [`@remotion/gif`](/docs/gif) package_\n\n<AvailableFrom v=\"3.2.22\" />\n\nGets the duration in seconds of a GIF.\n\n:::note\nRemote GIFs need to support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).\n\n<details>\n  <summary>More info</summary>\n  <ul>\n    <li>\n      Remotion's origin is usually <code>http://localhost:3000</code>, but it may be different if rendering on Lambda or the port is busy.\n    </li>\n    <li>\n      You can <a href=\"/docs/chromium-flags#--disable-web-security\">disable CORS</a> during renders.\n    </li>\n  </ul>\n</details>\n:::\n\n## Arguments\n\n### `src`\n\nA string pointing to a GIF asset\n\n## Return value\n\n`Promise<number>` - the duration of the GIF in seconds, not factoring in that whether it is looped.\n\n## Example\n\n```tsx twoslash\nimport {useCallback, useEffect} from 'react';\nimport {staticFile} from 'remotion';\n// ---cut---\nimport {getGifDurationInSeconds} from '@remotion/gif';\nimport gif from './cat.gif';\n\nconst MyComp: React.FC = () => {\n  const getDuration = useCallback(async () => {\n    const imported = await getGifDurationInSeconds(gif); // 127.452\n    const publicFile = await getGifDurationInSeconds(staticFile('giphy.gif')); // 2.10\n    const remote = await getGifDurationInSeconds('https://media.giphy.com/media/xT0GqH01ZyKwd3aT3G/giphy.gif'); // 3.23\n  }, []);\n\n  useEffect(() => {\n    getDuration();\n  }, []);\n\n  return null;\n};\n```\n\n## See also\n\n- [`<Gif>`](/docs/gif/gif)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/gif/src/get-gif-duration-in-seconds.ts)\n"

*Part of the [`@remotion/gif`](/docs/gif) package*
[v3.2.22](https://github.com/remotion-dev/remotion/releases/v3.2.22)

Gets the duration in seconds of a GIF.
](https://github.com/remotion-dev/remotion/releases/v3.2.22)](https://github.com/remotion-dev/remotion/releases/v3.2.22)
](https://github.com/remotion-dev/remotion/releases/v3.2.22)
- ](https://github.com/remotion-dev/remotion/releases/v3.2.22)
- ](https://github.com/remotion-dev/remotion/releases/v3.2.22)
- ](https://github.com/remotion-dev/remotion/releases/v3.2.22)
- ](https://github.com/remotion-dev/remotion/releases/v3.2.22)