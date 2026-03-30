> Sources:
> - https://trigger.dev/docs/management/envvars/list
> - https://trigger.dev/docs/management/envvars/create
> - https://trigger.dev/docs/management/envvars/retrieve
> - https://trigger.dev/docs/management/envvars/update
> - https://trigger.dev/docs/management/envvars/delete
> - https://trigger.dev/docs/management/envvars/import

# Environment Variables API

## List Env Vars

v3-openapi GET /api/v1/projects/{projectRef}/envvars/{env}
List all environment variables for a specific project and environment.

---

## Create Env Var

v3-openapi POST /api/v1/projects/{projectRef}/envvars/{env}
Create a new environment variable for a specific project and environment.

---

## Retrieve Env Var

v3-openapi GET /api/v1/projects/{projectRef}/envvars/{env}/{name}
Retrieve a specific environment variable for a specific project and environment.

---

## Update Env Var

v3-openapi PUT /api/v1/projects/{projectRef}/envvars/{env}/{name}
Update a specific environment variable for a specific project and environment.

---

## Delete Env Var

v3-openapi DELETE /api/v1/projects/{projectRef}/envvars/{env}/{name}
Delete a specific environment variable for a specific project and environment.

---

## Import Env Vars

v3-openapi POST /api/v1/projects/{projectRef}/envvars/{env}/import
Upload mulitple environment variables for a specific project and environment.

---
