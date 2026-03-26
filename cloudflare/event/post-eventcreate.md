# Creates a new event

`POST /accounts/{account_id}/cloudforce-one/events/create`

To create a dataset, see the [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/) endpoint. When `datasetId` parameter is unspecified, it will be created in a default dataset named `Cloudforce One Threat Events`.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **accountId** (number, optional): 
- **attacker** (string, optional): 
- **attackerCountry** (string, optional): 
- **category** (string, required): 
- **datasetId** (string, optional): 
- **date** (string, required): 
- **event** (string, required): 
- **indicator** (string, optional): 
- **indicatorType** (string, optional): 
- **indicators** (array, optional): Array of indicators for this event. Supports multiple indicators per event for complex scenarios.
- **insight** (string, optional): 
- **raw** (object, required): 
- **tags** (array, optional): 
- **targetCountry** (string, optional): 
- **targetIndustry** (string, optional): 
- **tlp** (string, required): 

## Response

### 200

Returns the created event.

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
