> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Make (Integromat) Integration

> Build powerful enrichment scenarios using the HTTP module in Make.

**Make** (formerly Integromat) allows you to integrate BlitzAPI into thousands of apps (Airtable, Hubspot, Google Sheets) visually.

Since BlitzAPI follows standard REST principles, you will use the generic **HTTP** app to interact with our endpoints.

## Standard Configuration

You will need the **HTTP** app > **Make a request** module.

<Steps>
  <Step title="1. Basic Settings">
    Create a new scenario and add the HTTP module.

    * **URL**: Paste your endpoint (e.g., `https://api.blitz-api.ai/v2/search/waterfall-icp-keyword`)
    * **Method**: `POST`
  </Step>

  <Step title="2. Authentication (Headers)">
    Do not use the "User name/Password" fields. Instead, add a generic Header.

    * **Item 1**:
      * **Name**: `x-api-key`
      * **Value**: `YOUR_BLITZ_API_KEY`
    * **Item 2** (Optional but recommended):
      * **Name**: `Content-Type`
      * **Value**: `application/json`
  </Step>

  <Step title="3. Body Configuration (Crucial)">
    Make offers a key-value interface, but for nested objects like our Waterfall Cascade, you must use **Raw** mode.

    * **Body type**: `Raw`
    * **Content type**: `JSON (application/json)`
    * **Request content**: Paste the JSON recipe below and map your variables (the colorful bubbles) inside the quote marks.
  </Step>
</Steps>

***

## ⚡ Handling Rate Limits

Make processes scenarios instantly. If you trigger a run with 500 rows from Google Sheets, Make will fire 500 requests in a split second, triggering a `429 Too Many Requests` error from BlitzAPI.

To fix this, you must slow down the execution loop.

### The "Sleep" Tool Solution

1. Click on the **Tools** icon (Purple wrench) at the bottom of your screen.
2. Select **Sleep**.
3. Place this module **immediately after** your HTTP module.
4. Set **Delay** to `1` second.

<Info>
  **Result**: Make will wait 1 second between each operation, keeping you safely under the 5 requests/second limit.
</Info>

***

## JSON Recipes (Raw Body)

Copy these payloads into the **"Request content"** field of your HTTP module. *`Note: Replace {{1.company_url}} with your actual mapped variable from previous modules.`*

### Scenario A: The Sales Leader

*Logic: Find the CRO or VP Sales. If not available, fallback to a Director level.*

```json  theme={null}
{
 "company_linkedin_url": "{{1.company_linkedin_url}}",
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

Logic: Prioritize the CMO globally. Fallback to VP or Head of Marketing.

```json  theme={null}
{
 "company_linkedin_url": "{{1.company_linkedin_url}}",
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

### Scenario C: Enrich Email

Target: Convert a Profile URL to a Verified Email.

Endpoint: `POST https://api.blitz-api.ai/v2/enrichment/email`

```json  theme={null}
{
 "person_linkedin_url": "{{1.person_linkedin_url}}"
}
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error 400: Bad Request">
    Check your Quotes. In Make's editor, it's easy to accidentally delete a quote mark " when dragging and dropping a variable bubble. Ensure your JSON syntax is valid.
  </Accordion>

  <Accordion title="Parse Error / JSON invalid">
    Check Content Type. Ensure you explicitly selected JSON (application/json) in the Content type dropdown of the HTTP module. If you leave it blank, the API might not interpret the body correctly.
  </Accordion>

  <Accordion title="How to extract the email from the response?">
    Parse the JSON. The HTTP module returns a raw JSON string/buffer. To use the data in the next step (e.g., update HubSpot), you must place a JSON > Parse JSON module after the HTTP request to convert the string back into mapped variables.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).