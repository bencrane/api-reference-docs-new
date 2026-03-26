# Prepare for Migration

Set up your RudderStack account and environment before diving into the migration process.

* * *

  * __less than a minute

  * 


It is essential to set up your RudderStack account and environment before diving into the migration process. This guide details the prerequisites for migration.

## Migration prerequisites

  1. [Sign up](<https://app.rudderstack.com/signup>) for a RudderStack Cloud account.
  2. You will be prompted to create a new workspace. Give your workspace a name and select the appropriate region.
  3. Once your workspace is created, click **Add Source** in the default **Connections** tab.

[![Add source](/docs/images/get-started/quickstart/add-source.webp)](</docs/images/get-started/quickstart/add-source.webp>)

  4. From the list of available sources, select the type of source you want to set up (for example, JavaScript, iOS (Obj-C), Android (Java), Node.js).
  5. After selecting your source, you will be provided with a write key and a [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>). These credentials are essential for initializing the RudderStack SDK in your application. Make sure to copy and store them securely.


> ![warning](/docs/images/warning.svg)
> 
> Before proceeding with the migration, it’s crucial to consider any existing Segment code snippets or libraries from your application to avoid data duplication. Search your codebase for any references to `analytics.js` or `segment.io` and document them.

With your RudderStack account set up and your environment prepared, you’re now ready to migrate existing Segment events, update your SDK implementations, and start sending data to RudderStack.

## Next steps

  * [Migrate Events from Segment](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/migrate-segment-events/>)