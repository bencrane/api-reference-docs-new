# Post Affiliate Pro

Send your event data from RudderStack to Post Affiliate Pro.

* * *

  * __6 minute read

  * 


[Post Affiliate Pro](<https://www.postaffiliatepro.com/>) is a popular affiliate marketing software that lets you manage your affiliate programs, track their performance, and boost your lead generation efforts.

RudderStack supports Post Affiliate Pro as a destination to which you can seamlessly send your customer data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Post Affiliate Pro** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> Based on your website’s content security policy, you might need to [allowlist the domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) you have defined in the **URL of Post Affiliate Pro** RudderStack dashboard setting to load the Post Affiliate Pro SDK successfully.

## Get started

Once you have confirmed that your source platform supports sending events to Post Affiliate Pro, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Post Affiliate Pro**.
  * Assign a name to the destination and click **Continue**.


### Connection settings

The connection settings required to configure Post Affiliate Pro as a destination in RudderStack are listed below:

[![Post Affiliate Pro connection settings](/docs/images/event-stream-destinations/pap-connection-settings-1.webp)](</docs/images/event-stream-destinations/pap-connection-settings-1.webp>)[![Post Affiliate Pro connection settings](/docs/images/event-stream-destinations/pap-connection-settings-2.webp)](</docs/images/event-stream-destinations/pap-connection-settings-2.webp>)[![Post Affiliate Pro connection settings](/docs/images/event-stream-destinations/pap-connection-settings-3.webp)](</docs/images/event-stream-destinations/pap-connection-settings-3.webp>)

  * **URL of Post Affiliate Pro** : Enter your Post Affiliate Pro tracking URL here.


> ![info](/docs/images/info.svg)
> 
> For more information on getting the Post Affiliate Pro URL, refer to the FAQ section below.

  * **Account ID** : Enter your network merchant account ID here.


> ![info](/docs/images/info.svg)
> 
> Post Affiliate Pro owners will have this value set to `default1`.

  * **Param Name User ID** : If you have changed the **Affiliate ID / Referrer ID** parameter value by going to **Configuration** \- **URL Parameter Names** in your Post Affiliate Pro dashboard, this new value should be entered here.

  * **Cookie Domain** : Enter your cookie domain name here. You can find this setting by going to your Post Affiliate Pro dashboard and navigating to **Configuration** \- **Cookies** :


[![Post Affiliate Pro cookie domain setting](/docs/images/event-stream-destinations/pap-cookie-domain.webp)](</docs/images/event-stream-destinations/pap-cookie-domain.webp>)

  * **Cookie to Custom Field** : Enter the ID of the field where the cookie will be written.

  * **Campaign to Custom Field** : Enter the ID of the field where the campaign value will be written.

  * **Affiliate to Custom Field** : Enter the ID of the field where the affiliate ID will be written.


#### Affiliate to Link settings

  * **Affiliate Link ID** : Enter your affiliate link ID here, e.g. `affiliateId`. This refers to the ID of the DOM object where the Affiliate ID is added.

  * **AffiliateId Parameter Name** : Enter your affiliate ID parameter name, e.g. `a_aid`.


Suppose you set the **Affiliate Link ID** to `affiliateId` and **AffiliateId Parameter Name** to `aff_id`. Then, the anchor link of the domain where you want to send the affiliate/referrer ID will be converted from: `[](http://abcd.com)` to: `["id="affiliateId">](http://abcd.com/?aff_id=<the_affiliate_id>)`.

#### Cookie to Link settings

  * **Cookie Link ID** : Enter your cookie link ID here. This refers to the ID of the DOM object where the cookie ID is added.

  * **Cookie Parameter Name** : Enter the cookie parameter name here.


> ![info](/docs/images/info.svg)
> 
> These settings are similar to the **Affiliate to Link** settings, except that the cookie will be written in place of the `affiliateId`.

#### Event tracking settings

  * **Merge Products** : This setting determines if RudderStack should merge the product information while making a sale call to Post Affiliate Pro. If disabled, an individual sale object will be created for each product.


> ![info](/docs/images/info.svg)
> 
> Refer to the Merging product information during sales tracking section for more information on this feature.

  * **Disable Tracking Method** : Disable this setting to disable flash cookie creation.

  * **List of Events for Click** : For [Clicks Tracking](<https://support.qualityunit.com/417400-Clicks-referrals-tracking>), RudderStack will consider only the events listed in this field.


> ![warning](/docs/images/warning.svg)
> 
> Make sure the event names specified in this field are comma-separated.

  * As this is a destination that supports sending events only via web device mode, the **Use device mode to send events** option will be always enabled.


Finally, click **Next** to complete the setup. Post Affiliate Pro will now be enabled as a destination in RudderStack.

## Identify

You can use the RudderStack `identify` method to set a unique customer ID. You can then use this ID to subsequently track the customer’s activities.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify(
      "user001", // visitor Id
    );
    

RudderStack calls the `setVisitorId` function of the Post Affiliate Pro SDK and sets the user ID provided in the `identify` call:
    
    
    PostAffTracker.setVisitorId("user001");
    

## Track

RudderStack supports two types of event tracking for Post Affiliate Pro:

  * **Clicks tracking** : RudderStack initiates Post Affiliate Pro’s clicks tracking mechanism for the events that are explicitly specified in the **List of Events for Click** field, while setting up the integration.

  * **Sales tracking** : RudderStack initiates Post Affiliate Pro’s sales tracking only for the **Order Completed** event.


### Clicks tracking

A sample `track` event for clicks tracking is as shown:
    
    
    rudderanalytics.track(
    "User Clicked", //event name
    {
          affiliateId: "affiliate id",
          bannerId: "banner id",
          campaignId: "campaign id",
          channel: "channel",
          data1: "data1",
          data2: "data2",
    } //properties
    );
    

> ![warning](/docs/images/warning.svg)
> 
> The **User Clicked** event must be explictly specified in the **List of Events for Click** field. Otherwise, the event will be discarded.

RudderStack maps the following properties to the Post Affiliate Pro click event properties:

**RudderStack Event Property**| **Post Affiliate Pro Property**  
---|---  
`data1`| `Data1`  
`data2`| `Data2`  
`affiliateId`| `AffiliateID`  
`bannerId`| `BannerID`  
`campaignId`| `CampaignID`  
`channel`| `Channel`  
  
### Sales tracking

In case of sales tracking, RudderStack creates a Post Affiliate Pro `sale` object. For the properties in the event, RudderStack then calls the respective `sale` object function.

A sample `Order Completed` event sent to Post Affiliate Pro sales tracking is shown below:
    
    
    rudderanalytics.track(
    "Order Completed", //event name
    {
          checkout_id: "12345",
          order_id: "1234",
          affiliation: "aff_id",
          total: 17.45,
          fixedCost: 20.5,
          revenue: 15.0,
          customCommision: 15,
          campaign: "campaignId",
          channel: "channelId",
          coupon: "ImagePro",
          currency: "EUR",
          status: "A",
          data1: "something",
          data2: "something",
          data3: "something",
          data4: "something",
          data5: "something",
          doNotDeleteCookies: true,
    
          products: [
            {
              product_id: "123",
              sku: "G-5",
              name: "Product1",
              price: 14,
              fixedCost: 20.5,
              quantity: 1,
              customCommision: 10.23,
              category: "Miscellaneous",
              currency: "USD",
              commisionStatus: "A",
              url: "https://www.website.com/product/path",
              image_url: "https://www.website.com/product/path.jpg",
            },
            {
              product_id: "345",
              sku: "F-5",
              name: "Product2",
              price: 2.45,
              fixedCost: 5.0,
              quantity: 2,
              customCommision: 10.50,
              commisionStatus: "A",
              category: "General",
            },
          ],
    } //properties
    );
    

When the **Merge Products** option is enabled while configuring the destination in the dashboard, RudderStack merges the product information and sends the `sale` object as seen in the Post Affiliate Pro dashboard below:

[![Post Affiliate Pro sale object with combined product information](/docs/images/event-stream-destinations/pap-mergeproduct-true.webp)](</docs/images/event-stream-destinations/pap-mergeproduct-true.webp>)

If this option is disabled, two separate `sale` objects are created and sent to Post Affiliate Pro:

[![Post Affiliate Pro separate sale objects](/docs/images/event-stream-destinations/pap-mergeproduct-false.webp)](</docs/images/event-stream-destinations/pap-mergeproduct-false.webp>)

## FAQ

#### Where do I get the Post Affiliate Pro URL?

To get your Post Affiliate Pro URL, follow these steps:

  1. Log into your Post Affiliate Pro merchant website.
  2. Then, click **Tools** and go to **Integration**.
  3. Under **Main Integration Steps** , choose any one of the **Clicks tracking** or **Sales/Leads Tracking** options.
  4. Finally, copy the `src` part as shown below:

[![Post Affiliate Pro tracking URL](/docs/images/event-stream-destinations/pap-tracking-url.webp)](</docs/images/event-stream-destinations/pap-tracking-url.webp>)