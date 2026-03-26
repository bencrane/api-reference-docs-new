# Remotion Technical Reference

**Comprehensive technical documentation for Remotion — the React framework for programmatic video generation**

Generated: 2026-03-26

This document covers the complete Remotion API surface for engineers building a programmatic video generation integration. It includes architecture fundamentals, the full composition and rendering model, all client and server APIs (CLI, Node.js, Lambda), media handling (assets, audio, text, shapes, transitions), the browser-embedded Player component, pricing and licensing details, and practical guidance for multi-tenant deployment. Use this as the canonical reference when designing, building, or debugging a Remotion-based video pipeline.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Core Package Inventory](#2-core-package-inventory)
3. [Composition & Component Model](#3-composition--component-model)
4. [Rendering Pipeline](#4-rendering-pipeline)
5. [Input Props & Dynamic Content](#5-input-props--dynamic-content)
6. [Asset Handling](#6-asset-handling)
7. [Transitions & Motion](#7-transitions--motion)
8. [Text & Typography](#8-text--typography)
9. [Shapes & Graphics](#9-shapes--graphics)
10. [Audio](#10-audio)
11. [The Remotion Player](#11-the-remotion-player)
12. [CLI Reference](#12-cli-reference)
13. [Node.js API Reference](#13-nodejs-api-reference)
14. [Lambda API Reference](#14-lambda-api-reference)
15. [Pricing & Licensing](#15-pricing--licensing)
16. [Integration Architecture for a Multi-Tenant API](#16-integration-architecture-for-a-multi-tenant-api)
17. [Gotchas, Limitations & Weird Stuff](#17-gotchas-limitations--weird-stuff)
18. [Version & Ecosystem](#18-version--ecosystem)


---

## 1. Architecture Overview

## What Is Remotion

Remotion is a framework for creating videos programmatically using React. It maps React components to video frames: every frame of the output video corresponds to a deterministic React render at that point in time. The pipeline is:

1. **Author** -- Write React components that accept a frame number and render visual output for that frame using standard HTML/CSS/SVG/Canvas.
2. **Preview** -- The Remotion Studio (a local dev server) or the `<Player>` component lets you scrub through the timeline in real time in a browser.
3. **Bundle** -- `@remotion/bundler` (Webpack) or the CLI compiles your React project into a static site (HTML + JS bundle).
4. **Render** -- A headless browser (Chrome/Chromium) opens the bundle, navigates to each frame, takes a screenshot, and pipes the screenshots to FFmpeg (or WebCodecs) which encodes them into a video file (MP4, WebM, etc.).

This architecture means:

- There is no imperative animation loop. You declare what frame `N` looks like and Remotion handles sequencing.
- Each frame render is independent and stateless (aside from `delayRender` for async data). This enables parallel rendering across multiple browser tabs or Lambda invocations.
- Any technology that works in Chrome works in Remotion: CSS animations driven by `useCurrentFrame()`, Three.js via `@remotion/three`, Lottie via `@remotion/lottie`, SVG, Canvas, etc.

## Core Rendering Pipeline

The end-to-end path from component to `.mp4` file:

1. **`registerRoot()`** -- Called once in the entry file (`src/index.ts`). Registers the root React component that declares all `<Composition>` elements.
2. **`<Composition>`** -- Each `<Composition>` defines a renderable unit with `id`, `width`, `height`, `fps`, `durationInFrames`, `component`, and optionally `defaultProps` / `schema` / `calculateMetadata`.
3. **`bundle()`** (`@remotion/bundler`) -- Compiles the project into a Webpack bundle served as static files.
4. **`selectComposition()`** (`@remotion/renderer`) -- Opens a headless browser, loads the bundle, resolves `calculateMetadata()`, and returns the final composition metadata (dimensions, duration, resolved props).
5. **`renderMedia()`** (`@remotion/renderer`) -- For each frame (potentially across `concurrency` browser tabs): sets `window.remotion_setFrame(n)`, waits for all `delayRender()` handles to be cleared via `continueRender()`, takes a screenshot, and feeds frames to FFmpeg for encoding. Audio is extracted separately from `<Html5Audio>`, `<Html5Video>`, `<OffthreadVideo>` sources and mixed into the final file.

## Key Concepts

| Concept | Description |
|---|---|
| **Composition** | A registered video or still defined by `id`, `width`, `height`, `fps`, `durationInFrames`, and a React component. |
| **Frame** | A single point in time, 0-indexed. Frame 0 is the first frame; the last frame is `durationInFrames - 1`. |
| **FPS** | Frames per second. Determines both playback speed and how many screenshots are taken during rendering. |
| **Duration** | Expressed in frames (`durationInFrames`). Duration in seconds = `durationInFrames / fps`. |
| **Sequence** | A component that time-shifts its children. Children see `useCurrentFrame()` relative to the sequence's `from` value. |
| **Input Props** | Data passed to a composition at render time (via CLI `--props` or API `inputProps`). Merged with `defaultProps` to produce the final props the component receives. |
| **`useCurrentFrame()`** | React hook returning the current frame number (relative to the nearest `<Sequence>`). |
| **`useVideoConfig()`** | React hook returning `{ width, height, fps, durationInFrames, id, defaultProps, props }`. |
| **`interpolate()`** | Pure function mapping an input range to an output range, used to drive animations from frame numbers. |

## Player vs Renderer

| Aspect | `<Player>` (`@remotion/player`) | Renderer (`@remotion/renderer`) |
|---|---|---|
| **Runs in** | Browser (any web app) | Node.js / Bun (server-side) |
| **Purpose** | Real-time preview and interactive playback | Produces an actual video/audio/image file |
| **Frame advancing** | `requestAnimationFrame` in real time | Deterministic: sets frame, waits for render, screenshots |
| **Output** | None (visual only) | `.mp4`, `.webm`, `.mov`, `.gif`, `.png`, `.jpeg`, etc. |
| **`delayRender()`** | No-op (ignored) | Blocks the screenshot until `continueRender()` is called |
| **Dependencies** | Only `remotion` + `@remotion/player` | `remotion` + `@remotion/bundler` + `@remotion/renderer` + Chrome + FFmpeg |

## What Runs Where

| Environment | What executes |
|---|---|
| **Browser (preview/Player)** | React components, `useCurrentFrame()`, `interpolate()`, `spring()`, `<Sequence>`, `<Series>`, media playback via HTML5 tags. `delayRender()` is a no-op. |
| **Browser (during render)** | Same React components, but inside a headless Chrome controlled by the renderer. `delayRender()` blocks screenshotting. `<OffthreadVideo>` extracts frames via FFmpeg instead of using `<video>` tag. |
| **Node.js / Bun** | `@remotion/renderer` APIs (`renderMedia`, `renderStill`, `renderFrames`, etc.), `@remotion/bundler` (`bundle()`), FFmpeg orchestration, composition selection. |
| **AWS Lambda** | `@remotion/lambda` distributes rendering across Lambda functions. Each function renders a chunk of frames, uploads to S3, then a final function stitches them. |
| **GCP Cloud Run** | `@remotion/cloudrun` provides equivalent cloud rendering on Google Cloud. |
| **Vercel** | `@remotion/vercel` renders inside Vercel Sandbox environments. |

---

## 2. Core Package Inventory

## Core Rendering

### `remotion`

The foundational package containing all essential building blocks for expressing videos. Exports components (`<Composition>`, `<Sequence>`, `<Series>`, `<AbsoluteFill>`, `<Freeze>`, `<Loop>`, `<Still>`, `<Img>`, `<IFrame>`, `<Html5Video>`, `<Html5Audio>`, `<OffthreadVideo>`, `<AnimatedImage>`, `<Artifact>`, `<Folder>`), hooks (`useCurrentFrame()`, `useVideoConfig()`, `useBufferState()`, `useCurrentScale()`, `useDelayRender()`, `useRemotionEnvironment()`), animation functions (`interpolate()`, `interpolateColors()`, `spring()`, `measureSpring()`, `Easing`), lifecycle functions (`delayRender()`, `continueRender()`, `cancelRender()`, `registerRoot()`), and utilities (`staticFile()`, `getInputProps()`, `getRemotionEnvironment()`, `getStaticFiles()`, `random()`, `prefetch()`, `VERSION`). Pure functions like `interpolate()` can also be used outside of Remotion. **Dependencies:** React.

**When to use:** Always -- this is required for every Remotion project.

### `@remotion/bundler`

Creates a Webpack bundle from a Remotion project, producing a static site that can be opened by a headless browser for rendering.

**Key exports:** `bundle()`

**When to use:** When rendering on the server side (Node.js/Bun). Required by `@remotion/renderer`. Not needed if only using `<Player>`.

**Dependencies:** `remotion`, Webpack.

### `@remotion/renderer`

Renders video, audio, and still images from Node.js or Bun. Controls headless Chrome instances, takes frame screenshots, and encodes output via FFmpeg.

**Key exports:** `renderMedia()`, `renderStill()`, `renderFrames()`, `stitchFramesToVideo()`, `getCompositions()`, `selectComposition()`, `openBrowser()`, `ensureBrowser()`, `makeCancelSignal()`, `getVideoMetadata()`, `getSilentParts()`, `combineChunks()`, `ensureFfmpeg()`, `ensureFfprobe()`, `getCanExtractFramesFast()`

**When to use:** For server-side rendering of videos, stills, and frame sequences. Core of any render pipeline outside of cloud rendering.

**Dependencies:** `remotion`, `@remotion/bundler`, Chrome/Chromium, FFmpeg.

### `@remotion/studio`

APIs for controlling the Remotion Studio development environment (the local dev server UI).

**Key exports:** `getStaticFiles()`, `watchPublicFolder()`, `watchStaticFile()`, `writeStaticFile()`, `saveDefaultProps()`, `updateDefaultProps()`, `deleteStaticFile()`, `restartStudio()`, `play()`, `pause()`, `toggle()`, `seek()`, `goToComposition()`, `focusDefaultPropsPath()`, `reevaluateComposition()`, `visualControl()`

**When to use:** For building custom Studio extensions, automating Studio workflows, or adding visual controls for props editing.

**Dependencies:** `remotion`.

### `@remotion/cli`

Command-line interface for Remotion. Provides `npx remotion studio` (dev server), `npx remotion render` (render video), `npx remotion still` (render image), and configuration management.

**Key exports:** CLI commands (not programmatic exports). Configuration via `remotion.config.ts`.

**When to use:** Primary development and rendering workflow for most users.

**Dependencies:** `remotion`, `@remotion/bundler`, `@remotion/renderer`.

### `@remotion/player`

Embeds a Remotion composition as an interactive, scrubable video player in any React web application. No server-side rendering required.

**Key exports:** `<Player>`, `<Thumbnail>`

**When to use:** When you want to preview or display Remotion compositions in a web app without generating actual video files.

**Dependencies:** `remotion`, React.

### `@remotion/web-renderer`

Renders video entirely in the browser using WebCodecs, without needing a server. Experimental.

**Key exports:** `renderMediaOnWeb()`, `renderStillOnWeb()`

**When to use:** Client-side rendering scenarios where no Node.js server is available.

**Dependencies:** `remotion`.

## Media Handling

### `@remotion/media`

An experimental package providing WebCodecs-based `<Video>` and `<Audio>` tags for embedding media. Intended to eventually replace `<Html5Video>` and `<Html5Audio>`.

**Key exports:** `<Video>`, `<Audio>`

**When to use:** When you want the latest WebCodecs-based media embedding, or need client-side rendering compatibility.

**Dependencies:** `remotion`.

### `@remotion/media-utils`

Utilities for obtaining metadata and waveform data from audio and video sources.

**Key exports:** `getAudioData()`, `getAudioDurationInSeconds()`, `getVideoMetadata()`, `getWaveformPortion()`, `useAudioData()`, `useWindowedAudioData()`, `visualizeAudio()`, `visualizeAudioWaveform()`, `audioBufferToDataUrl()`, `createSmoothSvgPath()`

**When to use:** Audio visualization, waveform display, reading media metadata in the browser.

**Dependencies:** `remotion`.

### `@remotion/media-parser`

A pure JavaScript library for parsing video and audio container formats without FFmpeg.

**Key exports:** `parseMedia()`, `downloadAndParseMedia()`, `parseMediaOnWebWorker()`, `parseMediaOnServerWorker()`, `mediaParserController()`, `hasBeenAborted()`, `WEBCODECS_TIMESCALE`

**When to use:** When you need to inspect media file structure, extract metadata, or perform media analysis in browser or Node.js without FFmpeg.

**Dependencies:** None (standalone).

### `@remotion/webcodecs`

Converts media files using WebCodecs and `@remotion/media-parser`. Runs in browser.

**Key exports:** `convertMedia()`, `getAvailableContainers()`, `webcodecsController()`, `canReencodeVideoTrack()`, `canReencodeAudioTrack()`, `canCopyVideoTrack()`, `canCopyAudioTrack()`, `getDefaultAudioCodec()`, `getDefaultVideoCodec()`, `extractFrames()`, `getPartialAudioData()`, `createAudioDecoder()`, `createVideoDecoder()`, `rotateAndResizeVideoFrame()`, `webFsWriter`, `bufferWriter`

**When to use:** Client-side video conversion, transcoding, or frame extraction.

**Dependencies:** `@remotion/media-parser`.

### `@remotion/gif`

Renders synchronized GIF animations in Remotion compositions.

**Key exports:** `<Gif>`, `getGifDurationInSeconds()`, `preloadGif()`

**When to use:** When embedding GIF images that should be synchronized with Remotion's timeline.

**Dependencies:** `remotion`.

### `@remotion/captions`

Common operations for working with subtitles and captions.

**Key exports:** `Caption` (type), `parseSrt()`, `serializeSrt()`, `createTikTokStyleCaptions()`

**When to use:** Subtitle parsing, serialization, and TikTok-style caption generation.

**Dependencies:** None.

### `@remotion/preload`

Preloads media assets (video, audio, images, fonts) using HTML `<link rel="preload">` for use with the `<Player>`.

**Key exports:** `preloadVideo()`, `preloadAudio()`, `preloadFont()`, `preloadImage()`, `resolveRedirect()`

**When to use:** When using `<Player>` and you want to hint the browser to start loading assets early, before they appear in the timeline.

**Dependencies:** None.

## Cloud Rendering

### `@remotion/lambda`

Renders videos and stills on AWS Lambda. Distributes rendering across multiple Lambda invocations for parallelism, stores assets in S3.

**Key exports:** `renderMediaOnLambda()`, `renderStillOnLambda()`, `getRenderProgress()`, `deployFunction()`, `deleteFunction()`, `deploySite()`, `deleteSite()`, `getSites()`, `getFunctions()`, `getOrCreateBucket()`, `estimatePrice()`, `presignUrl()`, `downloadMedia()`, `getRegions()`, `getUserPolicy()`, `getRolePolicy()`, `simulatePermissions()`, `speculateFunctionName()`, `validateWebhookSignature()`, `appRouterWebhook()`, `pagesRouterWebhook()`, `expressWebhook()`

**When to use:** Serverless video rendering on AWS at scale.

**Dependencies:** `remotion`, `@remotion/renderer`, AWS SDK.

### `@remotion/lambda-client`

A lightweight client-only package for triggering Lambda renders without bundling the full `@remotion/lambda` package. Useful for frontend or edge environments.

**Key exports:** Client-side Lambda trigger functions.

**When to use:** When you need to trigger Lambda renders from a frontend or edge function without the full Lambda SDK.

**Dependencies:** Minimal.

### `@remotion/cloudrun`

Renders videos and stills on Google Cloud Platform Cloud Run.

**Key exports:** `renderMediaOnCloudrun()`, `renderStillOnCloudrun()`, `deployService()`, `deleteService()`, `getServices()`, `getServiceInfo()`, `deploySite()`, `deleteSite()`, `getSites()`, `getOrCreateBucket()`, `getRegions()`, `speculateServiceName()`, `testPermissions()`

**When to use:** Serverless video rendering on GCP.

**Dependencies:** `remotion`, `@remotion/renderer`, GCP SDK.

### `@remotion/vercel`

Renders videos inside Vercel Sandbox environments.

**Key exports:** `createSandbox()`, `addBundleToSandbox()`, `renderMediaOnVercel()`, `renderStillOnVercel()`, `uploadToVercelBlob()`

**When to use:** When deploying render infrastructure on Vercel.

**Dependencies:** `remotion`.

### `@remotion/serverless` / `@remotion/serverless-client`

Shared infrastructure for serverless rendering implementations. Used internally by `@remotion/lambda` and `@remotion/cloudrun`.

**Key exports:** Internal serverless orchestration utilities.

**When to use:** Not typically used directly. Used by cloud rendering packages.

**Dependencies:** `remotion`.

## Utilities

### `@remotion/animation-utils`

CSS animation helpers.

**Key exports:** `makeTransform()`, `interpolateStyles()`

**When to use:** When building CSS `transform` strings or interpolating between CSS style objects.

**Dependencies:** `remotion`.

### `@remotion/paths`

SVG path manipulation and analysis.

**Key exports:** `getLength()`, `cutPath()`, `getPointAtLength()`, `getTangentAtLength()`, `reversePath()`, `normalizePath()`, `interpolatePath()`, `evolvePath()`, `translatePath()`, `warpPath()`, `scalePath()`, `getBoundingBox()`, `resetPath()`, `extendViewBox()`, `getSubpaths()`, `parsePath()`, `serializeInstructions()`, `reduceInstructions()`

**When to use:** SVG path animations, morphing, drawing, and analysis.

**Dependencies:** None.

### `@remotion/shapes`

Generate SVG shape paths and render them as components.

**Key exports:** `<Arrow>`, `<Rect>`, `<Circle>`, `<Heart>`, `<Pie>`, `<Ellipse>`, `<Triangle>`, `<Star>`, `<Polygon>`, and corresponding `make*()` path generators.

**When to use:** When you need geometric shapes as SVG paths or React components.

**Dependencies:** `@remotion/paths`.

### `@remotion/noise`

Deterministic noise generation for procedural visuals.

**Key exports:** `noise2D()`, `noise3D()`, `noise4D()`

**When to use:** Procedural animations, particle effects, organic motion.

**Dependencies:** None.

### `@remotion/layout-utils`

Text measurement and layout helpers.

**Key exports:** `measureText()`, `fillTextBox()`, `fitText()`, `fitTextOnNLines()`

**When to use:** Dynamic text sizing, computing line breaks, fitting text to containers.

**Dependencies:** None.

### `@remotion/motion-blur`

Motion blur effects.

**Key exports:** `<Trail>`, `<CameraMotionBlur>`

**When to use:** Adding motion blur to fast-moving elements.

**Dependencies:** `remotion`.

### `@remotion/transitions`

Scene transition effects.

**Key exports:** `<TransitionSeries>`, `springTiming()`, `linearTiming()`, presentation effects: `fade()`, `slide()`, `wipe()`, `flip()`, `clockWipe()`, `iris()`, `cube()`, `none()`

**When to use:** Transitioning between scenes with visual effects.

**Dependencies:** `remotion`.

### `@remotion/zod-types`

Zod schema types that enable visual editing in Remotion Studio. Based on Zod v4 (since v4.0.426).

**Key exports:** `zColor()`, `zTextarea()`, `zMatrix()`

**When to use:** When defining prop schemas for visual editing in Studio. `zColor()` renders a color picker, `zTextarea()` renders a multi-line text input, `zMatrix()` renders a matrix editor.

**Dependencies:** `zod` (v4).

### `@remotion/zod-types-v3`

Same as `@remotion/zod-types` but for projects that must stay on Zod v3.22.3.

**Key exports:** Same as `@remotion/zod-types`.

**When to use:** When staying on Zod 3.

**Dependencies:** `zod` (v3).

### `@remotion/fonts`

Load font files (local or remote) onto a page.

**Key exports:** `loadFont()`

**When to use:** Loading custom font files (`.woff2`, `.ttf`, etc.) from URLs or local files.

**Dependencies:** None.

### `@remotion/google-fonts`

Load Google Fonts.

**Key exports:** `loadFont()`, `getAvailableFonts()`, `getInfo()`, `loadFontFromInfo()`

**When to use:** Using Google Fonts in compositions.

**Dependencies:** None.

## Integrations

### `@remotion/three`

Integrate React Three Fiber for 3D scenes.

**Key exports:** `<ThreeCanvas>`, `useVideoTexture()`, `useOffthreadVideoTexture()`

**When to use:** 3D video content using Three.js.

**Dependencies:** `remotion`, `@react-three/fiber`, `three`.

### `@remotion/skia`

React Native Skia integration for low-level graphics.

**Key exports:** `enableSkia()`, `<SkiaCanvas>`

**When to use:** High-performance 2D graphics using Skia.

**Dependencies:** `remotion`, `@shopify/react-native-skia`.

### `@remotion/lottie`

Embed Lottie animations.

**Key exports:** `<Lottie>`, `getLottieMetadata()`

**When to use:** Including Lottie/Bodymovin animations in compositions.

**Dependencies:** `remotion`, `lottie-web`.

### `@remotion/rive`

Embed Rive animations.

**Key exports:** `<RemotionRiveCanvas>`

**When to use:** Including Rive animations in compositions.

**Dependencies:** `remotion`, `@rive-app/canvas`.

### `@remotion/tailwind`

Webpack override to enable TailwindCSS v3.

**Key exports:** `enableTailwind()`

**When to use:** Using TailwindCSS v3 in Remotion projects.

**Dependencies:** `tailwindcss` (v3).

### `@remotion/tailwind-v4`

Webpack override to enable TailwindCSS v4.

**Key exports:** `enableTailwind()`

**When to use:** Using TailwindCSS v4 in Remotion projects.

**Dependencies:** `tailwindcss` (v4).

### `@remotion/enable-scss`

Webpack override for SASS/SCSS.

**Key exports:** `enableScss()`

**When to use:** Using SCSS stylesheets in Remotion projects.

**Dependencies:** `sass`.

### `@remotion/animated-emoji`

Google Fonts Animated Emojis as components.

**Key exports:** `<AnimatedEmoji>`, `getAvailableEmoji()`

**When to use:** Displaying animated emoji in compositions.

**Dependencies:** `remotion`.

### `@remotion/sfx`

Built-in sound effects library.

**Key exports:** `whip`, `whoosh`, `pageTurn`, `uiSwitch`, `mouseClick`, `shutterModern`, `shutterOld`, `ding`, `bruh`, `vineBoom`, `windowsXpError`

**When to use:** Quick access to common sound effects without sourcing your own audio files.

**Dependencies:** `remotion`.

### `@remotion/light-leaks`

Light leak visual effects.

**Key exports:** `<LightLeak>`

**When to use:** Adding cinematic light leak overlays.

**Dependencies:** `remotion`.

### `@remotion/starburst`

Starburst ray visual effect.

**Key exports:** `<Starburst>`

**When to use:** Adding starburst/ray effects.

**Dependencies:** `remotion`.

### `@remotion/install-whisper-cpp`

Install and run Whisper.cpp for local audio transcription.

**Key exports:** `installWhisperCpp()`, `downloadWhisperModel()`, `transcribe()`, `toCaptions()`

**When to use:** Automated captioning using local Whisper models.

**Dependencies:** System C++ compiler.

### `@remotion/openai-whisper`

Convert OpenAI Whisper API transcription output to Remotion caption format.

**Key exports:** `openAiWhisperApiToCaptions()`

**When to use:** When using OpenAI's Whisper API for transcription and converting results to `Caption` objects.

**Dependencies:** None.

### `@remotion/licensing`

Report and query company license usage.

**Key exports:** `registerUsageEvent()`, `getUsage()`

**When to use:** Tracking render usage for commercial licensing.

**Dependencies:** None.

### `@remotion/convert`

> **Gap:** No dedicated documentation found in the source docs. This package exists in the repository but its public API is not documented in the reviewed files.

### `@remotion/mcp`

> **Gap:** No dedicated documentation found in the source docs. This package provides Model Context Protocol integration but its API is not documented in the reviewed files.

### `@remotion/streaming`

> **Gap:** No dedicated documentation found in the source docs. This package exists in the repository but its public API is not documented in the reviewed files.

---

## 3. Composition & Component Model

## Defining Compositions

A composition is registered using the `<Composition>` component inside the root component (registered via `registerRoot()`). Each composition defines a renderable unit that appears in the Studio sidebar and can be rendered via CLI or API.

```tsx
import {Composition} from 'remotion';
import {MyComponent} from './MyComponent';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="my-video"
        component={MyComponent}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: 'Hello World',
        }}
      />
    </>
  );
};
```

### `<Composition>` Props

| Prop | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | Yes | Unique identifier. Only letters, numbers, and `-`. Used for rendering and sidebar display. |
| `component` | `React.ComponentType` | Yes (or `lazyComponent`) | The React component to render. |
| `lazyComponent` | `() => Promise<{default: React.ComponentType}>` | Yes (or `component`) | Dynamic import for code splitting. Requires default export. |
| `width` | `number` | Yes | Width in pixels. |
| `height` | `number` | Yes | Height in pixels. |
| `fps` | `number` | Yes | Frames per second. |
| `durationInFrames` | `number` | Yes | Total number of frames. |
| `defaultProps` | `object` | No | Default props for the component. Must be JSON-serializable (with `Date`, `Map`, `Set`, `staticFile()` exceptions). |
| `schema` | `ZodType` | No | Zod schema for props validation and visual editing in Studio. |
| `calculateMetadata` | `CalculateMetadataFunction` | No | Callback to dynamically set metadata and transform props. |

### `<Still>` Component

A `<Still>` is a single-frame `<Composition>`. It does not require `durationInFrames` or `fps`:

```tsx
<Still id="my-thumbnail" component={MyComp} width={1080} height={1080} />
```

### `<Folder>` Component

Organizes compositions in the Studio sidebar. Purely visual, no rendering effect:

```tsx
<Folder name="Marketing">
  <Composition id="ad-1" ... />
  <Composition id="ad-2" ... />
</Folder>
```

## Input Props: Schema and Validation

Props can be typed using a Zod schema passed to `<Composition schema={...}>`. This enables:

- Runtime validation of props
- Visual editing UI in Remotion Studio (color pickers for `zColor()`, textareas for `zTextarea()`, etc.)
- Type-safe prop resolution

```tsx
import {z} from 'zod';
import {zColor} from '@remotion/zod-types';

const mySchema = z.object({
  title: z.string(),
  color: zColor(),
  fontSize: z.number().min(10).max(200),
});

<Composition
  id="my-comp"
  schema={mySchema}
  defaultProps={{title: 'Hello', color: '#ff0000', fontSize: 48}}
  ...
/>
```

**Restrictions on props:**
- Must be pure JSON-serializable objects (no functions, classes, or non-serializable values).
- Exception: `Date`, `Map`, `Set`, and `staticFile()` return values are supported.
- Functions are allowed when using `<Player>` but not during rendering.
- Use `type` (not `interface`) for TypeScript prop definitions.
- Avoid huge objects in `defaultProps` as they can cause performance issues.

## Component Lifecycle During Rendering

During rendering, **each frame is a separate, independent React render**. The renderer:

1. Sets the frame number on the page.
2. React re-renders the entire component tree for that frame.
3. Waits for all `delayRender()` handles to be cleared.
4. Takes a screenshot.

This means:
- `useState` state does not persist across frames (each frame starts fresh).
- Side effects in `useEffect` run once per frame render.
- All animation must be derived from `useCurrentFrame()`, not from accumulated state.
- `Math.random()` will produce different values across render threads -- use `random(seed)` instead.

## `useCurrentFrame()`

```ts
function useCurrentFrame(): number
```

Returns the current frame number (0-indexed). Inside a `<Sequence from={N}>`, returns the frame relative to that sequence's start.

```tsx
import {useCurrentFrame} from 'remotion';

const MyComponent = () => {
  const frame = useCurrentFrame(); // 0 at start, increments each frame
  return <div style={{opacity: frame / 30}}>Fading in...</div>;
};
```

**Behavior inside Sequences:** If the timeline is at frame 25 and a component is inside `<Sequence from={10}>`, `useCurrentFrame()` returns `15`.

## `useVideoConfig()`

```ts
function useVideoConfig(): VideoConfig
```

Returns an object describing the current composition:

| Property | Type | Description |
|---|---|---|
| `width` | `number` | Composition width in pixels (or `<Sequence>` width if overridden). |
| `height` | `number` | Composition height in pixels (or `<Sequence>` height if overridden). |
| `fps` | `number` | Frames per second. |
| `durationInFrames` | `number` | Duration (of the composition, or of the containing `<Sequence>`). |
| `id` | `string` | Composition ID. |
| `defaultProps` | `object` | The `defaultProps` from the `<Composition>`. |
| `props` | `object` | Resolved props after all transformations (v4.0.0+). |
| `defaultCodec` | `Codec \| null` | Default codec for the composition (v4.0.54+). |

## `interpolate()`

```ts
function interpolate(
  input: number,
  inputRange: number[],
  outputRange: number[],
  options?: InterpolateOptions
): number
```

Maps a value from one range to another. The primary animation utility.

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `number` | -- | The input value (typically the current frame). |
| `inputRange` | `number[]` | -- | Monotonically increasing input breakpoints. |
| `outputRange` | `number[]` | -- | Corresponding output values. Must be same length as `inputRange`. |
| `options` | `InterpolateOptions` | `{}` | See below. |

### Options

| Option | Type | Default | Description |
|---|---|---|---|
| `extrapolateLeft` | `'extend' \| 'clamp' \| 'wrap' \| 'identity'` | `'extend'` | Behavior when input is below the first input range value. |
| `extrapolateRight` | `'extend' \| 'clamp' \| 'wrap' \| 'identity'` | `'extend'` | Behavior when input is above the last input range value. |
| `easing` | `(t: number) => number` | `(x) => x` | Easing function applied to the interpolation. |

### Extrapolation Modes

| Mode | Behavior |
|---|---|
| `extend` | Continue interpolating outside the range (default). |
| `clamp` | Clamp to the nearest output range boundary. |
| `wrap` | Loop the value. |
| `identity` | Return the raw input value. |

### Examples

```ts
// Fade in over first 20 frames
const opacity = interpolate(frame, [0, 20], [0, 1]);

// Fade in and out
const opacity = interpolate(
  frame,
  [0, 20, durationInFrames - 20, durationInFrames],
  [0, 1, 1, 0]
);

// With easing and clamping
const scale = interpolate(frame, [0, 30], [0, 1], {
  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
});
```

## `interpolateColors()`

```ts
function interpolateColors(
  input: number,
  inputRange: number[],
  outputColors: string[]
): string
```

Maps a numeric value to a color, interpolating between colors. Returns an `rgba()` string. Supports `rgb`, `rgba`, `hsl`, `hsla`, hex, CSS color names, `oklch`, `oklab`, `lab`, `lch`, and `hwb` color formats.

```ts
const color = interpolateColors(frame, [0, 30], ['red', 'blue']);
// Returns: "rgba(128, 0, 128, 1)" at frame 15
```

## `spring()`

```ts
function spring(options: SpringOptions): number
```

A physics-based animation primitive that animates from `from` to `to` with configurable spring physics.

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `frame` | `number` | -- | Current frame (typically from `useCurrentFrame()`). |
| `fps` | `number` | -- | Frames per second (from `useVideoConfig()`). |
| `from` | `number` | `0` | Start value. |
| `to` | `number` | `1` | End value. |
| `reverse` | `boolean` | `false` | Play in reverse. |
| `config.mass` | `number` | `1` | Weight of the spring. Lower = faster. |
| `config.damping` | `number` | `10` | Deceleration force. Higher = less bounce. |
| `config.stiffness` | `number` | `100` | Spring stiffness. Higher = bouncier. |
| `config.overshootClamping` | `boolean` | `false` | If true, clamp to `to` value (no overshoot). |
| `durationInFrames` | `number` | -- | Stretch animation to exact frame count. |
| `durationRestThreshold` | `number` | -- | Threshold for "finished" when using `durationInFrames`. |
| `delay` | `number` | -- | Delay the animation start by N frames. |

### Example

```ts
const frame = useCurrentFrame();
const {fps} = useVideoConfig();

const scale = spring({
  frame,
  fps,
  config: {damping: 100, stiffness: 200},
});
// Use: style={{transform: `scale(${scale})`}}
```

### `measureSpring()`

```ts
function measureSpring(options: {
  fps: number;
  config?: Partial<SpringConfig>;
  threshold?: number;
  from?: number;
  to?: number;
}): number
```

Returns the number of frames a spring animation takes to settle. Useful for calculating `durationInFrames` of a `<Sequence>` that wraps a spring animation.

## `Easing`

The `Easing` module provides easing functions for use with `interpolate()`.

**Standard functions:** `linear`, `quad`, `cubic`, `poly(n)`

**Predefined animations:** `ease`, `back(s)`, `bounce`, `elastic(bounciness)`

**Additional functions:** `bezier(x1, y1, x2, y2)`, `circle`, `sin`, `exp`

**Modifiers:** `in(easing)`, `out(easing)`, `inOut(easing)`

**Step functions:** `step0(n)`, `step1(n)`

```ts
interpolate(frame, [0, 100], [0, 1], {
  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),
});
```

## Sequences: Composing Segments into a Timeline

### `<Sequence>`

Time-shifts its children so they start at a different point in the composition timeline.

| Prop | Type | Default | Description |
|---|---|---|---|
| `from` | `number` | `0` | Frame at which children start. Negative values trim the beginning. |
| `durationInFrames` | `number` | `Infinity` | How many frames the sequence is visible. Children unmount after. |
| `name` | `string` | -- | Label shown in Studio timeline. |
| `layout` | `'absolute-fill' \| 'none'` | `'absolute-fill'` | Whether to wrap children in an `<AbsoluteFill>`. |
| `style` | `CSSProperties` | -- | CSS styles for the container. |
| `className` | `string` | -- | CSS class for the container. |
| `width` | `number` | -- | Override `useVideoConfig().width` for children. |
| `height` | `number` | -- | Override `useVideoConfig().height` for children. |
| `premountFor` | `number` | `0` (v4), `fps` (v5) | Pre-mount the sequence N frames early. |
| `postmountFor` | `number` | -- | Keep mounted N frames after ending. |
| `showInTimeline` | `boolean` | `true` | Whether to show in Studio timeline. |

**Key behaviors:**
- Children of `<Sequence>` see `useCurrentFrame()` values shifted by `from`. At composition frame 30, inside `<Sequence from={10}>`, `useCurrentFrame()` returns 20.
- Sequences cascade when nested: a sequence starting at 60 inside one starting at 30 effectively starts at 90.
- Negative `from` values trim the start of the child animation.

```tsx
const MyTrailer = () => (
  <>
    <Sequence durationInFrames={30}>
      <Intro />  {/* frames 0-29 */}
    </Sequence>
    <Sequence from={30} durationInFrames={30}>
      <Clip />   {/* frames 30-59 */}
    </Sequence>
    <Sequence from={60}>
      <Outro />  {/* frames 60 to end */}
    </Sequence>
  </>
);
```

### `<Series>` Component

A helper that automatically sequences children one after another without manual `from` calculation.

```tsx
import {Series} from 'remotion';

const MyVideo = () => (
  <Series>
    <Series.Sequence durationInFrames={40}>
      <SceneOne />
    </Series.Sequence>
    <Series.Sequence durationInFrames={20}>
      <SceneTwo />
    </Series.Sequence>
    <Series.Sequence durationInFrames={70}>
      <SceneThree />
    </Series.Sequence>
  </Series>
);
```

`<Series.Sequence>` accepts the following props:

| Prop | Type | Default | Description |
|---|---|---|---|
| `durationInFrames` | `number` | -- | Duration. Only the last can be `Infinity`. |
| `offset` | `number` | `0` | Positive delays, negative overlaps with the previous sequence. |
| `layout` | `'absolute-fill' \| 'none'` | `'absolute-fill'` | Layout mode. |
| `style` | `CSSProperties` | -- | Container styles. |
| `className` | `string` | -- | Container class. |
| `premountFor` | `number` | -- | Pre-mount frames. |

### `<Loop>` Component

Repeats its children for a set number of iterations or infinitely.

| Prop | Type | Default | Description |
|---|---|---|---|
| `durationInFrames` | `number` | -- | Duration of one loop iteration. |
| `times` | `number` | `Infinity` | Number of repetitions. |
| `layout` | `'absolute-fill' \| 'none'` | `'absolute-fill'` | Layout mode. |

Child components can call `Loop.useLoop()` to get `{ durationInFrames, iteration }` or `null` if not in a loop.

### `<Freeze>` Component

Freezes children at a specific frame.

| Prop | Type | Default | Description |
|---|---|---|---|
| `frame` | `number` | -- | The frame at which children freeze. |
| `active` | `boolean \| (frame: number) => boolean` | `true` | When false, freezing is disabled. |

Inside `<Freeze frame={30}>`, `useCurrentFrame()` always returns 30. Video elements pause; audio renders muted.

## How Audio Works

Audio is handled by `<Html5Audio>`, `<Audio>` (`@remotion/media`), and the audio tracks of `<Html5Video>`, `<OffthreadVideo>`, and `<Video>` (`@remotion/media`).

**Volume control:** Set a static volume or a per-frame volume callback:

```tsx
<Html5Audio src={staticFile('music.mp3')} volume={0.5} />

<Html5Audio
  src={staticFile('voice.mp3')}
  volume={(f) => interpolate(f, [0, 30], [0, 1], {extrapolateLeft: 'clamp'})}
/>
```

**Trimming:** Use `trimBefore` and `trimAfter` (frame-based) to trim audio:

```tsx
<Html5Audio src={staticFile('audio.mp3')} trimBefore={60} trimAfter={120} />
// Plays audio from 2s to 4s mark (at 30fps)
```

**Looping:** Pass `loop` prop to `<Html5Audio>` or `<Html5Video>`.

**Playback rate:** Control speed with `playbackRate` (e.g., `2` for double speed).

**Mixing:** During rendering, Remotion extracts audio from all media elements and mixes them into the final output file via FFmpeg. Multiple audio sources are mixed together.

**Tone frequency:** Adjust pitch during rendering with `toneFrequency` (0.01 to 2, where 1 is original pitch).

## How Images and Video Clips Are Embedded

### `<Img>`

Wraps HTML `<img>`. Remotion ensures the image is loaded (via `delayRender()`) before screenshotting the frame. Supports `maxRetries` (default 2) with exponential backoff.

```tsx
<Img src={staticFile('photo.png')} />
<Img src="https://example.com/image.jpg" />
```

### `<Html5Video>`

Wraps native `<video>` element, synchronized with Remotion's timeline. During preview, plays in real time. During rendering, frame extraction happens via the browser's video decoder.

### `<OffthreadVideo>`

Alternative to `<Html5Video>` that extracts frames using FFmpeg outside the browser during rendering. During preview it falls back to `<video>`. Displays frames as `<Img>` tags during render. Better for frame accuracy but slightly slower.

- `transparent={true}` extracts frames as PNG (slower, enables transparency).
- `toneMapped={true}` (default since v4.0.117) adjusts HDR colors to sRGB.

### `<AnimatedImage>`

Renders animated GIFs, APNGs, AVIF, and WebP images synchronized with Remotion's timeline. Uses the `ImageDecoder` Web API (Chrome and Firefox only).

### `staticFile()`

References files in the `public/` folder with a URL that works across preview and rendering:

```ts
const src = staticFile('/video.mp4'); // "/static-32e8nd/video.mp4"
```

Since v4.0, automatically encodes URI-unsafe characters. Always use `staticFile()` instead of raw `/public` paths.

---

## 4. Rendering Pipeline

## Local Rendering

### How Rendering Works Under the Hood

Remotion's rendering pipeline operates through the following stages:

1. **Bundling** — The Remotion project (React components) is bundled into a static Webpack bundle using `@remotion/bundler`. This bundle is a self-contained web application.
2. **Composition Resolution** — A headless Chrome/Chromium instance (Chrome Headless Shell by default since v4.0.248) loads the bundle and evaluates the Remotion Root to discover available compositions and their metadata (dimensions, fps, duration).
3. **Frame Rendering** — For each frame in the composition, the browser navigates to that frame number. Remotion waits for all `delayRender()` calls to resolve, then takes a screenshot of the page. Multiple browser tabs run in parallel according to the `concurrency` setting.
4. **Encoding** — Frame images are piped to FFmpeg, which encodes them into the final video container. If sufficient CPU and memory are available, Remotion uses "parallel encoding" — rendering frames and encoding happen simultaneously. Otherwise, all frames are rendered first, then stitched.
5. **Audio Mixing** — Audio from `<Audio>` and `<Video>` elements is downloaded, decoded, and mixed into the final output via FFmpeg.

The `renderMedia()` API combines steps 3 and 4 into one optimized call. The lower-level `renderFrames()` + `stitchFramesToVideo()` approach splits them for advanced use cases like distributed rendering.

### Concurrency Model

Remotion spawns multiple browser tabs (not processes) to render frames in parallel. The `--concurrency` flag (CLI) or `concurrency` option (API) controls how many tabs operate simultaneously.

- **Default**: Half of the available CPU threads.
- **Number**: Exact count of parallel render processes (e.g., `--concurrency=4`).
- **Percentage string**: Percentage of CPU threads (e.g., `"50%"`).
- **`null`**: Let Remotion decide automatically.

Higher concurrency speeds up rendering but increases memory usage. Each tab holds a full browser rendering context.

### Output Formats

| Format | Codec Flag | Container | Video Codec | Notes |
|--------|-----------|-----------|-------------|-------|
| MP4 (H.264) | `h264` | .mp4 | H.264 | Default. Widest compatibility. |
| MP4 (H.265) | `h265` | .mp4 | H.265/HEVC | Better compression, less compatibility. |
| WebM (VP8) | `vp8` | .webm | VP8 | Web-friendly, open format. |
| WebM (VP9) | `vp9` | .webm | VP9 | Better compression than VP8. |
| ProRes | `prores` | .mov | Apple ProRes | Professional editing workflows. Profiles: `4444-xq`, `4444`, `hq`, `standard`, `light`, `proxy`. |
| GIF | (via `.gif` extension) | .gif | N/A | Use `--every-nth-frame` to reduce frame rate. |
| MKV (H.264) | `h264-mkv` | .mkv | H.264 | Matroska container with H.264. |
| AV1 | `av1` | .webm | AV1 | Not available on Linux ARM64 GNU. |
| PNG sequence | `png` | directory | N/A | Image sequence output. |
| Audio-only | `mp3`, `aac`, `wav` | .mp3/.aac/.wav | N/A | Audio-only output. |

### Audio Codec Options

| Audio Codec | Compatible Video Codecs | Notes |
|-------------|------------------------|-------|
| `aac` | h264, h265, prores | Default for MP4 containers. |
| `opus` | vp8, vp9, av1 | Default for WebM containers. |
| `mp3` | h264-mkv | MP3 audio in MKV container. |
| `pcm-16` | Various | Uncompressed audio. |

### Performance Characteristics

- **Parallel encoding**: When CPU and memory allow, frame rendering and video encoding happen concurrently. Disable with `--disallow-parallel-encoding` to reduce memory usage at the cost of speed.
- **Hardware acceleration** (v4.0.228+): Set `--hardware-acceleration=if-possible` or `required` to use GPU-accelerated encoding. When enabled, `crf` cannot be used — use `--video-bitrate` instead.
- **Bundle caching**: Enabled by default. Reuses the Webpack bundle between renders unless source files change.
- **Browser reuse**: In the Node.js API, pass a `puppeteerInstance` (from `openBrowser()`) across multiple render calls to avoid browser startup overhead.

---

## `npx remotion render` — CLI

Render a video or audio based on the entry point and composition ID.

```
npx remotion render <entry-point|serve-url>? <composition-id> <output-location>
```

- If `composition-id` is omitted, Remotion prompts for selection.
- If `output-location` is omitted, output goes to the `out` folder.

### All Flags

| Flag | Since | Description |
|------|-------|-------------|
| `--props` | v1.0 | Input props as JSON string (`'{"key":"value"}'`) or path to JSON file. |
| `--height` | v3.2.40 | Override composition height. |
| `--width` | v3.2.40 | Override composition width. |
| `--fps` | v4.0.424 | Override composition frame rate. |
| `--duration` | v4.0.424 | Override composition duration. |
| `--concurrency` | v1.0 | Number of parallel render processes, percentage string, or `null`. Default: half CPU threads. |
| `--pixel-format` | v1.0 | Pixel format for output (e.g., `yuv420p`, `yuva420p` for transparency). |
| `--image-format` | v1.4.0 | Frame format: `jpeg` (default, fastest) or `png` (supports transparency) or `none` (audio only). |
| `--image-sequence-pattern` | v4.0.313 | Pattern for naming image sequence files. Supports `[frame]` and `[ext]` placeholders. |
| `--config` | v1.2.0 | Path to `remotion.config.ts` file. |
| `--env-file` | v2.2.0 | Path to `.env` file for environment variables. |
| `--jpeg-quality` | v4.0.0 | JPEG quality 0-100. Only applies when `--image-format=jpeg`. |
| `--output` | v4.0.0 | Alternative to positional `output-location` argument. |
| `--overwrite` | v1.0 | Overwrite existing output. Default: `true`. Use `--overwrite=false` to disable. |
| `--sequence` | v1.4.0 | Render as image sequence instead of video. |
| `--codec` | v1.4.0 | `h264`, `h265`, `av1`, `png`, `vp8`, `vp9`, `mp3`, `aac`, `wav`, `prores`, `h264-mkv`. Default: `h264`. |
| `--audio-codec` | v3.3.42 | Audio encoding: `aac`, `opus`, `mp3`, `pcm-16`. |
| `--audio-bitrate` | v3.2.32 | Target audio bitrate (e.g., `320k`, `512K`, `1M`). Default: `320k`. |
| `--video-bitrate` | v3.2.32 | Target video bitrate (e.g., `512K`, `1M`). |
| `--buffer-size` | v4.0.78 | Buffer size for rate control. |
| `--max-rate` | v4.0.78 | Maximum bitrate for rate control. |
| `--prores-profile` | v2.1.6 | ProRes profile: `4444-xq`, `4444`, `hq`, `standard`, `light`, `proxy`. |
| `--x264-preset` | v4.2.2 | x264 encoding preset. |
| `--crf` | v1.4.0 | Constant Rate Factor for quality control. Cannot be used with hardware acceleration. |
| `--browser-executable` | v1.5.0 | Absolute path to browser executable. |
| `--chrome-mode` | v4.0.248 | `headless-shell` (default) or `chrome-for-testing`. |
| `--scale` | v1.0 | Scale output dimensions by factor (0 < scale <= 16). Default: `1`. |
| `--frames` | v2.0.0 | Render specific frame or range (e.g., `0-99`, `50`). |
| `--every-nth-frame` | v3.1.0 | Render only every Nth frame. GIF only. |
| `--muted` | v3.2.1 | Disable audio output. |
| `--enforce-audio-track` | v3.2.1 | Render silent audio track if none exists. |
| `--disallow-parallel-encoding` | v4.0.315 | Disable simultaneous rendering and encoding. More memory-efficient but slower. |
| `--number-of-gif-loops` | v3.1.0 | GIF loop count. `null`=infinite, `0`=no loop, `1`=loop once. |
| `--color-space` | v4.0.28 | Color space: `default`, `bt601`, `bt709`, `bt2020-ncl`, `bt2020-cl`. |
| `--hardware-acceleration` | v4.0.228 | `disable` (default), `if-possible`, or `required`. |
| `--bundle-cache` | v2.0.0 | Enable/disable Webpack bundle caching. Default: `true`. |
| `--log` | v1.0 | Log level: `error`, `warn`, `info` (default), `verbose`. |
| `--port` | v1.0 | Prefer specific port for serving the project. |
| `--public-dir` | v3.2.13 | Location of the `public/` directory. |
| `--timeout` | v1.0 | Milliseconds before a frame times out on `delayRender()`. Default: `30000`. |
| `--ignore-certificate-errors` | v2.6.5 | Ignore invalid SSL certificates. |
| `--disable-web-security` | v2.6.5 | Disable CORS and other web security features. |
| `--dark-mode` | v4.0.381 | Emulate `prefers-color-scheme: dark`. Default: `false`. |
| `--gl` | v1.0 | OpenGL renderer: `angle`, `egl`, `swiftshader`, `swangle`, `vulkan` (v4.0.41+), `angle-egl` (v4.0.51+). |
| `--user-agent` | v3.3.83 | Custom user agent string. |
| `--media-cache-size-in-bytes` | v4.0.352 | Max cache size for `<Video>` and `<Audio>` from `@remotion/media`. |
| `--offthreadvideo-cache-size-in-bytes` | v4.0.23 | Cache size for `<OffthreadVideo>` frames. Default: half system memory. |
| `--offthreadvideo-video-threads` | v4.0.261 | Number of threads for OffthreadVideo decoding. |
| `--enable-multiprocess-on-linux` | v4.0.42 | Remove `--single-process` flag from Chromium on Linux. Default: `true` from v4.0.137. |
| `--repro` | v4.0.88 | Create a reproduction bundle for debugging. |
| `--binaries-directory` | v4.0.120 | Path to platform-specific binaries (ffmpeg, Rust binary, shared libraries). |
| `--experimental-rspack` | v4.0.426 | Use Rspack instead of Webpack as bundler. |
| `--for-seamless-aac-concatenation` | v4.0.123 | Prepare output for seamless AAC concatenation. |
| `--separate-audio-to` | v4.0.123 | Write audio to a separate file path. |
| `--metadata` | v4.0.216 | Metadata to embed in the video. |

---

## `npx remotion still` — CLI

Render a single still frame.

```
npx remotion still <serve-url|entry-point>? [<composition-id>] [<output-location>]
```

Available since v2.3.

### All Flags

| Flag | Since | Description |
|------|-------|-------------|
| `--props` | v2.3 | Input props as JSON string or path to JSON file. |
| `--image-format` | v2.3 | Output format: `png` (default), `jpeg`, `webp`, `pdf`. |
| `--config` | v2.3 | Path to config file. |
| `--env-file` | v2.3 | Path to `.env` file. |
| `--jpeg-quality` | v4.0.0 | JPEG quality 0-100. |
| `--output` | v4.0.0 | Output file path (alternative to positional argument). |
| `--overwrite` | v2.3 | Overwrite existing file. Default: `true`. |
| `--browser-executable` | v2.3 | Path to browser executable. |
| `--scale` | v2.3 | Scale factor (0 < scale <= 16). Default: `1`. |
| `--frame` | v2.3 | Frame number to render. Default: `0`. Negative values allowed (v3.2.27+). |
| `--bundle-cache` | v2.3 | Enable/disable bundle caching. |
| `--log` | v2.3 | Log level: `error`, `warn`, `info`, `verbose`. |
| `--port` | v2.3 | Preferred port. |
| `--public-dir` | v3.2.13 | Public directory location. |
| `--timeout` | v2.3 | Frame timeout in ms. Default: `30000`. |
| `--ignore-certificate-errors` | v2.6.5 | Ignore SSL errors. |
| `--disable-web-security` | v2.6.5 | Disable CORS. |
| `--dark-mode` | v4.0.381 | Emulate dark mode. |
| `--chrome-mode` | v4.0.248 | `headless-shell` or `chrome-for-testing`. |
| `--gl` | v2.3 | OpenGL renderer backend. |
| `--user-agent` | v3.3.83 | Custom user agent. |
| `--media-cache-size-in-bytes` | v4.0.352 | Media cache size. |
| `--offthreadvideo-cache-size-in-bytes` | v4.0.23 | OffthreadVideo cache size. |
| `--offthreadvideo-video-threads` | v4.0.261 | OffthreadVideo threads. |
| `--enable-multiprocess-on-linux` | v4.0.42 | Multi-process on Linux. |
| `--binaries-directory` | v4.0.120 | Binaries directory path. |
| `--experimental-rspack` | v4.0.426 | Use Rspack bundler. |

---

## WebCodecs Rendering

### Overview — `@remotion/webcodecs`

Available since v4.0.229. The `@remotion/webcodecs` package provides browser-based video conversion using the WebCodecs API, which has full GPU acceleration access. Unlike the standard rendering pipeline (which requires Node.js, a headless browser, and FFmpeg), WebCodecs runs entirely in the browser.

**Key differences from standard pipeline:**
- Runs in the browser, no server infrastructure needed.
- Uses native WebCodecs API with GPU acceleration — significantly faster than WebAssembly-based solutions.
- Designed for media conversion (re-encoding existing files), not for rendering Remotion compositions to video.
- Supports containers: `mp4`, `webm`, `wav`.
- Supports video codecs: `h264`, `h265`, `vp8`, `vp9`.
- Supports audio codecs: `opus`.

**Limitations:**
- Browser support required (Chrome 94+, Edge 94+; no Firefox/Safari as of writing).
- Cannot render Remotion compositions — only converts existing media files.
- The API is marked as unstable and may change.
- Being phased out in favor of "Mediabunny."

### `convertMedia()` API

Re-encodes a video using WebCodecs and `@remotion/media-parser`.

```ts
import { convertMedia } from "@remotion/webcodecs";

const result = await convertMedia({
  src: "https://example.com/video.mp4",
  container: "webm",
  videoCodec: "vp8",
  audioCodec: "opus",
});

const blob = await result.save();
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `src` | `string \| File \| Blob` | Yes | URL, File/Blob, or local file path. |
| `container` | `"mp4" \| "webm" \| "wav"` | Yes | Output container format. |
| `videoCodec` | `"h264" \| "h265" \| "vp8" \| "vp9"` | No | Video codec. Default per `getDefaultVideoCodec()`. |
| `audioCodec` | `"opus"` | No | Audio codec. Default per `getDefaultAudioCodec()`. |
| `expectedDurationInSeconds` | `number` | No | Helps estimate MP4 metadata size. Default allocates 2MB for metadata. |
| `expectedFrameRate` | `number` | No | Helps estimate MP4 metadata size. Default: `60`. |
| `controller` | `WebCodecsController` | No | Allows pause, resume, abort of conversion. |
| `reader` | `ReaderInterface` | No | Reader interface. Default: `webReader` (URLs and File objects). Use `nodeReader` for local files. |
| `writer` | `WriterInterface` | No | Writer interface. Default: `webFsWriter`. Alternative: `bufferWriter`. |
| `rotate` | `number` | No | Degrees to rotate the video. |
| `resize` | `ResizeOperation` | No | Resize the video dimensions. |
| `logLevel` | `"error" \| "warn" \| "info" \| "debug" \| "trace"` | No | Log level. Default: `"info"`. |
| `onProgress` | `ConvertMediaOnProgress` | No | Progress callback with `decodedVideoFrames`, `encodedVideoFrames`, `bytesWritten`, `overallProgress`, etc. |
| `onVideoFrame` | `ConvertMediaOnVideoFrame` | No | Hook into video frames for manipulation. Receives/returns `VideoFrame`. |
| `onAudioData` | `ConvertMediaOnAudioData` | No | Hook into audio data for manipulation. Receives/returns `AudioData`. |
| `onVideoTrack` | `ConvertMediaOnVideoTrackHandler` | No | Control per-track handling: re-encode, copy, or drop. |
| `onAudioTrack` | `ConvertMediaOnAudioTrackHandler` | No | Control per-track handling: re-encode, copy, or drop. |
| `selectM3uStream` | `SelectM3uStreamFn` | No | Callback for `.m3u8` stream selection. |
| `progressIntervalInMs` | `number` | No | Progress callback interval in ms. Default: `100`. `0` for unthrottled. |
| `seekingHints` | `object` | No | Hints about media file structure for optimized seeking. |
| `fields` | `object` | No | Request metadata fields from the source file (inherited from `parseMedia()`). |

#### Return Value

`ConvertMediaResult` object:
- `save()` — Returns `Promise<Blob>` with the converted video.
- `remove()` — Cleans up temporary resources.
- `finalState` — `ConvertMediaProgress` object with final conversion statistics.

---

## 5. Input Props & Dynamic Content

## Props Schema Definition and Validation

Define a Zod schema and pass it to `<Composition schema={...}>`:

```tsx
import {z} from 'zod';
import {zColor} from '@remotion/zod-types';

const schema = z.object({
  title: z.string(),
  backgroundColor: zColor(),
  items: z.array(z.object({
    label: z.string(),
    value: z.number(),
  })),
});

<Composition
  id="my-comp"
  schema={schema}
  defaultProps={{
    title: 'Default Title',
    backgroundColor: '#ffffff',
    items: [{label: 'Item 1', value: 42}],
  }}
  component={MyComponent}
  ...
/>
```

The schema enables:
- Validation of default props and input props
- A visual editing UI in Remotion Studio (the Props Editor / Data Sidebar)
- `zColor()` renders a color picker
- `zTextarea()` renders a multi-line text editor
- `zMatrix()` renders a matrix editor

## Passing Props at Render Time

### CLI `--props`

```bash
# Inline JSON
npx remotion render MyComp --props='{"title": "Custom Title"}'

# From a file
npx remotion render MyComp --props=./path/to/props.json
```

### Node.js API `inputProps`

```ts
await renderMedia({
  composition,
  serveUrl: bundleLocation,
  codec: 'h264',
  outputLocation: 'out/video.mp4',
  inputProps: {
    title: 'Custom Title',
    backgroundColor: '#ff0000',
  },
});
```

### Lambda API

```ts
await renderMediaOnLambda({
  ...config,
  inputProps: {title: 'Custom Title'},
});
```

### Props Resolution Order

1. `defaultProps` from `<Composition>` (lowest priority)
2. Props edited in Studio Data Sidebar
3. `inputProps` passed via CLI `--props` or API (highest priority)
4. `calculateMetadata()` can further transform resolved props

### `getInputProps()`

Retrieves input props in the root component. Returns an untyped object. Prefer accessing props through component props or `calculateMetadata()` for type safety.

```ts
import {getInputProps} from 'remotion';
const props = getInputProps(); // {title: "Custom Title"}
```

Returns `{}` in Node.js, Bun, serverless functions, Player, and client-side rendering contexts.

## `calculateMetadata()` for Dynamic Composition Configuration

The `calculateMetadata` prop on `<Composition>` runs once before rendering starts, allowing you to:
- Dynamically set `durationInFrames`, `width`, `height`, `fps`
- Transform props (e.g., fetch data and merge it in)
- Set per-composition default codec, image format, pixel format, ProRes profile

```tsx
const calculateMetadata: CalculateMetadataFunction<MyProps> = async ({
  props,
  defaultProps,
  abortSignal,
  compositionId,
  isRendering,
}) => {
  const data = await fetch('https://api.example.com/data', {signal: abortSignal});
  const json = await data.json();

  return {
    durationInFrames: json.scenes.length * 150,
    props: {
      ...props,
      apiData: json,
    },
    defaultCodec: 'h264',
  };
};
```

### Callback Arguments

| Argument | Type | Description |
|---|---|---|
| `defaultProps` | `object` | The raw default props from `<Composition>`. |
| `props` | `object` | Resolved props (default + input). |
| `abortSignal` | `AbortSignal` | Abort signal for canceling stale requests in Studio. |
| `compositionId` | `string` | The composition ID (v4.0.98+). |
| `isRendering` | `boolean` | `true` during rendering, `false` in Studio (v4.0.342+). |

### Return Value

| Field | Type | Description |
|---|---|---|
| `props` | `object` | Transformed props. Must match schema shape. |
| `durationInFrames` | `number` | Override duration. |
| `width` | `number` | Override width. |
| `height` | `number` | Override height. |
| `fps` | `number` | Override FPS. |
| `defaultCodec` | `Codec` | Per-composition default codec. |
| `defaultOutName` | `string` | Default output filename (without extension) (v4.0.268+). |
| `defaultVideoImageFormat` | `'png' \| 'jpeg' \| 'none'` | Default image format (v4.0.316+). |
| `defaultPixelFormat` | `string` | Default pixel format (v4.0.316+). |
| `defaultProResProfile` | `string` | Default ProRes profile (v4.0.367+). |

## `delayRender()` / `continueRender()` for Async Data Fetching

`delayRender()` pauses the render for the current frame, allowing async operations to complete before the screenshot is taken. It is a no-op in the Studio and Player.

```tsx
import {useEffect, useState} from 'react';
import {useDelayRender} from 'remotion';

const MyComp = () => {
  const [data, setData] = useState(null);
  const {delayRender, continueRender, cancelRender} = useDelayRender();
  const [handle] = useState(() => delayRender('Fetching data...'));

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        continueRender(handle);
      })
      .catch((err) => {
        cancelRender(err);
      });
  }, []);

  if (!data) return null;
  return <div>{data.title}</div>;
};
```

### Key Rules

- Must call `continueRender(handle)` within 30 seconds (configurable) or the render times out.
- Multiple `delayRender()` calls are allowed; rendering is blocked until all handles are cleared.
- Always use `useDelayRender()` hook (preferred) instead of importing global `delayRender`/`continueRender`.
- Keep `delayRender()` calls inside components (not top-level) to avoid blocking other compositions.
- Use `cancelRender(error)` to abort when async operations fail.

### Options

| Option | Type | Default | Description |
|---|---|---|---|
| `retries` | `number` | `0` | Number of retries if the handle times out. Tab is closed and frame re-rendered. |
| `timeoutInMilliseconds` | `number` | `30000` | Per-handle timeout override. |

### `calculateMetadata()` vs `delayRender()`

Prefer `calculateMetadata()` for data fetching when possible:
- Runs once (not once per concurrent render tab).
- No manual `continueRender()`/`cancelRender()` needed.
- Returns transformed props to the component directly.

Use `delayRender()` when data must be fetched per-frame or depends on frame-specific context.

## Dynamic Images, Fonts, and Media Loading

**Images:** Use `<Img>` (which wraps `delayRender()`) to ensure images load before the frame is captured:

```tsx
<Img src={dynamicImageUrl} />
```

**Fonts:** Load fonts dynamically using `@remotion/fonts` or `@remotion/google-fonts`:

```ts
import {loadFont} from '@remotion/google-fonts/Roboto';
const {fontFamily} = loadFont();
```

Or load a custom font:

```ts
import {loadFont} from '@remotion/fonts';
const {fontFamily} = loadFont({
  family: 'MyFont',
  url: staticFile('MyFont.woff2'),
});
```

Both methods work with `delayRender()` internally to ensure the font is loaded before rendering.

**Media:** `<Html5Audio>`, `<Html5Video>`, `<OffthreadVideo>`, and `<Video>` (`@remotion/media`) all handle `delayRender()` internally. Use `staticFile()` for local assets or remote URLs.

**Prefetching:** For the `<Player>`, use `prefetch()` to pre-load assets into memory:

```ts
const {free, waitUntilDone} = prefetch('https://example.com/video.mp4', {
  method: 'blob-url',
});
await waitUntilDone();
```

## Templatization Patterns

Remotion's prop system naturally supports templatization -- the same composition code renders different content per render, driven by input props.

**Pattern:** Define a composition with a rich schema, then trigger renders with different `inputProps`:

```ts
// Render 1
await renderMedia({...config, inputProps: {name: 'Alice', avatar: 'alice.png'}});

// Render 2
await renderMedia({...config, inputProps: {name: 'Bob', avatar: 'bob.png'}});
```

This is the foundation for:
- Personalized video campaigns (different name/avatar per recipient)
- Data-driven video generation (charts, reports from API data)
- Batch rendering with varying content

Use `calculateMetadata()` to fetch per-render data from APIs based on input props.

## Limitations on Prop Size, Complexity, and Serialization

- **JSON-serializable only:** Props must be plain JSON objects. Functions, class instances, Symbols, `undefined` (at top level), and circular references are not supported. Exceptions: `Date`, `Map`, `Set`, and `staticFile()` return values are serialized properly.
- **Performance with large props:** Passing huge objects to `defaultProps` can be slow because they are serialized/deserialized during the render pipeline. Fetch large datasets inside `calculateMetadata()` or within the component using `delayRender()` instead of passing them as props.
- **Serialization boundary:** Props cross a serialization boundary between the Node.js render process and the browser. Any value that cannot survive `JSON.stringify()` / `JSON.parse()` (plus the special-cased types above) will be lost.
- **No `interface` for props:** Use TypeScript `type` (not `interface`) for props when using Zod schemas.

> **Gap:** The exact maximum size of serialized props is not documented. Practically, props should remain small (under a few MB) and large data should be fetched dynamically via `calculateMetadata()` or `delayRender()`.


---

## 6. Asset Handling

### 6.1 Static Assets: `staticFile()` and the `public/` Directory

Remotion serves files from the `public/` directory of your project. Reference them at runtime with `staticFile()`:

```tsx
import {staticFile} from 'remotion';

const videoUrl = staticFile('video.webm');  // resolves to /public/video.webm at runtime
const imageUrl = staticFile('hero.png');
```

**Key rules:**

- Files in `public/` are copied into the bundle as-is; they are not processed by the bundler.
- `staticFile()` returns a URL string suitable for `src` props on `<Video>`, `<Audio>`, `<Img>`, and standard HTML elements.
- Do **not** use `import` / `require` for large media -- use `staticFile()` instead.
- During rendering, the file is served from a local HTTP server; CORS restrictions do not apply.

### 6.2 External URLs (Remote Images, CDN-Hosted Media)

Any `src` prop on `<Video>`, `<Audio>`, or `<Img>` accepts a full URL:

```tsx
<Video src="https://remotion.media/BigBuckBunny.mp4" />
<Audio src="https://remotion.media/audio.wav" />
```

**CORS requirement:** All remote assets must be either CORS-enabled or served from the bundle using `staticFile()`. Non-CORS resources will fail to load in the `@remotion/media` tags (and cannot be preloaded with `resolveRedirect()`).

**Credentials:** Use the `credentials` prop (available from v4.0.437) to send cookies or auth headers to cross-origin URLs:

```tsx
<Video credentials="include" src="https://example.com/protected-video.mp4" />
```

Accepted values: `"omit"`, `"same-origin"` (default), `"include"`.

### 6.3 Font Loading and Rendering

### `@remotion/fonts` -- `loadFont()`

Load local or remote fonts by URL. Automatically blocks rendering via `delayRender()` until ready.

```tsx
import {loadFont} from '@remotion/fonts';
import {staticFile} from 'remotion';

loadFont({
  family: 'Bangers',
  url: staticFile('bangers.ttf'),
});
```

| Parameter | Type | Description |
|---|---|---|
| `family` | `string` | **Required.** Name to reference in CSS `fontFamily`. |
| `url` | `string` | **Required.** URL or `staticFile()` path to the font file. |
| `format?` | `string` | Override format: `"woff2"`, `"woff"`, `"opentype"`, `"truetype"`. Derived from extension by default. |
| `ascentOverride?` | `string` | Ascent metric override. |
| `descentOverride?` | `string` | Descent metric override. |
| `display?` | `string` | CSS `font-display` equivalent. |
| `featureSettings?` | `string` | CSS `font-feature-settings` equivalent. |
| `lineGapOverride?` | `string` | Line gap metric override. |
| `stretch?` | `string` | CSS `font-stretch` equivalent. |
| `style?` | `string` | CSS `font-style` equivalent. |
| `weight?` | `string` | CSS `font-weight` equivalent. |
| `unicodeRange?` | `string` | Unicode range subset. |

**Returns:** `Promise<void>` -- resolves when the font is ready.

### `@remotion/google-fonts` (Pattern Summary)

The `@remotion/google-fonts` package provides a dedicated module for every Google Font (1,600+ fonts). Rather than listing each, the package follows a consistent pattern:

**Import pattern:** `@remotion/google-fonts/<FontName>` (PascalCase, e.g. `TitanOne`, `Inter`, `RobotoMono`).

```tsx
import {loadFont} from '@remotion/google-fonts/TitanOne';

const {fontFamily, waitUntilDone} = loadFont('normal', {
  weights: ['400'],
  subsets: ['latin'],
});
// fontFamily === "Titan One"
```

**`loadFont(style, options?)`**

| Parameter | Type | Description |
|---|---|---|
| `style` | `string` | `"normal"` or `"italic"`. |
| `options.weights?` | `string[]` | Array of weight strings (e.g. `['400', '700']`). Defaults to all. |
| `options.subsets?` | `string[]` | Array of subsets (e.g. `['latin']`). Defaults to all. |

**Returns:** `{ fontFamily: string; waitUntilDone: () => Promise<void>; unicodeRanges: Record<string,string> }`

**Utility functions:**

| Function | Import | Description |
|---|---|---|
| `getAvailableFonts()` | `@remotion/google-fonts` | Returns array of all available Google Fonts with metadata. |
| `getInfo()` | `@remotion/google-fonts/<Font>` | Returns metadata for a specific font (styles, weights, subsets, designers, URLs). |
| `loadFontFromInfo()` | `@remotion/google-fonts` | Load a font dynamically from an info object (useful when font name is not known at build time). |

> **Gap:** The docs do not document `loadFontFromInfo()` parameter tables in full detail beyond the info object shape.

### 6.4 Video Clip Compositing (Overlays, Picture-in-Picture)

Video compositing uses standard React layout. The `<Video>` component from `@remotion/media` renders into a `<canvas>` element and accepts a `style` prop:

```tsx
import {AbsoluteFill} from 'remotion';
import {Video} from '@remotion/media';

export const PiP = () => (
  <AbsoluteFill>
    {/* Background video */}
    <Video src="https://remotion.media/BigBuckBunny.mp4" />
    {/* Picture-in-picture overlay */}
    <Video
      src="https://remotion.media/webcam.mp4"
      style={{position: 'absolute', bottom: 20, right: 20, width: 320, height: 180}}
      muted
    />
  </AbsoluteFill>
);
```

### `<Video>` Component (`@remotion/media`) -- All Props

Based on WebCodecs and Mediabunny. Falls back to `<OffthreadVideo>` when decoding fails.

| Prop | Type | Default | Description |
|---|---|---|---|
| `src` | `string` | -- | **Required.** URL or `staticFile()` path. |
| `trimBefore?` | `number` | -- | Frame number to start playback from (trims beginning). |
| `trimAfter?` | `number` | -- | Frame number to end playback at (trims end). |
| `volume?` | `number \| (frame: number) => number` | `1` | Static volume or per-frame callback. |
| `playbackRate?` | `number` | `1` | Speed multiplier (0.5 = half speed, 2 = double). v4.0.354+. |
| `loop?` | `boolean` | `false` | Loop indefinitely. |
| `loopVolumeCurveBehavior?` | `"repeat" \| "extend"` | `"repeat"` | Volume callback frame behavior when looping. v4.0.354+. |
| `muted?` | `boolean` | `false` | Mute audio track. |
| `style?` | `React.CSSProperties` | -- | Applied to the underlying `<canvas>` element. |
| `name?` | `string` | -- | Label in Remotion Studio timeline. |
| `showInTimeline?` | `boolean` | `true` | Show layer in Studio timeline. |
| `onError?` | `(error: Error) => 'fallback' \| 'fail'` | -- | Error handler. v4.0.404+. |
| `onVideoFrame?` | `(frame: CanvasImageSource) => void` | -- | Callback per extracted frame. |
| `audioStreamIndex?` | `number` | `0` | Select audio stream for multi-stream files. |
| `credentials?` | `"omit" \| "same-origin" \| "include"` | `"same-origin"` | Fetch credentials mode. v4.0.437+. |
| `toneFrequency?` | `number` | `1` | Pitch shift (0.01-2). Server-side only. |
| `headless?` | `boolean` | `false` | No `<canvas>`, use with `onVideoFrame` for Three.js. v4.0.387+. |
| `delayRenderTimeoutInMilliseconds?` | `number` | -- | Custom `delayRender()` timeout. |
| `delayRenderRetries?` | `number` | -- | Custom `delayRender()` retry count. |
| `disallowFallbackToOffthreadVideo?` | `boolean` | `false` | Fail instead of falling back to `<OffthreadVideo>`. |
| `fallbackOffthreadVideoProps?` | `object` | -- | Props forwarded to `<OffthreadVideo>` on fallback. |
| `debugOverlay?` | `boolean` | `false` | Show debug overlay. |
| `debugAudioScheduling?` | `boolean` | `false` | Log audio scheduling info. |

### Supported Formats and Fallback Behavior

`@remotion/media` tags are based on Mediabunny and WebCodecs. When decoding fails (unsupported codec, CORS, missing WebGL for alpha channels), the component automatically falls back to `<OffthreadVideo>` or `<Html5Audio>`.

**Matroska limitation:** `.mkv`/`.webm` files require decoding all audio from the start up to the extraction point due to millisecond-precision timestamps. Prefer `.mp4`/`.mov`/`.m4a` for distributed rendering.

**Fallback is not possible in client-side rendering** (`@remotion/web-renderer`).

### In-Memory Cache

`@remotion/media` caches decoded video/audio frames. Default: up to 50% of system memory (min 500 MB, max 20 GB). Configurable per-render via `mediaCacheSizeInBytes` in all rendering APIs and CLI flags.

### 6.5 `@remotion/media-utils` -- All Functions

Utility functions for audio/video metadata and visualization. License: MIT.

### Listed Functions (from package index)

| Function | Description |
|---|---|
| `audioBufferToDataUrl()` | Serialize an AudioBuffer to a data URL. |
| `getAudioData()` | Get metadata of an audio source. |
| `getAudioDurationInSeconds()` | Get duration of an audio source. |
| `getVideoMetadata()` | Get metadata of a video source. |
| `getWaveformPortion()` | Trim audio data into a waveform portion. |
| `useAudioData()` | React hook wrapper around `getAudioData()`. |
| `useWindowedAudioData()` | Optimized for fetching only current data; works only with `.wav`. |
| `visualizeAudio()` | Process a music waveform for visualization. |
| `visualizeAudioWaveform()` | Process a voice waveform for visualization. |
| `createSmoothSvgPath()` | Turn waveform points into a smooth SVG path. |

> **Gap:** The source docs in the `18-media-utils/` folder only contain detailed pages for `visualizeAudioWaveform()` and `createSmoothSvgPath()`. The remaining functions (`audioBufferToDataUrl`, `getAudioData`, `getAudioDurationInSeconds`, `getVideoMetadata`, `getWaveformPortion`, `useAudioData`, `useWindowedAudioData`, `visualizeAudio`) are listed in the index but their full parameter tables are not included in the provided source files.

### `visualizeAudioWaveform(options)`

Processes `AudioData` for displaying as a waveform. Suitable for voice; use `visualizeAudio()` for music.

| Parameter | Type | Description |
|---|---|---|
| `audioData` | `AudioData` | Audio data from `useAudioData()` or `getAudioData()`. |
| `frame` | `number` | Current frame in the audio track. |
| `fps` | `number` | Frame rate of the composition. |
| `numberOfSamples` | `number` | Power of two (32, 64, 128, ...). Controls output array length. |
| `windowInSeconds` | `number` | Duration (seconds) of the waveform window. |
| `dataOffsetInSeconds?` | `number` | Offset for `useWindowedAudioData()`. v4.0.268+. |
| `normalize?` | `boolean` | Default `false`. Scale so biggest value is `1`. v4.0.280+. |

**Returns:** `number[]` -- amplitudes between -1 and 1, length = `numberOfSamples`.

### `createSmoothSvgPath(options)`

Adds SVG cubic bezier `C` commands between points for smooth paths.

| Parameter | Type | Description |
|---|---|---|
| `points` | `{x: number; y: number}[]` | Array of 2D points. |

**Returns:** `string` -- SVG path `d` attribute value.

### 6.6 `@remotion/preload` -- All Functions

Functions for preloading assets in the Player and Studio. Not required for rendering but enables seamless playback. License: MIT.

An alternative is `prefetch()` from `remotion` -- see docs for trade-off comparison.

### `preloadVideo(src)`

Preloads a video so `<Video>` tags play immediately on mount.

- Firefox: appends `<link rel="preload" as="video">` to `<head>`.
- Other browsers: appends `<video preload="auto">` to `<body>`.

**Parameters:** `src: string` -- video URL.
**Returns:** `() => void` -- call to un-preload.

### `preloadAudio(src)`

Preloads audio for immediate playback on mount.

- Firefox: appends `<link rel="preload" as="audio">` to `<head>`.
- Other browsers: appends `<audio preload="auto">` to `<body>`.

**Parameters:** `src: string` -- audio URL.
**Returns:** `() => void` -- call to un-preload.

### `preloadImage(src)`

Preloads an image for immediate display.

- Appends `<link rel="preload" as="image">` to `<head>`.

**Parameters:** `src: string` -- image URL.
**Returns:** `() => void` -- call to un-preload.

### `preloadFont(src)`

Preloads a font file.

- Appends `<link rel="preload" as="font">` to `<head>`.

**Parameters:** `src: string` -- font URL.
**Returns:** `() => void` -- call to un-preload.

### `resolveRedirect(url)`

Follows URL redirects until the final URL is resolved. Required when preloading assets behind redirects. Throws if the resource does not support CORS.

**Parameters:** `url: string` -- URL to resolve.
**Returns:** `Promise<string>` -- resolved final URL.

```tsx
import {preloadVideo, resolveRedirect} from '@remotion/preload';

resolveRedirect(videoUrl)
  .then((resolved) => { preloadVideo(resolved); })
  .catch(() => { preloadVideo(videoUrl); }); // best-effort fallback
```

### 6.7 `@remotion/media-parser` -- Media File Parsing

> **Note:** `@remotion/media-parser` is deprecated. Remotion is migrating to Mediabunny. The API remains functional but new projects should prefer Mediabunny.

A zero-dependency package for parsing video/audio files to extract metadata and samples.

**Supported containers:** `.mp4`, `.mov`, `.webm`, `.mkv`, `.avi`, `.m3u8`, `.ts`, `.mp3`, `.wav`, `.aac`, `.m4a`, `.flac`.
**Runtimes:** Browser, Node.js, Bun.

### Core Functions

#### `parseMedia(options)`

The main entry point. Functional TypeScript API that parses a media source.

| Parameter | Type | Description |
|---|---|---|
| `src` | `string \| ReadableStream \| Blob` | Media source. |
| `fields` | `object` | Which metadata fields to extract. |
| `reader?` | `Reader` | Custom reader (see readers below). |
| `controller?` | `MediaParserController` | For pause/resume/abort. |
| `onVideoTrack?` | `callback` | Called when a video track is found. |
| `onAudioTrack?` | `callback` | Called when an audio track is found. |

**Returns:** `Promise<ParseMediaResult>` -- object with requested fields.

#### `downloadAndParseMedia(options)`

Downloads and parses a remote media file. Same options as `parseMedia()` but with download-specific additions.

#### `parseMediaOnWebWorker(options)`

Runs `parseMedia()` in a Web Worker to avoid blocking the main thread.

#### `parseMediaOnServerWorker(options)`

Runs `parseMedia()` in a Node.js worker thread.

#### `MediaParserController`

Controller object for pausing, resuming, and aborting media parsing.

#### `hasBeenAborted(error)`

Utility to check if an error was caused by an abort signal.

### Readers

| Reader | Environment | Description |
|---|---|---|
| `nodeReader` | Node.js | Reads from the filesystem. |
| `webReader` | Browser | Reads using `fetch()`. |
| `universalReader` | Both | Auto-selects based on environment. |

### Writers

| Writer | Environment | Description |
|---|---|---|
| `nodeWriter` | Node.js | Writes to the filesystem. |

### Types

The package exports comprehensive TypeScript types for all parsed metadata fields including dimensions, duration, codec info, tracks, and more.

### `WEBCODECS_TIMESCALE`

A constant representing the timescale used by WebCodecs (1,000,000 microseconds per second).

---

## 7. Transitions & Motion

---

### 7.1 @remotion/transitions

*Available from v4.0.53. License: Remotion License.*

Provides the `<TransitionSeries>` component for transitioning between scenes, along with timing presets and presentation effects.

```
npm i @remotion/transitions
```

### 7.1.1 `<TransitionSeries>`

*Available from v4.0.59.*

Behaves like `<Series>` but allows `<TransitionSeries.Transition>` and `<TransitionSeries.Overlay>` components between sequences.

**Duration calculation:** Total duration = sum of all sequence durations minus the sum of all transition durations. Overlays do not shorten the timeline.

```tsx
import {linearTiming, springTiming, TransitionSeries} from '@remotion/transitions';
import {fade} from '@remotion/transitions/fade';
import {wipe} from '@remotion/transitions/wipe';

export const TransitionExample: React.FC = () => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="#0b84f3" />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        timing={springTiming({config: {damping: 200}})}
        presentation={fade()}
      />
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="pink" />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition
        timing={linearTiming({durationInFrames: 30})}
        presentation={wipe()}
      />
      <TransitionSeries.Sequence durationInFrames={60}>
        <Fill color="#2ecc71" />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};
```

#### Sub-components

| Component | Props | Description |
|---|---|---|
| `<TransitionSeries>` | `from?`, `name?`, `className?`, `style?` (inherited from `<Sequence>`) | Container. Can only contain `.Sequence`, `.Transition`, `.Overlay` children. |
| `<TransitionSeries.Sequence>` | `durationInFrames`, `name?`, `className?`, `style?`, `premountFor?`, `postmountFor?`, `layout?` | A scene in the series. |
| `<TransitionSeries.Transition>` | `timing: TransitionTiming`, `presentation?: TransitionPresentation` (default: `slide()`) | Placed between two sequences. Both scenes render simultaneously during the transition. Shortens total duration. |
| `<TransitionSeries.Overlay>` | `durationInFrames: number`, `offset?: number` (default: `0`) | *v4.0.415.* Placed between two sequences. Renders children on top of the cut point without affecting timing. Centered on cut point by default. |

**Rules:**
1. A transition must not be longer than the adjacent sequence.
2. Two transitions cannot be adjacent.
3. Two overlays cannot be adjacent.
4. A transition and an overlay cannot be adjacent.
5. There must be at least one sequence before or after a transition or overlay.

**Enter/exit animations:** Place a transition first or last in the `<TransitionSeries>` to animate entrance or exit of a single scene.

### 7.1.2 `useTransitionProgress()`

> **Gap:** The source docs reference `useTransitionProgress()` as a hook for reading transition progress inside a presentation component, but the detailed API parameters and return type are not included in the available source files. Consult the official docs at `/docs/transitions/usetransitionprogress` for the complete signature.

### 7.1.3 Timings

A **timing** controls the duration and progress curve of a transition. Remotion provides two built-in timings plus support for custom implementations.

**Getting the duration of a timing:**
```tsx
import {springTiming} from '@remotion/transitions';
springTiming({config: {damping: 200}}).getDurationInFrames({fps: 30}); // 23
```

| Timing | Description |
|---|---|
| `springTiming(options?)` | Uses Remotion's `spring()` under the hood. Accepts a `config` object with spring parameters. |
| `linearTiming({durationInFrames})` | Linear progress over a fixed frame count. Accepts an optional `easing` function. |
| Custom timings | Implement the `TransitionTiming` interface with `getDurationInFrames({fps})` and `getProgress({frame, fps})` methods. |

### 7.1.4 Presentations

A **presentation** defines the visual effect of a transition. Combined with a timing, it forms a complete transition.

| Presentation | Description |
|---|---|
| `fade()` | Animate the opacity of scenes. |
| `slide()` | Slide in the new scene and push out the previous scene. |
| `wipe()` | Slide over the previous scene (no push). |
| `flip()` | Rotate the previous scene. |
| `clockWipe()` | Reveal the new scene in a circular clockwise movement. |
| `iris()` | Reveal the scene through a circular mask expanding from center. |
| `cube()` | *Paid.* Rotate both scenes with 3D perspective. |
| `none()` | No visual effect (hard cut with timing overlap). |
| Custom presentations | Implement `TransitionPresentation` interface. |

**Audio transitions:** You can add sound effects to transitions. See the official docs for the audio transition API.

### 7.1.5 Building Custom Transitions

Custom timings must implement `TransitionTiming`:
- `getDurationInFrames({fps: number}): number` -- returns total frames
- `getProgress({frame: number, fps: number}): number` -- returns 0-1 progress

Custom presentations must implement `TransitionPresentation`:
- Returns an object with `EnteringComponent` and `ExitingComponent` that receive `progress` (0 to 1) and render the entering/exiting scenes.

> **Gap:** Full TypeScript type definitions for `TransitionTiming` and `TransitionPresentation` interfaces are not in the source files. See `/docs/transitions/timings/custom` and `/docs/transitions/presentations/custom`.

---

### 7.2 @remotion/animation-utils

*Available from v4.0.92. License: MIT.*

Functions for animating CSS styles, especially transform properties.

```
npm i @remotion/animation-utils
```

### 7.2.1 `makeTransform()`

Takes an array of transformation strings and combines them into a single CSS `transform` value.

```tsx
import {makeTransform, rotate, translate} from "@remotion/animation-utils";

const transform = makeTransform([rotate(45), translate(50, 50)]);
// => "rotate(45deg) translate(50px, 50px)"
```

If using a single transform, you can use it directly without `makeTransform()`:
```tsx
import {rotate} from "@remotion/animation-utils";
const transform = rotate(45); // => "rotate(45deg)"
```

#### All Transformation Functions

| Function | Signature | Example Output |
|---|---|---|
| `matrix()` | `matrix(a, b, c, d, tx, ty)` | `"matrix(1, 0, 0, 1, 50, 50)"` |
| `matrix3d()` | `matrix3d(16 numbers)` | `"matrix3d(1, 0, 0, 0, ...)"` |
| `perspective()` | `perspective(px)` | `"perspective(100px)"` |
| `rotate()` | `rotate(deg)` | `"rotate(45deg)"` |
| `rotate3d()` | `rotate3d(x, y, z, angle, unit?)` | `"rotate3d(1, 0, 0, 45deg)"` |
| `rotateX()` | `rotateX(angle, unit?)` | `"rotateX(45deg)"` |
| `rotateY()` | `rotateY(angle, unit?)` | `"rotateY(45deg)"` |
| `rotateZ()` | `rotateZ(angle, unit?)` | `"rotateZ(45deg)"` |
| `scale()` | `scale(x, y?)` | `"scale(2, 2)"` or `"scale(2, 3)"` |
| `scale3d()` | `scale3d(x, y, z)` | `"scale3d(2, 3, 4)"` |
| `scaleX()` | `scaleX(x)` | `"scaleX(2)"` |
| `scaleY()` | `scaleY(y)` | `"scaleY(2)"` |
| `scaleZ()` | `scaleZ(z)` | `"scaleZ(2)"` |
| `skew()` | `skew(deg)` | `"skew(45deg)"` |
| `skewX()` | `skewX(angle, unit?)` | `"skewX(45deg)"` |
| `skewY()` | `skewY(angle, unit?)` | `"skewY(45deg)"` |
| `translate()` | `translate(x, unitOrY?, y?, unit?)` | `"translate(10px, 20px)"` |
| `translate3d()` | `translate3d(x, unitOrY, y, unitOrZ, z, unit?)` | `"translate3d(10px, 20px, 30px)"` |
| `translateX()` | `translateX(x, unit?)` | `"translateX(10px)"` |
| `translateY()` | `translateY(y, unit?)` | `"translateY(10px)"` |
| `translateZ()` | `translateZ(z, unit?)` | `"translateZ(10px)"` |

All angle functions default to `deg`. Number values for translate default to `px`. String values are passed through (e.g., `"12rem"`).

### 7.2.2 `interpolateStyles()`

Interpolates CSS style objects based on a numeric input range -- the style equivalent of `interpolate()`.

```tsx
import {interpolateStyles, makeTransform, translateY} from "@remotion/animation-utils";

const animatedStyles = interpolateStyles(
  15,                    // input value
  [0, 30, 60],           // input range
  [
    {opacity: 0, transform: makeTransform([translateY(-50)])},
    {opacity: 1, transform: makeTransform([translateY(0)])},
    {opacity: 0, transform: makeTransform([translateY(50)])},
  ],
);
```

**Parameters:**

| # | Parameter | Type | Description |
|---|---|---|---|
| 1 | `input` | `number` | The current input value. |
| 2 | `inputRange` | `number[]` | Range of expected input values (min 2 elements). |
| 3 | `outputStylesRange` | `CSSProperties[]` | Output styles mapped to each input value (same length as inputRange). |
| 4 | `options?` | `object` | Same options as `interpolate()` (extrapolation, etc.). |

**Returns:** A `CSSProperties` object with interpolated values.

---

### 7.3 @remotion/motion-blur

*Available from v3.2.31. License: MIT.*

Higher-order components that create motion blur and trail effects by duplicating children at different time offsets.

```
npm i @remotion/motion-blur
```

**Important:** Children must be absolutely positioned (use `<AbsoluteFill>`). The `useCurrentFrame()` hook must be called **inside** the children components, not outside the motion blur wrapper.

### 7.3.1 `<Trail>`

*Available from v3.2.39 (previously called `<MotionBlur>`).*

Duplicates children with time offsets to create a trail effect.

| Prop | Type | Description |
|---|---|---|
| `layers` | `number` (integer) | Number of layers added below the content. |
| `lagInFrames` | `number` | Frames each layer lags behind the previous. Can be a float. |
| `trailOpacity` | `number` | Highest opacity of a trail layer. Lowest is 0; layers in between are interpolated. |

```tsx
import {Trail} from '@remotion/motion-blur';
import {AbsoluteFill} from 'remotion';

export const MyComposition = () => {
  return (
    <Trail layers={50} lagInFrames={0.1} trailOpacity={1}>
      <AbsoluteFill style={{backgroundColor: 'white', justifyContent: 'center', alignItems: 'center'}}>
        <BlueSquare />
      </AbsoluteFill>
    </Trail>
  );
};
```

### 7.3.2 `<CameraMotionBlur>`

*Available from v3.2.39.*

Produces natural-looking motion blur similar to a film camera by averaging multiple time-offset samples.

| Prop | Type | Default | Description |
|---|---|---|---|
| `shutterAngle?` | `number` | `180` | Amount of blur. Higher = more blur. Common: 90 or 180 degrees. |
| `samples?` | `number` | `10` | Number of frames averaged. Higher = better quality but potentially reduced image quality. Recommended: 5-10. |

```tsx
import {CameraMotionBlur} from '@remotion/motion-blur';
import {AbsoluteFill} from 'remotion';

export const MyComposition = () => {
  return (
    <CameraMotionBlur shutterAngle={180} samples={10}>
      <AbsoluteFill style={{backgroundColor: 'white', justifyContent: 'center', alignItems: 'center'}}>
        <RainbowSquare />
      </AbsoluteFill>
    </CameraMotionBlur>
  );
};
```

### 7.3.3 Common Mistake

`<Trail>` and `<CameraMotionBlur>` manipulate React context for the current time. If you call `useCurrentFrame()` **outside** the motion blur wrapper, the blur effect will not apply to that value. Always call `useCurrentFrame()` inside a child component of the blur wrapper.

---

## 8. Text & Typography

### 8.1 Text Rendering

Remotion renders text using standard React/CSS web typography. Since compositions render in a real Chromium browser, all CSS text properties work:

- `fontFamily`, `fontSize`, `fontWeight`, `fontStyle`
- `lineHeight`, `letterSpacing`, `textAlign`, `textTransform`
- `textShadow`, `textDecoration`, `wordBreak`, `whiteSpace`

Fonts must be loaded before rendering. Use `@remotion/fonts`, `@remotion/google-fonts`, or CSS `@font-face`.

### 8.2 Dynamic Text Sizing and Fitting

### `@remotion/layout-utils`

Available from v4.0.50. Utility functions for measuring text and computing dynamic layouts. Browser-only (not Node.js/Bun). License: MIT.

**Best practices:**
- Always wait for fonts to load before calling measurement functions.
- Pass `validateFontIsLoaded: true` (will be default in v5) to catch fallback-font measurement bugs.
- Match all CSS font properties between measurement calls and rendering markup.
- Do not use `padding` or `border` on measured text -- use `outline` instead.
- Text is measured with `whiteSpace: "pre"` and `display: "inline-block"`.

#### `measureText(options)`

Calculates width and height of text. Results are cached.

| Parameter | Type | Description |
|---|---|---|
| `text` | `string` | **Required.** The text to measure. |
| `fontFamily` | `string` | **Required.** CSS `font-family`. |
| `fontSize` | `number \| string` | **Required.** CSS `font-size`. Strings allowed from v4.0.125. |
| `fontWeight` | `string` | **Required.** CSS `font-weight`. |
| `letterSpacing?` | `string` | CSS `letter-spacing`. |
| `fontVariantNumeric?` | `string` | CSS `font-variant-numeric`. v4.0.57+. |
| `textTransform?` | `string` | CSS `text-transform`. v4.0.140+. |
| `validateFontIsLoaded?` | `boolean` | Throw if fallback font detected. v4.0.136+. |
| `additionalStyles?` | `object` | Extra CSS properties affecting layout. v4.0.140+. |

**Returns:** `{ width: number; height: number }`

#### `fillTextBox(options)`

Creates a text box that tracks line breaks and overflow as words are added.

**Constructor options:**

| Parameter | Type | Description |
|---|---|---|
| `maxBoxWidth` | `number` | Maximum width in pixels. |
| `maxLines` | `number` | Maximum number of lines. |

**`.add(options)` method parameters:**

| Parameter | Type | Description |
|---|---|---|
| `text` | `string` | Word to add. |
| `fontFamily` | `string` | CSS `font-family`. |
| `fontSize` | `number` | CSS `font-size` (px). |
| `fontWeight?` | `string` | CSS `font-weight`. |
| `fontVariantNumeric?` | `string` | CSS `font-variant-numeric`. |
| `textTransform?` | `string` | CSS `text-transform`. v4.0.140+. |
| `validateFontIsLoaded?` | `boolean` | Throw if fallback font detected. v4.0.136+. |
| `additionalStyles?` | `object` | Extra CSS layout properties. v4.0.140+. |

**`.add()` returns:** `{ exceedsBox: boolean; newLine: boolean }`

#### `fitText(options)`

Calculates the `fontSize` needed to fit text into a given width (single line).

| Parameter | Type | Description |
|---|---|---|
| `text` | `string` | **Required.** The text to fit. |
| `withinWidth` | `number` | **Required.** Target width in pixels. |
| `fontFamily` | `string` | **Required.** CSS `font-family`. |
| `fontWeight?` | `string \| number` | CSS `font-weight`. |
| `letterSpacing?` | `string` | CSS `letter-spacing`. |
| `fontVariantNumeric?` | `string` | CSS `font-variant-numeric`. |
| `textTransform?` | `string` | CSS `text-transform`. v4.0.140+. |
| `validateFontIsLoaded?` | `boolean` | Throw if fallback font detected. v4.0.136+. |
| `additionalStyles?` | `object` | Extra CSS layout properties. v4.0.140+. |

**Returns:** `{ fontSize: number }`

#### `fitTextOnNLines(options)`

Calculates `fontSize` to fit text within a width while respecting a max line count. Available from v4.0.313.

| Parameter | Type | Description |
|---|---|---|
| `text` | `string` | **Required.** The text to fit. |
| `maxBoxWidth` | `number` | **Required.** Maximum width in pixels. |
| `maxLines` | `number` | **Required.** Maximum number of lines. |
| `fontFamily` | `string` | **Required.** CSS `font-family`. |
| `fontWeight?` | `string \| number` | CSS `font-weight`. |
| `letterSpacing?` | `string` | CSS `letter-spacing`. |
| `fontVariantNumeric?` | `string` | CSS `font-variant-numeric`. |
| `textTransform?` | `string` | CSS `text-transform`. |
| `validateFontIsLoaded?` | `boolean` | Throw if fallback font detected. |
| `additionalStyles?` | `object` | Extra CSS layout properties. |
| `maxFontSize?` | `number` | Cap font size. Default: 2000. |

**Returns:** `{ fontSize: number; lines: string[] }`

### 8.3 Animated Text Effects

Remotion does not ship a dedicated animated-text package. Animated text is built with standard patterns:

- Use `useCurrentFrame()` and `interpolate()` to animate CSS properties (`opacity`, `transform`, `letterSpacing`) per-frame.
- Use `<Sequence>` to stagger word or character appearance.
- Use `spring()` for physics-based text animations.
- Combine with `@remotion/layout-utils` to measure text for precise positioning.

> **Gap:** No dedicated `@remotion/animated-text` package exists. Animated text effects are achieved through composition of core Remotion primitives.

### 8.4 Subtitle/Caption Rendering -- `@remotion/captions`

Available from v4.0.216. License: MIT.

### `Caption` Type

Standard data structure for captions across all Remotion transcription packages.

```ts
type Caption = {
  text: string;           // Whitespace-sensitive (include leading spaces)
  startMs: number;        // Start time in milliseconds
  endMs: number;          // End time in milliseconds
  timestampMs: number | null;  // Singular timestamp (t_dtw from whisper.cpp)
  confidence: number | null;   // 0-1 confidence score
};
```

**Whitespace:** Apply `white-space: pre` CSS to caption containers to preserve spaces.

### `parseSrt(options)`

Parses `.srt` file contents into `Caption` arrays.

| Parameter | Type | Description |
|---|---|---|
| `input` | `string` | **Required.** Contents of a `.srt` file. |

**Returns:** `{ captions: Caption[] }`

```tsx
import {parseSrt} from '@remotion/captions';

const {captions} = parseSrt({input: srtFileContents});
```

### `serializeSrt(options)`

Converts a two-dimensional `Caption` array into `.srt` format.

| Parameter | Type | Description |
|---|---|---|
| `lines` | `Caption[][]` | **Required.** Each top-level item = one subtitle line. Words within are concatenated (no spaces added). Start timestamp from first word's `startMs`, end from last word's `endMs`. Empty arrays are ignored. |

**Returns:** `string` -- `.srt` formatted content.

### `createTikTokStyleCaptions(options)`

Segments captions into "pages" for TikTok-style word-by-word or phrase-by-phrase display.

| Parameter | Type | Description |
|---|---|---|
| `captions` | `Caption[]` | **Required.** Array of caption objects. Text must include leading spaces. |
| `combineTokensWithinMilliseconds` | `number` | **Required.** Words closer than this threshold combine into one page. High = many words per page; low = word-by-word. |

**Returns:** `{ pages: TikTokPage[] }`

**`TikTokPage` structure:**

| Field | Type | Description |
|---|---|---|
| `text` | `string` | Combined page text. |
| `startMs` | `number` | Page start time. |
| `durationMs` | `number` | Page duration (from v4.0.261). |
| `tokens` | `{text, fromMs, toMs}[]` | Per-word timing for word-level animation. |

### 8.5 `@remotion/fonts` and `@remotion/google-fonts`

See Section 6.3 above for `@remotion/fonts` (`loadFont()`) and the `@remotion/google-fonts` pattern summary.

---

## 9. Shapes & Graphics

---

### 9.1 @remotion/shapes

*License: MIT.*

SVG shape components and corresponding `make*()` functions for programmatic path generation.

```
npm i @remotion/shapes
```

### Common Props (all shape components)

Every shape component (`<Arrow>`, `<Rect>`, `<Circle>`, `<Ellipse>`, `<Triangle>`, `<Heart>`, `<Star>`, `<Pie>`, `<Polygon>`) accepts these common SVG styling props:

| Prop | Type | Description |
|---|---|---|
| `fill` | `string` | Fill color of the shape. |
| `stroke` | `string` | Stroke color. Use with `strokeWidth`. |
| `strokeWidth` | `string` | Width of the stroke. Use with `stroke`. |
| `style` | `CSSProperties` | Applied to the `<svg>` tag. Default: `overflow: 'visible'`. |
| `pathStyle` | `CSSProperties` | Applied to the `<path>` tag. Default: `transform-box: 'fill-box'` and centered `transform-origin`. |
| `strokeDasharray` | `string` | For path animation. See `evolvePath()`. |
| `strokeDashoffset` | `string` | For path animation. See `evolvePath()`. |

All other props valid on `<path>` are forwarded.

### Common Return Type (all `make*()` functions)

| Property | Type | Description |
|---|---|---|
| `path` | `string` | SVG path string suitable for `<path d={...}>`. |
| `width` | `number` | Width for SVG `viewBox`. |
| `height` | `number` | Height for SVG `viewBox`. |
| `instructions` | `Instruction[]` | Array of SVG path instructions. |
| `transformOrigin` | `string` | Center point for rotation. Use with `transform-origin` CSS and `transform-box: fill-box`. |

---

### 9.1.1 `<Arrow />` / `makeArrow()`

Renders an SVG arrow shape.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `length` | `number` | `300` | Total length along direction axis. |
| `headWidth` | `number` | `185` | Width of arrowhead at widest point. |
| `headLength` | `number` | `120` | Length of the arrowhead portion. |
| `shaftWidth` | `number` | `80` | Width of the arrow shaft. |
| `direction` | `"left" \| "right" \| "up" \| "down"` | `"right"` | Direction the arrow points. |
| `cornerRadius` | `number` | `0` | Rounds corners using an arc. |

```tsx
import {Arrow} from '@remotion/shapes';
<Arrow length={300} headWidth={185} headLength={120} shaftWidth={80} fill="red" direction="right" />
```

```tsx
import {makeArrow} from '@remotion/shapes';
const {path, width, height, transformOrigin} = makeArrow({
  length: 300, headWidth: 185, headLength: 120, shaftWidth: 80, direction: 'right',
});
```

### 9.1.2 `<Rect />` / `makeRect()`

Renders an SVG rectangle.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `width` | `number` | -- | Width of the rectangle. |
| `height` | `number` | -- | Height of the rectangle. |
| `cornerRadius` | `number` | `0` | Rounds corners. Cannot be used with `edgeRoundness`. |
| `edgeRoundness` | `number \| null` | `null` | Rounds edges with bezier curves. `0` = rotated rect inside bounds; `1` = squircle. Cannot be used with `cornerRadius`. |
| `debug` | `boolean` | `false` | Draws bezier control lines. |

```tsx
import {Rect} from "@remotion/shapes";
<Rect width={200} height={200} fill="red" />
```

```tsx
import {makeRect} from "@remotion/shapes";
const {path, width, height, transformOrigin} = makeRect({width: 100, height: 100});
// path: "M 0 0 l 100 0 l 0 100 l -100 0 Z"
```

### 9.1.3 `<Triangle />` / `makeTriangle()`

Renders an equilateral triangle.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `length` | `number` | -- | Length of one side. |
| `direction` | `"left" \| "right" \| "up" \| "down"` | -- | Direction the triangle points. |
| `cornerRadius` | `number` | `0` | Rounds corners. Cannot be used with `edgeRoundness`. |
| `edgeRoundness` | `number \| null` | `null` | Bezier edge rounding. `Math.sqrt(2) - 1` draws a circle. |
| `debug` | `boolean` | `false` | Draws bezier control lines. |

```tsx
import {Triangle} from "@remotion/shapes";
<Triangle length={100} fill="red" direction="left" />
```

### 9.1.4 `<Circle />` / `makeCircle()`

Renders a circle.

| Prop / Argument | Type | Description |
|---|---|---|
| `radius` | `number` | The radius of the circle. |

```tsx
import {Circle} from "@remotion/shapes";
<Circle radius={100} fill="green" stroke="red" strokeWidth={1} />
```

```tsx
import {makeCircle} from "@remotion/shapes";
const {path, width, height, transformOrigin} = makeCircle({radius: 100});
```

### 9.1.5 `<Ellipse />` / `makeEllipse()`

Renders an ellipse.

| Prop / Argument | Type | Description |
|---|---|---|
| `rx` | `number` | Radius on the X axis. |
| `ry` | `number` | Radius on the Y axis. |

```tsx
import {Ellipse} from "@remotion/shapes";
<Ellipse rx={100} ry={50} fill="green" stroke="red" strokeWidth={1} />
```

### 9.1.6 `<Heart />` / `makeHeart()`

*Available from v4.0.315.*

Renders a heart shape.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `height` | `number` | -- | Height of the heart. |
| `aspectRatio` | `number` | `1.1` | Aspect ratio. |
| `bottomRoundnessAdjustment` | `number` | `0` | Negative = sharper bottom, positive = rounder. |
| `depthAdjustment` | `number` | `0` | Negative = deeper top dip, positive = shallower. |

```tsx
import {Heart} from '@remotion/shapes';
<Heart height={100} fill="red" stroke="black" strokeWidth={2} />
```

### 9.1.7 `<Star />` / `makeStar()`

Renders a star.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `points` | `number` | -- | Number of points on the star. |
| `innerRadius` | `number` | -- | Inner radius. |
| `outerRadius` | `number` | -- | Outer radius. |
| `cornerRadius` | `number` | `0` | Rounds corners. Cannot be used with `edgeRoundness`. |
| `edgeRoundness` | `number \| null` | `null` | Bezier edge rounding. |

```tsx
import {Star} from '@remotion/shapes';
<Star points={5} innerRadius={100} outerRadius={200} fill="red" />
```

### 9.1.8 `<Pie />` / `makePie()`

Renders a pie (arc) piece.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `radius` | `number` | -- | Radius of the circle. |
| `progress` | `number` | -- | Fill percentage: `0` = empty, `1` = full circle. |
| `counterClockwise` | `boolean` | `false` | Fill direction. |
| `closePath` | `boolean` | `true` | If `false`, draws an open arc (no line to center). |
| `rotation` | `number` | `0` | Rotation in radians. `Math.PI * 2` = full rotation. |

```tsx
import {Pie} from "@remotion/shapes";
<Pie radius={100} progress={0.5} fill="green" stroke="red" strokeWidth={1} />
```

### 9.1.9 `<Polygon />` / `makePolygon()`

Renders a regular polygon.

| Prop / Argument | Type | Default | Description |
|---|---|---|---|
| `points` | `number` | -- | Number of vertices. |
| `radius` | `number` | -- | Radius of the polygon. |
| `cornerRadius` | `number` | `0` | Rounds corners. Cannot be used with `edgeRoundness`. |
| `edgeRoundness` | `number \| null` | `null` | Bezier edge rounding. |

```tsx
import {Polygon} from "@remotion/shapes";
<Polygon points={5} radius={80} />
```

---

### 9.2 @remotion/paths

*License: MIT. No dependencies -- can be used without Remotion.*

Utility functions for manipulating SVG paths. Built on code from `svg-path-properties`, `svg-path-reverse`, `svgpath`, `svg-path-bbox`, `translate-svg-path`, and `d3-interpolate-path`.

```
npm i @remotion/paths
```

### 9.2.1 `getLength(path): number`

Returns the total length of an SVG path.

```tsx
import {getLength} from "@remotion/paths";
const length = getLength("M 0 0 L 100 0"); // 100
```

### 9.2.2 `getPointAtLength(path, length): {x, y}`

Returns coordinates of a point at a given length along the path.

```tsx
import {getPointAtLength} from "@remotion/paths";
const point = getPointAtLength("M 0 0 L 100 0", 50); // {x: 50, y: 0}
```

**Tip:** Use `getLength(path) * 0.5` to get the midpoint.

### 9.2.3 `getTangentAtLength(path, length): {x, y}`

Returns tangent vector at a given length.

```tsx
import {getTangentAtLength} from "@remotion/paths";
const tangent = getTangentAtLength("M 50 50 L 150 50", 50); // {x: 1, y: 0}
```

### 9.2.4 `getInstructionIndexAtLength(path, length): {index, lengthIntoInstruction}`

*Available from v4.0.84.*

Returns which SVG instruction contains the given length, and how far into that instruction.

```tsx
import {getInstructionIndexAtLength} from "@remotion/paths";
const {index, lengthIntoInstruction} = getInstructionIndexAtLength("M 0 0 L 100 0 L 200 0", 105);
// index: 1, lengthIntoInstruction: 5
```

### 9.2.5 `reversePath(path): string`

Reverses an SVG path so start and end are switched.

```tsx
import {reversePath} from "@remotion/paths";
reversePath("M 0 0 L 100 0"); // switches direction
```

### 9.2.6 `normalizePath(path): string`

Converts all relative coordinates to absolute coordinates.

```tsx
import {normalizePath} from "@remotion/paths";
normalizePath("M 50 50 l 100 0"); // "M 50 50 L 150 50"
```

### 9.2.7 `interpolatePath(value, firstPath, secondPath): string`

Interpolates between two SVG paths. `value` of `0` returns the first path, `1` returns the second.

```tsx
import {interpolatePath} from "@remotion/paths";
interpolatePath(0.5, "M 0 0 L 100 0", "M 100 0 L 0 0"); // "M 50 0 L 50 0"
```

### 9.2.8 `evolvePath(progress, path): {strokeDasharray, strokeDashoffset}`

Animates an SVG path from invisible to fully drawn. Pass the returned values to `<path>`.

```tsx
import {evolvePath} from "@remotion/paths";

const path = "M 0 0 L 100 0";
const evolution = evolvePath(0.5, path);
// {strokeDasharray: '100 100', strokeDashoffset: 50}

<path d={path} strokeDasharray={evolution.strokeDasharray} strokeDashoffset={evolution.strokeDashoffset} />
```

Values above `1` devolve from the start. Values below `0` evolve from the end.

### 9.2.9 `resetPath(path): string`

*Available from v3.3.40.*

Translates a path so the top-left of the bounding box is at `(0, 0)`.

```tsx
import {resetPath} from "@remotion/paths";
resetPath("M 10 10 L 20 20"); // "M 0 0 L 10 10"
```

### 9.2.10 `getSubpaths(path): string[]`

*Available from v3.3.6.*

Splits an SVG path at each `M`/`m` command into separate subpath strings.

```tsx
import {getSubpaths} from "@remotion/paths";
const parts = getSubpaths("M 0 0 L 100 0 M 0 100 L 200 100");
// ["M 0 0 L 100 0", "M 0 100 L 200 100"]
```

### 9.2.11 `translatePath(path, x, y): string`

Translates a path by given X and Y offsets.

```tsx
import {translatePath} from "@remotion/paths";
translatePath("M10 10 L15 15", 10, 10); // "M 20 20 L 25 25"
```

### 9.2.12 `warpPath(path, fn, options?): string`

*Available from v3.3.43.*

Remaps all coordinates through a function to create warp effects. Splits the path into many small segments internally.

```tsx
import {warpPath, WarpPathFn} from "@remotion/paths";

const fn: WarpPathFn = ({x, y}) => ({
  x: x + Math.sin(y / 4) * 5,
  y: y,
});
const newPath = warpPath("M 0 0 L 0 100", fn);
```

| Parameter | Type | Description |
|---|---|---|
| `path` | `string` | SVG path string. |
| `fn` | `WarpPathFn: ({x, y}) => {x, y}` | Coordinate remapping function. |
| `options.interpolationThreshold?` | `number` | Min segment length before stopping subdivision. Default: `Math.max(width, height) * 0.01`. |

### 9.2.13 `scalePath(path, xScale, yScale): string`

*Available from v3.3.43.*

Scales a path by given factors. Origin is the top-left corner.

```tsx
import {scalePath} from "@remotion/paths";
scalePath("M 0 0 L 100 100", 1, 2); // "M 0 0 L 100 200"
```

### 9.2.14 `getBoundingBox(path): BoundingBox`

*Available from v3.3.40.*

Returns the smallest rectangle containing the path.

```tsx
import {getBoundingBox} from "@remotion/paths";
const box = getBoundingBox("M 35,50 a 25,25,0,1,1,50,0 a 25,25,0,1,1,-50,0");
// {x1: 35, x2: 85, y1: ~25, y2: 75, width: 50, height: ~50, viewBox: "35 25 50 50"}
```

**Return type (`BoundingBox`):**

| Property | Type | Available From |
|---|---|---|
| `x1` | `number` | -- |
| `x2` | `number` | -- |
| `y1` | `number` | -- |
| `y2` | `number` | -- |
| `width` | `number` | v3.3.97 |
| `height` | `number` | v3.3.97 |
| `viewBox` | `string` | v3.3.97 |

### 9.2.15 `extendViewBox(viewBox, factor): string`

*Available from v3.2.25.*

Widens an SVG `viewBox` in all directions by a scale factor.

```tsx
import {extendViewBox} from "@remotion/paths";
extendViewBox("0 0 1000 1000", 2); // "-500 -500 2000 2000"
```

**Alternative:** Set `style={{overflow: 'visible'}}` on the SVG container.

### 9.2.16 `parsePath(path): Instruction[]`

*Available from v3.3.40.*

Parses an SVG path string into an array of typed instruction objects.

```tsx
import {parsePath} from "@remotion/paths";
parsePath("M 10 10 L 20 20");
// [{type: "M", x: 10, y: 10}, {type: "L", x: 20, y: 20}]
```

The `Instruction` union type covers all SVG path commands: `M`, `L`, `H`, `V`, `C`, `S`, `Q`, `T`, `A`, `Z` and their lowercase (relative) variants.

### 9.2.17 `serializeInstructions(instructions): string`

*Available from v3.3.40.*

Inverse of `parsePath()`. Converts an `Instruction[]` array back to a path string.

```tsx
import {serializeInstructions} from "@remotion/paths";
serializeInstructions([
  {type: "M", x: 10, y: 10},
  {type: "L", x: 20, y: 20},
]); // "M 10 10 L 20 20"
```

### 9.2.18 `reduceInstructions(instructions): ReducedInstruction[]`

*Available from v3.3.40.*

Reduces instruction variety to only `M`, `L`, `C`, `Q`, and `Z` types. Eliminates all relative and shorthand instructions.

```tsx
import {reduceInstructions} from "@remotion/paths";
reduceInstructions([
  {type: "m", dx: 10, dy: 10},
  {type: "h", dx: 100},
]);
// [{type: 'M', x: 10, y: 10}, {type: 'L', x: 110, y: 10}]
```

### 9.2.19 `getParts()` -- REMOVED

Removed in v4. Use `getSubpaths()` instead.

> **Gap:** The source docs list `cutPath()` in the table of contents but no corresponding source file exists in the `25-paths/` folder. This function may be documented elsewhere or be a newer addition.

---

### 9.3 @remotion/noise

*Available from v3.2.32. License: MIT.*

Simplex noise generation functions. Based on the `simplex-noise` npm package.

```
npm i @remotion/noise
```

### 9.3.1 `noise2D(seed, x, y): number`

Returns a value in `[-1, 1]` for 2D coordinates. Same seed + same coordinates = same result.

```tsx
import {noise2D} from "@remotion/noise";
noise2D("my-seed", 32, 40); // number in [-1, 1]
```

### 9.3.2 `noise3D(seed, x, y, z): number`

Returns a value in `[-1, 1]` for 3D coordinates.

```tsx
import {noise3D} from "@remotion/noise";
noise3D("my-seed", 32, 40, 50);
```

### 9.3.3 `noise4D(seed, x, y, z, w): number`

Returns a value in `[-1, 1]` for 4D coordinates.

```tsx
import {noise4D} from "@remotion/noise";
noise4D("my-seed", 32, 40, 50, 64);
```

**Common parameters for all noise functions:**

| Parameter | Type | Description |
|---|---|---|
| `seed` | `string \| number` | Determines the noise pattern. Same seed = deterministic output. |
| `x` | `number` | First dimension. |
| `y` | `number` | Second dimension. |
| `z` | `number` | Third dimension (3D/4D only). |
| `w` | `number` | Fourth dimension (4D only). |

---

### 9.4 @remotion/animated-emoji

*Available from v4.0.187. License: Remotion License. Emoji licensed under CC BY 4.0.*

Wraps Google Fonts Animated Emoji into Remotion components.

```
npm i @remotion/animated-emoji
```

### 9.4.1 `<AnimatedEmoji>`

> **Gap:** The detailed props for `<AnimatedEmoji>` (emoji name, size, playbackRate, etc.) are referenced in the source table of contents but not fully documented in the available source files. See `/docs/animated-emoji/animated-emoji`.

### 9.4.2 `getAvailableEmoji()`

> **Gap:** Returns the list of available emoji. Full signature and return type not documented in available source files. See `/docs/animated-emoji/get-available-emoji`.

---

### 9.5 @remotion/gif

*License: Remotion License.*

Renders GIF files in Remotion compositions, synchronized with the timeline.

```
npm i @remotion/gif
```

### 9.5.1 `<Gif>`

> **Gap:** Full props table for `<Gif>` component (src, width, height, fit, playbackRate, etc.) is referenced in the source but not fully included in the available files. See `/docs/gif/gif`.

### 9.5.2 `getGifDurationInSeconds(src): Promise<number>`

Returns the duration of a GIF in seconds.

### 9.5.3 `preloadGif(src): void`

Preloads a GIF for faster rendering.

> **Gap:** Detailed parameters and return types for `getGifDurationInSeconds()` and `preloadGif()` are listed in the table of contents but full API details are not in the available source files.

---

### 9.6 @remotion/lottie

*License: Remotion License. Requires `lottie-web` peer dependency.*

Renders Lottie animations synchronized with Remotion's timeline.

```
npm i @remotion/lottie lottie-web
```

**Supported:** Playing animations, speed control, forward/backward playback, remote files, dimension/duration detection.

**Unsupported:** Non-SVG renderers, `setSubFrame()`, `setLocationHref()`, limited expression support (expressions using `.goToAndStop()` may cause flickering).

### 9.6.1 `<Lottie>`

| Prop | Type | Description |
|---|---|---|
| `animationData` | `object` | The parsed JSON Lottie animation data. |

> **Gap:** Full props table (playbackRate, direction, style, etc.) is referenced in source but detailed parameter listing is not in the available files. See `/docs/lottie/lottie`.

**Loading from static file:**
```tsx
import {Lottie} from '@remotion/lottie';
import {useEffect, useState} from 'react';
import {continueRender, delayRender, staticFile} from 'remotion';

export const MyComp = () => {
  const [handle] = useState(() => delayRender());
  const [animationData, setAnimationData] = useState(null);

  useEffect(() => {
    fetch(staticFile('animation.json'))
      .then((data) => data.json())
      .then((json) => {
        setAnimationData(json);
        continueRender(handle);
      })
      .catch((err) => cancelRender(err));
  }, [handle]);

  if (!animationData) return null;
  return <Lottie animationData={animationData} />;
};
```

### 9.6.2 `getLottieMetadata(animationData)`

Returns metadata about a Lottie animation (duration, dimensions, etc.).

> **Gap:** Full return type not detailed in available source files. See `/docs/lottie/get-lottie-metadata`.

---

### 9.7 @remotion/rive

*Available from v3.3.75. License: Remotion License.*

Renders Rive animations synchronized with Remotion's timeline.

```
npm i @remotion/rive
```

### 9.7.1 `<RemotionRiveCanvas>`

| Prop | Type | Default | Description |
|---|---|---|---|
| `src` | `string` | -- | URL of the `.riv` file. Can use `staticFile()`. |
| `fit?` | `"contain" \| "cover" \| "fill" \| "fit-height" \| "none" \| "scale-down" \| "fit-width"` | `"contain"` | How the animation fits the canvas. |
| `alignment?` | `"center" \| "bottom-center" \| "bottom-left" \| "bottom-right" \| "center-left" \| "center-right" \| "top-center" \| "top-left" \| "top-right"` | `"center"` | Alignment within the canvas. |
| `artboard?` | `string \| number` | default artboard | Artboard name or index. |
| `animation?` | `string \| number` | default animation | Animation name or index. |
| `onLoad?` | `(file: File) => void` | -- | *v4.0.58.* Callback when Rive runtime loads. |
| `enableRiveAssetCdn?` | `boolean` | `true` | *v4.0.181.* Enable Rive Asset CDN. |
| `assetLoader?` | `(asset, bytes) => boolean` | -- | *v4.0.181.* Custom asset loader (must be memoized with `useCallback`). |

**Ref API** (*v4.0.180*): Attach a ref via `React.useRef<RiveCanvasRef>()` to access:
- `getAnimationInstance()` -- `LinearAnimationInstance`
- `getArtboard()` -- `Artboard`
- `getRenderer()` -- `CanvasRenderer`
- `getCanvas()` -- `RiveCanvas`

```tsx
import {RemotionRiveCanvas} from '@remotion/rive';

function App() {
  return <RemotionRiveCanvas src="https://example.com/myAnimation.riv" />;
}
```

---

### 9.8 @remotion/skia

*License: Remotion License. Requires `@shopify/react-native-skia` peer dependency.*

Integrates React Native Skia with Remotion for Canvas-based graphics.

```
npm i @remotion/skia @shopify/react-native-skia
```

**Setup requirements:**
1. Override Webpack config with `enableSkia()`.
2. Modify the entry point to load Skia WASM before `registerRoot()`.
3. Use `--gl=angle` for GPU rendering if Skia effects are slow on CPU.

### 9.8.1 `enableSkia(config): WebpackConfig`

Modifies Webpack configuration to support Skia.

```ts
import {Config} from "@remotion/cli/config";
import {enableSkia} from "@remotion/skia/enable";

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableSkia(currentConfiguration);
});
```

### 9.8.2 `<SkiaCanvas />`

Wraps a React Native Skia `<Canvas>` with Remotion contexts.

| Prop | Type | Description |
|---|---|---|
| `width` | `number` | Canvas width in pixels. |
| `height` | `number` | Canvas height in pixels. |

Also accepts all props from `@shopify/react-native-skia`'s `<Canvas>`.

```tsx
import {SkiaCanvas} from "@remotion/skia";
import {Fill} from "@shopify/react-native-skia";
import {useVideoConfig} from "remotion";

const MySkiaVideo: React.FC = () => {
  const {width, height} = useVideoConfig();
  return (
    <SkiaCanvas width={width} height={height}>
      <Fill color="black" />
    </SkiaCanvas>
  );
};
```

---

### 9.9 @remotion/three

*License: Remotion License. Requires `three`, `@react-three/fiber`, `@types/three`.*

Integrates React Three Fiber (R3F) with Remotion for 3D graphics.

```
npm i three @react-three/fiber @remotion/three @types/three
```

### APIs

| API | Description |
|---|---|
| `<ThreeCanvas />` | Allows `useCurrentFrame()` and other Remotion hooks inside R3F. Animations render declaratively in markup rather than in `useFrame()`. |
| `useVideoTexture()` | Use a Remotion `<Html5Video />` as a Three.js texture map. |
| `useOffthreadVideoTexture()` | Like `useVideoTexture()` but displays exact frames as `Three.ImageTexture` during rendering (similar to `<OffthreadVideo />`). |

**Important notes:**
- Pass `layout="none"` to `<Sequence>` components inside `<ThreeCanvas>` (default `<div>` wrapper is not allowed in Three.js scenes).
- Set `chromiumOptions.gl: "angle"` for server-side rendering. In config: `Config.setChromiumOpenGlRenderer('angle')`.

> **Gap:** Full props for `<ThreeCanvas>`, `useVideoTexture()`, and `useOffthreadVideoTexture()` are referenced but not in the available source files. See `/docs/three-canvas`, `/docs/use-video-texture`, `/docs/use-offthread-video-texture`.

---

### 9.10 @remotion/light-leaks

*Available from v4.0.415. License: Remotion License.*

WebGL-based light leak effects for video transitions.

```
npm i @remotion/light-leaks
```

### 9.10.1 `<LightLeak>`

Renders a light leak that reveals during the first half and retracts during the second half of its duration. Extends `<Sequence>` (accepts all Sequence props except `children` and `layout`).

| Prop | Type | Default | Description |
|---|---|---|---|
| `durationInFrames?` | `number` | composition duration | Total duration. Effect reveals during first half, retracts during second half. |
| `seed?` | `number` | `0` | Pattern shape. Different seeds produce different patterns. |
| `hueShift?` | `number` | `0` | Hue rotation in degrees (0-360). `0` = yellow-orange, `120` = green, `240` = blue. |

```tsx
import {LightLeak} from '@remotion/light-leaks';
import {AbsoluteFill} from 'remotion';

const MyVideo = () => (
  <AbsoluteFill style={{backgroundColor: 'black'}}>
    <LightLeak durationInFrames={60} seed={3} hueShift={30} />
  </AbsoluteFill>
);
```

**Compatibility:** Chrome, Firefox, Safari. Client-side rendering, server-side rendering, Player, Studio. Not compatible with Node.js, Bun, or serverless functions directly.

---

### 9.11 @remotion/starburst

*Available from v4.0.435. License: Remotion License.*

Static WebGL-based retro starburst ray pattern.

```
npm i @remotion/starburst
```

### 9.11.1 `<Starburst>`

Renders a starburst ray pattern. Extends `<Sequence>` (accepts all Sequence props except `children` and `layout`).

| Prop | Type | Default | Description |
|---|---|---|---|
| `rays` | `number` | -- | Number of rays (2-100). |
| `colors` | `string[]` | -- | Array of hex color strings (min 2). Colors assigned cyclically to rays. |
| `rotation?` | `number` | `0` | Pattern rotation in degrees (0-360). |
| `smoothness?` | `number` | `0` | Edge softness. `0` = hard edges, `1` = very soft edges. |
| `vignette?` | `number` | `1` | Radial transparency falloff. `1` = fully opaque, `0` = fully transparent. |
| `originOffsetX?` | `number` | `0` | Horizontal origin shift. `-1` = left edge, `1` = right edge. |
| `originOffsetY?` | `number` | `0` | Vertical origin shift. `-1` = top edge, `1` = bottom edge. |

```tsx
import {Starburst} from '@remotion/starburst';
import {AbsoluteFill} from 'remotion';

const MyVideo = () => (
  <AbsoluteFill style={{backgroundColor: 'black'}}>
    <Starburst
      durationInFrames={60}
      rays={16}
      colors={['#ffdd00', '#ff8800', '#ff4400']}
      rotation={15}
      width={1080}
      height={1080}
    />
  </AbsoluteFill>
);
```

**Compatibility:** Chrome, Firefox, Safari. Client-side rendering, server-side rendering, Player, Studio. Not compatible with Node.js, Bun, or serverless functions directly.

---

### 9.12 @remotion/rounded-text-box

*Available from v4.0.360. License: MIT.*

Creates TikTok/Instagram-style multiline text box SVG paths with rounded corners.

```
npm i @remotion/rounded-text-box
```

### 9.12.1 `createRoundedTextBox(options): {d, boundingBox, instructions}`

**Parameters (object):**

| Property | Type | Description |
|---|---|---|
| `textMeasurements` | `Dimensions[]` | Array of `{width, height}` for each line. Obtain via `measureText()` from `@remotion/layout-utils`. |
| `textAlign` | `"left" \| "center" \| "right"` | Text alignment. |
| `horizontalPadding` | `number` | Horizontal padding of the text box. |
| `borderRadius` | `number` | Border radius of the text box. |

**Return value:**

| Property | Type | Description |
|---|---|---|
| `d` | `string` | The SVG path string. |
| `boundingBox` | `BoundingBox` | Bounding box (see `getBoundingBox()` from `@remotion/paths`). |
| `instructions` | `ReducedInstruction[]` | SVG path instructions array for use with `@remotion/paths`. |

```tsx
import {measureText} from '@remotion/layout-utils';
import {createRoundedTextBox} from '@remotion/rounded-text-box';

const lines = ['Hello World', 'This is a test'];
const textMeasurements = lines.map((t) =>
  measureText({text: t, fontFamily: 'Figtree', fontSize: 36, fontWeight: '700',
    additionalStyles: {lineHeight: 1.5}, fontVariantNumeric: 'normal',
    letterSpacing: 'normal', textTransform: 'none', validateFontIsLoaded: true}),
);

const {d, boundingBox} = createRoundedTextBox({
  textMeasurements,
  textAlign: 'center',
  horizontalPadding: 20,
  borderRadius: 20,
});

// Use `d` as the `d` attribute of an SVG `<path>` element
// Use `boundingBox.width` and `boundingBox.height` for the container dimensions
```


---

## 10. Audio

### 10.1 `<Audio>` Component (`@remotion/media`) -- All Props

WebCodecs-based audio component. Extracts audio using Mediabunny during rendering. Falls back to `<Html5Audio>` on failure.

```tsx
import {Audio} from '@remotion/media';
import {staticFile} from 'remotion';

export const MyVideo = () => (
  <Audio src={staticFile('audio.mp3')} />
);
```

### Full Props Table

| Prop | Type | Default | Description |
|---|---|---|---|
| `src` | `string` | -- | **Required.** URL or `staticFile()` path. |
| `trimBefore?` | `number` | -- | Frame to start from (trims beginning). |
| `trimAfter?` | `number` | -- | Frame to end at (trims end). |
| `volume?` | `number \| (frame: number) => number` | `1` | Static volume or per-frame volume callback. |
| `playbackRate?` | `number` | `1` | Speed multiplier (e.g. `0.5`, `2`). Reverse not supported. |
| `loop?` | `boolean` | `false` | Loop indefinitely. v3.2.29+. |
| `loopVolumeCurveBehavior?` | `"repeat" \| "extend"` | `"repeat"` | Frame counter behavior in volume callback when looping. |
| `muted?` | `boolean` | `false` | Mute audio while keeping tag mounted. Value may change over time. |
| `name?` | `string` | -- | Label in Remotion Studio timeline. |
| `showInTimeline?` | `boolean` | `true` | Show layer in Studio timeline. |
| `onError?` | `(error: Error) => 'fallback' \| 'fail'` | -- | Error handler. Return `'fallback'` for `<Html5Audio>`, `'fail'` to abort. v4.0.404+. |
| `audioStreamIndex?` | `number` | `0` | Select audio stream for multi-stream files. |
| `credentials?` | `"omit" \| "same-origin" \| "include"` | `"same-origin"` | Fetch credentials mode. v4.0.437+. |
| `toneFrequency?` | `number` | `1` | Pitch shift (0.01-2). Server-side rendering only. |
| `delayRenderTimeoutInMilliseconds?` | `number` | -- | Custom `delayRender()` timeout. |
| `delayRenderRetries?` | `number` | -- | Custom `delayRender()` retry count. |
| `disallowFallbackToHtml5Audio?` | `boolean` | `false` | Fail instead of falling back to `<Html5Audio>`. |
| `fallbackHtml5AudioProps?` | `object` | -- | Props forwarded to `<Html5Audio>` on fallback (`onError`, `useWebAudioApi`, `acceptableTimeShiftInSeconds`, `pauseWhenBuffering`, `crossOrigin`). |
| `debugAudioScheduling?` | `boolean` | `false` | Log scheduling info to console. |

### 10.2 Volume Control, Fading, and Ducking

### Static Volume

```tsx
<Audio volume={0.5} src={staticFile('background.mp3')} />
```

### Fade In (Per-Frame Volume Callback)

```tsx
import {interpolate, staticFile} from 'remotion';
import {Audio} from '@remotion/media';

<Audio
  volume={(f) =>
    interpolate(f, [0, 30], [0, 1], {extrapolateLeft: 'clamp'})
  }
  src={staticFile('voice.mp3')}
/>
```

### Fade Out

```tsx
<Audio
  volume={(f) =>
    interpolate(f, [0, 90, 120], [1, 1, 0], {extrapolateRight: 'clamp'})
  }
  src={staticFile('music.mp3')}
/>
```

### Audio Ducking

Layer multiple `<Audio>` components with complementary volume curves -- lower background music volume when narration is active:

```tsx
<Audio volume={(f) => f >= 30 && f <= 150 ? 0.2 : 0.8} src={bgMusic} />
<Audio volume={(f) => f >= 30 && f <= 150 ? 1 : 0} src={narration} />
```

### 10.3 Multiple Audio Tracks

Mount multiple `<Audio>` components simultaneously. Each is an independent audio layer mixed in the final output:

```tsx
<AbsoluteFill>
  <Audio src={staticFile('background-music.mp3')} volume={0.3} />
  <Audio src={staticFile('narration.mp3')} volume={1} />
  <Audio src={staticFile('sfx-whoosh.wav')} />
</AbsoluteFill>
```

Use `<Sequence>` to time audio entry/exit points:

```tsx
<Sequence from={60}>
  <Audio src={staticFile('ding.wav')} />
</Sequence>
```

### 10.4 `@remotion/sfx` -- Sound Effects

Available from v4.0.429. Provides URL strings pointing to hosted WAV sound effects. Volume normalized to -3 dB peak. All usable without attribution (CC0 or similar). License: MIT (package).

### All Sound Effects

| Export | URL | Duration | Description |
|---|---|---|---|
| `whip` | `https://remotion.media/whip.wav` | 0.173s | Whip crack. 2ch, 96kHz, 24-bit. |
| `whoosh` | `https://remotion.media/whoosh.wav` | 0.154s | Whoosh/swipe. 1ch, 44.1kHz, 16-bit. |
| `pageTurn` | `https://remotion.media/page-turn.wav` | 0.400s | Page turn. 1ch, 44.1kHz, 16-bit. |
| `uiSwitch` | `https://remotion.media/switch.wav` | 0.330s | UI toggle switch. 2ch, 44.1kHz, 16-bit. |
| `mouseClick` | `https://remotion.media/mouse-click.wav` | 0.397s | Mouse click. 2ch, 44.1kHz, 16-bit. |
| `shutterModern` | `https://remotion.media/shutter-modern.wav` | 0.489s | Modern DSLR shutter. 1ch, 44.1kHz, 16-bit. |
| `shutterOld` | `https://remotion.media/shutter-old.wav` | 0.314s | Vintage camera shutter. 2ch, 44.1kHz, 16-bit. |
| `ding` | `https://remotion.media/ding.wav` | 1.400s | Notification ding. 2ch, 44.1kHz, 16-bit. v4.0.433+. |
| `bruh` | `https://remotion.media/bruh.wav` | 0.629s | Bruh meme sound. 2ch, 44.1kHz, 16-bit. v4.0.433+. |
| `vineBoom` | `https://remotion.media/vine-boom.wav` | 1.255s | Vine boom effect. 2ch, 44.1kHz, 16-bit. v4.0.433+. |
| `windowsXpError` | `https://remotion.media/windows-xp-error.wav` | 0.993s | Windows XP error. 1ch, 44.1kHz, 16-bit. v4.0.433+. |

**Usage:**

```tsx
import {whip} from '@remotion/sfx';
import {Audio} from '@remotion/media';

const MyVideo = () => <Audio src={whip} />;
```

All exports are plain URL strings -- they can also be used with `<Html5Audio>`, `preloadAudio()`, or any `src` prop.

### 10.5 Speech-to-Text

### `@remotion/install-whisper-cpp`

Available from v4.0.115. Provides cross-platform functions to install Whisper.cpp and transcribe audio locally. License: MIT.

#### `installWhisperCpp(options)`

Installs a Whisper.cpp version into a folder.

| Parameter | Type | Description |
|---|---|---|
| `to` | `string` | **Required.** Installation folder path. |
| `version` | `string` | **Required.** Whisper.cpp version without `v` prefix (e.g. `"1.5.5"`). |
| `printOutput?` | `boolean` | Print install output. Default: `true`. |
| `signal?` | `AbortSignal` | Abort controller signal. v4.0.156+. |

**Returns:** `Promise<{ alreadyExisted: boolean }>`

**Notes:**
- On Windows, a binary is downloaded (only semver format, nothing newer than 1.6.0).
- From 1.7.3+, `cmake` is required.
- Add the install folder to `.gitignore`.

#### `downloadWhisperModel(options)`

Downloads a Whisper model file.

| Parameter | Type | Description |
|---|---|---|
| `folder` | `string` | **Required.** Folder to download to. File saved as `ggml-${model}.bin`. |
| `model` | `string` | **Required.** Model name: `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`, `medium`, `medium.en`, `large-v1`, `large-v2`, `large-v3`, `large-v3-turbo`. |
| `onProgress?` | `(downloadedBytes: number, totalBytes: number) => void` | Progress callback. |
| `printOutput?` | `boolean` | Print progress. Default: `true`. |
| `signal?` | `AbortSignal` | Abort controller signal. v4.0.156+. |

**Returns:** `Promise<{ alreadyExisted: boolean }>`

#### `transcribe(options)`

Transcribes a media file using Whisper.cpp. Input must be 16-bit, 16kHz WAV.

| Parameter | Type | Description |
|---|---|---|
| `inputPath` | `string` | **Required.** Path to 16kHz WAV file. |
| `whisperPath` | `string` | **Required.** Path to whisper.cpp folder. |
| `whisperCppVersion` | `string` | **Required.** Version string. |
| `model?` | `string` | Model name. Default: `"base.en"`. |
| `tokenLevelTimestamps` | `boolean` | **Required.** Enable `--dtw` flag for precise timestamps. Requires v1.0.55+. |
| `modelFolder?` | `string` | Custom model folder. Default: `whisperPath/models`. |
| `translateToEnglish?` | `boolean` | Translate to English. Default: `false`. |
| `printOutput?` | `boolean` | Print output. Default: `true`. v4.0.132+. |
| `tokensPerItem?` | `number \| null` | Max tokens per item. Default: `1`. Only when `tokenLevelTimestamps: false`. v4.0.141+. |
| `splitOnWord?` | `boolean` | Cleaner word-for-word output. v4.0.208+. |
| `language?` | `string` | Spoken language code or name, or `"auto"`. v4.0.142+. |
| `signal?` | `AbortSignal` | Abort signal. v4.0.156+. |
| `onProgress?` | `(progress: number) => void` | Progress 0-1. v4.0.156+. |
| `flashAttention?` | `boolean` | Enable flash attention. v4.0.324+. |
| `additionalArgs?` | `(string \| [string, string])[]` | Extra CLI args. v4.0.324+. |

**Returns:** `Promise<TranscriptionJson>` -- contains `transcription` array with timestamps, offsets, text, and optional word-level tokens with `t_dtw` values.

#### `toCaptions(options)`

Converts `transcribe()` output into `@remotion/captions` `Caption[]` format. Available from v4.0.216.

| Parameter | Type | Description |
|---|---|---|
| `whisperCppOutput` | `TranscriptionJson` | **Required.** Output from `transcribe()`. |

**Returns:** `{ captions: Caption[] }`

#### `convertToCaptions()` (Deprecated)

Deprecated as of v4.0.216. Use `toCaptions()` + `createTikTokStyleCaptions()` instead.

### `@remotion/openai-whisper`

Available from v4.0.217. Converts OpenAI Whisper API output into Remotion `Caption[]`. License: MIT.

#### `openAiWhisperApiToCaptions(options)`

| Parameter | Type | Description |
|---|---|---|
| `transcription` | `OpenAI Transcription` | **Required.** Output from `openai.audio.transcriptions.create()` with `response_format: 'verbose_json'` and `timestamp_granularities: ['word']`. |

**Returns:** `{ captions: Caption[] }`

```tsx
import {openAiWhisperApiToCaptions} from '@remotion/openai-whisper';

const transcription = await openai.audio.transcriptions.create({
  file: fs.createReadStream('audio.mp3'),
  model: 'whisper-1',
  response_format: 'verbose_json',
  timestamp_granularities: ['word'],
});

const {captions} = openAiWhisperApiToCaptions({transcription});
```

**Note:** Do not call the OpenAI API from the browser -- your API key would be exposed.

### `@remotion/whisper-web`

**Experimental/unstable API.** Similar to `@remotion/install-whisper-cpp` but runs in the browser via WASM.

**Requirement:** `SharedArrayBuffer` support, which needs cross-origin isolation headers (`Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp`).

#### `canUseWhisperWeb()`

Checks whether the current browser environment supports `@remotion/whisper-web`.

**Returns:** `{ canUse: boolean; reason?: string }`

#### `getAvailableModels()`

Returns a list of available Whisper models that can be downloaded.

**Returns:** `WhisperModel[]`

#### `getLoadedModels()`

Returns models that have already been downloaded and are available for transcription.

**Returns:** `WhisperModel[]`

#### `downloadWhisperModel(options)`

Downloads a Whisper model for in-browser use.

| Parameter | Type | Description |
|---|---|---|
| `model` | `string` | **Required.** Model identifier. |
| `onProgress?` | `callback` | Download progress callback. |

**Returns:** `Promise<void>`

#### `transcribe(options)`

Transcribes audio in the browser using the WASM backend.

| Parameter | Type | Description |
|---|---|---|
| `audio` | `Float32Array` | **Required.** 16kHz mono audio samples. Use `resampleTo16kHz()` to prepare. |
| `model` | `string` | **Required.** Model identifier. |
| `onProgress?` | `callback` | Transcription progress callback. |

**Returns:** `Promise<WhisperWebTranscription>`

#### `resampleTo16kHz(options)`

Resamples audio data to 16kHz mono format required by Whisper.

| Parameter | Type | Description |
|---|---|---|
| `audioData` | `AudioBuffer \| Float32Array` | **Required.** Input audio. |
| `sampleRate` | `number` | **Required (if Float32Array).** Source sample rate. |

**Returns:** `Float32Array`

#### `toCaptions(options)`

Converts `@remotion/whisper-web` transcription output into `Caption[]` format.

| Parameter | Type | Description |
|---|---|---|
| `whisperWebOutput` | `WhisperWebTranscription` | **Required.** Output from `transcribe()`. |

**Returns:** `{ captions: Caption[] }`

> **Gap:** The `@remotion/whisper-web` API is marked as experimental. Parameter types and function signatures may change. The docs warn about a possible future switch to a WebGPU-based backend.


---

## 11. The Remotion Player

The `@remotion/player` package lets you embed Remotion video compositions directly inside any React application -- Next.js, Vite, Create React App, or any other React setup. Unlike server-side rendering via `@remotion/renderer`, the Player runs entirely in the browser and provides real-time interactive playback with seeking, play/pause, volume, fullscreen, and custom controls.

## Overview and Installation

Install the package into an existing React project:

```bash
npx remotion add @remotion/player
# or
npm i --save-exact @remotion/player@4.0.441
```

All `@remotion/*` packages must be pinned to the same version. Remove all `^` prefixes from version numbers to avoid conflicts.

## How It Works

The Player renders your Remotion composition as a React component inside a `<div>`. It does not use `<Composition>` -- you pass your video component directly via the `component` prop. The Player manages its own timeline, frame state, and audio playback internally. It scales the composition to fit its container using CSS transforms (similar to `object-fit`).

```tsx
import {Player} from '@remotion/player';
import {MyVideo} from './remotion/MyVideo';

export const App: React.FC = () => {
  return (
    <Player
      component={MyVideo}
      durationInFrames={120}
      compositionWidth={1920}
      compositionHeight={1080}
      fps={30}
    />
  );
};
```

## Components

The package exports two components:

- **`<Player>`** -- Full interactive video player with playback controls, seeking, volume, fullscreen.
- **`<Thumbnail>`** -- Renders a single frame of a composition as a static image. Available since v3.2.41.

### `<Thumbnail>` Usage

```tsx
import {Thumbnail} from '@remotion/player';
import {MyVideo} from './remotion/MyVideo';

export const App: React.FC = () => {
  return (
    <Thumbnail
      component={MyVideo}
      compositionWidth={600}
      compositionHeight={600}
      frameToDisplay={30}
      durationInFrames={120}
      fps={30}
      inputProps={{title: 'Foo'}}
    />
  );
};
```

## Full `<Player>` API -- Props

### Required Props

| Prop | Type | Description |
|------|------|-------------|
| `component` | `React.FC` | The React component to render. Mutually exclusive with `lazyComponent`. |
| `lazyComponent` | `() => Promise<{default: React.FC}>` | Dynamic import function. Wrap in `useCallback()` to avoid re-renders. Mutually exclusive with `component`. |
| `durationInFrames` | `number` (integer, > 0) | Total duration of the video in frames. |
| `fps` | `number` | Frame rate of the video. |
| `compositionWidth` | `number` | Composition width in pixels (the "logical" MP4 width). |
| `compositionHeight` | `number` | Composition height in pixels (the "logical" MP4 height). |

### Content Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `inputProps` | `object` | `undefined` | Props passed to the video component. TypeScript infers shape from `component`. |

### Playback Control Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `loop` | `boolean` | `false` | Restart when video ends. |
| `autoPlay` | `boolean` | `false` | Start playing immediately after load. |
| `playbackRate` | `number` | `1` | Speed multiplier (-4 to 4, excluding 0). Negative values play in reverse. Note: `<Audio>`, `<Video>`, and other media tags cannot play in reverse (browser limitation). |
| `initialFrame` | `number` | `0` | Frame to start from. Cannot be changed after mount. |
| `inFrame` | `number \| null` | `null` | Limit playback start frame. |
| `outFrame` | `number \| null` | `null` | Limit playback end frame. |
| `moveToBeginningWhenEnded` | `boolean` | `true` | Reset to frame 0 when ended. Only works if `loop` is false. (v3.1.3+) |
| `initiallyMuted` | `boolean` | `false` | Start muted. Useful for bypassing autoplay policies. (v3.3.81+) |

### UI / Controls Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `controls` | `boolean` | `false` | Show seek bar and play/pause button. |
| `showVolumeControls` | `boolean` | `true` | Show volume slider and mute button. Only effective when `controls` is `true`. |
| `allowFullscreen` | `boolean` | `true` | Allow fullscreen. Not supported on iOS Safari. |
| `clickToPlay` | `boolean` | `true` if `controls` is true, else `false` | Click to play/pause. |
| `doubleClickToFullscreen` | `boolean` | `false` | Double-click for fullscreen. Adds 200ms delay to single-click pause. Not supported on mobile. |
| `spaceKeyToPlayOrPause` | `boolean` | `true` | Space key toggles playback. Only works when `controls` is true. |
| `alwaysShowControls` | `boolean` | `false` | Keep controls visible at all times. (v3.3.55+) |
| `hideControlsWhenPointerDoesntMove` | `boolean \| number` | `true` (3000ms) | Auto-hide controls after mouse inactivity. Pass a number for custom delay in ms. (v4.0.124+) |
| `initiallyShowControls` | `boolean \| number` | `true` | Flash controls on mount, fade after 2s. Pass a number for custom duration in ms. (v3.2.24+) |
| `showPlaybackRateControl` | `boolean \| number[]` | `false` | Show gear icon for playback rate. `true` = `[0.5, 0.8, 1, 1.2, 1.5, 1.8, 2, 2.5, 3]`. (v3.3.98+) |
| `browserMediaControlsBehavior` | `string` | -- | Controls behavior for keyboard media keys / Chrome built-in controls. (v4.0.221+) |

### Poster Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `renderPoster` | `({height, width, isBuffering}) => ReactNode` | -- | Custom overlay UI. (v3.2.14+) |
| `showPosterWhenUnplayed` | `boolean` | `false` | Show poster before first play. |
| `showPosterWhenPaused` | `boolean` | `false` | Show poster when paused (not during scrub). |
| `showPosterWhenEnded` | `boolean` | `false` | Show poster when ended. Requires `moveToBeginningWhenEnded` = `false`. |
| `showPosterWhenBuffering` | `boolean` | `false` | Show poster when buffering and playing. (v4.0.111+) |
| `showPosterWhenBufferingAndPaused` | `boolean` | `false` | Show poster when buffering and paused. (v4.0.290+) |
| `posterFillMode` | `'player-size' \| 'composition-size'` | `'player-size'` | Poster sizing mode. (v4.0.78+) |

### Buffer & Loading Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `bufferStateDelayInMilliseconds` | `number` | `300` | Delay before showing buffering UI. `renderPoster` and `renderPlayPauseButton` report `isBuffering` only after this delay; `waiting`/`resume` events fire immediately. (v4.0.111+) |
| `renderLoading` | `({height, width}) => ReactNode` | -- | Custom loading UI (shown during Suspense or lazy component load). |
| `errorFallback` | `({error}) => ReactNode` | -- | Custom error UI when video component crashes. |

### Custom Render Props

| Prop | Type | Since | Description |
|------|------|-------|-------------|
| `renderPlayPauseButton` | `({playing, isBuffering}) => ReactNode \| null` | v3.2.32 | Custom play/pause button. Return `null` for default UI (v4.0.111+). |
| `renderFullscreenButton` | `({isFullscreen}) => ReactNode` | v3.2.32 | Custom fullscreen button. |
| `renderMuteButton` | `({muted, volume}) => ReactNode` | v4.0.188 | Custom mute button. Click action is disabled; attach handlers via PlayerRef. |
| `renderVolumeSlider` | `({isVertical, volume, onBlur, inputRef, setVolume}) => ReactNode` | v4.0.188 | Custom volume slider. |
| `renderCustomControls` | `() => ReactNode \| null` | v4.0.418 | Extra controls rendered between playback controls and fullscreen button. |

### Audio Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `numberOfSharedAudioTags` | `number` | `5` | Pre-mounted silent audio tags for iOS Safari autoplay workaround. Set `0` to opt out. Cannot be changed after mount. |
| `volumePersistenceKey` | `string` | `"remotion.volumePreference"` | localStorage key for volume persistence. (v4.0.305+) |

### Styling & Misc Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `style` | `CSSProperties` | -- | Style for the container `<div>`. Use `style={{width: 400}}` to scale. |
| `className` | `string` | -- | CSS class for the container. (v3.1.3+) |
| `overflowVisible` | `boolean` | `false` | Render content outside canvas bounds. Useful for drag-and-drop. (v4.0.173+) |
| `overrideInternalClassName` | `string` | `'__remotion-player'` | Replace the internal class name. (v4.0.233+) |
| `logLevel` | `string` | -- | Log verbosity level. (v4.0.250+) |
| `noSuspense` | `boolean` | `false` | Disable React Suspense. Useful for tests. (v4.0.271+) |
| `acknowledgeRemotionLicense` | `boolean` | `false` | Suppress license console message. (v4.0.253+) |

## PlayerRef -- Imperative API

Attach a ref to the `<Player>` to control it programmatically:

```tsx
import {Player, PlayerRef} from '@remotion/player';
import {useRef} from 'react';

const playerRef = useRef<PlayerRef>(null);
// Usage: playerRef.current?.play();
```

### Playback Methods

| Method | Description |
|--------|-------------|
| `play(event?)` | Start playback. Pass the SyntheticEvent from a user gesture to bypass autoplay restrictions. |
| `pause()` | Pause playback. |
| `toggle(event?)` | Toggle play/pause. |
| `pauseAndReturnToPlayStart()` | Pause and return to the frame where playback last started. (v4.0.67+) |
| `seekTo(frame)` | Seek to a specific frame number. Briefly pauses if playing. |

### State Query Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getCurrentFrame()` | `number` | Current frame index. |
| `isPlaying()` | `boolean` | Whether video is playing. (v2.5.7+) |
| `isMuted()` | `boolean` | Whether audio is muted. |
| `getVolume()` | `number` | Volume (0-1). |
| `isFullscreen()` | `boolean` | Whether in fullscreen mode. |
| `getScale()` | `number` | Scale factor (e.g., 0.5 if player is half composition width). (v3.2.24+) |
| `getContainerNode()` | `HTMLDivElement \| null` | The player's container DOM node. (v2.4.2+) |

### Control Methods

| Method | Description |
|--------|-------------|
| `mute()` | Mute audio. |
| `unmute()` | Unmute audio. |
| `setVolume(volume)` | Set volume (0-1). Throws if out of range. |
| `requestFullscreen()` | Enter fullscreen. Throws if `allowFullscreen` is false or unsupported. |
| `exitFullscreen()` | Exit fullscreen. |

### Event Methods

| Method | Description |
|--------|-------------|
| `addEventListener(event, callback)` | Subscribe to a player event. |
| `removeEventListener(event, callback)` | Unsubscribe from a player event. |

## Player Events

All events are accessed via `PlayerRef.addEventListener()`.

| Event | Payload | Description |
|-------|---------|-------------|
| `play` | -- | Video started or resumed playing. |
| `pause` | -- | Video paused or ended. |
| `ended` | -- | Video ended (only fires when `loop` is false). |
| `seeked` | `{frame: number}` | User seeked via scrub bar or `seekTo()`. Fires on every frame during seek. |
| `timeupdate` | `{frame: number}` | Periodic time updates during playback (throttled, max every 250ms). |
| `frameupdate` | `{frame: number}` | Every frame change during both playback and seeking. (v3.2.27+) |
| `ratechange` | `{playbackRate: number}` | Playback rate changed. |
| `volumechange` | `{volume: number}` | Volume changed. (v3.3.86+) |
| `scalechange` | `{scale: number}` | Player scale changed. (v3.3.86+) |
| `mutechange` | `{isMuted: boolean}` | Mute state changed. (v3.3.98+) |
| `fullscreenchange` | `{isFullscreen: boolean}` | Fullscreen state changed. (v3.2.0+) |
| `error` | `{error: Error}` | Uncaught error in the video component's render. |
| `waiting` | -- | Player entered buffering state. Fires immediately (not delayed by `bufferStateDelayInMilliseconds`). (v4.0.111+) |
| `resume` | -- | Player exited buffering state. (v4.0.111+) |

### Event Guidance: `seeked` vs `timeupdate` vs `frameupdate`

- **`seeked`**: Only fires during user seeking. Fires on every frame -- can cause performance issues if used for expensive renders.
- **`timeupdate`**: Fires during playback only, throttled to ~250ms. Best for non-critical UI updates.
- **`frameupdate`**: Fires for every frame change in all scenarios. Best when you need precise frame-level synchronization.

## `<Thumbnail>` API

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| `component` / `lazyComponent` | `React.FC` / `() => Promise` | Yes | Same as Player. |
| `compositionWidth` | `number` | Yes | Composition width in pixels. |
| `compositionHeight` | `number` | Yes | Composition height in pixels. |
| `frameToDisplay` | `number` | Yes | Which frame to render. |
| `durationInFrames` | `number` | Yes | Required for `useVideoConfig()` to work. |
| `fps` | `number` | Yes | Required for `useVideoConfig()` to work. |
| `inputProps` | `object` | No | Props for the component. |
| `style` | `CSSProperties` | No | Container style. |
| `className` | `string` | No | Container class. (v3.1.3+) |
| `overflowVisible` | `boolean` | No | Render outside canvas. (v4.0.173+) |
| `errorFallback` | `({error}) => ReactNode` | No | Custom error UI. |
| `renderLoading` | `({height, width}) => ReactNode` | No | Custom loading UI. |
| `logLevel` | `string` | No | Log verbosity. (v4.0.250+) |
| `noSuspense` | `boolean` | No | Disable Suspense. (v4.0.271+) |

### ThumbnailRef

| Method | Description |
|--------|-------------|
| `getScale()` | Scale factor of the thumbnail vs composition size. |
| `getContainerNode()` | The thumbnail's container DOM node. |
| `addEventListener(event, cb)` | Listen to events (`error`, `waiting`, `resume`). |
| `removeEventListener(event, cb)` | Remove event listener. |

## Non-React Usage

> **Gap:** The Remotion docs do not document any official way to use `@remotion/player` outside of React. The Player is a React component and requires a React render tree. There is no Web Component wrapper, vanilla JS API, or framework-agnostic embedding method documented. For non-React frameworks (Vue, Svelte, Angular), you would need to mount a React root manually.

## Performance Considerations

- **Shared Audio Tags**: The Player pre-mounts `numberOfSharedAudioTags` (default 5) silent audio elements on user interaction to work around iOS Safari autoplay restrictions. If your composition uses more `<Html5Audio>` tags than available shared tags, an error is thrown.
- **Buffering**: Use `bufferStateDelayInMilliseconds` (default 300ms) to prevent UI jank from brief buffer states. The `waiting`/`resume` events fire immediately, but poster/button `isBuffering` state is delayed.
- **Flickers**: Unloaded assets can cause flickers. Use preloading (`@remotion/preload`) and premounting to mitigate. The docs have a dedicated troubleshooting guide for player flicker issues.
- **`lazyComponent` re-renders**: Always wrap `lazyComponent` in `useCallback()` to prevent the Player from re-mounting the component on every render.
- **Error boundaries**: The Player uses React error boundaries internally. Only render-phase errors are caught; errors in event handlers or async code will not be caught.

## Guide Topics

The official docs cover these additional Player topics (not fully reproduced here):

- **Sizing/Scaling**: Use `style={{width}}` to control displayed size; `compositionWidth`/`compositionHeight` define the logical canvas.
- **Autoplay**: Browser policies require user interaction before audio playback. Pass `SyntheticEvent` to `play()` or use `initiallyMuted`.
- **Display Time**: Use `getCurrentFrame()` with special considerations for synchronized display components.
- **Preloading Assets**: Use `@remotion/preload` to ensure assets are ready when they appear.
- **Buffer State**: Player can pause while assets load; implement custom buffering UI via poster.
- **Premounting**: Mount components earlier to allow time to load.
- **Drag & Drop**: Enable with `overflowVisible` for interactive canvas elements.
- **Custom Controls**: Use render props and the `renderCustomControls` slot for custom UI.
- **Media Keys**: Configure browser media key behavior via `browserMediaControlsBehavior`.

---

## 12. CLI Reference

## Command Overview

Install the CLI via `@remotion/cli`. Run commands with:
- `npx remotion <command>` (npm)
- `yarn remotion <command>` (Yarn)
- `pnpm exec remotion <command>` (pnpm)
- `bunx remotion <command>` (Bun — uses Node by default; use `remotionb` for Bun runtime)

Inside an npm script, the `npx` prefix is not needed:
```json
{
  "scripts": {
    "render": "remotion render"
  }
}
```

### Runtime Variants

| Runtime | Command | Since |
|---------|---------|-------|
| Node.js (default) | `npx remotion` | v1.0 |
| Bun | `remotionb` | v4.0.118 |
| Deno (experimental, unsupported) | `remotiond` | v4.0.227 |

## All Commands

### `npx remotion studio`

Alias: `npx remotion preview`. Starts the Remotion Studio (interactive development environment).

```
npx remotion studio <entry-point>?
```

**Flags:** `--props`, `--config`, `--env-file`, `--log`, `--port`, `--public-dir`, `--disable-keyboard-shortcuts`, `--experimental-rspack`, `--webpack-poll`, `--no-open`, `--browser`, `--browser-args`, `--beep-on-finish`, `--ipv4`, `--number-of-shared-audio-tags`, `--cross-site-isolation`, `--disable-ask-ai`, `--force-new`, `--public-license-key`, `--enable-experimental-client-side-rendering`.

### `npx remotion render`

Render a video or audio. See Section 4 above for the full flag reference.

```
npx remotion render <entry-point|serve-url>? <composition-id> <output-location>
```

### `npx remotion still`

Render a single still frame. See Section 4 above for the full flag reference.

```
npx remotion still <serve-url|entry-point>? [<composition-id>] [<output-location>]
```

### `npx remotion compositions`

Print list of composition IDs from an entry point. Available since v2.6.12.

```
npx remotion compositions <serve-url|entry-file>?
```

**Flags:** `--props`, `--config`, `--env-file`, `--bundle-cache`, `--log`, `--port`, `--public-dir`, `--timeout`, `--ignore-certificate-errors`, `--disable-web-security`, `--dark-mode`, `--enable-multiprocess-on-linux`, `--user-agent`, `--media-cache-size-in-bytes`, `--offthreadvideo-cache-size-in-bytes`, `--offthreadvideo-video-threads`, `--binaries-directory`, `--chrome-mode`, `--quiet` / `--q` (only print IDs separated by spaces).

### `npx remotion bundle`

Create a Remotion Bundle. Available since v4.0.89. Equivalent to the `bundle()` Node.js API.

```
npx remotion bundle <serve-url|entry-file>?
```

**Flags:**

| Flag | Since | Description |
|------|-------|-------------|
| `--config` | v4.0.89 | Path to config file. |
| `--log` | v4.0.89 | Log level: `trace`, `verbose`, `info`, `warn`, `error`. |
| `--public-dir` | v4.0.89 | Location of public directory. |
| `--out-dir` | v4.0.89 | Output directory for the bundle. Default: `build` adjacent to Remotion Root. |
| `--public-path` | v4.0.127 | URL path where the bundle will be hosted. Default: `/`. |
| `--disable-git-source` | v4.0.182 | Disable Git Source integration in Studio. |
| `--experimental-rspack` | v4.0.426 | Use Rspack instead of Webpack. |

### `npx remotion benchmark`

Measure render time by running a render multiple times. Available since v3.2.28.

```
npx remotion benchmark src/index.ts [composition-ids]
```

Multiple composition IDs can be separated by comma. Inherits most flags from `npx remotion render`.

**Unique flags:**

| Flag | Description |
|------|-------------|
| `--runs` | Number of render iterations. Default: `3`. |
| `--concurrencies` | Comma-separated concurrency values to compare. |

### `npx remotion browser`

Commands for managing the browser used by Remotion. Available since v4.0.137.

Subcommands:
- `npx remotion browser ensure` — Ensure a browser is downloaded and ready for rendering.

### `npx remotion versions`

Print installed Remotion package versions and check alignment. Available since v2.6.2. Also checks `zod` and `mediabunny` versions.

```
npx remotion versions
```

### `npx remotion upgrade`

Upgrade all Remotion-related packages (and `mediabunny` if installed).

```
npx remotion upgrade
```

**Flags:**

| Flag | Since | Description |
|------|-------|-------------|
| `--package-manager` | v3.2.33 | Force `npm`, `yarn`, `pnpm`, or `bun`. |
| `--version` | v4.0.15 | Install a specific version. Also enables downgrading. |

Additional arguments are forwarded to the package manager.

### `npx remotion add`

Add Remotion packages with the same version as existing installations.

```
npx remotion add <package-name...>
```

Supports `@remotion/*` packages, `zod`, and `mediabunny`. Detects current Remotion version and installs matching versions.

**Flags:** `--package-manager` (v4.0.367+).

### `npx remotion gpu`

Print Chrome GPU usage information. Available since v4.0.52.

```
npx remotion gpu --gl=angle
```

**Flags:** `--log`, `--gl`, `--chrome-mode`.

### `npx remotion ffmpeg` / `npx remotion ffprobe`

Execute `ffmpeg` or `ffprobe` commands using Remotion's bundled binaries.

### `npx remotion help`

Print available commands and flags.

```
npx remotion help
```

---

## Environment Variable Configuration

Environment variables can be provided to Remotion renders via:
- `--env-file` flag pointing to a `.env` file
- The `envVariables` option in Node.js APIs (an object of key-value pairs)
- Standard `process.env` in Node.js

## Config File — `remotion.config.ts`

Remotion reads configuration from `remotion.config.ts` at the project root. This file can set defaults for CLI flags so they do not need to be passed every time.

> **Gap:** The source docs reference the config file extensively but the detailed config file API (all `Config.*` methods) was not included in the source folders provided for this section. The config file supports setting codec, CRF, image format, pixel format, log level, overwrite behavior, JPEG quality, concurrency, browser executable, OpenGL renderer, and many other options programmatically. See the Remotion documentation at `/docs/config` for the full `Config` API.

---

## 13. Node.js API Reference

All Node.js rendering APIs are part of the `@remotion/renderer` package. The bundling API is in `@remotion/bundler`.

## `bundle()`

*Package: `@remotion/bundler`*

Takes a Remotion project and bundles it using Webpack, producing a static bundle that can be passed to rendering functions.

```ts
import { bundle } from "@remotion/bundler";

const bundlePath = await bundle({
  entryPoint: require.resolve("./src/index.ts"),
});
```

The returned string is a local file path to the bundle directory. Pass it as `serveUrl` to `renderMedia()`, `renderStill()`, `getCompositions()`, or `selectComposition()`.

> **Gap:** The `bundle()` function's full parameter table was not included in the provided source files (only the `@remotion/bundler` overview was available). The function accepts `entryPoint`, `webpackOverride`, `outDir`, `publicDir`, `publicPath`, `onProgress`, and other options. See the Remotion documentation at `/docs/bundle` for the complete signature.

---

## `renderMedia()`

*Package: `@remotion/renderer`. Available since v3.0.*

Renders a video or audio programmatically.

```ts
import { renderMedia, selectComposition } from "@remotion/renderer";

const composition = await selectComposition({
  serveUrl,
  id: "my-video",
  inputProps,
});

const { buffer, slowestFrames } = await renderMedia({
  composition,
  serveUrl,
  codec: "h264",
  outputLocation: "/path/to/output.mp4",
  inputProps,
});
```

### Complete Parameter Table

| Parameter | Type | Required | Since | Description |
|-----------|------|----------|-------|-------------|
| `serveUrl` | `string` | Yes | v3.0 | Path to Webpack bundle (from `bundle()`) or URL where bundle is hosted. |
| `composition` | `VideoConfig` | Yes | v3.0 | Object with `id`, `width`, `height`, `fps`, `durationInFrames`, `defaultProps`, `props`. From `selectComposition()` or `getCompositions()`. |
| `codec` | `Codec` | Yes | v3.0 | `"h264"`, `"h265"`, `"vp8"`, `"vp9"`, `"av1"`, `"prores"`, `"h264-mkv"`, `"mp3"`, `"aac"`, `"wav"`, `"png"`. |
| `outputLocation` | `string \| null` | No | v3.0 | Absolute or relative path for output file. If `null`, returns buffer in memory. |
| `inputProps` | `object` | No | v3.0 | JSON object of props passed to the composition. |
| `port` | `number` | No | v3.0 | Preferred port for serving the project. |
| `frameRange` | `number \| [number, number] \| [number, null]` | No | v3.0 | Single frame, frame range, or `null` for all frames. `[n, null]` from v4.0.421. |
| `concurrency` | `number \| string \| null` | No | v3.0 | Parallel render processes. Number, percentage string (e.g. `"50%"`), or `null`. Default: half CPU threads. |
| `metadata` | `object` | No | v4.0.216 | Metadata to embed in the output video. |
| `logLevel` | `"trace" \| "verbose" \| "info" \| "warn" \| "error"` | No | v4.0.0 | Log verbosity. Default: `"info"`. |
| `onArtifact` | `OnArtifact` | No | v4.0.176 | Callback for artifacts emitted by `<Artifact>` component. |
| `audioCodec` | `AudioCodec` | No | v3.0 | `"aac"`, `"opus"`, `"mp3"`, `"pcm-16"`. Default depends on `codec`. |
| `audioBitrate` | `string` | No | v3.2.32 | Target audio bitrate (e.g. `"320k"`, `"512K"`, `"1M"`). Default: `"320k"`. |
| `videoBitrate` | `string` | No | v3.2.32 | Target video bitrate (e.g. `"512K"`, `"1M"`). |
| `crf` | `number \| null` | No | v1.4 | Constant Rate Factor for quality. Cannot be used with hardware acceleration. |
| `bufferSize` | `string` | No | v4.0.78 | Buffer size for rate control. |
| `maxRate` | `string` | No | v4.0.78 | Maximum bitrate for rate control. |
| `imageFormat` | `"jpeg" \| "png" \| "none"` | No | v3.0 | Frame image format. `jpeg` is fastest (default), `png` for transparency, `none` for audio-only. |
| `browserExecutable` | `string` | No | v3.0.11 | Absolute path to browser executable. |
| `everyNthFrame` | `number` | No | v3.1.0 | Render every Nth frame. GIF rendering only. |
| `numberOfGifLoops` | `number \| null` | No | v3.1.0 | GIF loop count. `null` = infinite. |
| `pixelFormat` | `PixelFormat` | No | v3.0 | Custom pixel format (e.g., `yuva420p` for transparent video). |
| `envVariables` | `Record<string, string>` | No | v3.0 | Environment variables injected into the project. |
| `jpegQuality` | `number` | No | v3.0 | JPEG quality 0-100. Default: browser default (~80). |
| `muted` | `boolean` | No | v3.2.1 | Disable audio output. |
| `hardwareAcceleration` | `"disable" \| "if-possible" \| "required"` | No | v4.0.228 | GPU-accelerated encoding. Default: `"disable"`. |
| `enforceAudioTrack` | `boolean` | No | v3.2.1 | Render silent audio track if none exists. |
| `puppeteerInstance` | `Browser` | No | v3.0 | Reusable browser instance from `openBrowser()`. |
| `scale` | `number` | No | v3.0 | Scale output dimensions. |
| `overwrite` | `boolean` | No | v3.0 | Overwrite existing output file. |
| `onStart` | `(data: OnStartData) => void` | No | v3.0 | Callback when rendering begins. Receives `frameCount`, `parallelEncoding` (v4.0.52), `resolvedConcurrency` (v4.0.180). |
| `onProgress` | `RenderMediaOnProgress` | No | v3.0 | Progress callback with `progress` (0-1), `renderedFrames`, `encodedFrames`, `renderedDoneIn`, `encodedDoneIn`, `stitchStage`. |
| `onDownload` | `RenderMediaOnDownload` | No | v3.0 | Callback when audio/video assets are downloaded. |
| `proResProfile` | `string` | No | v3.0 | ProRes profile: `"4444-xq"`, `"4444"`, `"hq"`, `"standard"`, `"light"`, `"proxy"`. |
| `x264Preset` | `string` | No | v4.2.2 | x264 encoding preset. |
| `onBrowserLog` | `(log: BrowserLog) => void` | No | v3.0 | Callback for `console.*` calls from the project. Receives `type`, `text`, `stackTrace`. |
| `timeoutInMilliseconds` | `number` | No | v3.0 | Timeout per frame for `delayRender()` resolution. Default: `30000`. |
| `cancelSignal` | `CancelSignal` | No | v3.0.15 | Token from `makeCancelSignal()` to cancel the render. |
| `chromiumOptions` | `ChromiumOptions` | No | v2.6.5 | Object with `disableWebSecurity`, `enableMultiProcessOnLinux`, `ignoreCertificateErrors`, `gl`, `userAgent`, `darkMode`. |
| `chromeMode` | `"headless-shell" \| "chrome-for-testing"` | No | v4.0.248 | Chrome mode. Default: `"headless-shell"`. |
| `ffmpegOverride` | `FfmpegOverrideFn` | No | v3.2.22 | Modify FFmpeg command arguments. Receives `{ type, args }`, returns modified args. Use with caution. |
| `disallowParallelEncoding` | `boolean` | No | v3.2.29 | Disable parallel encoding. More memory-efficient but slower. |
| `mediaCacheSizeInBytes` | `number \| null` | No | v4.0.352 | Cache size for `<Video>`/`<Audio>`. Default: half system memory. |
| `offthreadVideoCacheSizeInBytes` | `number \| null` | No | v4.0.23 | Cache for `<OffthreadVideo>` frames. Default: half system memory. |
| `offthreadVideoThreads` | `number` | No | v4.0.261 | Threads for OffthreadVideo decoding. |
| `colorSpace` | `string` | No | v4.0.28 | `"default"`, `"bt601"`, `"bt709"`, `"bt2020-ncl"`, `"bt2020-cl"`. |
| `repro` | `boolean` | No | v4.0.88 | Create reproduction bundle. Default: `false`. |
| `binariesDirectory` | `string \| null` | No | v4.0.120 | Path to Remotion platform binaries. Default: `node_modules/@remotion/compositor-*`. |
| `separateAudioTo` | `string` | No | v4.0.123 | Write audio to a separate file. |
| `forSeamlessAacConcatenation` | `boolean` | No | v4.0.123 | Prepare for seamless AAC concatenation. |
| `compositionStart` | `number` | No | v4.0.279 | For distributed rendering only. |
| `onBrowserDownload` | `OnBrowserDownload` | No | v4.0.137 | Hook into browser download progress. |
| `licenseKey` | `string` | No | v4.0.409 | Remotion license key. |
| `isProduction` | `boolean` | No | v4.0.409 | Whether this is a production render. Default: `true`. |

### Return Value (v4.0+)

```ts
{
  buffer: Buffer | null;       // Buffer if outputLocation is null, otherwise null
  slowestFrames: Array<{       // 10 slowest frames
    frame: number;
    time: number;
  }>;
  contentType: string;         // e.g., "video/mp4", "video/webm", "image/gif" (v4.0.426+)
}
```

**Compatibility:** Node.js, Bun. Not available in browsers, serverless functions, or the Player.

---

## `renderStill()`

*Package: `@remotion/renderer`. Available since v2.3.*

Renders a single frame to an image file.

```ts
import { renderStill } from "@remotion/renderer";

await renderStill({
  composition,
  serveUrl,
  output: "/tmp/still.png",
  inputProps: { custom: "data" },
});
```

### Complete Parameter Table

| Parameter | Type | Required | Since | Description |
|-----------|------|----------|-------|-------------|
| `composition` | `VideoConfig` | Yes | v2.3 | Composition config from `selectComposition()` or `getCompositions()`. |
| `serveUrl` | `string` | Yes | v2.3 | Path to bundle or URL. |
| `output` | `string` | No | v2.3 | Absolute path for the output image. If omitted, returns buffer. |
| `inputProps` | `object` | No | v2.3 | JSON props for the composition. |
| `port` | `number` | No | v2.3 | Preferred port. |
| `frame` | `number` | No | v2.3 | Frame number to render. Default: `0`. Negative values allowed from v3.2.27. |
| `imageFormat` | `"png" \| "jpeg" \| "webp" \| "pdf"` | No | v2.3 | Output format. Default: `"png"`. |
| `scale` | `number` | No | v2.3 | Scale output dimensions. |
| `jpegQuality` | `number` | No | v2.3 | JPEG quality 0-100. Only with `imageFormat: "jpeg"`. |
| `puppeteerInstance` | `Browser` | No | v2.3 | Reusable browser from `openBrowser()`. |
| `envVariables` | `Record<string, string>` | No | v2.3 | Environment variables. |
| `logLevel` | `string` | No | v4.0.115 | Log verbosity. |
| `onArtifact` | `OnArtifact` | No | v4.0.176 | Artifact callback. |
| `overwrite` | `boolean` | No | v2.3 | Overwrite existing output. Default: `true`. |
| `browserExecutable` | `string` | No | v2.3.1 | Browser executable path. |
| `onBrowserLog` | `(log: BrowserLog) => void` | No | v3.3.93 | Console log callback. |
| `timeoutInMilliseconds` | `number` | No | v2.6.3 | Timeout in ms. Default: `30000`. |
| `cancelSignal` | `CancelSignal` | No | v3.0.15 | Cancellation token. |
| `chromiumOptions` | `ChromiumOptions` | No | v2.6.5 | Chromium flags. |
| `chromeMode` | `string` | No | v4.0.248 | Chrome mode. |
| `mediaCacheSizeInBytes` | `number \| null` | No | v4.0.352 | Media cache size. |
| `offthreadVideoCacheSizeInBytes` | `number \| null` | No | v4.0.23 | OffthreadVideo cache. |
| `offthreadVideoThreads` | `number` | No | v4.0.261 | OffthreadVideo threads. |
| `binariesDirectory` | `string \| null` | No | v4.0.120 | Binaries directory. |
| `onBrowserDownload` | `OnBrowserDownload` | No | v4.0.137 | Browser download hook. |
| `licenseKey` | `string` | No | v4.0.409 | License key. |
| `isProduction` | `boolean` | No | v4.0.409 | Production flag. Default: `true`. |

### Return Value

```ts
{
  buffer: Buffer | null;    // Buffer if no output path provided, otherwise null (v3.3.9+)
  contentType: string;      // e.g., "image/png", "image/jpeg" (v4.0.426+)
}
```

**Compatibility:** Node.js, Bun.

---

## `renderFrames()`

*Package: `@remotion/renderer`.*

Renders a series of images and computes audio mixing information. This is the lower-level API — prefer `renderMedia()` for most use cases.

```ts
import { renderFrames } from "@remotion/renderer";

const { frameCount, assetsInfo } = await renderFrames({
  composition,
  serveUrl,
  onStart: ({ frameCount }) => console.log(`Rendering ${frameCount} frames`),
  onFrameUpdate: (framesRendered, frame, timeMs) => {},
  outputDir: "/path/to/frames",
  inputProps: {},
  imageFormat: "jpeg",
});
```

### Key Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `composition` | `VideoConfig` | Yes | Composition config. |
| `serveUrl` | `string` | Yes | Bundle path or URL. |
| `onStart` | `(data: OnStartData) => void` | Yes | Called when rendering begins. |
| `onFrameUpdate` | `(framesRendered, frame, timeMs) => void` | Yes | Called after each frame renders. |
| `outputDir` | `string \| null` | Yes | Directory for frame images. Pass `null` to use `onFrameBuffer` instead. |
| `inputProps` | `object` | Yes | Props for the composition. |
| `imageFormat` | `"jpeg" \| "png" \| "none"` | No | Frame format. Default: `"jpeg"`. |
| `imageSequencePattern` | `string` | No | File naming pattern with `[frame]` and `[ext]` placeholders. Default: `"element-[frame].[ext]"`. Since v4.0.313. |
| `concurrency` | `number \| string \| null` | No | Parallel processes. |
| `scale` | `number` | No | Scale factor. |
| `jpegQuality` | `number` | No | JPEG quality 0-100. |
| `port` | `number` | No | Preferred port. |
| `frameRange` | `number \| [number, number] \| [number, null]` | No | Frame range. |
| `muted` | `boolean` | No | Disable audio. |
| `logLevel` | `string` | No | Log verbosity. |
| `onArtifact` | `function` | No | Artifact callback. |
| `puppeteerInstance` | `Browser` | No | Reusable browser. |
| `envVariables` | `Record<string, string>` | No | Environment variables. |
| `onBrowserLog` | `function` | No | Console log callback. |
| `browserExecutable` | `string` | No | Browser path. |
| `cancelSignal` | `CancelSignal` | No | Cancellation token. |
| `onFrameBuffer` | `function` | No | Receive frame as Buffer (when `outputDir` is `null`). |
| `timeoutInMilliseconds` | `number` | No | Frame timeout. Default: `30000`. |
| `everyNthFrame` | `number` | No | Render every Nth frame. |
| `chromiumOptions` | `ChromiumOptions` | No | Chromium flags. |
| `chromeMode` | `string` | No | Chrome mode. |
| `offthreadVideoCacheSizeInBytes` | `number \| null` | No | OffthreadVideo cache. |
| `mediaCacheSizeInBytes` | `number \| null` | No | Media cache. |
| `offthreadVideoThreads` | `number` | No | OffthreadVideo threads. |
| `binariesDirectory` | `string \| null` | No | Binaries directory. |
| `onBrowserDownload` | `function` | No | Browser download hook. |

### Return Value

```ts
{
  frameCount: number;          // Number of frames rendered
  assetsInfo: RenderAssetInfo; // Internal data for stitchFramesToVideo()
}
```

---

## `stitchFramesToVideo()`

*Package: `@remotion/renderer`.*

Takes frame images and audio info from `renderFrames()` and encodes them into a video. Prefer `renderMedia()` for most cases.

```ts
import { stitchFramesToVideo } from "@remotion/renderer";

await stitchFramesToVideo({
  fps: 30,
  width: 1920,
  height: 1080,
  assetsInfo,  // from renderFrames()
  outputLocation: "/path/to/output.mp4",
  codec: "h264",
});
```

### Key Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `fps` | `number` | Yes | Output frame rate. |
| `width` | `number` | Yes | Output width in pixels. |
| `height` | `number` | Yes | Output height in pixels. |
| `assetsInfo` | `RenderAssetInfo` | Yes | From `renderFrames()` return value. |
| `outputLocation` | `string \| null` | No | Output file path. If `null`, returns buffer. |
| `force` | `boolean` | No | Overwrite existing file. Default: `true`. |
| `pixelFormat` | `string` | No | Pixel format. Default: `yuv420p`. |
| `codec` | `Codec` | No | Video codec. Default: `h264`. |
| `audioCodec` | `string` | No | Audio encoding. |
| `audioBitrate` | `string` | No | Audio bitrate. |
| `videoBitrate` | `string` | No | Video bitrate. |
| `bufferSize` | `string` | No | Rate control buffer. |
| `maxRate` | `string` | No | Maximum bitrate. |
| `crf` | `number` | No | Constant rate factor. |
| `proResProfile` | `string` | No | ProRes profile. |
| `x264Preset` | `string` | No | x264 preset. |
| `metadata` | `object` | No | Video metadata. Since v4.0.216. |
| `onProgress` | `(frameNumber: number) => void` | No | Encoding progress callback. |
| `onDownload` | `(src: string) => void` | No | Asset download notification. |
| `numberOfGifLoops` | `number \| null` | No | GIF loop count. |
| `muted` | `boolean` | No | Disable audio. |
| `hardwareAcceleration` | `string` | No | GPU encoding. |
| `cancelSignal` | `CancelSignal` | No | Cancellation token. |
| `enforceAudioTrack` | `boolean` | No | Force silent audio track. |
| `colorSpace` | `string` | No | Color space. |
| `ffmpegOverride` | `FfmpegOverrideFn` | No | Modify FFmpeg arguments. |
| `binariesDirectory` | `string \| null` | No | Binaries directory. |
| `separateAudioTo` | `string` | No | Separate audio file path. |
| `forSeamlessAacConcatenation` | `boolean` | No | AAC concatenation support. |

### Return Value

Promise resolving to `void` (output written to `outputLocation`), or a `Buffer` if `outputLocation` is `null`.

---

## `getCompositions()`

*Package: `@remotion/renderer`.*

Gets all compositions defined in a Remotion project. Evaluates `calculateMetadata()` for every composition.

```ts
import { getCompositions } from "@remotion/renderer";

const compositions = await getCompositions(serveUrl, {
  inputProps: {},
});
// Returns: [{ id, width, height, fps, durationInFrames, defaultProps }, ...]
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serveUrlOrWebpackUrl` | `string` | Yes (positional) | Bundle path or URL. |
| `inputProps` | `object` | No (required from v5.0) | Input props. |
| `puppeteerInstance` | `Browser` | No | Reusable browser. |
| `browserExecutable` | `string` | No | Browser path. |
| `onBrowserLog` | `function` | No | Console callback. |
| `timeoutInMilliseconds` | `number` | No | Timeout. Default: `30000`. |
| `port` | `number` | No | Preferred port. |
| `logLevel` | `string` | No | Log level. |
| `chromiumOptions` | `ChromiumOptions` | No | Chromium flags. |
| `offthreadVideoCacheSizeInBytes` | `number \| null` | No | OffthreadVideo cache. |
| `mediaCacheSizeInBytes` | `number \| null` | No | Media cache. |
| `offthreadVideoThreads` | `number` | No | OffthreadVideo threads. |
| `binariesDirectory` | `string \| null` | No | Binaries directory. |
| `onBrowserDownload` | `function` | No | Browser download hook. |
| `chromeMode` | `string` | No | Chrome mode. |

### Return Value

```ts
Promise<Array<{
  id: string;
  width: number;
  height: number;
  fps: number;
  durationInFrames: number;
  defaultProps: object | undefined;
}>>
```

---

## `selectComposition()`

*Package: `@remotion/renderer`. Available since v4.0.0.*

Evaluates a single composition by ID, running its `calculateMetadata()` function. More efficient than `getCompositions()` when you know which composition to render.

```ts
import { bundle } from "@remotion/bundler";
import { selectComposition } from "@remotion/renderer";

const bundled = await bundle({ entryPoint: require.resolve("./src/index.ts") });
const composition = await selectComposition({
  serveUrl: bundled,
  id: "MyComposition",
  inputProps: {},
});

console.log(composition.width, composition.height, composition.fps, composition.durationInFrames);
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serveUrl` | `string` | Yes | Bundle path or URL. |
| `id` | `string` | Yes | Composition ID. |
| `inputProps` | `object` | No (required from v5.0) | Input props. |
| `logLevel` | `string` | No | Log level. |
| `port` | `number` | No | Preferred port. |
| `chromiumOptions` | `ChromiumOptions` | No | Chromium flags. |
| `timeoutInMilliseconds` | `number` | No | Timeout. Default: `30000`. |
| `browserExecutable` | `string` | No | Browser path. |
| `onBrowserLog` | `function` | No | Console callback. |
| `puppeteerInstance` | `Browser` | No | Reusable browser. |
| `envVariables` | `Record<string, string>` | No | Environment variables. |
| `mediaCacheSizeInBytes` | `number \| null` | No | Media cache. |
| `offthreadVideoCacheSizeInBytes` | `number \| null` | No | OffthreadVideo cache. |
| `offthreadVideoThreads` | `number` | No | OffthreadVideo threads. |
| `binariesDirectory` | `string \| null` | No | Binaries directory. |
| `chromeMode` | `string` | No | Chrome mode. |
| `onBrowserDownload` | `function` | No | Browser download hook. |

Throws if no composition with the specified ID exists.

---

## `openBrowser()`

*Package: `@remotion/renderer`. Available since v3.0.*

Opens a reusable Chrome/Chromium browser instance. Sharing a browser across multiple `renderMedia()`, `renderStill()`, and `getCompositions()` calls avoids repeated startup overhead.

```ts
import { openBrowser } from "@remotion/renderer";

const browser = await openBrowser("chrome", {
  chromiumOptions: { gl: "angle" },
});

// Use browser across multiple renders...
await renderMedia({ puppeteerInstance: browser, ... });
await renderMedia({ puppeteerInstance: browser, ... });

// Clean up
browser.close({ silent: true });
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `browser` | `"chrome"` | Yes (positional) | Currently only `"chrome"` is supported. |
| `logLevel` | `string` | No | Log level. Since v4.0.189. |
| `browserExecutable` | `string \| null` | No | Browser executable path. |
| `chromiumOptions` | `ChromiumOptions` | No | Chromium flags (must be set at launch). |
| `forceDeviceScaleFactor` | `number` | No | Set scale factor at browser level. |
| `onBrowserDownload` | `function` | No | Browser download hook. Since v4.0.137. |
| `chromeMode` | `string` | No | Chrome mode. Since v4.0.248. |

Close with `browser.close({ silent: true })` — the `silent` option suppresses errors if already closed.

---

## `ensureBrowser()`

*Package: `@remotion/renderer`. Available since v4.0.137.*

Ensures a browser is downloaded and available for rendering. Call this during initialization to avoid download delays during the first render.

```ts
import { ensureBrowser } from "@remotion/renderer";

await ensureBrowser();

// With specific version and progress tracking:
await ensureBrowser({
  onBrowserDownload: () => {
    console.log("Downloading browser");
    return {
      version: "144.0.7559.20",  // or null for Remotion's recommended version
      onProgress: ({ percent }) => {
        console.log(`${Math.round(percent * 100)}% downloaded`);
      },
    };
  },
});
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `chromeMode` | `string` | No | `"headless-shell"` or `"chrome-for-testing"`. |
| `browserExecutable` | `string` | No | Path to existing browser executable (skips download). Throws if path does not exist. |
| `logLevel` | `string` | No | Log level. |
| `onBrowserDownload` | `OnBrowserDownload` | No | Specify Chrome version and track download progress. |

---

## Integrating Rendering into a Backend API

Here is a complete Express.js example showing how to integrate Remotion rendering into a backend service:

```ts
import express from "express";
import { bundle } from "@remotion/bundler";
import {
  renderMedia,
  selectComposition,
  openBrowser,
  ensureBrowser,
} from "@remotion/renderer";
import path from "path";

const app = express();
app.use(express.json());

let bundlePath: string;
let browser: Awaited<ReturnType<typeof openBrowser>>;

// Initialize on startup
async function init() {
  await ensureBrowser();

  bundlePath = await bundle({
    entryPoint: require.resolve("./src/index.ts"),
  });

  browser = await openBrowser("chrome");
}

app.post("/render", async (req, res) => {
  const { compositionId, inputProps } = req.body;

  try {
    const composition = await selectComposition({
      serveUrl: bundlePath,
      id: compositionId,
      inputProps,
      puppeteerInstance: browser,
    });

    const { buffer } = await renderMedia({
      composition,
      serveUrl: bundlePath,
      codec: "h264",
      outputLocation: null,  // Return as buffer
      inputProps,
      puppeteerInstance: browser,
    });

    res.set("Content-Type", "video/mp4");
    res.send(buffer);
  } catch (err) {
    res.status(500).json({ error: String(err) });
  }
});

init().then(() => {
  app.listen(3000, () => console.log("Render server on port 3000"));
});
```

Key patterns:
- **Pre-bundle** the project at startup so each render does not re-bundle.
- **Reuse the browser instance** across requests via `openBrowser()` + `puppeteerInstance`.
- **Call `ensureBrowser()`** at startup to ensure Chrome is downloaded.
- **Return buffer in-memory** by setting `outputLocation: null`, avoiding filesystem I/O for API responses.
- For production, add concurrency limits, queue management, and cleanup logic for the browser instance.


---

## 14. Lambda API Reference

### 14.1 Lambda Architecture

Remotion Lambda distributes video rendering across multiple AWS Lambda functions using a chunk-splitting strategy:

1. **Main (orchestrator) function**: Receives the render request, splits the video into frame-range chunks, spawns worker Lambda functions in parallel, waits for all chunks to complete, then concatenates them into the final output. This is the longest-running function.
2. **Worker (render) functions**: Each worker renders a short portion of the video (a chunk of frames) and writes the result to S3. Workers shut down after completing their chunk.
3. **Auxiliary functions**: Short-lived functions handle initialization and progress-fetching tasks. Their cost is negligible.

The final concatenation step (stitching chunks into a single video) runs on the orchestrator function. All intermediate chunks and the final output are stored in an S3 bucket under the `renders/{renderId}/` prefix.

**Concurrency model**: The `framesPerLambda` parameter controls how many frames each worker renders. Lower values spawn more Lambdas (higher parallelism, faster render, higher cost). The maximum number of concurrent Lambda workers is **200**. Alternatively, use the `concurrency` parameter (v4.0.322+) to set the number of workers directly.

### 14.2 Setup Requirements

To use Remotion Lambda, you need:

- **AWS Account** with programmatic access (access key ID + secret access key)
- **IAM User** with an inline policy returned by `getUserPolicy()`. This user's credentials execute CLI commands and Node.js API calls.
- **IAM Role** (`remotion-lambda-role`) with an inline policy returned by `getRolePolicy()`. This role is assumed by the Lambda function itself.
- **S3 Bucket** created via `getOrCreateBucket()`. Only **one bucket per region** is required.
- **Lambda Layer**: Remotion ships a pre-built Lambda layer containing Chromium and fonts. It is deployed automatically by `deployFunction()`.
- **Region selection**: Set via `REMOTION_AWS_REGION` env var or the `region` parameter. Default: `us-east-1`.

**Permissions validation**: Use `simulatePermissions()` or `npx remotion lambda policies validate` to verify IAM setup.

---

### 14.3 `renderMediaOnLambda()`

Kicks off a render process on Remotion Lambda. Returns immediately with a `renderId` for progress tracking via `getRenderProgress()`.

```ts
import { renderMediaOnLambda } from "@remotion/lambda/client";

const { bucketName, renderId } = await renderMediaOnLambda({
  region: "us-east-1",
  functionName: "remotion-render-bds9aab",
  composition: "MyVideo",
  serveUrl:
    "https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw",
  codec: "h264",
});
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `region` | `AwsRegion` | Yes | -- | AWS region where the Lambda function is deployed |
| `functionName` | `string` | Yes | -- | Name of the deployed Lambda function |
| `composition` | `string` | Yes | -- | ID of the composition to render |
| `serveUrl` | `string` | Yes | -- | URL of the deployed Remotion site (from `deploySite()`) |
| `codec` | `string` | Yes | -- | Video codec: `h264`, `h265`, `vp8`, `vp9`, `gif`, `prores`. Audio: `mp3`, `aac`, `wav`. Note: `av1` is not available on Lambda |
| `privacy` | `"public" \| "private" \| "no-acl"` | No | `"public"` | S3 ACL for the output file |
| `framesPerLambda` | `number` | No | auto | Frames per worker Lambda. Lower = more parallelism. Cannot result in >200 functions |
| `concurrency` | `number` | No | -- | Alternative to `framesPerLambda`: set worker count directly (v4.0.322+). Max 200. Cannot be used with `framesPerLambda` |
| `frameRange` | `number \| [number, number] \| [number, null]` | No | all frames | Subset of frames to render |
| `inputProps` | `object` | No | `{}` | JSON props passed to the composition's root component |
| `metadata` | `object` | No | -- | Metadata to attach to the render (v4.0.216+) |
| `audioCodec` | `string` | No | codec-dependent | Audio encoding: refer to Encoding guide for defaults |
| `imageFormat` | `"jpeg" \| "png"` | No | -- | Intermediate frame image format |
| `crf` | `number` | No | codec default | Constant Rate Factor for encoding quality |
| `jpegQuality` | `number` | No | browser default (~80) | JPEG quality (1-100), only for `imageFormat: "jpeg"` |
| `envVariables` | `Record<string, string>` | No | `{}` | Environment variables passed to the headless browser |
| `pixelFormat` | `string` | No | -- | Pixel format for FFmpeg |
| `proResProfile` | `string` | No | -- | ProRes profile (when codec is `prores`) |
| `x264Preset` | `string` | No | -- | x264 encoding preset |
| `audioBitrate` | `string` | No | -- | Audio bitrate (e.g., `"128k"`) |
| `videoBitrate` | `string` | No | -- | Video bitrate (e.g., `"5000k"`) |
| `bufferSize` | `string` | No | -- | FFmpeg buffer size (v4.0.78+) |
| `maxRate` | `string` | No | -- | FFmpeg max rate (v4.0.78+) |
| `muted` | `boolean` | No | `false` | Disable audio output |
| `scale` | `number` | No | `1` | Output scale factor |
| `forceHeight` | `number` | No | -- | Override composition height |
| `forceWidth` | `number` | No | -- | Override composition width |
| `forceFps` | `number` | No | -- | Override composition FPS (v4.0.424+) |
| `forceDurationInFrames` | `number` | No | -- | Override composition duration (v4.0.424+) |
| `maxRetries` | `number` | No | `1` | Retries per chunk on flaky errors |
| `timeoutInMilliseconds` | `number` | No | `30000` | Timeout for `delayRender()` calls |
| `concurrencyPerLambda` | `number` | No | `1` | Browser tabs per Lambda worker (v3.0.30+) |
| `everyNthFrame` | `number` | No | `1` | Render every Nth frame (GIF only) |
| `numberOfGifLoops` | `number \| null` | No | -- | GIF loop count |
| `outName` | `string \| object` | No | `"out.{ext}"` | Output filename or custom destination object |
| `downloadBehavior` | `object` | No | `{type: "play-in-browser"}` | Content-Disposition behavior for S3 URL |
| `overwrite` | `boolean` | No | `false` | Overwrite existing file at `outName` key (v3.2.25+) |
| `chromiumOptions` | `object` | No | `{}` | Chromium flags: `disableWebSecurity`, `ignoreCertificateErrors`, `gl`, `userAgent`, `darkMode` |
| `webhook` | `object` | No | -- | POST notification on render completion: `{url, secret, customData?}` |
| `rendererFunctionName` | `string` | No | -- | Use a different function for chunk rendering (v3.3.38+) |
| `forceBucketName` | `string` | No | auto | Force a specific S3 bucket |
| `logLevel` | `"trace" \| "verbose" \| "info" \| "warn" \| "error"` | No | `"info"` | Log verbosity. `verbose` preserves artifacts for debugging |
| `colorSpace` | `string` | No | -- | Color space for output (v4.0.28+) |
| `deleteAfter` | `string` | No | -- | Auto-delete render after time period (v4.0.32+) |
| `preferLossless` | `boolean` | No | -- | Prefer lossless audio (v4.0.123+) |
| `forcePathStyle` | `boolean` | No | -- | S3 client path style (v4.0.202+) |
| `storageClass` | `string` | No | `"STANDARD"` | S3 storage class identifier (v4.0.305+) |
| `licenseKey` | `string` | No | -- | Remotion license key for usage tracking (v4.0.409+) |
| `isProduction` | `boolean` | No | `true` | Whether this is a production render (v4.0.409+) |
| `mediaCacheSizeInBytes` | `number` | No | -- | Media cache size (v4.0.352+) |
| `offthreadVideoCacheSizeInBytes` | `number` | No | -- | OffthreadVideo cache size (v4.0.23+) |
| `offthreadVideoThreads` | `number` | No | -- | OffthreadVideo thread count (v4.0.261+) |

### Return Value

| Property | Type | Description |
|----------|------|-------------|
| `renderId` | `string` | Unique alphanumeric render identifier |
| `bucketName` | `string` | S3 bucket where files are saved |
| `cloudWatchLogs` | `string` | Link to CloudWatch logs (v3.2.10+) |
| `lambdaInsightsUrl` | `string` | Link to Lambda Insights dashboard (v4.0.61+) |
| `folderInS3Console` | `string` | Link to S3 folder in AWS console (v3.2.43+) |

---

### 14.4 `renderStillOnLambda()`

Renders a single frame as a still image. Returns the result immediately (no polling needed).

```ts
import { renderStillOnLambda } from "@remotion/lambda/client";

const { estimatedPrice, url, sizeInBytes } = await renderStillOnLambda({
  region: "us-east-1",
  functionName: "remotion-render-bds9aab",
  serveUrl: "https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw",
  composition: "MyVideo",
  inputProps: {},
  imageFormat: "png",
  maxRetries: 1,
  privacy: "public",
  envVariables: {},
  frame: 10,
});
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `region` | `AwsRegion` | Yes | -- | AWS region |
| `functionName` | `string` | Yes | -- | Deployed Lambda function name |
| `serveUrl` | `string` | Yes | -- | Deployed site URL |
| `composition` | `string` | Yes | -- | Composition ID |
| `inputProps` | `object` | No | `{}` | Props for the composition |
| `privacy` | `"public" \| "private" \| "no-acl"` | No | `"public"` | S3 ACL |
| `frame` | `number` | No | `0` | Which frame to render (zero-indexed, negative allowed from v3.2.27) |
| `imageFormat` | `"png" \| "jpeg"` | No | `"png"` | Output image format |
| `jpegQuality` | `number` | No | ~80 | JPEG quality (1-100) |
| `maxRetries` | `number` | No | `1` | Retry count for flaky errors |
| `envVariables` | `Record<string, string>` | No | `{}` | Env vars for the browser |
| `scale` | `number` | No | `1` | Scale factor |
| `forceHeight` | `number` | No | -- | Override height |
| `forceWidth` | `number` | No | -- | Override width |
| `forceFps` | `number` | No | -- | Override FPS (v4.0.424+) |
| `forceDurationInFrames` | `number` | No | -- | Override duration (v4.0.424+) |
| `outName` | `string \| object` | No | `"out.{ext}"` | Output filename or custom destination |
| `timeoutInMilliseconds` | `number` | No | `30000` | delayRender timeout |
| `downloadBehavior` | `object` | No | `{type: "play-in-browser"}` | Content-Disposition |
| `chromiumOptions` | `object` | No | `{}` | Chromium flags |
| `forceBucketName` | `string` | No | auto | Force specific bucket |
| `logLevel` | `string` | No | `"info"` | Log verbosity |
| `metadata` | `object` | No | -- | Render metadata (v4.0.216+) |
| `deleteAfter` | `string` | No | -- | Auto-delete timer (v4.0.32+) |
| `forcePathStyle` | `boolean` | No | -- | S3 path style (v4.0.202+) |
| `storageClass` | `string` | No | `"STANDARD"` | S3 storage class (v4.0.305+) |
| `licenseKey` | `string` | No | -- | License key (v4.0.409+) |
| `isProduction` | `boolean` | No | `true` | Production flag (v4.0.409+) |
| `onInit` | `function` | No | -- | Callback when render starts; receives `{renderId, cloudWatchLogs, lambdaInsightsUrl}` (v4.0.6+) |
| `mediaCacheSizeInBytes` | `number` | No | -- | Media cache (v4.0.352+) |
| `offthreadVideoCacheSizeInBytes` | `number` | No | -- | OffthreadVideo cache (v4.0.23+) |
| `offthreadVideoThreads` | `number` | No | -- | OffthreadVideo threads (v4.0.261+) |

### Return Value

| Property | Type | Description |
|----------|------|-------------|
| `bucketName` | `string` | S3 bucket name |
| `url` | `string` | Public URL of the rendered still |
| `outKey` | `string` | S3 key of the output (v4.0.141+) |
| `estimatedPrice` | `object` | Estimated cost information |
| `sizeInBytes` | `number` | Output file size |
| `renderId` | `string` | Unique render identifier |
| `cloudWatchLogs` | `string` | CloudWatch logs link (v3.2.10+) |
| `artifacts` | `array` | Artifacts created during render (v4.0.176+) |

---

### 14.5 `getRenderProgress()`

Polls the status of a render initiated via `renderMediaOnLambda()`. Each call triggers a Lambda invocation (or an S3 call with `skipLambdaInvocation`).

**Do NOT use for stills** -- `renderStillOnLambda()` returns results immediately.

```ts
import { getRenderProgress } from "@remotion/lambda/client";

const progress = await getRenderProgress({
  renderId: "d7nlc2y",
  bucketName: "remotionlambda-d9mafgx",
  functionName: "remotion-render-la8ffw",
  region: "us-east-1",
});

if (progress.done) {
  console.log("Output:", progress.outputFile);
  console.log("Time:", progress.timeToFinish, "ms");
} else if (progress.fatalErrorEncountered) {
  console.error("Errors:", progress.errors);
} else {
  console.log("Progress:", Math.round(progress.overallProgress * 100) + "%");
}
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `renderId` | `string` | Yes | -- | Render ID from `renderMediaOnLambda()` |
| `bucketName` | `string` | Yes | -- | S3 bucket from `renderMediaOnLambda()` |
| `functionName` | `string` | Yes | -- | Name of the function that triggered the render |
| `region` | `AwsRegion` | Yes | -- | AWS region |
| `customCredentials` | `object` | No | -- | Credentials for alternate cloud storage |
| `forcePathStyle` | `boolean` | No | -- | S3 path style (v4.0.202+) |
| `skipLambdaInvocation` | `boolean` | No | `false` | Read from S3 directly instead of invoking Lambda (cheaper/faster, v4.0.218+) |

### Response Shape

| Property | Type | Description |
|----------|------|-------------|
| `overallProgress` | `number` | 0-1 progress estimate |
| `chunks` | `number` | Chunks fully rendered |
| `done` | `boolean` | `true` when render is complete |
| `encodingStatus` | `{framesEncoded: number} \| null` | Encoding progress |
| `renderId` | `string` | Mirrors input |
| `renderMetadata` | `object` | `{frameRange, startedDate, totalChunks, estimatedTotalLambdaInvokations, estimatedRenderLambdaInvokations, compositionId, codec, dimensions}` |
| `bucket` | `string` | S3 bucket name |
| `outputFile` | `string \| null` | URL of final output (null until done) |
| `outKey` | `string \| null` | S3 key of final output |
| `timeToFinish` | `number \| null` | Total render time in ms |
| `errors` | `array` | Array of error objects |
| `fatalErrorEncountered` | `boolean` | `true` if render cannot complete |
| `currentTime` | `number` | Timestamp of response |
| `renderSize` | `number` | Bytes saved to S3 so far |
| `outputSizeInBytes` | `number` | Final output size (v3.3.9+) |
| `lambdasInvoked` | `number` | Workers invoked and started |
| `framesRendered` | `number` | Frames rendered (approx, divisible by 5) (v3.3.8+) |
| `costs` | `object` | `{accruedSoFar, currency, displayCost, disclaimer}` |
| `estimatedBillingDurationInMilliseconds` | `number` | Total Lambda runtime estimate (v4.0.74+) |
| `mostExpensiveFrameRanges` | `array \| null` | Top 5 slowest chunks: `{chunk, timeInMilliseconds, frameRange}` |
| `artifacts` | `array` | Artifacts created during render (v4.0.176+) |

---

### 14.6 Infrastructure Management APIs

### `deploySite()`

Bundles a Remotion project and uploads it to S3. Incremental: only uploads changed files.

```ts
import { deploySite } from "@remotion/lambda";
import path from "path";

const { serveUrl } = await deploySite({
  entryPoint: path.resolve(process.cwd(), "src/index.ts"),
  bucketName: "remotionlambda-c7fsl3d",
  region: "us-east-1",
  options: {
    onBundleProgress: (progress) => console.log(`Bundle: ${progress}%`),
    onUploadProgress: ({ filesUploaded, totalFiles }) =>
      console.log(`Upload: ${filesUploaded}/${totalFiles}`),
  },
});
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `entryPoint` | `string` | Yes | -- | Absolute path to project entry point |
| `bucketName` | `string` | Yes | -- | Target S3 bucket (from `getOrCreateBucket()`) |
| `region` | `AwsRegion` | Yes | -- | AWS region |
| `siteName` | `string` | No | random | Subfolder name in `sites/`. Reuse to overwrite |
| `logLevel` | `string` | No | `"info"` | Log verbosity (v4.0.140+) |
| `options.onBundleProgress` | `(progress: number) => void` | No | -- | Bundle progress callback (0-100) |
| `options.onUploadProgress` | `(info) => void` | No | -- | Upload progress: `{totalFiles, filesUploaded, totalSize, sizeUploaded}` |
| `options.webpackOverride` | `function` | No | -- | Custom Webpack config override |
| `options.enableCaching` | `boolean` | No | `true` | Webpack caching |
| `options.publicDir` | `string` | No | `"public"` | Public directory location |
| `options.rootDir` | `string` | No | cwd | Project root directory |
| `privacy` | `"public" \| "no-acl"` | No | `"public"` | S3 ACL for the site |
| `throwIfSiteExists` | `boolean` | No | `false` | Error if site already exists (v4.0.141+) |
| `forcePathStyle` | `boolean` | No | -- | S3 path style (v4.0.202+) |

**Returns**: `{ serveUrl: string, siteName: string, stats: { uploadedFiles, deletedFiles, untouchedFiles } }`

### `deployFunction()`

Creates a Lambda function in your AWS account. Idempotent: returns existing function if config matches.

```ts
import { deployFunction } from "@remotion/lambda";

const { functionName } = await deployFunction({
  region: "us-east-1",
  timeoutInSeconds: 120,
  memorySizeInMb: 2048,
  createCloudWatchLogGroup: true,
  diskSizeInMb: 2048,
});
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `region` | `AwsRegion` | Yes | -- | AWS region (must match Lambda Layer) |
| `timeoutInSeconds` | `number` | Yes | -- | Max execution time. Must be <900s. Recommended: 120s |
| `memorySizeInMb` | `number` | Yes | -- | RAM allocation. Range: 512-10240 MB. Recommended: 2048 |
| `createCloudWatchLogGroup` | `boolean` | No | -- | Enable CloudWatch logging (recommended) |
| `cloudWatchLogRetentionPeriodInDays` | `number` | No | `14` | Log retention period |
| `diskSizeInMb` | `number` | No | 2048 (<5.0) / 10240 (>=5.0) | Disk storage: 512-10240 MB |
| `customRoleArn` | `string` | No | `remotion-lambda-role` | Custom IAM role ARN |
| `enableLambdaInsights` | `boolean` | No | `false` | Enable CloudWatch Lambda Insights (v4.0.61+) |
| `runtimePreference` | `"default" \| "apple-emojis" \| "cjk"` | No | `"default"` | Font/emoji preference (v4.0.205+) |

**Returns**: `{ functionName: string, alreadyExisted: boolean }`

### `getOrCreateBucket()`

Ensures a Remotion S3 bucket exists. Only **1 bucket per region** is needed.

```ts
import { getOrCreateBucket } from "@remotion/lambda";

const { bucketName } = await getOrCreateBucket({ region: "us-east-1" });
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `region` | `AwsRegion` | Yes | -- | AWS region |
| `enableFolderExpiry` | `boolean \| null` | No | `null` | Enable S3 lifecycle policies for auto-delete (v4.0.32+) |
| `forcePathStyle` | `boolean` | No | -- | S3 path style (v4.0.202+) |

**Returns**: `{ bucketName: string, alreadyExisted: boolean }`

### `getFunctions()`

Lists deployed Remotion Lambda functions in a region.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `region` | `AwsRegion` | Yes | AWS region to query |
| `compatibleOnly` | `boolean` | Yes | Only return functions matching current `@remotion/lambda` version |
| `logLevel` | `string` | No | Log verbosity (v4.0.115+) |

**Returns**: `Array<{ functionName, memorySizeInMb, diskSizeInMb, version, timeoutInSeconds }>`

### `presignUrl()`

Creates a temporary public URL for a private S3 object.

```ts
import { presignUrl } from "@remotion/lambda/client";

const url = await presignUrl({
  region: "us-east-1",
  bucketName: "remotionlambda-c7fsl3d",
  objectKey: "renders/abc123/out.mp4",
  expiresInSeconds: 900,
  checkIfObjectExists: true,
});
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `region` | `AwsRegion` | Yes | -- | AWS region |
| `bucketName` | `string` | Yes | -- | S3 bucket |
| `objectKey` | `string` | Yes | -- | S3 object key |
| `expiresInSeconds` | `number` | Yes | -- | URL lifetime: 1 to 604800 (7 days) |
| `checkIfObjectExists` | `boolean` | No | `false` | If `true`, returns `null` when object missing; if `false`, throws |

**Returns**: `string | null`

### Other Management APIs

| Function | Description |
|----------|-------------|
| `deleteFunction({ region, functionName })` | Delete a deployed Lambda function |
| `getFunctionInfo({ region, functionName })` | Get memory, disk, timeout, version info |
| `deleteSite({ region, bucketName, siteName })` | Remove a site from S3 |
| `getSites({ region })` | List all deployed sites with metadata |
| `deleteRender({ region, bucketName, renderId })` | Delete render artifacts from S3 |
| `downloadMedia({ region, bucketName, renderId, outPath })` | Download rendered output to local disk |
| `getRegions()` | List all supported AWS regions |
| `getCompositionsOnLambda({ region, functionName, serveUrl, inputProps })` | List compositions inside a Lambda-hosted project |
| `getAwsClient({ region, service })` | Direct AWS SDK access (`s3`, `lambda`, `iam`, `cloudwatch`, `servicequotas`, `sts`) |
| `simulatePermissions({ region })` | Validate IAM user permissions |
| `speculateFunctionName({ memorySizeInMb, diskSizeInMb, timeoutInSeconds })` | Predict function name without API call |
| `getUserPolicy()` | Get required IAM user policy JSON |
| `getRolePolicy()` | Get required IAM role policy JSON |
| `estimatePrice({ region, durationInMilliseconds, memorySizeInMb, diskSizeInMb, lambdasInvoked })` | Estimate Lambda compute cost in USD |

---

### 14.7 Configuration Limits

| Setting | Min | Max | Default | Notes |
|---------|-----|-----|---------|-------|
| Memory | 512 MB | 10,240 MB | 2,048 MB | Cost scales linearly with memory |
| Timeout | -- | 900s | 120s recommended | Prefer higher concurrency over longer timeout |
| Disk | 512 MB | 10,240 MB | 2,048 MB (<v5) / 10,240 MB (>=v5) | Increase for longer videos |
| `framesPerLambda` | 4 | -- | auto (video-length dependent) | Cannot exceed 200 total functions |
| `concurrencyPerLambda` | 1 | -- | 1 | Browser tabs per worker |

---

### 14.8 Webhook Support

Remotion Lambda can send POST requests on render completion, error, or timeout.

```ts
const webhook = {
  url: "https://myapp.com/api/webhook",
  secret: process.env.WEBHOOK_SECRET,
  customData: { id: 42 }, // up to 1024 bytes
};
```

**Webhook helpers**:
- `validateWebhookSignature({ secret, body, signatureHeader })` -- throws if the `X-Remotion-Signature` header is invalid
- `appRouterWebhook({ secret, testing, onSuccess, onError, onTimeout })` -- Next.js App Router handler
- `pagesRouterWebhook({ secret, testing, onSuccess, onError, onTimeout })` -- Next.js Pages Router handler
- `expressWebhook({ secret, testing, onSuccess, onError, onTimeout })` -- Express.js handler

---

### 14.9 Cost Model

Remotion Lambda costs are composed of:

1. **AWS Lambda compute**: Billed per GB-second. Use `estimatePrice()` to estimate. Cost = f(region, memory, total duration of all invocations).
2. **S3 storage**: Not included in `estimatePrice()`. Standard S3 rates apply.
3. **Remotion licensing**: Separate from AWS costs. See Section 15.
4. **Data transfer**: Standard AWS egress fees for downloaded output.

The `costs` object in `getRenderProgress()` response provides real-time cost estimates:
- `accruedSoFar`: Float cost in USD
- `displayCost`: Formatted string
- `disclaimer`: No guarantees on accuracy

> **Gap:** The source docs note `estimatePrice()` does not include S3 costs or Remotion licensing fees. There is no documented formula for predicting total end-to-end cost inclusive of all components.

---

### 14.10 Region Support

Remotion Lambda supports multiple AWS regions. Use `getRegions()` to list them. The `enabledByDefaultOnly` option filters to regions enabled by default in new AWS accounts. Default region: `us-east-1`. Set via `REMOTION_AWS_REGION` environment variable or the `region` parameter on each API call.

> **Gap:** The source docs do not enumerate the full list of supported regions. The actual list is determined by the installed version of `@remotion/lambda`.

---

### Cloud Run: `@remotion/cloudrun`

#### Status and Architecture

**Status**: Cloud Run support is in **Alpha** and is **not actively being developed**.

`@remotion/cloudrun` renders video on Google Cloud Platform using Cloud Run services. Unlike Lambda's chunk-splitting architecture:

- **Cloud Run** runs a single long-running container that handles the entire render in one process (using `concurrency` browser tabs within a single instance).
- **Lambda** distributes work across many short-lived function invocations.

GCP Cloud Run uses pre-built Docker images from Remotion's public Artifact Registry. Services are deployed with configurable memory, CPU, and timeout limits.

#### GCP Setup Requirements

- **GCP Project** with Cloud Run, Cloud Storage, and Artifact Registry APIs enabled
- **Service Account** with appropriate permissions (validate with `testPermissions()`)
- **Cloud Storage Bucket** created via `getOrCreateBucket({ region })` -- one per region
- **Deployed Service** via `deployService()` -- idempotent (reuses matching configs)
- **Deployed Site** via `deploySite()` -- bundles project to Cloud Storage

#### `deployService()`

```ts
import { deployService } from "@remotion/cloudrun";

const { shortName, uri } = await deployService({
  memoryLimit: "2Gi",
  cpuLimit: "2.0",
  timeoutSeconds: 500,
  projectID: "my-remotion-project",
  region: "us-east1",
});
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `memoryLimit` | `string` | Yes | -- | RAM limit (e.g., `"2Gi"`). Range: 512MiB - 32GiB |
| `cpuLimit` | `string` | Yes | -- | CPU cores (e.g., `"2.0"`). Must satisfy GCP memory-CPU ratio requirements |
| `timeoutSeconds` | `number` | Yes | -- | Max run time. Must be <3600s |
| `projectID` | `string` | Yes | -- | GCP project ID |
| `region` | `string` | Yes | -- | GCP region |
| `minInstances` | `number` | No | `0` | Minimum warm instances (warning: billed even when idle) |
| `maxInstances` | `number` | No | `100` | Maximum instances |
| `performImageVersionValidation` | `boolean` | No | `true` | Validate Artifact Registry image exists |
| `onlyAllocateCpuDuringRequestProcessing` | `boolean` | No | -- | Disable CPU allocation when idle (v4.0.221+) |

**Returns**: `{ fullName, shortName, uri, alreadyExists }`

#### `renderMediaOnCloudrun()`

```ts
import { renderMediaOnCloudrun } from "@remotion/cloudrun/client";

const result = await renderMediaOnCloudrun({
  region: "us-east1",
  serviceName: "remotion-render-bds9aab",
  composition: "MyVideo",
  serveUrl: "https://storage.googleapis.com/remotioncloudrun-.../sites/abcdefgh",
  codec: "h264",
});

if (result.type === "success") {
  console.log(result.publicUrl);
}
```

Key differences from Lambda:
- Uses `serviceName` or `cloudRunUrl` instead of `functionName`
- Supports `concurrency` as a string (e.g., `"50%"`) for browser tab parallelism within a single container
- Supports `renderStatusWebhook` with progress intervals
- Returns `type: "success" | "crash"` discriminated union
- Supports `renderIdOverride` for custom render IDs
- No chunk-splitting; render runs in a single container

**Success return**: `{ type, renderId, bucketName, publicUrl, privacy, cloudStorageUri, size }`
**Crash return**: `{ type, cloudRunEndpoint, message, requestStartTime, requestCrashTime, requestElapsedTimeInSeconds }`

#### When to Use Each Platform

| Criterion | Lambda | Cloud Run | Local (`renderMedia`) |
|-----------|--------|-----------|----------------------|
| **Speed** | Fastest (parallel chunks) | Medium (single container) | Depends on hardware |
| **Max duration** | 15 min timeout, but chunks run in parallel | 60 min timeout | Unlimited |
| **Scalability** | Up to 200 concurrent workers per render | Single instance per render (GCP auto-scales instances for multiple renders) | Single machine |
| **Setup** | AWS account + IAM | GCP project + service account | None (local) |
| **Maturity** | Production-ready | Alpha, not actively developed | Production-ready |
| **Cost model** | Per-GB-second, scales with parallelism | Per-vCPU-second + memory | Machine cost only |
| **AV1 support** | No (function size limit) | Depends on container | Yes |

---

## 15. Pricing & Licensing

### 15.1 Licensing Model

Remotion uses a dual licensing model managed through the `@remotion/licensing` package (v4.0.237+):

### Free License
Available if you meet the eligibility criteria (typically individual developers, small companies, or open-source projects). You can still use `@remotion/licensing` to track renders without cost.

### Company License ("Remotion for Automators")
Required for companies exceeding the free license threshold. Managed at [remotion.pro](https://remotion.pro).

- **Seat-based** ("Remotion for Creators"): For low-volume, internal use. Telemetry reporting optional.
- **Render-based** ("Remotion for Automators"): For serving personalized videos to end users. Telemetry reporting **mandatory from Remotion 5.0**.

### License Key Integration

Pass `licenseKey` to render functions to enable usage tracking:

```ts
await renderMediaOnLambda({
  // ... other params
  licenseKey: "rm_pub_xxxxx",
  isProduction: true, // default
});
```

Supported packages: `@remotion/lambda`, `@remotion/renderer`, `@remotion/vercel`, `@remotion/web-renderer`.

> **Gap:** `@remotion/cloudrun` does not have built-in telemetry. Use `@remotion/licensing` directly via `registerUsageEvent()`.

### 15.2 Usage Tracking APIs

### `registerUsageEvent()`

```ts
import { registerUsageEvent } from "@remotion/licensing";

const result = await registerUsageEvent({
  licenseKey: "rm_pub_xxxxx",
  event: "cloud-render", // or "web-render"
  host: "https://myapp.com",
  succeeded: true,
});
// result: { billable: boolean, classification: "billable" | "development" | "failed" }
```

- `localhost` renders are classified as `"development"` (non-billable)
- Failed renders (`succeeded: false`) are non-billable
- Events: `"web-render"`, `"cloud-render"`

### `getUsage()`

Query usage from the backend (requires secret key `rm_sec_xxxxx`):

```ts
import { getUsage } from "@remotion/licensing";

const usage = await getUsage({
  licenseKey: "rm_sec_xxxxx",
  since: Date.now() - 30 * 24 * 60 * 60 * 1000, // 30 days
});
// { webRenders: { billable, development, failed }, cloudRenders: { billable, development, failed } }
```

- `since` defaults to beginning of current month (UTC)
- Minimum lookback: 90 days

### 15.3 Infrastructure Costs

**Lambda**: AWS charges per GB-second of compute. Use `estimatePrice()` to estimate Lambda-only costs. S3 storage and data transfer are additional.

**Cloud Run**: GCP charges per vCPU-second and GB-second of memory while processing requests. With `onlyAllocateCpuDuringRequestProcessing: true`, CPU costs stop when idle.

> **Gap:** Remotion does not charge per-render fees through infrastructure. The Company License is a separate subscription managed on remotion.pro. The source docs state that automatic usage-based billing is planned but not yet implemented -- currently, license holders manually adjust seat counts.

---

## 16. Integration Architecture for a Multi-Tenant API

This section synthesizes patterns from the Lambda, Cloud Run, and webhook documentation to describe how to build a multi-tenant video rendering API.

### 16.1 Template Management Patterns

- **One Remotion project per template set**: Bundle all compositions (templates) into a single project. Each composition ID represents a template.
- **Deploy once, render many**: Use `deploySite()` with a fixed `siteName` to maintain a stable serve URL. Redeploy when templates change.
- **Dynamic content via `inputProps`**: Templates accept structured JSON props. Each tenant or render request provides different props to the same composition.
- **Per-tenant branding**: Pass tenant-specific assets (logos, colors, fonts) through `inputProps`. Use `delayRender()` to load remote assets at render time.

```ts
// Deploy templates once
const { serveUrl } = await deploySite({
  entryPoint: "src/index.ts",
  bucketName,
  region: "us-east-1",
  siteName: "video-templates-v2",
});

// Render per-tenant content
const { renderId } = await renderMediaOnLambda({
  serveUrl,
  composition: "ProductShowcase",
  inputProps: {
    tenantId: "acme-corp",
    logoUrl: "https://cdn.acme.com/logo.png",
    products: [{ name: "Widget", price: 9.99 }],
    brandColor: "#FF5500",
  },
  // ...
});
```

### 16.2 Render Lifecycle

The full lifecycle of a render request in a multi-tenant system:

1. **Request**: API receives render request with template ID + structured content payload
2. **Validation**: Validate input props, check tenant authorization, estimate cost
3. **Queue** (application-level): Enqueue the render job to manage concurrency and rate limiting
4. **Trigger**: Call `renderMediaOnLambda()` (or Cloud Run equivalent) with validated props
5. **Progress**: Poll `getRenderProgress()` or use `webhook` for push notifications
6. **Completion**: Render finishes; output lands in S3 at `renders/{renderId}/out.mp4`
7. **Storage**: Generate `presignUrl()` for private access, or use public URLs
8. **Delivery**: Return URL to caller, or push via webhook to downstream systems

### 16.3 Output Storage & Delivery

| Strategy | Implementation | Use Case |
|----------|---------------|----------|
| **Public S3 URL** | `privacy: "public"` | Static content, no auth needed |
| **Presigned URL** | `privacy: "private"` + `presignUrl()` | Time-limited access (max 7 days) |
| **CDN** | CloudFront in front of S3 bucket | High-traffic delivery, caching |
| **Custom destination** | `outName` object with custom endpoint/credentials | Multi-cloud, custom storage |
| **Direct download** | `downloadBehavior: { type: "download" }` | Force browser download |
| **Auto-delete** | `deleteAfter` parameter | Ephemeral content, cost management |
| **Storage class** | `storageClass: "GLACIER"` etc. | Long-term archival |

### 16.4 Concurrency & Scaling

**Per-render concurrency** (Lambda):
- Up to 200 workers per render via `framesPerLambda` or `concurrency`
- Each worker can have multiple browser tabs via `concurrencyPerLambda`

**Multi-render concurrency**:
- Lambda: Limited by AWS account concurrent execution quota (default 1000). Each render uses `N` workers, so `1000 / N` simultaneous renders.
- Cloud Run: Limited by `maxInstances` setting and GCP quotas.

**Scaling patterns**:
- Use multiple AWS regions to multiply concurrency limits
- Use `rendererFunctionName` to dedicate different Lambda configurations to different workloads
- Monitor `estimatedBillingDurationInMilliseconds` in progress to track cost accumulation
- Use `estimatePrice()` for pre-render cost estimation

### 16.5 Cost Estimation

```ts
import { estimatePrice } from "@remotion/lambda";

const costUsd = estimatePrice({
  region: "us-east-1",
  durationInMilliseconds: 20000, // total Lambda execution time
  memorySizeInMb: 2048,
  diskSizeInMb: 2048,
  lambdasInvoked: 1,
}); // e.g., 0.00067
```

For multi-tenant budgeting:
- Track `costs.accruedSoFar` from `getRenderProgress()` per tenant
- Use `getUsage()` from `@remotion/licensing` to track render counts
- Factor in S3 storage costs separately (not estimated by Remotion)

### 16.6 Error Handling & Failure Modes

| Failure Mode | Detection | Recovery |
|-------------|-----------|----------|
| **Chunk render failure** | `errors` array in `getRenderProgress()` | Automatic retry via `maxRetries` (only for flaky errors) |
| **Fatal error** | `fatalErrorEncountered: true` | Stop polling, inspect `errors` array |
| **Lambda timeout** | Webhook `onTimeout` callback | Increase `timeoutInSeconds` or reduce video length |
| **delayRender timeout** | Error in render | Increase `timeoutInMilliseconds` or debug asset loading |
| **Permissions error** | API exception | Run `simulatePermissions()` to diagnose |
| **Version mismatch** | Empty function list / render failure | Redeploy function + site with matching versions |
| **Cloud Run crash** | `result.type === "crash"` | Check GCP logs, increase memory/timeout |
| **S3 overwrite conflict** | Error when `overwrite: false` | Use unique `outName` per render |

**Webhook error handling** (recommended for production):
```ts
await renderMediaOnLambda({
  // ...
  webhook: {
    url: "https://api.myapp.com/render-complete",
    secret: process.env.WEBHOOK_SECRET,
    customData: { tenantId: "acme", jobId: "j-123" },
  },
});
```

Validate incoming webhooks:
```ts
validateWebhookSignature({
  secret: process.env.WEBHOOK_SECRET,
  body: req.body,
  signatureHeader: req.headers["x-remotion-signature"],
});
```

### 16.7 Multi-Tenancy Patterns

### Tenant Isolation
- **Props-level isolation**: All tenants share one deployed site; isolation via `inputProps` containing tenant-specific data
- **Site-level isolation**: Deploy separate sites per tenant using unique `siteName` values
- **Function-level isolation**: Deploy separate Lambda functions per tenant (overkill for most cases)
- **Region-level isolation**: Deploy to different AWS regions for geographic tenants

### Tenant-Specific Branding
- Pass brand assets (logos, fonts, colors) via `inputProps`
- Use `envVariables` for tenant-specific API keys or configuration
- Use `metadata` (v4.0.216+) to tag renders with tenant identifiers

### Output Organization
- Use `outName` with tenant prefix: `renders/{renderId}/tenant-{tenantId}/out.mp4`
- Use `storageClass` to manage archival per tenant SLA
- Use `deleteAfter` for tenants with ephemeral content requirements

> **Gap:** Remotion does not provide built-in multi-tenancy primitives (tenant isolation, per-tenant quotas, access control). These must be implemented at the application layer wrapping the Remotion APIs.


---

## 17. Gotchas, Limitations & Weird Stuff

## Surprising / Counterintuitive Behaviors

### Player Does Not Use `<Composition>`

The `<Player>` and `<Thumbnail>` components do **not** use `<Composition>`. You pass your component directly. This is explicitly noted in the docs but catches developers who assume the Player mirrors the Studio's composition registration system.

### Shared Audio Tags and iOS Safari

The Player pre-mounts 5 silent `<audio>` elements by default (`numberOfSharedAudioTags`). These invisible elements exist specifically to work around iOS Safari's autoplay policy. If you mount more `<Html5Audio>` tags than shared tags available, Remotion throws an error at runtime -- not at build time. Once `numberOfSharedAudioTags` is set, it cannot be changed (an error is thrown if you try).

### Double-Click Fullscreen Adds Single-Click Delay

Enabling `doubleClickToFullscreen` introduces a 200ms delay on single-click pause/play detection while waiting to see if a second click arrives. This is explicitly documented but can feel sluggish.

### Reverse Playback Limitation

Setting `playbackRate` to a negative number (e.g., `-1`) plays the video timeline in reverse, but native `<Audio>`, `<Video>`, `<Html5Audio>`, `<Html5Video>`, and `<OffthreadVideo>` tags **cannot** play in reverse. This is a browser limitation, not a Remotion bug. The visual composition will reverse, but media elements will not produce audio/video output in reverse.

### `initialFrame` Is Immutable After Mount

The `initialFrame` prop on `<Player>` is read once at mount time. Changing it after mount has no effect. This is documented but surprising if you expect it to be reactive.

### Fullscreen Not Supported on iOS Safari

`requestFullscreen()` will throw on iOS Safari because the Fullscreen API is not supported on that platform. The docs note this but it requires explicit handling.

### Version Pinning Is Critical

All `@remotion/*` packages and the `remotion` core package must be pinned to the exact same version. Caret (`^`) ranges in version numbers can cause version conflicts. The docs repeat this warning on every installation page.

### SCSS Requires Specific Dependency Versions

The `@remotion/enable-scss` package requires exact versions: `sass@1.77.2`, `sass-loader@14.2.1`, `css-loader@5.2.7`. The docs explicitly warn that newer versions may not work.

### Tailwind Config Resolution

For `@remotion/tailwind` (v3), TailwindCSS resolves `tailwind.config.js` relative to the current working directory where you run the Remotion CLI -- not relative to the Remotion Root. If you run the CLI from a different directory, Tailwind will not find the config. Use the `configLocation` option (v4.0.187+) to fix this. This issue does not apply to `@remotion/tailwind-v4`.

### `bufferStateDelayInMilliseconds` Split Behavior

The `waiting` and `resume` events fire immediately when the Player enters/exits the buffer state, but `renderPoster()` and `renderPlayPauseButton()` only report `isBuffering: true` after the configured delay (default 300ms). This intentional split allows flexible custom UI but can be confusing.

## Experimental Features

### `@remotion/cloudrun` -- Alpha, Not Actively Developed

The entire `@remotion/cloudrun` package (Google Cloud Run rendering) is marked **EXPERIMENTAL** and "not actively being developed." All APIs in this package carry the experimental label.

### `--experimental-rspack` CLI Flag

Available since v4.0.426 on `npx remotion bundle` and `npx remotion benchmark`. Uses Rspack instead of Webpack as the bundler. Experimental status.

### `@remotion/webcodecs` -- Experimental Package

The `convertMedia()` API and the broader `@remotion/webcodecs` package are explicitly documented as experimental.

## Deprecated Features

### `@remotion/media-parser` (Deprecated Package Name)

The package `@remotion/media-parser` is deprecated. The replacement is referenced in the docs but the deprecated entry still exists.

### `@remotion/webcodecs` (Deprecated Package Name)

Similar to media-parser, the `@remotion/webcodecs` package has a deprecated reference page.

### `convertToCaptions()` from `@remotion/install-whisper-cpp`

Deprecated as of v4.0.216. Use `toCaptions()` from `@remotion/install-whisper-cpp` combined with `createTikTokStyleCaptions()` from `@remotion/captions`.

### `openBrowser()` from `@remotion/renderer`

Deprecated since v4.0.189, scheduled for removal in v5.0. Related to migration to Chrome Headless Shell.

### `getParts()` from `@remotion/paths`

Removed in v4 in favor of `getSubpaths()`.

### `--disable-headless` CLI flag

Deprecated in the `benchmark` command. With the migration to Chrome Headless Shell, this option is no longer functional. Will be removed in v5.0.0.

### Licensing: `webcodec-conversion` Usage Event

Deprecated. Use `web-render` instead when calling `registerUsageEvent()`.

### Licensing: `renders` Field in `getUsage()`

Deprecated in v4.0.409. Use `webRenders` instead.

### `@remotion/cloudrun` Telemetry

No telemetry is implemented for Cloud Run. Use `@remotion/licensing` directly.

### `@remotion/webcodecs` Telemetry

Telemetry was removed in v4.0.399 because the package is no longer monetized.

## Known Limitations

### Matroska Audio Extraction

Matroska-based files (`.mkv`, `.webm`) are supported, but for audio extraction, the entire audio stream up to the extraction point must be processed. This is because Matroska containers store only millisecond-precise timestamps, but more precision is needed to correctly concatenate audio parts.

### Google Fonts Known Issues

The `@remotion/google-fonts` package has documented known issues (referenced in its overview page) related to font loading.

### `@remotion/lambda-go` Lint Requires Go 1.23+

The lint step for `@remotion/lambda-go` requires Go >= 1.23.0. Environments with older Go versions will see lint failures, but this does not affect core functionality.

### `@remotion/openai-whisper` Tests Require API Key

One test in `@remotion/openai-whisper` fails without the `OPENAI_API_KEY` environment variable. This is expected and non-blocking.

## Production-at-Scale Concerns

> **Gap:** The Remotion docs do not provide dedicated guidance on production-at-scale deployment patterns for the Player component. Topics like: memory consumption with many simultaneous Player instances, concurrent rendering limits, CDN strategies for player bundles, SSR hydration behavior, and bundle size optimization are not covered in the source documentation reviewed.

> **Gap:** No documentation found on graceful degradation strategies when the Player encounters unsupported browsers, or on comprehensive browser compatibility matrices for the Player component specifically.

---

## 18. Version & Ecosystem

## Current Version

The current version of Remotion is **v4.0.441** (as declared in `packages/core/src/version.ts`).

## Major Version History

- **v1.x**: Initial release. React-based video creation framework.
- **v2.x**: Introduced shared audio tags, `getContainerNode()` on PlayerRef (v2.4.2), `isPlaying()` (v2.5.7).
- **v3.x**: Major expansion. Added `<Thumbnail>` (v3.2.41), player events (`fullscreenchange` v3.2.0, `frameupdate` v3.2.27), poster system (v3.2.14), custom render props for controls (v3.2.32), `enableTailwind()` for Tailwind v3 (v3.3.95), playback rate control UI (v3.3.98), `initiallyMuted` (v3.3.81).
- **v4.x**: Current major. Introduced buffer state management (v4.0.111), custom volume/mute controls (v4.0.188), `overflowVisible` for drag-and-drop (v4.0.173), media keys behavior (v4.0.221), Tailwind v4 support via `@remotion/tailwind-v4` (v4.0.256), SCSS support via `@remotion/enable-scss` (v4.0.162), `noSuspense` (v4.0.271), license acknowledgment (v4.0.253), experimental Rspack bundler (v4.0.426), `renderCustomControls` slot (v4.0.418), volume persistence (v4.0.305).

> **Gap:** No formal changelog or migration guide from v3 to v4 is present in the source documentation reviewed. The version increments (4.0.1 through 4.0.441) suggest a rapid patch cadence within the v4.0.x line with no minor version bumps.

## Ecosystem Tools

### Remotion Studio

The primary development UI. Run with `cd packages/example && bun run dev` (starts at `http://localhost:3000`). Used for previewing compositions, testing animations, and iterating on video content. The Studio uses `<Composition>` registration (unlike the Player).

### Remotion Preview / Player Testbed

A dedicated testbed for Player development: `cd packages/player-example && bun run dev`.

### Docs Site

Docusaurus-based documentation: `cd packages/docs && bun run start`.

### CLI Commands

- `npx create-video@latest` -- Scaffold a new Remotion project.
- `npx remotion compositions` -- List available compositions.
- `npx remotion render <comp-id> --output out.mp4` -- Render a video.
- `npx remotion still <comp-id> --output out.png` -- Render a still.
- `npx remotion bundle` -- Create a production bundle.
- `npx remotion benchmark` -- Performance benchmarking.

## Templates

Remotion ships 22 official templates as packages in the monorepo:

| Template | Package | Description |
|----------|---------|-------------|
| Audiogram | `template-audiogram` | Audio visualization with waveforms |
| Blank | `template-blank` | Minimal starter |
| Code Hike | `template-code-hike` | Code animation |
| Electron | `template-electron` | Desktop app wrapper |
| Hello World | `template-helloworld` | Basic example |
| JavaScript | `template-javascript` | JS (non-TypeScript) starter |
| Music Visualization | `template-music-visualization` | Audio-reactive visuals |
| Next.js (App Dir) | `template-next-app` | Next.js App Router + Player + Lambda |
| Next.js (App Dir + Tailwind) | `template-next-app-tailwind` | Next.js + Tailwind CSS |
| Next.js (Pages Dir) | `template-next-pages` | Next.js Pages Router |
| Overlay | `template-overlay` | Streaming overlay |
| Prompt to Motion Graphics | `template-prompt-to-motion-graphics` | AI-generated motion graphics |
| Prompt to Video | `template-prompt-to-video` | AI-generated video |
| React Router | `template-react-router` | React Router 7 (Remix) integration |
| Recorder | `template-recorder` | Screen/camera recording |
| Render Server | `template-render-server` | Self-hosted render API |
| Skia | `template-skia` | 2D graphics with Skia |
| Stargazer | `template-stargazer` | GitHub stars visualization |
| Still | `template-still` | Static image generation |
| Three.js | `template-three` | 3D graphics with Three.js |
| TikTok | `template-tiktok` | TikTok-format vertical video |
| Vercel | `template-vercel` | Vercel Sandbox rendering (instead of Lambda) |

## Third-Party Integrations

### `@remotion/lottie`

Render Lottie animations (After Effects exports via Bodymovin) as Remotion components. Enables embedding complex vector animations in video compositions.

### `@remotion/three`

Integration with Three.js for 3D graphics. Enables WebGL-based 3D scenes within Remotion compositions. Has a dedicated `template-three` starter.

### `@remotion/skia`

Integration with React Native Skia for high-performance 2D graphics. Enables Skia-based drawing primitives within compositions. Has a dedicated `template-skia` starter.

### `@remotion/gif`

Render GIF files as components with frame-accurate playback within Remotion compositions.

### `@remotion/rive`

Integration with Rive for interactive animations and state machines within Remotion compositions.

### `@remotion/google-fonts`

Load and use any Google Font in compositions. Provides a typed `loadFont()` API and a `getAvailableFonts()` discovery function. Has documented known issues with certain fonts.

### `@remotion/noise`

Perlin noise and simplex noise utilities for procedural animation effects.

### `@remotion/motion-blur`

Motion blur effects for compositions.

### `@remotion/paths`

SVG path manipulation utilities (`getSubpaths()`, etc.). Note: `getParts()` was removed in v4.

### `@remotion/shapes`

Primitive shape components for compositions.

### `@remotion/transitions`

Transition effects between scenes/compositions.

### `@remotion/captions`

Caption processing utilities including `createTikTokStyleCaptions()`.

### `@remotion/layout-utils`

Layout measurement utilities for text and other elements.

### `@remotion/zod-types`

Zod schemas for Remotion configuration types.

### `@remotion/preload`

Asset preloading utilities for ensuring media is ready before playback.

### `@remotion/media-utils`

Media file utility functions.

## Styling Integrations

### TailwindCSS v3 -- `@remotion/tailwind`

Available since v3.3.95. Provides `enableTailwind()` which modifies the Webpack configuration to support TailwindCSS v3.

```ts
// remotion.config.ts
import {Config} from '@remotion/cli/config';
import {enableTailwind} from '@remotion/tailwind';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind(currentConfiguration);
});
```

**Custom config location** (v4.0.187+): Pass `configLocation` as second argument to resolve `tailwind.config.js` relative to the Remotion Root instead of CWD:

```ts
import path from 'node:path';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind(currentConfiguration, {
    configLocation: path.join(__dirname, 'tailwind.config.js'),
  });
});
```

### TailwindCSS v4 -- `@remotion/tailwind-v4`

Available since v4.0.256. Same API pattern as v3, but imports from `@remotion/tailwind-v4`:

```ts
import {Config} from '@remotion/cli/config';
import {enableTailwind} from '@remotion/tailwind-v4';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind(currentConfiguration);
});
```

No `configLocation` option is documented for v4 (Tailwind v4 uses CSS-based configuration).

### SCSS/SASS -- `@remotion/enable-scss`

Available since v4.0.162. Provides `enableScss()` for Webpack configuration:

```ts
import {Config} from '@remotion/cli/config';
import {enableScss} from '@remotion/enable-scss';

Config.overrideWebpackConfig((currentConfiguration) => {
  return enableScss(currentConfiguration);
});
```

**Required peer dependencies** (exact versions):
- `sass@1.77.2`
- `sass-loader@14.2.1`
- `css-loader@5.2.7`

Newer versions of these dependencies may not work.

### Composing Multiple Webpack Overrides

All three styling packages support reducer-style composition for combining with other Webpack changes:

```ts
Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind({
    ...currentConfiguration,
    // other Webpack changes
  });
});
```

> **Gap:** No documentation found on using multiple styling integrations simultaneously (e.g., Tailwind + SCSS in the same project), or on potential conflicts between them.

