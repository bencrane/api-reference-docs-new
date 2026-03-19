# Errors

Lob uses RESTful HTTP response codes to indicate success or failure of an API request - read below for more information. In general, 2xx indicates success, 4xx indicate an input error, and 5xx indicates an error on Lob's end.

| Attribute | Description |
|-----------|-------------|
| `code` | A consistent machine-keyable string identifying the error. |
| `status_code` | A conventional HTTP status code. |
| `message` | A human-readable, subject-to-change message with more details about the error. |

## HTTP Status Code Summary

| Status Code | Code | Message |
|-------------|------|---------|
| 200 | SUCCESS | Successful API request |
| 401 | UNAUTHORIZED | Authorization error with your API key or account |
| 403 | FORBIDDEN | Forbidden error with your API key or account |
| 404 | NOT FOUND | The requested item does not exist |
| 422 | BAD REQUEST | The query or body parameters did not pass validation |
| 429 | TOO MANY REQUESTS | Too many requests have been sent with an API key in a given amount of time |
| 500 | SERVER ERROR | An internal server error occurred, please contact support@lob.com |

## Error Codes - Generic

| Status Code | Code | Message |
|-------------|------|---------|
| 422 | BAD_REQUEST | An invalid request was made. See error message for details. |
| 409/422 | CONFLICT | This operation would leave data in a conflicted state. |
| 403 | FEATURE_LIMIT_REACHED | The account has reached its resource limit and requires upgrading to add more. |
| 500 | INTERNAL_SERVER_ERROR | An error has occurred on Lob's servers. Please try request again. |
| 422 | INVALID | An invalid request was made. See error message for details. |
| 422 | NOT_DELETABLE | An attempt was made to delete a resource, but the resource cannot be deleted. |
| 404 | NOT_FOUND | The requested resource was not found. |
| 408 | REQUEST_TIMEOUT | The request took too long. Please try again. |
| 503 | SERVICE_UNAVAILABLE | The Lob servers are temporarily unavailable. Please try again. |
| 404 | UNRECOGNIZED_ENDPOINT | The requested endpoint doesn't exist. |
| 422 | UNSUPPORTED_LOB_VERSION | An unsupported Lob API version was requested. |

## Error Codes - Authentication

| Status Code | Code | Message |
|-------------|------|---------|
| 401 | EMAIL_REQUIRED | Account must have a verified email address before creating live resources. |
| 401 | UNAUTHORIZED | The request isn't authorized. |
| 401 | UNAUTHORIZED_TOKEN | Token isn't authorized. |
| 401/403 | INVALID_API_KEY | The API key is invalid. |
| 403 | PUBLISHABLE_KEY_NOT_ALLOWED | The requested operation needs a secret key, not a publishable key. See API Keys for more information. |
| 429 | RATE_LIMIT_EXCEEDED | Requests were sent too quickly and must be slowed down. |

## Error Codes - Advanced

| Status Code | Code | Message |
|-------------|------|---------|
| 401 | PAYMENT_METHOD_UNVERIFIED | You must have a verified bank account or credit card to submit live requests. |
| 404 | DELETED_BANK_ACCOUNT | Checks cannot be created with a deleted bank account. |
| 422 | ADDRESS_LENGTH_EXCEEDS_LIMIT | The sum of to.address_line1 and to.address_line2 cannot surpass 50 characters. |
| 422 | BANK_ACCOUNT_ALREADY_VERIFIED | The bank account has already been verified. |
| 422 | BANK_ERROR | There's an issue with the bank account. |
| 403 | BILLING_ADDRESS_REQUIRED | In order to create a live mail piece, your account needs to set up a billing address. |
| 422 | CUSTOM_ENVELOPE_INVENTORY_DEPLETED | Custom envelope inventory is depleted, and more will need to be ordered. |
| 422 | FAILED_DELIVERABILITY_STRICTNESS | The to address doesn't meet strictness requirements. See Account Settings to configure strictness. |
| 422 | FILE_PAGES_BELOW_MIN | Not enough pages. |
| 422 | FILE_PAGES_EXCEED_MAX | Too many pages. |
| 422 | FILE_SIZE_EXCEEDS_LIMIT | The file size is too large. See description for details. |
| 422 | FOREIGN_RETURN_ADDRESS | The 'from' address must be a US address. |
| 422 | INCONSISTENT_PAGE_DIMENSIONS | All pages of the input file must have the same dimensions. |
| 422 | INVALID_BANK_ACCOUNT | The provided bank routing number is invalid. |
| 422 | INVALID_BANK_ACCOUNT_VERIFICATION | Verification amounts do not match. |
| 422 | INVALID_CHECK_INTERNATIONAL | Checks cannot be sent internationally. |
| 422 | INVALID_COUNTRY_COVID | The postal service in the specified country is currently unable to process the request due to COVID-19 restrictions. |
| 422 | INVALID_FILE | The file is invalid. |
| 422 | INVALID_FILE_DIMENSIONS | File dimensions are incorrect for the selected mail type. |
| 422 | INVALID_FILE_DOWNLOAD_TIME | File download from remote server took too long. |
| 422 | INVALID_FILE_URL | The file URL when creating a resource is invalid. |
| 422 | INVALID_IMAGE_DPI | DPI must be at least 300. |
| 422 | INVALID_INTERNATIONAL_FEATURE | The specified product cannot be sent to the destination. |
| 422 | INVALID_PERFORATION_RETURN_ENVELOPE | Both `return_envelope` and `perforation` must be used together. |
| 422 | INVALID_TEMPLATE_HTML | The provided HTML is invalid. |
| 422 | MAIL_USE_TYPE_CAN_NOT_BE_NULL | `use_type` must be one of "marketing" or "operational". Alternatively, an admin can set the account default use type in Account Settings. |
| 422 | MERGE_VARIABLE_REQUIRED | A required merge variable is missing. |
| 422 | MERGE_VARIABLE_WHITESPACE | Merge variable names cannot contain whitespace. |
| 422 | PDF_ENCRYPTED | An encrypted PDF was provided. |
| 422 | SPECIAL_CHARACTERS_RESTRICTED | Cannot use special characters for merge variable names. |
| 422 | UNEMBEDDED_FONTS | The provided PDF contains non-standard unembedded fonts. See description for details. |