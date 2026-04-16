# Team Management

> https://documentation.enigma.com/console/team-management

Manage organizational access and permissions through Enigma Console's role-based system.

## Roles and Permissions

Three role levels control user capabilities:

| Capability | Owner | Admin | Member |
|---|---|---|---|
| View and search business data | Yes | Yes | Yes |
| Use API | Yes | Yes | Yes |
| Export lists | Yes | Yes | Yes |
| Invite members | Yes | Yes | — |
| Remove members | Yes | Yes | — |
| Change member roles | Yes | Yes | — |
| Configure SSO | Yes | Yes | — |
| Transfer ownership | Yes | — | — |

**Note:** "Each organization has exactly one Owner. The Owner role cannot be assigned through the role dropdown."

## View Team Members

Navigate to **Settings > Access > Users** to see all members and pending invitations.

## Invite a Team Member

1. Go to **Settings > Access > Users**
2. Click **Invite Users**
3. Enter email address(es)
4. Click **Confirm**

Invitees receive email instructions. New users join as Members by default and can be promoted to Admin afterward.

## Change a Member's Role

1. Navigate to **Settings > Access > Users**
2. Locate the user
3. Use the **Role** column dropdown
4. Select new role

Changes apply immediately. Only Admin or Member roles can be assigned via Console.

## Remove a Team Member

1. Go to **Settings > Access > Users**
2. Find the user
3. Click the three-dot actions menu
4. Select **Delete User**
5. Confirm

**Warning:** "Removing a member revokes their access immediately. They can no longer sign in to the Console or use API keys."

## Transfer Organization Ownership

Only current Owners can transfer ownership:

1. Navigate to **Settings > Access > Users**
2. Find the new Owner
3. Click the three-dot actions menu
4. Select **Transfer Ownership**
5. Confirm transfer

**Warning:** Transfer cannot be undone. The previous owner becomes Admin.

## Revoke a Pending Invitation

1. Go to **Settings > Access > Users**
2. Locate the pending invitation (marked "Invited")
3. Click the three-dot actions menu
4. Select **Delete Invite**
5. Confirm

The invitation link becomes invalid.
