# NCOALink Test Environment

In addition to sending live requests, you may also want to simulate what an NCOALink response might look like so that you can ensure your application behaves as expected. The behavior of NCOALink in Lob's Test Environment is very similar to our US Verifications Test Mode.

To simulate an NCOALink request, send a POST request to any of the four endpoints below with an `address_line1` field equal to `NCOA`:

* `POST /v1/addresses`
* `POST /v1/checks`
* `POST /v1/letters`
* `POST /v1/postcards`
* `POST /v1/self_mailers`

A static address will always be returned, as documented in the `ncoa_us_test` example under Response samples within the "Create an Address" section in Addresses (along with the corresponding request under "Request samples").