---
title: "Common mistake"
url: "https://www.remotion.dev/docs/motion-blur/common-mistake"
path: "/docs/motion-blur/common-mistake"
---

"---\nimage: /generated/articles-docs-motion-blur-common-mistake.png\ntitle: Common mistake with <MotionBlur> and <Trail>\nsidebar_label: Common mistake\n---\n\nThe [`<Trail>`](/docs/motion-blur/trail) and [`<CameraMotionBlur>`](/docs/motion-blur/camera-motion-blur) components manipulate the React context that holds the current time.  \nThis means that the motion blur effect doesn't work if you use the [`useCurrentFrame()`](/docs/use-current-frame) hook outside of a motion blur component.\n\n```tsx twoslash title=\"❌ Wrong - useCurrentFrame() outside of CameraMotionBlur\"\nimport {AbsoluteFill, useCurrentFrame} from 'remotion';\nimport {CameraMotionBlur} from '@remotion/motion-blur';\n\nexport const MyComp = () => {\n  const frame = useCurrentFrame();\n\n  return (\n    <AbsoluteFill>\n      <CameraMotionBlur>\n        <AbsoluteFill\n          style={{\n            backgroundColor: 'red',\n            justifyContent: 'center',\n            alignItems: 'center',\n            color: 'white',\n            fontSize: frame,\n          }}\n        >\n          A\n        </AbsoluteFill>\n      </CameraMotionBlur>\n    </AbsoluteFill>\n  );\n};\n```\n\nYou can fix this by extracting the animation into a separate component:\n\n```tsx twoslash title=\"✅ Correct - useCurrentFrame() inside the child component\"\nimport {AbsoluteFill, useCurrentFrame} from 'remotion';\nimport {CameraMotionBlur} from '@remotion/motion-blur';\n\nconst A: React.FC = () => {\n  const frame = useCurrentFrame();\n\n  return (\n    <AbsoluteFill\n      style={{\n        backgroundColor: 'red',\n        justifyContent: 'center',\n        alignItems: 'center',\n        color: 'white',\n        fontSize: frame,\n      }}\n    >\n      A\n    </AbsoluteFill>\n  );\n};\n\nexport const MyComp = () => {\n  return (\n    <AbsoluteFill>\n      <CameraMotionBlur>\n        <A />\n      </CameraMotionBlur>\n    </AbsoluteFill>\n  );\n};\n```\n\n## See also\n\n- [`<Trail>`](/docs/motion-blur/trail)\n- [`<CameraMotionBlur>`](/docs/motion-blur/camera-motion-blur)\n"

The [`<Trail>`](/docs/motion-blur/trail) and [`<CameraMotionBlur>`](/docs/motion-blur/camera-motion-blur) components manipulate the React context that holds the current time.

This means that the motion blur effect doesn't work if you use the [`useCurrentFrame()`](/docs/use-current-frame) hook outside of a motion blur component.

```

❌ Wrong - useCurrentFrame() outside of CameraMotionBlurimport {AbsoluteFill, useCurrentFrame} from 'remotion';
import {CameraMotionBlur} from '@remotion/motion-blur';

export const MyComp = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill>
      <CameraMotionBlur>
        <AbsoluteFill
          style={{
            backgroundColor: 'red',
            justifyContent: 'center',
            alignItems: 'center',
            color: 'white',
            fontSize: frame,
          }}
        >
          A
        </AbsoluteFill>
      </CameraMotionBlur>
    </AbsoluteFill>
  );
};Copy
```

You can fix this by extracting the animation into a separate component:

```

✅ Correct - useCurrentFrame() inside the child componentimport {AbsoluteFill, useCurrentFrame} from 'remotion';
import {CameraMotionBlur} from '@remotion/motion-blur';

const A: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: 'red',
        justifyContent: 'center',
        alignItems: 'center',
        color: 'white',
        fontSize: frame,
      }}
    >
      A
    </AbsoluteFill>
  );
};

export const MyComp = () => {
  return (
    <AbsoluteFill>
      <CameraMotionBlur>
        <A />
      </CameraMotionBlur>
    </AbsoluteFill>
  );
};Copy
```

## See also[​](#see-also)

- [`<Trail>`](/docs/motion-blur/trail)

- [`<CameraMotionBlur>`](/docs/motion-blur/camera-motion-blur)
](/docs/motion-blur/camera-motion-blur)](/docs/motion-blur/camera-motion-blur)
](/docs/motion-blur/camera-motion-blur)