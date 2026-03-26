---
title: "<RemotionRiveCanvas>"
url: "https://www.remotion.dev/docs/rive/remotionrivecanvas"
path: "/docs/rive/remotionrivecanvas"
---

"---\nimage: /generated/articles-docs-rive-remotionrivecanvas.png\ncrumb: '@remotion/rive'\nsidebar_label: '<RemotionRiveCanvas>'\ntitle: '<RemotionRiveCanvas>'\n---\n\n# &lt;RemotionRiveCanvas&gt;<AvailableFrom v=\"3.3.75\"/>\n\nThis component can render a [Rive](https://rive.app/) animation so it synchronizes with Remotion's time.\n\n## Example\n\n```tsx twoslash\nimport React from 'react';\nimport {RemotionRiveCanvas} from '@remotion/rive';\n\nfunction App() {\n  return <RemotionRiveCanvas src=\"https://example.com/myAnimation.riv\" />;\n}\n```\n\n## Props\n\n### `src`\n\na valid URL of the rive file to load. Can be a local file loaded using [`staticFile()`](/docs/staticfile) or a remote URL like `\"https://cdn.rive.app/animations/vehicles.riv\"`.\n\n### `fit?`\n\nOne of: `\"contain\" | \"cover\" | \"fill\" | \"fit-height\" | \"none\" | \"scale-down\" | \"fit-width\"`. Default is `\"contain\"`.\n\n### `alignment?`\n\nOne of: `\"center\" | \"bottom-center\" | \"bottom-left\" | \"bottom-right\" | \"center-left\" | \"center-right\" | \"top-center\" | \"top-left\" | \"top-right\"`. Default is `\"center\"`.\n\n### `artboard?`\n\nEither a `string` specifying the artboard name, a `number` specifying the artboard index, otherwise the default artboard is being used.\n\n### `animation?`\n\nEither a `string` specifying the animation name, a `number` specifying the animation index, otherwise the default animation is being used.\n\n### `onLoad?`<AvailableFrom v=\"4.0.58\" />\n\nA callback function that will be executed when the Rive Runtime is loaded. The argument callback is an object of type Rive `File`\n\n### `enableRiveAssetCdn?`<AvailableFrom v=\"4.0.181\" />\n\nWhether to enable the Rive Asset CDN. Default is `true`.\n\n### `assetLoader?`<AvailableFrom v=\"4.0.181\" />\n\nA custom asset loader. See [here](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets) for more information.\n\n:::note\nMemoize the assetLoader function using `useCallback`.\n:::\n\n```tsx\nimport {useCallback} from 'react';\nimport {RemotionRiveCanvas} from '@remotion/rive';\nimport {FileAsset, ImageAsset} from '@rive-app/canvas-advanced';\nimport {decodeImage} from '@rive-app/react-canvas';\n\nexport const MyComp: React.FC = () => {\n  const assetLoader = useCallback((asset: FileAsset, bytes: Uint8Array) => {\n    console.log('Asset properties to query', {\n      name: asset.name,\n      fileExtension: asset.fileExtension,\n      cdnUuid: asset.cdnUuid,\n      isFont: asset.isFont,\n      isImage: asset.isImage,\n      isAudio: asset.isAudio,\n      bytes,\n    });\n\n    // If the asset has a `cdnUuid`, return false to let the runtime handle\n    // loading it in from a CDN. Or if there are bytes found for the asset\n    // (aka, it was embedded), return false as there's no work needed here\n    if (asset.cdnUuid.length > 0 || bytes.length > 0) {\n      return false;\n    }\n\n    if (asset.isImage) {\n      fetch('https://picsum.photos/300/500').then(async (res) => {\n        console.log('doing this');\n        const image = await decodeImage(\n          new Uint8Array(await res.arrayBuffer()),\n        );\n\n        (asset as ImageAsset).setRenderImage(image);\n\n        // You could maintain a reference and update the image dynamically at any time.\n        // But be sure to call unref to release any references when no longer needed.\n        // This allows the engine to clean it up when it is not used by any more animations.\n        image.unref();\n      });\n\n      return true;\n    }\n\n    return false;\n  }, []);\n\n  return (\n    <RemotionRiveCanvas\n      src=\"https://example.com/myAnimation.riv\"\n      assetLoader={assetLoader}\n    />\n  );\n};\n```\n\n## Ref<AvailableFrom v=\"4.0.180\" />\n\nYou can attach a ref to the component to access the Rive Canvas instance.\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport React from 'react';\nimport {RemotionRiveCanvas, RiveCanvasRef} from '@remotion/rive';\nimport {useEffect} from 'react';\n\nconst MyComp: React.FC = () => {\n  const canvasRef = React.useRef<RiveCanvasRef>(null);\n\n  useEffect(() => {\n    if (!canvasRef.current) {\n      return;\n    }\n\n    canvasRef.current.getAnimationInstance(); // import(\"@rive-app/canvas-advanced\").LinearAnimationInstance\n    canvasRef.current.getArtboard(); // import(\"@rive-app/canvas-advanced\").Artboard\n    canvasRef.current.getRenderer(); // import(\"@rive-app/canvas-advanced\").CanvasRenderer\n    canvasRef.current.getCanvas(); // import(\"@rive-app/canvas-advanced\").RiveCanvas\n  }, [canvasRef]);\n\n  return (\n    <RemotionRiveCanvas\n      src=\"https://example.com/myAnimation.riv\"\n      ref={canvasRef}\n    />\n  );\n};\n```\n\nThe ref exposes the following methods:\n\n### `getAnimationInstance()`\n\nReturns a [`LinearAnimationInstance`](https://github.com/rive-app/rive-wasm/blob/caacb99a5b503d3fa56e8e921af2a7015478851c/js/src/rive_advanced.mjs.d.ts#L513) from the Rive Runtime.\n\n### `getArtboard()`\n\nReturns a [`Artboard`](https://github.com/rive-app/rive-wasm/blob/caacb99a5b503d3fa56e8e921af2a7015478851c/js/src/rive_advanced.mjs.d.ts) from the Rive Runtime.\n\n### `getRenderer()`\n\nReturns a [`CanvasRenderer`](https://github.com/rive-app/rive-wasm/blob/caacb99a5b503d3fa56e8e921af2a7015478851c/js/src/rive_advanced.mjs.d.ts#L221) from the Rive Runtime.\n\n### `getCanvas()`\n\nReturns a [`RiveCanvas`](https://github.com/rive-app/rive-wasm/blob/caacb99a5b503d3fa56e8e921af2a7015478851c/js/src/rive_advanced.mjs.d.ts#L14) from the Rive Runtime.\n\n## Set Text Run at Runtime Example\n\nThis example assumes that your Rive animation has a text run named \"city\". See [here](https://help.rive.app/runtimes/text#low-level-api-usage) for\nmore information about Text Runs on Rive.\n\n```tsx twoslash\nimport {RemotionRiveCanvas} from '@remotion/rive';\nimport {File} from '@rive-app/canvas-advanced';\nimport {useCallback} from 'react';\n\n// Make sure to wrap your onLoad handler on `useCallback` to avoid re-rendering this component every single time\nconst onLoadHandler = useCallback((file: File) => {\n  const artboard = file.defaultArtboard();\n  const textRun = artboard.textRun('city');\n  textRun.text = 'Tokyo';\n}, []);\n\nfunction App() {\n  return (\n    <RemotionRiveCanvas\n      src=\"https://example.com/myAnimation.riv\"\n      onLoad={onLoadHandler}\n    />\n  );\n}\n```\n\n## See also\n\n- [`@remotion/lottie`](/docs/lottie)\n"

This component can render a [Rive](https://rive.app/) animation so it synchronizes with Remotion's time.

## Example[​](#example)

```
import React from 'react';
import {RemotionRiveCanvas} from '@remotion/rive';

function App() {
  return <RemotionRiveCanvas src="https://example.com/myAnimation.riv" />;
}Copy
```

## Props[​](#props)

### `src`[​](#src)

a valid URL of the rive file to load. Can be a local file loaded using [`staticFile()`](/docs/staticfile) or a remote URL like `"https://cdn.rive.app/animations/vehicles.riv"`.

### `fit?`[​](#fit)

One of: `"contain" | "cover" | "fill" | "fit-height" | "none" | "scale-down" | "fit-width"`. Default is `"contain"`.

### `alignment?`[​](#alignment)

One of: `"center" | "bottom-center" | "bottom-left" | "bottom-right" | "center-left" | "center-right" | "top-center" | "top-left" | "top-right"`. Default is `"center"`.

### `artboard?`[​](#artboard)

Either a `string` specifying the artboard name, a `number` specifying the artboard index, otherwise the default artboard is being used.

### `animation?`[​](#animation)

Either a `string` specifying the animation name, a `number` specifying the animation index, otherwise the default animation is being used.

### `onLoad?`[v4.0.58](https://github.com/remotion-dev/remotion/releases/v4.0.58)[​](#onload)

A callback function that will be executed when the Rive Runtime is loaded. The argument callback is an object of type Rive `File`

### `enableRiveAssetCdn?`[v4.0.181](https://github.com/remotion-dev/remotion/releases/v4.0.181)[​](#enableriveassetcdn)

Whether to enable the Rive Asset CDN. Default is `true`.

### `assetLoader?`[v4.0.181](https://github.com/remotion-dev/remotion/releases/v4.0.181)[​](#assetloader)

A custom asset loader. See [here](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets) for more information.
](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)
- ](https://rive.app/community/doc/loading-assets/doct4wVHGPgC#handling-assets)