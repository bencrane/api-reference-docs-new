---
title: "@remotion/media-utils"
url: "https://www.remotion.dev/docs/media-utils/"
path: "/docs/media-utils/"
---

"---\nimage: /generated/articles-docs-media-utils-index.png\ntitle: \"@remotion/media-utils\"\n---\n\nimport {TableOfContents} from './table-of-contents';\n\nA package providing utility functions for getting information about video and audio, and for visualizing audio.\n\nExcept for [`useAudioData()`](/docs/use-audio-data), all functions can also be used outside of Remotion.\n\n<Installation pkg=\"@remotion/media-utils\"/>\n\n## Functions\n\n<TableOfContents />\n\n## License\n\nMIT\n"

A package providing utility functions for getting information about video and audio, and for visualizing audio.

Except for [`useAudioData()`](/docs/use-audio-data), all functions can also be used outside of Remotion.

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/media-utilsCopy
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

## Functions[​](#functions)

[
**audioBufferToDataUrl()**
Serialize an audio buffer](/docs/audio-buffer-to-data-url)[
**getAudioData()**
Get metadata of an audio source](/docs/get-audio-data)[
**getAudioDurationInSeconds()**
Get the duration of an audio source](/docs/get-audio-duration-in-seconds)[
**getVideoMetadata()**
Get metadata of a video source](/docs/get-video-metadata)[
**getWaveformPortion()**
Trims audio data into a waveform](/docs/get-waveform-portion)[
**useAudioData()**
`getAudioData()` as a hook](/docs/use-audio-data)[
**useWindowedAudioData()**
Optimized for fetching only current data, works only with `.wav`](/docs/use-windowed-audio-data)[
**visualizeAudio()**
Process a music waveform for visualization](/docs/visualize-audio)[
**visualizeAudioWaveform()**
Process a voice waveform for visualization](/docs/media-utils/visualize-audio-waveform)[
**createSmoothSvgPath()**
Turn waveform points into a smooth SVG path](/docs/media-utils/create-smooth-svg-path)

## License[​](#license)

MIT](#license)](#license)
](#license)
- ](#license)