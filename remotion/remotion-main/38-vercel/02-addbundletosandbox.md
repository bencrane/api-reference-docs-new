---
title: "addBundleToSandbox()"
url: "https://www.remotion.dev/docs/vercel/add-bundle-to-sandbox"
path: "/docs/vercel/add-bundle-to-sandbox"
---

"---\nimage: /generated/articles-docs-vercel-add-bundle-to-sandbox.png\ntitle: addBundleToSandbox()\ncrumb: '@remotion/vercel'\n---\n\n# addBundleToSandbox()<AvailableFrom v=\"4.0.426\" />\n\n:::warning\nExperimental package: We reserve the right to make breaking changes in order to correct bad design decisions until this notice is gone.\n:::\n\nCopies your Remotion bundle into a sandbox. Call this after [`createSandbox()`](/docs/vercel/create-sandbox) to add your bundle files.\n\n## Example\n\n```ts twoslash title=\"create-snapshot.ts\"\n// @module: es2022\n// @target: es2022\nimport {addBundleToSandbox, createSandbox} from '@remotion/vercel';\n// ---cut---\nconst sandbox = await createSandbox();\n\nawait addBundleToSandbox({\n  sandbox,\n  bundleDir: '/path/to/bundle',\n});\n\n// ... use the sandbox\n\nawait sandbox.stop();\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `sandbox`\n\nA [`Sandbox`](https://vercel.com/docs/vercel-sandbox/sdk-reference#sandbox-class) instance, typically obtained from [`createSandbox()`](/docs/vercel/create-sandbox).\n\n### `bundleDir`\n\nThe path to your Remotion bundle directory, relative to the current working directory.  \nA bundle can be created using the [`npx remotion bundle`](/docs/cli/bundle) command, or using the [`bundle()`](/docs/bundle) API.\n\n## Return value\n\n`Promise<void>` — resolves when the bundle has been copied into the sandbox.\n\n## See also\n\n- [`createSandbox()`](/docs/vercel/create-sandbox)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/vercel/src/add-bundle-to-sandbox.ts)\n"

]()]()
]()
- ]()
- ]()
- ]()
- ]()
- ]()