---
title: "getAvailableVideoCodecs()"
url: "https://www.remotion.dev/docs/webcodecs/get-available-video-codecs"
path: "/docs/webcodecs/get-available-video-codecs"
---

"---\nimage: /generated/articles-docs-webcodecs-get-available-video-codecs.png\nid: get-available-video-codecs\ntitle: getAvailableVideoCodecs()\nslug: /webcodecs/get-available-video-codecs\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nGiven a container, get a list of video codecs that the container can hold.  \nThis does not mean that a any video stream of this codec can be put into the container.  \nUse [`canReencodeVideoTrack()`](/docs/webcodecs/can-reencode-video-track) and [`canCopyVideoTrack()`](/docs/webcodecs/can-copy-video-track) to determine this.\n\n```tsx twoslash title=\"Get available video codecs for a container\"\nimport {getAvailableVideoCodecs} from '@remotion/webcodecs';\n\ngetAvailableVideoCodecs({container: 'webm'}); // ['vp8', 'vp9']\n```\n\n## See also\n\n- [Track Transformation](/docs/webcodecs/track-transformation)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-available-video-codecs.ts)\n"
]()]()
]()