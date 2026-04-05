# Create or Update Lead

**URL:** https://docs.emailbison.com/low-code-tools/clay/enrichments/create-or-update-lead

Add new leads or update existing leads in your EmailBison workspace directly from your Clay table.

1. Add the Enrichment - In your Clay table, click + Add column, Select Enrichments, Search for and select "Create or update lead"
2. Select Your Workspace - Choose your desired EmailBison account (workspace) from the dropdown. If you don't see your workspace, click + Add account and connect your workspace.
3. Map Your Data - Under Setup Inputs, map the required columns: First Name (required), Last Name (required), Email (required). All other fields are optional. If you are adding a custom variable, it must already exist in EmailBison. Follow the steps below to create a custom variable if needed.

**Creating a Custom Variable:** If you need to create a custom variable before running the Create or Update Lead enrichment: Click + Add column, select Enrichments, and search for HTTP API enrichment. Select Configure and authenticate through one of your connected accounts. Under Setup Inputs -> Method, select POST. Under Setup Inputs -> Endpoint, input: `https://subdomain.yourdomain.com/api/custom-variables`. In Setup Inputs -> Body, input: `{"name": "New Name"}` where "New Name" is the value of your new custom variable name.

4. Configure Update Behavior - Under Setup Input -> Select existing lead behaviour, you have two options:
   - **PUT (Full Replacement)** - Replaces the entire lead with only the fields you send. Any fields you don't include will be removed.
   - **PATCH (Partial Update)** - Updates only the specific fields you send. All other fields remain unchanged.

PUT Example: If you send `{"first_name": "Alex", "email": "alex@new.com"}` and the existing lead has `{"first_name": "Alex", "email": "alex@example.com", "phone": "123-4567"}`, Result: The lead is replaced with only the fields you sent. The phone field is removed because it wasn't included.

PATCH Example: If you send `{"email": "alex@new.com"}` and the existing lead has `{"first_name": "Alex", "email": "alex@example.com", "phone": "123-4567"}`, Result: Only the email is updated to alex@new.com. The first_name and phone fields remain unchanged.

5. Save and Run - After you've filled out all the required fields, save and add the enrichment as a column in your table. Run it to create or update leads in your workspace. Set this column to auto-run if you need your leads to be added or updated whenever new data flows into your table.
