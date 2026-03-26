Transaction Entries | Stripe API Reference
          
          - 
          
          

          
        
        
          [](/api)Find anything/Ask AI[Introduction](https://docs.stripe.com/api)[Authentication](https://docs.stripe.com/api/authentication)[Errors](https://docs.stripe.com/api/errors)[Expanding Responses](https://docs.stripe.com/api/expanding_objects)[Idempotent requests](https://docs.stripe.com/api/idempotent_requests)[Include-dependent response values (API v2)](https://docs.stripe.com/api/include_dependent_response_values)[Metadata](https://docs.stripe.com/api/metadata)[Pagination](https://docs.stripe.com/api/pagination)[Request IDs](https://docs.stripe.com/api/request_ids)[Connected Accounts](https://docs.stripe.com/api/connected-accounts)[Versioning](https://docs.stripe.com/api/versioning)Core Resources[Accountsv2](https://docs.stripe.com/api/v2/core/accounts)[Account Linksv2](https://docs.stripe.com/api/v2/core/account-links)[Account Tokensv2](https://docs.stripe.com/api/v2/core/account-tokens)[Balance](https://docs.stripe.com/api/balance)[Balance Transactions](https://docs.stripe.com/api/balance_transactions)[Charges](https://docs.stripe.com/api/charges)[Customers](https://docs.stripe.com/api/customers)[Customer Session](https://docs.stripe.com/api/customer_sessions)[Disputes](https://docs.stripe.com/api/disputes)[Events](https://docs.stripe.com/api/events)[Eventsv2](https://docs.stripe.com/api/v2/core/events)[Event Destinationsv2](https://docs.stripe.com/api/v2/core/event-destinations)[Files](https://docs.stripe.com/api/files)[File Links](https://docs.stripe.com/api/file_links)[Mandates](https://docs.stripe.com/api/mandates)[Payment Intents](https://docs.stripe.com/api/payment_intents)[Personsv2](https://docs.stripe.com/api/v2/core/persons)[Person Tokensv2](https://docs.stripe.com/api/v2/core/person-tokens)[Setup Intents](https://docs.stripe.com/api/setup_intents)[Setup Attempts](https://docs.stripe.com/api/setup_attempts)[Payouts](https://docs.stripe.com/api/payouts)[Refunds](https://docs.stripe.com/api/refunds)[Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)[Tokens](https://docs.stripe.com/api/tokens)Payment Methods[Payment Methods](https://docs.stripe.com/api/payment_methods)[Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations)[Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)[Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)[Cash Balance](https://docs.stripe.com/api/cash_balance)[Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions)[Cards](https://docs.stripe.com/api/cards)[Sources](https://docs.stripe.com/api/sources)Products[Products](https://docs.stripe.com/api/products)[Prices](https://docs.stripe.com/api/prices)[Coupons](https://docs.stripe.com/api/coupons)[Promotion Code](https://docs.stripe.com/api/promotion_codes)[Discounts](https://docs.stripe.com/api/discounts)[Tax Code](https://docs.stripe.com/api/tax_codes)[Tax Rate](https://docs.stripe.com/api/tax_rates)[Shipping Rates](https://docs.stripe.com/api/shipping_rates)Checkout[Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)Payment Links[Payment Link](https://docs.stripe.com/api/payment-link)Billing[Alerts](https://docs.stripe.com/api/billing/alert)[Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary)[Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)[Credit Grant](https://docs.stripe.com/api/billing/credit-grant)[Credit Note](https://docs.stripe.com/api/credit_notes)[Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions)[Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations)[Customer Portal Session](https://docs.stripe.com/api/customer_portal/sessions)[Invoices](https://docs.stripe.com/api/invoices)[Invoice Items](https://docs.stripe.com/api/invoiceitems)[Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)[Invoice Payment](https://docs.stripe.com/api/invoice-payment)[Invoice Rendering Templates](https://docs.stripe.com/api/invoice-rendering-template)[Meters](https://docs.stripe.com/api/billing/meter)[Meter Events](https://docs.stripe.com/api/billing/meter-event)[Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)[Meter Event Adjustmentsv2](https://docs.stripe.com/api/v2/billing/meter-event-adjustments)[Meter Event Streamsv2](https://docs.stripe.com/api/v2/meter-event-streams)[Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)[Meter Eventsv2](https://docs.stripe.com/api/v2/meter-events)[Plans](https://docs.stripe.com/api/plans)[Quote](https://docs.stripe.com/api/quotes)[Subscriptions](https://docs.stripe.com/api/subscriptions)[Subscription Items](https://docs.stripe.com/api/subscription_items)[Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)[Tax IDs](https://docs.stripe.com/api/tax_ids)[Test Clocks](https://docs.stripe.com/api/test_clocks)Capital[Financing Offer](https://docs.stripe.com/api/capital/financing_offers)[Financing Summary](https://docs.stripe.com/api/capital/financing_summary)Connect[Accounts](https://docs.stripe.com/api/accounts)[Login Links](https://docs.stripe.com/api/accounts/login_link)[Account Links](https://docs.stripe.com/api/account_links)[Account Session](https://docs.stripe.com/api/account_sessions)[Application Fees](https://docs.stripe.com/api/application_fees)[Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)[Capabilities](https://docs.stripe.com/api/capabilities)[Country Specs](https://docs.stripe.com/api/country_specs)[Balance Settings](https://docs.stripe.com/api/balance-settings)[External Bank Accounts](https://docs.stripe.com/api/external_accounts)[External Account Cards](https://docs.stripe.com/api/external_account_cards)[Person](https://docs.stripe.com/api/persons)[Top-ups](https://docs.stripe.com/api/topups)[Transfers](https://docs.stripe.com/api/transfers)[Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)[Secrets](https://docs.stripe.com/api/secret_management)ReservesFraudIssuingTerminalTreasuryPayment RecordsAccount EvaluationEntitlementsSigmaReportingFinancial ConnectionsTaxIdentityCryptoClimateForwardingPrivacyWebhooks# [Transaction Entries](/api/treasury/transaction_entries)Ask about this sectionCopy for LLMView as MarkdownTransactionEntries represent individual units of money movements within a single [Transaction](#transactions).
Endpoints[GET/v1/treasury/transaction_entries/:id](/api/treasury/transaction_entries/retrieve)[GET/v1/treasury/transaction_entries](/api/treasury/transaction_entries/list)# [The TransactionEntry object](/api/treasury/transaction_entries/object)Ask about this sectionCopy for LLMView as Markdown### Attributes#### idstringUnique identifier for the object.
- #### objectstringString representing the object’s type. Objects of the same type share the same value.
- #### balance_impactobjectThe current impact of the TransactionEntry on the FinancialAccount’s balance.
Show child attributes- #### createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- #### currencyenumThree-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
- #### effective_attimestampWhen the TransactionEntry will impact the FinancialAccount’s balance.
- #### financial_accountstringThe FinancialAccount associated with this object.
- #### flownullable stringToken of the flow associated with the TransactionEntry.
- #### flow_detailsnullable objectExpandableDetails of the flow associated with the TransactionEntry.
Show child attributes- #### flow_typeenumType of the flow associated with the TransactionEntry.
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
- #### transactionstringExpandableThe Transaction associated with this object.
- #### typeenumThe specific money movement that generated the TransactionEntry.
Possible enum valuescredit_reversalThe TransactionEntry was generated by a CreditReversal.
 | 
credit_reversal_postingThe TransactionEntry was generated by a posted CreditReversal.
 | 
debit_reversalThe TransactionEntry was generated by a DebitReversal.
 | 
inbound_transferThe TransactionEntry was generated by an InboundTransfer.
 | 
inbound_transfer_returnThe TransactionEntry was generated by an InboundTransferReturn.
 | 
issuing_authorization_holdThe TransactionEntry was generated by an Issuing authorization hold.
 | 
issuing_authorization_releaseThe TransactionEntry was generated by an Issuing authorization release.
 | 
otherThe TransactionEntry was generated by some other money movement.
 | 
outbound_paymentThe TransactionEntry was generated by an OutboundPayment.
 | 
outbound_payment_cancellationThe TransactionEntry was generated by a cancelled OutboundPayment.
 | 
Show 10 more | 
The TransactionEntry object```
`{  "id": "trxne_1MtkgV2eZvKYlo2CmofEnIwJ",  "object": "treasury.transaction_entry",  "balance_impact": {    "cash": 0,    "inbound_pending": 0,    "outbound_pending": -1000  },  "created": 1680756271,  "currency": "usd",  "effective_at": 1680756271,  "financial_account": "fa_1MtkgV2eZvKYlo2CdxyvnHeQ",  "flow": "obt_1MtkgV2eZvKYlo2CCxhXVFLB",  "flow_type": "outbound_transfer",  "livemode": false,  "transaction": "trxn_1MtkgV2eZvKYlo2CRYxD7KLh",  "type": "outbound_transfer"}`
```# [Retrieve a TransactionEntry](/api/treasury/transaction_entries/retrieve)Ask about this sectionCopy for LLMView as MarkdownRetrieves a TransactionEntry object.
### ParametersNo parameters.
### ReturnsReturns a TransactionEntry object.
GET /v1/treasury/transaction_entries/:id```
`curl https://api.stripe.com/v1/treasury/transaction_entries/trxne_1MtkgV2eZvKYlo2CmofEnIwJ \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "trxne_1MtkgV2eZvKYlo2CmofEnIwJ",  "object": "treasury.transaction_entry",  "balance_impact": {    "cash": 0,    "inbound_pending": 0,    "outbound_pending": -1000  },  "created": 1680756271,  "currency": "usd",  "effective_at": 1680756271,  "financial_account": "fa_1MtkgV2eZvKYlo2CdxyvnHeQ",  "flow": "obt_1MtkgV2eZvKYlo2CCxhXVFLB",  "flow_type": "outbound_transfer",  "livemode": false,  "transaction": "trxn_1MtkgV2eZvKYlo2CRYxD7KLh",  "type": "outbound_transfer"}`
```# [List all TransactionEntries](/api/treasury/transaction_entries/list)Ask about this sectionCopy for LLMView as MarkdownRetrieves a list of TransactionEntry objects.
### Parameters- #### financial_accountstringReturns objects associated with this FinancialAccount.
- #### createdobjectOnly return TransactionEntries that were created during the given date interval.
Show child parameters- #### order_byenumThe results are in reverse chronological order by created or effective_at. The default is created.
Possible enum valuescreatedTimestamp describing when the TransactionEntry was created.
 | 
effective_atTimestamp describing when the TransactionEntry was effective.
 | 
- #### transactionstringOnly return TransactionEntries associated with this Transaction.
### More parametersExpand all- #### ending_beforestring- #### limitinteger- #### starting_afterstring### ReturnsA dictionary with a data property that contains an array of up to limit TransactionEntries, starting after TransactionEntry starting_after. Each entry in the array is a separate TransactionEntry object. If no more TransactionEntries are available, the resulting array is empty.
GET /v1/treasury/transaction_entries```
`curl -G https://api.stripe.com/v1/treasury/transaction_entries \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d financial_account=fa_1MtkgV2eZvKYlo2CdxyvnHeQ \  -d limit=3`
```Response```
`{  "object": "list",  "url": "/v1/treasury/transaction_entries",  "has_more": false,  "data": [    {      "id": "trxne_1MtkgV2eZvKYlo2CmofEnIwJ",      "object": "treasury.transaction_entry",      "balance_impact": {        "cash": 0,        "inbound_pending": 0,        "outbound_pending": -1000      },      "created": 1680756271,      "currency": "usd",      "effective_at": 1680756271,      "financial_account": "fa_1MtkgV2eZvKYlo2CdxyvnHeQ",      "flow": "obt_1MtkgV2eZvKYlo2CCxhXVFLB",      "flow_type": "outbound_transfer",      "livemode": false,      "transaction": "trxn_1MtkgV2eZvKYlo2CRYxD7KLh",      "type": "outbound_transfer"    }  ]}`
```