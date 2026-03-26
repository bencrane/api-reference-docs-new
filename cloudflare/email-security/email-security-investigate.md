# Search email messages

`GET /accounts/{account_id}/email-security/investigate`

Returns information for each email that matches the search parameter(s).
If the search takes too long, the endpoint returns 202 with a Location header
pointing to a polling endpoint where results can be retrieved once ready.

## Parameters

- **account_id** (string, required) [path]: 
- **start** (string, optional) [query]: The beginning of the search date range.
Defaults to `now - 30 days` if not provided.
- **end** (string, optional) [query]: The end of the search date range.
Defaults to `now` if not provided.
- **query** (string, optional) [query]: The space-delimited term used in the query. The search is case-insensitive.

The content of the following email metadata fields are searched:
* alert_id
* CC
* From (envelope_from)
* From Name
* final_disposition
* md5 hash (of any attachment)
* sha1 hash (of any attachment)
* sha256 hash (of any attachment)
* name (of any attachment)
* Reason
* Received DateTime (yyyy-mm-ddThh:mm:ss)
* Sent DateTime (yyyy-mm-ddThh:mm:ss)
* ReplyTo
* To (envelope_to)
* To Name
* Message-ID
* smtp_helo_server_ip
* smtp_previous_hop_ip
* x_originating_ip
* Subject
- **detections_only** (boolean, optional) [query]: Determines if the search results will include detections or not.
- **action_log** (boolean, optional) [query]: Determines if the message action log is included in the response.
- **final_disposition** (string, optional) [query]: The dispositions the search filters by.
- **metric** (string, optional) [query]: 
- **message_action** (string, optional) [query]: The message actions the search filters by.
- **recipient** (string, optional) [query]: Filter by recipient. Matches either an email address or a domain.
- **sender** (string, optional) [query]: Filter by sender. Matches either an email address or a domain.
- **alert_id** (string, optional) [query]: 
- **domain** (string, optional) [query]: Filter by a domain found in the email: sender domain, recipient domain, or a domain in a link.
- **message_id** (string, optional) [query]: 
- **subject** (string, optional) [query]: Search for messages containing individual keywords in any order within the subject.
- **exact_subject** (string, optional) [query]: Search for messages with an exact subject match.
- **submissions** (boolean, optional) [query]: Search for submissions instead of original messages
- **cursor** (string, optional) [query]: 
- **per_page** (integer, optional) [query]: The number of results per page.
- **page** (integer, optional) [query]: Deprecated: Use cursor pagination instead.

## Response

### 200

Contains the search results for the provided query.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (array, optional): 
- **result_info** (object, optional): 

### 202

The search is taking longer than expected. Use the Location header to poll for results.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): 
- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

Client Error

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
