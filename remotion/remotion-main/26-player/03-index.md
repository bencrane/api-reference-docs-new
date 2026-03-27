---
title: "<Thumbnail>"
url: "https://www.remotion.dev/docs/player/thumbnail"
path: "/docs/player/thumbnail"
---

"---\nimage: /generated/articles-docs-player-thumbnail.png\nid: thumbnail\ntitle: '<Thumbnail>'\ncrumb: '@remotion/player'\n---\n\n<AvailableFrom v=\"3.2.41\" />\n\nA component which can be rendered in a regular React App (for example: for example: [Next.JS](https://nextjs.org), [Vite.js](https://vitejs.dev), [Create React App](https://create-react-app.dev/)) to display a single frame of a video.\n\n```tsx twoslash title=\"MyApp.tsx\"\n// @allowUmdGlobalAccess\n// @filename: ./remotion/MyVideo.tsx\nexport const MyVideo: React.FC<{title: string}> = ({title}) => <>{title}</>;\n\n// @filename: index.tsx\n// ---cut---\nimport {Thumbnail} from '@remotion/player';\nimport {MyVideo} from './remotion/MyVideo';\n\nexport const App: React.FC = () => {\n  return (\n    <Thumbnail\n      component={MyVideo}\n      compositionWidth={600}\n      compositionHeight={600}\n      frameToDisplay={30}\n      durationInFrames={120}\n      fps={30}\n      inputProps={{\n        title: 'Foo',\n      }}\n    />\n  );\n};\n```\n\n## API\n\n### `component` or `lazyComponent`\n\nPass a React component in directly **or** pass a function that returns a dynamic import. Passing neither or both of the props is an error.\n\nIf you use `lazyComponent`, wrap it in a `useCallback()` to avoid constant rendering. [See here for an example.](/docs/player/examples#loading-a-component-lazily)\n\n:::note\nThumbnail does not use [`<Composition>`](/docs/composition)'s. Pass your component directly and do not wrap it in a `<Composition>` component.\n:::\n\n### `frameToDisplay`\n\nIndex of the frame rendered by the composition in the Thumbnail.\n\n### `compositionWidth`\n\nThe width you would like the video to have when rendered as an MP4. Use `style={{width: <width>}}` to define a width to be assumed in the browser.\n\n:::note\n**Example**:\nIf you want to render a Full HD video, set `compositionWidth` to `1920` and `compositionHeight` to `1080`. By default, the thumbnail will also assume these dimensions.\nTo make it smaller, pass a `style` prop to give the Thumbnail a different width: `{\"style={{width: 400}}\"}`. See [Player Scaling](/docs/player/scaling) to learn more.\n:::\n\n### `compositionHeight`\n\nThe height of the canvas in pixels.\nThe height you would like the video to have when rendered as an MP4. Use `style={{height: <height>}}` to define a height to be assumed in the browser.\n\n### `durationInFrames`\n\nThe duration of the video in frames. Must be an integer and greater than 0.\n\n:::note\nThis prop is required for the Thumbnail component because your component may render differently based on what `useVideoConfig()` returns.\n:::\n\n### `fps`\n\nThe frame rate of the video. Must be a number.\n\n:::note\nThis prop is required for the Thumbnail component because your component may render differently based on what `useVideoConfig()` returns.\n:::\n\n### `errorFallback?`\n\nA callback for rendering a custom error message. See [Handling errors](#handling-errors) section for an example.\n\n### `renderLoading?`\n\nA callback function that allows you to return a custom UI that gets displayed while the thumbnail is loading.\n\nThe first parameter of the callback function contains the `height` and `width` of the thumbnail as it gets rendered.\n\n```tsx twoslash\nimport {RenderLoading, Thumbnail} from '@remotion/player';\nimport {useCallback} from 'react';\nimport {AbsoluteFill} from 'remotion';\n\nconst Component: React.FC = () => null;\n\n// ---cut---\n\nconst MyApp: React.FC = () => {\n  // `RenderLoading` type can be imported from \"@remotion/player\"\n  const renderLoading: RenderLoading = useCallback(({height, width}) => {\n    return (\n      <AbsoluteFill style={{backgroundColor: 'gray'}}>\n        Loading thumbnail ({height}x{width})\n      </AbsoluteFill>\n    );\n  }, []);\n\n  return <Thumbnail fps={30} component={Component} durationInFrames={100} compositionWidth={1080} compositionHeight={1080} frameToDisplay={30} renderLoading={renderLoading} />;\n};\n```\n\n:::info\nA thumbnail needs to be loaded if it contains elements that use React Suspense, or if the `lazyComponent` prop is being used.\n:::\n\n### `inputProps?`\n\nPass props to the component that you have specified using the `component` prop. The Typescript definition takes the shape of the props that you have given to your `component`. Default `undefined`.\n\n### `style?`\n\nA regular `style` prop for a HTMLDivElement. You can pass a different height and width if you would like different dimensions for the thumbnail than the original composition dimensions.\n\n### `className?`<AvailableFrom v=\"3.1.3\" />\n\nA HTML class name to be applied to the container.\n\n### `overflowVisible`<AvailableFrom v=\"4.0.173\"/>\n\nMakes the Player render things outside of the canvas. Useful if you have interactive elements in the video such as draggable elements.\n\n### `logLevel?`<AvailableFrom v=\"4.0.250\" />\n\n<Options id=\"log\" />\n\n### `noSuspense`<AvailableFrom v=\"4.0.271\" />\n\nDisables React Suspense, which is [useful for writing tests](/docs/player/thumbnail).\n\n## ThumbnailRef\n\nYou may attach a ref to the thumbnail and get some layout info.\n\n```tsx twoslash {15}\n// @allowUmdGlobalAccess\n\n// @filename: MyComposition.tsx\nexport const MyComposition: React.FC = () => null;\n\n// @filename: index.tsx\n// ---cut---\nimport {Thumbnail, ThumbnailRef} from '@remotion/player';\nimport {useEffect, useRef} from 'react';\nimport {MyComposition} from './MyComposition';\n\nconst MyComp: React.FC = () => {\n  const thumbnailRef = useRef<ThumbnailRef>(null);\n\n  useEffect(() => {\n    if (thumbnailRef.current) {\n      console.log(thumbnailRef.current.getScale());\n    }\n  }, []);\n\n  return (\n    <Thumbnail\n      ref={thumbnailRef}\n      durationInFrames={30}\n      compositionWidth={1080}\n      compositionHeight={1080}\n      fps={30}\n      frameToDisplay={30}\n      component={MyComposition}\n      // Many other optional props are available.\n    />\n  );\n};\n```\n\nThe following methods are available on the thumbnail ref:\n\n### `getContainerNode()`\n\nGets the container `HTMLDivElement` of the thumbnail. Useful if you'd like to manually attach listeners to the thumbnail element.\n\n```tsx twoslash\nimport {ThumbnailRef} from '@remotion/player';\nimport {useEffect, useRef} from 'react';\n// ---cut---\nconst thumbnailRef = useRef<ThumbnailRef>(null);\n\nuseEffect(() => {\n  if (!thumbnailRef.current) {\n    return;\n  }\n  const container = thumbnailRef.current.getContainerNode();\n  if (!container) {\n    return;\n  }\n\n  const onClick = () => {\n    console.log('thumbnail got clicked');\n  };\n\n  container.addEventListener('click', onClick);\n  return () => {\n    container.removeEventListener('click', onClick);\n  };\n}, []);\n```\n\n### `getScale()`\n\nReturns a number which says how much the content is scaled down compared to the natural composition size. For example, if the composition is `1920x1080`, but the thumbnail is 960px in width, this method would return `0.5`.\n\n### `addEventListener()`\n\nStart listening to an event. See the [Events](#events) section to see the function signature and the available events.\n\n### `removeEventListener()`\n\nStop listening to an event. See the [Events](#events) section to see the function signature and the available events.\n\n## Events\n\nUsing a [thumbnail ref](#thumbnailref), you can bind event listeners to get notified of certain events of the thumbnail.\n\n```tsx twoslash\nimport {ThumbnailRef} from '@remotion/player';\nimport {useEffect, useRef} from 'react';\n// ---cut---\nconst thumbnailRef = useRef<ThumbnailRef>(null);\n\nuseEffect(() => {\n  if (!thumbnailRef.current) {\n    return;\n  }\n\n  thumbnailRef.current.addEventListener('error', (e) => {\n    console.log('error', e.detail.error);\n  });\n}, []);\n```\n\n### `error`\n\nFires when an error or uncaught exception has happened in the thumbnail.\n\nYou may get the error by reading the `e.detail.error` value:\n\n```tsx twoslash\nimport {ThumbnailRef} from '@remotion/player';\nimport {useRef} from 'react';\nconst ref = useRef<ThumbnailRef>(null);\n// ---cut---\nref.current?.addEventListener('error', (e) => {\n  console.log('error ', e.detail.error); // error [Error: undefined is not a function]\n});\n```\n\n### `waiting`<AvailableFrom v=\"4.0.125\" />\n\nFires when the Player has entered into the [native buffering state](/docs/player/buffer-state).\n\nRead here [how to best implement state management](/docs/player/buffer-state#possible-states).\n\n### `resume`<AvailableFrom v=\"4.0.125\" />\n\nFires when the Player has exited the [native buffering state](/docs/player/buffer-state).\n\nRead here [how to best implement state management](/docs/player/buffer-state#possible-states).\n\n## Handling errors\n\nSee: [`<Player>` -> Handling errors](/docs/player/player#handling-errors)\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/player/src/Thumbnail.tsx)\n- [`<Composition>`](/docs/composition)\n- [`<Player>`](/docs/player)\n\n<Credits\n  contributors={[\n    {\n      username: 'Slashgear',\n      contribution: 'Implementation',\n    },\n  ]}\n/>\n"
[v3.2.41](https://github.com/remotion-dev/remotion/releases/v3.2.41)

A component which can be rendered in a regular React App (for example: for example: [Next.JS](https://nextjs.org), [Vite.js](https://vitejs.dev), [Create React App](https://create-react-app.dev/)) to display a single frame of a video.

```

MyApp.tsximport {Thumbnail} from '@remotion/player';
import {MyVideo} from './remotion/MyVideo';

export const App: React.FC = () => {
  return (
    <Thumbnail
      component={MyVideo}
      compositionWidth={600}
      compositionHeight={600}
      frameToDisplay={30}
      durationInFrames={120}
      fps={30}
      inputProps={{
        title: 'Foo',
      }}
    />
  );
};Copy
```

## API[​](#api)

### `component` or `lazyComponent`[​](#component-or-lazycomponent)

Pass a React component in directly **or** pass a function that returns a dynamic import. Passing neither or both of the props is an error.

If you use `lazyComponent`, wrap it in a `useCallback()` to avoid constant rendering. [See here for an example.](/docs/player/examples#loading-a-component-lazily)
](/docs/player/examples#loading-a-component-lazily)](/docs/player/examples#loading-a-component-lazily)
](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)
- ](/docs/player/examples#loading-a-component-lazily)