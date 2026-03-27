---
title: "@remotion/three"
url: "https://www.remotion.dev/docs/three"
path: "/docs/three"
---

"---\nimage: /generated/articles-docs-three.png\nid: three\ntitle: '@remotion/three'\nsidebar_label: Overview\n---\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {ThreeDPlayer} from '../components/3DPhonePlayer.tsx';\nimport {TableOfContents} from './three/TableOfContents';\n\nis a package for integrating [React Three Fiber](https://github.com/pmndrs/react-three-fiber) with Remotion.\n\n- [`<ThreeCanvas />`](/docs/three-canvas) will allow you to use `useCurrentFrame()` and other Remotion hooks within a R3F Canvas. Animations are now not inside a `useFrame()` hook, but directly rendered into the markup.\n\n- [`useVideoTexture()`](/docs/use-video-texture) allows you to use a Remotion [`<Html5Video />`](/docs/html5-video) as a texture map.\n\n- [`useOffthreadVideoTexture()`](/docs/use-offthread-video-texture) is an equivalent to [`useVideoTexture()`](/docs/use-video-texture), but displays the exact frame as an `Three.ImageTexture` during rendering, simillarly to [`<OffthreadVideo />`](/docs/offthreadvideo).\n\nThese are the only two APIs provided - for everything else you can use the standard [React Three Fiber](https://github.com/pmndrs/react-three-fiber) APIs.\n\n## Starter template\n\nCheck out [remotion-template-three](https://github.com/remotion-dev/template-three), a minimal boilerplate for Remotion and React Three Fiber. It is a template repository, you can click \"Use this template\" on the GitHub repo to get started.\n\n<ThreeDPlayer />\n\nThe template features a 3D phone with a video inside which you can effortlessly swap out. Just as easily, you can change properties like the color, size, thickness, corner radius of the phone.\n\nThe template serves as a soft introduction on how to use `<ThreeCanvas />` and `useVideoTexture()`. You can easily delete everything inside the canvas to start working on a different idea.\n\n## Installation\n\n<Tabs\ndefaultValue=\"npm\"\nvalues={[\n{ label: 'npm', value: 'npm', },\n{ label: 'yarn', value: 'yarn', },\n{ label: 'pnpm', value: 'pnpm', },\n]\n}>\n<TabItem value=\"npm\">\n\n```bash\nnpm i three @react-three/fiber @remotion/three @types/three\n```\n\n  </TabItem>\n\n  <TabItem value=\"yarn\">\n\n```bash\nyarn add three @react-three/fiber @remotion/three @types/three\n```\n\n  </TabItem>\n  <TabItem value=\"pnpm\">\n\n```bash\npnpm i three @react-three/fiber @remotion/three @types/three\n```\n\n  </TabItem>\n</Tabs>\n\nYou are now set up and can render a [`<ThreeCanvas />`](/docs/three-canvas) in your project.\n\n## Note on `<Sequence>`\n\nA [`<Sequence>`](/docs/sequence) by default will return a `<div>` component, which is not allowed inside a `<ThreeCanvas>`. To avoid an error, pass `layout=\"none\"` to `<Sequence>`.\n\n## Note on server-side rendering\n\nThree.JS does not render with the default OpenGL renderer - we recommend to set it to `angle`. The config file of new projects includes by default:\n\n```ts twoslash\nimport {Config} from '@remotion/cli/config';\n\nConfig.setChromiumOpenGlRenderer('angle');\n```\n\nSince the config file does not apply to server-side rendering, you need to explicitly add\n\n```json\n\"chromiumOptions\": {\n  \"gl\": \"angle\"\n}\n```\n\nto server-side rendering APIs like [`renderMedia()`](/docs/renderer/render-media), [`renderFrames()`](/docs/renderer/render-frames), [`getCompositions()`](/docs/renderer/get-compositions), [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) and [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel).\n\n## Thanks\n\nA big thanks to [Björn Zeutzheim](https://github.com/olee) for researching and discovering the techniques needed for React Three Fiber integration and for doing the initial implementation of the @remotion/three APIs.\n\n## APIs\n\n<TableOfContents />\n"

is a package for integrating [React Three Fiber](https://github.com/pmndrs/react-three-fiber) with Remotion.

- 

[`<ThreeCanvas />`](/docs/three-canvas) will allow you to use `useCurrentFrame()` and other Remotion hooks within a R3F Canvas. Animations are now not inside a `useFrame()` hook, but directly rendered into the markup.

- 

[`useVideoTexture()`](/docs/use-video-texture) allows you to use a Remotion [`<Html5Video />`](/docs/html5-video) as a texture map.

- 

[`useOffthreadVideoTexture()`](/docs/use-offthread-video-texture) is an equivalent to [`useVideoTexture()`](/docs/use-video-texture), but displays the exact frame as an `Three.ImageTexture` during rendering, simillarly to [`<OffthreadVideo />`](/docs/offthreadvideo).

These are the only two APIs provided - for everything else you can use the standard [React Three Fiber](https://github.com/pmndrs/react-three-fiber) APIs.

## Starter template[​](#starter-template)

Check out [remotion-template-three](https://github.com/remotion-dev/template-three), a minimal boilerplate for Remotion and React Three Fiber. It is a template repository, you can click "Use this template" on the GitHub repo to get started.

The template features a 3D phone with a video inside which you can effortlessly swap out. Just as easily, you can change properties like the color, size, thickness, corner radius of the phone.

The template serves as a soft introduction on how to use `<ThreeCanvas />` and `useVideoTexture()`. You can easily delete everything inside the canvas to start working on a different idea.

## Installation[​](#installation)

- npm
- yarn
- pnpm

```
npm i three @react-three/fiber @remotion/three @types/threeCopy
```

```
yarn add three @react-three/fiber @remotion/three @types/threeCopy
```

```
pnpm i three @react-three/fiber @remotion/three @types/threeCopy
```

You are now set up and can render a [`<ThreeCanvas />`](/docs/three-canvas) in your project.

## Note on `<Sequence>`[​](#note-on-sequence)

A [`<Sequence>`](/docs/sequence) by default will return a `<div>` component, which is not allowed inside a `<ThreeCanvas>`. To avoid an error, pass `layout="none"` to `<Sequence>`.

## Note on server-side rendering[​](#note-on-server-side-rendering)

Three.JS does not render with the default OpenGL renderer - we recommend to set it to `angle`. The config file of new projects includes by default:

```
import {Config} from '@remotion/cli/config';

Config.setChromiumOpenGlRenderer('angle');Copy
```

Since the config file does not apply to server-side rendering, you need to explicitly add

```
"chromiumOptions": {
  "gl": "angle"
}Copy
```

to server-side rendering APIs like [`renderMedia()`](/docs/renderer/render-media), [`renderFrames()`](/docs/renderer/render-frames), [`getCompositions()`](/docs/renderer/get-compositions), [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) and [`renderMediaOnVercel()`](/docs/vercel/render-media-on-vercel).

## Thanks[​](#thanks)

A big thanks to [Björn Zeutzheim](https://github.com/olee) for researching and discovering the techniques needed for React Three Fiber integration and for doing the initial implementation of the @remotion/three APIs.

## APIs[​](#apis)

[
**<ThreeCanvas>**
A wrapper for React Three Fiber' Canvas](/docs/three-canvas)[
**useVideoTexture(**
Use a video in React Three Fiber ](/docs/use-video-texture)[
**useOffthreadVideoTexture()**
Use an <OffthreadVideo> in React Three Fiber ](/docs/use-offthread-video-texture)](/docs/use-offthread-video-texture)](/docs/use-offthread-video-texture)
](/docs/use-offthread-video-texture)
- ](/docs/use-offthread-video-texture)
- ](/docs/use-offthread-video-texture)
- ](/docs/use-offthread-video-texture)
- ](/docs/use-offthread-video-texture)
- ](/docs/use-offthread-video-texture)