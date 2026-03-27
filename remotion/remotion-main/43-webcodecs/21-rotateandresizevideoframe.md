---
title: "rotateAndResizeVideoFrame()"
url: "https://www.remotion.dev/docs/webcodecs/rotate-and-resize-video-frame"
path: "/docs/webcodecs/rotate-and-resize-video-frame"
---

"---\nimage: /generated/articles-docs-webcodecs-rotate-and-resize-video-frame.png\nid: rotate-and-resize-video-frame\ntitle: rotateAndResizeVideoFrame()\nslug: /webcodecs/rotate-and-resize-video-frame\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\n# rotateAndResizeVideoFrame()<AvailableFrom v=\"4.0.316\"/>\n\n_Part of the [`@remotion/webcodecs`](/docs/webcodecs) package._\n\nimport {LicenseDisclaimer} from './LicenseDisclaimer';\n\n<details>\n  <summary>💼 Important License Disclaimer</summary>\n  <LicenseDisclaimer />\n</details>\n\nResizes and/or rotates a [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object.  \nReturns a new [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object with the applied transformations, or the original frame if no transformations are applied.\n\n```tsx twoslash title=\"Rotating a video frame by 90 degrees\"\nimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';\n\n// Assume you have a VideoFrame object\ndeclare const frame: VideoFrame;\n\nconst rotatedFrame = rotateAndResizeVideoFrame({\n  frame,\n  rotation: 90,\n  resizeOperation: null,\n});\n\nconsole.log('Original dimensions:', frame.displayWidth, 'x', frame.displayHeight);\nconsole.log('Rotated dimensions:', rotatedFrame.displayWidth, 'x', rotatedFrame.displayHeight);\n```\n\n```tsx twoslash title=\"Resizing a video frame by width\"\nimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';\n\n// Assume you have a VideoFrame object\ndeclare const frame: VideoFrame;\n\nconst resizedFrame = rotateAndResizeVideoFrame({\n  frame,\n  rotation: 0,\n  resizeOperation: {\n    mode: 'width',\n    width: 640,\n  },\n});\n\nconsole.log('Resized frame width:', resizedFrame.displayWidth);\n```\n\n```tsx twoslash title=\"Rotating and resizing together\"\nimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';\n\n// Assume you have a VideoFrame object\ndeclare const frame: VideoFrame;\n\nconst transformedFrame = rotateAndResizeVideoFrame({\n  frame,\n  rotation: 180,\n  resizeOperation: {\n    mode: 'height',\n    height: 480,\n  },\n  needsToBeMultipleOfTwo: true,\n});\n```\n\n## API\n\n### `frame`\n\nA [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object to be transformed.\n\n### `rotation`\n\nThe rotation angle in degrees. Only multiples of 90 degrees are supported (0, 90, 180, 270, etc.).\n\n### `resizeOperation`\n\nA resize operation to apply to the frame, or `null` if no resizing is needed.  \nSee: [Resize modes](/docs/webcodecs/resize-a-video#resize-modes) for available options.\n\n### `needsToBeMultipleOfTwo?`\n\nWhether the resulting dimensions should be multiples of 2. Default: `false`.  \nThis is often required if encoding to a codec like H.264.  \nIf `true`, the dimensions will be rounded down to the nearest even number.\n\n## Behavior\n\nThe function returns the **original frame** unchanged in these cases:\n\n- No rotation (0°) and no resize operation is specified\n- No rotation (0°) and resize operation results in the same dimensions\n\nOtherwise, it returns a **new `VideoFrame`** object:\n\n- When rotation is applied (90°, 180°, 270°, etc.)\n- When resizing changes the dimensions\n- When both rotation and resizing are applied\n\nAdditional behavior notes:\n\n- Rotation is applied first, then resizing\n- For 90° and 270° rotations, the width and height are swapped\n- The function creates a new `VideoFrame` using an `OffscreenCanvas` for the transformation\n\n## Memory Management\n\n**Important**: You are responsible for closing `VideoFrame` objects to prevent memory leaks. Since this function may return either the original frame or a new frame, you should check if a new frame was created before closing the original:\n\n```tsx twoslash title=\"Proper memory cleanup\"\nimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';\n\n// Assume you have a VideoFrame object\ndeclare const originalFrame: VideoFrame;\n\nconst transformedFrame = rotateAndResizeVideoFrame({\n  frame: originalFrame,\n  rotation: 90,\n  resizeOperation: null,\n});\n\n// Only close the original frame if a new one was created\nif (transformedFrame !== originalFrame) {\n  originalFrame.close();\n}\n\n// Remember to also close the transformed frame when you're done with it\n// transformedFrame.close();\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)\n"

*Part of the [`@remotion/webcodecs`](/docs/webcodecs) package.*

💼 Important License Disclaimer

This package is licensed under the [Remotion License](/docs/license).
We consider a team of 4 or more people a "company".

**For "companies"**: A Remotion Company license needs to be obtained to use this package.
 In a future version of [`@remotion/webcodecs`](), this package will also require the purchase of a newly created "WebCodecs Conversion Seat". [Get in touch](/contact) with us if you are planning to use this package.

**For individuals and teams up to 3:** You can use this package for free.

This is a short, non-binding explanation of our license. See the [License](/docs/license) itself for more details.

Resizes and/or rotates a [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object.

Returns a new [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object with the applied transformations, or the original frame if no transformations are applied.

```

Rotating a video frame by 90 degreesimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';

// Assume you have a VideoFrame object
declare const frame: VideoFrame;

const rotatedFrame = rotateAndResizeVideoFrame({
  frame,
  rotation: 90,
  resizeOperation: null,
});

console.log('Original dimensions:', frame.displayWidth, 'x', frame.displayHeight);
console.log('Rotated dimensions:', rotatedFrame.displayWidth, 'x', rotatedFrame.displayHeight);Copy
```

```

Resizing a video frame by widthimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';

// Assume you have a VideoFrame object
declare const frame: VideoFrame;

const resizedFrame = rotateAndResizeVideoFrame({
  frame,
  rotation: 0,
  resizeOperation: {
    mode: 'width',
    width: 640,
  },
});

console.log('Resized frame width:', resizedFrame.displayWidth);Copy
```

```

Rotating and resizing togetherimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';

// Assume you have a VideoFrame object
declare const frame: VideoFrame;

const transformedFrame = rotateAndResizeVideoFrame({
  frame,
  rotation: 180,
  resizeOperation: {
    mode: 'height',
    height: 480,
  },
  needsToBeMultipleOfTwo: true,
});Copy
```

## API[​](#api)

### `frame`[​](#frame)

A [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object to be transformed.

### `rotation`[​](#rotation)

The rotation angle in degrees. Only multiples of 90 degrees are supported (0, 90, 180, 270, etc.).

### `resizeOperation`[​](#resizeoperation)

A resize operation to apply to the frame, or `null` if no resizing is needed.

See: [Resize modes](/docs/webcodecs/resize-a-video#resize-modes) for available options.

### `needsToBeMultipleOfTwo?`[​](#needstobemultipleoftwo)

Whether the resulting dimensions should be multiples of 2. Default: `false`.

This is often required if encoding to a codec like H.264.

If `true`, the dimensions will be rounded down to the nearest even number.

## Behavior[​](#behavior)

The function returns the **original frame** unchanged in these cases:

- No rotation (0°) and no resize operation is specified

- No rotation (0°) and resize operation results in the same dimensions

Otherwise, it returns a **new `VideoFrame`** object:

- When rotation is applied (90°, 180°, 270°, etc.)

- When resizing changes the dimensions

- When both rotation and resizing are applied

Additional behavior notes:

- Rotation is applied first, then resizing

- For 90° and 270° rotations, the width and height are swapped

- The function creates a new `VideoFrame` using an `OffscreenCanvas` for the transformation

## Memory Management[​](#memory-management)

**Important**: You are responsible for closing `VideoFrame` objects to prevent memory leaks. Since this function may return either the original frame or a new frame, you should check if a new frame was created before closing the original:

```

Proper memory cleanupimport {rotateAndResizeVideoFrame} from '@remotion/webcodecs';

// Assume you have a VideoFrame object
declare const originalFrame: VideoFrame;

const transformedFrame = rotateAndResizeVideoFrame({
  frame: originalFrame,
  rotation: 90,
  resizeOperation: null,
});

// Only close the original frame if a new one was created
if (transformedFrame !== originalFrame) {
  originalFrame.close();
}

// Remember to also close the transformed frame when you're done with it
// transformedFrame.close();Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/rotate-and-resize-video-frame.ts)