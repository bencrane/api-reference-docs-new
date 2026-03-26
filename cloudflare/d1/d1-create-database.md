# Create D1 Database

`POST /accounts/{account_id}/d1/database`

Returns the created D1 database.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **jurisdiction** (string, optional): Specify the location to restrict the D1 database to run and store data. If this option is present, the location hint is ignored. Values: `eu`, `fedramp`
- **name** (string, required): D1 database name.
- **primary_location_hint** (string, optional): Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as possible to the current user. Values: `wnam`, `enam`, `weur`, `eeur`, `apac`, `oc`

## Response

### 200

Returns the created D1 database's metadata

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): The details of the D1 database.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Database details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
