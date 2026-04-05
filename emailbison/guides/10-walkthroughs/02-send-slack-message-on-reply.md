# Send Slack Message on Campaign Reply

**URL:** https://docs.emailbison.com/walkthroughs/send-slack-message-on-reply

This walkthrough will go over sending a Slack message every time you get a campaign reply on a workspace. Although this workspace is specific to campaign replies, it can be easily altered for different events such as when an untracked reply is received, when a sender email disconnects etc. by listening to different webhook events.

**n8n steps:**
1. **Create n8n Workspace** - Navigate to https://n8n.io. In a workspace, click the + to add a new node.
2. **Create Webhook Node** - Search for Webhook and click on it. Set the HTTP Method in the webhook to POST. Copy the Test URL to put into EmailBison later.
3. **Create Slack Node** - Add a new node for slack by clicking on the + again. Search for "Slack", click on it, then search for "Send a message", click on it. On the Credential to connect with input field, click Create new credential, make sure it is on OAuth2, click Connect my account. Proceed with the Slack login, close the pop-up after it says Account Connected. Fill out the input fields with the desired channel you want the updates sent to.
4. **Create EmailBison Webhook** - In EmailBison, navigate to Settings -> Webhooks -> New Webhook URL. Give a name for your webhook and paste the n8n Test URL you copied earlier into the input field. Toggle on Contact Replied and click Subscribe to webhooks.
5. **Send a Test Event** - Navigate back to your n8n workbook. Double-click on the Webhook node, click Listen for test event. Navigate to the webhook you created on EmailBison, click on Send test webhook, select Contact replied as the webhook event, click Send test event.
6. **Extract Data from Webhook** - To extract the data you want from the webhook, Double-click on your Slack node in your n8n workbook. On the Message Text field, switch it from fixed to expression. Drag and Drop the desired fields from the input tab on the left-hand side. Click on Test step on the top of the page, you should receive a Slack message with the details you chose.
7. **Switch to Production URL** - In your n8n workbook, double click the Webhook node. Under Webhook URLs, switch the button from Test URL to Production URL, copy this URL. Navigate to EmailBison -> Settings -> Webhooks. Click edit on the Webhook you just created, replace the Webhook URL with the production URL you just copied. You should now receive a Slack message on every campaign reply in that workspace.

