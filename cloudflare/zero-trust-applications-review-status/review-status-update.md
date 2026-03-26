# Update applications review statuses

`PUT /accounts/{account_id}/gateway/apps/review_status`

Update the statuses of your applications.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **approved_apps** (array, required): Contains the ids of the approved applications.
- **in_review_apps** (array, required): Contains the ids of the applications in review.
- **unapproved_apps** (array, required): Contains the ids of the unapproved applications.

## Response

### 200

Update applications review status response.

_Empty object_

### 4XX

Update applications review status failure response.

_Empty object_
