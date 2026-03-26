---
title: "getAvailableAudioCodecs()"
url: "https://www.remotion.dev/docs/webcodecs/get-available-audio-codecs"
path: "/docs/webcodecs/get-available-audio-codecs"
---

"---\nimage: /generated/articles-docs-webcodecs-get-available-audio-codecs.png\nid: get-available-audio-codecs\ntitle: getAvailableAudioCodecs()\nslug: /webcodecs/get-available-audio-codecs\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nGiven a container, get a list of audio codecs that the container can hold.  \nThis does not mean that a any audio stream of this codec can be put into the container.  \nUse [`canReencodeAudioTrack()`](/docs/webcodecs/can-reencode-audio-track) and [`canCopyAudioTrack()`](/docs/webcodecs/can-copy-audio-track) to determine this.\n\n```tsx twoslash title=\"Get available audio codecs for a container\"\nimport {getAvailableAudioCodecs} from '@remotion/webcodecs';\n\ngetAvailableAudioCodecs({container: 'webm'}); // ['opus']\n```\n\n## See also\n\n- [Track Transformation](/docs/webcodecs/track-transformation)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-available-audio-codecs.ts)\n"
]()]()
]()