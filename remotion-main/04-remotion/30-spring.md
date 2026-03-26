---
title: "spring()"
url: "https://www.remotion.dev/docs/spring"
path: "/docs/spring"
---

"---\nimage: /generated/articles-docs-spring.png\nid: spring\ntitle: spring()\ncrumb: 'API'\n---\n\nA physics-based animation primitive.\n\nExample usage:\n\n```tsx twoslash title=\"spring-example.ts\"\nimport {spring, useCurrentFrame, useVideoConfig} from 'remotion';\n// ---cut---\nconst frame = useCurrentFrame();\nconst {fps} = useVideoConfig();\n\nconst value = spring({\n  frame,\n  fps,\n  config: {\n    stiffness: 100,\n  },\n});\n```\n\nIn the following example, the <code>value</code> controls the [`scale`](/docs/transforms#scale) property of the div:\n\n<Demo type=\"spring\" />\n\nTo disable the default bounce, increase the [`damping`](#damping) parameter.\n\n<Demo type=\"spring-damping\" />\n\nFor a more advanced playground, visit [remotion.dev/timing-editor](https://www.remotion.dev/timing-editor).\n\n## Parameters\n\n### `frame`\n\nThe current time value. Most of the time you want to pass in the return value of [`useCurrentFrame()`](/docs/use-current-frame). The spring animation starts at frame 0, so if you would like to delay the animation, you can pass a different value like `frame - 20`.\n\n### `fps`\n\nFor how many frames per second the spring animation should be calculated. This should always be the `fps` property of the return value of [`useVideoConfig()`](/docs/use-video-config).\n\n### `from?`\n\n_Default:_ `0`\n\nThe initial value of the animation.\n\n### `to?`\n\n_Default:_ `1`\n\nThe end value of the animation. Note that depending on the parameters, spring animations may overshoot the target a bit, before they bounce back to their final target.\n\n### `reverse?`<AvailableFrom v=\"3.3.92\" />\n\n_Default:_ `false`\n\nRender the animation in reverse. See: [Order of operations](#order-of-operations)\n\n### `config?`\n\nAn optional object that allows you to customize the physical properties of the animation.\n\n#### `mass?`\n\n_Default:_ `1`\n\nThe weight of the spring. If you reduce the mass, the animation becomes faster!\n\n#### `damping?`\n\n_Default_: `10`\n\nHow hard the animation decelerates.\n\n#### `stiffness?`\n\n_Default_: `100`\n\nSpring stiffness coefficient. Play with this one and it will affect how bouncy your animation is.\n\n#### `overshootClamping?`\n\n_Default_: `false`\n\nDetermines whether the animation can shoot over the `to` value. If set to true, if the animation goes over `to`, it will just return the value of `to`.\n\n### `durationInFrames?`<AvailableFrom v=\"3.0.27\" />\n\nStretches the animation curve so it is exactly as long as you specify.\n\n```tsx twoslash title=\"spring-example.ts\"\nimport {spring, useCurrentFrame, useVideoConfig} from 'remotion';\n// ---cut---\nconst frame = useCurrentFrame();\nconst {fps} = useVideoConfig();\n\nconst value = spring({\n  frame,\n  fps,\n  config: {\n    stiffness: 100,\n  },\n  durationInFrames: 40,\n});\n```\n\nSee also: [Order of operations](#order-of-operations)\n\n### `durationRestThreshold?`<AvailableFrom v=\"3.0.27\" />\n\nHow close the animation should be to the end in order to be considered finished for the calculation of the duration. Only has an effect if `durationInFrames` is also specified.\n\nFor example, if a `durationRestThreshold` of `0.001` is given, and the durationOfFrames is `30`, it means that after 30 frames, the spring has reached 99.9% (`1 - 0.001 = 0.999`) of it's distance to the end value.\n\n### `delay?`<AvailableFrom v=\"3.3.90\" />\n\nHow many frames to delay the animation for.\n\nFor example, if a `delay` of `25` is given frames 0-24 will return the initial value, and the animation will effectively start from frame 25. See also: [Order of operations](#order-of-operations)\n\n## Order of operations\n\nHere is the order of which the `durationInFrames`, `reverse` and `delay` operations are applied:\n\n<Step>1</Step> First the spring animation is stretched to the duration that you pass using <a href=\"#durationinframes\"><code>durationInFrames</code></a>, if you pass a duration.<br/>\n<Step>2</Step> Then the animation is reversed if you pass <a href=\"#reverse-\"><code>reverse: true</code></a>.<br/>\n<Step>3</Step> Then the animation is delayed if you pass <a href=\"#delay-\"><code>delay</code></a>.\n\n## Credit\n\nThis function was taken from [Reanimated 2](https://github.com/software-mansion/react-native-reanimated), which in itself was a huge inspiration for Remotion.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={true} bun={true} serverlessFunctions clientSideRendering serverSideRendering player studio />\n\n## See also\n\n- [Spring animation example](/docs/animating-properties#using-spring-animations)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/spring/index.ts)\n- [`interpolate()`](/docs/interpolate)\n- [`measureSpring()`](/docs/measure-spring)\n"

A physics-based animation primitive.

Example usage:

```

spring-example.tsconst frame = useCurrentFrame();
const {fps} = useVideoConfig();

const value = spring({
  frame,
  fps,
  config: {
    stiffness: 100,
  },
});Copy
```

In the following example, the `value` controls the [`scale`](/docs/transforms#scale) property of the div:

damping
`10`
mass
`1`
stiffness
`100`
durationInFrames
``
overshootClamping
reverse

To disable the default bounce, increase the [`damping`](#damping) parameter.

damping
`100`

For a more advanced playground, visit [remotion.dev/timing-editor](https://www.remotion.dev/timing-editor).

## Parameters[​](#parameters)

### `frame`[​](#frame)

The current time value. Most of the time you want to pass in the return value of [`useCurrentFrame()`](/docs/use-current-frame). The spring animation starts at frame 0, so if you would like to delay the animation, you can pass a different value like `frame - 20`.

### `fps`[​](#fps)

For how many frames per second the spring animation should be calculated. This should always be the `fps` property of the return value of [`useVideoConfig()`](/docs/use-video-config).

### `from?`[​](#from)

*Default:* `0`

The initial value of the animation.

### `to?`[​](#to)

*Default:* `1`

The end value of the animation. Note that depending on the parameters, spring animations may overshoot the target a bit, before they bounce back to their final target.

### `reverse?`[v3.3.92](https://github.com/remotion-dev/remotion/releases/v3.3.92)[​](#reverse)

*Default:* `false`

Render the animation in reverse. See: [Order of operations](#order-of-operations)

### `config?`[​](#config)

An optional object that allows you to customize the physical properties of the animation.

#### `mass?`[​](#mass)

*Default:* `1`

The weight of the spring. If you reduce the mass, the animation becomes faster!

#### `damping?`[​](#damping)

*Default*: `10`

How hard the animation decelerates.

#### `stiffness?`[​](#stiffness)

*Default*: `100`

Spring stiffness coefficient. Play with this one and it will affect how bouncy your animation is.

#### `overshootClamping?`[​](#overshootclamping)

*Default*: `false`

Determines whether the animation can shoot over the `to` value. If set to true, if the animation goes over `to`, it will just return the value of `to`.

### `durationInFrames?`[v3.0.27](https://github.com/remotion-dev/remotion/releases/v3.0.27)[​](#durationinframes)

Stretches the animation curve so it is exactly as long as you specify.

```

spring-example.tsconst frame = useCurrentFrame();
const {fps} = useVideoConfig();

const value = spring({
  frame,
  fps,
  config: {
    stiffness: 100,
  },
  durationInFrames: 40,
});Copy
```

See also: [Order of operations](#order-of-operations)

### `durationRestThreshold?`[v3.0.27](https://github.com/remotion-dev/remotion/releases/v3.0.27)[​](#durationrestthreshold)

How close the animation should be to the end in order to be considered finished for the calculation of the duration. Only has an effect if `durationInFrames` is also specified.

For example, if a `durationRestThreshold` of `0.001` is given, and the durationOfFrames is `30`, it means that after 30 frames, the spring has reached 99.9% (`1 - 0.001 = 0.999`) of it's distance to the end value.

### `delay?`[v3.3.90](https://github.com/remotion-dev/remotion/releases/v3.3.90)[​](#delay)

How many frames to delay the animation for.

For example, if a `delay` of `25` is given frames 0-24 will return the initial value, and the animation will effectively start from frame 25. See also: [Order of operations](#order-of-operations)

## Order of operations[​](#order-of-operations)

Here is the order of which the `durationInFrames`, `reverse` and `delay` operations are applied:

[](#1)
[1](#1)[ ](#1) First the spring animation is stretched to the duration that you pass using [`durationInFrames`](#durationinframes), if you pass a duration.

[
2 ](#2) Then the animation is reversed if you pass [`reverse: true`](#reverse-).

[
3 ](#3) Then the animation is delayed if you pass [`delay`](#delay-).

## Credit[​](#credit)

This function was taken from [Reanimated 2](https://github.com/software-mansion/react-native-reanimated), which in itself was a huge inspiration for Remotion.

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

- [Spring animation example](/docs/animating-properties#using-spring-animations)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/spring/index.ts)

- [`interpolate()`](/docs/interpolate)

- [`measureSpring()`](/docs/measure-spring)
](/docs/measure-spring)](/docs/measure-spring)
](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)
- ](/docs/measure-spring)