---
title: "<Trail>"
url: "https://www.remotion.dev/docs/motion-blur/trail"
path: "/docs/motion-blur/trail"
---

"---\nimage: /generated/articles-docs-motion-blur-trail.png\ntitle: '<Trail>'\nslug: trail\ncrumb: 'Motion blur'\n---\n\nimport {TrailExample} from '../../components/TrailExample/TrailExample';\n\n```twoslash include example\nconst BlueSquare: React.FC = () => <div></div>\n// - BlueSquare\n```\n\n_available from v3.2.39, previously called `<MotionBlur>`_\n\nThe `<Trail>` component duplicates it's children and adds a time offset to each layer in order to create a trail effect.\n\nFor this technique to work, the children must be absolutely positioned so many layers can be created without influencing the layout.  \nYou can use the [`<AbsoluteFill>`](/docs/absolute-fill) component to absolutely position content.\n\n## API\n\nWrap your content in `<Trail>` and add the following props in addition.\n\n### `layers`\n\nHow many layers are added below the content. Must be an integer\n\n### `lagInFrames`\n\nHow many frames each layer is lagging behind the last one. Can also a floating point number.\n\n### `trailOpacity`\n\n_previously called `blurOpacity`_\n\nThe highest opacity of a layer. The lowest opacity is 0 and layers intbetween get interpolated.\n\n## Example usage\n\n```tsx twoslash\n// @include: example-BlueSquare\n// ---cut---\nimport {Trail} from '@remotion/motion-blur';\nimport {AbsoluteFill} from 'remotion';\n\nexport const MyComposition = () => {\n  return (\n    <Trail layers={50} lagInFrames={0.1} trailOpacity={1}>\n      <AbsoluteFill\n        style={{\n          backgroundColor: 'white',\n          justifyContent: 'center',\n          alignItems: 'center',\n        }}\n      >\n        <BlueSquare />\n      </AbsoluteFill>\n    </Trail>\n  );\n};\n```\n\n## Demo\n\n<TrailExample />\n\n<Credits\n  contributors={[\n    {\n      username: 'UmungoBungo',\n      contribution: 'Implementation',\n    },\n  ]}\n/>\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/motion-blur/src/Trail.tsx)\n- [Common mistake with `<Trail>` and `<CameraMotionBlur>`](/docs/motion-blur/common-mistake)\n"

*available from v3.2.39, previously called `<MotionBlur>`*

The `<Trail>` component duplicates it's children and adds a time offset to each layer in order to create a trail effect.

For this technique to work, the children must be absolutely positioned so many layers can be created without influencing the layout.

You can use the [`<AbsoluteFill>`](/docs/absolute-fill) component to absolutely position content.

## API[​](#api)

Wrap your content in `<Trail>` and add the following props in addition.

### `layers`[​](#layers)

How many layers are added below the content. Must be an integer

### `lagInFrames`[​](#laginframes)

How many frames each layer is lagging behind the last one. Can also a floating point number.

### `trailOpacity`[​](#trailopacity)

*previously called `blurOpacity`*

The highest opacity of a layer. The lowest opacity is 0 and layers intbetween get interpolated.

## Example usage[​](#example-usage)

```
import {Trail} from '@remotion/motion-blur';
import {AbsoluteFill} from 'remotion';

export const MyComposition = () => {
  return (
    <Trail layers={50} lagInFrames={0.1} trailOpacity={1}>
      <AbsoluteFill
        style={{
          backgroundColor: 'white',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <BlueSquare />
      </AbsoluteFill>
    </Trail>
  );
};Copy
```

## Demo[​](#demo)

`layers={50}`
`trailOpacity={1}`
`lagInFrames={0.3}`

CONTRIBUTORS

[

**UmungoBungo**
Implementation](https://github.com/UmungoBungo)

## See also[​](#see-also)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/motion-blur/src/Trail.tsx)

- [Common mistake with `<Trail>` and `<CameraMotionBlur>`](/docs/motion-blur/common-mistake)
](/docs/motion-blur/common-mistake)](/docs/motion-blur/common-mistake)
](/docs/motion-blur/common-mistake)
- ](/docs/motion-blur/common-mistake)
- ](/docs/motion-blur/common-mistake)
- ](/docs/motion-blur/common-mistake)
- ](/docs/motion-blur/common-mistake)
- ](/docs/motion-blur/common-mistake)
- ](/docs/motion-blur/common-mistake)