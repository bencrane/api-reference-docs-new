---
title: "@remotion/paths"
url: "https://www.remotion.dev/docs/paths/"
path: "/docs/paths/"
---

"---\nimage: /generated/articles-docs-paths-index.png\ntitle: \"@remotion/paths\"\ncrumb: \"SVG\"\n---\n\nimport {TableOfContents} from './table-of-contents';\n\nA package providing utility functions for dealing with SVG paths. This package includes code from [`svg-path-properties`](https://www.npmjs.com/package/svg-path-properties), [`svg-path-reverse`](https://github.com/Pomax/svg-path-reverse#readme), [`svgpath`](https://github.com/fontello/svgpath), [`svg-path-bbox`](https://github.com/mondeja/svg-path-bbox), [`translate-svg-path`](https://github.com/michaelrhodes/translate-svg-path) and [`d3-interpolate-path`](https://github.com/pbeshai/d3-interpolate-path) with the following improvements:\n\n- Functional style APIs\n- First class Typescript types\n- Documentation with examples\n- ESM import style\n\nThis package has no dependencies, meaning this package can be used without Remotion.\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\n\n<Tabs\ndefaultValue=\"npm\"\nvalues={[\n{ label: 'npm', value: 'npm', },\n{ label: 'pnpm', value: 'pnpm', },\n{ label: 'yarn', value: 'yarn', },\n]\n}>\n<TabItem value=\"npm\">\n\n```bash\nnpm i @remotion/paths\n```\n\n  </TabItem>\n\n  <TabItem value=\"pnpm\">\n\n```bash\npnpm i @remotion/paths\n```\n\n  </TabItem>\n\n  <TabItem value=\"yarn\">\n\n```bash\nyarn add @remotion/paths\n```\n\n  </TabItem>\n</Tabs>\n\n## Functions\n\n<TableOfContents />\n\n## License\n\nMIT\n"

A package providing utility functions for dealing with SVG paths. This package includes code from [`svg-path-properties`](https://www.npmjs.com/package/svg-path-properties), [`svg-path-reverse`](https://github.com/Pomax/svg-path-reverse#readme), [`svgpath`](https://github.com/fontello/svgpath), [`svg-path-bbox`](https://github.com/mondeja/svg-path-bbox), [`translate-svg-path`](https://github.com/michaelrhodes/translate-svg-path) and [`d3-interpolate-path`](https://github.com/pbeshai/d3-interpolate-path) with the following improvements:

- Functional style APIs

- First class Typescript types

- Documentation with examples

- ESM import style

This package has no dependencies, meaning this package can be used without Remotion.

- npm
- pnpm
- yarn

```
npm i @remotion/pathsCopy
```

```
pnpm i @remotion/pathsCopy
```

```
yarn add @remotion/pathsCopy
```

## Functions[​](#functions)

[
**getLength()**
Obtain length of an SVG path](/docs/paths/get-length)[
**cutPath()**
Cut an SVG path at a specified length](/docs/paths/cut-path)[
**getPointAtLength()**
Get coordinates at a certain point of an SVG path](/docs/paths/get-point-at-length)[
**getTangentAtLength()**
Gets tangents `x` and `y` of a point which is on an SVG path](/docs/paths/get-tangent-at-length)[
**reversePath()**
Switch direction of an SVG path](/docs/paths/reverse-path)[
**normalizePath()**
Replace relative with absolute coordinates](/docs/paths/normalize-path)[
**interpolatePath()**
Interpolates between two SVG paths](/docs/paths/interpolate-path)[
**evolvePath()**
Animate an SVG path](/docs/paths/evolve-path)[
**translatePath()**
Translates the position of an path against X/Y coordinates](/docs/paths/translate-path)[
**warpPath()**
Remap the coordinates of a path](/docs/paths/warp-path)[
**scalePath()**
Grow or shrink the size of the path](/docs/paths/scale-path)[
**getBoundingBox()**
Get the bounding box of a SVG path](/docs/paths/get-bounding-box)[
**resetPath()**
Translates an SVG path to `(0, 0)`](/docs/paths/reset-path)[
**extendViewBox()**
Widen an SVG viewBox in all directions](/docs/paths/extend-viewbox)[
**getSubpaths()**
Split SVG path into its parts](/docs/paths/get-subpaths)[
**parsePath()**
Parse a string into an array of instructions](/docs/paths/parse-path)[
**serializeInstructions()**
Turn an array of instructions into a SVG path](/docs/paths/serialize-instructions) [
**reduceInstructions()**
Reduce the amount of instruction types](/docs/paths/reduce-instructions) 

## License[​](#license)

MIT](#license)](#license)
](#license)
- ](#license)