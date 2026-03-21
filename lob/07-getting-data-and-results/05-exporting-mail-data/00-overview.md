# Exporting mail data

Lob captures data for each mailpiece created and provides an easy way to export it as a CSV file. Exporting data allows for in-depth performance analysis, auditing, or other purposes, but we strongly recommend customers do this on a regular cadence for record-keeping and maintenance.&#x20;

{% hint style="warning" %}
Lob’s will retain customer mailpiece data for a total period of ninety (90) days. See our [data retention policy](https://help.lob.com/print-and-mail/getting-data-and-results/broken-reference) for further information.
{% endhint %}

## Data available for download

<table data-header-hidden><thead><tr><th width="141"></th><th></th></tr></thead><tbody><tr><td><strong>Mailpiece details</strong></td><td>ID, Description, URL, Color, Double Sided, Address Placement, Return Envelope, Perforated Page, Extra Service, Expected Delivery Date, Tracking Number, Mail Type, Size, Metadata, Date Created, Send Date, Merge Variables</td></tr><tr><td><strong>Sender details</strong></td><td>To.ID, To.Description, To.Name, To.Company, To.Phone, To.Email, To.Address Line1, To.Address Line2, To.Address City, To.Address State, To.Address Zip, To.Address Country, To.Metadata, To.Date Created</td></tr><tr><td><strong>Recipient details</strong></td><td>From.ID, From.Description, From.Name, From.Company, From.Phone, From.Email, From.Address Line1, From.Address Line2, From.Address City, From.Address State, From.Address Zip, From.Address Country, From.Metadata, From.Date Created</td></tr><tr><td><strong>Tracking events (if applicable)</strong></td><td><p><strong>Regular Mail</strong>: Mailed, In Transit, In Local Area, Processed for Delivery, Re-Routed, Returned to Sender <br></p><p><strong>Certified Mail</strong>: Mailed (Certified), In Transit (Certified), In Local Area (Certified), Processed for Delivery (Certified), Re-Routed (Certified), Returned to Sender (Certified), Delivered (Certified), Pickup Available (Certified), Issue (Certified)</p></td></tr></tbody></table>

## Exporting your data from the Lob dashboard

1. [Log in](https://dashboard.lob.com/login) to your Lob dashboard.
2. In the left side menu of your dashboard, navigate to the appropriate mail format for which you'd like to download your data (e.g., "Postcards.")

3\. Select the [environment](https://help.lob.com/account-management/api-keys#test-vs-live-environment-keys-2) (Live or Test) from which to download your data. In our example below, "Test" environment is selected.

{% hint style="info" %}
Recall that physical mail is only sent when requests are made in the Live Environment.
{% endhint %}

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FcJu0xxi1BKP6dXTvED5E%2Fexport_select.png?alt=media\&token=140577ab-3e0b-4707-9a4d-bf5082eb9e1e)

4\. Filter for the date range you want mailing details.&#x20;

This search is inclusive, i.e., the first date that will have information retrieved will be the Start Date from 00:00 UTC, and the last day of information returned will be the End Date up until 23:59 UTC.&#x20;

{% hint style="info" %}
If you are retrieving multiple years' worth of data, we recommend that you download one year at a time, as larger requests will require more time to generate.&#x20;

**Note that we have a limit of 250K rows per export at this point in time.**
{% endhint %}

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FnpH9JRl69NVyriIHEc9U%2Ftracking_filters.png?alt=media&#x26;token=024e1f5e-3ec8-4010-b7e6-692166d330b9" alt="" width="563"><figcaption></figcaption></figure>

5\. Once you have your filters selected, click "Apply" to filter on the range being displayed.

6\. From this newly filtered view, select the "Export" button.

* **Export Tracking events:** If you are exporting Live environment requests, and there are tracking events associated with them, a pop-up will appear to "Select Tracking Events." If you choose Yes, you will receive a second export of tracking events. You will have the option to include all events or a specific subset of events. Click "Submit."

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FqyXmGjHFW9yZ3f8PuWsy%2Ftracking_export.png?alt=media&#x26;token=7a888ef8-3034-4340-b026-d9550865d294" alt="" width="375"><figcaption></figcaption></figure>

* A pop-up will show your data selections for the **Product, Mode**, and **Date Range** parameters. If you have selected to receive an additional CSV of tracking events, this will be noted. Once you are satisfied with your data selections, hit the “Confirm” option on the bottom right.  Examples:

| Test data export - no tracking events                                                                                                                                                                                                                                      | Live data export - with tracking events                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FnLuTS4PGsptgDbkQRPSv%2Ftracking_confirm_test.png?alt=media&#x26;token=ddad95c3-677e-4605-92c5-e5b35c9bc5a2" alt="" data-size="original"> | <img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FyLClv2YQ0cMAo1UhiLrO%2Ftracking_confirm.png?alt=media&#x26;token=82cead47-e66d-4866-8087-02bfca29895d" alt="" data-size="original"> |

7\. You will be emailed an export link to the report that you just requested. (This will be emailed to the user who is logged into the Lob dashboard making the request.)

<table><thead><tr><th width="292">Data export examples</th><th>Email examples</th></tr></thead><tbody><tr><td>Test environment data export with no tracking events</td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FrGv3pDLkYzV66I18NhRu%2FScreen%20Shot%202022-12-21%20at%204.23.01%20PM.png?alt=media&#x26;token=cdd3dba9-36f9-462c-af03-1c3fc3d215d0" alt=""></td></tr><tr><td>Live environment data export with tracking events</td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F9YGgaTokvdsMdboGvrpA%2F10?alt=media" alt="" data-size="original"></td></tr></tbody></table>

## **Video walkthrough**

{% embed url="<https://lob.wistia.com/medias/ybxnsi18lt>" %}

If you have any questions regarding exporting your data, reach out to your Customer Success Manager or to <support@lob.com>.&#x20;