---
title: "getRegions()"
url: "https://www.remotion.dev/docs/cloudrun/getregions"
path: "/docs/cloudrun/getregions"
---

"---\nimage: /generated/articles-docs-cloudrun-getregions.png\nid: getregions\ntitle: getRegions()\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nGets an array of all supported GCP regions of this release of Remotion Cloud Run.\n\n## Example\n\n```tsx twoslash\nimport {getRegions} from '@remotion/cloudrun/client';\n\n// ---cut---\n\nconst regions = getRegions();\n// [\"asia-east1\", \"us-east1\"]\n```\n\n:::note\nImport from [`@remotion/cloudrun/client`](/docs/cloudrun/light-client) to not import the whole renderer, which cannot be bundled.\n:::\n\n## Return value\n\nAn array of supported regions by this release of Remotion Cloud Run.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/get-regions.ts)\n- [Region selection](/docs/cloudrun/region-selection)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Gets an array of all supported GCP regions of this release of Remotion Cloud Run.

## Example[​](#example)

```

const regions = getRegions();
// ["asia-east1", "us-east1"]Copy
```

](#example)](#example)
](#example)
- ](#example)
- ](#example)