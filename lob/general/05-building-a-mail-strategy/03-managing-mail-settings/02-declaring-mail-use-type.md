# Declaring mail use type

## Overview

Identifying your mail **use type** helps Lob populate the right mail settings and postage options to ensure your mail is produced and delivered in an optimal way. Lob requires that you identify—or tag—your mail with one of the following use type options:

* **Marketing mail**: Any mailers that are sent for marketing, advertising, and promotional purposes
* **Operational mail**: All other mail, typically transactional or functional in nature, such as invoices, adverse action notices, statements, and other confidential mail that include sensitive PII/PHI data

{% hint style="success" %}
It will be your full responsibility to accurately represent the purpose of mail that is created and sent. Lob will be unable to make any determination of which use type should be applied to your mail being sent, or for making retroactive changes to your API calls.
{% endhint %}

## How to declare your mail use type

You should declare your mail’s use type at the appropriate level based on your organization's usage (at the account, campaign, or mailpiece level).&#x20;

### 1. Setting use type for an account (default) <a href="#id-1-setting-use-type-as-an-account-default-3" id="id-1-setting-use-type-as-an-account-default-3"></a>

If the majority of your mailpieces have a singular use type, then it is best to configure a default use type at the account level. This can be changed by an account administrator in the Use Type section in the [Accounts Tab in the dashboard settings](https://dashboard.lob.com/settings/account). **An account-level setting will be applied to any mailpiece created without a `use_type` at the individual mailpiece or campaign level.**

{% hint style="warning" %}
While an account-level designation is not required, the failure to declare a mail use type at *any* level means that in the absence of a default value, your organization will be prevented from sending any mail until a use type is declared.&#x20;
{% endhint %}

To set an account-level default, go to your [Dashboard Settings > Accounts](https://dashboard.lob.com/settings/account) tab:

<figure><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/2094102/Screen_Shot_2022-07-05_at_5.32.22_PM.png" alt=""><figcaption></figcaption></figure>

### 2. Setting use types for each mailpiece <a href="#id-2-setting-use-types-for-each-mailpiece-4" id="id-2-setting-use-types-for-each-mailpiece-4"></a>

If you or your team sends mailpieces with varying use types (including different teams that utilize the same Lob account for different purposes), then it is best to declare your use types at the single mailpiece level or at the campaign level.  &#x20;

If you have built a native Lob integration to trigger individual mailpieces, you will want to configure a use type at the individual mailpiece level. **A mailpiece designation will override your account-level use type, regardless of whether the default selection is made.**&#x20;

#### **In the Dashboard**

When sending a single mailpiece through the dashboard, use type will be a required selection for every mailpiece format ([letters](https://dashboard.lob.com/letters/create), [postcards](https://dashboard.lob.com/postcards/create), [self-mailers](https://dashboard.lob.com/self-mailers/create), or [checks](https://dashboard.lob.com/checks/create)).

**Example:** Use Type selection when creating a new [postcard](https://dashboard.lob.com/postcards/create) in the Dashboard

<figure><img src="https://lh3.googleusercontent.com/lU3KZtIBL1i7ex8hQ7oSaJmLdeS-M1qAaDsAoL8_9tYfpSc2Nd-Jz8WS9GiVt673q9L0yViRCQc-Cz9N1bKFwPg9Lj7BU8NKKovIQVkH2QSBTmObLYSOO0aOHoNzSyYN-DcOp-oWlrDtaW_XV8Mw6Y4kTvbiY1JJoMPryBTI7R1KPLI9x-M3-7WFtwbQ8BMU=nw" alt=""><figcaption></figcaption></figure>

#### **In the API**

When sending a `POST` request to the below endpoints, pass in a `use_type` value of either `marketing` or `operational`. Note that the account default will be overridden by passing in a `use_type` for each mailpiece. If no account default is set and no single endpoint-level `use_type` is passed in the request, the mailpiece cannot be created and will fail with a 422 error.

`api.lob.com/v1/letters`\
`api.lob.com/v1/postcards`\
`api.lob.com/v1/self_mailers`\
`api.lob.com/v1/checks`

Example: `POST /v1/postcards` request with `use_type` included

```html
{
    "description": "demo",
    "to": "adr_42bb83a3a643c43f",
    "from": "adr_42bb83a3a643c43d",
    "front": "tmpl_a1234dddg",
    "back": "tmpl_a1234dddg",
    "size": "6x9",
    "mail_type": "usps_first_class",
    "use_type": "operational",
    "send_date": "2022-05-01T00:00:00.000Z"
} 
```

### 3. Setting use types for each campaign <a href="#id-3-setting-use-types-for-each-campaign-7" id="id-3-setting-use-types-for-each-campaign-7"></a>

The Campaigns product is designed to help send large volumes of mail quickly, either through the [dashboard](https://dashboard.lob.com/campaigns) or [Campaigns API](https://docs.lob.com/#tag/Campaigns).&#x20;

If you have built a native Lob integration to send mail campaigns, you will want to configure a use type at the campaign level. **A campaign-level designation will override your account-level mail use type, regardless of whether the default selection is made.**&#x20;

#### **In the Dashboard**

When sending a Campaign on the dashboard, selecting a campaign use type is a required step during the “[Configure campaign](https://dashboard.lob.com/campaigns/create/settings)” page in Step 1. You will be able to select one of two options: Marketing or Operational. Any selection will be applied to all mailpieces within the same campaign.

Example:

<figure><img src="https://lh3.googleusercontent.com/6fyIxk7fS35qtckIh6UByNcQf9owJyzzDvBibsIbyDA3gpHBlZFvvlbdC1B_DicLE_pMjsAgjSdSkrEyqvzwejis1I7CoyrVRfb9a8yu5XgMI0HdwYi0EPzKjS70iHtPFbQeNBVouLYJhPVeFLE_RKvFExAv0xnT1MXLOV4r0o3zyRuqmEv30Rf058HQvVWC=nw" alt=""><figcaption></figcaption></figure>

#### **In the API**

When using the [Campaigns API](https://docs.lob.com/#tag/Campaigns), add the `use_type` field to the `POST /v1/campaigns` request. If the `use_type` is not added, the campaign will use the account default `use_type`. If no account default is set and no campaign-level `use_type` is passed in the request, the campaign cannot be created and will fail with a 422 error.

Example: `POST /v1/campaigns` request with `use_type` included

```html
{
    "name": "Summer Campaign",
    "description": "Acquisition for new customers",
    "schedule_type": "immediate",
    "cancel_window_campaign_minutes": 40,
    "use_type": "marketing"
}
```

## Error reference

If no account default is set and no campaign or mailpiece `use_type` field is passed in your API requests, your calls will fail with a 422 error.  &#x20;

Read more about [error codes](https://docs.lob.com/#tag/Errors) under the "Error Codes - Advanced" section of our API Reference.

{% hint style="danger" %}
To ensure your mail sends do not fail in the future, we strongly recommend you **set an** **account default** as a fall-back option as soon as possible
{% endhint %}