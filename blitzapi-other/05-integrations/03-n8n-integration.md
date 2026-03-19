> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# n8n Integration

> Automate your enrichment pipelines using the HTTP Request node in n8n.

**n8n** is the ideal orchestrator for complex BlitzAPI workflows. Its node-based architecture allows you to chain our **Waterfall Search**, **Enrichment**, and **CRM Sync** steps into a single autonomous agent.

## Standard Configuration

You will interact with BlitzAPI using the native **HTTP Request** node.

<Steps>
  <Step title="1. Create Credentials">
    To avoid copy-pasting your key in every node, create a reusable credential.

    1. Go to **Credentials** > **New** > Search for **"Header Auth"**.
    2. **Name**: `x-api-key`
    3. **Value**: `YOUR_BLITZ_API_KEY`
    4. Save as "BlitzAPI Production".
  </Step>

  <Step title="2. Configure the Node">
    Drag an **HTTP Request** node to your canvas.

    * **Method**: `POST`
    * **URL**: `https://api.blitz-api.ai/v2/search/waterfall-icp-keyword`
    * **Authentication**: Select `Generic Credential Type` -> `Header Auth`.
    * **Credential**: Select the "BlitzAPI Production" credential you just created.
  </Step>

  <Step title="3. Map the JSON Body">
    Set **Send Body** to `active` and **Body Content Type** to `JSON`.

    Use the **Expression Editor** to map your input data (e.g., `{{ $json.company_url }}`) into the JSON structure.
  </Step>
</Steps>

***

## ⚡ Handling Rate Limits (Crucial)

n8n executes workflows extremely fast. If you process 1,000 items without precautions, you will hit BlitzAPI's limit of **5 requests per second** immediately, causing `429` errors.

To scale safely, you must implement a **Throttling Pattern**.

### The "Split In Batches" Pattern

Do not connect the trigger directly to the HTTP Request. Use this structure:

1. **Split In Batches** Node:

* Set **Batch Size** to `1` (or `5` maximum).

2. **HTTP Request** (BlitzAPI):

* Connect it after the split.

3. **Wait** Node:

* Connect it after the HTTP Request.
* Set **Amount** to `200` milliseconds.

4. **Loop Back**:

* Connect the Wait node back to the input of the "Split In Batches" node.

<Info>
  **Why?** This forces n8n to process items sequentially (or in small groups) with a tiny pause, ensuring you never exceed the API throughput capacity.
</Info>

***

## Waterfall Recipes (Copy-Paste)

Here are optimized JSON payloads for common targeting scenarios.

### Scenario A: The Sales Leader

*Logic: Find the CRO or VP Sales. If not available, fallback to a Director level.*

```json  theme={null}
{
 "company_linkedin_url": "{{ $json.company_linkedin_url }}",
 "cascade": [
   {
     "include_title": ["Chief Revenue Officer", "CRO", "VP Sales"],
     "location": ["US", "GB"],
     "include_headline_search": false
   },
   {
     "include_title": ["Head of Sales", "Sales Director"],
     "location": ["US", "GB"],
     "include_headline_search": true
   }
 ],
 "max_results": 1
}
```

### Scenario B: The Marketing Decision Maker

*Logic: Prioritize the CMO globally. Fallback to VP or Head of Marketing.*

```json  theme={null}
{
 "company_linkedin_url": "{{ $json.company_linkedin_url }}",
 "cascade": [
   {
     "include_title": ["Chief Marketing Officer", "CMO"],
     "location": ["WORLD"],
     "include_headline_search": false
   },
   {
     "include_title": ["VP Marketing", "Head of Marketing"],
     "exclude_title": ["Assistant", "Intern"],
     "location": ["WORLD"],
     "include_headline_search": false
   }
 ],
 "max_results": 1
}
```

### Scenario C: The Founder (SMB Targeting)

*Logic: Find the Owner or CEO, specifically in France or Germany.*

```json  theme={null}
{
 "company_linkedin_url": "{{ $json.company_linkedin_url }}",
 "cascade": [
   {
     "include_title": ["Founder", "Co-Founder", "Owner"],
     "location": ["FR", "DE"],
     "include_headline_search": true
   },
   {
     "include_title": ["CEO", "PDG", "Gerant"],
     "location": ["FR", "DE"],
     "include_headline_search": false
   }
 ],
 "max_results": 1
}
```

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error: 'Data is not a valid JSON'">
    **Check Expression Mode.** In the Body parameter, ensure you are in **JSON mode** (not Form-Urlencoded). If using expressions like `{{ $json.id }}`, make sure they resolve to valid strings, not objects.
  </Accordion>

  <Accordion title="I see '[Array]' instead of data">
    **Check n8n Data Structure.** BlitzAPI returns a `results` array for searches. You might need to add an **"Item Lists"** node (operation: *Split Out Items*) after the HTTP Request to flatten the `results` array into separate n8n items.
  </Accordion>

  <Accordion title="Error 401 Unauthorized">
    **Check Credential Name.** In your "Header Auth" credential, the name of the header **must** be exactly `x-api-key`. If you named it `api-key` or `Authorization`, it will fail.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).