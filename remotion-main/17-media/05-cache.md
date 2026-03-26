---
title: "Cache"
url: "https://www.remotion.dev/docs/media/cache"
path: "/docs/media/cache"
---

"---\nimage: /generated/articles-docs-media-cache.png\ntitle: In-memory cache for @remotion/media\nsidebar_label: Cache\ncrumb: 'API - @remotion/media'\n---\n\n[`@remotion/media`](/docs/media) keeps a cache of recently decoded video and audio frames.\n\n## Mechanism\n\nVideo streams consist of key frames and delta frames.  \nIn order to decode a delta frame, the last keyframe and all the delta frames since the last keyframe also need to be decoded.\n\nDue to Remotion's [multithreaded rendering and each frame being independent](/docs/flickering), it is not guaranteed that video frames are needed in their natural order.\n\nThe cache is shared across all of the instances of [`<Video>`](/docs/media/video) and [`<Audio>`](/docs/media/audio).  \nTherefore, the settings for the cache are per-render, not per tag.\n\n## Default cache size\n\nBy default, the cache may grow to up to 50% of the available system memory.  \nA minimum of 500MB and a maximum of 20GB is enforced.\n\n## Customizing the cache size\n\nThe rendering APIs allow you to customize this limit on a per-render basis:\n\n- [`renderMedia()` → `mediaCacheSizeInBytes`](/docs/renderer/render-media#mediacachesizeinbytes)\n- [`renderStill()` → `mediaCacheSizeInBytes`](/docs/renderer/render-still#mediacachesizeinbytes)\n- [`selectComposition()` → `mediaCacheSizeInBytes`](/docs/renderer/select-composition#mediacachesizeinbytes)\n- [`renderMediaOnCloudRun()` → `mediaCacheSizeInBytes`](/docs/cloudrun/rendermediaoncloudrun#mediacachesizeinbytes)\n- [`renderStillOnCloudRun()` → `mediaCacheSizeInBytes`](/docs/cloudrun/renderstilloncloudrun#mediacachesizeinbytes)\n- [`getCompositionsOnLambda()` → `mediaCacheSizeInBytes`](/docs/lambda/getcompositionsonlambda#mediacachesizeinbytes)\n- [`renderMediaOnLambda()` → `mediaCacheSizeInBytes`](/docs/lambda/rendermediaonlambda#mediacachesizeinbytes)\n- [`renderStillOnLambda()` → `mediaCacheSizeInBytes`](/docs/lambda/renderstillonlambda#mediacachesizeinbytes)\n- [`getCompositions()` → `mediaCacheSizeInBytes`](/docs/lambda/getcompositionsonlambda#mediacachesizeinbytes)\n- [`renderFrames()` → `mediaCacheSizeInBytes`](/docs/renderer/render-frames#mediacachesizeinbytes)\n- [`npx remotion benchmark` → `--media-cache-size-in-bytes`](/docs/cli/benchmark#--media-cache-size-in-bytes)\n- [`npx remotion compositions` → `--media-cache-size-in-bytes`](/docs/cli/compositions#--media-cache-size-in-bytes)\n- [`npx remotion render` → `--media-cache-size-in-bytes`](/docs/cli/render#--media-cache-size-in-bytes)\n- [`npx remotion still` → `--media-cache-size-in-bytes`](/docs/cli/still#--media-cache-size-in-bytes)\n- [`npx remotion lambda render` → `--media-cache-size-in-bytes`](/docs/lambda/cli/render#--media-cache-size-in-bytes)\n- [`npx remotion lambda still` → `--media-cache-size-in-bytes`](/docs/lambda/cli/still#--media-cache-size-in-bytes)\n- [`npx remotion lambda compositions` → `--media-cache-size-in-bytes`](/docs/lambda/cli/compositions#--media-cache-size-in-bytes)\n- [`npx remotion cloudrun render` → `--media-cache-size-in-bytes`](/docs/cloudrun/cli/render#--media-cache-size-in-bytes)\n- [`npx remotion cloudrun still` → `--media-cache-size-in-bytes`](/docs/cloudrun/cli/still#--media-cache-size-in-bytes)\n- [`npx remotion cloudrun render` → `--media-cache-size-in-bytes`](/docs/cloudrun/cli/render#--media-cache-size-in-bytes)\n- [Remotion Studio](/docs/studio): Set the cache size under the \"Advanced\" tab\n"

[`@remotion/media`](/docs/media) keeps a cache of recently decoded video and audio frames.

## Mechanism[​](#mechanism)

Video streams consist of key frames and delta frames.

In order to decode a delta frame, the last keyframe and all the delta frames since the last keyframe also need to be decoded.

Due to Remotion's [multithreaded rendering and each frame being independent](/docs/flickering), it is not guaranteed that video frames are needed in their natural order.

The cache is shared across all of the instances of [`<Video>`](/docs/media/video) and [`<Audio>`](/docs/media/audio).

Therefore, the settings for the cache are per-render, not per tag.

## Default cache size[​](#default-cache-size)

By default, the cache may grow to up to 50% of the available system memory.

A minimum of 500MB and a maximum of 20GB is enforced.

## Customizing the cache size[​](#customizing-the-cache-size)

The rendering APIs allow you to customize this limit on a per-render basis:

- [`renderMedia()` → `mediaCacheSizeInBytes`](/docs/renderer/render-media#mediacachesizeinbytes)

- [`renderStill()` → `mediaCacheSizeInBytes`](/docs/renderer/render-still#mediacachesizeinbytes)

- [`selectComposition()` → `mediaCacheSizeInBytes`](/docs/renderer/select-composition#mediacachesizeinbytes)

- [`renderMediaOnCloudRun()` → `mediaCacheSizeInBytes`](/docs/cloudrun/rendermediaoncloudrun#mediacachesizeinbytes)

- [`renderStillOnCloudRun()` → `mediaCacheSizeInBytes`](/docs/cloudrun/renderstilloncloudrun#mediacachesizeinbytes)

- [`getCompositionsOnLambda()` → `mediaCacheSizeInBytes`](/docs/lambda/getcompositionsonlambda#mediacachesizeinbytes)

- [`renderMediaOnLambda()` → `mediaCacheSizeInBytes`](/docs/lambda/rendermediaonlambda#mediacachesizeinbytes)

- [`renderStillOnLambda()` → `mediaCacheSizeInBytes`](/docs/lambda/renderstillonlambda#mediacachesizeinbytes)

- [`getCompositions()` → `mediaCacheSizeInBytes`](/docs/lambda/getcompositionsonlambda#mediacachesizeinbytes)

- [`renderFrames()` → `mediaCacheSizeInBytes`](/docs/renderer/render-frames#mediacachesizeinbytes)

- [`npx remotion benchmark` → `--media-cache-size-in-bytes`](/docs/cli/benchmark#--media-cache-size-in-bytes)

- [`npx remotion compositions` → `--media-cache-size-in-bytes`](/docs/cli/compositions#--media-cache-size-in-bytes)

- [`npx remotion render` → `--media-cache-size-in-bytes`](/docs/cli/render#--media-cache-size-in-bytes)

- [`npx remotion still` → `--media-cache-size-in-bytes`](/docs/cli/still#--media-cache-size-in-bytes)

- [`npx remotion lambda render` → `--media-cache-size-in-bytes`](/docs/lambda/cli/render#--media-cache-size-in-bytes)

- [`npx remotion lambda still` → `--media-cache-size-in-bytes`](/docs/lambda/cli/still#--media-cache-size-in-bytes)

- [`npx remotion lambda compositions` → `--media-cache-size-in-bytes`](/docs/lambda/cli/compositions#--media-cache-size-in-bytes)

- [`npx remotion cloudrun render` → `--media-cache-size-in-bytes`](/docs/cloudrun/cli/render#--media-cache-size-in-bytes)

- [`npx remotion cloudrun still` → `--media-cache-size-in-bytes`](/docs/cloudrun/cli/still#--media-cache-size-in-bytes)

- [`npx remotion cloudrun render` → `--media-cache-size-in-bytes`](/docs/cloudrun/cli/render#--media-cache-size-in-bytes)

- [Remotion Studio](/docs/studio): Set the cache size under the "Advanced" tab
](/docs/studio)](/docs/studio)
](/docs/studio)
- ](/docs/studio)
- ](/docs/studio)