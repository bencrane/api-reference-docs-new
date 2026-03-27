---
title: "interpolate()"
url: "https://www.remotion.dev/docs/interpolate"
path: "/docs/interpolate"
---

"---\nimage: /generated/articles-docs-interpolate.png\ntitle: interpolate()\nid: interpolate\ncrumb: 'API'\n---\n\n<YouTube minutes={6} href=\"https://www.youtube.com/watch?v=sff_CdWw_-c\" thumb=\"https://i.ytimg.com/vi/sff_CdWw_-c/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDPXdTFxf6qNNfkSr_91y0xVTXaXQ\" title=\"How to interpolate()\" />\n\nAllows you to map a range of values to another using a concise syntax.\n\n## Example: Fade-in effect\n\nIn this example, we are fading in some content by calculating the opacity for a certain point of time.\nAt frame 0 (the start of the video), we want the opacity to be 0.\nAt frame 20, we want the opacity to be 1.\n\nUsing the following snippet, we can calculate the current opacity for any frame:\n\n```ts twoslash\nimport {interpolate, useCurrentFrame} from 'remotion';\n\nconst frame = useCurrentFrame(); // 10\nconst opacity = interpolate(frame, [0, 20], [0, 1]); // 0.5\n```\n\n## Example: Fade in and out\n\nWe keep our fade in effect but add a fade out effect at the end.\n20 frames before the video ends, the opacity should still be 1.\nAt the end, the opacity should be 0.\n\nWe can interpolate over multiple points in one go and use [`useVideoConfig()`](/docs/use-video-config) to determine the duration of the composition.\n\n```ts twoslash\nimport {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';\n\nconst frame = useCurrentFrame();\nconst {durationInFrames} = useVideoConfig();\nconst opacity = interpolate(\n  frame,\n  [0, 20, durationInFrames - 20, durationInFrames],\n  // v--v---v----------------------v\n  [0, 1, 1, 0],\n);\n```\n\n## Example: interpolate a spring animation\n\nWe don't necessarily have to interpolate over time - we can use any value to drive an animation.\nLet's assume we want to animate an object on the X axis from 0 to 200 pixels and use a spring animation for it.\n\nLet's create a spring:\n\n```twoslash include example\nimport {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';\n\nconst frame = useCurrentFrame();\nconst {fps} = useVideoConfig();\nconst driver = spring({\n  frame,\n  fps\n});\n// - spring\n```\n\n```ts twoslash\n// @include: example-spring\n```\n\nA [`spring()`](/docs/spring) animation with it's default settings will animate from 0 to 1.\nGiven that knowledge, we can interpolate the spring value to go from 0 to 200.\n\n```ts twoslash\n// @include: example-spring\n// ---cut---\nconst marginLeft = interpolate(driver, [0, 1], [0, 200]);\n```\n\nWe can then apply it to an HTML element.\n\n```tsx twoslash {1}\n// @include: example-spring\nconst marginLeft = interpolate(driver, [0, 1], [0, 200]);\n// ---cut---\nconst Component: React.FC = () => <div style={{marginLeft}}></div>;\n```\n\n## Example: Prevent the output from going outside the output range\n\nConsider the following interpolation which is supposed to animate the scale over 20 frames:\n\n```tsx twoslash\nimport {interpolate, useCurrentFrame} from 'remotion';\nconst frame = useCurrentFrame();\n// ---cut---\nconst scale = interpolate(frame, [0, 20], [0, 1]);\n```\n\nThis works, but after 20 frames, the value keeps growing. For example, at frame 40, the scale will be `2`.\nTo prevent this, this we can use the `extrapolateLeft` and `extrapolateRight` options and set them to `'clamp'` to prevent the result going outside the output range.\n\n```tsx twoslash\nimport {interpolate, useCurrentFrame} from 'remotion';\nconst frame = useCurrentFrame();\n// ---cut---\nconst scale = interpolate(frame, [0, 20], [0, 1], {\n  extrapolateRight: 'clamp',\n});\n```\n\n## API\n\nTakes four arguments:\n\n1. The input value.\n2. The range of values that you expect the input to assume.\n3. The range of output values that you want the input to map to.\n4. Options object:\n\n### extrapolateLeft?\n\n_Default_: `extend`\n\nWhat should happen if the input value is outside the left side of the input range:\n\n- `extend`: Interpolate nonetheless, even if outside output range.\n- `clamp`: Return the closest value inside the range instead\n- `wrap`: Loops the value change.\n- `identity`: Return the input value instead.\n\n### extrapolateRight?\n\n_Default_: `extend`\n\nSame as [extrapolateLeft](#extrapolateleft), except for values outside right the input range.\n\nExample:\n\n```tsx twoslash\nimport {interpolate} from 'remotion';\n// ---cut---\ninterpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'extend'}); // 3\ninterpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'clamp'}); // 2\ninterpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'identity'}); // 1.5\ninterpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'wrap'}); // 1\n```\n\n### easing?\n\n_Default_: `(x) => x`\n\nFunction which allows you to customize the input, for example to apply a certain easing function.\nBy default, the input is left unmodified, resulting in a pure linear interpolation. [Read the documentation for the built-in easing functions](/docs/easing).\n\n```ts twoslash\nimport {useCurrentFrame} from 'remotion';\nconst frame = useCurrentFrame();\n// ---cut---\nimport {interpolate, Easing} from 'remotion';\n\ninterpolate(frame, [0, 100], [0, 1], {\n  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),\n  extrapolateLeft: 'clamp',\n  extrapolateRight: 'clamp',\n});\n\n//this is Remotion2.0 feature\ninterpolate(frame, [0, 10, 40, 100], [0, 0.2, 0.6, 1], {\n  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),\n  extrapolateLeft: 'clamp',\n  extrapolateRight: 'clamp',\n});\n```\n\n## Types\n\nSince `v3.3.77`, types for the options are exported from Remotion.\n\n```tsx twoslash\nimport {ExtrapolateType, InterpolateOptions} from 'remotion';\n\nconst extrapolate: ExtrapolateType = 'clamp';\nconst option: InterpolateOptions = {extrapolateLeft: extrapolate};\n```\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs bun serverlessFunctions clientSideRendering serverSideRendering player studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/interpolate.ts)\n- [Easing](/docs/easing)\n- [spring()](/docs/spring)\n- [interpolateColors()](/docs/interpolate-colors)\n"
[

Also available as a 6min video 
**How to interpolate()**](https://www.youtube.com/watch?v=sff_CdWw_-c)

Allows you to map a range of values to another using a concise syntax.

## Example: Fade-in effect[​](#example-fade-in-effect)

In this example, we are fading in some content by calculating the opacity for a certain point of time.
At frame 0 (the start of the video), we want the opacity to be 0.
At frame 20, we want the opacity to be 1.

Using the following snippet, we can calculate the current opacity for any frame:

```
import {interpolate, useCurrentFrame} from 'remotion';

const frame = useCurrentFrame(); // 10
const opacity = interpolate(frame, [0, 20], [0, 1]); // 0.5Copy
```

## Example: Fade in and out[​](#example-fade-in-and-out)

We keep our fade in effect but add a fade out effect at the end.
20 frames before the video ends, the opacity should still be 1.
At the end, the opacity should be 0.

We can interpolate over multiple points in one go and use [`useVideoConfig()`](/docs/use-video-config) to determine the duration of the composition.

```
import {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';

const frame = useCurrentFrame();
const {durationInFrames} = useVideoConfig();
const opacity = interpolate(
  frame,
  [0, 20, durationInFrames - 20, durationInFrames],
  // v--v---v----------------------v
  [0, 1, 1, 0],
);Copy
```

## Example: interpolate a spring animation[​](#example-interpolate-a-spring-animation)

We don't necessarily have to interpolate over time - we can use any value to drive an animation.
Let's assume we want to animate an object on the X axis from 0 to 200 pixels and use a spring animation for it.

Let's create a spring:

```
import {useCurrentFrame, interpolate, spring, useVideoConfig} from 'remotion';

const frame = useCurrentFrame();
const {fps} = useVideoConfig();
const driver = spring({
  frame,
  fps
});Copy
```

A [`spring()`](/docs/spring) animation with it's default settings will animate from 0 to 1.
Given that knowledge, we can interpolate the spring value to go from 0 to 200.

```
const marginLeft = interpolate(driver, [0, 1], [0, 200]);Copy
```

We can then apply it to an HTML element.

```
const Component: React.FC = () => <div style={{marginLeft}}></div>;Copy
```

## Example: Prevent the output from going outside the output range[​](#example-prevent-the-output-from-going-outside-the-output-range)

Consider the following interpolation which is supposed to animate the scale over 20 frames:

```
const scale = interpolate(frame, [0, 20], [0, 1]);Copy
```

This works, but after 20 frames, the value keeps growing. For example, at frame 40, the scale will be `2`.
To prevent this, this we can use the `extrapolateLeft` and `extrapolateRight` options and set them to `'clamp'` to prevent the result going outside the output range.

```
const scale = interpolate(frame, [0, 20], [0, 1], {
  extrapolateRight: 'clamp',
});Copy
```

## API[​](#api)

Takes four arguments:

- The input value.

- The range of values that you expect the input to assume.

- The range of output values that you want the input to map to.

- Options object:

### extrapolateLeft?[​](#extrapolateleft)

*Default*: `extend`

What should happen if the input value is outside the left side of the input range:

- `extend`: Interpolate nonetheless, even if outside output range.

- `clamp`: Return the closest value inside the range instead

- `wrap`: Loops the value change.

- `identity`: Return the input value instead.

### extrapolateRight?[​](#extrapolateright)

*Default*: `extend`

Same as [extrapolateLeft](#extrapolateleft), except for values outside right the input range.

Example:

```
interpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'extend'}); // 3
interpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'clamp'}); // 2
interpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'identity'}); // 1.5
interpolate(1.5, [0, 1], [0, 2], {extrapolateRight: 'wrap'}); // 1Copy
```

### easing?[​](#easing)

*Default*: `(x) => x`

Function which allows you to customize the input, for example to apply a certain easing function.
By default, the input is left unmodified, resulting in a pure linear interpolation. [Read the documentation for the built-in easing functions](/docs/easing).

```
import {interpolate, Easing} from 'remotion';

interpolate(frame, [0, 100], [0, 1], {
  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
});

//this is Remotion2.0 feature
interpolate(frame, [0, 10, 40, 100], [0, 0.2, 0.6, 1], {
  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
});Copy
```

## Types[​](#types)

Since `v3.3.77`, types for the options are exported from Remotion.

```
import {ExtrapolateType, InterpolateOptions} from 'remotion';

const extrapolate: ExtrapolateType = 'clamp';
const option: InterpolateOptions = {extrapolateLeft: extrapolate};Copy
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

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/interpolate.ts)

- [Easing](/docs/easing)

- [spring()](/docs/spring)

- [interpolateColors()](/docs/interpolate-colors)
](/docs/interpolate-colors)](/docs/interpolate-colors)
](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)
- ](/docs/interpolate-colors)