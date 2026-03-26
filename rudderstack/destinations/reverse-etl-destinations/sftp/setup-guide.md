# Setup Guide Beta

Set up and configure SFTP as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up SFTP as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to your downstream apps via SFTP.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **SFTP**. Then, click **Continue**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify your destination in RudderStack.  
Host| Enter the host name or IP address of the server **without** the port number.  
Port| Enter the port number of the server.  
User name| Enter the user name.  
Authentication| Select the authentication mechanism from the dropdown. RudderStack provides the following options:

  * **Username + Password**
  * **Username + SSH key**

  
Password| If you have selected **Username + Password** , enter the password for the above user.  
Private key| If you have selected **Username + SSH key** , enter the full private key for the user including the header and footer.  
File format| Select the file format (CSV or JSON) from the dropdown.  
File path| Specify the path name where RudderStack stores the data. For example:  
  
`directory/{destinationID}/{jobRunID}/{YYYY}_{MM}_{DD}/file_{timestampInMS}.csv`  
  
Note that:  
  


  * The parent directory of the file should already exist.
  * RudderStack supports specifying the date, time, and sync metadata variables within curly brackets (`{}`).
  * `destinationID` and `jobRunID` are required fields.
  * The date and time variables correspond to the upload time.

  
  
## Specify file path variables

While specifying the file path where RudderStack stores all the data, you can also specify the date, time, and sync metadata variables within curly brackets (`{}`).

RudderStack supports the following date/time variables:

Variable| Description  
---|---  
`YYYY`| Year in four digits. For example, `2024`.  
`MM`| Month in two digits. For example, `05`.  
`DD`| Day in two digits. For example, `09`.  
`hh`| Hour in two digits (in 24-hour format). For example, `15`.  
`mm`| Minutes in two digits. For example, `56`.  
`ss`| Seconds in two digits. For example, `13`.  
`ms`| Milliseconds in three digits. For example, `460`.  
`timestampInSec`| UNIX timestamp in seconds.  
`timestampInMS`| UNIX timestamp in milliseconds.  
  
You also need to specify the following sync metadata variables in the path:

Variable| Description  
---|---  
`destinationID`  
Required| The destination ID.  
`jobRunID`  
Required| Job run ID of a sync.  
  
Some sample paths specified in the **File path** connection setting are shown below:

  * `directory/{destinationID}/{jobRunID}/file_{timestampInMS}.csv`
  * `directory/{destinationID}/file_{jobRunID}_{timestampInMS}.csv`


## Next steps

  * [Connect Reverse ETL source to SFTP destination](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/sftp/connect-retl-source/>)