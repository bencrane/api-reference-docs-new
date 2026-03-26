# Reads an event

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/events/{event_id}`

Retrieves a specific event by its UUID.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.
- **event_id** (string, required) [path]: Event UUID.

## Response

### 200

Returns the event.

- **attacker** (string): 
- **attackerCountry** (string): 
- **category** (string): 
- **datasetId** (string): 
- **date** (string): 
- **event** (string): 
- **hasChildren** (boolean): 
- **indicator** (string): 
- **indicatorType** (string): 
- **indicatorTypeId** (number): 
- **insight** (string): 
- **killChain** (number): 
- **mitreAttack** (array): 
- **mitreCapec** (array): 
- **numReferenced** (number): 
- **numReferences** (number): 
- **rawId** (string): 
- **referenced** (array): 
- **referencedIds** (array): 
- **references** (array): 
- **referencesIds** (array): 
- **releasabilityId** (string): 
- **tags** (array): 
- **targetCountry** (string): 
- **targetIndustry** (string): 
- **tlp** (string): 
- **uuid** (string): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
