# Create a new app

`POST /accounts/{account_id}/calls/apps`

Creates a new Cloudflare calls app. An app is an unique enviroment where each Session can access all Tracks within the app.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): A short description of Calls app, not shown to end users.

## Response

### 201

Created a new app

- **result** (object, optional):
