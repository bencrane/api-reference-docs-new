---
title: "interpolateStyles()"
url: "https://www.remotion.dev/docs/animation-utils/interpolate-styles"
path: "/docs/animation-utils/interpolate-styles"
---

"---\nimage: /generated/articles-docs-animation-utils-interpolate-styles.png\ntitle: interpolateStyles()\nid: interpolate-styles\ncrumb: \"@remotion/animation-utils\"\n---\n\n_Part of the [`@remotion/animation-utils`](/docs/animation-utils) package._\n\nThis function provides a convenient way to interpolate styles based on a specified range of values, allowing for smooth animations between different styles.\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {\n  interpolateStyles,\n  makeTransform,\n  translateY,\n} from \"@remotion/animation-utils\";\n\nconst MyComponent: React.FC = () => {\n  const animatedStyles = interpolateStyles(\n    15,\n    [0, 30, 60],\n    [\n      { opacity: 0, transform: makeTransform([translateY(-50)]) },\n      { opacity: 1, transform: makeTransform([translateY(0)]) },\n      { opacity: 0, transform: makeTransform([translateY(50)]) },\n    ],\n  );\n\n  return <div style={animatedStyles} />;\n};\n```\n\n## API\n\nA function that takes 3-4 arguments:\n\n1. The input value.\n2. The range of values that you expect the input to assume.\n3. The range of output styles that you want the input to map to.\n4. Options object, same as the options of [`interpolate()`](/docs/interpolate#extrapolateleft). Optional.\n\n## Return value\n\n- A style object representing the interpolated styles based on the current frame.\n\n## Usage Notes\n\n- Ensure that the `inputRange` and `outputStylesRange` arrays contain at least two values to facilitate interpolation between styles.\n\n- The `outputStylesRange` array must have the same number of elements as `inputRange`. Each style in `outputStylesRange` corresponds to a specific value in the input range.\n\n## See also\n\n- [Source code for this hook](https://github.com/remotion-dev/remotion/blob/main/packages/animation-utils/src/transformation-helpers/interpolate-styles/index.tsx)\n- [`@remotion/animation-utils`](/docs/animation-utils)\n"

*Part of the [`@remotion/animation-utils`](/docs/animation-utils) package.*

This function provides a convenient way to interpolate styles based on a specified range of values, allowing for smooth animations between different styles.

## Example[​](#example)

```
import {
  interpolateStyles,
  makeTransform,
  translateY,
} from "@remotion/animation-utils";

const MyComponent: React.FC = () => {
  const animatedStyles = interpolateStyles(
    15,
    [0, 30, 60],
    [
      { opacity: 0, transform: makeTransform([translateY(-50)]) },
      { opacity: 1, transform: makeTransform([translateY(0)]) },
      { opacity: 0, transform: makeTransform([translateY(50)]) },
    ],
  );

  return <div style={animatedStyles} />;
};Copy
```

## API[​](#api)

A function that takes 3-4 arguments:

- The input value.

- The range of values that you expect the input to assume.

- The range of output styles that you want the input to map to.

- Options object, same as the options of [`interpolate()`](/docs/interpolate#extrapolateleft). Optional.

## Return value[​](#return-value)

- A style object representing the interpolated styles based on the current frame.

## Usage Notes[​](#usage-notes)

- 

Ensure that the `inputRange` and `outputStylesRange` arrays contain at least two values to facilitate interpolation between styles.

- 

The `outputStylesRange` array must have the same number of elements as `inputRange`. Each style in `outputStylesRange` corresponds to a specific value in the input range.

## See also[​](#see-also)

- [Source code for this hook](https://github.com/remotion-dev/remotion/blob/main/packages/animation-utils/src/transformation-helpers/interpolate-styles/index.tsx)

- [`@remotion/animation-utils`](/docs/animation-utils)
](/docs/animation-utils)](/docs/animation-utils)
](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)