---
title: "createVideoDecoder()"
url: "https://www.remotion.dev/docs/webcodecs/create-video-decoder"
path: "/docs/webcodecs/create-video-decoder"
---

"---\nimage: /generated/articles-docs-webcodecs-create-video-decoder.png\nsidebar_label: createVideoDecoder()\ntitle: createVideoDecoder()\nslug: /webcodecs/create-video-decoder\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nimport {UnstableDisclaimer} from './UnstableDisclaimer';\n\n:::warning\n\n<UnstableDisclaimer />\n:::\n\n# createVideoDecoder()<AvailableFrom v=\"4.0.307\" />\n\nThis function is a wrapper around the [`VideoDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder) Web API.\n\n```tsx twoslash title=\"Create a video decoder\"\nimport type {MediaParserVideoTrack} from '@remotion/media-parser';\n\nconst track = {} as unknown as MediaParserVideoTrack;\n\n// ---cut---\n\nimport {createVideoDecoder} from '@remotion/webcodecs';\n\nconst decoder = await createVideoDecoder({\n  track,\n  onFrame: console.log,\n  onError: console.error,\n});\n```\n\n## Differences to `VideoDecoder`\n\n- Two new methods are added: [`.waitForQueueToBeLessThan()`](#waitforqueuetobelessthan) and `.waitForFinish()`.\n- The [`dequeue`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder/dequeue_event) event is not supported as it is not reliable across browsers.\n- In addition to [`EncodedVideoChunk`](https://developer.mozilla.org/en-US/docs/Web/API/EncodedVideoChunk), [`EncodedVideoChunkInit`](https://www.w3.org/TR/webcodecs/#dictdef-encodedvideochunkinit) objects are also accepted for `.decode()`.\n- A [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance can be passed in to the function, allowing for decoding to be paused, resumed and aborted.\n- `.decode()` is async, and returns a promise, allowing for a halt if the decoder is paused.\n- A [`logLevel`](#loglevel) can be passed in to the function, allowing the queue to be debugged.\n- The [`onFrame`](#onframe) callback is being awaited. When rejected, the error lands in the [`onError`](#onerror) callback. When resolved, only then the queue size counter will be decreased.\n\n## API\n\nTakes an object with the following properties:\n\n### `track`\n\nAn [`VideoDecoderConfig`](https://www.w3.org/TR/webcodecs/#dictdef-videodecoderconfig) object.  \nYou may pass a [`MediaParserVideoTrack`](/docs/media-parser/types#mediaparservideotrack) object from [`parseMedia()`](/docs/media-parser/parse-media), which also is an `VideoDecoderConfig` object.\n\n### `onFrame`\n\nA callback that is called when a frame is decoded.\n\nTakes a single argument, which is a [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object.\n\nIf the passed callback is asynchronous, the queue size counter will be decreased only after the callback has been resolved.\n\nHowever, the callback for the next frame may already be called while your callback is still running.  \nWe do not ensure that callbacks are running sequentially.\n\n### `onError`\n\nA callback that is called when an error occurs or the decode is aborted through the controller.\n\nTakes a single argument, which is an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object.\n\n### `controller?`\n\nA [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance.\n\nIf provided, you can call [`.pause()`](/docs/webcodecs/webcodecs-controller#pause), [`.resume()`](/docs/webcodecs/webcodecs-controller#resume) and [`.abort()`](/docs/webcodecs/webcodecs-controller#abort) on the controller to pause, resume and abort the decoding.\n\n### `logLevel?`\n\n_string_ <TsType type=\"LogLevel\" source=\"@remotion/media-parser\"/>\n\nOne of `\"error\"`, `\"warn\"`, `\"info\"`, `\"debug\"`, `\"trace\"`.  \nDefault value: `\"info\"`, which logs only important information.\n\n## Return type\n\nReturns an object with the following properties:\n\n### `waitForQueueToBeLessThan()`\n\nPass a number to wait for the queue to be less than the given number.\n\nA promise that resolves when the queue size is less than the given number.  \nThe queue is only decremented when the[ `onFrame`](#onframe) callback resolves.\n\n### `flush()`\n\nFlushes the decoder, forcing the queue to be cleared. Returns a promise that resolves when all frames have been cleared and the [`onFrame()`](#onframe) callback has beeen resolved for all frames.\n\n### `reset()`\n\nClears the queue and resets the decoder. Same as [`VideoDecoder.reset()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder/reset) + [`VideoDecoder.configure()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder/close).\n\n### `close()`\n\nCloses the decoder. Same as [`AudioDecoder.close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/close).\n\n### `checkReset()`<AvailableFrom v=\"4.0.312\" />\n\nReturns a handle with a `wasReset()` function. If the decoder was reset inbetween the call to `.checkReset()` and the call to `wasReset()`, `wasReset()` will return `true`. See [below](#checking-if-the-decoder-was-reset) for an example.\n\n### `getMostRecentSampleInput()`<AvailableFrom v=\"4.0.312\" />\n\nReturn the `.timestamp` of the most recently input sample.\n\n## Example usage with `@remotion/media-parser`\n\n```tsx twoslash title=\"Decode a video track\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {createVideoDecoder} from '@remotion/webcodecs';\n\nawait parseMedia({\n  src: 'https://remotion.media/video.mp4',\n  onVideoTrack: async ({track, container}) => {\n    const decoder = await createVideoDecoder({\n      track,\n      onFrame: console.log,\n      onError: console.error,\n    });\n\n    return async (sample) => {\n      // Called on every sample\n      await decoder.waitForQueueToBeLessThan(10);\n      await decoder.decode(sample);\n\n      return async () => {\n        // Called when the track is done\n        await decoder.flush();\n        decoder.close();\n      };\n    };\n  },\n});\n```\n\n## Checking if the decoder was reset\n\nA potential race condition you may face is that `decoder.reset()` is called while a sample is waiting for the queue to be less than a certain number. Use `.checkReset()` to check if the decoder was reset after any asynchronous operation, and abort the processing of the sample if needed.\n\n```tsx twoslash title=\"Check if the decoder was reset\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {createVideoDecoder} from '@remotion/webcodecs';\n\nawait parseMedia({\n  src: 'https://remotion.media/video.mp4',\n  onVideoTrack: async ({track, container}) => {\n    const decoder = await createVideoDecoder({\n      track,\n      onFrame: console.log,\n      onError: console.error,\n    });\n\n    return async (sample) => {\n      const {wasReset} = decoder.checkReset();\n\n      await decoder.waitForQueueToBeLessThan(10);\n      if (wasReset()) {\n        return;\n      }\n\n      await decoder.decode(sample);\n      if (wasReset()) {\n        return;\n      }\n\n      return async () => {\n        if (wasReset()) {\n          return;\n        }\n\n        // Called when the track is done\n        await decoder.flush();\n        decoder.close();\n      };\n    };\n  },\n});\n```\n\n## Undecodable video<AvailableFrom v=\"4.0.333\" />\n\nIf the video cannot be decoded by the browser, an `VideoUndecodableError` will be thrown.\n\n```tsx twoslash title=\"Undecodable audio\"\nimport {VideoUndecodableError, createVideoDecoder} from '@remotion/webcodecs';\n\ntry {\n  await createVideoDecoder({\n    track: {codec: 'invalid'},\n    onFrame: console.log,\n    onError: console.error,\n  });\n} catch (error) {\n  if (error instanceof VideoUndecodableError) {\n    console.log('The video cannot be decoded by this browser');\n  } else {\n    throw error;\n  }\n}\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/create-video-decoder.ts)\n- [`@remotion/webcodecs`](/docs/webcodecs)\n"

This function is a wrapper around the [`VideoDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder) Web API.

```

Create a video decoder
import {createVideoDecoder} from '@remotion/webcodecs';

const decoder = await createVideoDecoder({
  track,
  onFrame: console.log,
  onError: console.error,
});Copy
```

## Differences to `VideoDecoder`[​](#differences-to-videodecoder)

- Two new methods are added: [`.waitForQueueToBeLessThan()`](#waitforqueuetobelessthan) and `.waitForFinish()`.

- The [`dequeue`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder/dequeue_event) event is not supported as it is not reliable across browsers.

- In addition to [`EncodedVideoChunk`](https://developer.mozilla.org/en-US/docs/Web/API/EncodedVideoChunk), [`EncodedVideoChunkInit`](https://www.w3.org/TR/webcodecs/#dictdef-encodedvideochunkinit) objects are also accepted for `.decode()`.

- A [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance can be passed in to the function, allowing for decoding to be paused, resumed and aborted.

- `.decode()` is async, and returns a promise, allowing for a halt if the decoder is paused.

- A [`logLevel`](#loglevel) can be passed in to the function, allowing the queue to be debugged.

- The [`onFrame`](#onframe) callback is being awaited. When rejected, the error lands in the [`onError`](#onerror) callback. When resolved, only then the queue size counter will be decreased.

## API[​](#api)

Takes an object with the following properties:

### `track`[​](#track)

An [`VideoDecoderConfig`](https://www.w3.org/TR/webcodecs/#dictdef-videodecoderconfig) object.

You may pass a [`MediaParserVideoTrack`](/docs/media-parser/types#mediaparservideotrack) object from [`parseMedia()`](/docs/media-parser/parse-media), which also is an `VideoDecoderConfig` object.

### `onFrame`[​](#onframe)

A callback that is called when a frame is decoded.

Takes a single argument, which is a [`VideoFrame`](https://developer.mozilla.org/en-US/docs/Web/API/VideoFrame) object.

If the passed callback is asynchronous, the queue size counter will be decreased only after the callback has been resolved.

However, the callback for the next frame may already be called while your callback is still running.

We do not ensure that callbacks are running sequentially.

### `onError`[​](#onerror)

A callback that is called when an error occurs or the decode is aborted through the controller.

Takes a single argument, which is an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object.

### `controller?`[​](#controller)

A [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance.

If provided, you can call [`.pause()`](/docs/webcodecs/webcodecs-controller#pause), [`.resume()`](/docs/webcodecs/webcodecs-controller#resume) and [`.abort()`](/docs/webcodecs/webcodecs-controller#abort) on the controller to pause, resume and abort the decoding.

### `logLevel?`[​](#loglevel)

*string* `LogLevel`

One of `"error"`, `"warn"`, `"info"`, `"debug"`, `"trace"`.

Default value: `"info"`, which logs only important information.

## Return type[​](#return-type)

Returns an object with the following properties:

### `waitForQueueToBeLessThan()`[​](#waitforqueuetobelessthan)

Pass a number to wait for the queue to be less than the given number.

A promise that resolves when the queue size is less than the given number.

The queue is only decremented when the[ `onFrame`](#onframe) callback resolves.

### `flush()`[​](#flush)

Flushes the decoder, forcing the queue to be cleared. Returns a promise that resolves when all frames have been cleared and the [`onFrame()`](#onframe) callback has beeen resolved for all frames.

### `reset()`[​](#reset)

Clears the queue and resets the decoder. Same as [`VideoDecoder.reset()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder/reset) + [`VideoDecoder.configure()`](https://developer.mozilla.org/en-US/docs/Web/API/VideoDecoder/close).

### `close()`[​](#close)

Closes the decoder. Same as [`AudioDecoder.close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/close).

### `checkReset()`[v4.0.312](https://github.com/remotion-dev/remotion/releases/v4.0.312)[​](#checkreset)

Returns a handle with a `wasReset()` function. If the decoder was reset inbetween the call to `.checkReset()` and the call to `wasReset()`, `wasReset()` will return `true`. See [below](#checking-if-the-decoder-was-reset) for an example.

### `getMostRecentSampleInput()`[v4.0.312](https://github.com/remotion-dev/remotion/releases/v4.0.312)[​](#getmostrecentsampleinput)

Return the `.timestamp` of the most recently input sample.

## Example usage with `@remotion/media-parser`[​](#example-usage-with-remotionmedia-parser)

```

Decode a video trackimport {parseMedia} from '@remotion/media-parser';
import {createVideoDecoder} from '@remotion/webcodecs';

await parseMedia({
  src: 'https://remotion.media/video.mp4',
  onVideoTrack: async ({track, container}) => {
    const decoder = await createVideoDecoder({
      track,
      onFrame: console.log,
      onError: console.error,
    });

    return async (sample) => {
      // Called on every sample
      await decoder.waitForQueueToBeLessThan(10);
      await decoder.decode(sample);

      return async () => {
        // Called when the track is done
        await decoder.flush();
        decoder.close();
      };
    };
  },
});Copy
```

## Checking if the decoder was reset[​](#checking-if-the-decoder-was-reset)

A potential race condition you may face is that `decoder.reset()` is called while a sample is waiting for the queue to be less than a certain number. Use `.checkReset()` to check if the decoder was reset after any asynchronous operation, and abort the processing of the sample if needed.

```

Check if the decoder was resetimport {parseMedia} from '@remotion/media-parser';
import {createVideoDecoder} from '@remotion/webcodecs';

await parseMedia({
  src: 'https://remotion.media/video.mp4',
  onVideoTrack: async ({track, container}) => {
    const decoder = await createVideoDecoder({
      track,
      onFrame: console.log,
      onError: console.error,
    });

    return async (sample) => {
      const {wasReset} = decoder.checkReset();

      await decoder.waitForQueueToBeLessThan(10);
      if (wasReset()) {
        return;
      }

      await decoder.decode(sample);
      if (wasReset()) {
        return;
      }

      return async () => {
        if (wasReset()) {
          return;
        }

        // Called when the track is done
        await decoder.flush();
        decoder.close();
      };
    };
  },
});Copy
```

## Undecodable video[v4.0.333](https://github.com/remotion-dev/remotion/releases/v4.0.333)[​](#undecodable-video)

If the video cannot be decoded by the browser, an `VideoUndecodableError` will be thrown.

```

Undecodable audioimport {VideoUndecodableError, createVideoDecoder} from '@remotion/webcodecs';

try {
  await createVideoDecoder({
    track: {codec: 'invalid'},
    onFrame: console.log,
    onError: console.error,
  });
} catch (error) {
  if (error instanceof VideoUndecodableError) {
    console.log('The video cannot be decoded by this browser');
  } else {
    throw error;
  }
}Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/create-video-decoder.ts)

- [`@remotion/webcodecs`](/docs/webcodecs)
](/docs/webcodecs)](/docs/webcodecs)
](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)
- ](/docs/webcodecs)