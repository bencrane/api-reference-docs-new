# Connecting Modal to your Datadog account

You can use the Modal + Datadog Integration to export Modal function logs to Datadog. You’ll find the Modal Datadog Integration available for install in the Datadog marketplace.

What this integration does 

This integration allows you to:

Export Modal audit logs in Datadog
Export Modal function logs to Datadog
Export container metrics to Datadog
Installing the integration 
Open the Modal Tile (or the EU tile here) in the Datadog integrations page
Click “Install Integration”
Click Connect Accounts to begin authorization of this integration. You will be redirected to log into Modal, and once logged in, you’ll be redirected to the Datadog authorization page.
Click “Authorize” to complete the integration setup
Metrics 

The Modal Datadog Integration will forward the following metrics to Datadog:

modal.cpu.utilization
modal.memory.usage
modal.gpu.memory.usage
modal.gpu.compute.utilization
modal.container.running
modal.input_events.elapsed_time_us
modal.input_events.input_queue_time_us
modal.input_events.coldstart_time_us
modal.input_events.successes
modal.input_events.total_inputs
modal.function.pending_inputs
modal.function.running_inputs

All metrics are tagged with container_id, environment_name, app_name, app_id, function_name, function_id, workspace_name, and workspace_id.

Deprecated metrics:

modal.memory.utilization (use modal.memory.usage)
modal.gpu.memory.utilization (use modal.gpu.memory.usage)

modal.input_events.successes and modal.input_events.total_inputs can be used to measure the success rate of a certain function or app.

As an official Datadog integration, Modal metrics are free on Datadog while logs are charged.

Structured logging 

Logs from Modal are sent to Datadog in plaintext without any structured parsing. This means that if you have custom log formats, you’ll need to set up a log processing pipeline in Datadog to parse them.

Modal passes log messages in the .message field of the log record. To parse logs, you should operate over this field. Note that the Modal Integration does set up some basic pipelines. In order for your pipelines to work, ensure that your pipelines come before Modal’s pipelines in your log settings.

Cost Savings 

The Modal Datadog Integration will forward all logs to Datadog which could be costly for verbose apps. We recommend using either Log Pipelines or Index Exclusion Filters to filter logs before they are sent to Datadog.

The Modal Integration tags all logs with the environment attribute. The simplest way to filter logs is to create a pipeline that filters on this attribute and to isolate verbose apps in a separate environment.

Uninstalling the integration 

Once the integration is uninstalled, all logs will stop being sent to Datadog, and authorization will be revoked.

Navigate to the Modal metrics settings page and select “Delete Datadog Integration”.
On the Configure tab in the Modal integration tile in Datadog, click Uninstall Integration.
Confirm that you want to uninstall the integration.
Ensure that all API keys associated with this integration have been disabled by searching for the integration name on the API Keys page.
