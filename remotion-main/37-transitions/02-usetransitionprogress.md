---
title: "useTransitionProgress()"
url: "https://www.remotion.dev/docs/transitions/use-transition-progress"
path: "/docs/transitions/use-transition-progress"
---

"---\nimage: /generated/articles-docs-transitions-use-transition-progress.png\ncrumb: \"@remotion/transitions\"\nsidebar_label: useTransitionProgress()\ntitle: useTransitionProgress()\n---\n\n# useTransitionProgress()<AvailableFrom v=\"4.0.177\"/>\n\nA hook that can be used inside a child of a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries) to get the progress of the transition to directly manipulate the objects inside the scene.\n\nIt is meant to be used together with the [`none()`](/docs/transitions/presentations/none) presentation, but can be used with any other presentation.\n\n## Example\n\n```tsx twoslash title=\"useTransitionProgress()\"\nimport { useTransitionProgress } from \"@remotion/transitions\";\nimport { linearTiming, TransitionSeries } from \"@remotion/transitions\";\nimport { none } from \"@remotion/transitions/none\";\n\nconst A: React.FC = () => {\n  const progress = useTransitionProgress();\n  console.log(progress.entering); // Always `1`\n  console.log(progress.exiting); // Going from 0 to 1\n  console.log(progress.isInTransitionSeries); //  `true`\n\n  return <div>A</div>;\n};\n\nconst B: React.FC = () => {\n  const progress = useTransitionProgress();\n  console.log(progress.entering); // Going from 0 to 1\n  console.log(progress.exiting); // Always `0`\n  console.log(progress.isInTransitionSeries); //  `true`\n\n  return <div>B</div>;\n};\n\nconst C: React.FC = () => {\n  const progress = useTransitionProgress();\n  console.log(progress.entering); // Always `1`\n  console.log(progress.exiting); // Always `0`\n  console.log(progress.isInTransitionSeries); //  `false`\n\n  return <div>C</div>;\n};\n\nconst Transition: React.FC = () => {\n  return (\n    <>\n      <TransitionSeries>\n        <TransitionSeries.Sequence durationInFrames={40}>\n          <A />\n        </TransitionSeries.Sequence>\n        <TransitionSeries.Transition\n          presentation={none()}\n          timing={linearTiming({ durationInFrames: 30 })}\n        />\n        <TransitionSeries.Sequence durationInFrames={60}>\n          <B />\n        </TransitionSeries.Sequence>\n      </TransitionSeries>\n      <C />\n    </>\n  );\n};\n```\n\n## API\n\nA React hook that returns an object with the following properties:\n\n### `entering`\n\nThe progress of the entering scene. If not inside a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries), it will always be `1`.\n\n### `exiting`\n\nThe progress of the exiting scene. If not inside a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries), it will always be `0`.\n\n### `isInTransitionSeries`\n\nWhether the current scene is inside a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries).\n\n## See also\n\n- [Source code for this hook](https://github.com/remotion-dev/remotion/blob/main/packages/transitions/src/use-transition-progress.ts)\n- [`<TransitionSeries>`](/docs/transitions/transitionseries)\n"

A hook that can be used inside a child of a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries) to get the progress of the transition to directly manipulate the objects inside the scene.

It is meant to be used together with the [`none()`](/docs/transitions/presentations/none) presentation, but can be used with any other presentation.

## Example[​](#example)

```

useTransitionProgress()import { useTransitionProgress } from "@remotion/transitions";
import { linearTiming, TransitionSeries } from "@remotion/transitions";
import { none } from "@remotion/transitions/none";

const A: React.FC = () => {
  const progress = useTransitionProgress();
  console.log(progress.entering); // Always `1`
  console.log(progress.exiting); // Going from 0 to 1
  console.log(progress.isInTransitionSeries); //  `true`

  return <div>A</div>;
};

const B: React.FC = () => {
  const progress = useTransitionProgress();
  console.log(progress.entering); // Going from 0 to 1
  console.log(progress.exiting); // Always `0`
  console.log(progress.isInTransitionSeries); //  `true`

  return <div>B</div>;
};

const C: React.FC = () => {
  const progress = useTransitionProgress();
  console.log(progress.entering); // Always `1`
  console.log(progress.exiting); // Always `0`
  console.log(progress.isInTransitionSeries); //  `false`

  return <div>C</div>;
};

const Transition: React.FC = () => {
  return (
    <>
      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={40}>
          <A />
        </TransitionSeries.Sequence>
        <TransitionSeries.Transition
          presentation={none()}
          timing={linearTiming({ durationInFrames: 30 })}
        />
        <TransitionSeries.Sequence durationInFrames={60}>
          <B />
        </TransitionSeries.Sequence>
      </TransitionSeries>
      <C />
    </>
  );
};Copy
```

## API[​](#api)

A React hook that returns an object with the following properties:

### `entering`[​](#entering)

The progress of the entering scene. If not inside a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries), it will always be `1`.

### `exiting`[​](#exiting)

The progress of the exiting scene. If not inside a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries), it will always be `0`.

### `isInTransitionSeries`[​](#isintransitionseries)

Whether the current scene is inside a [`<TransitionSeries.Sequence>`](/docs/transitions/transitionseries).

## See also[​](#see-also)

- [Source code for this hook](https://github.com/remotion-dev/remotion/blob/main/packages/transitions/src/use-transition-progress.ts)

- [`<TransitionSeries>`](/docs/transitions/transitionseries)
](/docs/transitions/transitionseries)](/docs/transitions/transitionseries)
](/docs/transitions/transitionseries)
- ](/docs/transitions/transitionseries)
- ](/docs/transitions/transitionseries)
- ](/docs/transitions/transitionseries)
- ](/docs/transitions/transitionseries)
- ](/docs/transitions/transitionseries)