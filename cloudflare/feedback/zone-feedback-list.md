# List zone feedback reports

`GET /zones/{zone_id}/bot_management/feedback`

Returns all feedback reports previously submitted for the specified zone. Feedback reports help improve detection by sharing samples of traffic that were misclassified as bots or humans.


## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List of feedback reports

Type: array

### 4XX

Feedback list failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
