---
title: "<Gif>"
url: "https://www.remotion.dev/docs/gif/gif"
path: "/docs/gif/gif"
---

"---\nimage: /generated/articles-docs-gif-gif.png\nslug: gif\nsidebar_label: '<Gif>'\ntitle: '<Gif>'\ncrumb: '@remotion/gif'\n---\n\n_Part of the [`@remotion/gif`](/docs/gif) package_\n\nDisplays a GIF that synchronizes with Remotions [`useCurrentFrame()`](/docs/use-current-frame).\n\n```tsx twoslash\nimport {useRef} from 'react';\nimport {useVideoConfig} from 'remotion';\n// ---cut---\nimport {Gif} from '@remotion/gif';\n\nexport const MyComponent: React.FC = () => {\n  const {width, height} = useVideoConfig();\n  const ref = useRef<HTMLCanvasElement>(null);\n\n  return (\n    <Gif\n      ref={ref}\n      src=\"https://media.giphy.com/media/3o72F7YT6s0EMFI0Za/giphy.gif\"\n      width={width}\n      height={height}\n      fit=\"fill\"\n      playbackRate={2}\n    />\n  );\n};\n```\n\n## Props\n\n### `src`\n\nThe source of the GIF. Can be an URL or a local image - see [Importing assets](/docs/assets).\n\n:::note\nRemote GIFs need to support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).\n\n<details>\n  <summary>More info</summary>\n  <ul>\n    <li>\n      Remotion's origin is usually <code>http://localhost:3000</code>, but it\n      may be different if rendering on Lambda or the port is busy.\n    </li>\n    <li>\n      You can{' '}\n      <a href=\"/docs/chromium-flags#--disable-web-security\">disable CORS</a>{' '}\n      during renders.\n    </li>\n  </ul>\n</details>\n:::\n\n### `width`\n\nThe display width.\n\n### `height`\n\nThe display height.\n\n### `fit`\n\nMust be one of these values:\n\n- `'fill'`: The GIF will completely fill the container, and will be stretched if necessary. (_default_)\n- `'contain'`: The GIF is scaled to fit the box, while aspect ratio is maintained.\n- `'cover'`: The GIF completely fills the container and maintains it's aspect ratio. It will be cropped if necessary.\n\n### `onLoad`\n\nCallback that gets called once the GIF has loaded and finished processing. As its only argument, the callback gives the following object:\n\n- `width`: Width of the GIF file in pixels.\n- `height`: Height of the GIF file in pixels.\n- `delays`: Array of timestamps of type `number` containing position of each frame.\n- `frames`: Array of frames of type [`ImageData`](https://developer.mozilla.org/en-US/docs/Web/API/ImageData)\n\n### `style`\n\nAllows to pass in custom CSS styles. You may not pass `width` and `height`, instead use the props `width` and `height` to set the size of the GIF.\n\n### `loopBehavior`<AvailableFrom v=\"3.3.4\" />\n\nThe looping behavior of the GIF. Can be one of these values:\n\n- `'loop'`: The GIF will loop infinitely. (_default_)\n- `'pause-after-finish'`: The GIF will play once and then show the last frame.\n- `'unmount-after-finish'`: The GIF will play once and then unmount. Note that if you attach a `ref`, it will become `null` after the GIF has finished playing.\n\n### `ref`<AvailableFrom v=\"3.3.88\" />\n\nYou can add a [React ref](https://react.dev/learn/manipulating-the-dom-with-refs) to `<Gif>`. If you use TypeScript, you need to type it with `HTMLCanvasElement`.\n\n### playbackRate<AvailableFrom v=\"4.0.44\" />\n\nThe `playbackRate` prop controls the playback speed of the GIF animation within your Remotion video. It enables you to adjust how fast or slow the GIF animation plays, allowing for precise synchronization with your video content.\n\nDefault: 1 (Normal speed)\nValues:\n\n- `1`: Plays the GIF at normal speed.\n- `< 1`: Slows down the GIF speed (e.g., 0.5 plays it at half speed).\n- `> 1:` Speeds up the GIF speed (e.g., 2.0 plays it at double speed).\n\n### `delayRenderTimeoutInMilliseconds?`<AvailableFrom v=\"4.0.403\" />\n\nModifies the timeout of the internal [`delayRender()`](/docs/delay-render) call when loading the GIF. By default, Remotion will wait 30 seconds for the GIF to load before timing out. You can increase or decrease this timeout by passing a custom value.\n\nSee: [Modifying the timeout](/docs/delay-render#modifying-the-timeout)\n\n```tsx\n<Gif\n  src=\"https://example.com/large-gif.gif\"\n  delayRenderTimeoutInMilliseconds={60000} // 60 seconds\n/>\n```\n\n## Differences to `<AnimatedImage>`\n\n- `<Gif>` does not support animated AVIF and WebP images.\n- `<Gif>` works in Safari as well since it uses a JavaScript-based GIF decoder.\n- `<Gif>` supports the [`onLoad`](#onload) prop.\n\n## See also\n\n- [`<AnimatedImage>`](/docs/animatedimage)\n- [`getGifDurationInSeconds()`](/docs/gif/get-gif-duration-in-seconds)\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/gif/src/Gif.tsx)\n"

*Part of the [`@remotion/gif`](/docs/gif) package*

Displays a GIF that synchronizes with Remotions [`useCurrentFrame()`](/docs/use-current-frame).

```
import {Gif} from '@remotion/gif';

export const MyComponent: React.FC = () => {
  const {width, height} = useVideoConfig();
  const ref = useRef<HTMLCanvasElement>(null);

  return (
    <Gif
      ref={ref}
      src="https://media.giphy.com/media/3o72F7YT6s0EMFI0Za/giphy.gif"
      width={width}
      height={height}
      fit="fill"
      playbackRate={2}
    />
  );
};Copy
```

## Props[​](#props)

### `src`[​](#src)

The source of the GIF. Can be an URL or a local image - see [Importing assets](/docs/assets).
](/docs/assets)](/docs/assets)
](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)
- ](/docs/assets)