---
title: "@remotion/player"
url: "https://www.remotion.dev/docs/player/installation"
path: "/docs/player/installation"
---

"---\nimage: /generated/articles-docs-player-installation.png\nid: installation\ntitle: Installation\nslug: /player/installation\ncrumb: '@remotion/player'\n---\n\nimport {PlayerTableOfContents, PlayerGuide} from './TableOfContents';\n\nTo install the Player, run the following command in a React project:\n\n<Installation pkg=\"@remotion/player\" />\n\n## Components\n\n<PlayerTableOfContents />\n\n## Guide\n\n<PlayerGuide />\n"

To install the Player, run the following command in a React project:

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/playerCopy
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

## Components[​](#components)

[
**<Player>**
Embed a Remotion composition in a web app](/docs/player/player)[
**<Thumbnail>**
Embed a still in a web app](/docs/player/thumbnail)

## Guide[​](#guide)

[
**Installation**
Install the Player into your project](/docs/player/installation)[
**Examples**
Code samples for various scenarios](/docs/player/examples)[
**Sizing**
Setting the size of the Player](/docs/player/scaling)[
**Autoplay**
Dealing with browser autoplay policies](/docs/player/autoplay)[
**Display time**
Write a custom component for displaying the current time](/docs/player/current-time)[
**Preloading assets**
Make assets ready to play when they appear in the video](/docs/player/preloading)[
**Best practices**
Checklist of correct implementation](/docs/player/best-practices)[
**Buffer state**
Pause the Player while assets are loading](/docs/player/buffer-state)[
**Avoiding flickers**
Troubleshooting for flickers due to unloaded assets](/docs/troubleshooting/player-flicker)[
**Premounting**
Mount components earlier to allow them to load](/docs/player/premounting)[
**Drag & Drop**
Allow interactivity on the canvas](/docs/player/drag-and-drop)[
**Custom controls**
Recipes for custom Play buttons, volume sliders, etc.](/docs/player/custom-controls)[
**Media Keys**
Control what happens when users presses ⏯️](/docs/player/media-keys)](/docs/player/media-keys)](/docs/player/media-keys)
](/docs/player/media-keys)
- ](/docs/player/media-keys)