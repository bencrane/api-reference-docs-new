# Send campaigns via the Campaigns API

{% hint style="info" %}
This functionality is in beta. Please reach out to <support@lob.com> or your Account Manager with any feedback or feature requests.&#x20;
{% endhint %}

Use our Campaigns API to send your large-scale direct mail campaign sends more programmatically.

When creating campaigns, you’ll interact with 3 main models: **campaigns**, **creatives**, and **uploads**.&#x20;

* The **campaigns** model is used to set up high-level information about your campaign
* The **creatives** model is used for uploading artwork and artwork settings for your campaign
* The **uploads** model is used to build your audience and configure any recipient-level details for your campaign

Follow the steps below to create your first campaign in the API.&#x20;

### Step 1: Create your campaign  <a href="#step-1-create-your-campaign-7" id="step-1-create-your-campaign-7"></a>

**Endpoint**: `POST api.lob.com/v1/campaigns`\
**Documentation**: [Create Campaign](https://docs.lob.com/#tag/Campaigns/operation/campaign_create)

First, create your campaign. At a minimum, your campaign needs a `name` and a `schedule_type` and a `use_type` if one has not been declared at the account level. It is highly recommended that a `cancel_window_campaign_minutes` is provided given it will allow you to cancel the campaign within the specified window if needed.

```json
{ 
    "name": "Demo Campaign",
    "schedule_type": "immediate",
    "use_type": "marketing",
    "cancel_window_campaign_minutes": "120"
}
```

### Step 2: Add creative <a href="#step-2-add-creative-8" id="step-2-add-creative-8"></a>

**Endpoint**: `POST api.lob.com/v1/creatives`\
**Documentation**: [Create Creatives](https://docs.lob.com/#tag/Creatives/operation/creative_create)

The next step is to create your creative object that will be associated with the campaign. You can only associate a single creative with a campaign. You are required to add a `campaign_id`, `resource_type`, and any requirements for your selected `resource_type`. This payload is subject to change depending on your form factor. See examples below.

{% tabs %}
{% tab title="Postcard" %}

```json
{ 
    "campaign_id": "campaign_id",
    "resource_type": "postcard",
    "front": "{{pdf || url || template_id}}",
    "back": "{{pdf || url || template_id}}",
    "details": {
        "size": "4x6",
        "mail_type": "usps_standard_class",
    }
}
```

{% endtab %}

{% tab title="Letter" %}
Note: the `details` section has additional optional parameters, [see docs for more info.](https://docs.lob.com/#tag/Creatives/operation/creative_create)

```json
{ 
    "campaign_id": "campaign_id",
    "resource_type": "letter",
    "file": "{{pdf || url || template_id}}",
    "from": {
        "name": "Lob.com",
        "address_line1": "210 King St.",
        "address_city": "San Francisco",
        "address_state": "CA",
        "address_zip": "94107"
    }
    "details": {
        "color": true,
        "mail_type": "usps_standard_class"
    }
}
```

{% endtab %}
{% endtabs %}

### Step 3: Map columns from your data file to specified fields <a href="#step-3-create-your-upload-object-9" id="step-3-create-your-upload-object-9"></a>

**Endpoint**: `POST api.lob.com/v1/uploads`\
**Documentation**: [Create Upload](https://docs.lob.com/#tag/Uploads)

Uploading your audience data file is the next step. Step 3 can be done prior to Step 2 as well. For more information on how to best structure your upload for Steps 3 and 4, visit our [campaign audience guide](https://help.lob.com/print-and-mail/reaching-your-audience/campaign-audience-guide).&#x20;

If using `optionalAddressColumnMapping`, all fields must be specified (which means unused fields must be declared with a `null` value). If you're using an HTML template, double check that you have provided all keys and values for `mergeVariableColumnMapping`, if not all merge variables are mapped, your campaign will not be executable when it comes time to send.

```json
{
    "campaignId": "{{campaign_id}}",
    "requiredAddressColumnMapping": {
        "name": "recipient",
        "address_line1": "address_line1",
        "address_city": "address_city",
        "address_state": "address_state",
        "address_zip": "address_zip"
    },
    "optionalAddressColumnMapping": {
        "address_line2": "address_line2",
        "company": null,
        "address_country": null
    },
    "mergeVariableColumnMapping": {
        "date": "date",
        "firstName": "firstName",
        ...
        "qr_url": "qr_url"
    },
    "metadata": {
        "columns": [
            "email"
        ]
    }
}
```

### Step 4: Upload your file <a href="#step-4-upload-your-file-10" id="step-4-upload-your-file-10"></a>

**Endpoint**: `POST api.lob.com/v1/uploads/{{upload_id}}/file`\
**Documentation**: [Upload File](https://docs.lob.com/#tag/Uploads/operation/upload_file)

After creating your upload object, you can now upload your file as a byte stream (binary file).

```json
{ 
    "file": "{{file.csv}}"
}
```

### Step 5: Execute your campaign <a href="#step-5-validate-your-file-11" id="step-5-validate-your-file-11"></a>

**Endpoint**: `POST api.lob.com/v1/campaigns/{{campaign_id}}/send`\
**Documentation**: [Send Campaign](https://docs.lob.com/#tag/Campaigns/operation/campaign_send)

Finally, you can execute your campaign! To see the status of your mail pieces as they are created, use the `GET api.lob.com/v1/uploads/{{upload_id}}` endpoint.

```json
{
   "is_draft": "false"
}
```

### Step 6: Get failed addresses <a href="#step-7-export-failures-13" id="step-7-export-failures-13"></a>

**Endpoint**: `POST api.lob.com/v1/uploads/{{upload_id}}/exports`\
**Documentation**: [Create Export](https://docs.lob.com/#tag/Uploads/operation/upload_export_create)

First, let us know that you would like to create a failure export. Your response will include an export ID, which will be used to retrieve the export URL in the next step.&#x20;

```json
{
   "type": "failures"
}
```

**Endpoint**: `GET api.lob.com/v1/uploads/{{upload_id}}/exports/{{export_id}}`\
**Documentation**: [Retrieve Export](https://docs.lob.com/#tag/Uploads/operation/export_retrieve)

You can then retrieve the S3 URL of the export from the `GET` response above. Your export will include row-level details on why each record failed.

### Step 7: Cancel your campaign <a href="#step-8-cancel-your-campaign-14" id="step-8-cancel-your-campaign-14"></a>

**Endpoint**: `DELETE api.lob.com/v1/campaigns`\
**Documentation**: [Delete Campaign](https://docs.lob.com/#tag/Campaigns/operation/campaign_delete)

As long as your campaign cancellation window has not passed, you can [cancel](https://help.lob.com/building-a-mail-strategy/managing-mail-settings#cancellation-windows-4) your campaign using our `DELETE` route on the campaigns endpoint.&#x20;

And that's it! If you have any questions, feel free to reach out to your Customer Success Manager, or to <support@lob.com>.