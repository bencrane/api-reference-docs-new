---
title: "deleteService()"
url: "https://www.remotion.dev/docs/cloudrun/deleteservice"
path: "/docs/cloudrun/deleteservice"
---

"---\nimage: /generated/articles-docs-cloudrun-deleteservice.png\nid: deleteservice\ntitle: deleteService()\nslug: /cloudrun/deleteservice\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nDeletes a deployed Cloud Run service based on its name.\n\nTo retrieve a list of services, call [`getServices()`](/docs/cloudrun/getservices) first.\n\n## Example\n\n```ts twoslash\nimport {deleteService, getServices} from '@remotion/cloudrun';\n\nconst services = await getServices({\n  region: 'us-east1',\n  compatibleOnly: false,\n});\nfor (const service of services) {\n  await deleteService({\n    region: 'us-east1',\n    serviceName: service.serviceName,\n  });\n}\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [GCP region](/docs/cloudrun/region-selection) to which the service was deployed to.\n\n### `serviceName`\n\nThe name of the service to be deleted.\n\n## Return value\n\nNothing. If the deletion failed, the service rejects with an error.\n\n## See also\n\n- [Source code for this service](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/delete-service.ts)\n- [deployService()](/docs/cloudrun/deployservice)\n- [getServices()](/docs/cloudrun/getservices)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Deletes a deployed Cloud Run service based on its name.

To retrieve a list of services, call [`getServices()`](/docs/cloudrun/getservices) first.

## Example[​](#example)

```
import {deleteService, getServices} from '@remotion/cloudrun';

const services = await getServices({
  region: 'us-east1',
  compatibleOnly: false,
});
for (const service of services) {
  await deleteService({
    region: 'us-east1',
    serviceName: service.serviceName,
  });
}Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [GCP region](/docs/cloudrun/region-selection) to which the service was deployed to.

### `serviceName`[​](#servicename)

The name of the service to be deleted.

## Return value[​](#return-value)

Nothing. If the deletion failed, the service rejects with an error.

## See also[​](#see-also)

- [Source code for this service](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/delete-service.ts)

- [deployService()](/docs/cloudrun/deployservice)

- [getServices()](/docs/cloudrun/getservices)
](/docs/cloudrun/getservices)](/docs/cloudrun/getservices)
](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)