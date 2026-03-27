---
title: "gpu"
url: "https://www.remotion.dev/docs/cli/gpu"
path: "/docs/cli/gpu"
---

"---\nimage: /generated/articles-docs-cli-gpu.png\ncrumb: CLI Reference\nsidebar_label: gpu\ntitle: npx remotion gpu\n---\n\n<AvailableFrom v=\"4.0.52\" />\n\nPrints out how the Chrome browser uses the GPUs.\n\n```bash\nnpx remotion gpu --gl=angle\n```\n\nThe command takes the same arguments for `--gl` as `npx remotion render` and also picks up the [`Config.setChromiumOpenGlRenderer()`](/docs/config#setchromiumopenglrenderer) option.  \nTry out different values to find which one is the best for your system.\n\n```bash title=\"Example output\"\nCanvas: Hardware accelerated\nCanvas out-of-process rasterization: Enabled\nDirect Rendering Display Compositor: Disabled\nCompositing: Hardware accelerated\nMultiple Raster Threads: Enabled\nOpenGL: Enabled\nRasterization: Hardware accelerated\nRaw Draw: Disabled\nSkia Graphite: Disabled\nVideo Decode: Hardware accelerated\nVideo Encode: Hardware accelerated\nWebGL: Hardware accelerated\nWebGL2: Hardware accelerated\nWebGPU: Hardware accelerated\n```\n\nThe output should not be used for automated parsing, as it may change inbetween any Remotion and Chrome versions.\n\n## API\n\n### `--log`\n\n<Options id=\"log\" />\n\n### `--gl`\n\n<Options id=\"gl\" />\n\n### `--chrome-mode`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cli/src/gpu.ts)\n- [Using the GPU](/docs/gpu)\n"
[v4.0.52](https://github.com/remotion-dev/remotion/releases/v4.0.52)

Prints out how the Chrome browser uses the GPUs.

```
npx remotion gpu --gl=angleCopy
```

The command takes the same arguments for `--gl` as `npx remotion render` and also picks up the [`Config.setChromiumOpenGlRenderer()`](/docs/config#setchromiumopenglrenderer) option.

Try out different values to find which one is the best for your system.

```

Example outputCanvas: Hardware accelerated
Canvas out-of-process rasterization: Enabled
Direct Rendering Display Compositor: Disabled
Compositing: Hardware accelerated
Multiple Raster Threads: Enabled
OpenGL: Enabled
Rasterization: Hardware accelerated
Raw Draw: Disabled
Skia Graphite: Disabled
Video Decode: Hardware accelerated
Video Encode: Hardware accelerated
WebGL: Hardware accelerated
WebGL2: Hardware accelerated
WebGPU: Hardware acceleratedCopy
```

The output should not be used for automated parsing, as it may change inbetween any Remotion and Chrome versions.

## API[​](#api)

### `--log`[​](#--log)

One of `trace`, `verbose`, `info`, `warn`, `error`.
 Determines how much info is being logged to the console.

 Default `info`.

### `--gl`[​](#--gl)

Changelog
- From Remotion v2.6.7 until v3.0.7, the default for Remotion Lambda was `swiftshader`, but from v3.0.8 the default is `swangle` (Swiftshader on Angle) since Chrome 101 added support for it.
- From Remotion v2.4.3 until v2.6.6, the default was `angle`, however it turns out to have a small memory leak that could crash long Remotion renders.

Select the OpenGL renderer backend for Chromium. 
Accepted values:
- `"angle"`
- `"egl"`
- `"swiftshader"`
- `"swangle"`
- `"vulkan"` (*from Remotion v4.0.41*)
- `"angle-egl"` (*from Remotion v4.0.51*)

The default is `null`, letting Chrome decide, except on Lambda where the default is `"swangle"`

### `--chrome-mode`[v4.0.248](https://github.com/remotion-dev/remotion/releases/v4.0.248)[​](#--chrome-mode)

One of `headless-shell, ``chrome-for-testing`. Default `headless-shell`. [Use `chrome-for-testing` to take advantage of GPU drivers on Linux.](https://remotion.dev/docs/miscellaneous/chrome-headless-shell)

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cli/src/gpu.ts)

- [Using the GPU](/docs/gpu)
](/docs/gpu)](/docs/gpu)
](/docs/gpu)
- ](/docs/gpu)
- ](/docs/gpu)
- ](/docs/gpu)
- ](/docs/gpu)