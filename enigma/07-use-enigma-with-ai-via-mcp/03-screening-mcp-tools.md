# Screening MCP Tools​

URL: https://documentation.enigma.com/guides/ai-mcp/screening-tools

Beta
The Enigma remote MCP server is currently in beta.

The Enigma MCP server provides tools for sanctions screening and compliance workflows. These tools enable your AI to screen individuals and businesses against global sanctions lists including OFAC SDN, EU sanctions, UN sanctions, and other watchlists, as well as manage screening decisions.

For API-level documentation, see the [Screening API Reference](/screening/api) .

## Screening Tools Overview

| Tool | Purpose | Key Inputs 
| `screen_customer` | Screen individuals against sanctions lists | Name (required), DOB, Country 
| `screen_business` | Screen organizations against sanctions lists | Organization name (required), Country, Address, BIC 
| `screen_entity_search` | Look up details for a specific sanctioned entity | Entity ID (required) 
| `find_decision` | Retrieve a single screening decision | Request ID (required) 
| `find_decisions` | Query multiple screening decisions with filters | Date range, Status, Alert, Assignee 
| `update_decision` | Update a decision's status, assignee, or notes | Request ID (required), User ID (required) 

## screen_customer

Screen an individual against sanctions lists for compliance and due diligence.

Use this tool to check individuals against global sanctions lists including OFAC SDN, EU sanctions, UN sanctions, and other watchlists. Do not use this tool for companies or organizations—use `screen_business` instead.

### Parameters

| Parameter | Type | Required | Description 
| `name` | string | Yes | The person's full name (e.g., "John Hanafin") 
| `dob` | string | No | Date of birth in YYYYMMDD format (e.g., "19740710" for July 10, 1974). Recommended for more precise results. 
| `country` | string | No | Country of affiliation, full name capitalized (e.g., "Ireland", "United States"). Recommended for more precise results. 
| `passport_number` | string | No | Government-issued passport number 
| `passport_country` | string | No | Country of passport issuance 
| `tag` | string | No | Custom tag to associate with this screening request 
| `list_groups` | array/string | No | List groups to screen against. Defaults to `["pos/sdn/all", "pos/non_sdn/all"]` 

### Available List Groups

- `pos/sdn/all` - OFAC Specially Designated Nationals
- `pos/non_sdn/all` - OFAC Non-SDN Lists
- `enigma/rogues` - Enigma curated rogues list
- `enigma/testing` - Testing list

### Returns

Sanctions screening results including:

- Match confidence scores
- List of potential matches with details
- Hit/alert status based on configured thresholds
- Source list information (SDN, Non-SDN, etc.)

### Example Prompts

> "Screen John Hanafin, born July 10, 1974, from Ireland against OFAC sanctions lists"

> "Check if Maria Garcia with passport number AB123456 from Spain appears on any sanctions lists"

## screen_business

Screen a business or organization against sanctions lists for compliance.

Use this tool to check organizations against global sanctions lists including OFAC SDN, EU sanctions, UN sanctions, and other watchlists.

### Parameters

| Parameter | Type | Required | Description 
| `org_name` | string | Yes | The organization name to screen 
| `country_of_affiliation` | string | No | Country associated with the organization 
| `address` | string | No | Address string for the organization 
| `bic` | string | No | Bank Identifier Code (triggers separate search if provided) 
| `tag` | string | No | Custom tag to associate with this screening request 
| `list_groups` | array/string | No | List groups to screen against. Defaults to `["pos/sdn/all", "pos/non_sdn/all"]` 

### Returns

Sanctions screening results including:

- Match confidence scores
- List of potential matches with details
- Hit/alert status based on configured thresholds
- Source list information (SDN, Non-SDN, etc.)

### Example Prompts

> "Screen Banco de Bogota from Colombia against sanctions lists"

> "Check if Acme Trading LLC at 123 Main Street, Tehran is on any OFAC lists"

## screen_entity_search

Look up detailed information about a specific sanctioned entity by its ID.

Use this tool when you have an entity ID from a previous screening result and want to retrieve the full entity profile with all available attributes.

### Parameters

| Parameter | Type | Required | Description 
| `entity_id` | string | Yes | The sanctioned entity ID (e.g., "ofac/sdn/43085") 
| `format` | string | No | Response format: `raw` , `display` , `structured` , or `attributes` . Defaults to `structured` . 

### Response Formats

- **raw** - The raw API response as a JSON object
- **display** - HTML-formatted display of the entity
- **structured** - Structured JSON response (default)
- **attributes** - Entity attributes as a JSON object

### Example Prompts

> "Get the full details for sanctioned entity ofac/sdn/43085"

> "Show me all attributes for entity ofac/non_sdn/12345"

## Enabling Decision Recording

To use the decision management tools ( `find_decision` , `find_decisions` , `update_decision` ), you must enable case management in your screening configuration. Without this, screening requests will not create decision records.

Include `"general": {"use_case_manager": true}` in the `configuration_overrides` of your screening requests:

```json
{
  "configuration_overrides": {
    "general": {
      "use_case_manager": true
    }
  }
}
```

Once enabled, every screening request will automatically create a decision record. The `request_id` returned in the screening response can then be used to retrieve or update the decision.

## find_decision

Retrieve a single screening decision by its request ID.

Decisions are created when screening requests are processed with case management enabled (see Enabling Decision Recording above). Use this tool to look up the current status and details of a specific screening decision.

### Parameters

| Parameter | Type | Required | Description 
| `request_id` | string | Yes | The UUID of the screening request (e.g., "32cb66d1-a86c-4f19-9c4b-70c5e12aa7fb") 

### Returns

Decision details including:

- Request ID and timestamp
- Alert status
- Current status (e.g., pending, approved, rejected)
- Assignee information
- Associated tags and notes

### Example Prompts

> "Find the decision for screening request 32cb66d1-a86c-4f19-9c4b-70c5e12aa7fb"

> "What's the status of decision fed01a4a-da7e-11ee-8600-0a58a9feac02?"

## find_decisions

Query multiple screening decisions with optional filters.

Use this tool to search and paginate through screening decisions. Results are returned in database ID order, oldest to newest.

### Parameters

| Parameter | Type | Required | Description 
| `from_date` | string | No | Start datetime in `YYYY-MM-DDTHH:MM:SS` format (UTC). Defaults to 30 days ago. 
| `to_date` | string | No | End datetime in `YYYY-MM-DDTHH:MM:SS` format (UTC). Defaults to end of current year. 
| `page` | integer | No | Page number (0-indexed) 
| `amt` | integer | No | Results per page (default: 100) 
| `alert` | boolean | No | Filter by alert status. Omit to return all results. 
| `status` | string | No | Filter by status (e.g., "pending", "approved", "rejected", "in_progress", "on_hold", "cancelled") 
| `assignee_id` | string | No | Filter by assigned user ID 
| `tag` | string | No | Filter by request tag 

### Returns

Paginated list of decisions with:

- Request IDs and timestamps
- Alert and status information
- Assignee details
- Associated tags

### Example Prompts

> "Show me all screening decisions from the last week that triggered alerts"

> "Find all pending decisions assigned to user 8b738bc8-dac1-11f0-90ac-9af3bc73d0e6"

> "Get the first 50 rejected decisions from October 2025"

## update_decision

Update a screening decision's status, assignee, or add notes.

Use this tool to manage the workflow for screening decisions—assign reviewers, update statuses, and add notes as part of the review process.

### Parameters

| Parameter | Type | Required | Description 
| `request_id` | string | Yes | The UUID of the decision to update 
| `user_id` | string | Yes | The database ID of the user making the update 
| `assignee_id` | string | No | New assignee's user ID 
| `status` | string | No | New status string (e.g., "approved", "rejected", "pending", "in_progress", "on_hold") 
| `note` | string | No | Note to add to the decision 

### Returns

Updated decision details confirming the changes.

### Example Prompts

> "Approve decision 32cb66d1-a86c-4f19-9c4b-70c5e12aa7fb and add a note that it was reviewed and cleared"

> "Assign decision fed01a4a-da7e-11ee-8600-0a58a9feac02 to user test2 and set status to in_progress"

> "Add a note to decision abc123 saying 'Pending additional documentation from customer'"

## Workflow Examples

### Basic Customer Screening

```text
User: "Screen Maria Rodriguez, DOB March 15, 1985, from Mexico against OFAC lists"

AI uses: screen_customer(name="Maria Rodriguez", dob="19850315", country="Mexico")
```

### Business Due Diligence

```text
User: "Check if Global Trade Partners LLC in Dubai appears on any sanctions lists"

AI uses: screen_business(org_name="Global Trade Partners LLC", country_of_affiliation="United Arab Emirates", address="Dubai")
```

### Decision Review Workflow

```text
User: "Show me all screening alerts from last week that need review"

AI uses: find_decisions(from_date="2025-01-20T00:00:00", to_date="2025-01-27T23:59:59", alert=true, status="pending")

User: "Approve the first decision and mark it as a false positive"

AI uses: update_decision(request_id="...", user_id="...", status="approved", note="Reviewed - false positive, name similarity only")
```

### Entity Investigation

```text
User: "One of our screenings matched entity ofac/sdn/43085. Show me the full details."

AI uses: screen_entity_search(entity_id="ofac/sdn/43085", format="structured")
```

## Related Resources

- [Screening Endpoint API Guide](/screening/api) - Full API documentation
- [Screening Console Guide](/screening/console-guide) - Console-based screening guide
- [MCP Tools](/guides/ai-mcp/tools) - All available Enigma MCP tools