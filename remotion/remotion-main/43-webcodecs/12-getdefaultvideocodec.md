---
title: "getDefaultVideoCodec()"
url: "https://www.remotion.dev/docs/webcodecs/get-default-video-codec"
path: "/docs/webcodecs/get-default-video-codec"
---

"---\nimage: /generated/articles-docs-webcodecs-get-default-video-codec.png\nid: get-default-video-codec\ntitle: getDefaultVideoCodec()\nslug: /webcodecs/get-default-video-codec\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\n:::warning\n**Unstable API**: This package is experimental. We might change the API at any time, until we remove this notice.\n:::\n\nGets the default video codec for a container that `@remotion/webcodecs` uses if no other audio codec was specified.\n\n```tsx twoslash title=\"Get the default video codec for a container\"\nimport {getDefaultVideoCodec} from '@remotion/webcodecs';\n\ngetDefaultVideoCodec({container: 'webm'}); // 'vp8'\n```\n\nimport {DefaultVideoCodecs} from './DefaultVideoCodecs';\n\n## Default video codecs\n\n<DefaultVideoCodecs />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-default-video-codec.ts)\n- [`getDefaultAudioCodec()`](/docs/webcodecs/get-default-audio-codec)\n"
]()]()
]()
- ]()