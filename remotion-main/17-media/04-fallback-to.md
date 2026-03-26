---
title: "Fallback to <OffthreadVideo>"
url: "https://www.remotion.dev/docs/media/fallback"
path: "/docs/media/fallback"
---

"---\nimage: /generated/articles-docs-media-fallback.png\ntitle: 'Fallback from @remotion/media to <OffthreadVideo> or <Html5Audio>'\nsidebar_label: 'Fallback to <OffthreadVideo>'\ncrumb: '@remotion/media'\n---\n\nSometimes, a media file cannot be embedded using [`@remotion/media`](/docs/media)'s [`<Video>`](/docs/media/video) and [`<Audio>`](/docs/media/audio) tags.  \nIn such cases, a fallback to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) from the `remotion` package is attempted.\n\n## When a fallback is attempted\n\nHere are some cases where [`@remotion/media`](/docs/media) may fall back to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) from `remotion`:\n\n- The resource fails to load due to [CORS restrictions](/docs/cors-issues)\n- The container format is not supported by [Mediabunny](/docs/mediabunny/formats)\n- The codec cannot be decoded by WebCodecs (e.g. a H.265 stream during rendering)\n- The video has an alpha channel and the browser does not support WebGL which is required to decode the alpha channel. The default configuration of the headless browser does not have WebGL enabled.\n\n## Observing when a fallback happens\n\nIf [`@remotion/media`](/docs/media) falls back to another tag, then a warning message will be logged in the render:\n\n```\nCannot decode /public/video-h265.mp4, falling back to <OffthreadVideo>\n```\n\nIf you are rendering on an environment where the logs are not immediately visible (e.g. Lambda), observe whether a fallback has happened by visiting the logs (e.g. CloudWatch).\n\n## Preventing a fallback from happening\n\nTo prevent [`<Video>`](/docs/media/video) from falling back to [`<OffthreadVideo>`](/docs/offthreadvideo), set the [`disallowFallbackToOffthreadVideo`](/docs/media/video#disallowfallbacktooffthreadvideo) prop:\n\n```tsx twoslash title=\"No fallback to OffthreadVideo\"\nimport {Video} from '@remotion/media';\n\nexport const MyComp: React.FC = () => {\n  return <Video src=\"https://remotion.media/video.mp4\" disallowFallbackToOffthreadVideo />;\n};\n```\n\nTo prevent [`<Audio>`](/docs/media/audio) from falling back to [`<Html5Audio>`](/docs/html5-audio) from [`remotion`](/docs/remotion), set the [`disallowFallbackToHtml5Audio`](/docs/media/audio#disallowfallbacktohtml5audio) prop:\n\n```tsx twoslash title=\"No fallback to HTML5 audio tag\"\nimport {Audio} from '@remotion/media';\n\nexport const MyComp: React.FC = () => {\n  return <Audio src=\"https://remotion.media/audio.mp3\" disallowFallbackToHtml5Audio />;\n};\n```\n\nIf a fallback is prevented, the render will be cancelled instead.\n\n## Behavior of the `loop` prop during fallback\n\nThe [`loop`](/docs/media/video#loop) prop of [`<Video>`](/docs/media/video) is handled differently depending on the environment:\n\n**During preview**, the fallback uses [`<Html5Video>`](/docs/html5-video), which natively supports the `loop` prop. Looping works as expected.\n\n**During rendering**, [`<OffthreadVideo>`](/docs/offthreadvideo) does not natively support looping. To work around this, `@remotion/media` attempts to determine the duration of the video and automatically wraps [`<OffthreadVideo>`](/docs/offthreadvideo) in a [`<Loop>`](/docs/loop) component.\n\n- In most cases, the duration can be extracted from the media container even if the codec is not supported.\n- If the duration **cannot** be determined (e.g. due to [CORS issues](/docs/cors-issues) or a broken container), the render will fail with an error.\n\nTo ensure looping works reliably during rendering, make sure:\n\n- The video file is valid and not corrupted\n- There are no [CORS issues](/docs/cors-issues) preventing the file from being read\n\n## Fallback is not possible in client-side rendering\n\nWhen using [`@remotion/web-renderer`](/docs/web-renderer) for client-side rendering, fallback to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) is **not possible**.\n\nThis is because these fallback components require server-side capabilities that are not available in the browser.\n\nIf a media file cannot be rendered using [`@remotion/media`](/docs/media) during client-side rendering, the render will fail with an error message describing the issue.\n"

Sometimes, a media file cannot be embedded using [`@remotion/media`](/docs/media)'s [`<Video>`](/docs/media/video) and [`<Audio>`](/docs/media/audio) tags.

In such cases, a fallback to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) from the `remotion` package is attempted.

## When a fallback is attempted[​](#when-a-fallback-is-attempted)

Here are some cases where [`@remotion/media`](/docs/media) may fall back to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) from `remotion`:

- The resource fails to load due to [CORS restrictions](/docs/cors-issues)

- The container format is not supported by [Mediabunny](/docs/mediabunny/formats)

- The codec cannot be decoded by WebCodecs (e.g. a H.265 stream during rendering)

- The video has an alpha channel and the browser does not support WebGL which is required to decode the alpha channel. The default configuration of the headless browser does not have WebGL enabled.

## Observing when a fallback happens[​](#observing-when-a-fallback-happens)

If [`@remotion/media`](/docs/media) falls back to another tag, then a warning message will be logged in the render:

```
Cannot decode /public/video-h265.mp4, falling back to <OffthreadVideo>Copy
```

If you are rendering on an environment where the logs are not immediately visible (e.g. Lambda), observe whether a fallback has happened by visiting the logs (e.g. CloudWatch).

## Preventing a fallback from happening[​](#preventing-a-fallback-from-happening)

To prevent [`<Video>`](/docs/media/video) from falling back to [`<OffthreadVideo>`](/docs/offthreadvideo), set the [`disallowFallbackToOffthreadVideo`](/docs/media/video#disallowfallbacktooffthreadvideo) prop:

```

No fallback to OffthreadVideoimport {Video} from '@remotion/media';

export const MyComp: React.FC = () => {
  return <Video src="https://remotion.media/video.mp4" disallowFallbackToOffthreadVideo />;
};Copy
```

To prevent [`<Audio>`](/docs/media/audio) from falling back to [`<Html5Audio>`](/docs/html5-audio) from [`remotion`](/docs/remotion), set the [`disallowFallbackToHtml5Audio`](/docs/media/audio#disallowfallbacktohtml5audio) prop:

```

No fallback to HTML5 audio tagimport {Audio} from '@remotion/media';

export const MyComp: React.FC = () => {
  return <Audio src="https://remotion.media/audio.mp3" disallowFallbackToHtml5Audio />;
};Copy
```

If a fallback is prevented, the render will be cancelled instead.

## Behavior of the `loop` prop during fallback[​](#behavior-of-the-loop-prop-during-fallback)

The [`loop`](/docs/media/video#loop) prop of [`<Video>`](/docs/media/video) is handled differently depending on the environment:

**During preview**, the fallback uses [`<Html5Video>`](/docs/html5-video), which natively supports the `loop` prop. Looping works as expected.

**During rendering**, [`<OffthreadVideo>`](/docs/offthreadvideo) does not natively support looping. To work around this, `@remotion/media` attempts to determine the duration of the video and automatically wraps [`<OffthreadVideo>`](/docs/offthreadvideo) in a [`<Loop>`](/docs/loop) component.

- In most cases, the duration can be extracted from the media container even if the codec is not supported.

- If the duration **cannot** be determined (e.g. due to [CORS issues](/docs/cors-issues) or a broken container), the render will fail with an error.

To ensure looping works reliably during rendering, make sure:

- The video file is valid and not corrupted

- There are no [CORS issues](/docs/cors-issues) preventing the file from being read

## Fallback is not possible in client-side rendering[​](#fallback-is-not-possible-in-client-side-rendering)

When using [`@remotion/web-renderer`](/docs/web-renderer) for client-side rendering, fallback to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) is **not possible**.

This is because these fallback components require server-side capabilities that are not available in the browser.

If a media file cannot be rendered using [`@remotion/media`](/docs/media) during client-side rendering, the render will fail with an error message describing the issue.](/docs/media)](/docs/media)
](/docs/media)
- ](/docs/media)
- ](/docs/media)
- ](/docs/media)
- ](/docs/media)