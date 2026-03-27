---
title: "@remotion/web-renderer"
url: "https://www.remotion.dev/docs/web-renderer/"
path: "/docs/web-renderer/"
---

"---\nimage: /generated/articles-docs-web-renderer-index.png\nsidebar_label: Overview\ntitle: '@remotion/web-renderer'\ncrumb: API\n---\n\n:::warning\nExperimental feature - expect bugs and breaking changes at any time.  \n[Track progress on GitHub](https://github.com/remotion-dev/remotion/issues/5913) and discuss in the [`#web-renderer`](https://remotion.dev/discord) channel on Discord.\n:::\n\nThis package allows you to render videos and stills directly in the browser, without requiring server-side infrastructure.\n\n### Key differences from server-side rendering\n\nUnlike server-side rendering with [`@remotion/renderer`](/docs/renderer), client-side rendering:\n\n- Runs in the browser instead of Node.js\n- Encodes with WebCodecs using [Mediabunny](/docs/mediabunny) instead of FFmpeg\n- Limited to a subset of tags and CSS properties - see [limitations](/docs/client-side-rendering/limitations)\n- No bundling step - takes components and video config directly\n\n## Installation\n\n<Installation pkg=\"@remotion/web-renderer\" />\n\n## API\n\nimport {TableOfContents} from './TableOfContents';\n\n<TableOfContents />\n\n## See also\n\n- [Client-side rendering overview](/docs/client-side-rendering)\n- [How client-side rendering works](/docs/client-side-rendering/how-it-works)\n- [Limitations](/docs/client-side-rendering/limitations)\n- [Telemetry](/docs/client-side-rendering/telemetry)\n- [Server-side rendering](/docs/ssr)\n"
]()]()
]()
- ]()
- ]()
- ]()