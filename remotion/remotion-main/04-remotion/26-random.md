---
title: "random()"
url: "https://www.remotion.dev/docs/random"
path: "/docs/random"
---

"---\nimage: /generated/articles-docs-random.png\nid: random\ntitle: random()\ncrumb: \"API\"\n---\n\nThe `random()` API will give deterministic pseudorandom values between `0` and `1`. Unlike the `Math.random()` function, Remotions function takes in a seed which can be a `number` or a `string`. If the seed is the same, the output is always the same.\n\n```ts twoslash\nimport { random } from \"remotion\";\n\nconst rand = random(1); // 0.07301638228818774\nconst rand2 = random(1); // still 0.07301638228818774\n\nconst randomCoordinates = new Array(10).fill(true).map((a, i) => {\n  return {\n    x: random(`random-x-${i}`),\n    y: random(`random-y-${i}`),\n  };\n}); // will always be [{x: 0.2887063352391124, y: 0.18660089606419206}, ...]\n\n// @ts-expect-error\nrandom(); // Error: random() argument must be a number or a string\n```\n\n## Use cases\n\nRandomness can be used to create interesting visualizations, such as particle effect for example. Since Remotion renders a video on multiple threads and opens the website multiple times, the value returned by a `Math.random()` call will not be the same across multiple threads, making it hard to create animations based on randomness. Using this API will ensure that the pseudorandom number will be the same always.\n\n## Accessing true randomness\n\nCalling `Math.random()` results in an ESLint warning in Remotion since often it leads to bugs in rendering. If you are sure you want a true random number, and want to bypass this message without adding an ignore comment, use `random(null)`\n\n```ts twoslash\nconst random = (seed: number | string | null) => Math.random();\n// ---cut---\n// Passing null will result in a different value every time.\nrandom(null) === random(null); // false\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs bun serverlessFunctions clientSideRendering serverSideRendering player studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/random.ts)\n- [Using randomness](/docs/using-randomness)\n"

The `random()` API will give deterministic pseudorandom values between `0` and `1`. Unlike the `Math.random()` function, Remotions function takes in a seed which can be a `number` or a `string`. If the seed is the same, the output is always the same.

```
import { random } from "remotion";

const rand = random(1); // 0.07301638228818774
const rand2 = random(1); // still 0.07301638228818774

const randomCoordinates = new Array(10).fill(true).map((a, i) => {
  return {
    x: random(`random-x-${i}`),
    y: random(`random-y-${i}`),
  };
}); // will always be [{x: 0.2887063352391124, y: 0.18660089606419206}, ...]

// @ts-expect-error
random(); // Error: random() argument must be a number or a stringCopy
```

## Use cases[​](#use-cases)

Randomness can be used to create interesting visualizations, such as particle effect for example. Since Remotion renders a video on multiple threads and opens the website multiple times, the value returned by a `Math.random()` call will not be the same across multiple threads, making it hard to create animations based on randomness. Using this API will ensure that the pseudorandom number will be the same always.

## Accessing true randomness[​](#accessing-true-randomness)

Calling `Math.random()` results in an ESLint warning in Remotion since often it leads to bugs in rendering. If you are sure you want a true random number, and want to bypass this message without adding an ignore comment, use `random(null)`

```
// Passing null will result in a different value every time.
random(null) === random(null); // falseCopy
```

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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/random.ts)

- [Using randomness](/docs/using-randomness)
](/docs/using-randomness)](/docs/using-randomness)
](/docs/using-randomness)
- ](/docs/using-randomness)
- ](/docs/using-randomness)
- ](/docs/using-randomness)