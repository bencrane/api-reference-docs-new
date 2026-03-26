# Create Transformations

Add and test a new transformation in RudderStack.

* * *

  * __5 minute read

  * 


This guide will help you add a new transformation in the [RudderStack dashboard](<https://app.rudderstack.com/>). It also contains the steps to capturing any event-related information in your transformation using the `log` function.

[![](https://img.shields.io/badge/Node.js%20Version-18.x-7447fc.svg?logo=data:image/png;base64,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&logoColor=&logoWidth=&style=)](<>) ![](https://img.shields.io/badge/Python%20Version-3.11-7447fc.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAYAAAA8AXHiAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAl8SURBVHgB7Z1NbFzVFcfPfeOAFGR3WpqU4iwmFIli2tSVgHSXaaVK2TQgGhASSG3KKqlUpwvworhxJCyRZJMQJXSXqRSkCBIriQqq5CiZ7JKYxQiBbaoUJlJMRSqBsQMSMDOPe579wsh4PjJ+c979+P8kZ+zxmzzb9zfnfp+rqAPuH9yepyo9FpLKkaJBCsOsfjpLwAlCRSUV0pxSdJECKl4tnSzSbaLavTA3+Hg2qPUM6RvuJkjkGaqs/ymuyWT2zpROlNt6RasLIBSoJyQ6eEem51ArwZqKxVVeWFXH9H+XIwBuocoqDHdcfbdxFZlp9I37Nj05RDU6QYhS4LtkdUj64/fvGaBPP566uNIFK4p136bte3TV9zIB0ARd3eUbyfUdsZakGiUA2mBJrs+0XJeWPf8ti20qukAA3CY6GP26vs11S6zc4NO5TLV6AQ110BmqXM18/cty6fQcfxXETwe1yhCkAp0T5npqPbvjr6KItRitKh8SAKtjrpqpbOSoFUUsXQXuIQBWTzaOWnFVmCcAEiAMaYgfFXqCIGm4hxjo0fU8AZAgYRA+HujQtYUASJJQ5QKlMBcIkkb9giPWIAGQKGE2IACSB2KB7tBDHrKhfz09sc3dPkvhtbdofv5zShMvxerrvYv+svMpcpXxMxdTF8vLqnB+/iZJMj//BfmGn2ItyBb0/E1ZkU3AU7E+F40iMzPXyDe87RXO/u8GSXH9I7l7mYK3Yl2efI+k4Ajpm1zeijX1fpkkuTI5RT7hrVjnzk+SJNIip423YnH1dPltuepw/EyRfMLrKZ0JwaglLXLaeC0WRxHJYYdXXn2DfMFrsTiKFF77F0nBPVFfeofer26QjlqHPYla3ot1/aP/i0atU1pkH6IW1mNpCsffEo1awyNHyXUgFi22tYb/foSk4LYWy+wyEGuJifNXRAv7lVdfd7pKhFh1cGFPz5RJAo6Su4YOOLtWC2LVwYW9c/d+sUjC0zxjB46Ri0CsZXAv8dk/jYrJxb3E4RG59p0UEGsFINfqgVgNiOWSanOxXNuefN6ZBj3EagLL9bunnheb4+M2F8vswmQ1xGoD7i3mt+4SiSYs8zNarrH9BaujF8RqEy7w/NY/R20hiQI/dvzNKHrZuo4LYt0m3BaKBZvu8qpQlvkFfR+OluOWzTF6uRM6CVgw/hh4IEdPPJanB3+ao80PP0TdIBaM2fzIQ/T7bXl69JEB2nDvejIV9ZOfbw/JALhgeOu7zfT1rqUHtWj80dd3F/XrgufneH39qbNFSpoN967T91gX3a+/f3309+PnOKKmHd2MEav47yNGvwNtwgSxvGxj+biBVBpjxJrV7QhXwU7oFJmdlROLJZZcVbCw4OYKhmYYI5b0u1oyd4PUtJBJGCPW9PuyGVkkC5vfNL7lyDJGLMkkHYz0lvfp//h1BpYxYklnZDl3/gpJMiGcKyJtjBpukJwX49Fsl0VOG6PEuvy2bKofaZGRuyEluJ0l+ceX3oLlU3Vo3Mi7ZBRJI5WRL71D48SS3oIumQFGOglJmhg5VyiZOCON6teHqGWkWBy1JAt7+MUjYoXNUevwP14n1zF2dcPYvgJJwT02ycLmZceu9xCNFSvaJby/QFJIF7ZklEwDo9djpVHYUh0HjpKubq9njF/ot3PogGhhSybq4Lakq3lJjReLG7uS292lE3XwnkUX5bJiaXIauRR27paLXC7KZc2ad+lcCpyI7dnn9ojJ7JpcVm2mSCuXgpTMLNczz42SC2vkrdylI1kA0jLzTIDNW+tjrN3+xQXA++e4wCUEixODSBR4vPOZ23m2Rq/MD340MEoWw+NcvNOYj+Pt71/X1m5q3qXTiSB8j4kLk9Fr+T68e7vdn7GTtWYffDgbzS3yz8s7q9vd0BvNRy6ke9i49WIxXOBcePwH5U0ZX335dSTZnXfeseL1nYpVf79YME4M0qrQOxUrhu/B94p/Zv691v0w2/B6E8RyLikI9+b4g0YWE2hwXgPOZxDnhujtXauHEZL5o0fLm5eSg8QRbPPDAzTwwEbq7Vsb5VVIEr7fS0vTXIu/08bofiw1v5H4dzMFY3I3ALdAfizQFSAW6AoQC3QFiAW6AsQCXQFiga4AsUBXgFigKxgz8v7b3zxq1MixzZzT001JzS50ijFi/e2FPyBrckLwqo+0xUJVCLoCxHKQ+ZvpRisGYjlI2tUgA7Ec47oh+fIhlmPMGrKUGWI5hgnVIAOxHMOULDYQyzGkD2JoBMRyjGnhgxEaAbEcgqtBtLFA4ph0GBTEcgje62gKEMsReCu+9EFXzYBYjnBlUva4mFZALEfgpCUmAbEcgHuDpswRxkAsBzAxlxbEshxutJ+CWCBpDhuatxRiWYyp0YqBWBZjarRiIJaljC8lfDMViGUhXAWaNm61HIhlIYejTNFmjVstB2JZhulVYAzEsgiuAl8SPMNxNUAsS2Cp+MSKtNNstwvEsgCWaVd0bqPZ7ap6IJYFjO37Z3RglE1ALMMZfvEonTp7gWzDuZMpXIGrv+GRIzRx3pzlxrcDxDIQbqhzm8q26q8eiGUYLNOuof1WNdRXAmIZROH4m9aMU7UCYhkAV33DI0eN2mWzWiBWynCU4lNibRn4bBeIlRK8AWJsX8HqBnozIJYwLBRHKJeqvZWAWAJwNRetSjhbNCq/QjeBWF2CZeJD0GOZXGtDtQJiJQT37GZmrtElXdVxjirXq7pWGCMWn7zeZ9GRJzyAubDwBc3O3og+9y0itQKHjYOugNUNoCuwWHMEQMJosRTEAokSKioFiqhEACRIENJcEKqaGYnBgTsouhiomjpNACRJjYqKH/WQw6f6IUsArBalyv99542NweLndIgASIKQivwQiVUJKgcJww4gAdZkMnv5MRKrXDo9h6gFVk0YHpopnSjzp7dG3qOopetHAqATtDtretYcjL+8JVYUtWrhDgKgA9idOFoxmfpvfnJjqnz3PQOf6U+3EgBtokLae/Xdk4X65zLLL/rk46lLd68fUHqQK08AtGBJqtHlz2dWulhHriLkAq1QNfrr1fdOvrzi95q98P6fbc+HgTqmW/s5AiBGN9S5TaUjVbHRJZlmr+c21/d+vOlMUKvq6KV+RcBvFM3pqm9fNVPZ8cE74zPNL22T3ODTuUy1MqoF24II5hksVI0OVXoqB3n0oL2XdABXkXqgIq+H77fo/yEbhjRIwA0Uz8AojkylMKxd01XV6WZVXiO+ASW4fHjWfkysAAAAAElFTkSuQmCC&logoColor=&logoWidth=&style=)

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage transformations.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) depending on their workspace policy:

Resource| Permission| Description  
---|---|---  
Transformations| **Edit**|  Make changes to the configuration of transformations  
Transformations| **Connect**|  Connect a transformation to a destination  
Transformations| **Create & Delete**| Create or delete transformations  
  
> ![warning](/docs/images/warning.svg)
> 
> To make a connection, that is, connect a transformation to a destination, the member must have both **Edit** and **Connect** permissions on both the resources.

**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to manage transformations in RudderStack dashboard](/docs/images/access-management/transformations.webp)  


#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can create, edit, delete, and connect transformations to destinations
  * Members must have the **Grant edit access** permission in **Transformations and Library** toggled on to create, edit, delete, and manage transformations
  * Members with the **Connections Admin** or **Connections Editor** role in their workspace policy can only connect transformations to destinations

[![Transformations permissions in the legacy framework](/docs/images/access-management/permissions/legacy/transformations.webp)](</docs/images/access-management/permissions/legacy/transformations.webp>)

## Add new transformation

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Collect** > **Transformations** and click **Create Transformation**.
  3. Choose a [transformation template](<https://www.rudderstack.com/docs/transformations/templates/>) for implementing specific use cases on your event data. To create a transformation from scratch, click **Custom transformation**.

[![Custom transformation option](/docs/images/features/transformations/custom-transformation.webp)](</docs/images/features/transformations/custom-transformation.webp>)

  4. Name your transformation. It must contain at least 2 characters.

[![Name your  transformation](/docs/images/features/transformations/name-transformation.webp)](</docs/images/features/transformations/name-transformation.webp>)

  5. In the **Transformation** window, select the language to write your transformation. RudderStack provides two options - **JavaScript** and **Python 3.11**.

[![Select transformation language](/docs/images/features/transformations/transformation-language.webp)](</docs/images/features/transformations/transformation-language.webp>)

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack uses [this Node.js version](<https://github.com/rudderlabs/rudder-transformer/blob/main/.nvmrc>) for JavaScript transformations and libraries.
>   * Python transformations are available only in the RudderStack Cloud [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.
> 


> ![warning](/docs/images/warning.svg)
> 
> JavaScript transformations run in an isolated environment — no Node.js modules (like `fs`, `require`) or browser APIs (like `window`, `btoa`) are available. Only standard JavaScript features are supported.

  5. Add your transformation function. You can also add other functions and call them from within the [`transformEvent`](<https://www.rudderstack.com/docs/transformations/usage/#apply-transformation-on-single event>) function.

[![Adding a Transformation](/docs/images/features/transformations/add-transformation-function.webp)](</docs/images/features/transformations/add-transformation-function.webp>)

  6. To test your transformation, import a payload using the **Import event** button. Then, click the **Run Test** button next to it.


> ![info](/docs/images/info.svg)
> 
> If you don’t import any event and click **Run Test** directly, RudderStack tests your transformation against a default `track` event payload.

[![Import event and run test](/docs/images/features/transformations/import-event-run-test.webp)](</docs/images/features/transformations/import-event-run-test.webp>)

> ![success](/docs/images/tick.svg)
> 
> You can also switch between the portrait and landscape views for better readability by clicking the button next to **Save Transformation**.
> 
> ![Switch between portrait and landscape views](/docs/images/features/transformations/switch-view.webp)

## Save transformation

To save the transformation, click the **Save Transformation** button at the bottom right.

[![Save a transformation](/docs/images/features/transformations/save-transformation.webp)](</docs/images/features/transformations/save-transformation.webp>)

Note that to save a transformation, it must run successfully with a test event. You will **not** be able to save a transformation in the following cases:

  * Transformation code is invalid.
  * Transformation gives an error upon running it with a test event, as shown:

[![Error while saving a transformation](/docs/images/features/transformations/save-transformation-error.webp)](</docs/images/features/transformations/save-transformation-error.webp>)

## Test transformation

RudderStack lets you test your transformations to identify and prevent any transformation errors. With this feature, you can thoroughly test various scenarios and edge cases on your event payloads, and ensure effective event processing within RudderStack.

### Import event payload

To import a test payload, click the **Import Event** button.

[![Import event and run test](/docs/images/features/transformations/import-event-run-test.webp)](</docs/images/features/transformations/import-event-run-test.webp>)

RudderStack gives you the following options to test your transformations:

  * Use sample/placeholder event data within the **RudderStack Events** tab to test your transformations on default RudderStack event payloads. This is helpful when you don’t have any live events in your workspace.
  * Edit an event payload and save it as a new event. You can then use it to test your transformation.
  * Use the **Live Events** feature to test your transformations on live events generated from your source.


You can select any default RudderStack event to test your transformation. RudderStack provides four sample payloads (`identify`, `track`, `page`, and `screen`) that correspond to common RudderStack events.

![Default RudderStack events](/docs/images/features/transformations/import-rudderstack-events.webp)

From the dropdown, select the source. Then, send some events from this source - they will appear in this window automatically.

![Import live events](/docs/images/features/transformations/import-live-events.webp)

Choose a live event and click **Import**. You can then test your transformation on this payload.

> ![warning](/docs/images/warning.svg)
> 
> Once you import a live event, all the live events shown in the window are lost. You need to send new events to import a live event again.

### IP allowlisting

For testing transformations that [leverage external API calls](<https://www.rudderstack.com/docs/transformations/usage/#make-external-api-requests>), make sure that these API providers allowlist the following IPs depending on your RudderStack region:

> ![info](/docs/images/info.svg)
> 
> Allowlisting these IPs is required when you want to make API calls to servers or services that control the IPs from which they accept API requests.

Region  
---  
**US**| **EU**  
  
  * 3.216.35.97
  * 18.214.35.254
  * 23.20.96.9
  * 34.198.90.241
  * 34.211.241.254
  * 44.236.60.231
  * 52.38.160.231
  * 54.147.40.62
  * 100.20.239.77

| 

  * 3.64.201.167
  * 3.66.99.198
  * 3.123.104.182
  * 3.125.132.33
  * 18.196.167.201
  * 18.198.90.215

  
  
> ![warning](/docs/images/warning.svg)
> 
> For production use cases, the IP addresses to allowlist while making external API calls depend on your [RudderStack plan](<https://www.rudderstack.com/pricing>) and region.
> 
> See the [IP allowlisting FAQ](<https://www.rudderstack.com/docs/transformations/faq/#ip-allowlisting>) for details.

### Limitations

  * You cannot import multiple sample events to test your transformation.
  * The live events contain payloads present at the source. They do not resemble the enriched events you see in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#transformations-live-events>) viewer in your transformation.


## Capture event information with logs

Once you add a transformation, you can capture any event-related information in the form of logs while testing it. You can do this by including the [`log` function](<https://www.rudderstack.com/docs/transformations/runtime-functions/#log>) in your transformation code, as shown:
    
    
    export function transformEvent(event, metadata) {
      const meta = metadata(event);
      event.sourceId = meta.sourceId;
    
      log("Event Name is", event.event, ";", "Message ID is", event.messageId);
      log("Source ID is", meta.sourceId);
    
      return event;
    }
    
    
    
    def transformEvent(event, metadata):
        meta = metadata(event)
        event['sourceId'] = meta['sourceId']
        
        log("Event Name is", event['event'], ";", "Message ID is", event['messageId'])
        log("Source ID is", meta['sourceId'])
        
        return event
    

On adding the above transformation and clicking **Run Test** , you can see the resulting log in the **Logs** section of the dashboard:

[![Transformation log](/docs/images/features/transformations/transformation-logs.webp)](</docs/images/features/transformations/transformation-logs.webp>)