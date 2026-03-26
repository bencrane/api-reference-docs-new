---
title: "resampleTo16Khz()"
url: "https://www.remotion.dev/docs/whisper-web/resample-to-16khz"
path: "/docs/whisper-web/resample-to-16khz"
---

"---\nimage: /generated/articles-docs-whisper-web-resample-to-16khz.png\ntitle: resampleTo16Khz()\ncrumb: '@remotion/whisper-web'\n---\n\n:::warning\n**Unstable API**: This package is experimental for the moment. As we test it, we might make a few changes to the API and switch to a WebGPU-based backend in the future.\n:::\n\n# resampleTo16Khz()\n\nProcesses an audio `File` or `Blob` by decoding it, converting it to mono, and resampling it to a 16kHz `Float32Array`. This prepares the audio data for use with the [`transcribe()`](/docs/whisper-web/transcribe) function.\n\nThis function operates in a browser environment as it relies on the Web Audio API (`AudioContext`, `OfflineAudioContext`) and `FileReader`.\n\n## Arguments\n\n### `file`\n\nThe audio `File` or `Blob` object that you want to process. The function will attempt to decode the audio from common formats (e.g., WAV, MP3, Ogg) supported by the browser's Web Audio API.\n\n### `onProgress?`\n\nA callback function that receives progress updates during the resampling process. The `progress` value is a number between 0 and 1, where 0 indicates the start and 1 indicates completion.\n\n### `logLevel?`\n\nDefault: `info`\n\n**Type:** `'trace' | 'verbose' | 'info' | 'warn' | 'error'`\n\nOptional. Determines the level of detail for logs printed to the console during the resampling process. Useful for debugging.\n\n## Return value\n\n`Promise<Float32Array>`\n\nThis array contains the raw audio waveform data for a single channel (mono), sampled at 16kHz. This output is ready to be passed to the `channelWaveform` argument of the [`transcribe()`](/docs/whisper-web/transcribe) function.\n\n## Behavior notes\n\n- **Browser environment:** This function is intended for use in a browser environment due to its reliance on Web Audio APIs (`AudioContext`, `OfflineAudioContext`) and `FileReader`.\n- **Audio decoding:** It uses the browser's built-in audio decoding capabilities. The range of supported audio formats may vary slightly between browsers.\n- **Output format:** The output is always a mono `Float32Array` at 16kHz, regardless of the input file's original channel count or sample rate.\n\n## See also\n\n- [`transcribe()`](/docs/whisper-web/transcribe)\n- [`@remotion/whisper-web`](/docs/whisper-web)\n"

Processes an audio `File` or `Blob` by decoding it, converting it to mono, and resampling it to a 16kHz `Float32Array`. This prepares the audio data for use with the [`transcribe()`](/docs/whisper-web/transcribe) function.

This function operates in a browser environment as it relies on the Web Audio API (`AudioContext`, `OfflineAudioContext`) and `FileReader`.

## Arguments[​](#arguments)

### `file`[​](#file)

The audio `File` or `Blob` object that you want to process. The function will attempt to decode the audio from common formats (e.g., WAV, MP3, Ogg) supported by the browser's Web Audio API.

### `onProgress?`[​](#onprogress)

A callback function that receives progress updates during the resampling process. The `progress` value is a number between 0 and 1, where 0 indicates the start and 1 indicates completion.

### `logLevel?`[​](#loglevel)

Default: `info`

**Type:** `'trace' | 'verbose' | 'info' | 'warn' | 'error'`

Optional. Determines the level of detail for logs printed to the console during the resampling process. Useful for debugging.

## Return value[​](#return-value)

`Promise<Float32Array>`

This array contains the raw audio waveform data for a single channel (mono), sampled at 16kHz. This output is ready to be passed to the `channelWaveform` argument of the [`transcribe()`](/docs/whisper-web/transcribe) function.

## Behavior notes[​](#behavior-notes)

- **Browser environment:** This function is intended for use in a browser environment due to its reliance on Web Audio APIs (`AudioContext`, `OfflineAudioContext`) and `FileReader`.

- **Audio decoding:** It uses the browser's built-in audio decoding capabilities. The range of supported audio formats may vary slightly between browsers.

- **Output format:** The output is always a mono `Float32Array` at 16kHz, regardless of the input file's original channel count or sample rate.

## See also[​](#see-also)

- [`transcribe()`](/docs/whisper-web/transcribe)

- [`@remotion/whisper-web`](/docs/whisper-web)
](/docs/whisper-web)](/docs/whisper-web)
](/docs/whisper-web)
- ](/docs/whisper-web)
- ](/docs/whisper-web)
- ](/docs/whisper-web)
- ](/docs/whisper-web)
- ](/docs/whisper-web)
- ](/docs/whisper-web)