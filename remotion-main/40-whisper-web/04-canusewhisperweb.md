---
title: "canUseWhisperWeb()"
url: "https://www.remotion.dev/docs/whisper-web/can-use-whisper-web"
path: "/docs/whisper-web/can-use-whisper-web"
---

"---\nimage: /generated/articles-docs-whisper-web-can-use-whisper-web.png\ntitle: canUseWhisperWeb()\ncrumb: '@remotion/whisper-web'\n---\n\n:::warning\n**Unstable API**: This package is experimental for the moment. As we test it, we might make a few changes to the API and switch to a WebGPU-based backend in the future.\n:::\n\n# canUseWhisperWeb()\n\nChecks if the current browser environment supports running `@remotion/whisper-web` with a specified model.  \nThis function verifies various browser capabilities like `crossOriginIsolated`, `IndexedDB`, `navigator.storage.estimate()`, and available storage space.\n\n## Enabling cross-origin isolation\n\nThis package requires a page that is [cross-origin isolated](/docs/miscellaneous/cross-origin-isolation).\n\n## Example usage\n\n```tsx twoslash\nimport {canUseWhisperWeb, type WhisperWebModel} from '@remotion/whisper-web';\nimport {useState, useEffect} from 'react';\n\nexport default function MyComponent() {\n  const [supported, setSupported] = useState<boolean | null>(null);\n  const [reason, setReason] = useState<string | undefined>(undefined);\n\n  useEffect(() => {\n    const checkSupport = async () => {\n      const modelToUse: WhisperWebModel = 'tiny.en'; // Or any other model\n      const result = await canUseWhisperWeb(modelToUse);\n      setSupported(result.supported);\n      if (!result.supported) {\n        setReason(result.detailedReason ?? result.reason);\n      }\n    };\n\n    checkSupport();\n  }, []);\n\n  if (supported === null) {\n    return <p>Checking if Whisper Web can be used...</p>;\n  }\n\n  if (supported) {\n    return <p>Can use Whisper Web!</p>;\n  }\n\n  return <p>Using Whisper Web is not possible: {reason}</p>;\n}\n```\n\n## Arguments\n\n### `model`\n\nThe Whisper model intended to be used. This is used to check if there's enough storage space for the model.\nPossible values: `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`.\n\nRefer to the `WhisperWebModel` type exported by the package for a comprehensive list.\n\n## Return value\n\nA `Promise` that resolves to a `CanUseWhisperWebResult` object with the following properties:\n\n### `supported`\n\nA boolean indicating whether a transcription can be done. `true` if supported, `false` otherwise.\n\n### `reason?`\n\nIf `supported` is `false`, this field provides a brief, categorized reason for the lack of support.\n\nPossible values values include:\n\n- `window-undefined`: `window` object is not available.\n- `not-cross-origin-isolated`: The page is not cross-origin isolated.\n- `indexed-db-unavailable`: IndexedDB is not available.\n- `navigator-storage-unavailable`: `navigator.storage.estimate()` API is not available.\n- `quota-undefined`: Storage quota could not be determined.\n- `usage-undefined`: Storage usage could not be determined.\n- `not-enough-space`: Insufficient storage space for the specified model.\n- `error-estimating-storage`: An error occurred while trying to estimate storage.\n\n### `detailedReason?`\n\nIf `supported` is `false`, this field may contain a more detailed, human-readable explanation of why a transcription is not possible.\n\n## Important considerations\n\n- **Cross-Origin Isolation:** For `SharedArrayBuffer` to work, which is required by `@remotion/whisper-web`, the page must be served with specific HTTP headers:\n  - `Cross-Origin-Opener-Policy: same-origin`\n  - `Cross-Origin-Embedder-Policy: require-corp`\n    Ensure your server is configured to send these headers. See [MDN documentation on `crossOriginIsolated`](https://developer.mozilla.org/en-US/docs/Web/API/Window/crossOriginIsolated) for more details.\n\n- **Browser Compatibility:** While this function checks for necessary APIs, always test on your target browsers as support for WebAssembly, IndexedDB, and storage estimation can vary.\n\n## See also\n\n- [Source code for `canUseWhisperWeb()`](https://github.com/remotion-dev/remotion/blob/main/packages/whisper-web/src/can-use-whisper-web.ts)\n- [`@remotion/whisper-web`](/docs/whisper-web)\n- [`transcribe()`](/docs/whisper-web/transcribe)\n- [`downloadWhisperModel()`](/docs/whisper-web/download-whisper-model)\n"

Checks if the current browser environment supports running `@remotion/whisper-web` with a specified model.

This function verifies various browser capabilities like `crossOriginIsolated`, `IndexedDB`, `navigator.storage.estimate()`, and available storage space.

## Enabling cross-origin isolation[​](#enabling-cross-origin-isolation)

This package requires a page that is [cross-origin isolated](/docs/miscellaneous/cross-origin-isolation).

## Example usage[​](#example-usage)

```
import {canUseWhisperWeb, type WhisperWebModel} from '@remotion/whisper-web';
import {useState, useEffect} from 'react';

export default function MyComponent() {
  const [supported, setSupported] = useState<boolean | null>(null);
  const [reason, setReason] = useState<string | undefined>(undefined);

  useEffect(() => {
    const checkSupport = async () => {
      const modelToUse: WhisperWebModel = 'tiny.en'; // Or any other model
      const result = await canUseWhisperWeb(modelToUse);
      setSupported(result.supported);
      if (!result.supported) {
        setReason(result.detailedReason ?? result.reason);
      }
    };

    checkSupport();
  }, []);

  if (supported === null) {
    return <p>Checking if Whisper Web can be used...</p>;
  }

  if (supported) {
    return <p>Can use Whisper Web!</p>;
  }

  return <p>Using Whisper Web is not possible: {reason}</p>;
}Copy
```

## Arguments[​](#arguments)

### `model`[​](#model)

The Whisper model intended to be used. This is used to check if there's enough storage space for the model.
Possible values: `tiny`, `tiny.en`, `base`, `base.en`, `small`, `small.en`.

Refer to the `WhisperWebModel` type exported by the package for a comprehensive list.

## Return value[​](#return-value)

A `Promise` that resolves to a `CanUseWhisperWebResult` object with the following properties:

### `supported`[​](#supported)

A boolean indicating whether a transcription can be done. `true` if supported, `false` otherwise.

### `reason?`[​](#reason)

If `supported` is `false`, this field provides a brief, categorized reason for the lack of support.

Possible values values include:

- `window-undefined`: `window` object is not available.

- `not-cross-origin-isolated`: The page is not cross-origin isolated.

- `indexed-db-unavailable`: IndexedDB is not available.

- `navigator-storage-unavailable`: `navigator.storage.estimate()` API is not available.

- `quota-undefined`: Storage quota could not be determined.

- `usage-undefined`: Storage usage could not be determined.

- `not-enough-space`: Insufficient storage space for the specified model.

- `error-estimating-storage`: An error occurred while trying to estimate storage.

### `detailedReason?`[​](#detailedreason)

If `supported` is `false`, this field may contain a more detailed, human-readable explanation of why a transcription is not possible.

## Important considerations[​](#important-considerations)

- 

**Cross-Origin Isolation:** For `SharedArrayBuffer` to work, which is required by `@remotion/whisper-web`, the page must be served with specific HTTP headers:

- `Cross-Origin-Opener-Policy: same-origin`

- `Cross-Origin-Embedder-Policy: require-corp`
Ensure your server is configured to send these headers. See [MDN documentation on `crossOriginIsolated`](https://developer.mozilla.org/en-US/docs/Web/API/Window/crossOriginIsolated) for more details.

- 

**Browser Compatibility:** While this function checks for necessary APIs, always test on your target browsers as support for WebAssembly, IndexedDB, and storage estimation can vary.

## See also[​](#see-also)

- [Source code for `canUseWhisperWeb()`](https://github.com/remotion-dev/remotion/blob/main/packages/whisper-web/src/can-use-whisper-web.ts)

- [`@remotion/whisper-web`](/docs/whisper-web)

- [`transcribe()`](/docs/whisper-web/transcribe)

- [`downloadWhisperModel()`](/docs/whisper-web/download-whisper-model)
](/docs/whisper-web/download-whisper-model)](/docs/whisper-web/download-whisper-model)
](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)
- ](/docs/whisper-web/download-whisper-model)