# Creating Workspaces

**URL:** https://docs.emailbison.com/workspaces/creating-workspaces

This workflow requires a super-admin key.

**Creating a Workspace:**
Send a POST request to `/api/workspaces/v1.1`. You must include a name field in a JSON body, this field is the name of the workspace you are creating.

Example:
```
curl https://dedi.emailbison.com/api/workspaces/v1.1 \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "name": "New name"
  }'
```
