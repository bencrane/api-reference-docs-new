---
title: "<CameraMotionBlur>"
url: "https://www.remotion.dev/docs/motion-blur/camera-motion-blur"
path: "/docs/motion-blur/camera-motion-blur"
---

"---\nimage: /generated/articles-docs-motion-blur-camera-motion-blur.png\ntitle: '<CameraMotionBlur>'\nslug: camera-motion-blur\ncrumb: 'Realistic camera effect'\n---\n\nimport {CameraMotionBlurExample} from '../../components/CameraMotionBlurExample/CameraMotionBlurExample';\n\n```twoslash include example\nconst RainbowSquare: React.FC = () => <div></div>\n// - RainbowSquare\n```\n\n<AvailableFrom v=\"3.2.39\" />\n\nThe `<CameraMotionBlur>` produces natural looking motion blur similar to what would be produced by\na film camera.\n\nFor this technique to work, the children must be absolutely positioned so many layers can be created without influencing the layout.  \nYou can use the [`<AbsoluteFill>`](/docs/absolute-fill) component to absolutely position content.\n\n:::note\nThe technique is destructive to colors. It is recommended to keep the `samples` property as low as\npossible and carefully inspect that the output is of acceptable quality.\n:::\n\n## API\n\nWrap your content in `<CameraMotionBlur>` and optionally add the following props in addition.\n\n### `shutterAngle?`\n\nControls the amount of blur. Default: `180`.\n\nA lower value will result in less blur and a higher value will result in more.\n\nThe blur also depends on the frames per second (FPS). Higher FPS will naturally have less blur and\nlower FPS will have more blur.\n\nIn movies and TV common values are (FPS/shutter angle):\n\n- 24 fps / 180&deg; or 90&deg;\n- 25 fps / 180&deg; or 90&deg;\n- 30 fps / 180&deg; or 90&deg;\n- 50 fps / 180&deg; or 90&deg;\n- 60 fps / 180&deg; or 90&deg;\n\n<details>\n<summary>What is \"shutter angle\"?</summary>\nMany analog film cameras use rotating discs with partial cut-outs to block or let light through to\nexpose the analog film. Zero degrees is equal to completely blocking the light, and 360 degrees is\nthe same as not blocking any light at all.\n\nThe most common values used in the film industry are 90 and 180 degrees. These values are the same\nas what you've experienced in most movies.\n\nRead more here: [Rotary disc shutter on Wikipedia](https://en.wikipedia.org/wiki/Rotary_disc_shutter)\n\n</details>\n\n### `samples?`\n\nThe final image is an average of the samples. Default: `10`. For a value of `10` the component will render ten\nframes with different time offsets and combine them into a final image.\n\n:::caution\nA high number will produce a higher quality blur at the cost of image quality. See example below.\n\nRecommended values: 5-10.\n:::\n\n## Example usage\n\n```tsx twoslash\n// @include: example-RainbowSquare\n// ---cut---\nimport {CameraMotionBlur} from '@remotion/motion-blur';\nimport {AbsoluteFill} from 'remotion';\n\nexport const MyComposition = () => {\n  return (\n    <CameraMotionBlur shutterAngle={180} samples={10}>\n      <AbsoluteFill\n        style={{\n          backgroundColor: 'white',\n          justifyContent: 'center',\n          alignItems: 'center',\n        }}\n      >\n        <RainbowSquare />\n      </AbsoluteFill>\n    </CameraMotionBlur>\n  );\n};\n```\n\n## Demo\n\n<CameraMotionBlurExample />\n\n## See also\n\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/motion-blur/src/CameraMotionBlur.tsx)\n- [Common mistake with `<Trail>` and `<CameraMotionBlur>`](/docs/motion-blur/common-mistake)\n\n<Credits\n  contributors={[\n    {\n      username: 'UmungoBungo',\n      contribution: 'Idea',\n    },\n    {\n      username: 'marcusstenbeck',\n      contribution: 'Implementation',\n    },\n  ]}\n/>\n"

[v3.2.39](https://github.com/remotion-dev/remotion/releases/v3.2.39)

The `<CameraMotionBlur>` produces natural looking motion blur similar to what would be produced by
a film camera.

For this technique to work, the children must be absolutely positioned so many layers can be created without influencing the layout.

You can use the [`<AbsoluteFill>`](/docs/absolute-fill) component to absolutely position content.
](/docs/absolute-fill)](/docs/absolute-fill)
](/docs/absolute-fill)
- ](/docs/absolute-fill)
- ](/docs/absolute-fill)
- ](/docs/absolute-fill)
- ](/docs/absolute-fill)
- ](/docs/absolute-fill)