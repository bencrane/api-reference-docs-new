# NCOALink Live Environment

Though there are no changes to API requests, there are significant changes to our API responses, but only in the event that an address has been changed through NCOALink. If an address has not been changed through NCOALink, the response would be identical to our standard responses, except the addition of a `recipient_moved` field, which is `false` for unchanged addresses.

If an address has been changed through NCOALink, we are required to suppress the following response fields for that address:

* `address_line1`
* `address_line2`
* The +4 portion of the ZIP+4 (5-digit ZIP code will still be present)

See the `ncoa_us_live` example under Response samples within the "Create an Address" section in Addresses.