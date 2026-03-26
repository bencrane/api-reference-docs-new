---
title: "audioBufferToDataUrl()"
url: "https://www.remotion.dev/docs/audio-buffer-to-data-url"
path: "/docs/audio-buffer-to-data-url"
---

"---\nimage: /generated/articles-docs-audiobuffertodataurl.png\nid: audio-buffer-to-data-url\ntitle: audioBufferToDataUrl()\ncrumb: '@remotion/media-utils'\n---\n\n_Part of the `@remotion/media-utils` package of helper functions. Available from v2.5.7._\n\nThis API takes an [`AudioBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer) instance and converts it to a Base 64 Data URL so it can be passed to an [`<Html5Audio />`](/docs/html5-audio) tag.\n\n## API Usage\n\n```tsx twoslash\nconst audioBuffer = new AudioBuffer({length: 0, sampleRate: 44100});\n// ---cut---\nimport {audioBufferToDataUrl} from '@remotion/media-utils';\n\nconst str = audioBufferToDataUrl(audioBuffer);\n```\n\n## Example: Rendering a sine tone\n\nThe following composition will render a sine tone with a C4 pitch.\n\n```tsx twoslash\nimport {audioBufferToDataUrl} from '@remotion/media-utils';\nimport {useCallback, useEffect, useState} from 'react';\nimport {Html5Audio, cancelRender, continueRender, delayRender, interpolate, useVideoConfig} from 'remotion';\n\nconst C4_FREQUENCY = 261.63;\nconst sampleRate = 44100;\n\nexport const OfflineAudioBufferExample: React.FC = () => {\n  const [handle] = useState(() => delayRender());\n  const [audioBuffer, setAudioBuffer] = useState<string | null>(null);\n  const {fps, durationInFrames} = useVideoConfig();\n  const lengthInSeconds = durationInFrames / fps;\n\n  const renderAudio = useCallback(async () => {\n    const offlineContext = new OfflineAudioContext({\n      numberOfChannels: 2,\n      length: sampleRate * lengthInSeconds,\n      sampleRate,\n    });\n    const oscillatorNode = offlineContext.createOscillator();\n    const gainNode = offlineContext.createGain();\n    oscillatorNode.connect(gainNode);\n    gainNode.connect(offlineContext.destination);\n    gainNode.gain.setValueAtTime(0.5, offlineContext.currentTime);\n\n    oscillatorNode.type = 'sine';\n    oscillatorNode.frequency.value = C4_FREQUENCY;\n\n    const {currentTime} = offlineContext;\n    oscillatorNode.start(currentTime);\n    oscillatorNode.stop(currentTime + lengthInSeconds);\n\n    const buffer = await offlineContext.startRendering();\n    setAudioBuffer(audioBufferToDataUrl(buffer));\n\n    continueRender(handle);\n  }, [handle, lengthInSeconds]);\n\n  useEffect(() => {\n    renderAudio().catch((err) => cancelRender(err));\n  }, [renderAudio]);\n\n  return audioBuffer ? (\n    <Html5Audio\n      src={audioBuffer}\n      trimAfter={100}\n      volume={(f) =>\n        interpolate(f, [0, 50, 100], [0, 1, 0], {\n          extrapolateLeft: 'clamp',\n          extrapolateRight: 'clamp',\n        })\n      }\n    />\n  ) : null;\n};\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/audio-buffer/audio-url-helpers.ts)\n- [Rendering audio only](/docs/audio/exporting#audio-only)\n"

*Part of the `@remotion/media-utils` package of helper functions. Available from v2.5.7.*

This API takes an [`AudioBuffer`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBuffer) instance and converts it to a Base 64 Data URL so it can be passed to an [`<Html5Audio />`](/docs/html5-audio) tag.

## API Usage[​](#api-usage)

```
import {audioBufferToDataUrl} from '@remotion/media-utils';

const str = audioBufferToDataUrl(audioBuffer);Copy
```

## Example: Rendering a sine tone[​](#example-rendering-a-sine-tone)

The following composition will render a sine tone with a C4 pitch.

```
import {audioBufferToDataUrl} from '@remotion/media-utils';
import {useCallback, useEffect, useState} from 'react';
import {Html5Audio, cancelRender, continueRender, delayRender, interpolate, useVideoConfig} from 'remotion';

const C4_FREQUENCY = 261.63;
const sampleRate = 44100;

export const OfflineAudioBufferExample: React.FC = () => {
  const [handle] = useState(() => delayRender());
  const [audioBuffer, setAudioBuffer] = useState<string | null>(null);
  const {fps, durationInFrames} = useVideoConfig();
  const lengthInSeconds = durationInFrames / fps;

  const renderAudio = useCallback(async () => {
    const offlineContext = new OfflineAudioContext({
      numberOfChannels: 2,
      length: sampleRate * lengthInSeconds,
      sampleRate,
    });
    const oscillatorNode = offlineContext.createOscillator();
    const gainNode = offlineContext.createGain();
    oscillatorNode.connect(gainNode);
    gainNode.connect(offlineContext.destination);
    gainNode.gain.setValueAtTime(0.5, offlineContext.currentTime);

    oscillatorNode.type = 'sine';
    oscillatorNode.frequency.value = C4_FREQUENCY;

    const {currentTime} = offlineContext;
    oscillatorNode.start(currentTime);
    oscillatorNode.stop(currentTime + lengthInSeconds);

    const buffer = await offlineContext.startRendering();
    setAudioBuffer(audioBufferToDataUrl(buffer));

    continueRender(handle);
  }, [handle, lengthInSeconds]);

  useEffect(() => {
    renderAudio().catch((err) => cancelRender(err));
  }, [renderAudio]);

  return audioBuffer ? (
    <Html5Audio
      src={audioBuffer}
      trimAfter={100}
      volume={(f) =>
        interpolate(f, [0, 50, 100], [0, 1, 0], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        })
      }
    />
  ) : null;
};Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/media-utils/src/audio-buffer/audio-url-helpers.ts)

- [Rendering audio only](/docs/audio/exporting#audio-only)
](/docs/audio/exporting#audio-only)](/docs/audio/exporting#audio-only)
](/docs/audio/exporting#audio-only)
- ](/docs/audio/exporting#audio-only)
- ](/docs/audio/exporting#audio-only)