---
title: "Command line"
url: "https://www.remotion.dev/docs/cli/"
path: "/docs/cli/"
---

"---\nimage: /generated/articles-docs-cli-cli.png\ntitle: Command line reference\nsidebar_label: CLI reference\nid: cli\n---\n\nimport {TableOfContents} from './table-of-contents';\n\n## How to use\n\nYou can run the CLI by installing `@remotion/cli` and running:\n\n- `npx remotion` inside a npm project\n- `yarn remotion` inside a Yarn project\n- `pnpm exec remotion` inside a pnpm project.\n- `bunx remotion` inside a Bun project\n\nFor brevity, in the documentation we always say `npx remotion`.\n\nInside an npm script, you don't need the `npx` prefix:\n\n```json title=\"package.json\"\n{\n  \"scripts\": {\n    \"render\": \"remotion render\"\n  }\n}\n```\n\n### Using Bun<AvailableFrom v=\"4.0.118\" />\n\nBy default, the `npx remotion` command is being executed using Node.  \nEven `bunx remotion` is using Node, unless you add the `--bun` flag.  \nTo use Bun, replace `remotion` with `remotionb`.\n\n```json title=\"package.json\"\n{\n  \"scripts\": {\n    \"render\": \"remotionb render\"\n  }\n}\n```\n\n### Using Deno<AvailableFrom v=\"4.0.227\" />\n\nDeno is not supported by Remotion.  \nIf you like to experiment nonetheless, use `npx remotiond` to run the Deno version of the CLI.\n\n```json title=\"package.json\"\n{\n  \"scripts\": {\n    \"render\": \"remotiond render\"\n  }\n}\n```\n\n## Commands\n\nThe following commands are available - you can always run them using `npx remotion` or even without the `npx` prefix if you put the command inside an npm script.\n\n<TableOfContents />\n\n## Example command\n\n```\nnpx remotion render --codec=vp8 HelloWorld out/video.webm\n```\n\n## See also\n\n- [Render your video](/docs/render)\n- [Configuration file](/docs/config)\n"

## How to use[​](#how-to-use)

You can run the CLI by installing `@remotion/cli` and running:

- `npx remotion` inside a npm project

- `yarn remotion` inside a Yarn project

- `pnpm exec remotion` inside a pnpm project.

- `bunx remotion` inside a Bun project

For brevity, in the documentation we always say `npx remotion`.

Inside an npm script, you don't need the `npx` prefix:

```

package.json{
  "scripts": {
    "render": "remotion render"
  }
}Copy
```

### Using Bun[v4.0.118](https://github.com/remotion-dev/remotion/releases/v4.0.118)[​](#using-bun)

By default, the `npx remotion` command is being executed using Node.

Even `bunx remotion` is using Node, unless you add the `--bun` flag.

To use Bun, replace `remotion` with `remotionb`.

```

package.json{
  "scripts": {
    "render": "remotionb render"
  }
}Copy
```

### Using Deno[v4.0.227](https://github.com/remotion-dev/remotion/releases/v4.0.227)[​](#using-deno)

Deno is not supported by Remotion.

If you like to experiment nonetheless, use `npx remotiond` to run the Deno version of the CLI.

```

package.json{
  "scripts": {
    "render": "remotiond render"
  }
}Copy
```

## Commands[​](#commands)

The following commands are available - you can always run them using `npx remotion` or even without the `npx` prefix if you put the command inside an npm script.

[
**studio**
Start the Remotion Studio](/docs/cli/studio)[
**render**
Render video or audio](/docs/cli/render)[
**still**
Render a still image](/docs/cli/still)[
**compositions**
List available compositions](/docs/cli/compositions)[
**lambda**
Control Remotion Lambda](/docs/lambda/cli)[
**bundle**
Create a Remotion Bundle](/docs/cli/bundle)[
**browser**
Ensure Remotion has a browser to use](/docs/cli/browser)[
**cloudrun**
Control Remotion Cloud Run](/docs/cloudrun/cli)[
**benchmark**
Measure and optimize render time](/docs/cli/benchmark)[
**skills**
Install or update skills](/docs/cli/skills)[
**versions**
List and validate Remotion package versions](/docs/cli/versions)[
**upgrade**
Upgrade to a newer version](/docs/cli/upgrade)[
**add**
Add Remotion packages with matching version](/docs/cli/add)[
**gpu**
Print information about Chrome's usage of the GPU](/docs/cli/gpu)[
**ffmpeg**
Execute an `ffmpeg` command](/docs/cli/ffmpeg)[
**ffprobe**
Execute an `ffprobe` command](/docs/cli/ffprobe)[
**help**
Show CLI commands](/docs/cli/help)

## Example command[​](#example-command)

```
npx remotion render --codec=vp8 HelloWorld out/video.webmCopy
```

## See also[​](#see-also)

- [Render your video](/docs/render)

- [Configuration file](/docs/config)
](/docs/config)](/docs/config)