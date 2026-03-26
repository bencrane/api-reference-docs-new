---
title: "getImageDimensions()"
url: "https://www.remotion.dev/docs/get-image-dimensions"
path: "/docs/get-image-dimensions"
---

"---\nimage: /generated/articles-docs-get-image-dimensions.png\ntitle: getImageDimensions()\nid: get-image-dimensions\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils` package of helper functions. Available from v4.0.143._\n\nTakes an image `src`, retrieves the dimensions of an image.\n\n## Arguments\n\n### `src`\n\nA string that specifies the URL or path of the image.\n\n## Return value\n\n_`Promise<ImageDimensions>`_\n\nAn object with information about the image dimensions:\n\n### `width`\n\n_number_\n\nThe image width, in pixels (px).\n\n### `height`\n\n_number_\n\nThe image height, in pixels (px).\n\n## Example\n\n```ts twoslash\nimport {getImageDimensions} from '@remotion/media-utils';\n\nconst {width, height} = await getImageDimensions('https://example.com/remote-image.png');\nconsole.log(width, height);\n```\n\n## Caching behavior\n\nThis function is memoizing the results it returns.\n\nIf you pass in the same argument to `src` multiple times, it will return a cached version from the second time on, regardless of if the file has changed.  \nTo clear the cache, you have to reload the page.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/get-image-dimensions.ts)\n- [Preload image](/docs/preload/preload-image)\n- [`<Img />`](/docs/img)\n- [`getAudioData()`](/docs/get-audio-data)\n"

*Part of the `@remotion/media-utils` package of helper functions. Available from v4.0.143.*

Takes an image `src`, retrieves the dimensions of an image.

## Arguments[​](#arguments)

### `src`[​](#src)

A string that specifies the URL or path of the image.

## Return value[​](#return-value)

*`Promise<ImageDimensions>`*

An object with information about the image dimensions:

### `width`[​](#width)

*number*

The image width, in pixels (px).

### `height`[​](#height)

*number*

The image height, in pixels (px).

## Example[​](#example)

```
import {getImageDimensions} from '@remotion/media-utils';

const {width, height} = await getImageDimensions('https://example.com/remote-image.png');
console.log(width, height);Copy
```

## Caching behavior[​](#caching-behavior)

This function is memoizing the results it returns.

If you pass in the same argument to `src` multiple times, it will return a cached version from the second time on, regardless of if the file has changed.

To clear the cache, you have to reload the page.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/get-image-dimensions.ts)

- [Preload image](/docs/preload/preload-image)

- [`<Img />`](/docs/img)

- [`getAudioData()`](/docs/get-audio-data)
](/docs/get-audio-data)](/docs/get-audio-data)
](/docs/get-audio-data)
- ](/docs/get-audio-data)
- ](/docs/get-audio-data)
- ](/docs/get-audio-data)
- ](/docs/get-audio-data)
- ](/docs/get-audio-data)
- ](/docs/get-audio-data)
- ](/docs/get-audio-data)