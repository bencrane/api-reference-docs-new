# Inviting and Accepting Members

**URL:** https://docs.emailbison.com/workspaces/inviting-and-accepting-members

This workflow requires that the user has already registered on your EmailBison instance. If not, visit the Creating Users page to add them to your instance using the API. Existing users can be invited to any workspace using the API. Furthermore, their invitations can be programmatically accepted using the API.

**Inviting Members:**
If you are also going to be accepting invitations, you will use the ID given in the response of this API call. Send a POST request to `/api/workspaces/v1.1/invite-member`.

This request takes a JSON body with the following 2 required fields:
- **email** (string, required) - The email of the registered user.
- **role** (string, required) - A role for the user. One of admin, editor, client.

Example:
```
curl https://dedi.emailbison.com/api/workspaces/v1.1/invite-members \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "email": "example@example.com",
    "role": "admin"
  }'
```

**Accepting Invitations:**
You can use the API to accept invitations to workspaces on behalf of users. Send a POST request to `/api/workspaces/v1.1/accept/{team_invitation_id}` where {team_invitation_id} is the ID received back when inviting members. This request does not take a body.
