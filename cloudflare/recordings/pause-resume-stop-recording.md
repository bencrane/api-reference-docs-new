# Pause/Resume/Stop recording

`PUT /accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}`

Pause/Resume/Stop a given recording ID.

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: A Cloudflare-generated unique identifier for an item.
- **recording_id** (string, required) [path]: ID of the recording

## Request Body

- **action** (string, required):  Values: `stop`, `pause`, `resume`

## Response

### 200

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation
