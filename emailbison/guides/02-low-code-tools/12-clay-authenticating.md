# Clay Authenticating Requests

**URL:** https://docs.emailbison.com/low-code-tools/clay/authenticating-requests

This page covers authentication for non-native requests using the HTTP API enrichment. If you're using native EmailBison enrichments, authentication is handled automatically through your connected workspace accounts. Requests to EmailBison need to be authenticated with an API Key. You can either send a header with an Authorization key each time you add a new HTTP API enrichment, or you can save this header to your accounts so you can select it from a dropdown.

**Saving the headers to your accounts:**
1. In your Clay HTTP API enrichment, scroll down to Account.
2. Click + Add Account.
3. Put in a friendly name, such as EmailBison Workspace A
4. Click Add a new Key and Value pair.
5. In the Key field, input Authorization.
6. In the Value field, input Bearer YOUR_API_KEY (the word Bearer, a space, and your API Key).
7. Click Save.
You can now select this account from the Accounts dropdown for any future columns you add to your Clay workspace.

**Manually authorizing each request:**
1. In your Clay HTTP API enrichment, scroll down to Headers.
2. Click Add a new Key and Value pair.
3. In the Key field, input Authorization.
4. In the Value field, input Bearer YOUR_API_KEY (the word Bearer, a space, and your API Key).

Once you've familiarized yourself with how to authenticate your requests using Clay, visit Clay - GET Requests and Clay - POST Requests for instructions that will apply to the majority of API requests to EmailBison.
