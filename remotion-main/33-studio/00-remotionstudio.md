---
title: "@remotion/studio"
url: "https://www.remotion.dev/docs/studio/api"
path: "/docs/studio/api"
---

"---\nimage: /generated/articles-docs-studio-api.png\nsidebar_label: \"@remotion/studio\"\ntitle: \"@remotion/studio\"\n---\n\nimport { TableOfContents } from \"./TableOfContents\";\n\nYou can install this package from NPM:\n\n<Installation pkg=\"@remotion/studio\" />\n\n## APIs\n\nThe following APIs are available:\n\n<TableOfContents />\n"

You can install this package from NPM:

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/studioCopy
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

## APIs[​](#apis)

The following APIs are available:

[
**getStaticFiles()**
Get a list of files in the `public` folder](/docs/studio/get-static-files)[
**watchPublicFolder()**
Listen to changes in the public folder](/docs/studio/watch-public-folder)[
**watchStaticFile()**
Listen to changes of a static file](/docs/studio/watch-static-file)[
**writeStaticFile()**
Save content to a file in the public directory](/docs/studio/write-static-file)[
**saveDefaultProps()**
Save default props to the root file](/docs/studio/save-default-props)[
**updateDefaultProps()**
Update default props in the Props editor](/docs/studio/update-default-props)[
**deleteStaticFile()**
Delete a file from the public directory](/docs/studio/delete-static-file)[
**restartStudio()**
Restart the Studio Server.](/docs/studio/restart-studio)[
**play()**
Start playback in the timeline](/docs/studio/play)[
**pause()**
Pause playback in the timeline](/docs/studio/pause)[
**toggle()**
Toggle playback in the timeline](/docs/studio/toggle)[
**seek()**
Jump to a position in the timeline](/docs/studio/seek)[
**goToComposition()**
Select a composition in the composition selector](/docs/studio/go-to-composition)[
**focusDefaultPropsPath()**
Scrolls to a specific field in the default props editor](/docs/studio/focus-default-props-path)[
**reevaluateComposition()**
Re-runs calculateMetadata() on the current composition](/docs/studio/reevaluate-composition)[
**visualControl()**
Create a control in the right sidebar of the Studio](/docs/studio/visual-control)](/docs/studio/visual-control)](/docs/studio/visual-control)
](/docs/studio/visual-control)