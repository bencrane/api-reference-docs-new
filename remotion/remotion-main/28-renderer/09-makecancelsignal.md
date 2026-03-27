---
title: "makeCancelSignal()"
url: "https://www.remotion.dev/docs/renderer/make-cancel-signal"
path: "/docs/renderer/make-cancel-signal"
---

"---\nimage: /generated/articles-docs-renderer-make-cancel-signal.png\nid: make-cancel-signal\ntitle: makeCancelSignal()\ncrumb: '@remotion/renderer'\n---\n\n# makeCancelSignal()<AvailableFrom v=\"3.0.15\" />\n\n_Part of the `@remotion/renderer` package._\n\nThis function returns a signal and a cancel function that allows to you cancel a render triggered using [`renderMedia()`](/docs/renderer/render-media), [`renderStill()`](/docs/renderer/render-still), [`renderFrames()`](/docs/renderer/render-frames) or [`stitchFramesToVideo()`](/docs/renderer/stitch-frames-to-video)\n.\n\n## Example\n\n```tsx twoslash\nimport {VideoConfig} from 'remotion';\nconst composition: VideoConfig = {\n  durationInFrames: 1000000,\n  fps: 30,\n  height: 720,\n  id: 'react-svg',\n  width: 1280,\n  defaultProps: {},\n  props: {},\n  defaultCodec: null,\n  defaultOutName: null,\n  defaultVideoImageFormat: null,\n  defaultPixelFormat: null,\n  defaultProResProfile: null,\n};\n// ---cut---\nimport {makeCancelSignal, renderMedia} from '@remotion/renderer';\n\nconst {cancelSignal, cancel} = makeCancelSignal();\n\n// Note that no `await` is used yet\nconst render = renderMedia({\n  composition,\n  codec: 'h264',\n  serveUrl: '/path/to/bundle',\n  outputLocation: 'out/render.mp4',\n  cancelSignal,\n});\n\n// Cancel render after 10 seconds\nsetTimeout(() => {\n  cancel();\n}, 10000);\n\n// If the render completed within 10 seconds, renderMedia() will resolve\nawait render;\n\n// If the render did not complete, renderMedia() will reject\n// ==> \"[Error: renderMedia() got cancelled]\"\n```\n\n## API\n\nCalling `makeCancelSignal` returns an object with two properties:\n\n- `cancelSignal`: An object to be passed to one of the above mentioned render functions\n- `cancel`: A function you should call when you want to cancel the render.\n\n## Compatibility\n\n<CompatibilityTable chrome={false} firefox={false} safari={false} nodejs={true} bun={true} serverlessFunctions={false} clientSideRendering={false} serverSideRendering={true} player={false} studio={false} />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/make-cancel-signal.ts)\n- [`renderMedia()`](/docs/renderer/render-media)\n- [`renderStill()`](/docs/renderer/render-still)\n- [`renderFrames()`](/docs/renderer/render-frames)\n- [`stitchFramesToVideo()`](/docs/renderer/stitch-frames-to-video)\n"

*Part of the `@remotion/renderer` package.*

This function returns a signal and a cancel function that allows to you cancel a render triggered using [`renderMedia()`](/docs/renderer/render-media), [`renderStill()`](/docs/renderer/render-still), [`renderFrames()`](/docs/renderer/render-frames) or [`stitchFramesToVideo()`](/docs/renderer/stitch-frames-to-video)
.

## Example[​](#example)

```
import {makeCancelSignal, renderMedia} from '@remotion/renderer';

const {cancelSignal, cancel} = makeCancelSignal();

// Note that no `await` is used yet
const render = renderMedia({
  composition,
  codec: 'h264',
  serveUrl: '/path/to/bundle',
  outputLocation: 'out/render.mp4',
  cancelSignal,
});

// Cancel render after 10 seconds
setTimeout(() => {
  cancel();
}, 10000);

// If the render completed within 10 seconds, renderMedia() will resolve
await render;

// If the render did not complete, renderMedia() will reject
// ==> "[Error: renderMedia() got cancelled]"Copy
```

## API[​](#api)

Calling `makeCancelSignal` returns an object with two properties:

- `cancelSignal`: An object to be passed to one of the above mentioned render functions

- `cancel`: A function you should call when you want to cancel the render.

## Compatibility[​](#compatibility)

|  Browsers Servers Environments
|  
Chrome 
Firefox 
Safari 
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
 
 
 
 

## See also[​](#see-also)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/renderer/src/make-cancel-signal.ts)

- [`renderMedia()`](/docs/renderer/render-media)

- [`renderStill()`](/docs/renderer/render-still)

- [`renderFrames()`](/docs/renderer/render-frames)

- [`stitchFramesToVideo()`](/docs/renderer/stitch-frames-to-video)
](/docs/renderer/stitch-frames-to-video)](/docs/renderer/stitch-frames-to-video)
](/docs/renderer/stitch-frames-to-video)
- ](/docs/renderer/stitch-frames-to-video)
- ](/docs/renderer/stitch-frames-to-video)
- ](/docs/renderer/stitch-frames-to-video)