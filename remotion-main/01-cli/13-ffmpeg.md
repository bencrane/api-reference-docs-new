---
title: "ffmpeg"
url: "https://www.remotion.dev/docs/cli/ffmpeg"
path: "/docs/cli/ffmpeg"
---

"---\nimage: /generated/articles-docs-cli-ffmpeg.png\nid: ffmpeg\ntitle: npx remotion ffmpeg\ncrumb: '@remotion/cli'\nsidebar_label: 'ffmpeg'\n---\n\n_available since v4.0_\n\nIn order to use `ffmpeg` without having to directly install it, Remotion provides it via `npx remotion ffmpeg`.\n\nNote that in order to keep the binary size small, the FFmpeg binary only understand the codecs that Remotion itself supports: H.264, H.265, VP8, VP9 and ProRes. A binary from the 7.1 release line of FFmpeg is used.\n\n# Example\n\nConvert a video file to an audio file\n\n```bash\nnpx remotion ffmpeg -i input.mp4 output.mp3\n```\n\nTo find out more about FFmpeg, visit their [docs](https://ffmpeg.org/documentation.html).\n\n## See also\n\n- [`npx remotion ffprobe`](/docs/cli/ffprobe)\n"

*available since v4.0*

In order to use `ffmpeg` without having to directly install it, Remotion provides it via `npx remotion ffmpeg`.

Note that in order to keep the binary size small, the FFmpeg binary only understand the codecs that Remotion itself supports: H.264, H.265, VP8, VP9 and ProRes. A binary from the 7.1 release line of FFmpeg is used.

Convert a video file to an audio file

```
npx remotion ffmpeg -i input.mp4 output.mp3Copy
```

To find out more about FFmpeg, visit their [docs](https://ffmpeg.org/documentation.html).

## See also[​](#see-also)

- [`npx remotion ffprobe`](/docs/cli/ffprobe)
](/docs/cli/ffprobe)](/docs/cli/ffprobe)
](/docs/cli/ffprobe)