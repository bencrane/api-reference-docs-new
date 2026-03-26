# Connect Reverse ETL Source to HubSpot

Configure a Reverse ETL source with your HubSpot destination.

* * *

  * __4 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the HubSpot destination. It also takes you through the required scopes, predefined identifiers, and creating the association between the object records.

The below steps assume that you have already [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and [configured the connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/setup-guide/#connection-settings>).

> ![success](/docs/images/tick.svg)
> 
> You can connect multiple Reverse ETL sources to the HubSpot destination.

## Required scopes

If you’re connecting a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) source to HubSpot that uses [private app access token](<https://developers.hubspot.com/docs/api/intro-to-auth#private-app-access-tokens>) for authentication, make sure your access token has the following scopes:
    
    
    crm.lists.read
    crm.objects.contacts.read
    crm.objects.contacts.write
    crm.schemas.custom.read
    crm.objects.custom.read
    crm.objects.custom.write
    crm.schemas.custom.write
    crm.objects.companies.write
    crm.schemas.contacts.read
    crm.lists.write
    crm.objects.companies.read
    crm.objects.deals.read
    crm.objects.deals.write
    crm.schemas.companies.read
    crm.schemas.companies.write
    crm.schemas.contacts.write
    crm.schemas.deals.read
    crm.schemas.deals.write
    crm.objects.owners.read
    crm.objects.quotes.write
    crm.objects.quotes.read
    crm.schemas.quotes.read
    crm.objects.line_items.read
    crm.objects.line_items.write
    crm.schemas.line_items.read
    

See the [HubSpot documentation](<https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#create-a-new-private-app>) for more information on adding the above scopes.

## Data mapping

Follow these steps to define the data mapping settings:

  1. From the dropdown, select the HubSpot **Object** where you want to sync the data.
  2. Select the object to associate with the above data.
  3. Specify the required association from the dropdown.
  4. Specify the **Sync mode**. This integration only supports **Upsert** mode currently.
  5. Optionally, toggle on the **Use cursor column** setting for your incremental sync. Then, select the required column from the dropdown. See [Cursor Column Support](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/cursor-column-support/#use-the-cursor-column-feature>) for more information on this feature.
  6. Under **Choose identifier** , select the warehouse column that acts as a unique identifier to map your records. Then, select the corresponding HubSpot field from the dropdown.


  1. Click the **Map with JSON** button.
  2. Specify the **Sync mode**. This integration only supports **Upsert** mode currently.
  3. Optionally, toggle on the **Use cursor column** setting for your incremental sync. Then, select the required column from the dropdown. See [Cursor Column Support](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/cursor-column-support/#use-the-cursor-column-feature>) for more information on this feature.
  4. Choose the **Event Type** \- RudderStack supports sending data to HubSpot as **Identify** and **Track** events.
  5. If you select **Track** , you can optionally toggle on the **Lookup event name by column** setting and select the required warehouse column. RudderStack uses this column to perform the lookup. If this setting is not toggled on, specify the event name to be used for lookup.
  6. Choose the user identifiers (**user_id** and **anonymous_id**) from the dropdown.


## Predefined identifiers

While connecting a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) source with HubSpot using [Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>), choose a warehouse column and HubSpot field to map your records in the [Choose identifier](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/#choosing-the-identifier>) section:

[![HubSpot connection settings](/docs/images/event-stream-destinations/hubspot-data-mapping-settings.webp)](</docs/images/event-stream-destinations/hubspot-data-mapping-settings.webp>)

If you select a standard HubSpot **Object** , the **Destination fields** dropdown displays the predefined unique identifiers along with any other unique field of the object.

The following table lists the predefined identifiers corresponding to the standard HubSpot objects:

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * These fields are visible only when the **Create associations between object records** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/setup-guide/#new-api-settings>) is toggled off.
>   * The values of unique identifiers are case-sensitive and should be sent exactly as they are present in HubSpot.
> 


Standard HubSpot object| Predefined unique identifiers  
---|---  
Company| Company Domain Name  
Contact| Email  
Deal| Deal Name  
Line Item| Name  
Quote| Quote number  
  
If you select a custom HubSpot **Object** , only the unique fields of the object are displayed in the **Destination fields** dropdown.

## Create association between object records

Note that:

  * You can create an association between the HubSpot object records while connecting your HubSpot destination to a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) source using the [Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) feature.
  * You must create **two separate connections** in the RudderStack dashboard using the Reverse ETL sources and HubSpot destination as shown:

[![HubSpot create associations](/docs/images/event-stream-destinations/hubspot-create-associations.webp)](</docs/images/event-stream-destinations/hubspot-create-associations.webp>)

### Workflow

  * The first connection pushes data into the HubSpot object, for example, a company object.
  * The second connection creates an association between the object records. For example, associating the company and contact objects.


### Steps to create association

  1. Add a Reverse ETL source and connect the HubSpot destination to it. While [configuring the destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/setup-guide/#new-api-settings>), make sure to toggle on the **Create associations between object record** setting.
  2. In the Data mapping settings, select the **Object** where you want to sync the data.
  3. In the next dropdown, select the HubSpot object with which you want to associate the above-mentioned object.
  4. Based on the object selections, the relevant associations (from HubSpot account) are populated in the **Association** dropdown. Select the required association.
  5. Specify the **Sync mode**.
  6. In the **Choose identifier** section, select a warehouse column and HubSpot destination field to map your records. You can choose any destination field from the dropdown that acts as a unique identifier.
  7. Choose a warehouse column each for **From Record ID** and **To Record ID** fields which act as Hubspot’s unique ID to identify an object.


> ![info](/docs/images/info.svg)
> 
> **From Record ID** and **To Record ID** are the column names of the two objects you want to associate.
> 
> For example, if you want to associate a company and a contact, the **From Record ID** should be a `Company Id` and **To Record ID** should be a `Contact Id`.

Similarly, you can create more such associations between the object records.