# Create a zone ruleset

`POST /zones/{zone_id}/rulesets`

Creates a ruleset at the zone level.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An informative description of the ruleset.
- **id** (object, optional): 
- **last_updated** (string, optional): The timestamp of when the ruleset was last modified.
- **name** (string, optional): The human-readable name of the ruleset.
- **version** (object, optional): 
- **kind** (string, optional): The kind of the ruleset. Values: `managed`, `custom`, `root`, `zone`
- **phase** (string, optional): The phase of the ruleset. Values: `ddos_l4`, `ddos_l7`, `http_config_settings`, `http_custom_errors`, `http_log_custom_fields`, `http_ratelimit`, `http_request_cache_settings`, `http_request_dynamic_redirect`, `http_request_firewall_custom`, `http_request_firewall_managed`, `http_request_late_transform`, `http_request_origin`, `http_request_redirect`, `http_request_sanitize`, `http_request_sbfm`, `http_request_transform`, `http_response_cache_settings`, `http_response_compression`, `http_response_firewall_managed`, `http_response_headers_transform`, `magic_transit`, `magic_transit_ids_managed`, `magic_transit_managed`, `magic_transit_ratelimit`
- **rules** (array, optional): The list of rules in the ruleset.

## Response

### 200

A ruleset response.

- **errors** (enum, optional):  Values: ``
- **messages** (array, optional): A list of warning messages.
- **result** (object, optional): 
- **success** (enum, optional):  Values: `true`

### 4XX

A failure response.

- **errors** (array, optional): A list of error messages.
- **messages** (array, optional): A list of warning messages.
- **result** (enum, optional):  Values: ``
- **success** (enum, optional):  Values: `false`
