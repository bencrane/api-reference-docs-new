---
title: "<TransitionSeries>"
url: "https://www.remotion.dev/docs/transitions/transitionseries"
path: "/docs/transitions/transitionseries"
---

"---\nimage: /generated/articles-docs-transitions-transitionseries.png\ncrumb: '@remotion/transitions'\nsidebar_label: '<TransitionSeries>'\ntitle: '<TransitionSeries>'\n---\n\nimport {TransitionsDuration} from '../../components/TransitionsDuration';\n\n# &lt;TransitionSeries&gt;<AvailableFrom v=\"4.0.59\" />\n\nThe `<TransitionSeries>` component behaves the same as the [`<Series>`](/docs/series) component, but allows for [`<TransitionSeries.Transition>`](#transitionseriestransition) and [`<TransitionSeries.Overlay>`](#transitionseriesoverlay) components to be rendered between [`<TransitionSeries.Sequence>`](#transitionseriessequence) components.\n\nBetween any two sequences, you can place either a transition or an overlay:\n\n- A [`<TransitionSeries.Transition>`](#transitionseriestransition) crossfades, slides, or otherwise animates between two scenes.  \n  It [shortens](#duration-of-a-transitionseries) the total duration because both scenes overlap during the transition.\n- A [`<TransitionSeries.Overlay>`](#transitionseriesoverlay) renders children on top of the cut point without affecting timing.  \n  The sequences remain at full length — useful for effects like [light leaks](/docs/light-leaks/light-leak) or flashes.\n\n### Transition example\n\n```tsx twoslash title=\"TransitionExample.tsx\"\nimport {AbsoluteFill} from 'remotion';\nconst Fill = ({color}: {color: string}) => <AbsoluteFill style={{backgroundColor: color}} />;\n\n// ---cut---\nimport {linearTiming, springTiming, TransitionSeries} from '@remotion/transitions';\nimport {fade} from '@remotion/transitions/fade';\nimport {wipe} from '@remotion/transitions/wipe';\n\nexport const TransitionExample: React.FC = () => {\n  return (\n    <TransitionSeries>\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Fill color=\"#0b84f3\" />\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Transition timing={springTiming({config: {damping: 200}})} presentation={fade()} />\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Fill color=\"pink\" />\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Transition timing={linearTiming({durationInFrames: 30})} presentation={wipe()} />\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Fill color=\"#2ecc71\" />\n      </TransitionSeries.Sequence>\n    </TransitionSeries>\n  );\n};\n```\n\n<Demo type=\"transition-series-transition\" />\n\n### Overlay example<AvailableFrom v=\"4.0.415\" />\n\n```tsx twoslash title=\"OverlayExample.tsx\"\nimport {AbsoluteFill} from 'remotion';\nconst Fill = ({color}: {color: string}) => <AbsoluteFill style={{backgroundColor: color}} />;\n\n// ---cut---\nimport {LightLeak} from '@remotion/light-leaks';\nimport {TransitionSeries} from '@remotion/transitions';\n\nexport const OverlayExample: React.FC = () => {\n  return (\n    <TransitionSeries>\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Fill color=\"blue\" />\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Overlay durationInFrames={20}>\n        <LightLeak />\n      </TransitionSeries.Overlay>\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Fill color=\"black\" />\n      </TransitionSeries.Sequence>\n    </TransitionSeries>\n  );\n};\n```\n\n<Demo type=\"transition-series-overlay\" />\n\n## API\n\n### `<TransitionSeries>`\n\nInherits the [`from`](/docs/sequence#from), [`name`](/docs/sequence#name), [`className`](/docs/sequence#classname), and [`style`](/docs/sequence#style) props from [`<Sequence>`](/docs/sequence).\n\nThe `<TransitionSeries>` component can only contain `<TransitionSeries.Sequence>`, `<TransitionSeries.Transition>`, and `<TransitionSeries.Overlay>` components.\n\n### `<TransitionSeries.Sequence>`\n\nInherits the [`durationInFrames`](/docs/sequence#durationinframes), [`name`](/docs/sequence#name), [`className`](/docs/sequence#classname), [`style`](/docs/sequence#style), [`premountFor`](/docs/sequence#premountfor), [`postmountFor`](/docs/sequence#postmountfor) and [`layout`](/docs/sequence#layout) props from [`<Sequence>`](/docs/sequence).\n\nAs children, put the contents of your scene.\n\n### `<TransitionSeries.Transition>`\n\nPlaced between two sequences to animate from one scene to the next.  \nDuring the transition, both scenes are rendered simultaneously and the total duration is [shortened](#duration-of-a-transitionseries) by the transition length.\n\nTakes two props:\n\n- `timing`: A timing of type `TransitionTiming`. See [Timings](/docs/transitions/timings) for more information.\n- `presentation?`: A presentation of type `TransitionPresentation`. If not specified, the default value is [`slide()`](/docs/transitions/presentations/slide). See [Presentations](/docs/transitions/presentations) for more information.\n\nMust be a direct child of `<TransitionSeries>`.\nAt least one `<TransitionSeries.Sequence>` component must come before or after the `<TransitionSeries.Transition>` component.\n\n### `<TransitionSeries.Overlay>`<AvailableFrom v=\"4.0.415\" />\n\nPlaced between two sequences to render children on top of the cut point.  \nThe overlay does [not shorten](#duration-of-a-transitionseries) the timeline — adjacent sequences remain at full length.\n\nThe overlay is centered on the cut point by default: half the duration before the cut, half after.  \nChildren animate independently — no progress context is provided.\n\nTakes two props:\n\n- `durationInFrames`: How long the overlay is visible. Must be a positive integer.\n- `offset?`: Shifts the overlay relative to the center of the cut point. Positive values shift right (later), negative values shift left (earlier). Default: `0`. Must be a finite integer.\n\nThe overlay must not extend before frame 0 or beyond the duration of the adjacent sequences.\n\n## Enter and exit animations\n\nYou don't necessarily have to use `<TransitionSeries>` for transitions between scenes. You can also use it to animate the entrace or exit of a scene by putting a transition first or last in the `<TransitionSeries>`.\n\n```tsx twoslash title=\"SlideTransition.tsx\"\nimport {AbsoluteFill} from 'remotion';\n\nconst Letter: React.FC<{\n  children: React.ReactNode;\n  color: string;\n}> = ({children, color}) => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: color,\n        opacity: 0.9,\n        justifyContent: 'center',\n        alignItems: 'center',\n        fontSize: 200,\n        color: 'white',\n      }}\n    >\n      {children}\n    </AbsoluteFill>\n  );\n};\n// ---cut---\nimport {linearTiming, TransitionSeries} from '@remotion/transitions';\nimport {slide} from '@remotion/transitions/slide';\n\nconst BasicTransition = () => {\n  return (\n    <TransitionSeries>\n      <TransitionSeries.Sequence durationInFrames={40}>\n        <Letter color=\"#0b84f3\">A</Letter>\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 30})} />\n    </TransitionSeries>\n  );\n};\n```\n\n<Demo type=\"transition-series-enter-exit\" />\n\n## Duration of a `<TransitionSeries>`\n\n[Transitions](#transitionseriestransition) shorten the total duration because both scenes overlap.  \n[Overlays](#transitionseriesoverlay) do not — the total duration stays the same as if no overlay was present.\n\nConsider this example:\n\n```tsx twoslash title=\"SlideTransition.tsx\"\nimport {AbsoluteFill} from 'remotion';\n\nconst Letter: React.FC<{\n  children: React.ReactNode;\n  color: string;\n}> = ({children, color}) => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: color,\n        opacity: 0.9,\n        justifyContent: 'center',\n        alignItems: 'center',\n        fontSize: 200,\n        color: 'white',\n      }}\n    >\n      {children}\n    </AbsoluteFill>\n  );\n};\n// ---cut---\nimport {linearTiming, TransitionSeries} from '@remotion/transitions';\nimport {slide} from '@remotion/transitions/slide';\n\nconst BasicTransition = () => {\n  return (\n    <TransitionSeries>\n      <TransitionSeries.Sequence durationInFrames={40}>\n        <Letter color=\"#0b84f3\">A</Letter>\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 30})} />\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Letter color=\"pink\">B</Letter>\n      </TransitionSeries.Sequence>\n    </TransitionSeries>\n  );\n};\n```\n\n`A` is visible for 40 frames, `B` for 60 frames and the duration of the transition is 30 frames.\nDuring this time, both slides are rendered. This means the total duration of the animation is `60 + 40 - 30 = 70`.\n\n<TransitionsDuration />\n\n<details>\n<summary>Example with 3 slides</summary>\n\n```tsx twoslash title=\"SlideTransition.tsx\"\nimport {AbsoluteFill} from 'remotion';\n\nconst Letter: React.FC<{\n  children: React.ReactNode;\n  color: string;\n}> = ({children, color}) => {\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: color,\n        opacity: 0.9,\n        justifyContent: 'center',\n        alignItems: 'center',\n        fontSize: 200,\n        color: 'white',\n      }}\n    >\n      {children}\n    </AbsoluteFill>\n  );\n};\n// ---cut---\nimport {linearTiming, TransitionSeries} from '@remotion/transitions';\nimport {slide} from '@remotion/transitions/slide';\n\nconst BasicTransition = () => {\n  return (\n    <TransitionSeries>\n      <TransitionSeries.Sequence durationInFrames={40}>\n        <Letter color=\"#0b84f3\">A</Letter>\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 30})} />\n      <TransitionSeries.Sequence durationInFrames={60}>\n        <Letter color=\"pink\">B</Letter>\n      </TransitionSeries.Sequence>\n      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 45})} />\n      <TransitionSeries.Sequence durationInFrames={90}>\n        <Letter color=\"green\">C</Letter>\n      </TransitionSeries.Sequence>\n    </TransitionSeries>\n  );\n};\n```\n\n- The first slide is shown for 40 frames\n- The second slide is shown for 60 frames\n- The third slide is shown for 90 frames\n- There are two transitions, one 30 frames long and one 45 frames long\n\n1. Sum up the durations: `40 + 60 + 90 = 190`\n2. Subtract the duration of the transitions: `190 - 30 - 45 = 115`\n\n</details>\n\n## Getting the duration of a transition\n\nYou can get the duration of a transition by calling `getDurationInFrames()` on the timing:\n\n```tsx twoslash title=\"Assuming a framerate of 30fps\"\nimport {springTiming} from '@remotion/transitions';\n\nspringTiming({config: {damping: 200}}).getDurationInFrames({fps: 30}); // 23\n```\n\n## Rules\n\n<Step>1</Step> A transition must not be longer than the duration of the previous or next sequence.\n\n<Step>2</Step> Two transitions cannot be adjacent.\n\n<Step>3</Step> Two overlays cannot be adjacent.\n\n<Step>4</Step> A transition and an overlay cannot be adjacent — they occupy the same slot between sequences.\n\n<Step>5</Step> There must be at least one sequence before or after a transition or overlay.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/transitions/src/TransitionSeries.tsx)\n- [Transitions](/docs/transitioning)\n- [Timings](/docs/transitions/timings)\n- [Presentations](/docs/transitions/presentations)\n- [`<Series>`](/docs/series)\n"

The `<TransitionSeries>` component behaves the same as the [`<Series>`](/docs/series) component, but allows for [`<TransitionSeries.Transition>`](#transitionseriestransition) and [`<TransitionSeries.Overlay>`](#transitionseriesoverlay) components to be rendered between [`<TransitionSeries.Sequence>`](#transitionseriessequence) components.

Between any two sequences, you can place either a transition or an overlay:

- A [`<TransitionSeries.Transition>`](#transitionseriestransition) crossfades, slides, or otherwise animates between two scenes.

It [shortens](#duration-of-a-transitionseries) the total duration because both scenes overlap during the transition.

- A [`<TransitionSeries.Overlay>`](#transitionseriesoverlay) renders children on top of the cut point without affecting timing.

The sequences remain at full length — useful for effects like [light leaks](/docs/light-leaks/light-leak) or flashes.

### Transition example[​](#transition-example)

```

TransitionExample.tsximport {linearTiming, springTiming, TransitionSeries} from '@remotion/transitions';
import {fade} from '@remotion/transitions/fade';
import {wipe} from '@remotion/transitions/wipe';

export const TransitionExample: React.FC = () => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="#0b84f3" />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition timing={springTiming({config: {damping: 200}})} presentation={fade()} />
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="pink" />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition timing={linearTiming({durationInFrames: 30})} presentation={wipe()} />
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="#2ecc71" />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};Copy
```

presentation
fadeslidewipe
transitionDuration
`15`

### Overlay example[v4.0.415](https://github.com/remotion-dev/remotion/releases/v4.0.415)[​](#overlay-example)

```

OverlayExample.tsximport {LightLeak} from '@remotion/light-leaks';
import {TransitionSeries} from '@remotion/transitions';

export const OverlayExample: React.FC = () => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="blue" />
      </TransitionSeries.Sequence>
      <TransitionSeries.Overlay durationInFrames={20}>
        <LightLeak />
      </TransitionSeries.Overlay>
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="black" />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};Copy
```

overlayDuration
`30`
offset
`0`

## API[​](#api)

### `<TransitionSeries>`[​](#transitionseries-1)

Inherits the [`from`](/docs/sequence#from), [`name`](/docs/sequence#name), [`className`](/docs/sequence#classname), and [`style`](/docs/sequence#style) props from [`<Sequence>`](/docs/sequence).

The `<TransitionSeries>` component can only contain `<TransitionSeries.Sequence>`, `<TransitionSeries.Transition>`, and `<TransitionSeries.Overlay>` components.

### `<TransitionSeries.Sequence>`[​](#transitionseriessequence)

Inherits the [`durationInFrames`](/docs/sequence#durationinframes), [`name`](/docs/sequence#name), [`className`](/docs/sequence#classname), [`style`](/docs/sequence#style), [`premountFor`](/docs/sequence#premountfor), [`postmountFor`](/docs/sequence#postmountfor) and [`layout`](/docs/sequence#layout) props from [`<Sequence>`](/docs/sequence).

As children, put the contents of your scene.

### `<TransitionSeries.Transition>`[​](#transitionseriestransition)

Placed between two sequences to animate from one scene to the next.

During the transition, both scenes are rendered simultaneously and the total duration is [shortened](#duration-of-a-transitionseries) by the transition length.

Takes two props:

- `timing`: A timing of type `TransitionTiming`. See [Timings](/docs/transitions/timings) for more information.

- `presentation?`: A presentation of type `TransitionPresentation`. If not specified, the default value is [`slide()`](/docs/transitions/presentations/slide). See [Presentations](/docs/transitions/presentations) for more information.

Must be a direct child of `<TransitionSeries>`.
At least one `<TransitionSeries.Sequence>` component must come before or after the `<TransitionSeries.Transition>` component.

### `<TransitionSeries.Overlay>`[v4.0.415](https://github.com/remotion-dev/remotion/releases/v4.0.415)[​](#transitionseriesoverlay)

Placed between two sequences to render children on top of the cut point.

The overlay does [not shorten](#duration-of-a-transitionseries) the timeline — adjacent sequences remain at full length.

The overlay is centered on the cut point by default: half the duration before the cut, half after.

Children animate independently — no progress context is provided.

Takes two props:

- `durationInFrames`: How long the overlay is visible. Must be a positive integer.

- `offset?`: Shifts the overlay relative to the center of the cut point. Positive values shift right (later), negative values shift left (earlier). Default: `0`. Must be a finite integer.

The overlay must not extend before frame 0 or beyond the duration of the adjacent sequences.

## Enter and exit animations[​](#enter-and-exit-animations)

You don't necessarily have to use `<TransitionSeries>` for transitions between scenes. You can also use it to animate the entrace or exit of a scene by putting a transition first or last in the `<TransitionSeries>`.

```

SlideTransition.tsximport {linearTiming, TransitionSeries} from '@remotion/transitions';
import {slide} from '@remotion/transitions/slide';

const BasicTransition = () => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={40}>
        <Letter color="#0b84f3">A</Letter>
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 30})} />
    </TransitionSeries>
  );
};Copy
```

presentation
slidefadewipe

## Duration of a `<TransitionSeries>`[​](#duration-of-a-transitionseries)

[Transitions](#transitionseriestransition) shorten the total duration because both scenes overlap.

[Overlays](#transitionseriesoverlay) do not — the total duration stays the same as if no overlay was present.

Consider this example:

```

SlideTransition.tsximport {linearTiming, TransitionSeries} from '@remotion/transitions';
import {slide} from '@remotion/transitions/slide';

const BasicTransition = () => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={40}>
        <Letter color="#0b84f3">A</Letter>
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 30})} />
      <TransitionSeries.Sequence durationInFrames={60}>
        <Letter color="pink">B</Letter>
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};Copy
```

`A` is visible for 40 frames, `B` for 60 frames and the duration of the transition is 30 frames.
During this time, both slides are rendered. This means the total duration of the animation is `60 + 40 - 30 = 70`.

Example with 3 slides

```

SlideTransition.tsximport {linearTiming, TransitionSeries} from '@remotion/transitions';
import {slide} from '@remotion/transitions/slide';

const BasicTransition = () => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={40}>
        <Letter color="#0b84f3">A</Letter>
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 30})} />
      <TransitionSeries.Sequence durationInFrames={60}>
        <Letter color="pink">B</Letter>
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={slide()} timing={linearTiming({durationInFrames: 45})} />
      <TransitionSeries.Sequence durationInFrames={90}>
        <Letter color="green">C</Letter>
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};Copy
```

- The first slide is shown for 40 frames

- The second slide is shown for 60 frames

- The third slide is shown for 90 frames

- There are two transitions, one 30 frames long and one 45 frames long

- Sum up the durations: `40 + 60 + 90 = 190`

- Subtract the duration of the transitions: `190 - 30 - 45 = 115`

## Getting the duration of a transition[​](#getting-the-duration-of-a-transition)

You can get the duration of a transition by calling `getDurationInFrames()` on the timing:

```

Assuming a framerate of 30fpsimport {springTiming} from '@remotion/transitions';

springTiming({config: {damping: 200}}).getDurationInFrames({fps: 30}); // 23Copy
```

## Rules[​](#rules)

[](#1)
[1](#1)[ ](#1) A transition must not be longer than the duration of the previous or next sequence.

[](#2)
[2](#2)[ ](#2) Two transitions cannot be adjacent.

[](#3)
[3](#3)[ ](#3) Two overlays cannot be adjacent.

[](#4)
[4](#4)[ ](#4) A transition and an overlay cannot be adjacent — they occupy the same slot between sequences.

[](#5)
[5](#5)[ ](#5) There must be at least one sequence before or after a transition or overlay.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/transitions/src/TransitionSeries.tsx)

- [Transitions](/docs/transitioning)

- [Timings](/docs/transitions/timings)

- [Presentations](/docs/transitions/presentations)

- [`<Series>`](/docs/series)
](/docs/series)](/docs/series)
](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)
- ](/docs/series)