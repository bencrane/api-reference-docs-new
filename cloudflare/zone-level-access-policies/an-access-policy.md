# Create an Access policy

`POST /zones/{zone_id}/access/apps/{app_id}/policies`

Create a new Access policy for an application.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **approval_groups** (array, optional): Administrators who can approve a temporary authentication request.
- **approval_required** (boolean, optional): Requires the user to request access from an administrator at the start of each session.
- **decision** (string, required): The action Access will take if a user matches this policy. Values: `allow`, `deny`, `non_identity`, `bypass`
- **exclude** (array, optional): Rules evaluated with a NOT logical operator. To match the policy, a user cannot meet any of the Exclude rules.
- **include** (array, required): Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.
- **isolation_required** (boolean, optional): Require this application to be served in an isolated browser for users matching this policy.
- **name** (string, required): The name of the Access policy.
- **precedence** (integer, optional): The order of execution for this policy. Must be unique for each policy.
- **purpose_justification_prompt** (string, optional): A custom message that will appear on the purpose justification screen.
- **purpose_justification_required** (boolean, optional): Require users to enter a justification when they log in to the application.
- **require** (array, optional): Rules evaluated with an AND logical operator. To match the policy, a user must meet all of the Require rules.

## Response

### 201

Create an Access policy response

_Empty object_

### 4XX

Create an Access policy response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
