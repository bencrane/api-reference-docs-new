# Update Logpush job

`PUT /zones/{zone_id}/logpush/jobs/{job_id}`

Updates a Logpush job.

## Parameters

- **job_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **destination_conf** (string, optional): Uniquely identifies a resource (such as an s3 bucket) where data. will be pushed. Additional configuration parameters supported by the destination may be included.
- **enabled** (boolean, optional): Flag that indicates if the job is enabled.
- **filter** (string, optional): The filters to select the events to include and/or remove from your logs. For more information, refer to [Filters](https://developers.cloudflare.com/logs/reference/filters/).
- **frequency** (string, optional): This field is deprecated. Please use `max_upload_*` parameters instead. . The frequency at which Cloudflare sends batches of logs to your destination. Setting frequency to high sends your logs in larger quantities of smaller files. Setting frequency to low sends logs in smaller quantities of larger files. Values: `high`, `low`
- **kind** (string, optional): The kind parameter (optional) is used to differentiate between Logpush and Edge Log Delivery jobs (when supported by the dataset). Values: ``, `edge`
- **logpull_options** (string, optional): This field is deprecated. Use `output_options` instead. Configuration string. It specifies things like requested fields and timestamp formats. If migrating from the logpull api, copy the url (full url or just the query string) of your call here, and logpush will keep on making this call for you, setting start and end times appropriately.
- **max_upload_bytes** (integer, optional): The maximum uncompressed file size of a batch of logs. This setting value must be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size.
- **max_upload_interval_seconds** (integer, optional): The maximum interval in seconds for log batches. This setting must be between 30 and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify a minimum interval for log batches; this means that log files may be sent in shorter intervals than this.
- **max_upload_records** (integer, optional): The maximum number of log lines per batch. This setting must be between 1000 and 1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this.
- **name** (string, optional): Optional human readable job name. Not unique. Cloudflare suggests. that you set this to a meaningful string, like the domain name, to make it easier to identify your job.
- **output_options** (object, optional): The structured replacement for `logpull_options`. When including this field, the `logpull_option` field will be ignored.
- **ownership_challenge** (string, optional): Ownership challenge token to prove destination ownership.

## Response

### 200

Update Logpush job response.

- **result** (object, optional): 

### 4XX

Update Logpush job response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
