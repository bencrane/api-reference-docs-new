# Zoho Configuration Settings Beta

Advanced configuration settings for Zoho destination.

* * *

  * __2 minute read

  * 


This guide lists the advanced configuration settings to receive the data correctly in Zoho.

## Configuration settings

  * **Zoho module** : Specify the object you selected while [setting up the mappings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/#set-up-connection>).
  * **Add Zoho-defined duplicated check fields as the secondary duplicate check fields** : Toggle on this setting to use the field specified in the [**Choose identifier**](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/>) setting as the primary key for deduplicating records.


> ![info](/docs/images/info.svg)
> 
> By default, Zoho provides a system-defined field to be used as a primary key. However, it also supports setting more than one field as the primary key for checking duplicate records.
> 
>   * When you toggle on this setting, Zoho uses the field specified in the [**Choose identifier**](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/#set-up-connection>) setting as the primary key and ignores the system-defined field.
>   * When you toggle off this setting, Zoho uses both the system-defined field along with the field specified in **Choose identifier** as the primary key.
> 


  * **Trigger action** : Select the Zoho trigger option from the dropdown.


> ![info](/docs/images/info.svg)
> 
> Zoho lets you set multiple trigger options and define which triggers to fire for a particular sync.
> 
>   * If you do not want any triggers to fire, choose **None**.
>   * To fire all triggers configured for your account, choose **Default**.
>   * To fire a specific trigger, choose one of **workflow** , **approval** , or **blueprint** as per your requirement.
> 


## Field level specification

Any Zoho module has some fields that can store multiple values. Using the [Zoho API calls](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/#supported-apis>), you can append a value to an existing value in the record or replace it completely.

In this section, select the **Zoho Multi Select Picklist Type Fields** corresponding to the Zoho module you chose while [specifying the mappings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/#set-up-connection>). Then, map it to the **Multiselect Field Action** setting which provides two options - **true** or **false**.

  * If you select **true** , RudderStack appends the new value from the sync to the existing value in the record.
  * If you select **false** , RudderStack replaces the existing value with the new value.

[![](/docs/images/reverse-etl-destinations/zoho-action-mapping.webp)](</docs/images/reverse-etl-destinations/zoho-action-mapping.webp>)

For example, suppose there is an existing field in Zoho called `known_languages` that contains the value `English`. You send the field (`known_languages`) in a particular sync with a different value `German` and specify it in the **Zoho Multi Select Picklist Type Fields** dropdown.

  * If **Multiselect Field Action** is set to **true** , Zoho stores both `English` and `German` values for the `known_languages` field.
  * If **Multiselect Field Action** is set to **false** , Zoho stores only `German` as the value for the `known_languages` field.