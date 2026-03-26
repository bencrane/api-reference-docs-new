# Creates a new tag

`POST /accounts/{account_id}/cloudforce-one/events/tags/create`

Creates a new tag to be used accross threat events.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **activeDuration** (string, optional): 
- **actorCategory** (string, optional): 
- **aliasGroupNames** (array, optional): 
- **aliasGroupNamesInternal** (array, optional): 
- **analyticPriority** (number, optional): 
- **attributionConfidence** (string, optional): 
- **attributionOrganization** (string, optional): 
- **categoryUuid** (string, optional): 
- **externalReferenceLinks** (array, optional): 
- **internalDescription** (string, optional): 
- **motive** (string, optional): 
- **opsecLevel** (string, optional): 
- **originCountryISO** (string, optional): 
- **priority** (number, optional): 
- **sophisticationLevel** (string, optional): 
- **value** (string, required): 

## Response

### 200

Returns the created tag.

- **activeDuration** (string): 
- **actorCategory** (string): 
- **aliasGroupNames** (array): 
- **aliasGroupNamesInternal** (array): 
- **analyticPriority** (number): 
- **attributionConfidence** (string): 
- **attributionOrganization** (string): 
- **categoryName** (string): 
- **categoryUuid** (string): 
- **externalReferenceLinks** (array): 
- **internalDescription** (string): 
- **motive** (string): 
- **opsecLevel** (string): 
- **originCountryISO** (string): 
- **priority** (number): 
- **sophisticationLevel** (string): 
- **uuid** (string): 
- **value** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): 

### 404

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
