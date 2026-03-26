Transactions | Stripe API Reference
          
          - 
          
          

          
        
        
          [](/api)Find anything/Ask AI[Introduction](https://docs.stripe.com/api)[Authentication](https://docs.stripe.com/api/authentication)[Errors](https://docs.stripe.com/api/errors)[Expanding Responses](https://docs.stripe.com/api/expanding_objects)[Idempotent requests](https://docs.stripe.com/api/idempotent_requests)[Include-dependent response values (API v2)](https://docs.stripe.com/api/include_dependent_response_values)[Metadata](https://docs.stripe.com/api/metadata)[Pagination](https://docs.stripe.com/api/pagination)[Request IDs](https://docs.stripe.com/api/request_ids)[Connected Accounts](https://docs.stripe.com/api/connected-accounts)[Versioning](https://docs.stripe.com/api/versioning)Core Resources[Accountsv2](https://docs.stripe.com/api/v2/core/accounts)[Account Linksv2](https://docs.stripe.com/api/v2/core/account-links)[Account Tokensv2](https://docs.stripe.com/api/v2/core/account-tokens)[Balance](https://docs.stripe.com/api/balance)[Balance Transactions](https://docs.stripe.com/api/balance_transactions)[Charges](https://docs.stripe.com/api/charges)[Customers](https://docs.stripe.com/api/customers)[Customer Session](https://docs.stripe.com/api/customer_sessions)[Disputes](https://docs.stripe.com/api/disputes)[Events](https://docs.stripe.com/api/events)[Eventsv2](https://docs.stripe.com/api/v2/core/events)[Event Destinationsv2](https://docs.stripe.com/api/v2/core/event-destinations)[Files](https://docs.stripe.com/api/files)[File Links](https://docs.stripe.com/api/file_links)[Mandates](https://docs.stripe.com/api/mandates)[Payment Intents](https://docs.stripe.com/api/payment_intents)[Personsv2](https://docs.stripe.com/api/v2/core/persons)[Person Tokensv2](https://docs.stripe.com/api/v2/core/person-tokens)[Setup Intents](https://docs.stripe.com/api/setup_intents)[Setup Attempts](https://docs.stripe.com/api/setup_attempts)[Payouts](https://docs.stripe.com/api/payouts)[Refunds](https://docs.stripe.com/api/refunds)[Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)[Tokens](https://docs.stripe.com/api/tokens)Payment Methods[Payment Methods](https://docs.stripe.com/api/payment_methods)[Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations)[Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)[Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)[Cash Balance](https://docs.stripe.com/api/cash_balance)[Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions)[Cards](https://docs.stripe.com/api/cards)[Sources](https://docs.stripe.com/api/sources)Products[Products](https://docs.stripe.com/api/products)[Prices](https://docs.stripe.com/api/prices)[Coupons](https://docs.stripe.com/api/coupons)[Promotion Code](https://docs.stripe.com/api/promotion_codes)[Discounts](https://docs.stripe.com/api/discounts)[Tax Code](https://docs.stripe.com/api/tax_codes)[Tax Rate](https://docs.stripe.com/api/tax_rates)[Shipping Rates](https://docs.stripe.com/api/shipping_rates)Checkout[Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)Payment Links[Payment Link](https://docs.stripe.com/api/payment-link)Billing[Alerts](https://docs.stripe.com/api/billing/alert)[Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary)[Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)[Credit Grant](https://docs.stripe.com/api/billing/credit-grant)[Credit Note](https://docs.stripe.com/api/credit_notes)[Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions)[Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations)[Customer Portal Session](https://docs.stripe.com/api/customer_portal/sessions)[Invoices](https://docs.stripe.com/api/invoices)[Invoice Items](https://docs.stripe.com/api/invoiceitems)[Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)[Invoice Payment](https://docs.stripe.com/api/invoice-payment)[Invoice Rendering Templates](https://docs.stripe.com/api/invoice-rendering-template)[Meters](https://docs.stripe.com/api/billing/meter)[Meter Events](https://docs.stripe.com/api/billing/meter-event)[Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)[Meter Event Adjustmentsv2](https://docs.stripe.com/api/v2/billing/meter-event-adjustments)[Meter Event Streamsv2](https://docs.stripe.com/api/v2/meter-event-streams)[Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)[Meter Eventsv2](https://docs.stripe.com/api/v2/meter-events)[Plans](https://docs.stripe.com/api/plans)[Quote](https://docs.stripe.com/api/quotes)[Subscriptions](https://docs.stripe.com/api/subscriptions)[Subscription Items](https://docs.stripe.com/api/subscription_items)[Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)[Tax IDs](https://docs.stripe.com/api/tax_ids)[Test Clocks](https://docs.stripe.com/api/test_clocks)Capital[Financing Offer](https://docs.stripe.com/api/capital/financing_offers)[Financing Summary](https://docs.stripe.com/api/capital/financing_summary)Connect[Accounts](https://docs.stripe.com/api/accounts)[Login Links](https://docs.stripe.com/api/accounts/login_link)[Account Links](https://docs.stripe.com/api/account_links)[Account Session](https://docs.stripe.com/api/account_sessions)[Application Fees](https://docs.stripe.com/api/application_fees)[Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)[Capabilities](https://docs.stripe.com/api/capabilities)[Country Specs](https://docs.stripe.com/api/country_specs)[Balance Settings](https://docs.stripe.com/api/balance-settings)[External Bank Accounts](https://docs.stripe.com/api/external_accounts)[External Account Cards](https://docs.stripe.com/api/external_account_cards)[Person](https://docs.stripe.com/api/persons)[Top-ups](https://docs.stripe.com/api/topups)[Transfers](https://docs.stripe.com/api/transfers)[Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)[Secrets](https://docs.stripe.com/api/secret_management)ReservesFraudIssuingTerminalTreasuryPayment RecordsAccount EvaluationEntitlementsSigmaReportingFinancial ConnectionsTaxIdentityCryptoClimateForwardingPrivacyWebhooks# [Transactions](/api/treasury/transactions)Ask about this sectionCopy for LLMView as MarkdownTransactions represent changes to a [FinancialAccount’s](#financial_accounts) balance.
Endpoints[GET/v1/treasury/transactions/:id](/api/treasury/transactions/retrieve)[GET/v1/treasury/transactions](/api/treasury/transactions/list)# [The Transaction object](/api/treasury/transactions/object)Ask about this sectionCopy for LLMView as Markdown### Attributes#### idstringUnique identifier for the object.
- #### objectstringString representing the object’s type. Objects of the same type share the same value.
- #### amountintegerAmount (in cents) transferred.
- #### balance_impactobjectThe change made to each of the FinancialAccount’s sub-balances by the Transaction.
Show child attributes- #### createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- #### currencyenumThree-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
- #### descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.
- #### entriesnullable objectExpandableA list of TransactionEntries that are part of this Transaction. This cannot be expanded in any list endpoints.
Show child attributes- #### financial_accountstringThe FinancialAccount associated with this object.
- #### flownullable stringID of the flow that created the Transaction.
- #### flow_detailsnullable objectExpandableDetails of the flow that created the Transaction.
Show child attributes- #### flow_typeenumType of the flow that created the Transaction.
Possible enum valuescredit_reversalThe Transaction is associated with a CreditReversal.
 | 
debit_reversalThe Transaction is associated with a DebitReversal.
 | 
inbound_transferThe Transaction is associated with an InboundTransfer.
 | 
issuing_authorizationThe Transaction is associated with an Issuing authorization.
 | 
otherThe Transaction is associated with some other money movement not listed above.
 | 
outbound_paymentThe Transaction is associated with an OutboundPayment.
 | 
outbound_transferThe Transaction is associated with an OutboundTransfer.
 | 
received_creditThe Transaction is associated with a ReceivedCredit.
 | 
received_debitThe Transaction is associated with a ReceivedDebit.
 | 
- #### livemodebooleanIf the object exists in live mode, the value is true. If the object exists in test mode, the value is false.
- #### statusenumStatus of the Transaction.
Possible enum valuesopenThe initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.
 | 
postedFunds have successfully entered or left the account. The current balance was affected.
 | 
voidThe Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.
 | 
- #### status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.
Show child attributesThe Transaction object```
`{  "id": "trxn_1MtkYw2eZvKYlo2ClMGIO54z",  "object": "treasury.transaction",  "amount": -100,  "balance_impact": {    "cash": -100,    "inbound_pending": 0,    "outbound_pending": 100  },  "created": 1680755802,  "currency": "usd",  "description": "Jane Austen (6789) | Outbound transfer | transfer",  "financial_account": "fa_1MtkYw2eZvKYlo2CrqmzUo3O",  "flow": "obt_1MtkYw2eZvKYlo2CqsyBpQts",  "flow_type": "outbound_transfer",  "livemode": false,  "status": "open",  "status_transitions": {    "posted_at": null,    "void_at": null  }}`
```# [Retrieve a Transaction](/api/treasury/transactions/retrieve)Ask about this sectionCopy for LLMView as MarkdownRetrieves the details of an existing Transaction.
### ParametersNo parameters.
### ReturnsReturns a Transaction object if a valid identifier was provided. Otherwise, returns an error.
GET /v1/treasury/transactions/:id```
`curl https://api.stripe.com/v1/treasury/transactions/trxn_1MtkYw2eZvKYlo2ClMGIO54z \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "trxn_1MtkYw2eZvKYlo2ClMGIO54z",  "object": "treasury.transaction",  "amount": -100,  "balance_impact": {    "cash": -100,    "inbound_pending": 0,    "outbound_pending": 100  },  "created": 1680755802,  "currency": "usd",  "description": "Jane Austen (6789) | Outbound transfer | transfer",  "financial_account": "fa_1MtkYw2eZvKYlo2CrqmzUo3O",  "flow": "obt_1MtkYw2eZvKYlo2CqsyBpQts",  "flow_type": "outbound_transfer",  "livemode": false,  "status": "open",  "status_transitions": {    "posted_at": null,    "void_at": null  }}`
```# [List all Transactions](/api/treasury/transactions/list)Ask about this sectionCopy for LLMView as MarkdownRetrieves a list of Transaction objects.
### Parameters- #### financial_accountstringReturns objects associated with this FinancialAccount.
- #### createdobjectOnly return Transactions that were created during the given date interval.
Show child parameters- #### order_byenumThe results are in reverse chronological order by created or posted_at. The default is created.
Possible enum valuescreatedTimestamp describing when the Transaction was created.
 | 
posted_atTimestamp describing when the Transaction was posted.
 | 
- #### statusenumOnly return Transactions that have the given status: open, posted, or void.
Possible enum valuesopenThe initial state for all Transactions. The Transaction results in updates to the sub-balance amounts, but the current balance is not affected until the Transaction posts.
 | 
postedFunds have successfully entered or left the account. The current balance was affected.
 | 
voidThe Transaction never impacted the balance. For example, a Transaction would enter this state if an OutboundPayment was initiated but then canceled before the funds left the account.
 | 
- #### status_transitionsobjectA filter for the status_transitions.posted_at timestamp. When using this filter, status=posted and order_by=posted_at must also be specified.
Show child parameters### More parametersExpand all- #### ending_beforestring- #### limitinteger- #### starting_afterstring### ReturnsA dictionary with a data property that contains an array of up to limit Transactions, starting after Transaction starting_after. Each entry in the array is a separate Transaction object. If no more Transactions are available, the resulting array will be empty.
GET /v1/treasury/transactions```
`curl -G https://api.stripe.com/v1/treasury/transactions \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d financial_account=fa_1MtkYw2eZvKYlo2CrqmzUo3O \  -d limit=3`
```Response```
`{  "object": "list",  "url": "/v1/treasury/transactions",  "has_more": false,  "data": [    {      "id": "trxn_1MtkYw2eZvKYlo2ClMGIO54z",      "object": "treasury.transaction",      "amount": -100,      "balance_impact": {        "cash": -100,        "inbound_pending": 0,        "outbound_pending": 100      },      "created": 1680755802,      "currency": "usd",      "description": "Jane Austen (6789) | Outbound transfer | transfer",      "financial_account": "fa_1MtkYw2eZvKYlo2CrqmzUo3O",      "flow": "obt_1MtkYw2eZvKYlo2CqsyBpQts",      "flow_type": "outbound_transfer",      "livemode": false,      "status": "open",      "status_transitions": {        "posted_at": null,        "void_at": null      }    }  ]}`
```