---
title: "getInputProps()"
url: "https://www.remotion.dev/docs/get-input-props"
path: "/docs/get-input-props"
---

"---\nimage: /generated/articles-docs-get-input-props.png\ntitle: getInputProps()\nid: get-input-props\ncrumb: 'API'\n---\n\n<AvailableFrom v=\"2.0\" />\n\nUsing this method, you can retrieve inputs that you pass in from the command line using [`--props`](/docs/cli), or the [`inputProps`](/docs/ssr) parameter if you are using the Node.JS APIs ([`renderMedia()`](/docs/renderer/render-media), [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda)).\n\nThis method is useful if you want to retrieve the input props in the [root component](/docs/terminology/root-file).\n\nThis method is not available when inside a [`<Player>`](/docs/player) or [when client-side rendering](/docs/miscellaneous/render-in-browser). Instead, get the props as React props from the component you passed as the `component` prop to the player.\n\n## You might not need this API\n\nPrefer the following ways of getting your input props:\n\n- A component that was rendered as a [composition](/docs/composition) will retrieve the input props as regular props.\n- In the [root component](/docs/terminology/root-file), you can get the input props by using the [`calculateMetadata()`](/docs/calculate-metadata) function.\n\nIn both cases, you can type the props, which is better than using this API which returns a non-typesafe object.\n\n## API\n\nPass in a [parseable](/docs/cli) JSON representation using the `--props` flag to either `remotion studio` or `remotion render`:\n\n```bash\nnpx remotion render --props='{\"hello\": \"world\"}'\n```\n\nTo simulate how it behaves, you can also pass props when using the Remotion Studio:\n\n```bash\nnpx remotion studio --props='{\"hello\": \"world\"}'\n```\n\nYou may also specify a file containing JSON and Remotion will parse the file for you:\n\n```bash\nnpx remotion render --props=./path/to/props.json\n```\n\nYou can then access the props anywhere in your Remotion project:\n\n```tsx twoslash {3}\nimport {Composition} from 'remotion';\nconst getInputProps = () => ({hello: 'world'}) as const;\nconst MyComp: React.FC = () => null;\nconst config = {\n  component: MyComp,\n  durationInFrames: 100,\n  fps: 30,\n  width: 1000,\n  height: 1000,\n  id: 'MyComp',\n} as const;\n// ---cut---\n\nexport const Root: React.FC = () => {\n  const {hello} = getInputProps(); // \"world\"\n\n  return <Composition {...config} />;\n};\n```\n\nIn this example, the props also get passed to the component of the composition with the id `my-composition`.\n\n## Compatibility\n\n<CompatibilityTable chrome firefox safari nodejs={'No-op, returns {}'} bun={'No-op, returns {}'} serverlessFunctions={'No-op, returns {}'} clientSideRendering={'No-op, returns {}'} serverSideRendering player={'No-op, returns {}'} studio />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/config/input-props.ts)\n- [Dynamic duration, FPS & dimensions](/docs/dynamic-metadata)\n"
[v2.0](https://github.com/remotion-dev/remotion/releases/v2.0)

Using this method, you can retrieve inputs that you pass in from the command line using [`--props`](/docs/cli), or the [`inputProps`](/docs/ssr) parameter if you are using the Node.JS APIs ([`renderMedia()`](/docs/renderer/render-media), [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda)).

This method is useful if you want to retrieve the input props in the [root component](/docs/terminology/root-file).

This method is not available when inside a [`<Player>`](/docs/player) or [when client-side rendering](/docs/miscellaneous/render-in-browser). Instead, get the props as React props from the component you passed as the `component` prop to the player.

## You might not need this API[​](#you-might-not-need-this-api)

Prefer the following ways of getting your input props:

- A component that was rendered as a [composition](/docs/composition) will retrieve the input props as regular props.

- In the [root component](/docs/terminology/root-file), you can get the input props by using the [`calculateMetadata()`](/docs/calculate-metadata) function.

In both cases, you can type the props, which is better than using this API which returns a non-typesafe object.

## API[​](#api)

Pass in a [parseable](/docs/cli) JSON representation using the `--props` flag to either `remotion studio` or `remotion render`:

```
npx remotion render --props='{"hello": "world"}'Copy
```

To simulate how it behaves, you can also pass props when using the Remotion Studio:

```
npx remotion studio --props='{"hello": "world"}'Copy
```

You may also specify a file containing JSON and Remotion will parse the file for you:

```
npx remotion render --props=./path/to/props.jsonCopy
```

You can then access the props anywhere in your Remotion project:

```

export const Root: React.FC = () => {
  const {hello} = getInputProps(); // "world"

  return <Composition {...config} />;
};Copy
```

In this example, the props also get passed to the component of the composition with the id `my-composition`.

## Compatibility[​](#compatibility)

|  Browsers Servers Environments
|  
Chrome 
Firefox 
Safari 
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
No-op, returns {} 
No-op, returns {} 
No-op, returns {} 
No-op, returns {} 
 
No-op, returns {} 

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/core/src/config/input-props.ts)

- [Dynamic duration, FPS & dimensions](/docs/dynamic-metadata)
](/docs/dynamic-metadata)](/docs/dynamic-metadata)
](/docs/dynamic-metadata)
- ](/docs/dynamic-metadata)
- ](/docs/dynamic-metadata)
- ](/docs/dynamic-metadata)