# Updates an event

`POST /accounts/{account_id}/cloudforce-one/events/{event_id}`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **event_id** (string, required) [path]: Event UUID.

## Request Body

- **attacker** (string, optional): 
- **attackerCountry** (string, optional): 
- **category** (string, optional): 
- **createdAt** (string, optional): 
- **datasetId** (string, required): Dataset ID containing the event to update.
- **date** (string, optional): 
- **event** (string, optional): 
- **indicator** (string, optional): 
- **indicatorType** (string, optional): 
- **insight** (string, optional): 
- **raw** (object, optional): 
- **targetCountry** (string, optional): 
- **targetIndustry** (string, optional): 
- **tlp** (string, optional): 

## Response

### 200

Returns the updated event.

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

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
