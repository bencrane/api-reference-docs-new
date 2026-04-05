# Clay POST Requests (with examples)

**URL:** https://docs.emailbison.com/low-code-tools/clay/post-requests

This page covers using POST requests for all non-native actions, the majority of use cases can use the native EmailBison enrichments. This page will give step-by-step instructions on making POST requests from Clay to EmailBison. These instructions can be slightly altered for different POST, PUT, and PATCH endpoints, the overall Clay enrichment will be the same. This page will provide the instructions to add leads to EmailBison, and then chain an API call to add the leads to a campaign.

**1. Adding a lead to EmailBison:**
For this example, we have a Clay table containing leads with the following columns: Email, First Name, Last Name, Company, Title, Notes, AI Enriched Paragraph, Linkedin URL.

Steps:
1. In your Clay table, add a new column. Select Add enrichment.
2. Search for and select HTTP API.
3. Authenticate through one of the methods listed above.
4. Under Setup Inputs -> Method, select POST from the dropdown.
5. Under Setup Inputs -> Endpoint, input the leads endpoint: `https://subdomain.yourdomain.com/api/leads`
6. For the body of the request in Setup Inputs -> Body, reference the API Reference to view the parameters this request takes. For example, for the first_name parameter, we will input / and find the First Name column in our Clay table. Repeat this step for all the columns in your Clay table. For any columns in the table that are not specifically named in the EmailBison request, we will use the custom_variables array. An example would be AI Enriched Paragraph or Linkedin URL.
7. Save the enrichment.

**2. Attaching a lead to an EmailBison campaign:**
These instructions will follow the previous instructions. We will also assume we have a Clay column that decides which campaign each lead will go to.

Steps:
1. In your Clay table, add a new column. Select Add enrichment.
2. Search for and select HTTP API.
3. Authenticate through one of the methods listed above.
4. Under Setup Inputs -> Method, select POST from the dropdown.
5. Under Setup Inputs -> Endpoint, input the attach leads to campaign endpoint: `https://subdomain.yourdomain.com/api/campaigns/{campaign_id}/leads/attach-leads`. Replace {campaign_id} with the ID of the EmailBison campaign you want these leads to be attached to. Alternatively, use the Clay / feature to use the Clay column that contains the campaign ID.
6. For the body of the request, reference the API Reference to view the parameters this request takes. Under Setup Inputs -> Body, input the JSON curly braces ({}), a key named lead_ids, and then square brackets ([]) to denote an array. For the value of the lead_ids array, input /, find the HTTP API enrichment that ran before this one, click on it, click on data, and then click on id. This is the ID EmailBison will use to identify this lead, and returns to you when you create a lead.
7. Save the enrichment.

After implementing these steps, every row (lead) in your Clay table will be added to EmailBison, and then attached to a campaign you choose after the enrichments run.
