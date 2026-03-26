---
title: "getDefaultAudioCodec()"
url: "https://www.remotion.dev/docs/webcodecs/get-default-audio-codec"
path: "/docs/webcodecs/get-default-audio-codec"
---

"---\nimage: /generated/articles-docs-webcodecs-get-default-audio-codec.png\nid: get-default-audio-codec\ntitle: getDefaultAudioCodec()\nslug: /webcodecs/get-default-audio-codec\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\n:::warning\n**Unstable API**: This package is experimental. We might change the API at any time, until we remove this notice.\n:::\n\nGets the default audio codec for a container that `@remotion/webcodecs` uses if no other audio codec was specified.\n\n```tsx twoslash title=\"Get the default audio codec for a container\"\nimport {getDefaultAudioCodec} from '@remotion/webcodecs';\n\ngetDefaultAudioCodec({container: 'webm'}); // 'opus'\n```\n\nCurrently, the only supported container is `webm`, for which the default audio codec is `opus`.\n\n## Default audio codecs\n\nimport {DefaultAudioCodecs} from './DefaultAudioCodecs';\n\n<DefaultAudioCodecs />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-default-audio-codec.ts)\n- [`getDefaultVideoCodec()`](/docs/webcodecs/get-default-video-codec)\n"
]()]()
]()
- ]()