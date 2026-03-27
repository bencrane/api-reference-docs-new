---
title: "Easing"
url: "https://www.remotion.dev/docs/easing"
path: "/docs/easing"
---

"---\nimage: /generated/articles-docs-easing.png\nid: easing\ntitle: Easing\ncrumb: \"API\"\n---\n\nThe `Easing` module implements common easing functions. You can use it with the [`interpolate()`](/docs/interpolate) API.\n\nYou can find a visualization of some common easing functions at http://easings.net/\n\n### Predefined animations\n\nThe `Easing` module provides several predefined animations through the following methods:\n\n- [`back`](/docs/easing#back) provides a basic animation where the object goes slightly back before moving forward\n- [`bounce`](/docs/easing#bounce) provides a bouncing animation\n- [`ease`](/docs/easing#ease) provides a basic inertial animation\n- [`elastic`](/docs/easing#elastic) provides a basic spring interaction\n\n### Standard functions\n\nThree standard easing functions are provided:\n\n- [`linear`](/docs/easing#linear)\n- [`quad`](/docs/easing#quad)\n- [`cubic`](/docs/easing#cubic)\n\nThe [`poly`](/docs/easing#poly) function can be used to implement quartic, quintic, and other higher power functions.\n\n### Additional functions\n\nAdditional mathematical functions are provided by the following methods:\n\n- [`bezier`](/docs/easing#bezier) provides a cubic bezier curve\n- [`circle`](/docs/easing#circle) provides a circular function\n- [`sin`](/docs/easing#sin) provides a sinusoidal function\n- [`exp`](/docs/easing#exp) provides an exponential function\n\nThe following helpers are used to modify other easing functions.\n\n- [`in`](/docs/easing#ineasing) runs an easing function forwards\n- [`inOut`](/docs/easing#inout) makes any easing function symmetrical\n- [`out`](/docs/easing#out) runs an easing function backwards\n\n## Example\n\n```tsx twoslash\nimport { AbsoluteFill, useCurrentFrame } from \"remotion\";\n// ---cut---\nimport { Easing, interpolate } from \"remotion\";\n\nconst MyVideo: React.FC = () => {\n  const frame = useCurrentFrame();\n  const interpolated = interpolate(frame, [0, 100], [0, 1], {\n    easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),\n    extrapolateLeft: \"clamp\",\n    extrapolateRight: \"clamp\",\n  });\n  return (\n    <AbsoluteFill\n      style={{\n        transform: `scale(${interpolated})`,\n        backgroundColor: \"red\",\n      }}\n    />\n  );\n};\n```\n\n---\n\n# Reference\n\n## Methods\n\n### `step0`\n\n```jsx\nstatic step0(n): number\n```\n\nA stepping function, returns 1 for any positive value of `n`.\n\n---\n\n### `step1`\n\n```jsx\nstatic step1(n): number\n```\n\nA stepping function, returns 1 if `n` is greater than or equal to 1.\n\n---\n\n### `linear`\n\n```jsx\nstatic linear(t): number\n```\n\nA linear function, `f(t) = t`. Position correlates to elapsed time one to one.\n\nhttp://cubic-bezier.com/#0,0,1,1\n\n---\n\n### `ease`\n\n```jsx\nstatic ease(t): number\n```\n\nA basic inertial interaction, similar to an object slowly accelerating to speed.\n\nhttp://cubic-bezier.com/#.42,0,1,1\n\n---\n\n### `quad`\n\n```jsx\nstatic quad(t): number\n```\n\nA quadratic function, `f(t) = t * t`. Position equals the square of elapsed time.\n\nhttp://easings.net/#easeInQuad\n\n---\n\n### `cubic`\n\n```jsx\nstatic cubic(t): number\n```\n\nA cubic function, `f(t) = t * t * t`. Position equals the cube of elapsed time.\n\nhttp://easings.net/#easeInCubic\n\n---\n\n### `poly()`\n\n```jsx\nstatic poly(n): (t) => number\n```\n\nA power function. Position is equal to the Nth power of elapsed time.\n\nn = 4: http://easings.net/#easeInQuart n = 5: http://easings.net/#easeInQuint\n\n---\n\n### `sin`\n\n```jsx\nstatic sin(t): number\n```\n\nA sinusoidal function.\n\nhttp://easings.net/#easeInSine\n\n---\n\n### `circle`\n\n```jsx\nstatic circle(t): number\n```\n\nA circular function.\n\nhttp://easings.net/#easeInCirc\n\n---\n\n### `exp`\n\n```jsx\nstatic exp(t): number\n```\n\nAn exponential function.\n\nhttp://easings.net/#easeInExpo\n\n---\n\n### `elastic()`\n\n```jsx\nstatic elastic(bounciness): (t) =>  number\n```\n\nA basic elastic interaction, similar to a spring oscillating back and forth.\n\nDefault bounciness is 1, which overshoots a little bit once. 0 bounciness doesn't overshoot at all, and bounciness of N > 1 will overshoot about N times.\n\nhttp://easings.net/#easeInElastic\n\n---\n\n### `back()`\n\n```jsx\nstatic back(s): (t) => number\n```\n\nUse with `Animated.parallel()` to create a basic effect where the object animates back slightly as the animation starts.\n\n---\n\n### `bounce`\n\n```jsx\nstatic bounce(t): number\n```\n\nProvides a basic bouncing effect.\n\nhttp://easings.net/#easeInBounce\n\nSee an example of how you might use it below\n\n```jsx\ninterpolate(0.5, [0, 1], [0, 1], {\n  easing: Easing.bounce,\n});\n```\n\n---\n\n### `bezier()`\n\n```jsx\nstatic bezier(x1, y1, x2, y2) => (t): number\n```\n\nProvides a cubic bezier curve, equivalent to CSS Transitions' `transition-timing-function`.\n\nA useful tool to visualize cubic bezier curves can be found at http://cubic-bezier.com/\n\n```jsx\ninterpolate(0.5, [0, 1], [0, 1], {\n  easing: Easing.bezier(0.5, 0.01, 0.5, 1),\n});\n```\n\n---\n\n### `in(easing)`\n\n<!-- prettier-ignore-start -->\n```jsx\nstatic in(easing: (t: number) => number): (t: number) => number;\n```\n<!-- prettier-ignore-end -->\n\nRuns an easing function forwards.\n\n```jsx\n{\n  easing: Easing.in(Easing.ease);\n}\n```\n\n---\n\n### `out()`\n\n```jsx\nstatic out(easing: (t: number) => number): (t: number) => number;\n```\n\nRuns an easing function backwards.\n\n```jsx\n{\n  easing: Easing.out(Easing.ease);\n}\n```\n\n---\n\n### `inOut()`\n\n```jsx\nstatic inOut(easing: (t: number) => number): (t: number) => number;\n```\n\n```jsx\n{\n  easing: Easing.inOut(Easing.ease);\n}\n```\n\nMakes any easing function symmetrical. The easing function will run forwards for half of the duration, then backwards for the rest of the duration.\n\n## Credits\n\nThe Easing API is the exact same as the one from [React Native](https://reactnative.dev/docs/easing) and the documentation has been copied over. Credit goes to them for this excellent API.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs bun serverlessFunctions clientSideRendering serverSideRendering player studio />\n\n## See also\n\n- [Source code for this helper](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/easing.ts)\n\n<Credits contributors={[\n{\nusername: \"kaf-lamed-beyt\",\ncontribution: \"Improved function signatures\"\n},\n]} />\n"

The `Easing` module implements common easing functions. You can use it with the [`interpolate()`](/docs/interpolate) API.

You can find a visualization of some common easing functions at [http://easings.net/](http://easings.net/)

### Predefined animations[​](#predefined-animations)

The `Easing` module provides several predefined animations through the following methods:

- [`back`](/docs/easing#back) provides a basic animation where the object goes slightly back before moving forward

- [`bounce`](/docs/easing#bounce) provides a bouncing animation

- [`ease`](/docs/easing#ease) provides a basic inertial animation

- [`elastic`](/docs/easing#elastic) provides a basic spring interaction

### Standard functions[​](#standard-functions)

Three standard easing functions are provided:

- [`linear`](/docs/easing#linear)

- [`quad`](/docs/easing#quad)

- [`cubic`](/docs/easing#cubic)

The [`poly`](/docs/easing#poly) function can be used to implement quartic, quintic, and other higher power functions.

### Additional functions[​](#additional-functions)

Additional mathematical functions are provided by the following methods:

- [`bezier`](/docs/easing#bezier) provides a cubic bezier curve

- [`circle`](/docs/easing#circle) provides a circular function

- [`sin`](/docs/easing#sin) provides a sinusoidal function

- [`exp`](/docs/easing#exp) provides an exponential function

The following helpers are used to modify other easing functions.

- [`in`](/docs/easing#ineasing) runs an easing function forwards

- [`inOut`](/docs/easing#inout) makes any easing function symmetrical

- [`out`](/docs/easing#out) runs an easing function backwards

## Example[​](#example)

```
import { Easing, interpolate } from "remotion";

const MyVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const interpolated = interpolate(frame, [0, 100], [0, 1], {
    easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill
      style={{
        transform: `scale(${interpolated})`,
        backgroundColor: "red",
      }}
    />
  );
};Copy
```

---

# Reference

## Methods[​](#methods)

### `step0`[​](#step0)

```
static step0(n): numberCopy
```

A stepping function, returns 1 for any positive value of `n`.

---

### `step1`[​](#step1)

```
static step1(n): numberCopy
```

A stepping function, returns 1 if `n` is greater than or equal to 1.

---

### `linear`[​](#linear)

```
static linear(t): numberCopy
```

A linear function, `f(t) = t`. Position correlates to elapsed time one to one.

[http://cubic-bezier.com/#0,0,1,1](http://cubic-bezier.com/#0,0,1,1)

---

### `ease`[​](#ease)

```
static ease(t): numberCopy
```

A basic inertial interaction, similar to an object slowly accelerating to speed.

[http://cubic-bezier.com/#.42,0,1,1](http://cubic-bezier.com/#.42,0,1,1)

---

### `quad`[​](#quad)

```
static quad(t): numberCopy
```

A quadratic function, `f(t) = t * t`. Position equals the square of elapsed time.

[http://easings.net/#easeInQuad](http://easings.net/#easeInQuad)

---

### `cubic`[​](#cubic)

```
static cubic(t): numberCopy
```

A cubic function, `f(t) = t * t * t`. Position equals the cube of elapsed time.

[http://easings.net/#easeInCubic](http://easings.net/#easeInCubic)

---

### `poly()`[​](#poly)

```
static poly(n): (t) => numberCopy
```

A power function. Position is equal to the Nth power of elapsed time.

n = 4: [http://easings.net/#easeInQuart](http://easings.net/#easeInQuart) n = 5: [http://easings.net/#easeInQuint](http://easings.net/#easeInQuint)

---

### `sin`[​](#sin)

```
static sin(t): numberCopy
```

A sinusoidal function.

[http://easings.net/#easeInSine](http://easings.net/#easeInSine)

---

### `circle`[​](#circle)

```
static circle(t): numberCopy
```

A circular function.

[http://easings.net/#easeInCirc](http://easings.net/#easeInCirc)

---

### `exp`[​](#exp)

```
static exp(t): numberCopy
```

An exponential function.

[http://easings.net/#easeInExpo](http://easings.net/#easeInExpo)

---

### `elastic()`[​](#elastic)

```
static elastic(bounciness): (t) =>  numberCopy
```

A basic elastic interaction, similar to a spring oscillating back and forth.

Default bounciness is 1, which overshoots a little bit once. 0 bounciness doesn't overshoot at all, and bounciness of N > 1 will overshoot about N times.

[http://easings.net/#easeInElastic](http://easings.net/#easeInElastic)

---

### `back()`[​](#back)

```
static back(s): (t) => numberCopy
```

Use with `Animated.parallel()` to create a basic effect where the object animates back slightly as the animation starts.

---

### `bounce`[​](#bounce)

```
static bounce(t): numberCopy
```

Provides a basic bouncing effect.

[http://easings.net/#easeInBounce](http://easings.net/#easeInBounce)

See an example of how you might use it below

```
interpolate(0.5, [0, 1], [0, 1], {
  easing: Easing.bounce,
});Copy
```

---

### `bezier()`[​](#bezier)

```
static bezier(x1, y1, x2, y2) => (t): numberCopy
```

Provides a cubic bezier curve, equivalent to CSS Transitions' `transition-timing-function`.

A useful tool to visualize cubic bezier curves can be found at [http://cubic-bezier.com/](http://cubic-bezier.com/)

```
interpolate(0.5, [0, 1], [0, 1], {
  easing: Easing.bezier(0.5, 0.01, 0.5, 1),
});Copy
```

---

### `in(easing)`[​](#ineasing)

```
static in(easing: (t: number) => number): (t: number) => number;Copy
```

Runs an easing function forwards.

```
{
  easing: Easing.in(Easing.ease);
}Copy
```

---

### `out()`[​](#out)

```
static out(easing: (t: number) => number): (t: number) => number;Copy
```

Runs an easing function backwards.

```
{
  easing: Easing.out(Easing.ease);
}Copy
```

---

### `inOut()`[​](#inout)

```
static inOut(easing: (t: number) => number): (t: number) => number;Copy
```

```
{
  easing: Easing.inOut(Easing.ease);
}Copy
```

Makes any easing function symmetrical. The easing function will run forwards for half of the duration, then backwards for the rest of the duration.

## Credits[​](#credits)

The Easing API is the exact same as the one from [React Native](https://reactnative.dev/docs/easing) and the documentation has been copied over. Credit goes to them for this excellent API.

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

- [Source code for this helper](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/easing.ts)

CONTRIBUTORS

[

**kaf-lamed-beyt**
Improved function signatures](https://github.com/kaf-lamed-beyt)](https://github.com/kaf-lamed-beyt)](https://github.com/kaf-lamed-beyt)
](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)
- ](https://github.com/kaf-lamed-beyt)