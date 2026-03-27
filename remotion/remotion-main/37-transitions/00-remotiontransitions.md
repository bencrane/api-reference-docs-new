---
title: "@remotion/transitions"
url: "https://www.remotion.dev/docs/transitions/"
path: "/docs/transitions/"
---

"---\nimage: /generated/articles-docs-transitions-index.png\nsidebar_label: Overview\ntitle: '@remotion/transitions'\n---\n\n_available from v4.0.53_\n\nimport Tabs from '@theme/Tabs';\nimport TabItem from '@theme/TabItem';\nimport {TableOfContents} from './table-of-contents';\n\nThis package provides the [`<TransitionSeries>`](/docs/transitions/transitionseries) component for transitioning between two scenes as well as timing presets.\n\n## Installation\n\n<Installation pkg=\"@remotion/transitions\" />\n\n## API\n\n<TableOfContents />\n\n## License\n\n[Remotion License](https://remotion.dev/license)\n\n## See also\n\n- [Transitions](/docs/transitioning)\n"

*available from v4.0.53*

This package provides the [`<TransitionSeries>`](/docs/transitions/transitionseries) component for transitioning between two scenes as well as timing presets.

## Installation[​](#installation)

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/transitionsCopy
```

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

## API[​](#api)

### Components

[
**`<TransitionSeries>`**
A `<Series>` with transitions inbetween](/docs/transitions/transitionseries)

### Timings

[
**`springTiming()`**
Transition with a `spring()`](/docs/transitions/timings/springtiming)[
**`linearTiming()`**
Transition linearly with optional Easing](/docs/transitions/timings/lineartiming)[
**Custom timings**
Implement your own timing](/docs/transitions/timings/custom)

### Presentations

Hover over an effect to see the preview.
[
**Overview**
List of available presentations](/docs/transitions/presentations)[
**Custom presentations**
Implement your own effect](/docs/transitions/presentations/custom)[

**`fade()`**
Animate the opacity of the scenes](/docs/transitions/presentations/fade)[

**`slide()`**
Slide in and push out the previous scene](/docs/transitions/presentations/slide)[

**`wipe()`**
Slide over the previous scene](/docs/transitions/presentations/wipe)[

**`flip()`**
Rotate the previous scene](/docs/transitions/presentations/flip)[

**`clockWipe()`**
Reveal the new scene in a circular movement](/docs/transitions/presentations/clock-wipe)[

**`iris()`**
Reveal the scene through a circular mask from center](/docs/transitions/presentations/iris)[

**`cube()`**
Paid
Rotate both scenes with 3D perspective](/docs/transitions/presentations/cube)[

**`none()`**
Have no visual effect.](/docs/transitions/presentations/none)[

**Audio transitions**
Add a sound effect to a transition](/docs/transitions/audio-transitions)

## License[​](#license)

[Remotion License](https://remotion.dev/license)

## See also[​](#see-also)

- [Transitions](/docs/transitioning)
](/docs/transitioning)](/docs/transitioning)
](/docs/transitioning)
- ](/docs/transitioning)
- ](/docs/transitioning)
- ](/docs/transitioning)