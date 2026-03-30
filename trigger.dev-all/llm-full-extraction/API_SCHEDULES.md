> Sources:
> - https://trigger.dev/docs/management/schedules/list
> - https://trigger.dev/docs/management/schedules/create
> - https://trigger.dev/docs/management/schedules/retrieve
> - https://trigger.dev/docs/management/schedules/update
> - https://trigger.dev/docs/management/schedules/delete
> - https://trigger.dev/docs/management/schedules/deactivate
> - https://trigger.dev/docs/management/schedules/activate
> - https://trigger.dev/docs/management/schedules/timezones

# Schedules API

## List Schedules

v3-openapi GET /api/v1/schedules
List all schedules. You can also paginate the results.

---

## Create Schedule

v3-openapi POST /api/v1/schedules
Create a new `IMPERATIVE` schedule based on the specified options.

---

## Retrieve Schedule

v3-openapi GET /api/v1/schedules/{schedule_id}
Get a schedule by its ID.

---

## Update Schedule

v3-openapi PUT /api/v1/schedules/{schedule_id}
Update a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.

---

## Delete Schedule

v3-openapi DELETE /api/v1/schedules/{schedule_id}
Delete a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.

---

## Deactivate Schedule

v3-openapi POST /api/v1/schedules/{schedule_id}/deactivate
Deactivate a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.

---

## Activate Schedule

v3-openapi POST /api/v1/schedules/{schedule_id}/activate
Activate a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.

---

## Get timezones

v3-openapi GET /api/v1/timezones
Get all supported timezones that schedule tasks support.

---
