# Transformations Overview

Transform event data in real-time with custom JavaScript and Python functions.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


RudderStack’s **Transformations** feature lets you write custom functions to implement specific use-cases on your event data, like:

  * Filtering or sampling events
  * Cleaning or aggregating data
  * Data masking or removing sensitive PII to ensure data privacy
  * Enriching events by implementing static logic or leveraging an external API
  * Using an API to implement specific actions on the events


> ![info](/docs/images/info.svg)
> 
> RudderStack’s **Free** and **Starter** plans let you create 5 JavaScript transformations. However, you can create unlimited transformations in the **Growth** and **Enterprise** plans. See the [Pricing](<https://www.rudderstack.com/pricing/>) page for more information.

Learn more about transformations in this self-paced product tour:

## Key features

  * Transformations are easy to build, manage, debug, and reuse.
  * Enrich your events in-flight with custom logic before sending them to your destinations.
  * Use prebuilt templates to create transformations for specific use-cases by leveraging [Templates](<https://www.rudderstack.com/docs/transformations/templates/>).
  * Write transformations in JavaScript and Python.


> ![info](/docs/images/info.svg)
> 
> RudderStack’s Python transformations feature lets you use custom Python code to transform your source events on the fly. It is especially useful for the data teams that generally deal with Python.
> 
> Note that:
> 
>   * Python transformations are available only for:
>     * RudderStack [Growth](<https://www.rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.
>     * Destinations that support sending events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).
>   * RudderStack supports Python version 3.11 for writing transformations.
>   * RudderStack supports only some of the built-in Python packages to write transformations. These are [datetime](<https://docs.python.org/3.10/library/datetime.html>), [json](<https://docs.python.org/3.10/library/json.html>), [math](<https://docs.python.org/3.10/library/math.html>), [random](<https://docs.python.org/3.10/library/random.html>), [requests](<https://pypi.org/project/requests/>), [time](<https://docs.python.org/3.10/library/time.html>), and [urllib](<https://docs.python.org/3.10/library/urllib.html>), along with the external package [python-dateutil](<https://pypi.org/project/python-dateutil/2.8.2/>).
> 


  * Use transformations across your [Event Streams](<https://www.rudderstack.com/docs/sources/event-streams/>) and [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) pipelines in both [cloud mode](<https://www.rudderstack.com/docs/transformations/usage/#cloud-mode>) and [device mode](<https://www.rudderstack.com/docs/transformations/usage/#device-mode>).
  * Version control your transformations.
  * Create an organization-wide sandbox where your team can store all transformations before publishing them in production.
  * Leverage the [Transformations API](<https://www.rudderstack.com/docs/api/transformation-api/>) to programmatically manage your transformations.


## In this section

See the following guides to learn more about the different Transformations features and their usage:

Guide| Description  
---|---  
[Create Transformations](<https://www.rudderstack.com/docs/transformations/create/>)| Add and test new transformations in RudderStack  
[Use Transformations](<https://www.rudderstack.com/docs/transformations/usage/>)| Use transformations in different [RudderStack connection modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>)  
[Runtime Functions](<https://www.rudderstack.com/docs/transformations/runtime-functions/>)| Reference for various runtime functions available in transformations  
[Manage Transformations](<https://www.rudderstack.com/docs/transformations/manage/>)| Perform different operations on your transformations like connecting them to destinations, managing notifications, etc  
[Transformation Libraries](<https://www.rudderstack.com/docs/transformations/libraries/>)| Reuse transformation code with transformation libraries  
[Transformation Templates](<https://www.rudderstack.com/docs/transformations/templates/>)| Use prebuilt transformations to implement specific use cases on your event data  
[Manage Transformations using Rudder CLI](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/>)| Define transformations and libraries as YAML, then validate, test, and apply them through Rudder CLI  
[Geolocation Service](<https://www.rudderstack.com/docs/transformations/geolocation-enrichment/>)| Leverage transformations to fetch geolocation information from IP address using RudderStack’s geolocation service  
[Transformation Action](<https://www.rudderstack.com/docs/transformations/transformation-action/>)| Create, test, and publish your JavaScript/Python transformations and libraries directly from your development repository  
[Observability](<https://www.rudderstack.com/docs/transformations/observability/>)| Get full visibility into the transformation-specific metrics including errors  
[Debugging Errors](<https://www.rudderstack.com/docs/transformations/debugging-errors/>)| Debug various transformation and library errors  
[FAQ](<https://www.rudderstack.com/docs/transformations/faq/>)| Answers to some of the commonly asked questions on transformations