---
title: "<Artifact>"
url: "https://www.remotion.dev/docs/artifact"
path: "/docs/artifact"
---

"---\nimage: /generated/articles-docs-artifact.png\ntitle: '<Artifact>'\ncrumb: API\n---\n\n# `<Artifact>`<AvailableFrom v=\"4.0.176\"/>\n\nBy rendering an `<Artifact>` tag in your Remotion markup, [an extra file will get emitted during rendering](/docs/artifacts).\n\n```tsx twoslash title=\"MyComp.tsx\"\nimport {Artifact, useCurrentFrame} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const frame = useCurrentFrame();\n\n  return frame === 0 ? <Artifact filename=\"my-file.txt\" content=\"Hello World!\" /> : null;\n};\n```\n\nIf rendered on the CLI or via the Studio, this will emit an additional file:\n\n```\n$ npx remotion render MyComp\n+ out/MyComp.mp4\n+ my-file.txt (12B)\n```\n\nIt is allowed for a composition to emit multiple files.  \nHowever, the file names must be unique.\n\nThe component will get evaluated on every frame, which means if you want to emit just one file, only render it on one frame.\n\n```tsx twoslash title=\"❌ Will generate an asset on every frame and throw an error because the file name is not unique\"\nimport {Artifact, useCurrentFrame} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const frame = useCurrentFrame();\n\n  return frame === 0 ? <Artifact filename=\"my-file.txt\" content=\"Hello World!\" /> : null;\n};\n```\n\n## API\n\n### `filename`\n\nA string that is the name of the file that will be emitted.  \nUse forward slashes only, even on Windows.  \nMust match the regex `/^([0-9a-zA-Z-!_.*'()/:&$@=;+,?]+)/g`.\n\n### `content`\n\nA `string` or `Uint8Array` that is the content of the file that will be emitted. Don't consider an `Uint8Array` to be faster, because it needs to be serialized.\n\n### `downloadBehavior?`<AvailableFrom v=\"4.0.296\" />\n\nOnly applies to serverless rendering.\n\nHow the output file should behave when accessed through the output link in the browser.  \nEither:\n\n- `{\"type\": \"play-in-browser\"}` - the default. The video will play in the browser.\n- `{\"type\": \"download\", fileName: null}` or `{\"type\": \"download\", fileName: \"download.mp4\"}` - a `Content-Disposition` header will be added which makes the browser download the file. You can optionally override the filename.\n\nThe default behavior is the same download behavior you defined for the main rendering output.\n\n## `Artifact.Thumbnail`<AvailableFrom v=\"4.0.290\" />\n\nA special symbol that if you pass it to the [`content`](/docs/artifact#content) prop, it will [emit the image data of the current frame as an artifact](/docs/artifacts#emitting-thumbnails).\n\n```tsx twoslash title=\"Emitting the first frame as a thumbnail\"\nimport {Artifact, useCurrentFrame} from 'remotion';\n\nexport const MyComp: React.FC = () => {\n  const frame = useCurrentFrame();\n  return <>{frame === 0 ? <Artifact content={Artifact.Thumbnail} filename=\"thumbnail.jpeg\" /> : null}</>;\n};\n```\n\nSee the [Emitting Thumbnails](/docs/artifacts#emitting-thumbnails) page for more important information.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs=\"\" bun=\"\" serverlessFunctions=\"\" clientSideRendering serverSideRendering player=\"No-op\" studio=\"No-op\" hideServers />\n\n## See also\n\n- [Emitting Artifacts](/docs/artifacts)\n- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)\n"

By rendering an `<Artifact>` tag in your Remotion markup, [an extra file will get emitted during rendering](/docs/artifacts).

```

MyComp.tsximport {Artifact, useCurrentFrame} from 'remotion';

export const MyComp: React.FC = () => {
  const frame = useCurrentFrame();

  return frame === 0 ? <Artifact filename="my-file.txt" content="Hello World!" /> : null;
};Copy
```

If rendered on the CLI or via the Studio, this will emit an additional file:

```
$ npx remotion render MyComp
+ out/MyComp.mp4
+ my-file.txt (12B)Copy
```

It is allowed for a composition to emit multiple files.

However, the file names must be unique.

The component will get evaluated on every frame, which means if you want to emit just one file, only render it on one frame.

```

❌ Will generate an asset on every frame and throw an error because the file name is not uniqueimport {Artifact, useCurrentFrame} from 'remotion';

export const MyComp: React.FC = () => {
  const frame = useCurrentFrame();

  return frame === 0 ? <Artifact filename="my-file.txt" content="Hello World!" /> : null;
};Copy
```

## API[​](#api)

### `filename`[​](#filename)

A string that is the name of the file that will be emitted.

Use forward slashes only, even on Windows.

Must match the regex `/^([0-9a-zA-Z-!_.*'()/:&$@=;+,?]+)/g`.

### `content`[​](#content)

A `string` or `Uint8Array` that is the content of the file that will be emitted. Don't consider an `Uint8Array` to be faster, because it needs to be serialized.

### `downloadBehavior?`[v4.0.296](https://github.com/remotion-dev/remotion/releases/v4.0.296)[​](#downloadbehavior)

Only applies to serverless rendering.

How the output file should behave when accessed through the output link in the browser.

Either:

- `{"type": "play-in-browser"}` - the default. The video will play in the browser.

- `{"type": "download", fileName: null}` or `{"type": "download", fileName: "download.mp4"}` - a `Content-Disposition` header will be added which makes the browser download the file. You can optionally override the filename.

The default behavior is the same download behavior you defined for the main rendering output.

## `Artifact.Thumbnail`[v4.0.290](https://github.com/remotion-dev/remotion/releases/v4.0.290)[​](#artifactthumbnail)

A special symbol that if you pass it to the [`content`](/docs/artifact#content) prop, it will [emit the image data of the current frame as an artifact](/docs/artifacts#emitting-thumbnails).

```

Emitting the first frame as a thumbnailimport {Artifact, useCurrentFrame} from 'remotion';

export const MyComp: React.FC = () => {
  const frame = useCurrentFrame();
  return <>{frame === 0 ? <Artifact content={Artifact.Thumbnail} filename="thumbnail.jpeg" /> : null}</>;
};Copy
```

See the [Emitting Thumbnails](/docs/artifacts#emitting-thumbnails) page for more important information.

## Compatibility[​](#compatibility)

|  Browsers Environments
|  
Chrome 
Firefox 
Safari 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
No-op 
No-op

## See also[​](#see-also)

- [Emitting Artifacts](/docs/artifacts)

- [Source code for this component](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/Artifact.tsx)