---
title: "Guide"
url: "https://www.remotion.dev/docs/webcodecs"
path: "/docs/webcodecs"
---

"---\nimage: /generated/articles-docs-webcodecs-index.png\nsidebar_label: Overview\ntitle: '@remotion/webcodecs'\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {TableOfContents, WebCodecsGuide} from './TableOfContents';\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n_available from v4.0.229_\n\nThis package provides APIs for converting videos in the browser.  \nIt leverages [`@remotion/media-parser`](/docs/media-parser) to parse the video and audio data, and then uses the [WebCodecs API](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) to encode the video.\n\nimport {LicenseDisclaimer} from './LicenseDisclaimer';\nimport {UnstableDisclaimer} from './UnstableDisclaimer';\n\n## What can you do with this package?\n\nIn browsers that implement WebCodecs, you can use this package to:\n\n- [Convert videos from one format to another](/docs/webcodecs/convert-a-video) (From .mp4, .webm, .mov, .mkv, .m3u8, .ts, .avi, .mp3, .flac, .wav, .m4a, .aac to .mp4, .webm, .wav)\n- [Rotate videos](/docs/webcodecs/rotate-a-video)\n- [Efficiently extract frames from a video](/docs/webcodecs/extract-frames)\n- Extract audio from a video\n- Manipulate the pixels of a video\n- [Fix videos that were recorded with `MediaRecorder`](/docs/webcodecs/fix-mediarecorder-video)\n- Soon: Compress, trim, crop videos\n\n## Is it fast?\n\nUnlike solutions which leverage WebAssembly, WebCodecs have full access to GPU acceleration.  \nYou can expect vastly faster processing than with online converters or WebAssembly-based processing.\n\nSee a [comparison](https://github.com/remotion-dev/webcodecs-benchmark) here.\n\n## 💼 License Disclaimer\n\n<LicenseDisclaimer />\n\n## 🚧 Unstable API Warning\n\n<UnstableDisclaimer />\n\n## Installation\n\n<Installation pkg=\"@remotion/webcodecs\" />\n\n## Guide\n\n<WebCodecsGuide />\n\n## APIs\n\nThe following APIs are available:\n\n<TableOfContents />\n"

]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()
- ]()