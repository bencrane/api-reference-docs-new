# Data Catalog Properties

Create and manage properties in your Data Catalog.

* * *

  * __7 minute read

  * 


This guide walks you through creating and managing your properties in the Data Catalog.

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to manage event properties in the Data Catalog.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the following [permission](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) in their workspace policy:

Resource| Permission| Description  
---|---|---  
Data Catalog| **Edit**|  Make changes to the configuration of Data Catalog  
  
**Click here to see how these permissions appear in the workspace policy**.  
![Data Catalog permissions to manage properties](/docs/images/access-management/data-catalog-permissions.webp)  


#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to manage the Data Catalog
  * Members must have the **Connections Admin** role in their workspace policy to manage the Data Catalog

[![Data Catalog permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)](</docs/images/access-management/tracking-plan-permissions-legacy-framework.webp>)

## Add property

RudderStack provides two ways of creating and adding properties to your Data Catalog:

  * In the Data Catalog itself
  * While editing your tracking plan


### In Data Catalog

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com/>) and go to **Govern** > **Data Catalog** option in the left sidebar.
  2. Go to the **Properties** tab, click **Add property**.

[![Add new property](/docs/images/data-governance/data-catalog-add-property.webp)](</docs/images/data-governance/data-catalog-add-property.webp>)

  3. In the **Property details** tab, specify the property name and description.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You cannot set a blank property name - it must be at least 1 character long.
> 
>   * RudderStack supports all the UTF-8 characters in property names.
> 
>   * The property name can start with a letter, number, or special character. Some examples of valid property names:
> 
>     * `test_property`
>     * `1test_property`
>     * `@1Ttest property`
> 


  4. Choose the data type for your property from the dropdown. You can also:

     * Choose multiple data types as per your requirement.
     * Leave this field empty to accept any data type.
     * Select a custom data type for the property.

[![Add new property to catalog](/docs/images/data-governance/add-new-property-to-catalog.webp)](</docs/images/data-governance/add-new-property-to-catalog.webp>)

  5. If you choose **Array** from the dropdown, select the data type of its elements in the **Array of** field . For example, if you choose **String** , RudderStack accepts only string elements for that array.

[![Array property type](/docs/images/data-governance/array-property-type.webp)](</docs/images/data-governance/array-property-type.webp>)

  6. Click **Save** to save the changes and add the new property to your Data Catalog.


### While editing a tracking plan

You can also create a new property while [adding a new event schema](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#add-a-new-event-schema>) or [updating an existing event schema](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#update-an-existing-event-schema>) for your tracking plan.

  1. Go to **Govern** > **Tracking Plans** to see all the tracking plans in your workspace. Then, click a tracking plan.
  2. Click the meatballs menu (`...`) next to an event and click **Edit event schema**.
  3. Click the **Add properties** button.

[![Add new property](/docs/images/data-governance/tracking-plans/add-properties.webp)](</docs/images/data-governance/tracking-plans/add-properties.webp>)

  4. In the right panel, click **Create new property**.
  5. Specify the property name, description, and data type.
  6. Click **Create property**.

[![Create new property](/docs/images/data-governance/tracking-plans/create-new-property.webp)](</docs/images/data-governance/tracking-plans/create-new-property.webp>)

### Add multiple properties with the same name

You can create multiple properties with the same name as long as:

  * They have a different data type, OR
  * In case of arrays, they have different **Array of** values. For example, if you create a property called `test_property` of the array data type and the **Array of** field set to **String** , as shown:

[![Add multiple properties with same name](/docs/images/data-governance/multiple-properties-name.webp)](</docs/images/data-governance/multiple-properties-name.webp>)

In that case:

  * You can create another property called `test_property` with a different data type, for example, Integer.
  * You can create another property called `test_property` with an array data type and a different **Array of** field setting, for example, Boolean and String.
  * You **cannot** create another property called `test_property` with an array data type and the **Array of** field set to String.


## Property details

Once created, you can click the property to see the following information:

  * Property details like name, description, and data type. You can also make any changes to these details - make sure to click **Save** for any changes to take effect.
  * Connections to tracking plans, along with the connected sources and associated events (only visible after you map the property to an event while creating a tracking plan).
  * Delete property from Data Catalog. Note that you **cannot** delete any property from the catalog if it is already a part of any tracking plan.

[![Add new property](/docs/images/data-governance/view-property.webp)](</docs/images/data-governance/view-property.webp>)

## Set advanced rules for a property

While adding or editing a property, use the **Advanced rules** tab to add rules that define how RudderStack should capture a property.

> ![info](/docs/images/info.svg)
> 
> You can set advanced rules for properties of all the data types except **Object** and **Null**.

You can define the following advanced rules for the property depending on its data type:

  * **Enum** : Define the acceptable values for the property.

![Define the acceptable values for the property](/docs/images/data-governance/advanced-rules-enum.webp)

  * **Format** : Define the acceptable format in which the property values should be captured. RudderStack supports the below formats:

    * date-time
    * date
    * time
    * email
    * hostname
    * ipv4
    * ipv6
    * uuid

![Define the property format](/docs/images/data-governance/advanced-rules-format.webp)

  * **Pattern** : Define the property constraints using regular expressions. RudderStack supports the below patterns:

    * Email
    * Date-time (`YYYY-MM-DDTHH:MM:SS`)
    * Date (`YYYY-MM-DD`)
    * Time (`HH:MM:SS`)
    * URL
    * IPv4
    * IPv6
    * Custom (define a custom pattern)

![Define the property constraints via patterns](/docs/images/data-governance/advanced-rules-pattern.webp)

  * **Minimum/maximum length** : Define the acceptable string length for the property.

![Define the property string length](/docs/images/data-governance/advanced-rules-length.webp)

  * **Enum** : Define the acceptable values for the property.

![Define the acceptable values for the property](/docs/images/data-governance/advanced-rules-num-enum.webp)

  * **Minimum/Maximum** : Define the range acceptable for the property.

![Define the min/max range for the property](/docs/images/data-governance/advanced-rules-minmax.webp)

  * **Exclusive Minimum/Maximum** : Define the exclusive range acceptable for the property.

![Define the acceptable exclusive min/max range for the property](/docs/images/data-governance/advanced-rules-excl-minmax.webp)

  * **Multiple Of** : Define a number whose multiples are the only acceptable values for this property.

![Define the acceptable multiples for the property](/docs/images/data-governance/advanced-rules-multipleof.webp)

  * **Minimum/Maximum items** : Define the minimum and maximum number of items acceptable for this property.

![Define the acceptable number of items for the property](/docs/images/data-governance/advanced-rules-minmax-array.webp)

  * **Unique items** : Specify whether RudderStack should accept arrays with only unique items. To do so, turn on the **Allow unique items** toggle.

![Define unique items setting for the property](/docs/images/data-governance/advanced-rules-unique.webp)

  * **Enum** : Define the acceptable values for the property.

![Define the acceptable values for the property](/docs/images/data-governance/advanced-rules-enum.webp)

## Custom data types

> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Closed Beta** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/beta-features/closed-beta/>), where we work with early users and customers to test new features and get feedback before making them generally available.
> 
> [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

  


You can use the **Custom Data Types** tab to set predefined rules and later apply them to multiple event properties as per your requirement. With this approach, you can avoid setting the same set of advanced rules to each property individually.

This section highlights the steps for adding a custom type in your Data Catalog and then defining a new property to use that custom type.

### Define custom types

  1. Go to the **Properties** tab of the Data Catalog and click the **Custom Data Types (beta)** tab. Then, click **Add custom type**.

[![Add custom data type](/docs/images/data-governance/add-custom-type.webp)](</docs/images/data-governance/add-custom-type.webp>)

  2. Specify the name, description, and data type under **Type details** :


> ![warning](/docs/images/warning.svg)
> 
> The custom type name must be between 2 and 65 characters long. Also, it must start with a capital letter and contain only letters, numbers, underscores and dashes. Spaces are **not** allowed.

[![Define custom type](/docs/images/data-governance/define-custom-type.webp)](</docs/images/data-governance/define-custom-type.webp>)

  3. Go to the **Rules** tab and define the rules for the data type selected above. An example for a string is shown below:

[![Define custom type rules](/docs/images/data-governance/define-custom-type-rules.webp)](</docs/images/data-governance/define-custom-type-rules.webp>)

  4. Click **Save** to save the changes.


### Examples

This section highlights some specific use cases of creating new custom types in your Data Catalog.

#### Create a custom type that is an array of other custom types

You can create a custom type that is an array of another custom type, that is, it accepts only a list of that custom type.

  1. Specify the name and description (optional) of the custom type.
  2. Under **Type** , select **Array**.
  3. Under **Array of** , select **Custom data type (beta)**.
  4. Select the required **Custom data type**.
  5. Specify the rules for this new array custom type, as required.


The following image highlights a custom type named `ArrayCustomType` that is an array of another custom type `StringCustomType`.

[![Define array of custom types](/docs/images/data-governance/new-custom-type-array.webp)](</docs/images/data-governance/new-custom-type-array.webp>)

Note that you can specify **only one** custom type in the **Array of** field, as seen in the above image.

#### Create an object custom type that accepts specific properties

You can create a custom data type of object type that **only accepts** specific properties present in your Data Catalog:

  1. Specify the name and description (optional) of the custom type.
  2. Under **Type** , select **Object**.
  3. Select the required properties present in your Data Catalog in the **Properties** field.
  4. Mark the properties as **Optional** or **Required** , as per your requirement.

[![Define object custom type](/docs/images/data-governance/object-custom-type.webp)](</docs/images/data-governance/object-custom-type.webp>)

### Create new properties using custom types

  1. In the **Properties** tab of the Data Catalog, click **Add property**.

[![Add new property](/docs/images/data-governance/data-catalog-add-property.webp)](</docs/images/data-governance/data-catalog-add-property.webp>)

  2. Enter the property name and description.
  3. Under **Data type** , select **Custom data type (beta)**. Then, select the custom data type defined in Step 1 above.

[![Select custom data type for property](/docs/images/data-governance/add-property-data-type.webp)](</docs/images/data-governance/add-property-data-type.webp>)

Once you select the custom data type, the property automatically inherits all the rules that you defined while creating the custom data type.

[![Custom data type applied property](/docs/images/data-governance/add-property-custom-type-details.webp)](</docs/images/data-governance/add-property-custom-type-details.webp>)

#### Create a property that accepts an array of a custom type

You can create a new property that accepts an array of a custom data type.

  1. Specify the property name and description (optional).
  2. Choose **Data type** as **Array**.
  3. Set the **Array of** field to **Custom data type (beta)**.
  4. Select the required **Custom data type**.
  5. Set the **Property rules** , as required.


The following image highlights a new property called `products_array` that is an array of a custom type `StringCustomType`:

[![Define array of custom data type](/docs/images/data-governance/array-custom-type.webp)](</docs/images/data-governance/array-custom-type.webp>)