---
title: "Supported media"
url: "https://www.remotion.dev/docs/media/support"
path: "/docs/media/support"
---

"---\nimage: /generated/articles-docs-media-support.png\ntitle: Supported media\nsidebar_label: Supported media\ncrumb: '@remotion/media'\n---\n\nThe new [`<Audio>`](/docs/media/audio) and [`<Video>`](/docs/media/video) tags from `@remotion/media` are based on [Mediabunny](https://mediabunny.dev) and WebCodecs.\n\n## CORS\n\nAny assets must be either CORS-enabled or served from the bundle using [`staticFile()`](/docs/staticfile).\n\n## Supported formats and codecs\n\nThe supported formats and codecs are defined here: [Mediabunny - Supported formats and codecs](/docs/mediabunny/formats).\n\n## Matroska limitation\n\nMatroska-based files (`.mkv`, `.webm`) are supported, but for the audio to be extracted, the entire audio up to the point of extraction must be extracted as well because Matroska containers only store millisecond-precise timestamps in the container, but more precision is needed correctly concatenate audio parts.\n\nFor example: If you want to render the third minute of a 10 minute audio, the first 2 minutes of the audio must be decoded as well because only then the precise timestamps of the audio will be unveiled.\n\nPrefer non-Matroska-based files (`.mp4`, `.mov`, `.m4a`) when you are doing distributed rendering (e.g. on Lambda) if possible.\n\n## Fallback to `<OffthreadVideo>`\n\nIf a media file cannot be decoded, be it because of an unsupported codec or because it does not support CORS, or it has an alpha channel and the browser does not support WebGL which is required to decode the alpha channel, then `@remotion/media` automatically falls back to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) from the [`remotion`](/docs/remotion) package.\n\nSee: [Fallback from `@remotion/media` to `<OffthreadVideo>` or `<Html5Audio>`](/docs/media/fallback)\n"

The new [`<Audio>`](/docs/media/audio) and [`<Video>`](/docs/media/video) tags from `@remotion/media` are based on [Mediabunny](https://mediabunny.dev) and WebCodecs.

## CORS[​](#cors)

Any assets must be either CORS-enabled or served from the bundle using [`staticFile()`](/docs/staticfile).

## Supported formats and codecs[​](#supported-formats-and-codecs)

The supported formats and codecs are defined here: [Mediabunny - Supported formats and codecs](/docs/mediabunny/formats).

## Matroska limitation[​](#matroska-limitation)

Matroska-based files (`.mkv`, `.webm`) are supported, but for the audio to be extracted, the entire audio up to the point of extraction must be extracted as well because Matroska containers only store millisecond-precise timestamps in the container, but more precision is needed correctly concatenate audio parts.

For example: If you want to render the third minute of a 10 minute audio, the first 2 minutes of the audio must be decoded as well because only then the precise timestamps of the audio will be unveiled.

Prefer non-Matroska-based files (`.mp4`, `.mov`, `.m4a`) when you are doing distributed rendering (e.g. on Lambda) if possible.

## Fallback to `<OffthreadVideo>`[​](#fallback-to-offthreadvideo)

If a media file cannot be decoded, be it because of an unsupported codec or because it does not support CORS, or it has an alpha channel and the browser does not support WebGL which is required to decode the alpha channel, then `@remotion/media` automatically falls back to [`<OffthreadVideo>`](/docs/offthreadvideo) or [`<Html5Audio>`](/docs/html5-audio) from the [`remotion`](/docs/remotion) package.

See: [Fallback from `@remotion/media` to `<OffthreadVideo>` or `<Html5Audio>`](/docs/media/fallback)](/docs/media/fallback)](/docs/media/fallback)
](/docs/media/fallback)
- ](/docs/media/fallback)
- ](/docs/media/fallback)
- ](/docs/media/fallback)