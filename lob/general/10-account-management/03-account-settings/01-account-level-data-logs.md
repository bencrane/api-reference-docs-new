# Account-level data logs

### Webhooks <a href="#webhooks-7" id="webhooks-7"></a>

Webhooks are an easy way to get notifications on events happening asynchronously within Lob's architecture. You can view, create, and debug webhooks on the Lob dashboard, as well as view subscribed events. Note that in Live mode, you can only have as many non-deleted webhooks as allotted in your current Print & Mail Edition. There is no limit in Test mode.

See our [Webhooks integration guide](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks) for more details on how to integrate.&#x20;

See the full list of [event types available](https://docs.lob.com/#tag/Events) for subscription in our API documentation.

### Audit logs  <a href="#audit-logs-8" id="audit-logs-8"></a>

All actions available through the dashboard's settings panel are recorded in the [Logs](https://dashboard.lob.com/settings/logs) section, which can be fully accessed by admins in Enterprise-level accounts. Only API logs for the past 30 days are saved as they are meant for simple real-time debugging.&#x20;

Click on the '**+**' sign for any user row at the right side of the screen to see more details, or click on the Filter button at the top to narrow your search for specific audit logs, such as:&#x20;

* Action
* Associated user
* IP address
* User agent
* Time stamp (UTC)

<details>

<summary>Recorded actions</summary>

* Changed the account's address
* Changed the account's bank account
* Changed the account's credit card
* Changed the SAML configuration
* Changed the account's company name
* Changed the account's deliverability strictness
* Changed the account's merge variable strictness
* Changed the account's cancellation window for checks
* Changed the account's cancellation window for letters
* Changed the account's cancellation window for postcards
* Redeemed a code
* Logged in
* Downgraded the Print & Mail edition
* Downgraded the Address Verification plan
* Downgraded the support plan
* Upgraded the Print & Mail edition
* Upgraded the Address Verification plan
* Upgraded the support plan
* Joined
* Deleted a team member
* Invited a user
* Reset their password
* Resent a team invite
* Requested a password reset
* Changed their password
* Changed their email address
* Changed a user's role
* Changed their name
* Verified their email address

</details>

### NCOA export <a href="#ncoa-export-10" id="ncoa-export-10"></a>

National Change of Address (NCOA) is a service offered by the USPS, which allows individuals or businesses who have recently moved to have any mail forwarded from their previous address to their new address.

As a CASS-certified address verification provider, Lob also offers NCOA functionality to our Print & Mail customers. With the Lob NCOA feature enabled, postcards, self-mailers, letters, checks and addresses can automatically be corrected to reflect an individual's or business' new address in the case that they have moved (only if they have registered an NCOA with the USPS).

For Enterprise edition accounts with NCOA enabled, Lob generates a weekly report of suppressed API response data for addresses that have been changed through NCOA. These reports can be downloaded in the dashboard under the [Reporting tab](https://dashboard.lob.com/settings/reporting). In order to gain access to and download NCOA'd data, customers must send **at least** **100 addresses** within a single USPS-defined 'week' period.

Read more on the [NCOA functionality](https://help.lob.com/print-and-mail/reaching-your-audience/all-about-addresses#national-change-of-address-ncoa-7) offered by Lob.

### Event logs <a href="#event-logs-11" id="event-logs-11"></a>

Event logs are records of the mail piece events associated to your account's API submissions.

Within the [Event logs](https://dashboard.lob.com/events) section use the filter to select a date range, a resource type, and desired event type to generate a list of Reference IDs that apply to the selected criteria.&#x20;

While it is also possible to go to any resource type (postcards, letters, checks, etc.) in the left menu of the dashboard and export all selected tracking events in a CSV file, the Event Logs section is currently the only place where you can generate tracking events for return envelopes. &#x20;

See [Mail data & tracking](https://help.lob.com/print-and-mail/getting-data-and-results/tracking-your-mail) for more information.

### API logs <a href="#api-logs-12" id="api-logs-12"></a>

API logs are records of your requests, tied to the specific information you provided for the submission.&#x20;

Use the filter to select a date range, reference ID, path, method, or status code which will generate a list of API logs that apply to the selected criteria. Click on any API log to view more details, including the request post body and response body.

If you are looking for more context behind any error codes you have received, check the response body in the API logs for detailed error messages. You can also see the [full list of error messages](https://docs.lob.com/#tag/Errors) in our API documentation.   &#x20;

We only save API logs for the preceding 30 days, as they are meant for simple real-time debugging.