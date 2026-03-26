# Update an Access application

`PUT /accounts/{account_id}/access/apps/{app_id}`

Updates an Access application.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

One of: Self Hosted Application, SaaS Application, Browser SSH Application, Browser VNC Application, App Launcher Application, Device Enrollment Permissions Application, Browser Isolation Permissions Application, Gateway Identity Proxy Endpoint Application, Bookmark application, Infrastructure application, Browser RDP Application, MCP Server Application, MCP Server Portal Application

## Response

### 200

Update an Access application response

- **result** (object, optional): 

### 4XX

Update an Access application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
