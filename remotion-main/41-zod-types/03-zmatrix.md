---
title: "zMatrix()"
url: "https://www.remotion.dev/docs/zod-types/z-matrix"
path: "/docs/zod-types/z-matrix"
---

"---\nimage: /generated/articles-docs-zod-types-z-matrix.png\ntitle: zMatrix()\n---\n\nWith this type, you can visually edit a matrix in the [Props Editor](/docs/visual-editing).\n\nThe matrix has to be \"flat\", for example a 2x2 matrix has to be represented as an array of 4 numbers: `[0, 1, 1, 0]`.\n\nThe matrix has to be a square matrix, for example a 2x2, 3x3, 4x4, etc.\n\n```tsx\nconst myCompSchema = z.object({\n  matrix: zMatrix(),\n});\n\n// Two-dimensional matrix\nmyCompSchema.parse({\n  matrix: [0, 1, 1, 0],\n});\n\n// Three-dimensional matrix\nmyCompSchema.parse({\n  matrix: [1, 0, 0, 0, 1, 0, 0, 0, 1],\n});\n\n// Four-dimensional matrix\nmyCompSchema.parse({\n  matrix: [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],\n});\n```\n\n## See also\n\n- [Defining a schema for your props](/docs/schemas)\n"

With this type, you can visually edit a matrix in the [Props Editor](/docs/visual-editing).

The matrix has to be "flat", for example a 2x2 matrix has to be represented as an array of 4 numbers: `[0, 1, 1, 0]`.

The matrix has to be a square matrix, for example a 2x2, 3x3, 4x4, etc.

```
const myCompSchema = z.object({
  matrix: zMatrix(),
});

// Two-dimensional matrix
myCompSchema.parse({
  matrix: [0, 1, 1, 0],
});

// Three-dimensional matrix
myCompSchema.parse({
  matrix: [1, 0, 0, 0, 1, 0, 0, 0, 1],
});

// Four-dimensional matrix
myCompSchema.parse({
  matrix: [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
});Copy
```

## See also[​](#see-also)

- [Defining a schema for your props](/docs/schemas)
](/docs/schemas)](/docs/schemas)
](/docs/schemas)