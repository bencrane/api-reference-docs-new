# Clay Workspace Setup

**URL:** https://docs.emailbison.com/low-code-tools/clay/workspace-setup

Before using the official EmailBison integration in Clay, you'll need to connect your EmailBison workspace(s). In order to access each workspace's data (to push or pull data), you will need to create an api-user key for each workspace and connect them one by one in Clay. There are two ways to connect your workspace:

**Method 1: From Clay Settings:**
1. Access Clay Settings - Go to Clay settings and navigate to the Connections tab.
2. Add EmailBison Connection - Click + Add connection and search for EmailBison.
3. Enter Workspace Details - Input the following: Connection name - Your workspace name; Workspace domain (Instance URL) - Your workspace domain (this will always be your instance URL); API Key - Your user-api key (see API Key)
4. Save - Click Save. You can now select this workspace from the Account dropdown for any EmailBison enrichment.
5. Adding Multiple Workspaces - Repeat these steps for each workspace you want to connect to Clay. Each workspace requires its own api-user key.

**Method 2: From Within an Enrichment:**
1. Access EmailBison Enrichments - Click on Actions, or click + Add column then Add enrichment. Search emailbison and select any of the enrichments.
2. Add Your Workspace Account - Under Account, click + Add account.
3. Enter Workspace Details - Input the following: Connection name - Your workspace name; Workspace domain (Instance URL) - Your workspace domain (this will always be your instance URL); API Key - Your user-api key (see API Key)
4. Save - Click Save. You can now select this workspace from the Account dropdown for any EmailBison enrichment.
5. Adding Multiple Workspaces - Repeat these steps for each workspace you want to connect to Clay. Each workspace requires its own api-user key.

Once you've connected your workspace(s), browse the available enrichments to start integrating EmailBison with your Clay tables.
