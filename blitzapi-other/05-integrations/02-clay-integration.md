> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Clay Integration

> Enrich thousands of leads using the Clay HTTP API (Sculptor or Manual).

**Clay** is the ultimate partner for BlitzAPI. By combining our **Unlimited Data** with Clay's spreadsheet interface, you can build massive enrichment waterfalls without writing a single line of code.

## 🚀 The "Sculptor" Method (Fastest)

Clay's new **Sculptor** feature allows you to setup the integration simply by copy-pasting our documentation.

<Steps>
  <Step title="1. Copy the Request">
    Go to our [API Reference](/api-reference) or [Quickstart](/guide/getting-started/quickstart) and copy any **cURL** command.

    *Example:*

    ```bash  theme={null}
    curl -X POST "https://api.blitz-api.ai/v2/search/waterfall-icp-keyword"\
         -H "Content-Type: application/json"\
         -H "x-api-key: YOUR_KEY"\
         -d '{ "company_linkedin_url": "..." }'
    ```
  </Step>

  <Step title="2. Paste into Clay">
    In your Clay table:

    1. Click **Add Enrichment** > **HTTP API**.
    2. Look for the **"Paste cURL"** or **"Sculptor"** button.
    3. Paste the code.
  </Step>

  <Step title="3. AI Mapping">
    Clay's AI will automatically detect the `company_linkedin_url` (or other parameters) in the code and ask you which column in your table matches that data.

    Simply select the correct column, and you are ready to run!
  </Step>
</Steps>

***

## ⚙️ Manual Setup (Standard)

If you prefer to configure the HTTP node manually, follow these settings.

1. **Method**: `POST`
2. **URL**: `https://api.blitz-api.ai/v2/search/waterfall-icp-keyword` (or other endpoint)
3. **Headers**:

* `content-type`: `application/json`
* `x-api-key`: `YOUR_API_KEY`

4. **Body**:

```json  theme={null}
{
 "company_linkedin_url": "https://www.linkedin.com/company/wttj-fr",
 "cascade": [
   {
     "include_title": ["HRD", "Human Director"],
     "exclude_title": ["assistant", "intern", "product", "junior"],
     "location": ["US", "CA"],
     "include_headline_search": false
   },
   {
     "include_title": ["HRD", "Human Director"],
     "exclude_title": ["junior", "assistant", "intern", "hacker"],
     "location": ["WORLD"],
     "include_headline_search": false
   },
   {
     "include_title": ["HR", "Human resources "],
     "exclude_title": ["junior", "assistant", "intern", "UX", "UI", "Design"],
     "location": ["US", "CA"],
     "include_headline_search": false
   },
   {
     "include_title": ["HR", "Human resources"],
     "exclude_title": ["junior", "assistant", "intern", "product"],
     "location": ["US", "CA"],
     "include_headline_search": true
   },
   {
     "include_title": ["Talent", "Staff", "Office"],
     "exclude_title": ["junior", "assistant", "intern"],
     "location": ["WORLD"],
     "include_headline_search": false
   }
 ],
 "max_results": 10
}
```

***

## 🛑 Critical: Rate Limiting

To respect BlitzAPI's throughput and ensure stability, you **must** configure the rate limit settings in Clay. We allow 5 requests per second.

In the HTTP Enrichment settings, go to **Rate Limit** and set exactly:

| Setting          | Value       |
| :--------------- | :---------- |
| **Max Requests** | **5**       |
| **Time Period**  | **1000** ms |

<Warning>
  **Strict Requirement**: Failure to set this limit to `1000ms` will result in `429 Too Many Requests` errors during bulk runs.
</Warning>

***

## Popular Clay Payloads

Copy-paste these JSON bodies directly into your integration.

### 1. Waterfall Search (Find Decision Maker)

*Target: Find Marketing Decision Maker.*

```json  theme={null}
{
 "company_linkedin_url": "https://www.linkedin.com/company/wttj-fr",
 "cascade": [
   {
     "include_title": ["Marketing Director", "Head Marketing", "Chief Marketing Officer"],
     "exclude_title": ["assistant", "intern", "product", "junior"],
     "location": ["WORLD"],
     "include_headline_search": false
   },
   {
     "include_title": ["Marketing Manager", "Head Growth", "Growth manager"],
     "exclude_title": ["junior", "assistant", "intern", "hacker"],
     "location": ["WORLD"],
     "include_headline_search": false
   },
   {
     "include_title": ["Communication Director", "Brand Director", "Content Director"],
     "exclude_title": ["junior", "assistant", "intern", "UX", "UI", "Design"],
     "location": ["WORLD"],
     "include_headline_search": false
   },
   {
     "include_title": ["Communication", "marketing", "growth", "brand"],
     "exclude_title": ["junior", "assistant", "intern", "product"],
     "location": ["US", "CA"],
     "include_headline_search": true
   },
   {
     "include_title": ["CEO", "founder", "cofounder", "owner", "General Director"],
     "exclude_title": ["junior", "assistant", "intern"],
     "location": ["WORLD"],
     "include_headline_search": false
   }
 ],
 "max_results": 10
}
```

### 2. Enrich Email (Find Work Email)

*Target: Get verified email from a Profile URL.*

```json  theme={null}
{
 "person_linkedin_url": "{{Linkedin Profile Column}}"
}
```

***

## Mapping the Output

Once the request runs successfully:

1. Hover over the `results` cell in Clay.
2. Click **"Add to Table"**.
3. Select the fields you need (e.g., `email`, `phone`, `person_linkedin_url`).

<Tip>
  Always map the `icp` field. It tells you which tier of your cascade was matched (`1` = Top Priority / Tier 1), helping you score and route your leads instantly.
</Tip>


Built with [Mintlify](https://mintlify.com).