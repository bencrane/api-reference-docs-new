Create a Reader | Stripe API Reference
          
          - 
          
          

          
        
        
          [](/api)Find anything/Ask AI[Introduction](https://docs.stripe.com/api)[Authentication](https://docs.stripe.com/api/authentication)[Errors](https://docs.stripe.com/api/errors)[Expanding Responses](https://docs.stripe.com/api/expanding_objects)[Idempotent requests](https://docs.stripe.com/api/idempotent_requests)[Include-dependent response values (API v2)](https://docs.stripe.com/api/include_dependent_response_values)[Metadata](https://docs.stripe.com/api/metadata)[Pagination](https://docs.stripe.com/api/pagination)[Request IDs](https://docs.stripe.com/api/request_ids)[Connected Accounts](https://docs.stripe.com/api/connected-accounts)[Versioning](https://docs.stripe.com/api/versioning)Core Resources[Accountsv2](https://docs.stripe.com/api/v2/core/accounts)[Account Linksv2](https://docs.stripe.com/api/v2/core/account-links)[Account Tokensv2](https://docs.stripe.com/api/v2/core/account-tokens)[Balance](https://docs.stripe.com/api/balance)[Balance Transactions](https://docs.stripe.com/api/balance_transactions)[Charges](https://docs.stripe.com/api/charges)[Customers](https://docs.stripe.com/api/customers)[Customer Session](https://docs.stripe.com/api/customer_sessions)[Disputes](https://docs.stripe.com/api/disputes)[Events](https://docs.stripe.com/api/events)[Eventsv2](https://docs.stripe.com/api/v2/core/events)[Event Destinationsv2](https://docs.stripe.com/api/v2/core/event-destinations)[Files](https://docs.stripe.com/api/files)[File Links](https://docs.stripe.com/api/file_links)[Mandates](https://docs.stripe.com/api/mandates)[Payment Intents](https://docs.stripe.com/api/payment_intents)[Personsv2](https://docs.stripe.com/api/v2/core/persons)[Person Tokensv2](https://docs.stripe.com/api/v2/core/person-tokens)[Setup Intents](https://docs.stripe.com/api/setup_intents)[Setup Attempts](https://docs.stripe.com/api/setup_attempts)[Payouts](https://docs.stripe.com/api/payouts)[Refunds](https://docs.stripe.com/api/refunds)[Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)[Tokens](https://docs.stripe.com/api/tokens)Payment Methods[Payment Methods](https://docs.stripe.com/api/payment_methods)[Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations)[Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)[Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)[Cash Balance](https://docs.stripe.com/api/cash_balance)[Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions)[Cards](https://docs.stripe.com/api/cards)[Sources](https://docs.stripe.com/api/sources)Products[Products](https://docs.stripe.com/api/products)[Prices](https://docs.stripe.com/api/prices)[Coupons](https://docs.stripe.com/api/coupons)[Promotion Code](https://docs.stripe.com/api/promotion_codes)[Discounts](https://docs.stripe.com/api/discounts)[Tax Code](https://docs.stripe.com/api/tax_codes)[Tax Rate](https://docs.stripe.com/api/tax_rates)[Shipping Rates](https://docs.stripe.com/api/shipping_rates)Checkout[Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)Payment Links[Payment Link](https://docs.stripe.com/api/payment-link)Billing[Alerts](https://docs.stripe.com/api/billing/alert)[Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary)[Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)[Credit Grant](https://docs.stripe.com/api/billing/credit-grant)[Credit Note](https://docs.stripe.com/api/credit_notes)[Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions)[Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations)[Customer Portal Session](https://docs.stripe.com/api/customer_portal/sessions)[Invoices](https://docs.stripe.com/api/invoices)[Invoice Items](https://docs.stripe.com/api/invoiceitems)[Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)[Invoice Payment](https://docs.stripe.com/api/invoice-payment)[Invoice Rendering Templates](https://docs.stripe.com/api/invoice-rendering-template)[Meters](https://docs.stripe.com/api/billing/meter)[Meter Events](https://docs.stripe.com/api/billing/meter-event)[Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)[Meter Event Adjustmentsv2](https://docs.stripe.com/api/v2/billing/meter-event-adjustments)[Meter Event Streamsv2](https://docs.stripe.com/api/v2/meter-event-streams)[Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)[Meter Eventsv2](https://docs.stripe.com/api/v2/meter-events)[Plans](https://docs.stripe.com/api/plans)[Quote](https://docs.stripe.com/api/quotes)[Subscriptions](https://docs.stripe.com/api/subscriptions)[Subscription Items](https://docs.stripe.com/api/subscription_items)[Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)[Tax IDs](https://docs.stripe.com/api/tax_ids)[Test Clocks](https://docs.stripe.com/api/test_clocks)Capital[Financing Offer](https://docs.stripe.com/api/capital/financing_offers)[Financing Summary](https://docs.stripe.com/api/capital/financing_summary)Connect[Accounts](https://docs.stripe.com/api/accounts)[Login Links](https://docs.stripe.com/api/accounts/login_link)[Account Links](https://docs.stripe.com/api/account_links)[Account Session](https://docs.stripe.com/api/account_sessions)[Application Fees](https://docs.stripe.com/api/application_fees)[Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)[Capabilities](https://docs.stripe.com/api/capabilities)[Country Specs](https://docs.stripe.com/api/country_specs)[Balance Settings](https://docs.stripe.com/api/balance-settings)[External Bank Accounts](https://docs.stripe.com/api/external_accounts)[External Account Cards](https://docs.stripe.com/api/external_account_cards)[Person](https://docs.stripe.com/api/persons)[Top-ups](https://docs.stripe.com/api/topups)[Transfers](https://docs.stripe.com/api/transfers)[Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)[Secrets](https://docs.stripe.com/api/secret_management)ReservesFraudIssuingTerminalTreasuryPayment RecordsAccount EvaluationEntitlementsSigmaReportingFinancial ConnectionsTaxIdentityCryptoClimateForwardingPrivacyWebhooks# [Create a Reader](/api/terminal/readers/create)Ask about this sectionCopy for LLMView as MarkdownCreates a new Reader object.
### Parameters#### registration_codestringRequiredA code generated by the reader used for registering to an account.
- #### labelstringCustom label given to the reader for easier identification. If no label is specified, the registration code will be used.
- #### locationstringRequiredThe location to assign the reader to.
- #### metadataobjectSet of [key-value pairs](/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.
### ReturnsReturns a Reader object if creation succeeds.
POST /v1/terminal/readers```
`curl https://api.stripe.com/v1/terminal/readers \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d "label=Blue Rabbit" \  -d registration_code=simulated-wpe \  -d location=tml_FDOtHwxAAdIJOh`
```Response```
`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "2.37.2.0",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`
```# [Update a Reader](/api/terminal/readers/update)Ask about this sectionCopy for LLMView as MarkdownUpdates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
### Parameters- #### labelstringThe new label of the reader.
- #### metadataobjectSet of [key-value pairs](/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.
### ReturnsReturns an updated Reader object if a valid identifier was provided.
POST /v1/terminal/readers/:id```
`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d "metadata[order_id]=6735"`
```Response```
`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "2.37.2.0",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {    "order_id": "6735"  },  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`
```# [Retrieve a Reader](/api/terminal/readers/retrieve)Ask about this sectionCopy for LLMView as MarkdownRetrieves a Reader object.
### ParametersNo parameters.
### ReturnsReturns a Reader object if a valid identifier was provided.
GET /v1/terminal/readers/:id```
`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "2.37.2.0",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`
```# [List all Readers](/api/terminal/readers/list)Ask about this sectionCopy for LLMView as MarkdownReturns a list of Reader objects.
### Parameters- #### device_typeenumFilters readers by device type
Possible enum valuesbbpos_chipper2xBBPOS Chipper 2X BT reader.
 | 
bbpos_wisepad3BBPOS WisePad 3 reader.
 | 
bbpos_wisepos_eBBPOS WisePOS E reader.
 | 
mobile_phone_readerTap to Pay device.
 | 
simulated_stripe_s700Simulated Stripe S700 reader.
 | 
simulated_stripe_s710Simulated Stripe S710 reader.
 | 
simulated_wisepos_eSimulated BBPOS WisePOS E reader.
 | 
stripe_m2Stripe M2 reader.
 | 
stripe_s700Stripe S700 reader.
 | 
stripe_s710Stripe S710 reader.
 | 
- #### locationstringA location ID to filter the response list to only readers at the specific location
- #### serial_numberstringFilters readers by serial number
- #### statusenumA status filter to filter readers to only offline or online readers
### More parametersExpand all- #### ending_beforestring- #### limitinteger- #### starting_afterstring### ReturnsA dictionary with a data property that contains an array of up to limit readers, starting after reader starting_after. Each entry in the array is a separate Terminal Reader object. If no more readers are available, the resulting array will be empty.
GET /v1/terminal/readers```
`curl -G https://api.stripe.com/v1/terminal/readers \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d limit=3`
```Response```
`{  "object": "list",  "url": "/v1/terminal/readers",  "has_more": false,  "data": [    {      "id": "tmr_FDOt2wlRZEdpd7",      "object": "terminal.reader",      "action": null,      "device_sw_version": "2.37.2.0",      "device_type": "simulated_wisepos_e",      "ip_address": "0.0.0.0",      "label": "Blue Rabbit",      "last_seen_at": 1681320543815,      "livemode": false,      "location": "tml_FDOtHwxAAdIJOh",      "metadata": {},      "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",      "status": "online"    }  ]}`
```# [Delete a Reader](/api/terminal/readers/delete)Ask about this sectionCopy for LLMView as MarkdownDeletes a Reader object.
### ParametersNo parameters.
### ReturnsReturns the Reader object that was deleted.
DELETE /v1/terminal/readers/:id```
`curl -X DELETE https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "deleted": true}`
```