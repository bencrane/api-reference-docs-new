---
title: "preloadGif()"
url: "https://www.remotion.dev/docs/gif/preload-gif"
path: "/docs/gif/preload-gif"
---

"---\nimage: /generated/articles-docs-gif-preload-gif.png\ntitle: preloadGif()\ncrumb: \"@remotion/gif\"\n---\n\n_available from v3.3.38_\n\nCall `preloadGif(src)` with the URL of the GIF that you would like to load and the GIF will be prepared for display in the [`<Player>`](/docs/player).\n\nThe function returns an object with two entries: `waitUntilDone()` that returns a Promise which can be awaited and `free()` which will cancel preloading or free up the memory if the GIF is not being used anymore.\n\n```ts twoslash\nimport { preloadGif } from \"@remotion/gif\";\n\nconst { waitUntilDone, free } = preloadGif(\n  \"https://media.giphy.com/media/xT0GqH01ZyKwd3aT3G/giphy.gif\"\n);\n\nwaitUntilDone().then(() => {\n  console.log(\"The GIF is now ready to play!\");\n\n  // Later, free the memory of the GIF\n  free();\n});\n```\n\n## See also\n\n- [`<Gif>`](/docs/gif)\n- [Preloading](/docs/preload)\n"

*available from v3.3.38*

Call `preloadGif(src)` with the URL of the GIF that you would like to load and the GIF will be prepared for display in the [`<Player>`](/docs/player).

The function returns an object with two entries: `waitUntilDone()` that returns a Promise which can be awaited and `free()` which will cancel preloading or free up the memory if the GIF is not being used anymore.

```
import { preloadGif } from "@remotion/gif";

const { waitUntilDone, free } = preloadGif(
  "https://media.giphy.com/media/xT0GqH01ZyKwd3aT3G/giphy.gif"
);

waitUntilDone().then(() => {
  console.log("The GIF is now ready to play!");

  // Later, free the memory of the GIF
  free();
});Copy
```

## See also[​](#see-also)

- [`<Gif>`](/docs/gif)

- [Preloading](/docs/preload)
](/docs/preload)](/docs/preload)
](/docs/preload)