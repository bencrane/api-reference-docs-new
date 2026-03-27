---
title: "createAudioDecoder()"
url: "https://www.remotion.dev/docs/webcodecs/create-audio-decoder"
path: "/docs/webcodecs/create-audio-decoder"
---

"---\nimage: /generated/articles-docs-webcodecs-create-audio-decoder.png\nsidebar_label: createAudioDecoder()\ntitle: createAudioDecoder()\nslug: /webcodecs/create-audio-decoder\ncrumb: '@remotion/webcodecs'\n---\n\n:::warning\n[We are phasing out Remotion WebCodecs and are moving to Mediabunny](/blog/mediabunny)!\n:::\n\nimport {UnstableDisclaimer} from './UnstableDisclaimer';\n\n:::warning\n\n<UnstableDisclaimer />\n:::\n\n# createAudioDecoder()<AvailableFrom v=\"4.0.307\" />\n\nThis function is a wrapper around the [`AudioDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder) Web API.\n\n```tsx twoslash title=\"Create an audio decoder\"\nimport type {MediaParserAudioTrack} from '@remotion/media-parser';\n\nconst track = {} as unknown as MediaParserAudioTrack;\n\n// ---cut---\n\nimport {createAudioDecoder} from '@remotion/webcodecs';\n\nconst decoder = await createAudioDecoder({\n  track,\n  onFrame: console.log,\n  onError: console.error,\n});\n```\n\n## Differences to `AudioDecoder`\n\n- Samples with a `codec` of `pcm-s16` are accepted and passed through, even if the `AudioDecoder` object does not exist or support it.\n- Two new methods are added: [`.waitForQueueToBeLessThan()`](#waitforqueuetobelessthan) and `.waitForFinish()`.\n- The [`dequeue`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/dequeue_event) event is not supported as it is not reliable across browsers.\n- In addition to [`EncodedAudioChunk`](https://developer.mozilla.org/en-US/docs/Web/API/EncodedAudioChunk), [`EncodedAudioChunkInit`](https://www.w3.org/TR/webcodecs/#dictdef-encodedaudiochunkinit) objects are also accepted for `.decode()`.\n- A [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance can be passed in to the function, allowing for decoding to be paused, resumed and aborted.\n- `.decode()` is async, and returns a promise, allowing for a halt if the decoder is paused.\n- Only samples with a size of 16 bytes or more are actually being input, [to avoid a bug in Chrome](https://github.com/remotion-dev/remotion/blob/c7f18a85bcb1bc58d3811efcd9e68c96ff38ccae/packages/webcodecs/src/create-audio-decoder.ts#L121-L129).\n- A [`logLevel`](#loglevel) can be passed in to the function, allowing the queue to be debugged.\n- The [`onFrame`](#onframe) callback is being awaited. When rejected, the error lands in the [`onError`](#onerror) callback. When resolved, only then the queue size counter will be decreased.\n\n## API\n\nTakes an object with the following properties:\n\n### `track`\n\nAn [`AudioDecoderConfig`](https://www.w3.org/TR/webcodecs/#dictdef-audiodecoderconfig) object.  \nYou may pass a [`MediaParserAudioTrack`](/docs/media-parser/types#mediaparseraudiotrack) object from [`parseMedia()`](/docs/media-parser/parse-media), which also is an `AudioDecoderConfig` object.\n\n### `onFrame`\n\nA callback that is called when an audio frame is decoded.\n\nTakes a single argument, which is an [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object.\n\nIf the passed callback is asynchronous, the queue size counter will be decreased only after the callback has been resolved.\n\nHowever, the callback for the next frame may already be called while your callback is still running.  \nWe do not ensure that callbacks are running sequentially.\n\n### `onError`\n\nA callback that is called when an error occurs or the decode is aborted through the controller.\n\nTakes a single argument, which is an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object.\n\n### `controller?`\n\nA [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance.\n\nIf provided, you can call [`.pause()`](/docs/webcodecs/webcodecs-controller#pause), [`.resume()`](/docs/webcodecs/webcodecs-controller#resume) and [`.abort()`](/docs/webcodecs/webcodecs-controller#abort) on the controller to pause, resume and abort the decoding.\n\n### `logLevel?`\n\n_string_ <TsType type=\"LogLevel\" source=\"@remotion/media-parser\"/>\n\nOne of `\"error\"`, `\"warn\"`, `\"info\"`, `\"debug\"`, `\"trace\"`.  \nDefault value: `\"info\"`, which logs only important information.\n\n## Return type\n\nReturns an object with the following properties:\n\n### `decode(sample: EncodedAudioChunkInit | EncodedAudioChunk)`\n\nDecodes a sample. Same as [`AudioDecoder.decode()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/decode).  \nYou can pass in a [`MediaParserAudioSample`](/docs/media-parser/types#mediaparseraudiosample) object from [`parseMedia()`](/docs/media-parser/parse-media), which also satisfies the [`EncodedAudioChunkInit`](https://www.w3.org/TR/webcodecs/#dictdef-encodedaudiochunkinit) interface.\n\n### `waitForQueueToBeLessThan()`\n\nPass a number to wait for the queue to be less than the given number.\n\nA promise that resolves when the queue size is less than the given number.  \nThe queue is only decremented when the[ `onFrame`](#onframe) callback resolves.\n\n### `flush()`\n\nFlushes the decoder, forcing the queue to be cleared. Returns a promise that resolves when all frames have been cleared and the [`onFrame()`](#onframe) callback has beeen resolved for all frames.\n\n### `reset()`\n\nClears the queue and resets the decoder. Same as [`AudioDecoder.reset()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/reset) + [`AudioDecoder.configure()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/close).\n\n### `close()`\n\nCloses the decoder. Same as [`AudioDecoder.close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/close).\n\n### `checkReset()`<AvailableFrom v=\"4.0.312\" />\n\nReturns a handle with a `wasReset()` function. If the decoder was reset inbetween the call to `.checkReset()` and the call to `wasReset()`, `wasReset()` will return `true`. See [below](#checking-if-the-decoder-was-reset) for an example.\n\n### `getMostRecentSampleInput()`<AvailableFrom v=\"4.0.312\" />\n\nReturn the `.timestamp` of the most recently input sample.\n\n## Example usage with `@remotion/media-parser`\n\nIn this example, the whole audio track is decoded and the decoder is closed when the track is done.  \nBy using `async` / `await`, the [`parseMedia()`](/docs/media-parser/parse-media) call is artificially slowed down to not flood the `AudioDecoder` and cause much memory to be allocated.\n\n```tsx twoslash title=\"Decode an audio track\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {createAudioDecoder} from '@remotion/webcodecs';\n\nawait parseMedia({\n  src: 'https://remotion.media/video.mp4',\n  onAudioTrack: async ({track, container}) => {\n    const decoder = await createAudioDecoder({\n      track,\n      onFrame: console.log,\n      onError: console.error,\n    });\n\n    return async (sample) => {\n      // Called on every sample\n      await decoder.waitForQueueToBeLessThan(10);\n      await decoder.decode(sample);\n\n      return async () => {\n        // Called when the track is done\n        await decoder.flush();\n        decoder.close();\n      };\n    };\n  },\n});\n```\n\n## Checking if the decoder was reset\n\nA potential race condition you may face is that `decoder.reset()` is called while a sample is waiting for the queue to be less than a certain number. Use `.checkReset()` to check if the decoder was reset after any asynchronous operation, and abort the processing of the sample if needed.\n\n```tsx twoslash title=\"Check if the decoder was reset\"\nimport {parseMedia} from '@remotion/media-parser';\nimport {createAudioDecoder} from '@remotion/webcodecs';\n\nawait parseMedia({\n  src: 'https://remotion.media/video.mp4',\n  onAudioTrack: async ({track, container}) => {\n    const decoder = await createAudioDecoder({\n      track,\n      onFrame: console.log,\n      onError: console.error,\n    });\n\n    return async (sample) => {\n      const {wasReset} = decoder.checkReset();\n\n      await decoder.waitForQueueToBeLessThan(10);\n      if (wasReset()) {\n        return;\n      }\n\n      await decoder.decode(sample);\n      if (wasReset()) {\n        return;\n      }\n\n      return async () => {\n        if (wasReset()) {\n          return;\n        }\n\n        // Called when the track is done\n        await decoder.flush();\n        decoder.close();\n      };\n    };\n  },\n});\n```\n\n## Undecodable audio<AvailableFrom v=\"4.0.333\" />\n\nIf the audio cannot be decoded by the browser, an `AudioUndecodableError` will be thrown.\n\n```tsx twoslash title=\"Undecodable audio\"\nimport {AudioUndecodableError, createAudioDecoder} from '@remotion/webcodecs';\n\ntry {\n  await createAudioDecoder({\n    // @ts-expect-error - Invalid codec\n    track: {codec: 'invalid'},\n    onFrame: console.log,\n    onError: console.error,\n  });\n} catch (error) {\n  if (error instanceof AudioUndecodableError) {\n    console.log('The audio cannot be decoded by this browser');\n  } else {\n    throw error;\n  }\n}\n```\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/create-audio-decoder.ts)\n- [`@remotion/webcodecs`](/docs/webcodecs)\n"

This function is a wrapper around the [`AudioDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder) Web API.

```

Create an audio decoder
import {createAudioDecoder} from '@remotion/webcodecs';

const decoder = await createAudioDecoder({
  track,
  onFrame: console.log,
  onError: console.error,
});Copy
```

## Differences to `AudioDecoder`[​](#differences-to-audiodecoder)

- Samples with a `codec` of `pcm-s16` are accepted and passed through, even if the `AudioDecoder` object does not exist or support it.

- Two new methods are added: [`.waitForQueueToBeLessThan()`](#waitforqueuetobelessthan) and `.waitForFinish()`.

- The [`dequeue`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/dequeue_event) event is not supported as it is not reliable across browsers.

- In addition to [`EncodedAudioChunk`](https://developer.mozilla.org/en-US/docs/Web/API/EncodedAudioChunk), [`EncodedAudioChunkInit`](https://www.w3.org/TR/webcodecs/#dictdef-encodedaudiochunkinit) objects are also accepted for `.decode()`.

- A [`webcodecsController()`](/docs/webcodecs/webcodecs-controller) instance can be passed in to the function, allowing for decoding to be paused, resumed and aborted.

- `.decode()` is async, and returns a promise, allowing for a halt if the decoder is paused.

- Only samples with a size of 16 bytes or more are actually being input, [to avoid a bug in Chrome](https://github.com/remotion-dev/remotion/blob/c7f18a85bcb1bc58d3811efcd9e68c96ff38ccae/packages/webcodecs/src/create-audio-decoder.ts#L121-L129).

- A [`logLevel`](#loglevel) can be passed in to the function, allowing the queue to be debugged.

- The [`onFrame`](#onframe) callback is being awaited. When rejected, the error lands in the [`onError`](#onerror) callback. When resolved, only then the queue size counter will be decreased.

## API[​](#api)

Takes an object with the following properties:

### `track`[​](#track)

An [`AudioDecoderConfig`](https://www.w3.org/TR/webcodecs/#dictdef-audiodecoderconfig) object.

You may pass a [`MediaParserAudioTrack`](/docs/media-parser/types#mediaparseraudiotrack) object from [`parseMedia()`](/docs/media-parser/parse-media), which also is an `AudioDecoderConfig` object.

### `onFrame`[​](#onframe)

A callback that is called when an audio frame is decoded.

Takes a single argument, which is an [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) object.

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

### `decode(sample: EncodedAudioChunkInit | EncodedAudioChunk)`[​](#decodesample-encodedaudiochunkinit--encodedaudiochunk)

Decodes a sample. Same as [`AudioDecoder.decode()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/decode).

You can pass in a [`MediaParserAudioSample`](/docs/media-parser/types#mediaparseraudiosample) object from [`parseMedia()`](/docs/media-parser/parse-media), which also satisfies the [`EncodedAudioChunkInit`](https://www.w3.org/TR/webcodecs/#dictdef-encodedaudiochunkinit) interface.

### `waitForQueueToBeLessThan()`[​](#waitforqueuetobelessthan)

Pass a number to wait for the queue to be less than the given number.

A promise that resolves when the queue size is less than the given number.

The queue is only decremented when the[ `onFrame`](#onframe) callback resolves.

### `flush()`[​](#flush)

Flushes the decoder, forcing the queue to be cleared. Returns a promise that resolves when all frames have been cleared and the [`onFrame()`](#onframe) callback has beeen resolved for all frames.

### `reset()`[​](#reset)

Clears the queue and resets the decoder. Same as [`AudioDecoder.reset()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/reset) + [`AudioDecoder.configure()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/close).

### `close()`[​](#close)

Closes the decoder. Same as [`AudioDecoder.close()`](https://developer.mozilla.org/en-US/docs/Web/API/AudioDecoder/close).

### `checkReset()`[v4.0.312](https://github.com/remotion-dev/remotion/releases/v4.0.312)[​](#checkreset)

Returns a handle with a `wasReset()` function. If the decoder was reset inbetween the call to `.checkReset()` and the call to `wasReset()`, `wasReset()` will return `true`. See [below](#checking-if-the-decoder-was-reset) for an example.

### `getMostRecentSampleInput()`[v4.0.312](https://github.com/remotion-dev/remotion/releases/v4.0.312)[​](#getmostrecentsampleinput)

Return the `.timestamp` of the most recently input sample.

## Example usage with `@remotion/media-parser`[​](#example-usage-with-remotionmedia-parser)

In this example, the whole audio track is decoded and the decoder is closed when the track is done.

By using `async` / `await`, the [`parseMedia()`](/docs/media-parser/parse-media) call is artificially slowed down to not flood the `AudioDecoder` and cause much memory to be allocated.

```

Decode an audio trackimport {parseMedia} from '@remotion/media-parser';
import {createAudioDecoder} from '@remotion/webcodecs';

await parseMedia({
  src: 'https://remotion.media/video.mp4',
  onAudioTrack: async ({track, container}) => {
    const decoder = await createAudioDecoder({
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
import {createAudioDecoder} from '@remotion/webcodecs';

await parseMedia({
  src: 'https://remotion.media/video.mp4',
  onAudioTrack: async ({track, container}) => {
    const decoder = await createAudioDecoder({
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

## Undecodable audio[v4.0.333](https://github.com/remotion-dev/remotion/releases/v4.0.333)[​](#undecodable-audio)

If the audio cannot be decoded by the browser, an `AudioUndecodableError` will be thrown.

```

Undecodable audioimport {AudioUndecodableError, createAudioDecoder} from '@remotion/webcodecs';

try {
  await createAudioDecoder({
    // @ts-expect-error - Invalid codec
    track: {codec: 'invalid'},
    onFrame: console.log,
    onError: console.error,
  });
} catch (error) {
  if (error instanceof AudioUndecodableError) {
    console.log('The audio cannot be decoded by this browser');
  } else {
    throw error;
  }
}Copy
```

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/webcodecs/src/create-audio-decoder.ts)

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
- ](/docs/webcodecs)