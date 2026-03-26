# Add Prefix

`POST /accounts/{account_id}/addressing/prefixes`

Add a new prefix under the account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **asn** (integer, required): Autonomous System Number (ASN) the prefix will be advertised under.
- **cidr** (string, required): IP Prefix in Classless Inter-Domain Routing format.
- **delegate_loa_creation** (boolean, optional): Whether Cloudflare is allowed to generate the LOA document on behalf of the prefix owner.
- **description** (string, optional): Description of the prefix.
- **loa_document_id** (string, optional): Identifier for the uploaded LOA document.

## Response

### 201

Add Prefix response

- **result** (object, optional): 

### 4XX

Add Prefix response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
