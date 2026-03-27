---
title: "remotion"
url: "https://www.remotion.dev/docs/remotion"
path: "/docs/remotion"
---

"---\nimage: /generated/articles-docs-remotion.png\ntitle: 'remotion'\ncrumb: 'Core API Reference'\n---\n\nimport {TableOfContents} from './remotion/table-of-contents';\n\nA package containing the essential building blocks of expressing videos in Remotion.\n\nSome pure functions such as [`interpolate()`](/docs/interpolate) and [`interpolateColors()`](/docs/interpolate-colors) can also be used outside of Remotion.\n\n## Installation\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\n\n<Tabs\ndefaultValue=\"npm\"\nvalues={[\n{ label: 'npm', value: 'npm', },\n{ label: 'bun', value: 'bun', },\n{ label: 'pnpm', value: 'pnpm', },\n{ label: 'yarn', value: 'yarn', },\n]\n}>\n<TabItem value=\"npm\">\n\n```bash\nnpm i remotion\n```\n\n  </TabItem>\n<TabItem value=\"bun\">\n\n```bash\nbun i remotion\n```\n\n  </TabItem>\n\n  <TabItem value=\"pnpm\">\n\n```bash\npnpm i remotion\n```\n\n  </TabItem>\n\n  <TabItem value=\"yarn\">\n\n```bash\nyarn add remotion\n```\n\n  </TabItem>\n</Tabs>\n\n## API\n\nThe following functions and components are exposed:\n\n<TableOfContents />\n\n## License\n\n[Remotion License](https://remotion.dev/license)\n"

A package containing the essential building blocks of expressing videos in Remotion.

Some pure functions such as [`interpolate()`](/docs/interpolate) and [`interpolateColors()`](/docs/interpolate-colors) can also be used outside of Remotion.

## Installation[​](#installation)

- npm
- bun
- pnpm
- yarn

```
npm i remotionCopy
```

```
bun i remotionCopy
```

```
pnpm i remotionCopy
```

```
yarn add remotionCopy
```

## API[​](#api)

The following functions and components are exposed:

[
**<Composition>**
Define a video](/docs/composition)[
**<Still>**
Define a still](/docs/still)[
**<Folder>**
Organize compositions in the Studio sidebar](/docs/folder)[
**registerRoot()**
Initialize a Remotion project](/docs/register-root)[
**useCurrentFrame()**
Obtain the current time](/docs/use-current-frame)[
**useVideoConfig()**
Get the duration, dimensions and FPS of a composition](/docs/use-video-config)[
**interpolate()**
Map a range of values to another](/docs/interpolate)[
**spring()**
Physics-based animation primitive](/docs/spring)[
**interpolateColors()**
Map a range of values to colors](/docs/interpolate-colors)[
**measureSpring()**
Determine the duration of a spring](/docs/measure-spring)[
**Easing**
Customize animation curve of `interpolate()`](/docs/easing)[
**<Img>**
Render an `<img>` tag and wait for it to load](/docs/img)[
**<Html5Video>**
Synchronize a `<video>` with Remotion's time](/docs/html5-video)[
**<Html5Audio>**
Synchronize `<audio>` with Remotion's time](/docs/html5-audio)[
**<OffthreadVideo>**
Alternative to `<Html5Video>`](/docs/offthreadvideo)[
**<AnimatedImage>**
Disply a GIF, AVIF or animated WebP image](/docs/animatedimage)[
**<IFrame>**
Render an `<iframe>` tag and wait for it to load](/docs/iframe)[
**<Sequence>**
Time-shifts it's children](/docs/sequence)[
**<Series>**
Display contents after another](/docs/series)[
**<Freeze>**
Freeze some content in time](/docs/freeze)[
**<Loop>**
Play some content repeatedly](/docs/loop)[
**delayRender()**
Block a render from continuing](/docs/delay-render)[
**continueRender()**
Unblock a render](/docs/continue-render)[
**cancelRender()**
Abort an error](/docs/cancel-render) [
**getInputProps()**
Receive the user-defined input data](/docs/get-input-props)[
**getRemotionEnvironment()**
Determine if you are currently previewing or rendering](/docs/get-remotion-environment)[
**staticFile()**
Access file from `public/` folder](/docs/staticfile)[
**<AbsoluteFill>**
Position content absolutely and in full size](/docs/absolute-fill)[
**VERSION**
Get the current version of Remotion](/docs/version)

## License[​](#license)

[Remotion License](https://remotion.dev/license)](https://remotion.dev/license)](https://remotion.dev/license)
](https://remotion.dev/license)
- ](https://remotion.dev/license)
- ](https://remotion.dev/license)