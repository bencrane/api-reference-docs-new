# Setup Guide Beta

Send your event data from RudderStack to X Audience.

* * *

  * __less than a minute

  * 


This guide will help you set up X Audience as a destination in RudderStack when connecting to a [Reverse ETL source](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/eloqua/connect-retl-source/>).

> ![info](/docs/images/info.svg)
> 
> This guide assumes you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **X Audience**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify your destination in RudderStack.  
oAuth settings| Click **Create Account** > **Connect with X Audience** and give RudderStack the necessary permissions to access your X account. Then, click **Save**. You can add multiple accounts and choose any one to proceed with the setup.  
Select your account| RudderStack automatically populates the relevant X audience accounts - select the relevant account from the dropdown.  
  
### Configuration settings

This guide lists the advanced configuration settings to receive the data correctly in X Audience.

Setting| Description  
---|---  
Enable user data hashing| Turn on this setting to hash all user data before sending it to X Audience.  
  
**Note** : Do not turn on this setting if your data is already hashed.