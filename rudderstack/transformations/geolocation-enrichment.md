# Geolocation Enrichment using Transformations

Fetch geolocation information from IP address using RudderStack’s geolocation service.

Available Plans

  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> The most reliable way to enrich events with geolocation information is using RudderStack’s [Geolocation Enrichment at Source](<https://www.rudderstack.com/docs/data-governance/geolocation-service/>) feature.

This guide explains how to enrich events with users’ geolocation information using transformations.

## Overview

You can add a geolocation service function (`geolocation`) in your transformation takes the IP address present in the event (`request_ip`) as an argument. RudderStack supports both JavaScript and Python transformations for this feature.

The transformation returns the following geolocation data once it runs successfully:

  * City
  * Country
  * Region
  * Location
  * Postal code
  * Timezone


See [Runtime Functions in Transformations](<https://www.rudderstack.com/docs/transformations/runtime-functions/#geolocation>) for more information on using the `geolocation` function.

## License

This product includes GeoLite2 data created by MaxMind, available from [<https://www.maxmind.com>](<https://www.maxmind.com>).

For more information, see [Maxmind license agreement](<https://dev.maxmind.com/geoip/geolite2-free-geolocation-data#license>).

> ![info](/docs/images/info.svg)
> 
> RudderStack does not call the MaxMind API to get the geolocation data. Instead, the MaxMind database is embedded in RudderStack’s service and is served via RudderStack’s own API.

## Usage

> ![announcement](/docs/images/announcement.svg)
> 
> If you’re hosting RudderStack on-premise, contact [RudderStack Support](<mailto:support@rudderstack.com>) to use this feature.

To use the geolocation service, [add a new transformation](<https://www.rudderstack.com/docs/transformations/create/#adding-a-transformation>) as shown:
    
    
    /***
     * This transformation enriches events with geolocation data using an IP-to-geolocation API powered by Maxmind, available from https://www.maxmind.com.
     * This allows you to easily query events based on geolocation data, e.g., country, city.
     ***/
    
    export async function transformEvent(event, metadata) {
      if (event.request_ip) {
        try {
          if (!event.context) event.context = {};
          event.context.geo = await geolocation(event.request_ip);
        } catch (e) {
          log(e.message);
        }
      }
    
      return event;
    }
    
    
    
    def transformEvent(event, metadata):
        try:
            if event.get('request_ip'):
                res = geolocation(event["request_ip"])
                if not event.get('context', None):
                    event['context'] = {}
                event['context']['geo'] = res
        except Exception as e:
            log(str(e))
        return event
    

In the above transformation, the geolocation service function [`geolocation`](<https://www.rudderstack.com/docs/transformations/runtime-functions/#geolocation>) takes the IP address present in the event (`request_ip`) as an argument. Once it runs successfully, it returns the following geolocation data:

  * City
  * Country
  * Region
  * Location
  * Postal code
  * Timezone


> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * The geolocation data provided by RudderStack powered by Maxmind is not 100% accurate and varies by country. See the Maxmind website (link: <https://www.maxmind.com/en/geoip2-city-accuracy-comparison>) to get the accuracy information by country.
> 
>   * RudderStack returns a `400 Bad Request` error if you pass a malformed IP address.
> 
>   * If you currently use a [geolocation enrichment template](<https://www.rudderstack.com/docs/transformations/templates/#geolocation-enrichment>), switching to this transformation will result in some schema changes:
> 
>     * RudderStack creates new columns for the IP addresses in your warehouse.
>     * It stores the country code instead of country name.
> 


[![Geolocation information](/docs/images/features/rudderstack-geolocation-service.webp)](</docs/images/features/rudderstack-geolocation-service.webp>)

## FAQ

#### How is this feature different from the geolocation enrichment transformation template?

RudderStack’s geolocation service feature lets you enrich events with users’ geolocation information for a given IP address by leveraging the **licensed** GeoLite2 data created by [MaxMind](<https://www.maxmind.com>).

On the other hand, the [geolocation enrichment template](<https://www.rudderstack.com/docs/transformations/templates/#geolocation-enrichment>) enriches events with geolocation data using an IP-to-geolocation API endpoint that **you need to provide**.