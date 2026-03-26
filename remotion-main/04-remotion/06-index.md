---
title: "<Composition>"
url: "https://www.remotion.dev/docs/composition"
path: "/docs/composition"
---

"---\nimage: /generated/articles-docs-composition.png\nid: composition\ntitle: <Composition>\ncrumb: 'API'\n---\n\nThis is the component to use to register a video to make it renderable and make it show up in the sidebar of the Remotion development interface.\n\nA composition represents the video you want to create, as a collection of clips (for example, several `<Sequence>`) that will play back to back to form your video.\n\n```tsx twoslash title=\"src/Root.tsx\"\nconst Component: React.FC = () => null;\n// ---cut---\n\nimport {Composition} from 'remotion';\n\nexport const RemotionRoot: React.FC = () => {\n  return (\n    <>\n      <Composition component={Component} durationInFrames={300} width={1080} height={1080} fps={30} id=\"test-render\" defaultProps={{}} />\n      {/* Additional compositions can be rendered */}\n    </>\n  );\n};\n```\n\n## API\n\nA `<Composition />` should be placed within a fragment of the root component (which is registered using [`registerRoot()`](/docs/register-root)).\n\nThe component takes the following props:\n\n### `id`\n\nID of the composition, as shown in the sidebar and also a unique identifier of the composition that you need to specify if you want to render it. The ID can only contain letters, numbers and `-`.\n\n### `fps`\n\nAt how many frames the composition should be rendered.\n\n### `durationInFrames`\n\nHow many frames the composition should be long.\n\n### `height`\n\nHeight of the composition in pixels.\n\n### `width`\n\nWidth of the composition in pixels.\n\n### `component` **or** `lazyComponent`\n\nPass the component in directly **or** pass a function that returns a dynamic import. Passing neither or both of the props is an error.\n\n:::note\nIf you use `lazyComponent`, Remotion will use React Suspense to load the component. Components will be compiled by Webpack as they are needed, which will reduce startup time of Remotion. If you use `lazyComponent`, you need to use a default export for your component. This is a restriction of React Suspense.\n:::\n\n### `defaultProps?`\n\nGive your component default props. Default props can be overriden using the [Props editor](/docs/visual-editing) and with [Input Props](/docs/props-resolution).\n\nProps must be an object that contains only pure JSON-serializable values.  \nFunctions, classes, and other non-serializable values will be lost while rendering.  \n(This restriction does not apply to the [`<Player>`](/docs/player/player), where you are allowed to pass functions as props.)\n\nYou may in addition use `Date`, `Map`, `Set` and [`staticFile()`](/docs/staticfile) in your default props and Remotion will guarantee the proper serialization.\n\n:::note\nType your components using the `React.FC<{}>` type and the `defaultProps` prop will be typesafe.\n:::\n\n:::note\nPassing huge objects to `defaultProps` can be slow. [Learn how to avoid it.](/docs/troubleshooting/defaultprops-too-big)\n:::\n\n:::note\nUse a `type`, not an `interface` to type your `defaultProps`. [Learn why](/docs/4-0-migration#cannot-use-an-interface-for-props)\n:::\n\n### `calculateMetadata`\n\nSee: [`calculateMetadata()`](/docs/calculate-metadata)\n\n### `schema`\n\nPass a Zod schema which your default props must satisfy. By doing so, you enable [visual editing](/docs/visual-editing). See: [Define a schema](/docs/schemas)\n\n## Example using `component`\n\n```tsx twoslash\n// @allowUmdGlobalAccess\n// @filename: ./MyComp.tsx\nexport const MyComp = () => <></>;\n\n// @filename: index.tsx\n// ---cut---\nimport {Composition} from 'remotion';\nimport {MyComp} from './MyComp';\n\nexport const MyVideo = () => {\n  return (\n    <>\n      <Composition id=\"my-comp\" component={MyComp} width={1080} height={1080} fps={30} durationInFrames={3 * 30} />\n    </>\n  );\n};\n```\n\n## Example using `lazyComponent`\n\n```tsx\nexport const MyVideo = () => {\n  return (\n    <>\n      <Composition id=\"my-comp\" lazyComponent={() => import('./LazyComponent')} width={1080} height={1080} fps={30} durationInFrames={3 * 30} />\n    </>\n  );\n};\n```\n\n## Organize compositions using folders\n\nYou can use the [`<Folder />`](/docs/folder) component to organize your compositions in the sidebar.\n\n```tsx twoslash\nimport React from 'react';\nconst Component: React.FC = () => null;\n// ---cut---\nimport {Composition, Folder} from 'remotion';\n\nexport const Video = () => {\n  return (\n    <>\n      <Folder name=\"Visuals\">\n        <Composition id=\"CompInFolder\" durationInFrames={100} fps={30} width={1080} height={1080} component={Component} />\n      </Folder>\n      <Composition id=\"CompOutsideFolder\" durationInFrames={100} fps={30} width={1080} height={1080} component={Component} />\n    </>\n  );\n};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering={false} serverSideRendering player={false} studio hideServers />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Composition.tsx)\n- [`registerRoot()`](/docs/register-root)\n- [The fundamentals](/docs/the-fundamentals)\n- [CLI options](/docs/cli)\n- [`<Sequence />`](/docs/sequence)\n- [`<Still />`](/docs/still)\n- [`<Folder />`](/docs/folder)\n- [Avoid huge payloads for `defaultProps`](/docs/troubleshooting/defaultprops-too-big)\n"

This is the component to use to register a video to make it renderable and make it show up in the sidebar of the Remotion development interface.

A composition represents the video you want to create, as a collection of clips (for example, several `<Sequence>`) that will play back to back to form your video.

```

src/Root.tsx
import {Composition} from 'remotion';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition component={Component} durationInFrames={300} width={1080} height={1080} fps={30} id="test-render" defaultProps={{}} />
      {/* Additional compositions can be rendered */}
    </>
  );
};Copy
```

## API[​](#api)

A `<Composition />` should be placed within a fragment of the root component (which is registered using [`registerRoot()`](/docs/register-root)).

The component takes the following props:

### `id`[​](#id)

ID of the composition, as shown in the sidebar and also a unique identifier of the composition that you need to specify if you want to render it. The ID can only contain letters, numbers and `-`.

### `fps`[​](#fps)

At how many frames the composition should be rendered.

### `durationInFrames`[​](#durationinframes)

How many frames the composition should be long.

### `height`[​](#height)

Height of the composition in pixels.

### `width`[​](#width)

Width of the composition in pixels.

### `component` **or** `lazyComponent`[​](#component-or-lazycomponent)

Pass the component in directly **or** pass a function that returns a dynamic import. Passing neither or both of the props is an error.
](#component-or-lazycomponent)](#component-or-lazycomponent)
](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)
- ](#component-or-lazycomponent)