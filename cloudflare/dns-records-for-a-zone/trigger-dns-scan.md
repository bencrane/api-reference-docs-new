# Trigger DNS Record Scan

`POST /zones/{zone_id}/dns_records/scan/trigger`

Initiates an asynchronous scan for common DNS records on your domain. Note that this **does not** automatically add records to your zone. The scan runs in the background, and results can be reviewed later using the `/scan/review` endpoints. Useful if you haven't updated your nameservers yet.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Trigger DNS Records Scan Response

_Empty object_

### 4XX

Trigger DNS Records Scan response failure

_Empty object_
