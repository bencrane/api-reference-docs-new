Create

Creates a new postcard given information
AUTHORIZATIONS:
basicAuth
QUERY PARAMETERS

idempotency_key	
string <= 256 characters
Example: idempotency_key=026e7634-24d7-486c-a0bb-4a17fd0eebc5
A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide.
HEADER PARAMETERS

Idempotency-Key	
string <= 256 characters
Example: 026e7634-24d7-486c-a0bb-4a17fd0eebc5
A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our implementation guide.
REQUEST BODY SCHEMA: application/json

to
required
adr_id (string) or (inline_address ((address_editable_us (address obj with `name` defined (object) or address obj with `company` defined (object))) or (inline_address_intl ((address_editable_intl (address obj with `name` defined (object) or address obj with `company` defined (object))) or (address_editable_intl (address obj with `name` defined (object) or address obj with `company` defined (object)))))))
Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your Print & Mail Edition, US addresses may also be run through National Change of Address Linkage(NCOALink). Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account's US Mail strictness setting, the request will fail. Lob Guide: Verification of Mailing Addresses
front
required
html_string (string) or tmpl_id (string) or remote_file_url (string) or local_file_path (string) (psc_front)
The artwork to use as the front of your postcard.

Notes:

HTML merge variables should not include delimiting whitespace.
PDF, PNG, and JPGs must be sized at 4.25"x6.25", 6.25"x9.25", or 6.25"x11.25" at 300 DPI, while supplied HTML will be rendered to the specified size.
See here for HTML examples.
back
required
html_string (string) or tmpl_id (string) or remote_file_url (string) or local_file_path (string) (psc_back)
The artwork to use as the back of your postcard.

Notes:

HTML merge variables should not include delimiting whitespace.
PDF, PNG, and JPGs must be sized at 4.25"x6.25", 6.25"x9.25", or 6.25"x11.25" at 300 DPI, while supplied HTML will be rendered to the specified size.
Be sure to leave room for address and postage information by following the templates provided here:
4x6 template
6x9 template
6x11 template
See here for HTML examples.
use_type
required
string or null (psc_use_type)
Enum: "marketing" "operational" null
The use type for each mailpiece. Can be one of marketing, operational, or null. Null use_type is only allowed if an account default use_type is selected in Account Settings. For more information on use_type, see our Help Center article.
description	
string or null (resource_description) <= 255 characters
An internal description that identifies this resource. Must be no longer than 255 characters.
metadata	
object (metadata) <= 500 characters [^"\\]{0,500}
Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters " and \. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported. See Metadata for more information.
mail_type	
string (mail_type)
Default: "usps_first_class"
Enum: "usps_first_class" "usps_standard"
A string designating the mail postage type:

usps_first_class - (default)
usps_standard - a cheaper option which is less predictable and takes longer to deliver. usps_standard cannot be used with 4x6 postcards or for any postcards sent outside of the United States.
merge_variables	
object or null (merge_variables) <= 25000 characters
You can input a merge variable payload object to your template or QR code redirect URLs to render dynamic content. For example, if you have a template like: {{variable_name}}, pass in {"variable_name": "Harry"} to render Harry. merge_variables must be an object. Any type of value is accepted as long as the object is valid JSON; you can use strings, numbers, booleans, arrays, objects, or null. The max length of the object is 25,000 characters. If you call JSON.stringify on your object, it can be no longer than 25,000 characters. Your variable names cannot contain any whitespace or any of the following special characters: !, ", #, %, &, ', (, ), *, +, ,, /, ;, <, =, >, @, [, \, ], ^, `, {, |, }, ~. More instructions can be found in our guide to using html and merge variables. Depending on your Merge Variable strictness setting, if you define variables in your HTML but do not pass them here, you will either receive an error or the variable will render as an empty string. These settings only apply on HTML templates and not on QR code redirect URLs.
send_date	
string or string (send_date)
A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default cancellation window applied to the mailpiece. Until the send_date has passed, the mailpiece can be canceled. If a date in the format 2017-11-01 is passed, it will evaluate to midnight UTC of that date (2017-11-01T00:00:00.000Z). If a datetime is passed, that exact time will be used. A send_date passed with no time zone will default to UTC, while a send_date passed with a time zone will be converted to UTC.
print_speed	
string or null
Default: "core"
Value: "core"
A string designating the mail speed type:

core - 2 production business days
size	
string (postcard_size)
Default: "4x6"
Enum: "4x6" "6x9" "6x11"
Specifies the size of the postcard. Only 4x6 postcards can be sent to international destinations.
from	
adr_id (string) or (address_editable_us (address obj with `name` defined (object) or address obj with `company` defined (object)))
Required if to address is international. Must either be an address ID or an inline object with correct address parameters. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification.
billing_group_id	
string (billing_group_id)
An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See Billing Group API for more information.
qr_code	
object (qr_code)
Customize and place a QR code on the creative at the required position.
fsc	
boolean
Default: false
This is in beta. Contact support@lob.com or your account contact to learn more. Not available for 4x6 or A5 postcard sizes.
Responses

200 Returns a postcard object
RESPONSE HEADERS
ratelimit-limit	
integer
Example: 150
The rate limit for a given endpoint.
ratelimit-remaining	
integer
Example: 100
The number of requests remaining in the current window.
ratelimit-reset	
integer
Example: 1528749846
The time at which the rate limit window resets in UTC epoch seconds
RESPONSE SCHEMA: application/json

to
required
(address_us (address obj with `name` defined (object) or address obj with `company` defined (object))) or (address_intl (address obj with `name` defined (object) or address obj with `company` defined (object))) (address)
carrier
required
string
Default: "USPS"
Value: "USPS"
id
required
string (psc_id) ^psc_[a-zA-Z0-9]+$
Unique identifier prefixed with psc_.
front_template_id
required
string or null^tmpl_[a-zA-Z0-9]+$
The unique ID of the HTML template used for the front of the postcard. Only filled out when the request contains a valid postcard template ID.
back_template_id
required
string or null^tmpl_[a-zA-Z0-9]+$
The unique ID of the HTML template used for the back of the postcard. Only filled out when the request contains a valid postcard template ID.
url
required
string (signed_link) ^https://lob-assets.com/(letters|postcards|ba...Show pattern
A signed link served over HTTPS. The link returned will expire in 30 days to prevent mis-sharing. Each time a GET request is initiated, a new signed URL will be generated.
description	
string or null (resource_description) <= 255 characters
An internal description that identifies this resource. Must be no longer than 255 characters.
metadata	
object (metadata) <= 500 characters [^"\\]{0,500}
Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters " and \. i.e. '{"customer_id" : "NEWYORK2015"}' Nested objects are not supported. See Metadata for more information.
mail_type	
string (mail_type)
Default: "usps_first_class"
Enum: "usps_first_class" "usps_standard"
A string designating the mail postage type:

usps_first_class - (default)
usps_standard - a cheaper option which is less predictable and takes longer to deliver. usps_standard cannot be used with 4x6 postcards or for any postcards sent outside of the United States.
merge_variables	
object or null (merge_variables) <= 25000 characters
You can input a merge variable payload object to your template or QR code redirect URLs to render dynamic content. For example, if you have a template like: {{variable_name}}, pass in {"variable_name": "Harry"} to render Harry. merge_variables must be an object. Any type of value is accepted as long as the object is valid JSON; you can use strings, numbers, booleans, arrays, objects, or null. The max length of the object is 25,000 characters. If you call JSON.stringify on your object, it can be no longer than 25,000 characters. Your variable names cannot contain any whitespace or any of the following special characters: !, ", #, %, &, ', (, ), *, +, ,, /, ;, <, =, >, @, [, \, ], ^, `, {, |, }, ~. More instructions can be found in our guide to using html and merge variables. Depending on your Merge Variable strictness setting, if you define variables in your HTML but do not pass them here, you will either receive an error or the variable will render as an empty string. These settings only apply on HTML templates and not on QR code redirect URLs.
send_date	
string or string (send_date)
A timestamp in ISO 8601 format which specifies a date after the current time and up to 180 days in the future to send the letter off for production. Setting a send date overrides the default cancellation window applied to the mailpiece. Until the send_date has passed, the mailpiece can be canceled. If a date in the format 2017-11-01 is passed, it will evaluate to midnight UTC of that date (2017-11-01T00:00:00.000Z). If a datetime is passed, that exact time will be used. A send_date passed with no time zone will default to UTC, while a send_date passed with a time zone will be converted to UTC.
print_speed	
string or null (print_speed)
Default: "core"
Value: "core"
A string designating the mail speed type:

core - 2 production business days
size	
string (postcard_size)
Default: "4x6"
Enum: "4x6" "6x9" "6x11"
Specifies the size of the postcard. Only 4x6 postcards can be sent to international destinations.
thumbnails	
Array of objects (thumbnail)
expected_delivery_date	
string <date> (expected_delivery_date)
A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its send_date.
date_created	
string <date-time> (date_created)
A timestamp in ISO 8601 format of the date the resource was created.
date_modified	
string <date-time> (date_modified)
A timestamp in ISO 8601 format of the date the resource was last modified.
deleted	
boolean (deleted)
Only returned if the resource has been successfully deleted.
from	
address obj with `name` defined (object) or address obj with `company` defined (object) (address_us)
front_template_version_id	
string or null^vrsn_[a-zA-Z0-9]+$
The unique ID of the specific version of the HTML template used for the front of the postcard. Only filled out when the request contains a valid postcard template ID.
back_template_version_id	
string or null^vrsn_[a-zA-Z0-9]+$
The unique ID of the specific version of the HTML template used for the back of the postcard. Only filled out when the request contains a valid postcard template ID.
tracking_events	
Array of objects or null (tracking_event_normal)
An array of tracking_event objects ordered by ascending time. Will not be populated for postcards created in test mode.
campaign_id	
string or null (campaign_id) ^(cmp|camp)_[a-zA-Z0-9]+$
Denotes resources created by the provided campaign id, prefixed with cmp_. In the case of snap packs, booklets, and letters with size us_legal, however, the campaign id is prefixed with camp_ instead of cmp_.
use_type	
string or null (psc_use_type)
Enum: "marketing" "operational" null
The use type for each mailpiece. Can be one of marketing, operational, or null. Null use_type is only allowed if an account default use_type is selected in Account Settings. For more information on use_type, see our Help Center article.
fsc	
boolean
Default: false
This is in beta. Contact support@lob.com or your account contact to learn more. Not available for 4x6 or A5 postcard sizes.
status	
string (status)
Enum: "processed" "rendered" "failed"
A string describing the PDF render status:

processed - the rendering process is currently in progress.
rendered - a PDF has been successfully rendered of the mailpiece.
failed - one or more issues has caused the rendering process to fail.
failure_reason	
object or null
An object describing the reason for failure if the resource failed to render.
object	
string
Default: "postcard"
Value: "postcard"
Value is resource type.
default Error

POST
/postcards
Request samples

PayloadCURLTYPESCRIPTNODERUBYPYTHONPHPJAVAELIXIRCSHARPGO
Content type
application/json

{
  "description": "demo",
  "to": {
    "description": "Harry - Office",
    "name": "Harry Zhang",
    "company": "Lob",
    "email": "harry@lob.com",
    "phone": "5555555555",
    "address_line1": "210 King St",
    "address_line2": "# 6100",
    "address_city": "San Francisco",
    "address_state": "CA",
    "address_zip": "94107",
    "address_country": "US"
  },
  "from": {
    "description": "Harry - Office",
    "name": "Harry Zhang",
    "company": "Lob",
    "email": "harry@lob.com",
    "phone": "5555555555",
    "address_line1": "210 King St",
    "address_line2": "# 6100",
    "address_city": "San Francisco",
    "address_state": "CA",
    "address_zip": "94107",
    "address_country": "US"
  },
  "front": "tmpl_a1234dddg",
  "back": "tmpl_a1234dddg",
  "size": "6x9",
  "mail_type": "usps_first_class",
  "merge_variables": {
    "name": "Harry"
  },
  "metadata": {
    "spiffy": "true"
  },
  "send_date": "2017-11-01T00:00:00.000Z",
  "use_type": "marketing",
  "qr_code": {
    "position": "relative",
    "redirect_url": "https://www.lob.com",
    "width": "2.5",
    "top": "2.5",
    "right": "2.5",
    "pages": "front,back"
  },
  "fsc": true,
  "print_speed": "core"
}
Response samples

200default
Content type
application/json
Example
basic

{
  "id": "psc_208e45e48d271294",
  "description": null,
  "metadata": { },
  "to": {
    "id": "adr_210a8d4b0b76d77b",
    "description": null,
    "name": null,
    "company": "LOB",
    "phone": null,
    "email": null,
    "address_line1": "210 KING ST STE 6100",
    "address_line2": null,
    "address_city": "SAN FRANCISCO",
    "address_state": "CA",
    "address_zip": "94107-1741",
    "address_country": "UNITED STATES",
    "metadata": { },
    "date_created": "2018-12-08T03:01:07.651Z",
    "date_modified": "2018-12-08T03:01:07.651Z",
    "object": "address"
  },
  "url": "https://lob-assets.com/postcards/psc_208e45e48d271294.pdf?version=v1&expires=1619218302&signature=NfHHLBSr5tOHA_Z4kij4dKqZG8f3vMDtwvuFVeeF9pV_lylcjLsVVODhNCE5hR6-2slUr6t9WMNsi429Pj7_DA",
  "carrier": "USPS",
  "front_template_id": null,
  "back_template_id": null,
  "date_created": "2021-03-24T22:51:42.838Z",
  "date_modified": "2021-03-24T22:51:42.838Z",
  "send_date": "2021-03-24T22:51:42.838Z",
  "use_type": "marketing",
  "fsc": false,
  "sla": "2",
  "object": "postcard"
}