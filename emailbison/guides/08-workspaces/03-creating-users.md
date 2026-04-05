# Creating Users

**URL:** https://docs.emailbison.com/workspaces/creating-users

If a user (associated with an email account) has not registered yet for any of your workspaces on your EmailBison instance, you can programmatically register that email account using the API. If they have already registered, and you want to give them access to other workspaces using the API, visit the Inviting and Accepting Members page.

**Creating a User:**
Send a POST request to the following endpoint: `/api/workspaces/v1.1/users`

This request takes a JSON body with the following 4 fields:
- **name** (string, required) - A name for the user.
- **password** (string, required) - A password for the user.
- **email** (string, required) - The email address of the user.
- **role** (string, required) - A role for the user. One of admin, editor, client.

Example:
```
curl https://dedi.emailbison.com/api/workspaces/v1.1/users \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "name": "John Doe",
    "password": "securepasswordlol",
    "email": "example@example.com",
    "role": "admin"
  }'
```
