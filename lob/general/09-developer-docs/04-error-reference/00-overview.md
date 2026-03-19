# Error reference

Lob utilizes response codes to indicate whether an API request has succeeded or failed.&#x20;

Lob uses both Standard RESTful [HTTP status codes](#http-status-codes-3) and custom response codes, which reflect specific Lob requirements or functionality. Lob’s error response contains a message parameter containing developer-facing information about the reason for failure.

{% hint style="info" %}
Live requests that result in a non-2XX code response are indicative of resource creation being stopped. That is, those requests do not incur a postage cost as no resource is created.
{% endhint %}

## Error handling <a href="#error-handling-0" id="error-handling-0"></a>

Handling particular error messages can be crucial in ensuring you have a robust integration with Lob. The main categories of error status codes are 4xx and 5xx. However, timeouts can also be viewed as an error in and of itself.

### 5XX codes & timeouts <a href="#id-5xx-codes-timeouts-1" id="id-5xx-codes-timeouts-1"></a>

5XX error codes indicate a server failure, as mentioned below, whereas timeouts are indicative of just that. A request did not receive a response in the allotted amount of time. Either way, the request sent to Lob may or may not have been properly received.&#x20;

To ensure that your request to Lob was successful, it is advisable to institute **retry logic** accordingly. When setting up this retry logic, it is essential to keep the following in mind:

* [Idempotency-keys](https://docs.lob.com/#section/Idempotent-Requests) will ensure your retry attempts are safe by checking that no unique mail piece is created more than once. It is crucial to use these keys to make sure you do not incur any undesired usage costs.
* Backoff logic should be utilized to allow the network time to recover in the event of a short outage. Lob has sub-second response times, which means if a timeout occurs, it is likely a network issue.
* 3-5 retry attempts are considered best practice.

### 4XX codes <a href="#id-4xx-codes-2" id="id-4xx-codes-2"></a>

4XX error codes indicate something about the request was invalid. In the case of Lob, we have custom response codes that should be handled accordingly.&#x20;

{% tabs %}
{% tab title="429" %}
This code is related to exceeding your rate limit. If this status code is received, you should have logic in place to back off all requests to this specific endpoint and resume attempts after 5 seconds. You can utilize the 3 rate limit headers in your retry logic.&#x20;

`ratelimit-remaining` - The number of requests remaining in the current window.\
`ratelimit-remaining` - The number of requests remaining in the current window.\
`ratelimit-reset` - The time at which the rate limit window resets in UTC epoch seconds.
{% endtab %}

{% tab title="404" %}
If you receive a 404 response code on a `GET` request, it is recommended that you attempt that request with proper retry logic in place, as you may be attempting to retrieve a resource that has yet to be created. Usually, within a minute, these errors are resolved.
{% endtab %}

{% tab title="401/403" %}
These error codes should be investigated as they relate to authentication issues. No retry attempts are necessary.&#x20;
{% endtab %}

{% tab title="Everything else" %}
Other than the cases above, all errors should be acted upon as you see fit. Ultimately, the error code you receive from Lob can help you take corrective action, but not retry attempts are needed as you will get the same error message each time.
{% endtab %}
{% endtabs %}

**Note: For fields that are intended to accept only string values, submitting JSON objects in string format (stringified JSON objects) is not supported.** Our system automatically parses and validates incoming data according to their expected types. As a result, providing a stringified JSON object in a field designated for string input can cause parsing errors or lead to unexpected validation results.

## HTTP status codes <a href="#http-status-codes-3" id="http-status-codes-3"></a>

<table data-header-hidden><thead><tr><th width="244.50248970644554"></th><th width="78.11901424636054"></th><th></th></tr></thead><tbody><tr><td>SUCCESS</td><td>200</td><td>Successful API request</td></tr><tr><td>UNAUTHORIZED</td><td>401</td><td>Authorization error with your API key or account</td></tr><tr><td>FORBIDDEN</td><td>403</td><td>Forbidden error with your API key or account</td></tr><tr><td>NOT FOUND</td><td>404</td><td>The requested item does not exist</td></tr><tr><td>BAD REQUEST</td><td>422</td><td>The query or body parameters did not pass validation</td></tr><tr><td>TOO MANY REQUESTS</td><td>429</td><td>Too many requests have been sent with an API key in a given amount of time. Learn more about Lob’s rate limits <a href="https://docs.lob.com/#tag/Rate-Limiting">here</a>.</td></tr><tr><td>SERVER ERROR</td><td>500</td><td>An internal server error occurred, please contact support@lob.com</td></tr></tbody></table>

## Error codes - generic <a href="#error-codes-generic-4" id="error-codes-generic-4"></a>

<table data-header-hidden><thead><tr><th width="282.3333333333333"></th><th width="100.4011071967791"></th><th width="385.2655594698876"></th></tr></thead><tbody><tr><td>FEATURE_LIMIT_REACHED</td><td>403</td><td>The account has reached its resource limit and requires upgrading to add more.</td></tr><tr><td>UNRECOGNIZED_ENDPOINT</td><td>404</td><td>The requested endpoint doesn't exist.</td></tr><tr><td>NOT_FOUND</td><td>404</td><td>The requested resource was not found.</td></tr><tr><td>REQUEST_TIMEOUT</td><td>408</td><td>The request took too long. Please try again.</td></tr><tr><td>CONFLICT</td><td>409/422</td><td>This operation would leave data in a conflicted state.</td></tr><tr><td>BAD_REQUEST</td><td>422</td><td>An invalid request was made. See error message for details.</td></tr><tr><td>INVALID</td><td>422</td><td>An invalid request was made. See error message for details</td></tr><tr><td>NOT_DELETABLE</td><td>422</td><td>An attempt was made to delete a resource, but the resource cannot be deleted.</td></tr><tr><td>UNSUPPORTED_LOB_VERSION</td><td>422</td><td>An unsupported Lob API version was requested.</td></tr><tr><td>INTERNAL_SERVER_ERROR</td><td>500</td><td>An error has occurred on Lob's servers. Please try request again.</td></tr><tr><td>SERVICE_UNAVAILABLE</td><td>503</td><td>The Lob servers are temporarily unavailable. Please try again.</td></tr></tbody></table>

## Error codes - authentication <a href="#error-codes-authentication-5" id="error-codes-authentication-5"></a>

<table data-header-hidden><thead><tr><th width="318"></th><th width="99.33333333333331"></th><th></th></tr></thead><tbody><tr><td>EMAIL_REQUIRED</td><td>401</td><td>Account must have a verified email address before creating live resources.</td></tr><tr><td>UNAUTHORIZED</td><td>401</td><td>The request isn't authorized.</td></tr><tr><td>UNAUTHORIZED_TOKEN</td><td>401</td><td>Token isn't authorized.</td></tr><tr><td>INVALID_API_KEY</td><td>401/403</td><td>The API key is invalid.</td></tr><tr><td>PUBLISHABLE_KEY_NOT_ALLOWED</td><td>403</td><td>The requested operation needs a secret key, not a publishable key. See <a href="https://docs.lob.com/#section/API-Keys">API Keys</a> for more information.</td></tr><tr><td>RATE_LIMIT_EXCEEDED</td><td>429</td><td>Requests were sent too quickly and must be slowed down. Learn more about Lob’s rate limits <a href="https://docs.lob.com/#tag/Rate-Limiting">here</a>.</td></tr></tbody></table>

## Error codes - advanced <a href="#error-codes-advanced-6" id="error-codes-advanced-6"></a>

<table data-header-hidden><thead><tr><th width="332.85552610300664"></th><th width="72.1360889126355"></th><th></th></tr></thead><tbody><tr><td>PAYMENT_METHOD_UNVERIFIED</td><td>401</td><td>You must have a verified bank account or credit card to submit live requests.</td></tr><tr><td>BILLING_ADDRESS_REQUIRED</td><td>403</td><td>In order to create a live mail piece, your account needs to have a <a href="../../account-management/billing#adding-a-corporate-billing-address">billing address</a>.</td></tr><tr><td>DELETED_BANK_ACCOUNT</td><td>404</td><td>Checks cannot be created with a deleted bank account.</td></tr><tr><td>ADDRESS_LENGTH_EXCEEDS_LIMIT</td><td>422</td><td>The sum of <code>to.address_line1</code> and <code>to.address_line2</code> cannot surpass 50 characters.</td></tr><tr><td>BANK_ACCOUNT_ALREADY_VERIFIED</td><td>422</td><td>The bank account has already been verified.</td></tr><tr><td>BANK_ERROR</td><td>422</td><td>There's an issue with the bank account.</td></tr><tr><td>CUSTOM_ENVELOPE_INVENTORY_DEPLETED</td><td>422</td><td>Custom envelope inventory is depleted, and more will need to be ordered.</td></tr><tr><td>FAILED_DELIVERABILITY_STRICTNESS</td><td>422</td><td>The to address doesn't meet strictness requirements. See <a href="https://dashboard.lob.com/settings/account">Account Settings</a> to configure strictness.</td></tr><tr><td>FILE_PAGES_BELOW_MIN</td><td>422</td><td>Not enough pages.</td></tr><tr><td>FILE_PAGES_EXCEED_MAX</td><td>422</td><td>Too many pages.</td></tr><tr><td>FILE_SIZE_EXCEEDS_LIMIT</td><td>422</td><td>The file size is too large. See description for details.</td></tr><tr><td>FOREIGN_RETURN_ADDRESS</td><td>422</td><td>The <code>from</code> address must be a US address.</td></tr><tr><td>INCONSISTENT_PAGE_DIMENSIONS</td><td>422</td><td>All pages of the input file must have the same dimensions.</td></tr><tr><td>INVALID_BANK_ACCOUNT</td><td>422</td><td>The provided bank routing number is invalid.</td></tr><tr><td>INVALID_BANK_ACCOUNT_VERIFICATION</td><td>422</td><td>Verification amounts do not match.</td></tr><tr><td>INVALID_CHECK_INTERNATIONAL</td><td>422</td><td>Checks cannot be sent internationally.</td></tr><tr><td>INVALID_COUNTRY_COVID</td><td>422</td><td>The postal service in the specified country is currently unable to process the request due to COVID-19 restrictions.</td></tr><tr><td>INVALID_FILE</td><td>422</td><td>The file is invalid.</td></tr><tr><td>INVALID_FILE_DIMENSIONS</td><td>422</td><td>File dimensions are incorrect for the selected mail type.</td></tr><tr><td>INVALID_FILE_DOWNLOAD_TIME</td><td>422</td><td>File download from remote server took too long.</td></tr><tr><td>INVALID_FILE_URL</td><td>422</td><td>The file URL when creating a resource is invalid.</td></tr><tr><td>INVALID_IMAGE_DPI</td><td>422</td><td>DPI must be at least 300.</td></tr><tr><td>INVALID_INTERNATIONAL_FEATURE</td><td>422</td><td>The specified product cannot be sent to the destination.</td></tr><tr><td>INVALID_PERFORATION_RETURN_ENVELOPE</td><td>422</td><td>Both <code>return_envelope</code> and <code>perforation</code> must be used together.</td></tr><tr><td>INVALID_TEMPLATE_HTML</td><td>422</td><td>The provided HTML is invalid.</td></tr><tr><td>MAIL_USE_TYPE_CAN_NOT_BE_NULL</td><td>422</td><td><code>use_type</code> must be one of "marketing" or "operational". Alternatively, an admin can set the <a href="../print-and-mail/building-a-mail-strategy/managing-mail-settings/declaring-mail-use-type">account default use type</a> in <a href="https://dashboard.lob.com/settings/account">Account Settings</a>.</td></tr><tr><td>MERGE_VARIABLE_REQUIRED</td><td>422</td><td>A required merge variable is missing.</td></tr><tr><td>MERGE_VARIABLE_WHITESPACE</td><td>422</td><td>Merge variable names cannot contain whitespace.</td></tr><tr><td>PDF_ENCRYPTED</td><td>422</td><td>An encrypted PDF was provided.</td></tr><tr><td>SPECIAL_CHARACTERS_RESTRICTED</td><td>422</td><td>Cannot use special characters for merge variable names.</td></tr><tr><td>UNEMBEDDED_FONTS</td><td>422</td><td>The provided PDF contains non-standard unembedded fonts. See description for details.</td></tr></tbody></table>