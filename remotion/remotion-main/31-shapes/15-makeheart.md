---
title: "makeHeart()"
url: "https://www.remotion.dev/docs/shapes/make-heart"
path: "/docs/shapes/make-heart"
---

"---\nimage: /generated/articles-docs-shapes-make-heart.png\ntitle: makeHeart()\ncrumb: '@remotion/shapes'\n---\n\nimport {MakeShapeSeeAlso, ShapeOptions} from '../../components/shapes/shapes-info';\n\n_available from v4.0.315_\n\nGenerates an SVG path for a heart.\n\n## Example\n\n```ts twoslash title=\"make-heart.ts\"\nimport {makeHeart} from '@remotion/shapes';\n\nconst {path, width, height, transformOrigin, instructions} = makeHeart({\n  height: 100,\n});\n\nconsole.log(path); // M 100 120 C 40 110 20 70 60 60 C 90 40 110 40 140 60 C 180 70 160 110 100 120 Z\nconsole.log(width); // 200\nconsole.log(height); // 160\nconsole.log(transformOrigin); // \"100 80\"\nconsole.log(instructions); // Instruction[]\n```\n\n## Arguments\n\n<ShapeOptions shape=\"heart\" />\n\n## Return type\n\nThe function returns an object with the following properties:\n\n- `path`: The SVG path string\n- `width`: The width of the heart\n- `height`: The height of the heart\n- `transformOrigin`: The transform origin of the heart\n- `instructions`: An array of path instructions\n\n## See also\n\n<MakeShapeSeeAlso shape=\"heart\" />\n"

*available from v4.0.315*

Generates an SVG path for a heart.

## Example[​](#example)

```

make-heart.tsimport {makeHeart} from '@remotion/shapes';

const {path, width, height, transformOrigin, instructions} = makeHeart({
  height: 100,
});

console.log(path); // M 100 120 C 40 110 20 70 60 60 C 90 40 110 40 140 60 C 180 70 160 110 100 120 Z
console.log(width); // 200
console.log(height); // 160
console.log(transformOrigin); // "100 80"
console.log(instructions); // Instruction[]Copy
```

## Arguments[​](#arguments)

### `height`

*number*

The height of the heart.

### `aspectRatio`

*number*

The aspect ratio of the heart. Default 1.1.

### `bottomRoundnessAdjustment`

*number*

The amount of bottom roundness deviation from the default. Negative values make the bottom point sharper, positive values make it rounder.

### `depthAdjustment`

*number*

The deviation of the default depth (how deep the top of the heart is). Negative values make the heart deeper, positive values make it shallower.

## Return type[​](#return-type)

The function returns an object with the following properties:

- `path`: The SVG path string

- `width`: The width of the heart

- `height`: The height of the heart

- `transformOrigin`: The transform origin of the heart

- `instructions`: An array of path instructions

## See also[​](#see-also)

- [<Heart />](/docs/shapes/heart)
- [`@remotion/shapes`](/docs/shapes)
- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/shapes/src/utils/make-heart.ts)