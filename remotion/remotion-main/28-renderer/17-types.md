---
title: "Types"
url: "https://www.remotion.dev/docs/renderer/types"
path: "/docs/renderer/types"
---

"---\nimage: /generated/articles-docs-renderer-types.png\nid: types\nsidebar_label: Types\ntitle: TypeScript Types Reference\nslug: /renderer/types\ncrumb: '@remotion/renderer'\n---\n\nThe following types are part of the API of `@remotion/renderer`:\n\n## `Codec`\n\n```tsx twoslash\nimport type {Codec} from '@remotion/renderer';\n//                ^?\n```\n\nRefer to the [Encoding guide](/docs/encoding) for more information.\n\n## `AudioCodec`\n\n```tsx twoslash\nimport type {AudioCodec} from '@remotion/renderer';\n//                ^?\n```\n\nRefer to the [Encoding guide](/docs/encoding/#audio-codec) to see defaults and supported combinations.\n\n## `VideoImageFormat`\n\n```tsx twoslash\nimport type {VideoImageFormat} from '@remotion/renderer';\n//                ^?\n```\n\n## `StillImageFormat`\n\n```tsx twoslash\nimport type {StillImageFormat} from '@remotion/renderer';\n//                ^?\n```\n\n## `PixelFormat`\n\n```tsx twoslash\nimport type {PixelFormat} from '@remotion/renderer';\n//                ^?\n```\n\n## `FrameRange`\n\n```tsx twoslash\nimport type {FrameRange} from '@remotion/renderer';\n//                ^?\n```\n\n- A single number renders only that frame\n- A tuple `[start, end]` renders frames from `start` to `end` (inclusive)\n- A tuple `[start, null]` renders frames from `start` to the end of the composition<AvailableFrom v=\"4.0.421\" inline />\n\n## `Concurrency`\n\n```tsx twoslash\nimport type {Concurrency} from '@remotion/renderer';\n//                ^?\n```\n\n## `LogLevel`\n\n```tsx twoslash\nimport type {LogLevel} from '@remotion/renderer';\n//                ^?\n```\n\n## `OpenGlRenderer`\n\n```tsx twoslash\nimport type {OpenGlRenderer} from '@remotion/renderer';\n//                ^?\n```\n\n## `ChromeMode`\n\n```tsx twoslash\nimport type {ChromeMode} from '@remotion/renderer';\n//                ^?\n```\n\n## `ColorSpace`\n\n```tsx twoslash\nimport type {ColorSpace} from '@remotion/renderer';\n//                ^?\n```\n\n## `X264Preset`\n\n```tsx twoslash\nimport type {X264Preset} from '@remotion/renderer';\n//                ^?\n```\n\n## `Crf`\n\n```tsx twoslash\nimport type {Crf} from '@remotion/renderer';\n//            ^?\n```\n\n## `Bitrate`\n\n```tsx twoslash\nimport type {Bitrate} from '@remotion/renderer';\n//                ^?\n```\n\n## `ChromiumOptions`\n\n```tsx twoslash\nimport type {ChromiumOptions} from '@remotion/renderer';\n//                ^?\n```\n\n## `OnStartData`\n\n```tsx twoslash\nimport type {OnStartData} from '@remotion/renderer';\n//                ^?\n```\n\n- `frameCount`: The number of frames that will be rendered\n- `parallelEncoding`: Whether parallel encoding is enabled<AvailableFrom v=\"4.0.52\" inline />\n- `resolvedConcurrency`: The concurrency that will be used<AvailableFrom v=\"4.0.180\" inline />\n\n## `RenderMediaOnProgress`\n\n```tsx twoslash\nimport type {RenderMediaOnProgress} from '@remotion/renderer';\n//                ^?\n```\n\n## `StitchingState`\n\n```tsx twoslash\nimport type {StitchingState} from '@remotion/renderer';\n//                ^?\n```\n\n- `encoding`: Rendering frames and encoding into video\n- `muxing`: Encoding audio and combining it with video (only when parallel encoding is used)\n\n## `SlowFrame`\n\n```tsx twoslash\nimport type {SlowFrame} from '@remotion/renderer';\n//                ^?\n```\n\n## `RenderMediaOnDownload`\n\n```tsx twoslash\nimport type {RenderMediaOnDownload} from '@remotion/renderer';\n//                ^?\n```\n\n## `BrowserLog`\n\n```tsx twoslash\nimport type {BrowserLog} from '@remotion/renderer';\n//                ^?\n```\n\n- `type`: The `console.*` method (`log`, `warn`, `error`, etc.)\n- `text`: The logged message\n- `stackTrace`: The stack trace of the log\n\n## `FfmpegOverrideFn`\n\n```tsx twoslash\nimport type {FfmpegOverrideFn} from '@remotion/renderer';\n//                ^?\n```\n\n## `OnArtifact`\n\n```tsx twoslash\nimport type {OnArtifact} from '@remotion/renderer';\n//                ^?\n```\n\n## `EmittedArtifact`\n\n```tsx twoslash\nimport type {EmittedArtifact} from '@remotion/renderer';\n//                ^?\n```\n\n- `filename`: The name of the artifact file\n- `content`: The content of the artifact as a `string` or `Uint8Array`\n- `frame`: The frame number at which the artifact was emitted\n\n## `OnBrowserDownload`\n\n```tsx twoslash\nimport type {OnBrowserDownload} from '@remotion/renderer';\n//                ^?\n```\n\n## `DownloadBrowserProgressFn`\n\n```tsx twoslash\nimport type {DownloadBrowserProgressFn} from '@remotion/renderer';\n//                ^?\n```\n\n## `NumberOfGifLoops`\n\n```tsx twoslash\nimport type {NumberOfGifLoops} from '@remotion/renderer';\n//                ^?\n```\n\n## `RenderMediaOptions`\n\n```tsx twoslash\nimport type {RenderMediaOptions} from '@remotion/renderer';\n//                ^?\n```\n\n## `RenderStillOptions`\n\n```tsx twoslash\nimport type {RenderStillOptions} from '@remotion/renderer';\n//                ^?\n```\n\n## `RenderFramesOptions`\n\n```tsx twoslash\nimport type {RenderFramesOptions} from '@remotion/renderer';\n//                ^?\n```\n\n## `SelectCompositionOptions`\n\n```tsx twoslash\nimport type {SelectCompositionOptions} from '@remotion/renderer';\n//                ^?\n```\n"

The following types are part of the API of `@remotion/renderer`:

## `Codec`[​](#codec)

```
import type {Codec} from '@remotion/renderer';
              
(alias) type Codec = "h264" | "h265" | "vp8" | "vp9" | "mp3" | "aac" | "wav" | "prores" | "h264-mkv" | "h264-ts" | "gif"
import CodecCopy
```

Refer to the [Encoding guide](/docs/encoding) for more information.

## `AudioCodec`[​](#audiocodec)

```
import type {AudioCodec} from '@remotion/renderer';
                 
(alias) type AudioCodec = "pcm-16" | "aac" | "mp3" | "opus"
import AudioCodecCopy
```

Refer to the [Encoding guide](/docs/encoding/#audio-codec) to see defaults and supported combinations.

## `VideoImageFormat`[​](#videoimageformat)

```
import type {VideoImageFormat} from '@remotion/renderer';
                    
(alias) type VideoImageFormat = "png" | "jpeg" | "none"
import VideoImageFormatCopy
```

## `StillImageFormat`[​](#stillimageformat)

```
import type {StillImageFormat} from '@remotion/renderer';
                    
(alias) type StillImageFormat = "png" | "jpeg" | "pdf" | "webp"
import StillImageFormatCopy
```

## `PixelFormat`[​](#pixelformat)

```
import type {PixelFormat} from '@remotion/renderer';
                 
(alias) type PixelFormat = "yuv420p" | "yuva420p" | "yuv422p" | "yuv444p" | "yuv420p10le" | "yuv422p10le" | "yuv444p10le" | "yuva444p10le"
import PixelFormatCopy
```

## `FrameRange`[​](#framerange)

```
import type {FrameRange} from '@remotion/renderer';
                 
(alias) type FrameRange = number | [number, number] | [number, null]
import FrameRangeCopy
```

- A single number renders only that frame

- A tuple `[start, end]` renders frames from `start` to `end` (inclusive)

- A tuple `[start, null]` renders frames from `start` to the end of the composition[v4.0.421](https://github.com/remotion-dev/remotion/releases/v4.0.421)

## `Concurrency`[​](#concurrency)

```
import type {Concurrency} from '@remotion/renderer';
                 
(alias) type Concurrency = string | number | null
import ConcurrencyCopy
```

## `LogLevel`[​](#loglevel)

```
import type {LogLevel} from '@remotion/renderer';
                
(alias) type LogLevel = "trace" | "verbose" | "info" | "warn" | "error"
import LogLevelCopy
```

## `OpenGlRenderer`[​](#openglrenderer)

```
import type {OpenGlRenderer} from '@remotion/renderer';
                   
(alias) type OpenGlRenderer = "swangle" | "angle" | "egl" | "swiftshader" | "vulkan" | "angle-egl"
import OpenGlRendererCopy
```

## `ChromeMode`[​](#chromemode)

```
import type {ChromeMode} from '@remotion/renderer';
                 
(alias) type ChromeMode = "headless-shell" | "chrome-for-testing"
import ChromeModeCopy
```

## `ColorSpace`[​](#colorspace)

```
import type {ColorSpace} from '@remotion/renderer';
                 
(alias) type ColorSpace = "default" | "bt601" | "bt709" | "bt2020-ncl"
import ColorSpaceCopy
```

## `X264Preset`[​](#x264preset)

```
import type {X264Preset} from '@remotion/renderer';
                 
(alias) type X264Preset = "ultrafast" | "superfast" | "veryfast" | "faster" | "fast" | "medium" | "slow" | "slower" | "veryslow" | "placebo"
import X264PresetCopy
```

## `Crf`[​](#crf)

```
import type {Crf} from '@remotion/renderer';
             
(alias) type Crf = number | undefined
import CrfCopy
```

## `Bitrate`[​](#bitrate)

```
import type {Bitrate} from '@remotion/renderer';
               
(alias) type Bitrate = `${number}k` | `${number}K` | `${number}M`
import BitrateCopy
```

## `ChromiumOptions`[​](#chromiumoptions)

```
import type {ChromiumOptions} from '@remotion/renderer';
                   
(alias) type ChromiumOptions = {
    ignoreCertificateErrors?: boolean;
    disableWebSecurity?: boolean;
    gl?: ("swangle" | "angle" | "egl" | "swiftshader" | "vulkan" | "angle-egl") | null;
    userAgent?: string | null;
    enableMultiProcessOnLinux?: boolean;
    darkMode?: boolean;
} & {
    headless?: boolean;
}
import ChromiumOptionsCopy
```

## `OnStartData`[​](#onstartdata)

```
import type {OnStartData} from '@remotion/renderer';
                 
(alias) type OnStartData = {
    frameCount: number;
    parallelEncoding: boolean;
    resolvedConcurrency: number;
}
import OnStartDataCopy
```

- `frameCount`: The number of frames that will be rendered

- `parallelEncoding`: Whether parallel encoding is enabled[v4.0.52](https://github.com/remotion-dev/remotion/releases/v4.0.52)

- `resolvedConcurrency`: The concurrency that will be used[v4.0.180](https://github.com/remotion-dev/remotion/releases/v4.0.180)

## `RenderMediaOnProgress`[​](#rendermediaonprogress)

```
import type {RenderMediaOnProgress} from '@remotion/renderer';
                      
(alias) type RenderMediaOnProgress = (progress: {
    renderedFrames: number;
    encodedFrames: number;
    encodedDoneIn: number | null;
    renderedDoneIn: number | null;
    renderEstimatedTime: number;
    progress: number;
    stitchStage: StitchingState;
}) => void
import RenderMediaOnProgressCopy
```

## `StitchingState`[​](#stitchingstate)

```
import type {StitchingState} from '@remotion/renderer';
                   
(alias) type StitchingState = "encoding" | "muxing"
import StitchingStateCopy
```

- `encoding`: Rendering frames and encoding into video

- `muxing`: Encoding audio and combining it with video (only when parallel encoding is used)

## `SlowFrame`[​](#slowframe)

```
import type {SlowFrame} from '@remotion/renderer';
                
(alias) type SlowFrame = {
    frame: number;
    time: number;
}
import SlowFrameCopy
```

## `RenderMediaOnDownload`[​](#rendermediaondownload)

```
import type {RenderMediaOnDownload} from '@remotion/renderer';
                      
(alias) type RenderMediaOnDownload = (src: string) => ((progress: {
    percent: number | null;
    downloaded: number;
    totalSize: number | null;
}) => void) | undefined | void
import RenderMediaOnDownloadCopy
```

## `BrowserLog`[​](#browserlog)

```
import type {BrowserLog} from '@remotion/renderer';
                 
(alias) type BrowserLog = {
    text: string;
    stackTrace: ConsoleMessageLocation[];
    type: ConsoleMessageType;
}
import BrowserLogCopy
```

- `type`: The `console.*` method (`log`, `warn`, `error`, etc.)

- `text`: The logged message

- `stackTrace`: The stack trace of the log

## `FfmpegOverrideFn`[​](#ffmpegoverridefn)

```
import type {FfmpegOverrideFn} from '@remotion/renderer';
                    
(alias) type FfmpegOverrideFn = (info: {
    type: "pre-stitcher" | "stitcher";
    args: string[];
}) => string[]
import FfmpegOverrideFnCopy
```

## `OnArtifact`[​](#onartifact)

```
import type {OnArtifact} from '@remotion/renderer';
                 
(alias) type OnArtifact = (asset: EmittedArtifact) => void
import OnArtifactCopy
```

## `EmittedArtifact`[​](#emittedartifact)

```
import type {EmittedArtifact} from '@remotion/renderer';
                   
(alias) type EmittedArtifact = {
    filename: string;
    content: string | Uint8Array;
    frame: number;
    downloadBehavior: DownloadBehavior | null;
}
import EmittedArtifactCopy
```

- `filename`: The name of the artifact file

- `content`: The content of the artifact as a `string` or `Uint8Array`

- `frame`: The frame number at which the artifact was emitted

## `OnBrowserDownload`[​](#onbrowserdownload)

```
import type {OnBrowserDownload} from '@remotion/renderer';
                    
(alias) type OnBrowserDownload = (options: {
    chromeMode: ChromeMode;
}) => {
    onProgress: DownloadBrowserProgressFn;
    version: string | null;
}
import OnBrowserDownloadCopy
```

## `DownloadBrowserProgressFn`[​](#downloadbrowserprogressfn)

```
import type {DownloadBrowserProgressFn} from '@remotion/renderer';
                        
(alias) type DownloadBrowserProgressFn = (progress: {
    alreadyAvailable: boolean;
    percent: number;
    downloadedBytes: number;
    totalSizeInBytes: number;
}) => void
import DownloadBrowserProgressFnCopy
```

## `NumberOfGifLoops`[​](#numberofgifloops)

```
import type {NumberOfGifLoops} from '@remotion/renderer';
                    
(alias) type NumberOfGifLoops = number | null
import NumberOfGifLoopsCopy
```

## `RenderMediaOptions`[​](#rendermediaoptions)

```
import type {RenderMediaOptions} from '@remotion/renderer';
                     
(alias) type RenderMediaOptions = {
    outputLocation?: string | null | undefined;
    codec: Codec;
    composition: VideoConfig;
    inputProps?: Record<string, unknown> | undefined;
    crf?: number | null | undefined;
    imageFormat?: VideoImageFormat | undefined;
    pixelFormat?: PixelFormat | undefined;
    envVariables?: Record<string, string> | undefined;
    quality?: never | undefined;
    jpegQuality?: number | undefined;
    frameRange?: (FrameRange | null) | undefined;
    everyNthFrame?: number | undefined;
    puppeteerInstance?: HeadlessBrowser | undefined;
    overwrite?: boolean | undefined;
    onProgress?: RenderMediaOnProgress | undefined;
    ... 26 more ...;
    isProduction?: boolean | undefined;
} & (({
    ...;
} | {
    ...;
}) & Partial<...>)
import RenderMediaOptionsCopy
```

## `RenderStillOptions`[​](#renderstilloptions)

```
import type {RenderStillOptions} from '@remotion/renderer';
                     
(alias) type RenderStillOptions = {
    port?: number | null;
    composition: VideoConfig;
    output?: string | null;
    frame?: number;
    inputProps?: Record<string, unknown>;
    imageFormat?: StillImageFormat;
    puppeteerInstance?: HeadlessBrowser;
    dumpBrowserLogs?: boolean;
    envVariables?: Record<string, string>;
    overwrite?: boolean;
    browserExecutable?: BrowserExecutable;
    onBrowserLog?: (log: BrowserLog) => void;
    chromiumOptions?: ChromiumOptions;
    ... 7 more ...;
    isProduction?: boolean;
} & Partial<...> & {
    ...;
}
import RenderStillOptionsCopy
```

## `RenderFramesOptions`[​](#renderframesoptions)

```
import type {RenderFramesOptions} from '@remotion/renderer';
                     
(alias) type RenderFramesOptions = {
    onStart: (data: OnStartData) => void;
    onFrameUpdate: (framesRendered: number, frameIndex: number, timeToRenderInMilliseconds: number) => void;
    outputDir: string | null;
    inputProps: Record<string, unknown>;
    envVariables?: Record<string, string> | undefined;
    imageFormat?: VideoImageFormat | undefined;
    quality?: never | undefined;
    frameRange?: (FrameRange | null) | undefined;
    everyNthFrame?: number | undefined;
    dumpBrowserLogs?: boolean | undefined;
    verbose?: boolean | undefined;
    puppeteerInstance?: HeadlessBrowser | undefined;
    ... 23 more ...;
    readonly imageSequencePattern?: string | ... 1 more ... | undefined;
}
import RenderFramesOptionsCopy
```

## `SelectCompositionOptions`[​](#selectcompositionoptions)

```
import type {SelectCompositionOptions} from '@remotion/renderer';
                        
(alias) type SelectCompositionOptions = {
    inputProps?: Record<string, unknown> | undefined;
    envVariables?: Record<string, string> | undefined;
    puppeteerInstance?: HeadlessBrowser | undefined;
    onBrowserLog?: ((log: BrowserLog) => void) | undefined;
    browserExecutable?: BrowserExecutable | undefined;
    chromiumOptions?: ChromiumOptions | undefined;
    port?: number | null | undefined;
    verbose?: boolean | undefined;
    serveUrl: string;
    id: string;
    readonly mediaCacheSizeInBytes?: number | null | undefined;
    readonly offthreadVideoCacheSizeInBytes?: number | null | undefined;
    ... 5 more ...;
    readonly chromeMode?: "chrome-for-testing" | ... 1 more ... | undefined;
}
import SelectCompositionOptionsCopy
```
](#selectcompositionoptions)](#selectcompositionoptions)
](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)
- ](#selectcompositionoptions)