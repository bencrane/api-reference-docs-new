> Sources:
> - https://trigger.dev/docs/management/deployments/retrieve
> - https://trigger.dev/docs/management/deployments/get-latest
> - https://trigger.dev/docs/management/deployments/promote

# Deployments API

## Get deployment

v3-openapi GET /api/v1/deployments/{deploymentId}
Retrieve information about a specific deployment by its ID.

---

## Get latest deployment

v3-openapi GET /api/v1/deployments/latest
Retrieve information about the latest unmanaged deployment for the authenticated project.

---

## Promote deployment

v3-openapi POST /api/v1/deployments/{version}/promote
Promote a previously deployed version to be the current version for the environment. This makes the specified version active for new task runs.

---
