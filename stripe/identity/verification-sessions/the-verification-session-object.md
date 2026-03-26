Verification Session | Stripe API Reference
          
          - 
          
          

          
        
        
          [](/api)Find anything/Ask AI[Introduction](https://docs.stripe.com/api)[Authentication](https://docs.stripe.com/api/authentication)[Errors](https://docs.stripe.com/api/errors)[Expanding Responses](https://docs.stripe.com/api/expanding_objects)[Idempotent requests](https://docs.stripe.com/api/idempotent_requests)[Include-dependent response values (API v2)](https://docs.stripe.com/api/include_dependent_response_values)[Metadata](https://docs.stripe.com/api/metadata)[Pagination](https://docs.stripe.com/api/pagination)[Request IDs](https://docs.stripe.com/api/request_ids)[Connected Accounts](https://docs.stripe.com/api/connected-accounts)[Versioning](https://docs.stripe.com/api/versioning)Core Resources[Accountsv2](https://docs.stripe.com/api/v2/core/accounts)[Account Linksv2](https://docs.stripe.com/api/v2/core/account-links)[Account Tokensv2](https://docs.stripe.com/api/v2/core/account-tokens)[Balance](https://docs.stripe.com/api/balance)[Balance Transactions](https://docs.stripe.com/api/balance_transactions)[Charges](https://docs.stripe.com/api/charges)[Customers](https://docs.stripe.com/api/customers)[Customer Session](https://docs.stripe.com/api/customer_sessions)[Disputes](https://docs.stripe.com/api/disputes)[Events](https://docs.stripe.com/api/events)[Eventsv2](https://docs.stripe.com/api/v2/core/events)[Event Destinationsv2](https://docs.stripe.com/api/v2/core/event-destinations)[Files](https://docs.stripe.com/api/files)[File Links](https://docs.stripe.com/api/file_links)[Mandates](https://docs.stripe.com/api/mandates)[Payment Intents](https://docs.stripe.com/api/payment_intents)[Personsv2](https://docs.stripe.com/api/v2/core/persons)[Person Tokensv2](https://docs.stripe.com/api/v2/core/person-tokens)[Setup Intents](https://docs.stripe.com/api/setup_intents)[Setup Attempts](https://docs.stripe.com/api/setup_attempts)[Payouts](https://docs.stripe.com/api/payouts)[Refunds](https://docs.stripe.com/api/refunds)[Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)[Tokens](https://docs.stripe.com/api/tokens)Payment Methods[Payment Methods](https://docs.stripe.com/api/payment_methods)[Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations)[Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)[Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)[Cash Balance](https://docs.stripe.com/api/cash_balance)[Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions)[Cards](https://docs.stripe.com/api/cards)[Sources](https://docs.stripe.com/api/sources)Products[Products](https://docs.stripe.com/api/products)[Prices](https://docs.stripe.com/api/prices)[Coupons](https://docs.stripe.com/api/coupons)[Promotion Code](https://docs.stripe.com/api/promotion_codes)[Discounts](https://docs.stripe.com/api/discounts)[Tax Code](https://docs.stripe.com/api/tax_codes)[Tax Rate](https://docs.stripe.com/api/tax_rates)[Shipping Rates](https://docs.stripe.com/api/shipping_rates)Checkout[Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)Payment Links[Payment Link](https://docs.stripe.com/api/payment-link)Billing[Alerts](https://docs.stripe.com/api/billing/alert)[Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary)[Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)[Credit Grant](https://docs.stripe.com/api/billing/credit-grant)[Credit Note](https://docs.stripe.com/api/credit_notes)[Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions)[Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations)[Customer Portal Session](https://docs.stripe.com/api/customer_portal/sessions)[Invoices](https://docs.stripe.com/api/invoices)[Invoice Items](https://docs.stripe.com/api/invoiceitems)[Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)[Invoice Payment](https://docs.stripe.com/api/invoice-payment)[Invoice Rendering Templates](https://docs.stripe.com/api/invoice-rendering-template)[Meters](https://docs.stripe.com/api/billing/meter)[Meter Events](https://docs.stripe.com/api/billing/meter-event)[Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)[Meter Event Adjustmentsv2](https://docs.stripe.com/api/v2/billing/meter-event-adjustments)[Meter Event Streamsv2](https://docs.stripe.com/api/v2/meter-event-streams)[Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)[Meter Eventsv2](https://docs.stripe.com/api/v2/meter-events)[Plans](https://docs.stripe.com/api/plans)[Quote](https://docs.stripe.com/api/quotes)[Subscriptions](https://docs.stripe.com/api/subscriptions)[Subscription Items](https://docs.stripe.com/api/subscription_items)[Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)[Tax IDs](https://docs.stripe.com/api/tax_ids)[Test Clocks](https://docs.stripe.com/api/test_clocks)Capital[Financing Offer](https://docs.stripe.com/api/capital/financing_offers)[Financing Summary](https://docs.stripe.com/api/capital/financing_summary)Connect[Accounts](https://docs.stripe.com/api/accounts)[Login Links](https://docs.stripe.com/api/accounts/login_link)[Account Links](https://docs.stripe.com/api/account_links)[Account Session](https://docs.stripe.com/api/account_sessions)[Application Fees](https://docs.stripe.com/api/application_fees)[Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)[Capabilities](https://docs.stripe.com/api/capabilities)[Country Specs](https://docs.stripe.com/api/country_specs)[Balance Settings](https://docs.stripe.com/api/balance-settings)[External Bank Accounts](https://docs.stripe.com/api/external_accounts)[External Account Cards](https://docs.stripe.com/api/external_account_cards)[Person](https://docs.stripe.com/api/persons)[Top-ups](https://docs.stripe.com/api/topups)[Transfers](https://docs.stripe.com/api/transfers)[Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)[Secrets](https://docs.stripe.com/api/secret_management)ReservesFraudIssuingTerminalTreasuryPayment RecordsAccount EvaluationEntitlementsSigmaReportingFinancial ConnectionsTaxIdentityCryptoClimateForwardingPrivacyWebhooks# [Verification Session](/api/identity/verification_sessions)Ask about this sectionCopy for LLMView as MarkdownA VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what [verification check](/identity/verification-checks) to perform. Only create one VerificationSession for each verification in your system.
A VerificationSession transitions through [multiple statuses](/identity/how-sessions-work) throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.
Related guide: [The Verification Sessions API](/identity/verification-sessions)
Endpoints[POST/v1/identity/verification_sessions](/api/identity/verification_sessions/create)[POST/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/update)[GET/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/retrieve)[GET/v1/identity/verification_sessions](/api/identity/verification_sessions/list)[POST/v1/identity/verification_sessions/:id/cancel](/api/identity/verification_sessions/cancel)[POST/v1/identity/verification_sessions/:id/redact](/api/identity/verification_sessions/redact)# [The VerificationSession object](/api/identity/verification_sessions/object)Ask about this sectionCopy for LLMView as Markdown### Attributes#### idstringUnique identifier for the object.
- #### objectstringString representing the object’s type. Objects of the same type share the same value.
- #### client_reference_idnullable stringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
- #### client_secretnullable stringThe short-lived client secret used by Stripe.js to [show a verification modal](/js/identity/modal) inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on [passing the client secret to the frontend](/identity/verification-sessions#client-secret) to learn more.
- #### createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- #### last_errornullable objectIf present, this property tells you the last error encountered when processing the verification.
Show child attributes- #### last_verification_reportnullable stringExpandableID of the most recent VerificationReport. [Learn more about accessing detailed verification results.](/identity/verification-sessions#results)
- #### livemodebooleanIf the object exists in live mode, the value is true. If the object exists in test mode, the value is false.
- #### metadataobjectSet of [key-value pairs](/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- #### optionsnullable objectA set of options for the session’s verification checks.
Show child attributes- #### provided_detailsnullable objectExpandableDetails provided about the user being verified. These details may be shown to the user.
Show child attributes- #### redactionnullable objectRedaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.
Show child attributes- #### related_customernullable stringCustomer ID
- #### related_customer_accountnullable stringThe ID of the Account representing a customer.
- #### related_personnullable objectTokens referencing the related Person resource and it’s associated account.
Show child attributes- #### statusenumStatus of this VerificationSession. [Learn more about the lifecycle of sessions](/identity/how-sessions-work).
Possible enum valuescanceledThe VerificationSession has been invalidated for future submission attempts.
 | 
processingThe session has been submitted and is being processed. Most [verification checks](/identity/verification-checks) are processed in less than 1 minute.
 | 
requires_inputRequires user input before processing can continue.
 | 
verifiedProcessing of all the verification checks are complete and successfully verified.
 | 
- #### typeenumThe type of [verification check](/identity/verification-checks) to be performed.
Possible enum valuesdocument[Document check](/identity/verification-checks?type=document).
 | 
id_number[ID number check](/identity/verification-checks?type=id-number).
 | 
verification_flowConfiguration provided by verification flow
 | 
- #### urlnullable stringThe short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on [verifying identity documents](/identity/verify-identity-documents?platform=web&type=redirect) to learn how to redirect users to Stripe.
- #### verification_flownullable stringThe configuration token of a verification flow from the dashboard.
- #### verified_outputsnullable objectExpandableThe user’s verified data.
Show child attributesThe VerificationSession object```
`{  "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680526,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`
```# [Create a VerificationSession](/api/identity/verification_sessions/create)Ask about this sectionCopy for LLMView as MarkdownCreates a VerificationSession object.
After the VerificationSession is created, display a verification modal using the session client_secret or send your users to the session’s url.
If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.
Related guide: [Verify your users’ identity documents](/identity/verify-identity-documents)
### Parameters- #### client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
- #### metadataobjectSet of [key-value pairs](/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.
- #### optionsobjectA set of options for the session’s verification checks.
Show child parameters- #### provided_detailsobjectDetails provided about the user being verified. These details may be shown to the user.
Show child parameters- #### related_customerstringCustomer ID
- #### related_customer_accountstringThe ID of the Account representing a customer.
- #### related_personobjectTokens referencing a Person resource and it’s associated account.
Show child parameters- #### return_urlstringThe URL that the user will be redirected to upon completing the verification flow.
- #### typeenumThe type of [verification check](/identity/verification-checks) to be performed. You must provide a type if not passing verification_flow.
Possible enum valuesdocument[Document check](/identity/verification-checks?type=document).
 | 
id_number[ID number check](/identity/verification-checks?type=id-number).
 | 
- #### verification_flowstringThe ID of a verification flow from the Dashboard. See https://docs.stripe.com/identity/verification-flows.
### ReturnsReturns the created VerificationSession object
POST /v1/identity/verification_sessions```
`curl https://api.stripe.com/v1/identity/verification_sessions \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d type=document`
```Response```
`{  "id": "vs_1NuN4zLkdIwHu7ixleE6HvkI",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680197,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {},  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`
```# [Update a VerificationSession](/api/identity/verification_sessions/update)Ask about this sectionCopy for LLMView as MarkdownUpdates a VerificationSession object.
When the session status is requires_input, you can use this method to update the verification check and options.
### Parameters- #### metadataobjectSet of [key-value pairs](/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.
- #### optionsobjectA set of options for the session’s verification checks.
Show child parameters- #### provided_detailsobjectDetails provided about the user being verified. These details may be shown to the user.
Show child parameters- #### typeenumThe type of [verification check](/identity/verification-checks) to be performed.
Possible enum valuesdocument[Document check](/identity/verification-checks?type=document).
 | 
id_number[ID number check](/identity/verification-checks?type=id-number).
 | 
### ReturnsReturns the updated VerificationSession object
POST /v1/identity/verification_sessions/:id```
`curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN9WLkdIwHu7ix597AR9uz \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d type=id_number`
```Response```
`{  "id": "vs_1NuN9WLkdIwHu7ix597AR9uz",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680478,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {},  "redaction": null,  "status": "requires_input",  "type": "id_number",  "url": "..."}`
```# [Retrieve a VerificationSession](/api/identity/verification_sessions/retrieve)Ask about this sectionCopy for LLMView as MarkdownRetrieves the details of a VerificationSession that was previously created.
When the session status is requires_input, you can use this method to retrieve a valid client_secret or url to allow re-submission.
### ParametersNo parameters.
### ReturnsReturns a VerificationSession object
GET /v1/identity/verification_sessions/:id```
`curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuNAILkdIwHu7ixh7OtGMLw \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680526,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`
```