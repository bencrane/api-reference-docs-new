---
title: "extendViewBox()"
url: "https://www.remotion.dev/docs/paths/extend-viewbox"
path: "/docs/paths/extend-viewbox"
---

"---\nimage: /generated/articles-docs-paths-extend-viewbox.png\ntitle: extendViewBox()\ncrumb: \"@remotion/paths\"\n---\n\n_Part of the [`@remotion/paths`](/docs/paths) package. Available since v3.2.25_\n\nWidens an SVG `viewBox` in all directions by a certain scale factor.\n\n:::note\nThis function may be unnecessary: If you want the parts that go outside of the viewbox to be visible, you can also set `style={{overflow: 'visible'}}` on the SVG container.\n:::\n\n```tsx twoslash\nimport { extendViewBox } from \"@remotion/paths\";\n\nconst extended = extendViewBox(\"0 0 1000 1000\", 2);\nconsole.log(extended); // \"-500 -500 2000 2000\"\n```\n\nThe function will throw if the viewBox is invalid.\n\n## Example: Displaying an SVG path that goes out of bounds\n\nConsider the following SVG:\n\nThe path will go from `0` to `1500` on the horizontal axis, but it will be cut off because it goes beyond the viewport area.\n\n```tsx twoslash\nconst viewBox = \"0 0 1000 1000\";\n\nexport const ViewBoxExample: React.FC = () => {\n  return (\n    <svg viewBox={viewBox}>\n      <path d={\"0 500 1500 500\"} stroke=\"black\" strokeWidth={4} />\n    </svg>\n  );\n};\n```\n\nWe can fix the cutoff by doing two things:\n\n- Scaling the viewBox by a factor of 2\n- Applying a 2x scale transform to the SVG.\n\n```tsx twoslash\nimport { extendViewBox } from \"@remotion/paths\";\n\nconst viewBox = \"0 0 1000 1000\";\n\nexport const ViewBoxExample: React.FC = () => {\n  return (\n    <svg style={{ scale: \"2\" }} viewBox={extendViewBox(viewBox, 2)}>\n      <path d={\"0 500 1500 500\"} stroke=\"black\" strokeWidth={4} />\n    </svg>\n  );\n};\n```\n\nBy doing that, the each dimensions of the viewBox will be doubled, which will result in the picture being scaled down. By applying a scale transform, this can be corrected.\n\nIn this example, a factor of `2` was chosen because it is enough to fix the cutoff problem. The more the SVG path goes outside the container, the higher the factor needs to be to compensate.\n\n## See also\n\n- [`@remotion/paths`](/docs/paths)\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/paths/src/extend-viewbox.ts)\n"

*Part of the [`@remotion/paths`](/docs/paths) package. Available since v3.2.25*

Widens an SVG `viewBox` in all directions by a certain scale factor.
](/docs/paths)](/docs/paths)
](/docs/paths)
- ](/docs/paths)