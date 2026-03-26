# Lytics Bulk Upload Configuration Settings Beta

Advanced configuration settings for Lytics Bulk Upload destination.

* * *

  * __less than a minute

  * 


This guide lists the advanced configuration settings to receive the data correctly in Lytics Bulk Upload.

### Configuration settings

Setting| Description  
---|---  
Choose your account Specific Stream Name| Choose the Lytics stream name populated from your Lytics account. You can also add a custom stream name directly.  
  
### Stream Wise Property Mapping

Setting| Description  
---|---  
Stream-based Property Mapping| Click **Set-up mapping** to map the RudderStack event properties to Lytics stream-based properties. These are 1:1 mappings and RudderStack refers them from the `message.properties` key.  
  
### Timestamp Property Mapping

Setting| Description  
---|---  
Choose the field that can be used as timestamp| Enter the property name to be considered as timestamp in Lytics.