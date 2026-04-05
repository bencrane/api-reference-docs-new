# Creating Tags

**URL:** https://docs.emailbison.com/tags/creating-tags

Tags are a way for you to separate different leads/sender emails/campaigns into their own categories.

**API:**
Send a POST request to the following endpoint: `/api/tags`

There are 2 fields you can provide, name and default.
- **name** (string, required) - A name for the tag.
- **default** (boolean, default: "false", deprecated) - Whether this is a default tag.

Example:
```
curl https://dedi.emailbison.com/api/tags \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "name": "Important",
    "default": false
  }'
```

**UI:** Navigate to Settings -> Custom Tags. Click on Create custom tag, provide a name for your tag, click on Create custom tag.
