# Setup Guide Beta

Set up and configure Yandex.Metrica as a destination in RudderStack.

* * *

  * __less than a minute

  * 


This guide will help you set up Yandex.Metrica Offline Events as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Yandex.Metrica Offline Events.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Yandex Metrica Offline Events**.
  2. Assign a name to uniquely identify your destination in RudderStack. Then, click **Continue**.


### Connection settings

Setting| Description  
---|---  
Account Settings| Click **Create Account** > **Connect with Yandex Metrica Offline Events** and give RudderStack the necessary permissions to access your Yandex.Metrica account.  
Counter ID| Enter your Yandex.Metrica counter ID.  
Goal ID| Enter your Yandex.Metrica goal ID.  
  
## Next steps

  * [Connect Reverse ETL source to Yandex.Metrica Offline Events](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/yandex-metrica-offline-events/connect-retl-source/>)


## FAQ

#### **Where can I find the Yandex.Metrica Offline Events counter ID and goal ID?**

  1. Log in to your [Yandex.Metrica dashboard](<https://metrica.yandex.com/>).
  2. Under **My tags** , click the relevant offline conversion tag.

[![Yandex.Metrica tag](/docs/images/event-stream-destinations/yandex-metrica-tag.webp)](</docs/images/event-stream-destinations/yandex-metrica-tag.webp>)

  3. From the left sidebar, click **Goals**. You can see the counter ID and goal ID listed here:

[![Yandex.Metrica counter and goal ID](/docs/images/event-stream-destinations/yandex-counter-goal-id.webp)](</docs/images/event-stream-destinations/yandex-counter-goal-id.webp>)