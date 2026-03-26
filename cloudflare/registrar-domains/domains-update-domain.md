# Update domain

`PUT /accounts/{account_id}/registrar/domains/{domain_name}`

Update individual domain.

## Parameters

- **domain_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **auto_renew** (boolean, optional): Auto-renew controls whether subscription is automatically renewed upon domain expiration.
- **locked** (boolean, optional): Shows whether a registrar lock is in place for a domain.
- **privacy** (boolean, optional): Privacy option controls redacting WHOIS information.

## Response

### 200

Update domain response

- **result** (object, optional): 

### 4XX

Update domain response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
