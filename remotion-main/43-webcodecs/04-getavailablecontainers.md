---
title: "getAvailableContainers()"
url: "https://www.remotion.dev/docs/webcodecs/get-available-containers"
path: "/docs/webcodecs/get-available-containers"
---

"---\nimage: /generated/articles-docs-webcodecs-get-available-containers.png\nid: get-available-containers\ntitle: getAvailableContainers()\nslug: /webcodecs/get-available-containers\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nReturns an array of available containers that can be used with the `convertMedia` function.\n\n```tsx twoslash title=\"Getting available containers\"\nimport {getAvailableContainers} from '@remotion/webcodecs';\n\nconst containers = getAvailableContainers();\nconsole.log(containers);\n```\n\n:::note\nNew containers may be added to this function and it will not be considered a breaking change.\n:::\n\n## As a type\n\nIf you need a TypeScript type that covers the available output containers, you can import the type definition:\n\n```tsx twoslash title=\"Type definition\"\nimport type {ConvertMediaContainer} from '@remotion/webcodecs';\n//                 ^?\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/get-available-containers.ts)\n"
]()]()
]()
- ]()