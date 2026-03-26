# Connect Reverse ETL Source to Yandex.Metrica Offline Events Beta

Configure a Reverse ETL source with your Yandex.Metrica Offline Events destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Yandex.Metrica Offline Events destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Yandex.Metrica Offline Events destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/yandex-metrica-offline-events/setup-guide/#connection-settings>) for Yandex.Metrica Offline Events destination and click **Continue**.


> ![info](/docs/images/info.svg)
> 
> To sync the data successfully, make sure to give RudderStack the necessary permissions to access your Yandex.Metrica account. Also, enter the **Counter ID** and **Goal ID** in the configuration settings.

  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select the **Object**.
  3. Specify the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to Yandex.Metrica.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.


> ![info](/docs/images/info.svg)
> 
> You can map this warehouse column to any of the following Yandex.Metrica fields:
> 
>   * User ID
>   * Client ID
>   * YCLID
> 


  5. Map the other warehouse columns to specific Yandex.Metrica fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/yandex-metrica-map-fields.webp)](</docs/images/event-stream-destinations/yandex-metrica-map-fields.webp>)

### Supported mappings

RudderStack maps the following properties to the corresponding Yandex.Metrica properties:

> ![info](/docs/images/info.svg)
> 
> RudderStack [sends the offline conversion events](<https://yandex.com/dev/metrika/doc/api2/management/offline_conversion/upload.html#upload__response>) as [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) calls to Yandex.Metrica.

RudderStack property| Yandex.Metrica property| Description  
---|---|---  
`userId`  
Required| `USER_ID`| Mapped when the user ID is assigned by the site owner.  
`userId`  
Required| `CLIENT_ID`| Mapped when the site visitor ID is assigned by Yandex.Metrica.  
`userId`  
Required| `YCLID`| Mapped when the click ID on a Yandex.Direct ad is assigned by Yandex.Direct.  
`properties.target`  
Required| `Target`| The goal ID.  
`timestamp`  
Required| `DateTime`| Date and time of the conversion in UNIX timestamp.  
`properties.price`| `price`| Cost of the goal specified using a dot (`.`) as the decimal operator.  
`properties.currency`| `currency`| Currency using the three-letter code as per ISO 4217 standards.  
`properties.comment`| `comment`| Sent as a query parameter.  
  
## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.