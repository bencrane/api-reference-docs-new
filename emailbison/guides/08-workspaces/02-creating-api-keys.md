# Creating API Keys

**URL:** https://docs.emailbison.com/workspaces/creating-api-keys

This workflow requires a super-admin key. For a refresher on the difference between the key types, you can visit Authentication. You do not need to switch workspaces using the API or the UI for this workflow. api-user keys can be generated for workspaces using the API.

**Creating a Key (API):**
Send a POST request to the following endpoint: `/api/workspaces/v1.1/{workspace_id}/api-tokens`

- **workspace_id** (integer, required) - The ID of the workspace you want to generate a key for. Workspace IDs can be acquired by sending a GET request to `api/v1.1/workspaces`.

You must include a name field in a JSON body, this field is the name of the API key you are creating.

Example:
```
curl 'https://dedi.emailbison.com/api/workspaces/v1.1/54/api-tokens' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "name": "New token"
  }'
```

**Creating a Key (UI):** Navigate to Settings -> Developer API. Click the New API Token button near the top-right of the page. Provide a token name and token type. Click Generate Token.
