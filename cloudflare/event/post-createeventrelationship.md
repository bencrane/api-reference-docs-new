# Create a relationship between two events

`POST /accounts/{account_id}/cloudforce-one/events/relationships/create`

Creates a directed relationship between two events. The relationship is from parent to child with a specified type.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **childIds** (array, required): Array of UUIDs for child events. Single child = 1:1 relationship, multiple = 1:many relationships
- **datasetId** (string, required): Dataset identifier where the events are stored
- **parentId** (string, required): UUID of the parent event that will be the source of the relationship
- **relationshipType** (string, required): Type of relationship to create between parent and child events Values: `related_to`, `caused_by`, `attributed_to`

## Response

### 200

Relationship created successfully

- **childIds** (array): Array of child event UUIDs that were processed
- **errors** (array): Array of errors for relationships that failed to be created (only present if some relationships failed)
- **message** (string): Human-readable message describing the operation result
- **relationships** (array): Array of successfully created relationship objects
- **relationshipsCreated** (number): Number of relationships that were successfully created
- **success** (boolean): Whether the relationship creation operation completed successfully

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
