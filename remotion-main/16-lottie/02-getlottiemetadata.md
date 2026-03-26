---
title: "getLottieMetadata()"
url: "https://www.remotion.dev/docs/lottie/getlottiemetadata"
path: "/docs/lottie/getlottiemetadata"
---

"---\nimage: /generated/articles-docs-lottie-getlottiemetadata.png\nid: getlottiemetadata\ntitle: getLottieMetadata()\ncrumb: \"@remotion/lottie\"\n---\n\n_Part of the [`@remotion/lottie`](/docs/lottie) package._\n\nUsing this function, you can get the basic metadata such as dimensions, duration and framerate of a Lottie animation.\n\n```tsx twoslash title=\"Animation.tsx\"\n// @allowUmdGlobalAccess\n// @filename: animation.ts\nexport const animationData = {\n  v: \"5.9.6\",\n  fr: 29.9700012207031,\n  ip: 0,\n  op: 90.0000036657751,\n  w: 1920,\n  h: 1080,\n  nm: \"Comp 1\",\n  ddd: 0,\n  assets: [],\n  layers: [\n    {\n      ddd: 0,\n      ind: 1,\n      ty: 4,\n      nm: \"Shape Layer 1\",\n      sr: 1,\n      ks: {\n        o: { a: 0, k: 100, ix: 11 },\n        r: {\n          a: 1,\n          k: [\n            {\n              i: { x: [0.833], y: [0.833] },\n              o: { x: [0.167], y: [0.167] },\n              t: 0,\n              s: [360],\n            },\n            { t: 58.0000023623884, s: [0] },\n          ],\n          ix: 10,\n        },\n        p: {\n          a: 1,\n          k: [\n            {\n              i: { x: 0.833, y: 0.833 },\n              o: { x: 0.167, y: 0.167 },\n              t: 0,\n              s: [979.401, 1368, 0],\n              to: [0, -138, 0],\n              ti: [0, 138, 0],\n            },\n            { t: 58.0000023623884, s: [979.401, 540, 0] },\n          ],\n          ix: 2,\n          l: 2,\n        },\n        a: { a: 0, k: [517.365, 112.096, 0], ix: 1, l: 2 },\n        s: { a: 0, k: [100, 100, 100], ix: 6, l: 2 },\n      },\n      ao: 0,\n      shapes: [\n        {\n          ty: \"gr\",\n          it: [\n            {\n              ty: \"rc\",\n              d: 1,\n              s: { a: 0, k: [425.883, 425.883], ix: 2 },\n              p: { a: 0, k: [0, 0], ix: 3 },\n              r: { a: 0, k: 98, ix: 4 },\n              nm: \"Rectangle Path 1\",\n              mn: \"ADBE Vector Shape - Rect\",\n              hd: false,\n            },\n            {\n              ty: \"st\",\n              c: { a: 0, k: [1, 1, 1, 1], ix: 3 },\n              o: { a: 0, k: 100, ix: 4 },\n              w: { a: 0, k: 2, ix: 5 },\n              lc: 1,\n              lj: 1,\n              ml: 4,\n              bm: 0,\n              nm: \"Stroke 1\",\n              mn: \"ADBE Vector Graphic - Stroke\",\n              hd: false,\n            },\n            {\n              ty: \"fl\",\n              c: { a: 0, k: [0, 0.468933612108, 1, 1], ix: 4 },\n              o: { a: 0, k: 100, ix: 5 },\n              r: 1,\n              bm: 0,\n              nm: \"Fill 1\",\n              mn: \"ADBE Vector Graphic - Fill\",\n              hd: false,\n            },\n            {\n              ty: \"tr\",\n              p: { a: 0, k: [494.618, 123.481], ix: 2 },\n              a: { a: 0, k: [0, 0], ix: 1 },\n              s: { a: 0, k: [100, 100], ix: 3 },\n              r: { a: 0, k: 0, ix: 6 },\n              o: { a: 0, k: 100, ix: 7 },\n              sk: { a: 0, k: 0, ix: 4 },\n              sa: { a: 0, k: 0, ix: 5 },\n              nm: \"Transform\",\n            },\n          ],\n          nm: \"Rectangle 2\",\n          np: 3,\n          cix: 2,\n          bm: 0,\n          ix: 1,\n          mn: \"ADBE Vector Group\",\n          hd: false,\n        },\n      ],\n      ip: 0,\n      op: 90.0000036657751,\n      st: 0,\n      ct: 1,\n      bm: 0,\n    },\n    {\n      ddd: 0,\n      ind: 2,\n      ty: 1,\n      nm: \"White Solid 1\",\n      sr: 1,\n      ks: {\n        o: { a: 0, k: 100, ix: 11 },\n        r: { a: 0, k: 0, ix: 10 },\n        p: { a: 0, k: [960, 540, 0], ix: 2, l: 2 },\n        a: { a: 0, k: [960, 540, 0], ix: 1, l: 2 },\n        s: { a: 0, k: [100, 100, 100], ix: 6, l: 2 },\n      },\n      ao: 0,\n      sw: 1920,\n      sh: 1080,\n      sc: \"#ffffff\",\n      ip: 0,\n      op: 90.0000036657751,\n      st: 0,\n      bm: 0,\n    },\n  ],\n  markers: [],\n};\n\n// @filename: Animation.tsx\nimport { animationData } from \"./animation\";\n\n// ---cut---\nimport { getLottieMetadata } from \"@remotion/lottie\";\n\n// animationData is a JSON object, can be imported from a .json file, remote file or using staticFile()\nconst metadata = getLottieMetadata(animationData);\n\n/*\n{\n  durationInFrames: 90,\n  durationInSeconds: 3.0030030030030037,\n  fps: 29.9700012207031,\n  height: 1080,\n  width: 1920,\n}\n*/\n```\n\n## API\n\nThe function takes one argument, a JavaScript object that adheres to the Lottie schema.\n\n### Return value\n\nIf the metadata cannot be parsed, this function returns `null`.\n\nIf the metadata can be parsed, it returns an object with the following properties:\n\n#### `height`\n\nThe natural height of the animation in pixels.\n\n#### `width`\n\nThe natural width of the animation in pixels.\n\n#### `durationInSeconds`\n\nThe duration of the animation in seconds, if the `fps` from this object is used.\n\n#### `durationInFrames`\n\nThe duration of the animation in frames, if the `fps` from this object is used.\n\n:::note\nThis value is rounded down to the closest integer, since Remotion does not support non-integer values for `durationInFrames`.\n:::\n\n#### `fps`\n\nThe natural framerate of the Lottie animation.\n\n## See also\n\n- [Change Remotion composition metadata based on Lottie metadata](/docs/dynamic-metadata)\n"

*Part of the [`@remotion/lottie`](/docs/lottie) package.*

Using this function, you can get the basic metadata such as dimensions, duration and framerate of a Lottie animation.

```

Animation.tsximport { getLottieMetadata } from "@remotion/lottie";

// animationData is a JSON object, can be imported from a .json file, remote file or using staticFile()
const metadata = getLottieMetadata(animationData);

/*
{
  durationInFrames: 90,
  durationInSeconds: 3.0030030030030037,
  fps: 29.9700012207031,
  height: 1080,
  width: 1920,
}
*/Copy
```

## API[​](#api)

The function takes one argument, a JavaScript object that adheres to the Lottie schema.

### Return value[​](#return-value)

If the metadata cannot be parsed, this function returns `null`.

If the metadata can be parsed, it returns an object with the following properties:

#### `height`[​](#height)

The natural height of the animation in pixels.

#### `width`[​](#width)

The natural width of the animation in pixels.

#### `durationInSeconds`[​](#durationinseconds)

The duration of the animation in seconds, if the `fps` from this object is used.

#### `durationInFrames`[​](#durationinframes)

The duration of the animation in frames, if the `fps` from this object is used.
](#durationinframes)](#durationinframes)
](#durationinframes)
- ](#durationinframes)
- ](#durationinframes)