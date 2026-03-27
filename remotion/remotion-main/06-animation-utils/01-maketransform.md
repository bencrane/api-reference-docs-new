---
title: "makeTransform()"
url: "https://www.remotion.dev/docs/animation-utils/make-transform"
path: "/docs/animation-utils/make-transform"
---

"---\nimage: /generated/articles-docs-animation-utils-make-transform.png\ntitle: makeTransform()\nid: make-transform\ncrumb: \"@remotion/animation-utils\"\n---\n\n_Part of the [`@remotion/animation-utils`](/docs/animation-utils) package._\n\nApplies a sequence of transformation functions to generate a combined CSS `transform` property.\n\n## API\n\nTakes an array of strings (generated from the below transformation functions) and combines them into a single string.\n\n## Usage\n\n```tsx twoslash\nimport { makeTransform, rotate, translate } from \"@remotion/animation-utils\";\n\nconst transform = makeTransform([rotate(45), translate(50, 50)]);\n// => \"rotate(45deg) translate(50px, 50px)\"\n\nconst markup = <div style={{ transform }} />;\n```\n\n```tsx twoslash\nimport { rotate } from \"@remotion/animation-utils\";\n\nconst transform = rotate(45);\n// => \"rotate(45deg)\"\n\nconst markup = <div style={{ transform }} />;\n```\n\n## Transformation Functions\n\n### matrix()\n\n```tsx twoslash\nimport { matrix } from \"@remotion/animation-utils\";\n\nconst transform = matrix(1, 0, 0, 1, 50, 50);\n// => \"matrix(1, 0, 0, 1, 50, 50)\"\n```\n\n### matrix3d()\n\n```tsx twoslash\nimport { matrix3d } from \"@remotion/animation-utils\";\n\nconst transform = matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 50, 50, 0, 1);\n// => \"matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 50, 50, 0, 1)\"\n```\n\n### perspective()\n\n```tsx twoslash\nimport { perspective } from \"@remotion/animation-utils\";\n\nconst transform = perspective(100);\n// => \"perspective(100px)\"\n```\n\n### rotate()\n\n```tsx twoslash\nimport { rotate } from \"@remotion/animation-utils\";\n\nconst transform = rotate(45);\n// => \"rotate(45deg)\"\n```\n\n### rotate3d()\n\n```tsx twoslash\nimport { rotate3d } from \"@remotion/animation-utils\";\n\nconst transform = rotate3d(1, 0, 0, 45);\n// => \"rotate3d(1, 0, 0, 45deg)\"\n\nconst transform2 = rotate3d(1, 0, 0, \"45deg\");\n// => \"rotate3d(1, 0, 0, 45deg)\"\n\nconst transform3 = rotate3d(1, 0, 0, 45, \"deg\");\n// => \"rotate3d(1, 0, 0, 45deg)\"\n```\n\n### rotateX()\n\n```tsx twoslash\nimport { rotateX } from \"@remotion/animation-utils\";\n\nconst transform = rotateX(45);\n// => \"rotateX(45deg)\"\n\nconst transform2 = rotateX(\"45deg\");\n// => \"rotateX(45deg)\"\n\nconst transform3 = rotateX(1, \"rad\");\n// => \"rotateX(45rad)\"\n```\n\n### rotateY()\n\n```tsx twoslash\nimport { rotateY } from \"@remotion/animation-utils\";\n\nconst transform = rotateY(45);\n// => \"rotateY(45deg)\"\n\nconst transform2 = rotateY(\"45deg\");\n// => \"rotateY(45deg)\"\n\nconst transform3 = rotateY(1, \"rad\");\n// => \"rotateY(1rad)\"\n```\n\n### rotateZ()\n\n```tsx twoslash\nimport { rotateZ } from \"@remotion/animation-utils\";\n\nconst transform = rotateZ(45);\n// => \"rotateZ(45deg)\"\n\nconst transform2 = rotateZ(\"45deg\");\n// => \"rotateZ(45deg)\"\n\nconst transform3 = rotateZ(1, \"rad\");\n// => \"rotateZ(1rad)\"\n```\n\n### scale()\n\n```tsx twoslash\nimport { scale } from \"@remotion/animation-utils\";\n\nconst transform = scale(2);\n// => \"scale(2, 2)\"\n\nconst transform2 = scale(2, 3);\n// => \"scale(2, 3)\"\n```\n\n### scale3d()\n\n```tsx twoslash\nimport { scale3d } from \"@remotion/animation-utils\";\n\nconst transform = scale3d(2, 3, 4);\n// => \"scale3d(2, 3, 4)\"\n```\n\n### scaleX()\n\n```tsx twoslash\nimport { scaleX } from \"@remotion/animation-utils\";\n\nconst transform = scaleX(2);\n// => \"scaleX(2)\"\n```\n\n### scaleY()\n\n```tsx twoslash\nimport { scaleY } from \"@remotion/animation-utils\";\n\nconst transform = scaleY(2);\n// => \"scaleY(2)\"\n```\n\n### scaleZ()\n\n```tsx twoslash\nimport { scaleZ } from \"@remotion/animation-utils\";\n\nconst transform = scaleZ(2);\n// => \"scaleZ(2)\"\n```\n\n### skew()\n\n```tsx twoslash\nimport { skew } from \"@remotion/animation-utils\";\n\nconst transform = skew(45);\n// => \"skew(45deg)\"\n```\n\n### skewX()\n\n```tsx twoslash\nimport { skewX } from \"@remotion/animation-utils\";\n\nconst transform = skewX(45);\n// => \"skewX(45deg)\"\n\nconst transform2 = skewX(\"45deg\");\n// => \"skewX(45deg)\"\n\nconst transform3 = skewX(1, \"rad\");\n// => \"skewX(1rad)\"\n```\n\n### skewY()\n\n```tsx twoslash\nimport { skewY } from \"@remotion/animation-utils\";\n\nconst transform = skewY(45);\n// => \"skewY(45deg)\"\n\nconst transform2 = skewY(\"45deg\");\n// => \"skewY(45deg)\"\n\nconst transform3 = skewY(1, \"rad\");\n// => \"skewY(1rad)\"\n```\n\n### translate()\n\n```tsx twoslash\nimport { translate } from \"@remotion/animation-utils\";\n\nconst transform = translate(10);\n// => \"translate(10px)\"\n\nconst transform2 = translate(\"12rem\");\n// => \"translate(12rem)\"\n\nconst transform3 = translate(10, 20);\n// => \"translate(10px, 20px)\"\n\nconst transform4 = translate(10, \"%\");\n// => \"translate(10%)\"\n\nconst transform5 = translate(0, \"%\", 10, \"%\");\n// => \"translate(0%, 10%)\"\n\nconst transform6 = translate(\"10px\", \"30%\");\n// => \"translate(10px, 20%)\"\n```\n\n### translate3d()\n\n```tsx twoslash\nimport { translate3d } from \"@remotion/animation-utils\";\n\nconst transform = translate3d(10, 20, 30);\n// => \"translate3d(10px, 20px, 30px)\"\n\nconst transform2 = translate3d(\"10px\", \"20%\", \"30rem\");\n// => \"translate3d(10px, 20%, 30rem)\"\n\nconst transform3 = translate3d(10, \"%\", 20, \"px\", 30, \"px\");\n// => \"translate3d(10%, 20px, 30px)\"\n```\n\n### translateX()\n\n```tsx twoslash\nimport { translateX } from \"@remotion/animation-utils\";\n\nconst transform = translateX(10);\n// => \"translateX(10px)\"\n\nconst transform2 = translateX(\"12rem\");\n// => \"translateX(12rem)\"\n\nconst transform3 = translateX(10, \"%\");\n// => \"translateX(10%)\"\n```\n\n### translateY()\n\n```tsx twoslash\nimport { translateY } from \"@remotion/animation-utils\";\n\nconst transform = translateY(10);\n// => \"translateY(10px)\"\n\nconst transform2 = translateY(\"12rem\");\n// => \"translateY(12rem)\"\n\nconst transform3 = translateY(10, \"px\");\n// => \"translateY(10px)\"\n```\n\n### translateZ()\n\n```tsx twoslash\nimport { translateZ } from \"@remotion/animation-utils\";\n\nconst transform = translateZ(10);\n// => \"translateZ(10px)\"\n\nconst transform2 = translateZ(\"12rem\");\n// => \"translateZ(12rem)\"\n\nconst transform3 = translateZ(10, \"px\");\n// => \"translateZ(10px)\"\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/animation-utils/src/transformation-helpers/make-transform/index.ts)\n- [`@remotion/animation-utils`](/docs/animation-utils)\n"

*Part of the [`@remotion/animation-utils`](/docs/animation-utils) package.*

Applies a sequence of transformation functions to generate a combined CSS `transform` property.

## API[​](#api)

Takes an array of strings (generated from the below transformation functions) and combines them into a single string.

## Usage[​](#usage)

```
import { makeTransform, rotate, translate } from "@remotion/animation-utils";

const transform = makeTransform([rotate(45), translate(50, 50)]);
// => "rotate(45deg) translate(50px, 50px)"

const markup = <div style={{ transform }} />;Copy
```

```
import { rotate } from "@remotion/animation-utils";

const transform = rotate(45);
// => "rotate(45deg)"

const markup = <div style={{ transform }} />;Copy
```

## Transformation Functions[​](#transformation-functions)

### matrix()[​](#matrix)

```
import { matrix } from "@remotion/animation-utils";

const transform = matrix(1, 0, 0, 1, 50, 50);
// => "matrix(1, 0, 0, 1, 50, 50)"Copy
```

### matrix3d()[​](#matrix3d)

```
import { matrix3d } from "@remotion/animation-utils";

const transform = matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 50, 50, 0, 1);
// => "matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 50, 50, 0, 1)"Copy
```

### perspective()[​](#perspective)

```
import { perspective } from "@remotion/animation-utils";

const transform = perspective(100);
// => "perspective(100px)"Copy
```

### rotate()[​](#rotate)

```
import { rotate } from "@remotion/animation-utils";

const transform = rotate(45);
// => "rotate(45deg)"Copy
```

### rotate3d()[​](#rotate3d)

```
import { rotate3d } from "@remotion/animation-utils";

const transform = rotate3d(1, 0, 0, 45);
// => "rotate3d(1, 0, 0, 45deg)"

const transform2 = rotate3d(1, 0, 0, "45deg");
// => "rotate3d(1, 0, 0, 45deg)"

const transform3 = rotate3d(1, 0, 0, 45, "deg");
// => "rotate3d(1, 0, 0, 45deg)"Copy
```

### rotateX()[​](#rotatex)

```
import { rotateX } from "@remotion/animation-utils";

const transform = rotateX(45);
// => "rotateX(45deg)"

const transform2 = rotateX("45deg");
// => "rotateX(45deg)"

const transform3 = rotateX(1, "rad");
// => "rotateX(45rad)"Copy
```

### rotateY()[​](#rotatey)

```
import { rotateY } from "@remotion/animation-utils";

const transform = rotateY(45);
// => "rotateY(45deg)"

const transform2 = rotateY("45deg");
// => "rotateY(45deg)"

const transform3 = rotateY(1, "rad");
// => "rotateY(1rad)"Copy
```

### rotateZ()[​](#rotatez)

```
import { rotateZ } from "@remotion/animation-utils";

const transform = rotateZ(45);
// => "rotateZ(45deg)"

const transform2 = rotateZ("45deg");
// => "rotateZ(45deg)"

const transform3 = rotateZ(1, "rad");
// => "rotateZ(1rad)"Copy
```

### scale()[​](#scale)

```
import { scale } from "@remotion/animation-utils";

const transform = scale(2);
// => "scale(2, 2)"

const transform2 = scale(2, 3);
// => "scale(2, 3)"Copy
```

### scale3d()[​](#scale3d)

```
import { scale3d } from "@remotion/animation-utils";

const transform = scale3d(2, 3, 4);
// => "scale3d(2, 3, 4)"Copy
```

### scaleX()[​](#scalex)

```
import { scaleX } from "@remotion/animation-utils";

const transform = scaleX(2);
// => "scaleX(2)"Copy
```

### scaleY()[​](#scaley)

```
import { scaleY } from "@remotion/animation-utils";

const transform = scaleY(2);
// => "scaleY(2)"Copy
```

### scaleZ()[​](#scalez)

```
import { scaleZ } from "@remotion/animation-utils";

const transform = scaleZ(2);
// => "scaleZ(2)"Copy
```

### skew()[​](#skew)

```
import { skew } from "@remotion/animation-utils";

const transform = skew(45);
// => "skew(45deg)"Copy
```

### skewX()[​](#skewx)

```
import { skewX } from "@remotion/animation-utils";

const transform = skewX(45);
// => "skewX(45deg)"

const transform2 = skewX("45deg");
// => "skewX(45deg)"

const transform3 = skewX(1, "rad");
// => "skewX(1rad)"Copy
```

### skewY()[​](#skewy)

```
import { skewY } from "@remotion/animation-utils";

const transform = skewY(45);
// => "skewY(45deg)"

const transform2 = skewY("45deg");
// => "skewY(45deg)"

const transform3 = skewY(1, "rad");
// => "skewY(1rad)"Copy
```

### translate()[​](#translate)

```
import { translate } from "@remotion/animation-utils";

const transform = translate(10);
// => "translate(10px)"

const transform2 = translate("12rem");
// => "translate(12rem)"

const transform3 = translate(10, 20);
// => "translate(10px, 20px)"

const transform4 = translate(10, "%");
// => "translate(10%)"

const transform5 = translate(0, "%", 10, "%");
// => "translate(0%, 10%)"

const transform6 = translate("10px", "30%");
// => "translate(10px, 20%)"Copy
```

### translate3d()[​](#translate3d)

```
import { translate3d } from "@remotion/animation-utils";

const transform = translate3d(10, 20, 30);
// => "translate3d(10px, 20px, 30px)"

const transform2 = translate3d("10px", "20%", "30rem");
// => "translate3d(10px, 20%, 30rem)"

const transform3 = translate3d(10, "%", 20, "px", 30, "px");
// => "translate3d(10%, 20px, 30px)"Copy
```

### translateX()[​](#translatex)

```
import { translateX } from "@remotion/animation-utils";

const transform = translateX(10);
// => "translateX(10px)"

const transform2 = translateX("12rem");
// => "translateX(12rem)"

const transform3 = translateX(10, "%");
// => "translateX(10%)"Copy
```

### translateY()[​](#translatey)

```
import { translateY } from "@remotion/animation-utils";

const transform = translateY(10);
// => "translateY(10px)"

const transform2 = translateY("12rem");
// => "translateY(12rem)"

const transform3 = translateY(10, "px");
// => "translateY(10px)"Copy
```

### translateZ()[​](#translatez)

```
import { translateZ } from "@remotion/animation-utils";

const transform = translateZ(10);
// => "translateZ(10px)"

const transform2 = translateZ("12rem");
// => "translateZ(12rem)"

const transform3 = translateZ(10, "px");
// => "translateZ(10px)"Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/animation-utils/src/transformation-helpers/make-transform/index.ts)

- [`@remotion/animation-utils`](/docs/animation-utils)
](/docs/animation-utils)](/docs/animation-utils)
](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)
- ](/docs/animation-utils)