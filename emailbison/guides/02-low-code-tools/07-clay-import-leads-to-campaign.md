# Import Lead(s) to Campaign

**URL:** https://docs.emailbison.com/low-code-tools/clay/enrichments/import-leads-to-campaign

Add leads to specific EmailBison campaigns directly from your Clay table.

1. Add the Enrichment - In your Clay table, click + Add column, Select Enrichments, Search for and select "Import lead(s) to campaign"
2. Select Your Workspace - Choose your desired EmailBison account (workspace) from the dropdown. If you don't see your workspace, click + Add account and connect your workspace.
3. Map Required Fields - Under Setup Inputs, map the following required columns: Campaign ID, Lead ID(s)

**Finding Campaign IDs:** If you need to retrieve Campaign IDs, you can either: Go to an EmailBison campaign. Click Actions, Copy ID for API. -- or -- Click + Add column, select Enrichments, and search for HTTP API enrichment. Select Configure and authenticate through one of your connected accounts. Under Setup Inputs -> Method, select GET. Under Setup Inputs -> Endpoint, input: `https://subdomain.yourdomain.com/api/campaigns`. Save and run the enrichment to see your available campaigns.

4. Select Campaign and Leads - Select the Campaign ID from your available campaigns. For Lead ID(s), you have several options: Use the ID from the Create or Update Lead enrichment response; Use the ID from the Find Lead enrichment response; Use a GET request with leads endpoint; Supply a comma-separated list (e.g., "123,456,789") to add multiple leads at once. The Lead ID(s) data type must be changed from # to text, or you will get a runtime error.

5. Configure Parallel Sending - Toggle parallel sending on to import leads that are already in another campaign. By default, leads that are "in sequence" in other campaigns will be skipped. This includes leads in draft campaigns. Note that paused campaigns don't count for the parallel sending check, so leads can be added to other campaigns even with the toggle OFF.

6. Save and Run - Save the enrichment and run the column to import leads to your campaign. Set this column to auto-run if you need leads added or updated automatically when new data flows in.
