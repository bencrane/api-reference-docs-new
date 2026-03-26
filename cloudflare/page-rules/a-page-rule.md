# Create a Page Rule

`POST /zones/{zone_id}/pagerules`

Creates a new Page Rule.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **actions** (array, required): The set of actions to perform if the targets of this rule match the
request. Actions can redirect to another URL or override settings, but
not both.

- **priority** (integer, optional): The priority of the rule, used to define which Page Rule is processed
over another. A higher number indicates a higher priority. For example,
if you have a catch-all Page Rule (rule A: `/images/*`) but want a more
specific Page Rule to take precedence (rule B: `/images/special/*`),
specify a higher priority for rule B so it overrides rule A.

- **status** (string, optional): The status of the Page Rule. Values: `active`, `disabled`
- **targets** (array, required): The rule targets to evaluate on each request.

## Response

### 200

Create a Page Rule response

- **result** (object, optional): 

### 4XX

Create a Page Rule response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
