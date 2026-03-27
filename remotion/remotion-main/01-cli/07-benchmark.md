---
title: "benchmark"
url: "https://www.remotion.dev/docs/cli/benchmark"
path: "/docs/cli/benchmark"
---

"---\nimage: /generated/articles-docs-cli-benchmark.png\ntitle: npx remotion benchmark\nsidebar_label: benchmark\ncrumb: CLI Reference\n---\n\n<AvailableFrom v=\"3.2.28\" />\n\nMeasures render time by running a render multiple times, if desired with multiple compositions and concurrency values to compare against each other.\n\n```bash\nnpx remotion benchmark src/index.ts [composition-ids]\n```\n\nYou can provide multiple composition IDs separated by comma, ex: `npx remotion benchmark src/index.ts --codec=h264 Main,Canvas,CSS`\n\nIf `composition-ids` is not passed, Remotion will let you select compositions from a list.\n\n## Flags\n\n### `--runs`\n\n<Options id=\"runs\" />\n\n### `--concurrencies`\n\n<Options id=\"concurrencies\" />\n\n### `--codec`\n\nInherited from [`npx remotion render`](/docs/cli/render#--codec)\n\n### `--audio-codec`<AvailableFrom v=\"3.3.42\" />\n\n<Options id=\"audio-codec\" />\n\n### `--crf`\n\nInherited from [`npx remotion render`](/docs/cli/render#--crf)\n\n### `--frames`\n\nInherited from [`npx remotion render`](/docs/cli/render#--frames)\n\n### `--image-format`\n\nInherited from [`npx remotion render`](/docs/cli/render#--image-format)\n\n### `--pixel-format`\n\nInherited from [`npx remotion render`](/docs/cli/render#--pixel-format)\n\n### `--props`\n\nInherited from [`npx remotion render`](/docs/cli/render#--props)\n\n### `--prores-profile`\n\nInherited from [`npx remotion render`](/docs/cli/render#--prores-profile)\n\n### `--jpeg-quality`<AvailableFrom v=\"4.0.0\" />\n\nInherited from [`npx remotion render`](/docs/cli/render#--jpeg-quality)\n\n### ~~`--quality`~~\n\nRemoved in v4.0.0. Renamed to `--jpeg-quality`.\n\n### `--log`\n\nInherited from [`npx remotion render`](/docs/cli/render#--log)\n\n### `--ignore-certificate-errors`\n\nInherited from [`npx remotion render`](/docs/cli/render#--ignore-certificate-errors)\n\n### `--disable-web-security`\n\nInherited from [`npx remotion render`](/docs/cli/render#--disable-web-security)\n\n### `--dark-mode`<AvailableFrom v=\"4.0.381\"/>\n\n<Options id=\"dark-mode\" />\n\n### ~`--disable-headless`~\n\n<Options id=\"disable-headless\" />\n\n### `--enable-multiprocess-on-linux`<AvailableFrom v=\"4.0.42\"/>\n\n<Options cli id=\"enable-multiprocess-on-linux\" />\n\n### `--gl`\n\n<Options id=\"gl\" cli />\n\n### `--chrome-mode`<AvailableFrom v=\"4.0.248\" />\n\n<Options id=\"chrome-mode\" />\n\n### `--timeout`\n\nInherited from [`npx remotion render`](/docs/cli/render#--timeout)\n\n### `--scale`\n\nInherited from [`npx remotion render`](/docs/cli/render#--scale)\n\n### `--port`\n\nInherited from [`npx remotion render`](/docs/cli/render#--port)\n\n### `--number-of-gif-loops`\n\n<Options id=\"number-of-gif-loops\" />\n\n### `--every-nth-frame`\n\nInherited from [`npx remotion render`](/docs/cli/render#--every-nth-frame)\n\n### `--log`\n\nInherited from [`npx remotion render`](/docs/cli/render#--log)\n\n### `--muted`\n\nInherited from [`npx remotion render`](/docs/cli/render#--muted)\n\n### `--enforce-audio-track`\n\nInherited from [`npx remotion render`](/docs/cli/render#--enforce-audio-track)\n\n### `--disallow-parallel-encoding`<AvailableFrom v=\"4.0.315\" />\n\nInherited from [`npx remotion render`](/docs/cli/render#--disallow-parallel-encoding)\n\n### `--browser-executable`\n\nInherited from [`npx remotion render`](/docs/cli/render#--browser-executable)\n\n### `--public-dir`\n\nInherited from [`npx remotion render`](/docs/cli/render#--public-dir)\n\n### `--config`\n\nInherited from [`npx remotion render`](/docs/cli/render#--config)\n\n### `--bundle-cache`\n\nInherited from [`npx remotion render`](/docs/cli/render#--bundle-cache)\n\n### `--video-bitrate`\n\nInherited from [`npx remotion render`](/docs/cli/render#--video-bitrate)\n\n### `--audio-bitrate`\n\nInherited from [`npx remotion render`](/docs/cli/render#--audio-bitrate)\n\n### `--color-space`<AvailableFrom v=\"4.0.28\"/>\n\n<Options cli id=\"color-space\" />\n\n### `--hardware-acceleration`<AvailableFrom v=\"4.0.228\" />\n\n<Options cli id=\"hardware-acceleration\" />\n\n### `--offthreadvideo-cache-size-in-bytes`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `--media-cache-size-in-bytes`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `--binaries-directory`<AvailableFrom v=\"4.0.120\" />\n\n<Options cli id=\"binaries-directory\" />\n\n### `--experimental-rspack`<AvailableFrom v=\"4.0.426\" />\n\n<Options id=\"experimental-rspack\" />\n\n### ~~`--ffmpeg-executable`~~\n\nRemoved in v4.0. Inherited from [`npx remotion render`](/docs/cli/render#--ffmpeg-executable)\n\n### ~~`--ffprobe-executable`~~\n\nRemoved in v4.0. Inherited from [`npx remotion render`](/docs/cli/render#--ffprobe-executable-)\n"
[v3.2.28](https://github.com/remotion-dev/remotion/releases/v3.2.28)

Measures render time by running a render multiple times, if desired with multiple compositions and concurrency values to compare against each other.

```
npx remotion benchmark src/index.ts [composition-ids]Copy
```

You can provide multiple composition IDs separated by comma, ex: `npx remotion benchmark src/index.ts --codec=h264 Main,Canvas,CSS`

If `composition-ids` is not passed, Remotion will let you select compositions from a list.

## Flags[​](#flags)

### `--runs`[​](#--runs)

Specify how many times the video should be rendered during a benchmark. Default `3`.

### `--concurrencies`[​](#--concurrencies)

Specify which concurrency values should be used while benchmarking. Multiple values can be passed separated by comma. Learn more about [concurrency](https://remotion.dev/docs/terminology/concurrency).

### `--codec`[​](#--codec)

Inherited from [`npx remotion render`](/docs/cli/render#--codec)

### `--audio-codec`[v3.3.42](https://github.com/remotion-dev/remotion/releases/v3.3.42)[​](#--audio-codec)

Set the format of the audio that is embedded in the video. Not all codec and audio codec combinations are supported and certain combinations require a certain file extension and container format. See the table in the docs to see possible combinations.

### `--crf`[​](#--crf)

Inherited from [`npx remotion render`](/docs/cli/render#--crf)

### `--frames`[​](#--frames)

Inherited from [`npx remotion render`](/docs/cli/render#--frames)

### `--image-format`[​](#--image-format)

Inherited from [`npx remotion render`](/docs/cli/render#--image-format)

### `--pixel-format`[​](#--pixel-format)

Inherited from [`npx remotion render`](/docs/cli/render#--pixel-format)

### `--props`[​](#--props)

Inherited from [`npx remotion render`](/docs/cli/render#--props)

### `--prores-profile`[​](#--prores-profile)

Inherited from [`npx remotion render`](/docs/cli/render#--prores-profile)

### `--jpeg-quality`[v4.0.0](https://github.com/remotion-dev/remotion/releases/v4.0.0)[​](#--jpeg-quality)

Inherited from [`npx remotion render`](/docs/cli/render#--jpeg-quality)

### `--quality`[​](#--quality)

Removed in v4.0.0. Renamed to `--jpeg-quality`.

### `--log`[​](#--log)

Inherited from [`npx remotion render`](/docs/cli/render#--log)

### `--ignore-certificate-errors`[​](#--ignore-certificate-errors)

Inherited from [`npx remotion render`](/docs/cli/render#--ignore-certificate-errors)

### `--disable-web-security`[​](#--disable-web-security)

Inherited from [`npx remotion render`](/docs/cli/render#--disable-web-security)

### `--dark-mode`[v4.0.381](https://github.com/remotion-dev/remotion/releases/v4.0.381)[​](#--dark-mode)

Whether Chromium should pretend to be in dark mode by emulating the media feature 'prefers-color-scheme: dark'. Default is `false`.

### `--disable-headless`[​](#--disable-headless)

Deprecated - will be removed in 5.0.0. With the migration to [Chrome Headless Shell](/docs/miscellaneous/chrome-headless-shell), this option is not functional anymore.

 If disabled, the render will open an actual Chrome window where you can see the render happen. The default is headless mode.

### `--enable-multiprocess-on-linux`[v4.0.42](https://github.com/remotion-dev/remotion/releases/v4.0.42)[​](#--enable-multiprocess-on-linux)

Removes the `--single-process` flag that gets passed to Chromium on Linux by default. This will make the render faster because multiple processes can be used, but may cause issues with some Linux distributions or if window server libraries are missing.
Default: `false` until v4.0.136, then `true` from v4.0.137 on because newer Chrome versions don't allow rendering with the `--single-process` flag. 
This flag will be removed in Remotion v5.0.

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

### `--timeout`[​](#--timeout)

Inherited from [`npx remotion render`](/docs/cli/render#--timeout)

### `--scale`[​](#--scale)

Inherited from [`npx remotion render`](/docs/cli/render#--scale)

### `--port`[​](#--port)

Inherited from [`npx remotion render`](/docs/cli/render#--port)

### `--number-of-gif-loops`[​](#--number-of-gif-loops)

Allows you to set the number of loops as follows:
- `null` (or omitting in the CLI) plays the GIF indefinitely.
- `0` disables looping
- `1` loops the GIF once (plays twice in total)
- `2` loops the GIF twice (plays three times in total) and so on.

### `--every-nth-frame`[​](#--every-nth-frame)

Inherited from [`npx remotion render`](/docs/cli/render#--every-nth-frame)

### `--log`[​](#--log-1)

Inherited from [`npx remotion render`](/docs/cli/render#--log)

### `--muted`[​](#--muted)

Inherited from [`npx remotion render`](/docs/cli/render#--muted)

### `--enforce-audio-track`[​](#--enforce-audio-track)

Inherited from [`npx remotion render`](/docs/cli/render#--enforce-audio-track)

### `--disallow-parallel-encoding`[v4.0.315](https://github.com/remotion-dev/remotion/releases/v4.0.315)[​](#--disallow-parallel-encoding)

Inherited from [`npx remotion render`](/docs/cli/render#--disallow-parallel-encoding)

### `--browser-executable`[​](#--browser-executable)

Inherited from [`npx remotion render`](/docs/cli/render#--browser-executable)

### `--public-dir`[​](#--public-dir)

Inherited from [`npx remotion render`](/docs/cli/render#--public-dir)

### `--config`[​](#--config)

Inherited from [`npx remotion render`](/docs/cli/render#--config)

### `--bundle-cache`[​](#--bundle-cache)

Inherited from [`npx remotion render`](/docs/cli/render#--bundle-cache)

### `--video-bitrate`[​](#--video-bitrate)

Inherited from [`npx remotion render`](/docs/cli/render#--video-bitrate)

### `--audio-bitrate`[​](#--audio-bitrate)

Inherited from [`npx remotion render`](/docs/cli/render#--audio-bitrate)

### `--color-space`[v4.0.28](https://github.com/remotion-dev/remotion/releases/v4.0.28)[​](#--color-space)

Color space to use for the video. Acceptable values: `"default"`(default since 5.0), `"bt601"` (same as `"default"`, since v4.0.424), `"bt709"` (since v4.0.28), `"bt2020-ncl"` (since v4.0.88), `"bt2020-cl"` (since v4.0.88), .
For best color accuracy, it is recommended to also use `"png"` as the image format to have accurate color transformations throughout.
Only since v4.0.83, colorspace conversion is actually performed, previously it would only tag the metadata of the video.

### `--hardware-acceleration`[v4.0.228](https://github.com/remotion-dev/remotion/releases/v4.0.228)[​](#--hardware-acceleration)

			One of
			"disable", "if-possible", or "required"
			. Default "disable". Encode using a hardware-accelerated encoder if
			available. If set to "required" and no hardware-accelerated encoder is
			available, then the render will fail.
		

### `--offthreadvideo-cache-size-in-bytes`[v4.0.23](https://github.com/remotion-dev/remotion/releases/v4.0.23)[​](#--offthreadvideo-cache-size-in-bytes)

From v4.0, Remotion has a cache for [`<OffthreadVideo>`](https://remotion.dev/docs/offthreadvideo) frames. The default is `null`, corresponding to half of the system memory available when the render starts.
 This option allows to override the size of the cache. The higher it is, the faster the render will be, but the more memory will be used.
The used value will be printed when running in verbose mode.
Default: `null`

### `--media-cache-size-in-bytes`[v4.0.352](https://github.com/remotion-dev/remotion/releases/v4.0.352)[​](#--media-cache-size-in-bytes)

Specify the maximum size of the cache that `<Video>` and `<Audio>` from `@remotion/media` may use combined, in bytes. 
The default is half of the available system memory when the render starts.

### `--binaries-directory`[v4.0.120](https://github.com/remotion-dev/remotion/releases/v4.0.120)[​](#--binaries-directory)

The directory where the platform-specific binaries and libraries that Remotion needs are located. Those include an `ffmpeg` and `ffprobe` binary, a Rust binary for various tasks, and various shared libraries. If the value is set to `null`, which is the default, then the path of a platform-specific package located at `node_modules/@remotion/compositor-*` is selected.
This option is useful in environments where Remotion is not officially supported to run like bundled serverless functions or Electron.

### `--experimental-rspack`[v4.0.426](https://github.com/remotion-dev/remotion/releases/v4.0.426)[​](#--experimental-rspack)

Uses Rspack instead of Webpack as the bundler for the Studio or bundle.

### `--ffmpeg-executable`[​](#--ffmpeg-executable)

Removed in v4.0. Inherited from [`npx remotion render`](/docs/cli/render#--ffmpeg-executable)

### `--ffprobe-executable`[​](#--ffprobe-executable)

Removed in v4.0. Inherited from [`npx remotion render`](/docs/cli/render#--ffprobe-executable-)](/docs/cli/render#--ffprobe-executable-)](/docs/cli/render#--ffprobe-executable-)
](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)
- ](/docs/cli/render#--ffprobe-executable-)