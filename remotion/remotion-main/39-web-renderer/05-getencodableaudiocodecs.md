---
title: "getEncodableAudioCodecs()"
url: "https://www.remotion.dev/docs/web-renderer/get-encodable-audio-codecs"
path: "/docs/web-renderer/get-encodable-audio-codecs"
---

"---\nimage: /generated/articles-docs-web-renderer-get-encodable-audio-codecs.png\nid: get-encodable-audio-codecs\ntitle: getEncodableAudioCodecs()\ncrumb: '@remotion/web-renderer'\n---\n\n:::warning\nExperimental feature - expect bugs and breaking changes at any time.  \n[Track progress on GitHub](https://github.com/remotion-dev/remotion/issues/5913) and discuss in the [`#web-renderer`](https://remotion.dev/discord) channel on Discord.\n:::\n\n_Part of the `@remotion/web-renderer` package._\n\nReturns the audio codecs that the current browser can encode for a given container format.\n\nUse this function to dynamically show users which audio codecs are available in their browser.\n\n```tsx twoslash title=\"Example usage\"\nimport {getEncodableAudioCodecs} from '@remotion/web-renderer';\n\nconst codecs = await getEncodableAudioCodecs('mp4');\nconsole.log(codecs); // e.g. ['aac', 'opus'] or ['opus'] on Firefox\n```\n\n## Arguments\n\n### `container`\n\n_string_ <TsType type=\"WebRendererContainer\" source=\"@remotion/web-renderer\" /> - required\n\nThe container format: `\"mp4\"` or `\"webm\"`.\n\n### `options?`\n\n_object_ <TsType type=\"GetEncodableAudioCodecsOptions\" source=\"@remotion/web-renderer\" />\n\nOptional configuration object.\n\n#### `audioBitrate?`\n\n_number | string_ <TsType type=\"WebRendererQuality\" source=\"@remotion/web-renderer\" />\n\nA number (bits per second) or quality preset (`\"very-low\"`, `\"low\"`, `\"medium\"`, `\"high\"`, `\"very-high\"`).\n\n## Return value\n\nReturns a `Promise<WebRendererAudioCodec[]>` - an array of audio codec identifiers that the browser can encode.\n\nPossible values: `\"aac\"`, `\"opus\"`\n\n:::note\nAAC encoding is not supported in Firefox. On Firefox, only `[\"opus\"]` will be returned for both containers.\n:::\n\n## See also\n\n- [`getEncodableVideoCodecs()`](/docs/web-renderer/get-encodable-video-codecs)\n- [`canRenderMediaOnWeb()`](/docs/web-renderer/can-render-media-on-web)\n- [`renderMediaOnWeb()`](/docs/web-renderer/render-media-on-web)\n"
]()]()
]()
- ]()
- ]()
- ]()
- ]()