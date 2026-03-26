# View and Edit Tracking Plans

Manage your tracking plans in the RudderStack dashboard.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __9 minute read

  * 


This guide walks you through the different tracking plan management options in the RudderStack dashboard.

## View tracking plans

To see all the tracking plans associated with your workspace, go to **Govern** > **Tracking Plans**.

In this view, you get all the tracking plan-related details like name, description, last modified, tracking plan creation method, connected sources, and the last modified time.

[![Tracking Plan list](/docs/images/data-governance/view-tracking-plans.webp)](</docs/images/data-governance/view-tracking-plans.webp>)

The following table lists the different values for the **Creation type** column that explain how the tracking plan was created:

Creation type| Description  
---|---  
Migrated| Tracking plan was [migrated](<https://www.rudderstack.com/docs/data-governance/tracking-plans/migration-guide/>) from the old to new format.  
Template| Created using the [default template](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#2-using-a-tracking-plan-template>).  
Data Catalog| Created using the [data catalog](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#3-from-the-data-catalog>).  
Event Audit API| Created from the source events and properties collected via the [Event Audit API](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#pull-from-source>).  
Data Catalog API| Created using the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>).  
Google sheet/Tracking plan API| Created from the [tracking plan spreadsheet](<https://www.rudderstack.com/docs/data-governance/tracking-plans/tracking-plan-spreadsheet/>).  
  
### Tracking plan details

Click on a tracking plan to view the following details:

  * **Schema** : Displays the event schema for your tracking plan. Click an event to view its properties or the code which you can use to instrument the event in your source platform. You can also add a new event to the tracking plan by clicking the **Add event schema** button.

[![Tracking Plan schema tab](/docs/images/data-governance/tracking-plans/tracking-plan-schema.webp)](</docs/images/data-governance/tracking-plans/tracking-plan-schema.webp>)

  * **Sources** : Displays the source(s) connected to the tracking plan. You can view the source details, edit source settings, and disconnect the source from tracking plan by clicking the meatballs menu next to the source.
  * **Settings** : Lets you edit the name of the tracking plan or delete the tracking plan (only if not connected to any source).
  * **Activity** : Lets you view all the activities performed on the tracking plan like events/properties added, removed, or updated etc. along with the user who performed that action.

[![Tracking Plan Activity tab](/docs/images/data-governance/activity-tab.webp)](</docs/images/data-governance/activity-tab.webp>)

## Edit tracking plans

Go to **Govern** > **Tracking Plans** to see all the tracking plans in your workspace. Then, select a tracking plan to:

  * Add a new event schema for the tracking plan.
  * Modify an existing event schema.


### Add a new event schema

The **Add event schema** button lets you build a new event schema for the tracking plan. You can leverage an existing data catalog event or create a new event from scratch to build the new schema.

[![Tracking Plan schema tab](/docs/images/data-governance/tracking-plans/tracking-plan-schema.webp)](</docs/images/data-governance/tracking-plans/tracking-plan-schema.webp>)

To build an event schema for a new event created from scratch:

> ![info](/docs/images/info.svg)
> 
> RudderStack automatically adds this event to your [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>)

  1. Click **Add event schema** > **Create a new event**.

![Tracking Plan build schema event options](/docs/images/data-governance/tracking-plans/build-schema.webp)

  2. Specify the event type, name, description, and category.
  3. Click **Create event schema**.

![Tracking Plan create a new event](/docs/images/data-governance/tracking-plans/create-new-event.webp)

##### **Manage properties**

  4. Click the **Add properties** button. A panel pops up on the right where you can select the properties to associate with this event. You can also [create a new property from scratch](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#while-editing-a-tracking-plan>) from this panel.
  5. Select the properties from the list. You can also filter them by data type, search a property by name, or create a new property in the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>). Then, click the **Add properties** button.


> ![success](/docs/images/tick.svg)
> 
> You can also nest event properties within a property of Object or Array data type.

![Add properties for the new event](/docs/images/data-governance/tracking-plans/add-properties-new-event.webp)

  6. After adding the properties, you can add the required validation rules by marking them as **Required** or **Optional**.

![Add properties rules for the new event](/docs/images/data-governance/tracking-plans/properties-required-optional.webp)

##### **Manage tracking plan configurations**

  7. You can also define the following tracking plan configurations for this event:


  * Whether RudderStack should allow events to contain properties beyond those defined in this schema. Turn off the toggle to ensure that the tracking plan accepts only the configured event properties.
  * Which event object the tracking plan applies the rules to. See How tracking plans validate event information for more information.

![Additional configurations for event schema](/docs/images/data-governance/tracking-plans/event-schema-configuration-options.webp)

  8. Click **Save changes** to save the new event schema.


You will then see a shareable event spec page containing the event and property details and a [Codegen](<https://www.rudderstack.com/docs/data-governance/tracking-plans/codegen/>).

![Event schema details](/docs/images/data-governance/tracking-plans/event-schema-details.webp)

To build an event schema for an existing data catalog event:

  1. Click **Add event schema**.
  2. Select the required event from the list of data catalog events.
  3. Click **Add event schema**.

![Tracking Plan build schema from existing events](/docs/images/data-governance/tracking-plans/build-schema-existing-event.webp)

##### **Manage properties**

  4. Click the **Add properties** button. A panel pops up on the right where you can select the properties to associate with this event. You can also [create a new property from scratch](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#while-editing-a-tracking-plan>) from this panel.
  5. Select the properties from the list. You can also filter them by data type, search a property by name, or create a new property in the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>). Then, click the **Add properties** button.


> ![success](/docs/images/tick.svg)
> 
> You can also nest event properties within a property of Object or Array data type.

![Add properties for the new event](/docs/images/data-governance/tracking-plans/add-properties-new-event.webp)

  6. After adding the properties, you can add the required validation rules by marking them as **Required** or **Optional**.

![Add properties rules for the new event](/docs/images/data-governance/tracking-plans/properties-required-optional.webp)

##### **Manage tracking plan configurations**

  7. You can also define the following tracking plan configurations for this event:


  * Whether RudderStack should allow events to contain properties beyond those defined in this schema. Turn off the toggle to ensure that the tracking plan accepts only the configured event properties.
  * Which event object the tracking plan applies the rules to. See How tracking plans validate event information for more information.

![Additional configurations for event schema](/docs/images/data-governance/tracking-plans/event-schema-configuration-options.webp)

  8. Click **Save changes** to save the new event schema.


You will then see a shareable event spec page containing the event and property details and a [Codegen](<https://www.rudderstack.com/docs/data-governance/tracking-plans/codegen/>).

![Event schema details](/docs/images/data-governance/tracking-plans/event-schema-details.webp)

### Update an existing event schema

Click the meatballs (`...`) menu next to an event and select **Edit event schema**.

[![Edit Event schema](/docs/images/data-governance/tracking-plans/edit-event-schema.webp)](</docs/images/data-governance/tracking-plans/edit-event-schema.webp>)

In this view, you can:

  * Add or remove properties from the event schema.
  * Manage the tracking plan configurations for the event.
  * Perform bulk actions for the event properties like removing them or marking them all as **Required** or **Optional**.

[![Bulk actions on event properties](/docs/images/data-governance/tracking-plans/edit-schema-bulk-actions.webp)](</docs/images/data-governance/tracking-plans/edit-schema-bulk-actions.webp>)

Make sure to click **Save changes** for any schema changes to take effect.

> ![warning](/docs/images/warning.svg)
> 
> Note the following while editing an event schema:
> 
>   * You cannot specify or edit the advanced rules for an event property. To do so, you will need to go to the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>), click the required property, and go to the [Advanced rules](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#advanced-rules>) tab.
>   * You cannot change an event type. To do so, you will need to delete the event from the Data Catalog and [create a new event](<https://www.rudderstack.com/docs/data-governance/data-catalog/events/#add-event>).
> 


### Event structure for tracking plan validation

By default, RudderStack applies the tracking plan validation on the following objects present within an event:

Events| Object  
---|---  
`track` / `screen` / `page`| `properties`  
`identify` / `group`| `traits`  
  
If you are instrumenting your events such that the relevant information is present in a different object, make sure to select the relevant option from the **Apply rules to** dropdown.

> ![warning](/docs/images/warning.svg)
> 
> This dropdown is only available for the `identify`, `page`, `screen` and `group` events.
> 
> For `track` events, RudderStack automatically sets the object to `properties` by default - this is **not** editable.

[![Apply rules setting](/docs/images/data-governance/tracking-plans/validation-rules-object.webp)](</docs/images/data-governance/tracking-plans/validation-rules-object.webp>)

### Add nested event properties

RudderStack supports defining complex nested properties for an event in your tracking plan - this allows you to validate complex data structures in your inbound events and metadata.

You can add nested event properties while [creating a new tracking plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/>) or [updating your tracking plan schema](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/>):

  1. Click the **Add properties** button and choose an event property of the **Object** or **Array** data type from the right sidebar. Then, click the **Add property** button.

[![Add nested property to tracking plan](/docs/images/data-governance/tracking-plans/add-nested-property-1.webp)](</docs/images/data-governance/tracking-plans/add-nested-property-1.webp>)

> ![warning](/docs/images/warning.svg)
> 
> For nesting properties within a property of Array data type, you must set the [**Array of**](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#add-property>) setting to **Object** , as shown:
> 
> ![Array property type](/docs/images/data-governance/array-property-type.webp)

  2. A **+** sign will appear as you hover over the Object or Array property. Alternatively, you can click the meatballs menu next to property and click **Add nested property**.

[![Add nested property to tracking plan](/docs/images/data-governance/tracking-plans/add-nested-property-2.webp)](</docs/images/data-governance/tracking-plans/add-nested-property-2.webp>)

  3. Select the properties to nest from the right sidebar.

[![Add nested property to tracking plan](/docs/images/data-governance/tracking-plans/add-nested-property-3.webp)](</docs/images/data-governance/tracking-plans/add-nested-property-3.webp>)

  4. You can also enable the **Allow extras** toggle to allow nested properties beyond those defined in this schema. Disabling this toggle ensures only the specified nested properties are accepted.

[![Allow extras option in the nested property settings](/docs/images/data-governance/tracking-plans/nested-property-allow-extras.webp)](</docs/images/data-governance/tracking-plans/nested-property-allow-extras.webp>)

Note that:

  * You can nest properties only within a property of **Object** or **Array** data type.
  * RudderStack supports up to **three levels** of nested properties within an event property.
  * Removing the parent property from the tracking plan automatically removes all the nested properties.
  * You **cannot** nest properties within a property having both Array and Object data types. An example of such a property is shown:

[![Add nested property to tracking plan](/docs/images/data-governance/tracking-plans/add-nested-property-4.webp)](</docs/images/data-governance/tracking-plans/add-nested-property-4.webp>)

#### Use case for tracking plan created from source

For tracking plans created using the [Pull from source](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/#pull-from-source>) option, RudderStack populates the events and properties based on the schema sampled from your incoming events.

You can define up to three levels of nesting within an event property of Object or Array data type.

For example, consider the following event payload:
    
    
    {
      "type": "track",
      "event": "Product Viewed",
    
      ...
    
      "properties": {
        "products": [{
            "name": "Product 1",
            "product_id": "a123"
          },
          {
            "name": "Product 2",
            "product_id": "a124"
          }
        ],
        "filters": {
          "value": {
            "price": {
              "max": 10000
            },
            "rating": {
              "max": 5,
              "votes": {
                "min": 1000
              }
            }
          }
        },
      },
      ...
    }
    

Upon importing the above event in your tracking plan, you will see the following levels of nested properties within the `filters` and `products` properties:

[![Map properties for the tracking plan](/docs/images/data-governance/event-property-mapping-add-property.webp)](</docs/images/data-governance/event-property-mapping-add-property.webp>)

RudderStack will not show the property `min` nested within `votes` as it exceeds the third level of nesting.

## Share event spec pages

RudderStack supports sharing the spec for a tracking plan event across different workspace members for easier collaboration.

  1. Go to **Govern** > **Tracking Plans**.
  2. Click the tracking plan and select the event.
  3. Copy the URL and share it with your workspace members.

[![Shareable event spec](/docs/images/data-governance/tracking-plans/shareable-event-spec.webp)](</docs/images/data-governance/tracking-plans/shareable-event-spec.webp>)

This shareable page contains the following event details:

  * Event name and type

  * Property details like:

    * Property name and data type.
    * Whether it is required or optional, and
    * Details of the nested properties, if any.


> ![info](/docs/images/info.svg)
> 
> You will also see this view once you create or update the schema for that tracking plan event.

## View source-specific settings

Go to the source connected to the tracking plan to see the following settings in the **Tracking Plans** tab:

[![Unlink tracking plan from source](/docs/images/data-governance/manage-tracking-plan.webp)](</docs/images/data-governance/manage-tracking-plan.webp>)

  * **Unlink Tracking Plan** : Lets you unlink the tracking plan from your source.

  * **Previously linked tracking plans** : Lets you view the previously linked tracking plans for a source (in the last 30 days).

  * **Tracking plan settings** : Lets you edit the following tracking plan settings for each event type for the connected source. Once done, click **Save Settings** for the changes to take effect:

    * **Drop events with unplanned event names** : When toggled on, RudderStack drops all events that do not match the predefined event names in the tracking plan (only applicable for `track` events).
    * **Drop events with unplanned event properties** : When turned on, RudderStack drops all events that contain properties not matching the list of predefined properties for the specific event.
    * **Drop events with other violations** : When toggled on, RudderStack drops all events with violations that include Type Mismatch, Required Fields Missing, and others outlined in the [Violation types](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) section.
    * **Propagate errors** : When turned on, RudderStack captures the validation errors in the event’s `context` object and sends them downstream (user transformations, destinations), depending on your use-case. If toggled off, RudderStack drops the event containing the validation errors. It is recommended to keep this setting toggled on as it helps you assess the performance of your tracking plans.