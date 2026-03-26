# Chartbeat

Send your event data from RudderStack to Chartbeat.

* * *

  * __3 minute read

  * 


[Chartbeat](<https://chartbeat.com/>) is the industry leader for real-time content and web analytics, based on JavaScript.

RudderStack supports sending your events to Chartbeat from the web native SDK by calling RudderStack’s APIs.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Chartbeat** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have ascertained that the platform is supported by Chartbeat, please follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source and Chartbeat as a destination.
  * In the Connection Settings page, please enter the relevant information in the fields shown in the following screen:


[![](/docs/images/image%20%2818%29.webp)](</docs/images/image%20%2818%29.webp>)Connection Settings for Chartbeat

Each field is as explained below:

  * **Domain** \- Enter the domain name with which your Chartbeat account was configured. Don’t append any extra url parameters to it. For example: `rudderstack-test.com`
  * **UID -** Enter your Chartbeat UID here. You can find the UID on the Chartbeat [Adding The Code](<https://chartbeat.com/docs/adding_the_code/>) page.
  * **Send Name and Category as Title** \- Enable this setting if you want the RudderStack `page` API to send the page title as visible in Chartbeat dashboard as `page category` \+ `page name` .


> ![info](/docs/images/info.svg)
> 
> If this setting is enabled and the category is not set, RudderStack only sends the name as the page title.

  * **Use Chartbeat video script** \- Enable this setting if you want the RudderStack SDK to download `chartbeat_video.js` . This file is provided by Chartbeat to track and capture video interactions. Once the setting is enabled, the script will start capturing the play and pause events of mainly the HTML5 videos from the `<video ... </video>` tag.


## Page

Making a call to the `page` API will send out an object to Chartbeat containing the information of your page and its related properties.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("section-name", "home", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
      author: "author-name",
    });
    

The above code snippet populates the following properties along with the associated values:

Property| Value  
---|---  
`category`| section-name  
`name`| home  
`author`| author-name  
`path`| path  
`url`| url  
`title`| title  
`search`| search  
`referrer`| referrer  
  
### Single Page Applications

For Single Page Applications (SPAs), the first `page` call asynchronously loads `chartbeat.js` (or `chartbeat_video.js`) with the properties specified in the `page` call. All further `page` calls are sent to Chartbeat by calling Chartbeat’s virtual `page` API with the same properties that were passed to the initial `page` call.

## FAQ

#### Where do I find the Chartbeat UID?

You can find your Chartbeat UID on Chartbeat’s [Adding The Code](<https://chartbeat.com/docs/adding_the_code/>) page.