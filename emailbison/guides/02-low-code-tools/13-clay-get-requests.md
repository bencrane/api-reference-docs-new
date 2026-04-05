# Clay GET Requests (with examples)

**URL:** https://docs.emailbison.com/low-code-tools/clay/get-requests

This page covers using GET requests for all non-native actions, the majority of use cases can use the native EmailBison enrichments. This page will give step-by-step instructions on making a GET request from Clay to EmailBison. This example can be altered for different GET endpoints, the overall Clay enrichment will be almost identical.

For an example of a GET request, we will make a request to the leads endpoint: `/api/leads`. And we will pass in the following filters: search: john, filters: tag_ids = [11, 12], filters: replies = 0

Steps:
1. In your Clay table, add a new column. Select Add enrichment.
2. Search for and select HTTP API.
3. Authenticate through one of the methods listed above (select an account, or pass in an Authorization header). For this example, we will select an account from the dropdown.
4. Under Setup Inputs -> Method, select GET from the dropdown.
5. Under Setup Inputs -> Endpoint, input the leads endpoint: `https://subdomain.yourdomain.com/api/leads`
6. Under Setup Inputs -> Query Parameters, select Add a new Key and Value pair for each of the following steps:
   - Input `search` as the Key, and `john` as the Value.
   - Input `filters[replies][value]` as the Key, and `0` as the Value.
   - Input `filters[replies][criteria]` as the Key, and `=` as the Value.
   - Since Clay doesn't support duplicate keys, we need to pass an array with indexes, i.e. tag_ids[0] instead of tag_ids[]
   - Input `filters[tag_ids][0]` as the Key, and `11` as the Value.
   - Input `filters[tag_ids][1]` as the Key, and `12` as the Value.
7. Save the enrichment.

When this column runs, it will make a GET request to EmailBison fetching leads with these criteria. To use dynamic query parameters, use Clay's built-in / feature to pick data from previous columns.
