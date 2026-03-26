# Stop full PCAP

`PUT /accounts/{account_id}/pcaps/{pcap_id}/stop`

Stop full PCAP.

## Parameters

- **pcap_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 204

Stop full PCAP response.

### default

Stop full PCAP response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
