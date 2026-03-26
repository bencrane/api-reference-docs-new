---
title: "<AnimatedImage>"
url: "https://www.remotion.dev/docs/animatedimage"
path: "/docs/animatedimage"
---

"---\nimage: /generated/articles-docs-animatedimage.png\nid: animatedimage\ntitle: '<AnimatedImage>'\ncrumb: 'API'\n---\n\n# `<AnimatedImage>`<AvailableFrom v=\"4.0.246\" />\n\nRenders an animated GIF, PNG, AVIF or WebP image and syncs it with Remotion's timeline.  \nRelies on the [`ImageDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/ImageDecoder) Web API, meaning it only works in Google Chrome and Firefox as of writing.\n\n```tsx twoslash title=\"Loading a remote animated image\"\nimport {AnimatedImage} from 'remotion';\n\nexport const WebpAnimatedImage = () => {\n  return <AnimatedImage src=\"https://mathiasbynens.be/demo/animated-webp-supported.webp\" />;\n};\n```\n\n```tsx twoslash title=\"Loading a local animated image\"\nimport {AnimatedImage, staticFile} from 'remotion';\n\nexport const GifAnimatedImage = () => {\n  return <AnimatedImage src={staticFile('giphy.gif')} />;\n};\n```\n\n## Props\n\n### `src`\n\nThe URL of the animated image. Can be a remote URL or a local file path.\n\n:::note\nRemote images need to support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).\n\n<details>\n  <summary>More info</summary>\n  <ul>\n    <li>\n      Remotion's origin is usually <code>http://localhost:3000</code>, but it may be different if rendering on Lambda or the port is busy.\n    </li>\n    <li>\n      You can <a href=\"/docs/chromium-flags#--disable-web-security\">disable CORS</a> during renders.\n    </li>\n  </ul>\n</details>\n:::\n\n### `width?`\n\nThe display width.\n\n### `height?`\n\nThe display height.\n\n### `fit?`\n\nMust be one of these values:\n\n- `'fill'`: The image will completely fill the container, and will be stretched if necessary. (_default_)\n- `'contain'`: The image is scaled to fit the box, while aspect ratio is maintained.\n- `'cover'`: The image completely fills the container and maintains it's aspect ratio. It will be cropped if necessary.\n\n### `style?`\n\nAllows to pass in custom CSS styles. You may not pass `width` and `height`, instead use the props `width` and `height` to set the size of the image.\n\n### `loopBehavior?`\n\nThe looping behavior of the animated image. Can be one of these values:\n\n- `'loop'`: The animated image will loop infinitely. (_default_)\n- `'pause-after-finish'`: The animated image will play once and then show the last frame.\n- `'clear-after-finish'`: The animated image will play once and then clear the canvas.\n\n### `playbackRate?`\n\nThe playback rate of the animated image. Defaults to `1`. For example, `2` will play the animation twice as fast, `0.5` will play it at half speed.\n\n### `ref?`<AvailableFrom v=\"3.3.88\" />\n\nYou can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to `<AnimatedImage />`. If you use TypeScript, you need to type it with `HTMLCanvasElement`.\n\n## Differences to `<Gif>`\n\n- `<AnimatedImage>` also supports AVIF, APNG and WebP images.\n- `<AnimatedImage>` uses the [`ImageDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/ImageDecoder) Web API, which has limited browser support.\n- `<AnimatedImage>` does not support the `onLoad` prop.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari={false} nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/animated-image/AnimatedImage.tsx)\n- [`<Gif>`](/docs/gif)\n"

Renders an animated GIF, PNG, AVIF or WebP image and syncs it with Remotion's timeline.

Relies on the [`ImageDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/ImageDecoder) Web API, meaning it only works in Google Chrome and Firefox as of writing.

```

Loading a remote animated imageimport {AnimatedImage} from 'remotion';

export const WebpAnimatedImage = () => {
  return <AnimatedImage src="https://mathiasbynens.be/demo/animated-webp-supported.webp" />;
};Copy
```

```

Loading a local animated imageimport {AnimatedImage, staticFile} from 'remotion';

export const GifAnimatedImage = () => {
  return <AnimatedImage src={staticFile('giphy.gif')} />;
};Copy
```

## Props[​](#props)

### `src`[​](#src)

The URL of the animated image. Can be a remote URL or a local file path.
](#src)](#src)
](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)
- ](#src)