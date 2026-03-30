# Deactivate Schedule


v3-openapi POST /api/v1/schedules/{schedule_id}/deactivate
Deactivate a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.
