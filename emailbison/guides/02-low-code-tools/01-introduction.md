# Low-Code Tools Introduction

**URL:** https://docs.emailbison.com/low-code-tools/introduction

Automations can be set-up using low-code / no-code tools. Tools such as n8n, Clay, Zapier, Make. Clay users have access to an official EmailBison integration with pre-built enrichments. See Clay - Overview to get started.

The interaction between these tools and EmailBison will be done through: Listening to the EmailBison Webhooks, and Making API requests.

**Translating API calls:**
There are general guidelines on translating the API calls found in these docs and in the API reference. Please consult the documentation for your specific tool to supplement this.

- **Authorization** -- A header with your request with a Authorization key and a Bearer {api_key} value. Automation tools usually have a method of saving these tokens to be used for multiple automations, instead of having to pass in a header in your automation requests.
- **HTTP Method** -- One of GET, DELETE, POST, PUT, PATCH. This needs to match the HTTP method found in these docs, or the API Reference.
- **Endpoint** -- This is the path to the endpoint you wish to use in your automation. Example: https://send.greenmarketing.com/api/leads
- **Query Parameters** -- Used for GET requests. The parameters are usually sent one by one in these tools with an entry for the name of the parameter, and the value. More info.
- **Body** -- This will be 1:1 with the examples provided in this documentation and the API reference.
