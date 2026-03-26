# Submit a feedback report

`POST /zones/{zone_id}/bot_management/feedback`

Submit a feedback report for the specified zone. Use `type` to indicate whether the report is a false positive (good traffic flagged as bot) or a false negative (bot traffic missed). Furthermore, you can also use `expression` as a wirefilter to identify the affected traffic sample.

See more accepted API fields and expression types at https://developers.cloudflare.com/bots/concepts/feedback-loop/#api-fields and https://developers.cloudflare.com/bots/concepts/feedback-loop/#expression-fields, respectively.


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **created_at** (string, optional): 
- **description** (string, required): 
- **expression** (string, required): Wirefilter expression describing the traffic being reported.
- **first_request_seen_at** (string, required): 
- **last_request_seen_at** (string, required): 
- **requests** (integer, required): 
- **requests_by_attribute** (object, required): Top attributes contributing to the feedback sample. Keys include topASNs, topCountries, topHosts, topIPs, topJA3Hashes, topJA4s, topPaths, topUserAgents.
- **requests_by_score** (object, required): Map of bot scores (1-99) to request counts. Sum must equal `requests`.
- **requests_by_score_src** (object, required): Map of score source to request counts. Sum must equal `requests`.
- **subtype** (string, optional): 
- **type** (string, required): Type of feedback report. Values: `false_positive`, `false_negative`

## Response

### 201

Feedback report created

### 4XX

Feedback creation failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
