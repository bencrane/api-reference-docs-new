---
title: "getRegions()"
url: "https://www.remotion.dev/docs/lambda/getregions"
path: "/docs/lambda/getregions"
---

"---\nimage: /generated/articles-docs-lambda-getregions.png\nid: getregions\ntitle: getRegions()\ncrumb: 'Lambda API'\n---\n\nGets an array of all supported AWS regions of this release of Remotion Lambda.\n\n## Example\n\n```tsx twoslash\nimport {getRegions} from '@remotion/lambda';\n\n// ---cut---\n\nconst regions = getRegions();\n// [\"eu-central-1\", \"us-east-1\"]\n```\n\n## API\n\nThe function takes an optional object, with the following options:\n\n### `enabledByDefaultOnly`\n\n_available from v3.3.11_\n\nOnly return [the regions which are enabled by default](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in a new AWS account.\n\n## Return value\n\nAn array of supported regions by this release of Remotion Lambda.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-regions.ts)\n- [Region selection](/docs/lambda/region-selection)\n"

Gets an array of all supported AWS regions of this release of Remotion Lambda.

## Example[​](#example)

```

const regions = getRegions();
// ["eu-central-1", "us-east-1"]Copy
```

## API[​](#api)

The function takes an optional object, with the following options:

### `enabledByDefaultOnly`[​](#enabledbydefaultonly)

*available from v3.3.11*

Only return [the regions which are enabled by default](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in a new AWS account.

## Return value[​](#return-value)

An array of supported regions by this release of Remotion Lambda.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-regions.ts)

- [Region selection](/docs/lambda/region-selection)
](/docs/lambda/region-selection)](/docs/lambda/region-selection)
](/docs/lambda/region-selection)
- ](/docs/lambda/region-selection)
- ](/docs/lambda/region-selection)
- ](/docs/lambda/region-selection)
- ](/docs/lambda/region-selection)