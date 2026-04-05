# Creating Template Workspaces

**URL:** https://docs.emailbison.com/walkthroughs/creating-template-workspaces

This walkthrough will go over creating a workspace with the same base set-up each time. This is useful when you have common factors you re-create manually in every new workspace you create. For this walkthrough, the following manual steps are assumed to be done each time a workspace is created:
- Three users are invited (and they have to manually accept the invitations).
- Four custom tags are created.
- An API token is created.
- A webhook is created, with the same events listened to.

To automate all these steps, including accepting the invitations, start by making a new automation in your preferred tool. This automation will need a super-admin token for the first 2 requests, it is then able to switch to using the api-user token it created itself.

**General steps:**
1. The automation will make a POST request to create a workspace at this endpoint: `/api/workspaces/v1.1`
2. The automation will create an API token for this workspace by sending a POST request to this endpoint. The automation will use the team_id returned in the first request: `/api/workspaces/v1.1/{team_id}/api-tokens`
3. From this point, the super-admin key is no longer required, the automation will switch to using the api-user key just created and returned in the last response.
4. For each of the 3 users, the automation will invite them by sending a POST request to: `/api/workspaces/v1.1/invite-members`
5. The automation will then chain a POST request to this endpoint, using the team_invitation_id returned from the previous request: `/api/workspaces/v1.1/accept/{team_invitation_id}`
6. The automation will create the four tags on the workspace by sending a POST request to: `/api/tags`
7. The automation will create the webhook on the workspace by sending a POST request to: `/api/webhook-url`
8. The automation will have created the workspace with the desired set-up at this point.

(Also available as n8n-specific instructions in the tabbed view.)
