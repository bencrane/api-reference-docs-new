Accounts | Stripe API Reference
          
          - 
          
          

          
        
        
          [](/api)Find anything/Ask AI[Introduction](https://docs.stripe.com/api)[Authentication](https://docs.stripe.com/api/authentication)[Errors](https://docs.stripe.com/api/errors)[Expanding Responses](https://docs.stripe.com/api/expanding_objects)[Idempotent requests](https://docs.stripe.com/api/idempotent_requests)[Include-dependent response values (API v2)](https://docs.stripe.com/api/include_dependent_response_values)[Metadata](https://docs.stripe.com/api/metadata)[Pagination](https://docs.stripe.com/api/pagination)[Request IDs](https://docs.stripe.com/api/request_ids)[Connected Accounts](https://docs.stripe.com/api/connected-accounts)[Versioning](https://docs.stripe.com/api/versioning)Core Resources[Accountsv2](https://docs.stripe.com/api/v2/core/accounts)[Account Linksv2](https://docs.stripe.com/api/v2/core/account-links)[Account Tokensv2](https://docs.stripe.com/api/v2/core/account-tokens)[Balance](https://docs.stripe.com/api/balance)[Balance Transactions](https://docs.stripe.com/api/balance_transactions)[Charges](https://docs.stripe.com/api/charges)[Customers](https://docs.stripe.com/api/customers)[Customer Session](https://docs.stripe.com/api/customer_sessions)[Disputes](https://docs.stripe.com/api/disputes)[Events](https://docs.stripe.com/api/events)[Eventsv2](https://docs.stripe.com/api/v2/core/events)[Event Destinationsv2](https://docs.stripe.com/api/v2/core/event-destinations)[Files](https://docs.stripe.com/api/files)[File Links](https://docs.stripe.com/api/file_links)[Mandates](https://docs.stripe.com/api/mandates)[Payment Intents](https://docs.stripe.com/api/payment_intents)[Personsv2](https://docs.stripe.com/api/v2/core/persons)[Person Tokensv2](https://docs.stripe.com/api/v2/core/person-tokens)[Setup Intents](https://docs.stripe.com/api/setup_intents)[Setup Attempts](https://docs.stripe.com/api/setup_attempts)[Payouts](https://docs.stripe.com/api/payouts)[Refunds](https://docs.stripe.com/api/refunds)[Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)[Tokens](https://docs.stripe.com/api/tokens)Payment Methods[Payment Methods](https://docs.stripe.com/api/payment_methods)[Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations)[Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)[Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)[Cash Balance](https://docs.stripe.com/api/cash_balance)[Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions)[Cards](https://docs.stripe.com/api/cards)[Sources](https://docs.stripe.com/api/sources)Products[Products](https://docs.stripe.com/api/products)[Prices](https://docs.stripe.com/api/prices)[Coupons](https://docs.stripe.com/api/coupons)[Promotion Code](https://docs.stripe.com/api/promotion_codes)[Discounts](https://docs.stripe.com/api/discounts)[Tax Code](https://docs.stripe.com/api/tax_codes)[Tax Rate](https://docs.stripe.com/api/tax_rates)[Shipping Rates](https://docs.stripe.com/api/shipping_rates)Checkout[Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)Payment Links[Payment Link](https://docs.stripe.com/api/payment-link)Billing[Alerts](https://docs.stripe.com/api/billing/alert)[Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary)[Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)[Credit Grant](https://docs.stripe.com/api/billing/credit-grant)[Credit Note](https://docs.stripe.com/api/credit_notes)[Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions)[Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations)[Customer Portal Session](https://docs.stripe.com/api/customer_portal/sessions)[Invoices](https://docs.stripe.com/api/invoices)[Invoice Items](https://docs.stripe.com/api/invoiceitems)[Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)[Invoice Payment](https://docs.stripe.com/api/invoice-payment)[Invoice Rendering Templates](https://docs.stripe.com/api/invoice-rendering-template)[Meters](https://docs.stripe.com/api/billing/meter)[Meter Events](https://docs.stripe.com/api/billing/meter-event)[Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)[Meter Event Adjustmentsv2](https://docs.stripe.com/api/v2/billing/meter-event-adjustments)[Meter Event Streamsv2](https://docs.stripe.com/api/v2/meter-event-streams)[Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)[Meter Eventsv2](https://docs.stripe.com/api/v2/meter-events)[Plans](https://docs.stripe.com/api/plans)[Quote](https://docs.stripe.com/api/quotes)[Subscriptions](https://docs.stripe.com/api/subscriptions)[Subscription Items](https://docs.stripe.com/api/subscription_items)[Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)[Tax IDs](https://docs.stripe.com/api/tax_ids)[Test Clocks](https://docs.stripe.com/api/test_clocks)Capital[Financing Offer](https://docs.stripe.com/api/capital/financing_offers)[Financing Summary](https://docs.stripe.com/api/capital/financing_summary)Connect[Accounts](https://docs.stripe.com/api/accounts)[Login Links](https://docs.stripe.com/api/accounts/login_link)[Account Links](https://docs.stripe.com/api/account_links)[Account Session](https://docs.stripe.com/api/account_sessions)[Application Fees](https://docs.stripe.com/api/application_fees)[Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)[Capabilities](https://docs.stripe.com/api/capabilities)[Country Specs](https://docs.stripe.com/api/country_specs)[Balance Settings](https://docs.stripe.com/api/balance-settings)[External Bank Accounts](https://docs.stripe.com/api/external_accounts)[External Account Cards](https://docs.stripe.com/api/external_account_cards)[Person](https://docs.stripe.com/api/persons)[Top-ups](https://docs.stripe.com/api/topups)[Transfers](https://docs.stripe.com/api/transfers)[Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)[Secrets](https://docs.stripe.com/api/secret_management)ReservesFraudIssuingTerminalTreasuryPayment RecordsAccount EvaluationEntitlementsSigmaReportingFinancial ConnectionsTaxIdentityCryptoClimateForwardingPrivacyWebhooks# [Accounts](/api/financial_connections/accounts)Ask about this sectionCopy for LLMView as MarkdownA Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
Endpoints[GET/v1/financial_connections/accounts/:id](/api/financial_connections/accounts/retrieve)[GET/v1/financial_connections/accounts](/api/financial_connections/accounts/list)[POST/v1/financial_connections/accounts/:id/disconnect](/api/financial_connections/accounts/disconnect)[POST/v1/financial_connections/accounts/:id/refresh](/api/financial_connections/accounts/refresh)[POST/v1/financial_connections/accounts/:id/subscribe](/api/financial_connections/accounts/subscribe)[POST/v1/financial_connections/accounts/:id/unsubscribe](/api/financial_connections/accounts/unsubscribe)# [The Account object](/api/financial_connections/accounts/object)Ask about this sectionCopy for LLMView as Markdown### Attributes#### idstringUnique identifier for the object.
- #### objectstringString representing the object’s type. Objects of the same type share the same value.
- #### account_holdernullable objectThe account holder that this account belongs to.
Show child attributes- #### account_numbersnullable array of objectsDetails about the account numbers.
Show child attributes- #### balancenullable objectThe most recent information about the account’s balance.
Show child attributes- #### balance_refreshnullable objectThe state of the most recent attempt to refresh the account balance.
Show child attributes- #### categoryenumThe type of the account. Account category is further divided in subcategory.
Possible enum valuescashThe account represents real funds held by the institution (e.g. a checking or savings account).
 | 
creditThe account represents credit extended by the institution (e.g. a credit card or mortgage).
 | 
investmentThe account represents investments, or any account where there are funds of unknown liquidity.
 | 
otherThe account does not fall under the other categories.
 | 
- #### createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- #### display_namenullable stringA human-readable name that has been assigned to this account, either by the account holder or by the institution.
- #### institution_namestringThe name of the institution that holds this account.
- #### last4nullable stringThe last 4 digits of the account number. If present, this will be 4 numeric characters.
- #### livemodebooleanIf the object exists in live mode, the value is true. If the object exists in test mode, the value is false.
- #### ownershipnullable stringExpandableThe most recent information about the account’s owners.
- #### ownership_refreshnullable objectThe state of the most recent attempt to refresh the account owners.
Show child attributes- #### permissionsnullable array of enumsThe list of permissions granted by this account.
Possible enum valuesbalancesAllows accessing balance data from the account.
 | 
ownershipAllows accessing ownership data from the account.
 | 
payment_methodAllows the creation of a payment method from the account.
 | 
transactionsAllows accessing transactions data from the account.
 | 
- #### statusenumThe status of the link to the account.
Possible enum valuesactiveStripe is able to retrieve data from the Account without issues.
 | 
disconnectedAccount connection has been terminated through the [disconnect API](/api/financial_connections/accounts/disconnect) or an [end user request](https://support.stripe.com/user/how-do-i-disconnect-my-linked-financial-account).
 | 
inactiveStripe cannot retrieve data from the Account.
 | 
- #### subcategoryenumIf category is cash, one of:
checking- savings- otherIf category is credit, one of:
- mortgage- line_of_credit- credit_card- otherIf category is investment or other, this will be other.
Possible enum valuescheckingThe account is a checking account.
 | 
credit_cardThe account represents a credit card.
 | 
line_of_creditThe account represents a line of credit.
 | 
mortgageThe account represents a mortgage.
 | 
otherThe account does not fall under any of the other subcategories.
 | 
savingsThe account is a savings account.
 | 
- #### subscriptionsnullable array of enumsThe list of data refresh subscriptions requested on this account.
Possible enum valuestransactionsSubscribes to periodic transactions data refreshes from the account.
 | 
- #### supported_payment_method_typesarray of enumsThe [PaymentMethod type](/api/payment_methods/object#payment_method_object-type)(s) that can be created from this account.
Possible enum valueslinkA link PaymentMethod can be created.
 | 
us_bank_accountA us_bank_account PaymentMethod can be created.
 | 
- #### transaction_refreshnullable objectThe state of the most recent attempt to refresh the account transactions.
Show child attributesThe Account object```
`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "financial_connections.account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`
```# [Retrieve an Account](/api/financial_connections/accounts/retrieve)Ask about this sectionCopy for LLMView as MarkdownRetrieves the details of an Financial Connections Account.
### ParametersNo parameters.
### ReturnsReturns an Account object if a valid identifier was provided, and raises [an error](#errors) otherwise.
GET /v1/financial_connections/accounts/:id```
`curl https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "financial_connections.account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "active",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`
```# [List Accounts](/api/financial_connections/accounts/list)Ask about this sectionCopy for LLMView as MarkdownReturns a list of Financial Connections Account objects.
### Parameters- #### account_holderobjectIf present, only return accounts that belong to the specified account holder. account_holder[customer] and account_holder[account] are mutually exclusive.
Show child parameters- #### sessionstringIf present, only return accounts that were collected as part of the given session.
### More parametersExpand all- #### ending_beforestring- #### limitinteger- #### starting_afterstring### ReturnsA dictionary with a data property that contains an array of up to limit Account objects, starting after account starting_after. Each entry in the array is a separate Account object. If no more accounts are available, the resulting array will be empty. This request will raise an error if more than one of account_holder[account], account_holder[customer], or session is specified.
GET /v1/financial_connections/accounts```
`curl -G https://api.stripe.com/v1/financial_connections/accounts \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \  -d limit=3`
```Response```
`{  "object": "list",  "url": "/v1/financial_connections/accounts",  "has_more": false,  "data": [    {      "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",      "object": "financial_connections.account",      "account_holder": {        "customer": "cus_9s6XI9OFIdpjIg",        "type": "customer"      },      "balance": null,      "balance_refresh": null,      "category": "cash",      "created": 1681412208,      "display_name": "Sample Checking Account",      "institution_name": "StripeBank",      "last4": "6789",      "livemode": false,      "ownership": null,      "ownership_refresh": null,      "permissions": [],      "status": "active",      "subcategory": "checking",      "subscriptions": [],      "supported_payment_method_types": [        "us_bank_account"      ],      "transaction_refresh": null    }  ]}`
```# [Disconnect an Account](/api/financial_connections/accounts/disconnect)Ask about this sectionCopy for LLMView as MarkdownDisables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).
### ParametersNo parameters.
### ReturnsReturns an Account object if a valid identifier was provided, and raises [an error](#errors) otherwise.
POST /v1/financial_connections/accounts/:id/disconnect```
`curl -X POST https://api.stripe.com/v1/financial_connections/accounts/fca_1MwVK82eZvKYlo2Cjw8FMxXf/disconnect \  -u "sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"`
```Response```
`{  "id": "fca_1MwVK82eZvKYlo2Cjw8FMxXf",  "object": "financial_connections.account",  "account_holder": {    "customer": "cus_9s6XI9OFIdpjIg",    "type": "customer"  },  "balance": null,  "balance_refresh": null,  "category": "cash",  "created": 1681412208,  "display_name": "Sample Checking Account",  "institution_name": "StripeBank",  "last4": "6789",  "livemode": false,  "ownership": null,  "ownership_refresh": null,  "permissions": [],  "status": "disconnected",  "subcategory": "checking",  "subscriptions": [],  "supported_payment_method_types": [    "us_bank_account"  ],  "transaction_refresh": null}`
```