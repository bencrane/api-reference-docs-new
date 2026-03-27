---
title: "speculateServiceName()"
url: "https://www.remotion.dev/docs/cloudrun/speculateservicename"
path: "/docs/cloudrun/speculateservicename"
---

"---\nimage: /generated/articles-docs-cloudrun-speculateservicename.png\nid: speculateservicename\ntitle: speculateServiceName()\nslug: /cloudrun/speculateservicename\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nSpeculate the name of the Cloud Run service that will be created by [deployService()](/docs/cloudrun/deployservice) or its CLI equivalent, [`npx remotion cloudrun services deploy`](/docs/cloudrun/cli/services). This could be useful in cases when the configuration of the Cloud Run service is known in advance, and the name of the service is needed.\n\nIf you are not sure whether a service exists, use [`getServiceInfo()`](/docs/cloudrun/getserviceinfo) and catch the error that gets thrown if it does not exist.\n\nIf you want to get a list of deployed services, use [`getServices()`](/docs/cloudrun/getservices) instead.\n\n## Service name pattern\n\nThe service name depends on the following parameters:\n\n- Remotion version\n- Memory Limit\n- CPU Limit\n- Timeout in seconds\n\nThe name of the service resembles the following pattern:\n\n```\nremotion--3-3-96--mem2gi--cpu1-0--t-1900\n          ^^^^^^   ^^^     ^^^      ^^^\n            |       |       |        |-- Timeout in seconds\n            |       |       |----------- Cpu limit\n            |       |------------------- Memory limit\n            |--------------------------- Remotion version with dots replaced by dashes\n```\n\n## Example\n\n```ts twoslash\nimport {speculateServiceName} from '@remotion/cloudrun';\n\nconst speculatedServiceName = speculateServiceName({\n  memoryLimit: '2Gi',\n  cpuLimit: '2',\n  timeoutSeconds: 300,\n});\n\nconsole.log(speculatedServiceName); // remotion--3-3-96--mem2gi--cpu2-0--t-300\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `memoryLimit`\n\nThe upper bound on the amount of RAM that the Cloud Run service can consume.\n\n### `cpuLimit`\n\nThe maximum number of CPU cores that the Cloud Run service can use to process requests.\n\n### `timeoutSeconds`\n\nThe timeout that has been assigned to the Cloud Run service.\n\n## Return value\n\nA string with the speculated name of the service.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/speculate-service-name.ts)\n- [deployService()](/docs/cloudrun/deployservice)\n- CLI version of `deployService()`: [`npx remotion cloudrun services deploy`](/docs/cloudrun/cli/services/deploy)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Speculate the name of the Cloud Run service that will be created by [deployService()](/docs/cloudrun/deployservice) or its CLI equivalent, [`npx remotion cloudrun services deploy`](/docs/cloudrun/cli/services). This could be useful in cases when the configuration of the Cloud Run service is known in advance, and the name of the service is needed.

If you are not sure whether a service exists, use [`getServiceInfo()`](/docs/cloudrun/getserviceinfo) and catch the error that gets thrown if it does not exist.

If you want to get a list of deployed services, use [`getServices()`](/docs/cloudrun/getservices) instead.

## Service name pattern[​](#service-name-pattern)

The service name depends on the following parameters:

- Remotion version

- Memory Limit

- CPU Limit

- Timeout in seconds

The name of the service resembles the following pattern:

```
remotion--3-3-96--mem2gi--cpu1-0--t-1900
          ^^^^^^   ^^^     ^^^      ^^^
            |       |       |        |-- Timeout in seconds
            |       |       |----------- Cpu limit
            |       |------------------- Memory limit
            |--------------------------- Remotion version with dots replaced by dashesCopy
```

## Example[​](#example)

```
import {speculateServiceName} from '@remotion/cloudrun';

const speculatedServiceName = speculateServiceName({
  memoryLimit: '2Gi',
  cpuLimit: '2',
  timeoutSeconds: 300,
});

console.log(speculatedServiceName); // remotion--3-3-96--mem2gi--cpu2-0--t-300Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `memoryLimit`[​](#memorylimit)

The upper bound on the amount of RAM that the Cloud Run service can consume.

### `cpuLimit`[​](#cpulimit)

The maximum number of CPU cores that the Cloud Run service can use to process requests.

### `timeoutSeconds`[​](#timeoutseconds)

The timeout that has been assigned to the Cloud Run service.

## Return value[​](#return-value)

A string with the speculated name of the service.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/speculate-service-name.ts)

- [deployService()](/docs/cloudrun/deployservice)

- CLI version of `deployService()`: [`npx remotion cloudrun services deploy`](/docs/cloudrun/cli/services/deploy)
](/docs/cloudrun/cli/services/deploy)](/docs/cloudrun/cli/services/deploy)
](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)
- ](/docs/cloudrun/cli/services/deploy)