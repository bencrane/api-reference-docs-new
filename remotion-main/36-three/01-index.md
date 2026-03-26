---
title: "<ThreeCanvas>"
url: "https://www.remotion.dev/docs/three-canvas"
path: "/docs/three-canvas"
---

"---\nimage: /generated/articles-docs-three-canvas.png\nid: three-canvas\ntitle: <ThreeCanvas>\ncrumb: '@remotion/three'\n---\n\nA wrapper for [React Three Fiber](https://github.com/pmndrs/react-three-fiber)'s `<Canvas />` which synchronizes with Remotions [`useCurrentFrame()`](/docs/use-current-frame).\n\nSince React Three Fiber is a custom renderer, normally the React contexts that surround it don't work inside. This would normally break the usage of it in Remotion, but this component wraps the contexts so you can write your markup as expected.\n\nInstead of using React Three Fibers `useFrame` API, you can (and must) write your animations fully declaratively using Remotions `useCurrentFrame` API. This will ensure that you can scrub back and forth in the timeline and pause the animation.\n\nA browser bug [would normally cause the layout to be broken](https://github.com/pmndrs/react-three-fiber/issues/1394) because we apply a `scale` transform to the canvas in the Studio. To work around this problem, the `<ThreeCanvas />` requires the `width` and `height` props to be set.\n\n## Example\n\nA spinning, color changing, scaling cube. This example can also be found in the `examples` folder of the Remotion repo.\n\n```tsx twoslash\nimport {ThreeCanvas} from '@remotion/three';\nimport {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';\n\nconst ThreeBasic: React.FC = () => {\n  const frame = useCurrentFrame();\n  const {width, height} = useVideoConfig();\n\n  return (\n    <ThreeCanvas\n      orthographic={false}\n      width={width}\n      height={height}\n      style={{\n        backgroundColor: 'white',\n      }}\n      camera={{fov: 75, position: [0, 0, 470]}}\n    >\n      <ambientLight intensity={0.15} />\n      <pointLight args={[undefined, 0.4]} position={[200, 200, 0]} />\n      <mesh position={[0, 0, 0]} rotation={[frame * 0.06 * 0.5, frame * 0.07 * 0.5, frame * 0.08 * 0.5]} scale={interpolate(Math.sin(frame / 10), [-1, 1], [0.8, 1.2])}>\n        <boxGeometry args={[100, 100, 100]} />\n        <meshStandardMaterial color={[Math.sin(frame * 0.12) * 0.5 + 0.5, Math.cos(frame * 0.11) * 0.5 + 0.5, Math.sin(frame * 0.08) * 0.5 + 0.5]} />\n      </mesh>\n    </ThreeCanvas>\n  );\n};\n\nexport default ThreeBasic;\n```\n\n## `frameloop` behavior during rendering\n\nDuring rendering, `<ThreeCanvas>` overrides the `frameloop` prop to `'never'` regardless of what you pass. This means the Three.js scene will not re-render on its own — it is only re-rendered on demand via `advance()`.\n\nIf you update textures asynchronously (e.g. from a [`<Video>`](/docs/media/video) `onVideoFrame` callback), you must call `advance(performance.now())` instead of `invalidate()` to synchronously re-render the scene before the frame is captured. See [Using a video as a texture](/docs/videos/as-threejs-texture) for a full example.\n\n## Note on `<Sequence>`\n\nA [`<Sequence>`](/docs/sequence) by default will return a `<div>` component which is not allowed inside a `<ThreeCanvas>`. To avoid an error, pass `layout=\"none\"` to `<Sequence>`.\n\n## Using videos inside a `<ThreeCanvas>`\n\nYou can create a Three.js texture backed by a [`<Video>`](/docs/media/video) by using [this](/docs/videos/as-threejs-texture) approach.\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)\n"

A wrapper for [React Three Fiber](https://github.com/pmndrs/react-three-fiber)'s `<Canvas />` which synchronizes with Remotions [`useCurrentFrame()`](/docs/use-current-frame).

Since React Three Fiber is a custom renderer, normally the React contexts that surround it don't work inside. This would normally break the usage of it in Remotion, but this component wraps the contexts so you can write your markup as expected.

Instead of using React Three Fibers `useFrame` API, you can (and must) write your animations fully declaratively using Remotions `useCurrentFrame` API. This will ensure that you can scrub back and forth in the timeline and pause the animation.

A browser bug [would normally cause the layout to be broken](https://github.com/pmndrs/react-three-fiber/issues/1394) because we apply a `scale` transform to the canvas in the Studio. To work around this problem, the `<ThreeCanvas />` requires the `width` and `height` props to be set.

## Example[​](#example)

A spinning, color changing, scaling cube. This example can also be found in the `examples` folder of the Remotion repo.

```
import {ThreeCanvas} from '@remotion/three';
import {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';

const ThreeBasic: React.FC = () => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();

  return (
    <ThreeCanvas
      orthographic={false}
      width={width}
      height={height}
      style={{
        backgroundColor: 'white',
      }}
      camera={{fov: 75, position: [0, 0, 470]}}
    >
      <ambientLight intensity={0.15} />
      <pointLight args={[undefined, 0.4]} position={[200, 200, 0]} />
      <mesh position={[0, 0, 0]} rotation={[frame * 0.06 * 0.5, frame * 0.07 * 0.5, frame * 0.08 * 0.5]} scale={interpolate(Math.sin(frame / 10), [-1, 1], [0.8, 1.2])}>
        <boxGeometry args={[100, 100, 100]} />
        <meshStandardMaterial color={[Math.sin(frame * 0.12) * 0.5 + 0.5, Math.cos(frame * 0.11) * 0.5 + 0.5, Math.sin(frame * 0.08) * 0.5 + 0.5]} />
      </mesh>
    </ThreeCanvas>
  );
};

export default ThreeBasic;Copy
```

## `frameloop` behavior during rendering[​](#frameloop-behavior-during-rendering)

During rendering, `<ThreeCanvas>` overrides the `frameloop` prop to `'never'` regardless of what you pass. This means the Three.js scene will not re-render on its own — it is only re-rendered on demand via `advance()`.

If you update textures asynchronously (e.g. from a [`<Video>`](/docs/media/video) `onVideoFrame` callback), you must call `advance(performance.now())` instead of `invalidate()` to synchronously re-render the scene before the frame is captured. See [Using a video as a texture](/docs/videos/as-threejs-texture) for a full example.

## Note on `<Sequence>`[​](#note-on-sequence)

A [`<Sequence>`](/docs/sequence) by default will return a `<div>` component which is not allowed inside a `<ThreeCanvas>`. To avoid an error, pass `layout="none"` to `<Sequence>`.

## Using videos inside a `<ThreeCanvas>`[​](#using-videos-inside-a-threecanvas)

You can create a Three.js texture backed by a [`<Video>`](/docs/media/video) by using [this](/docs/videos/as-threejs-texture) approach.

## See also[​](#see-also)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/three/src/ThreeCanvas.tsx)