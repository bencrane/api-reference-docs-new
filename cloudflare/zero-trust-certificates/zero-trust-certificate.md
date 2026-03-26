# Create Zero Trust certificate

`POST /accounts/{account_id}/gateway/certificates`

Create a new Zero Trust certificate.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **validity_period_days** (integer, optional): Sets the certificate validity period in days (range: 1-10,950 days / ~30 years). Defaults to 1,825 days (5 years). **Important**: This field is only settable during the certificate creation.  Certificates becomes immutable after creation - use the `/activate` and `/deactivate` endpoints to manage certificate lifecycle.

## Response

### 200

Creates Zero Trust certificate response.

_Empty object_

### 4XX

Creates Zero Trust certificate response failure.

_Empty object_
