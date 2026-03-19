# GraphQL API Reference​

URL: https://documentation.enigma.com/reference/graphql_api

info
This page has all of the context an LLM needs to construct GraphQL queries for the Enigma API. Try it by [downloading this document](/files/graphql_api.mdx) and providing it to an LLM.

Welcome to the Enigma GraphQL API reference. This API provides access to Enigma data and services through a flexible GraphQL interface.

This reference is intended for developers who are familiar with GraphQL and provides extensive details on the schema, queries, mutations, and more.

## Getting Started

You can interact with the Enigma GraphQL API through various means. Here, we will walk through a few common ones.

### GraphQL Playground

Head over to the [API Playground](https://console.enigma.com/explore/graphql) in the Enigma Console. Click on the "Execute query" button to run the example query.

![](/img/graphql/graphql_playground.png)
### Programmatic Access

#### Authentication

All API requests to the GraphQL API must include an `x-api-key` header with your API key:

```bash
x-api-key: YOUR_API_KEY
```

#### Base URL

The GraphQL API endpoint is:

```text
https://api.enigma.com/graphql
```

#### Making Requests

You can make requests to the GraphQL API using any GraphQL client. Here are examples (replace `YOUR_API_KEY` with your actual API key):

Curl
```bash
curl -i 'https://api.enigma.com/graphql' \
    -H 'content-type: application/json' \
    -H 'x-api-key: YOUR_API_KEY' \
    -d '{"query":"query{search(searchInput:{name:\"Enigma\",entityType:BRAND,address:{state:\"NY\",city:\"New York\"}}){... on Brand{names{edges{node{name}}}operatingLocations{edges{node{addresses(first:1){edges{node{fullAddress}}}}}}}}}"}'
```

Python
```python
import requests

    query = f"""
    query brandSearch($searchInput: SearchInput!) {{
        search(
            searchInput: $searchInput
        ) {{
            ... on Brand {{
                names {{
                    edges {{
                        node {{
                            name
                        }}
                    }}
                }}
                operatingLocations {{
                    edges {{
                        node {{
                            addresses(first: 1) {{
                                edges {{
                                    node {{
                                        fullAddress
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }}
        }}
    }}
    """

    variables =  {
        "searchInput": {
            "name": "Enigma",
            "entityType": "BRAND",
            "address": { "state": "NY", "city": "New York" }
        }
    }

    response=requests.post(
        'https://api.enigma.com/graphql',
        headers={"x-api-key":"YOUR_API_KEY"},
        json={"query": query, "variables": variables}
    )

    print(response.json())
```

Postman Postman provides handy tools for working with GraphQL requests. Refer to [Postman's documentation](https://learning.postman.com/docs/sending-requests/graphql/graphql-http/) on how to set up GraphQL requests on Postman.

### Usage with LLMs

Follow these best practices for using this documentation with an LLM:

- We find that [Claude](https://claude.ai/) most consistently generates correct GraphQL queries using this resource.
- Click [here](/files/graphql_api.mdx) to download this document as a markdown file and provide it to [Claude](https://claude.ai/) . When using the Claude app, ensure that Claude can read the content of the whole file dragging and dropping it into context, instead of selecting it through the "Upload a file" button.
- Direct [Claude](https://claude.ai/) to use the document in your prompt, for example: "Using the attached documentation, create a GraphQL query to ..."
[Contact us](https://www.enigma.com/contact-us) if you have any issues with your GraphQL query.

## GraphQL Schema Definition Language (SDL)

Find the GraphQL Schema Definition Language (SDL) below:

schema.graphql
```graphql
"""Exposes a URL that specifies the behavior of this scalar."""
directive @specifiedBy(
  """The URL that specifies the behavior of this scalar."""
  url: String!
) on SCALAR

type Account {
  customerId: ID
  customerEmail: String
  billingAccountId: ID
  pricingPlan: String
  creditsAvailable: Boolean
  autoRenewEnabled: Boolean
  autoRechargeDesiredState: Boolean
  autoRechargeCurrentState: Boolean
  autoRechargeThresholdAmount: Int
  autoRechargeRechargeToAmount: Int
  autoRechargeLimitUsd: Int
  autoRechargeReenableAfterTimestamp: String
}

"""
## [Description](#description)
The address is a physical street address for the business. We conform to the
standards provided by [USPS Publication
28](https://pe.usps.com/text/pub28/welcome.htm) where possible.

If information is available we indicate the specific street address and unit.
This means that two units in the same building appear as two distinct addresses.
Otherwise, the address may be a postal code or city/state rather than a complete
street address.
"""
type Address implements MathFunctions {
  """
  The complete address including street address, unit, city, state and ZIP code.
  The `full_address` field is rendered without punctuation.

  So for example "1223 18 MILE RD, STERLING HEIGHTS, MI 48314" becomes "1223 18 MILE RD STERLING HEIGHTS MI 48314".

  """
  fullAddress: String
  id: UUID!

  """
  Typically consists of a street number, street name, street type abbreviation,
  and, if available, abbreviated pre or post directionals. Where a streets has
  multiple names we attempt to provide the one indicated as the USPS standard.

  """
  streetAddress1: String

  """
  Contains any additional address information such as the unit, suite or floor
  number, or other information. We present this using [USPS standard
  abbreviations](https://pe.usps.com/text/pub28/28c2_003.htm).

  """
  streetAddress2: String

  """
  The city where this address is located.

  """
  city: String

  """
  The two-letter abbreviation of the U.S. state or territory.

  """
  state: String

  """
  The five-digit U.S. postal code of the address. If the address information
  pertains to an earlier period when a different postal code was used, we
  provide the postal code that is **currently** used.

  """
  zip: String
  firstObservedDate: String
  lastObservedDate: String

  """
  The county where this address is located.

  """
  county: String

  """
  The Metropolitan/Micropolitan Statistical Area where this address is located.

  """
  msa: String

  """
  The Combined Statistical Area where this address is located.

  """
  csa: String

  """
  The approximate latitude (decimal form) of the street address. We do not provide latitudes for all addresses.

  """
  latitude: Float

  """
  The approximate longitude (decimal form) of the street address. We do not provide longitudes for all addresses.

  """
  longitude: Float

  """
  The h3 index (resolution 10) corresponding to the latitude and longitude. We
  provide this as a convenience for geo-hashing applications.

  """
  h3Index: String

  """
  The three-digit ISO3 country code. We provide a country code where can
  unambiguously identify the country. Where the country code is null, it can
  generally be inferred that the address is located in the USA.

  """
  country: String
  internalId: String
  internalAddressId: String
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): AddressOperatingLocationConnection
  registrations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): AddressRegistrationConnection
  deliverabilities(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): AddressDeliverabilityConnection
  watchlistEntries(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): AddressWatchlistEntryConnection
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): AddressLegalEntityConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

"""
## [Description](#description)
The address is a physical street address for the business. We conform to the
standards provided by [USPS Publication
28](https://pe.usps.com/text/pub28/welcome.htm) where possible.

If information is available we indicate the specific street address and unit.
This means that two units in the same building appear as two distinct addresses.
Otherwise, the address may be a postal code or city/state rather than a complete
street address.
"""
type AddressDeliverability implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  Residential Delivery Indicator that indicates whether the USPS has identified
  the address as Residential or Commercial for mail delivery purposes.

  """
  rdi: String

  """
  The type of mail delivery for this address.  Values include
  * Street. a street address
  * Multi-Tenant Building. address contains apartment or building sub-units
  * Post Office Box
  * Firm. mail delivered and internally restributed to the recipient
  * Rural Route or Highway Contract Route
  * General Delivery. mail is held at local post office
  * null - there is not enough information to determine the delivery type

  """
  deliveryType: String

  """
  The possible values are * "deliverable” - The address is confirmed present in
  the USPS data and is not vacant. * “vacant” - The address is confirmed present
  in the USPS data but is vacant (most cases, unoccupied over 90 days) and is
  not receiving deliveries. * “not_deliverable” - USPS is temporarily declaring
  the address undeliverable. * null - there is not enough information to
  determine whether it's deliveral or not.
  """
  deliverable: String

  """
  The possible values are * "virtual_cmra" - The address is virtual and
  associated with a valid CMRA. * "not_virtual" - The address is not virtual and
  not associated with a CMRA. * null - there is not enough information to
  determine whether it's virtual or not.
  """
  virtual: String
  internalId: String
  internalAddressId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type AddressDeliverabilityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [AddressDeliverabilityEdge]!
}

"""A Relay edge containing a `AddressDeliverability` and its cursor."""
type AddressDeliverabilityEdge {
  """The item at the end of the edge"""
  node: AddressDeliverability

  """A cursor for use in pagination"""
  cursor: String!
}

input AddressInput {
  id: ID
  street1: String
  street2: String
  city: String
  state: String
  postalCode: String
}

type AddressLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [AddressLegalEntityEdge]!
}

"""A Relay edge containing a `AddressLegalEntity` and its cursor."""
type AddressLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityReceivesMailAtAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityReceivesMailAtAddressId: String
}

type AddressOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [AddressOperatingLocationEdge]!
}

"""A Relay edge containing a `AddressOperatingLocation` and its cursor."""
type AddressOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationOperatesAtAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationOperatesAtAddressId: String
}

type AddressRegistrationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [AddressRegistrationEdge]!
}

"""A Relay edge containing a `AddressRegistration` and its cursor."""
type AddressRegistrationEdge {
  """The item at the end of the edge"""
  node: Registration

  """A cursor for use in pagination"""
  cursor: String!
  registrationRecordedAddressId: UUID
  addressType: String
  rank: Int
  id: ID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalRegistrationRecordedAddressId: String
}

type AddressWatchlistEntryConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [AddressWatchlistEntryEdge]!
}

"""A Relay edge containing a `AddressWatchlistEntry` and its cursor."""
type AddressWatchlistEntryEdge {
  """The item at the end of the edge"""
  node: WatchlistEntry

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  addressAppearsOnWatchlistEntryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalAddressAppearsOnWatchlistEntryId: String
}

type AggregateResult {
  count(field: String!, conditions: Conditions): Int
}

type AttributeMetadata {
  rank: Int
  matched: String
}

type BackgroundTask {
  id: UUID!
  apiKeyId: String!
  backgroundTaskType: String!
  status: String!
  args: JSON
  result: JSON
  lastError: String
  executionAttempts: Int!
  etag: String!
  createdTimestamp: DateTime!
  updatedTimestamp: DateTime!
  lastExecutionTimestamp: DateTime
  nextExecutionTimestamp: DateTime!
}

type Brand implements MathFunctions & Entity {
  id: ID!
  internalId: String
  enigmaId: String
  tieBreakerMetadata: BrandTieBreakerMetadata
  searchMetadata: Searchmetadata
  names(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandNameConnection
  websites(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandWebsiteConnection
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandOperatingLocationConnection
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandLegalEntityConnection
  affiliatedBrands(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandBrandConnection
  cardTransactions(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandCardTransactionConnection
  industries(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandIndustryConnection
  revenueQualities(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandRevenueQualityConnection
  locationDescriptions(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandLocationDescriptionConnection
  isMarketables(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandIsMarketableConnection
  activities(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): BrandActivityConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
  minDate(field: String!, conditions: Conditions): Date @deprecated(reason: "Use minDateTime instead")
  maxDate(field: String!, conditions: Conditions): Date @deprecated(reason: "Use maxDateTime instead")
}

"""
## [Description](#description)
Identifies businesses that engage in activities with a high compliance risk.

## [Child attributes](#child-attributes)
- activity_type response values refer to high-risk categories of business activities.
- compliance_risk_level is `high` for all flagged businesses in Enigma KYB,
which will expand in future iterations to varying levels of risk.

## [Coverage](#coverage)
- Brands: We have classified ~130K brands as having high-risk activities. This
includes online-only businesses (those without any identifiable physical address).

## [Data sources](#data-sources)
- The "High-risk activities" attribute is derived from the list of names,
websites, and public web descriptions associated with a business via a set of
heuristics. Names and websites are derived from all Enigma data sources,
from card transactions to legal entity registrations.

## [Methodology](#methodology)
- Enigma looks for keywords through industry descriptions, names, and website
URLs associated with businesses. Enigma does not currently look at the content of a website.
- For example, to classify a business as having a high-risk activity of
"cannabis", Enigma looks for key terms within industry descriptions, names, and
website URLs: cannabis, marijuana, dispensary, CBD, THC, Ganja.

## [Why use Enigma KYB's high-risk classification?](#why-use-enigma-kybs-high-risk-classification)
- The Enigma high-risk classification improves automated customer onboarding by
identifying businesses that engage in activities with a high compliance risk,
allowing those businesses to be reviewed manually or follow additional risk
assessment processes before onboarding. This increases confidence in your
organization's automated onboarding workflow and ensures you're only bringing on
businesses that meet your desired risk standards.

## [High-risk categories](#high-risk-categories)
- Cannabis: Brick & mortar or online retail stores that primarily sell
cannabis/marijuana and related products (THC, CBD, etc.), cannabis/marijuana
growers or distributors, and software providers for the cannabis/marijuana industry.
- Tobacco and Vaping: Brick & mortar or online retail stores that primarily sell
tobacco and vaping products (cigarettes, cigars, e-cigarettes).
- Firearms, Weapons and Ammunition: Brick & mortar or online retailers that
primarily sell guns, firearms, weapons, and ammunition. or shooting ranges or
related locations.
- Adult Entertainment and Dating: Dating (online dating sites and applications),
Adult entertainment clubs (clubs that are primarily strip clubs, gentlemen's
clubs, sex clubs) but not businesses that are primarily just night clubs, adult
entertainment retail stores (e.g., sex shops, but not other types of stores like
lingerie stores), online adult entertainment sites (pornography sites, pay per
view chat sites/apps)
- Gambling and Sports Betting: Casinos, online gambling sites, sports betting
websites and B&M retail locations, fantasy sports leagues (but not other
sports-related businesses), bingo halls
- Payments and Money Transfer: Payment processors, POS providers, crowdfunding sites, factoring, lending services
- Multi-level marketing: Multi-level marketing, pyramid schemes
- Pawn Shops, Check Cashing and Payday Loans
- Cryptocurrencies and Digital Assets: Cryptocurrencies, blockchain, digital
assets, digital wallets, crypto/blockchain related infrastructure
- Investments and Financing: Investment brokers, lending instruments
- Legal Finance: Collections agencies, bail bonds
- Gift Cards: Gift card retailers, retail stores that buy unused gift cards,
websites whose primary purpose is selling gift cards
- Health and Lifestyle: Diet centers, supplements/nutraceuticals and other
products not regulated by the FDA, hair extensions
- Prescription Drugs: Pharmacies likely to sell prescription drugs
"""
type BrandActivity implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The type of high-risk activity associated with the business.
  High risk categories are: - Cannabis - Tobacco and Vaping - Firearms, Weapons
  and Ammunition - Adult Entertainment and Dating - Gambling and Sports Betting
  - Payments and Money Transfer - Multi-level marketing - Pawn Shops, Check
  Cashing and Payday Loans - Cryptocurrencies and Digital Assets - Investments
  and Financing - Legal Finance - Gift Cards - Health and Lifestyle -
  Prescription Drugs

  """
  activityType: String
  internalId: String
  internalBrandId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type BrandActivityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandActivityEdge]!
}

"""A Relay edge containing a `BrandActivity` and its cursor."""
type BrandActivityEdge {
  """The item at the end of the edge"""
  node: BrandActivity

  """A cursor for use in pagination"""
  cursor: String!
}

type BrandBrandConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandBrandEdge]!
}

"""A Relay edge containing a `BrandBrand` and its cursor."""
type BrandBrandEdge {
  """The item at the end of the edge"""
  node: Brand

  """A cursor for use in pagination"""
  cursor: String!
  brandIsAffiliatedWithBrandId: UUID
  rank: Int
  id: ID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  affiliationType: String
  internalId: String
  internalBrandIsAffiliatedWithBrandId: String
}

"""
## [Description](#description)
Contains quantitative information about the card transactions processed by the brand.

## [Data Sources](#data-sources)
The card transaction data is derived from a panel of around a third of all U.S. credit card transactions.
"""
type BrandCardTransaction implements MathFunctions {
  """
  This field indicates the type of quantity represented in the record.

  It may contain the following values:
  - **avg_transaction_size**: The record is the average transaction size in dollars for the brand for that time period.
  - **has_transactions**: The record is a 1 if the brand had any transactions in the time period, and 0 otherwise.
  - **refunds_amount**: The record is the total amount of refunds in dollars for the brand for that time period.
  - **card_transactions_count**: The record is the total number of card transactions for the brand for that time period.
  - **card_revenue_amount**: The record is the total sales amount in dollars for the brand for that time period.
  - **card_customers_average_daily_count**: The record is the average number of
  unique daily customers for the brand for that time period.
  - **card_revenue_yoy_growth**: The record is the ratio of the brand's current
  period's revenue to the period one year prior's revenue.
  - **card_revenue_prior_period_growth**: The record is the ratio of the brand's
  current period's revenue to the previous period's revenue.

  """
  quantityType: String

  """
  This field indicates the length of the time period represented in the record.

  It may contain the following values:
  - **1m**: One month.
  - **3m**: Three months.
  - **12m**: Twelve months.

  """
  period: String

  """
  This field contains the value for the quantity specified in quantity type. In
  cases where the underlying data is based on fewer than a threshold number of
  transactions required by the data provider for compliance reasons, this number
  may be null for all quantity_types except for "has_transactions".

  """
  projectedQuantity: Float

  """
  This field contains the brand id of the platform that processed the transaction.

  A null value indicates that the given quantity is not attributed to any particular platform.

  """
  platformBrandId: UUID
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  This field contains the start date of the time period represented in the record.

  """
  periodStartDate: Date

  """
  This field contains the end date of the time period represented in the record.

  """
  periodEndDate: Date
  internalId: String
  internalBrandId: String
  internalPlatformBrandId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type BrandCardTransactionConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandCardTransactionEdge]!
}

"""A Relay edge containing a `BrandCardTransaction` and its cursor."""
type BrandCardTransactionEdge {
  """The item at the end of the edge"""
  node: BrandCardTransaction

  """A cursor for use in pagination"""
  cursor: String!
}

type BrandConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandEdge]!
}

"""A Relay edge containing a `Brand` and its cursor."""
type BrandEdge {
  """The item at the end of the edge"""
  node: Brand

  """A cursor for use in pagination"""
  cursor: String!
}

type BrandIndustryConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandIndustryEdge]!
}

"""A Relay edge containing a `BrandIndustry` and its cursor."""
type BrandIndustryEdge {
  """The item at the end of the edge"""
  node: Industry

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  brandDoesBusinessWithinIndustryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalBrandDoesBusinessWithinIndustryId: String
}

"""
## [Description](#description)
Contains a boolean value indicating whether the brand is marketable.

## [Data Sources](#data-sources)
A brand is considered marketable if it meets certain criteria, like whether it
has open locations, revenue in the last 12 months, or reviews in the last 12 months.
"""
type BrandIsMarketable implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  This field contains a boolean value indicating whether the brand is marketable.

  """
  isMarketable: Boolean
  internalId: String
  internalBrandId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type BrandIsMarketableConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandIsMarketableEdge]!
}

"""A Relay edge containing a `BrandIsMarketable` and its cursor."""
type BrandIsMarketableEdge {
  """The item at the end of the edge"""
  node: BrandIsMarketable

  """A cursor for use in pagination"""
  cursor: String!
}

type BrandLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandLegalEntityEdge]!
}

"""A Relay edge containing a `BrandLegalEntity` and its cursor."""
type BrandLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityDoesBusinessAsBrandId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityDoesBusinessAsBrandId: String
}

"""
## [Description](#description)
A human-readable description of where a brand operates geographically, based on the states of its operating locations.

For brands with multiple locations, this shows the top states where the brand
has a significant presence (either more than 10% of locations or more than 5
locations). Up to 5 states are listed alphabetically (e.g., "CA, FL, NY, TX, WA"
or "CA, FL, NY, TX, WA and others" if there are more than 5 significant states).

For brands with a single location, this shows the specific city and state of that location (e.g., "San Francisco, CA").

This attribute provides a quick summary of a brand's geographic footprint
without needing to examine all individual locations.

## [Time Structure](#time-structure)
This attribute does not include time series data and reflects the most current state of the brand's locations.

## [Data Sources](#data-sources)
This attribute is derived from:
- Brand to operating location relationships
- Operating location to address relationships
- Address state and city information
"""
type BrandLocationDescription implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  A text description of the brand's geographic presence based on its operating locations.

  For brands with multiple locations, this shows up to 5 states where the brand
  has a significant presence, listed alphabetically. If there are more than 5
  significant states, "and others" is appended (e.g., "CA, FL, NY, TX, WA and others").

  For brands with a single location, this shows the specific city and state of that location (e.g., "San Francisco, CA").

  A state is considered significant if it contains either more than 10% of the brand's locations or more than 5 locations.

  """
  locationDescription: String
  internalId: String
  internalBrandId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type BrandLocationDescriptionConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandLocationDescriptionEdge]!
}

"""A Relay edge containing a `BrandLocationDescription` and its cursor."""
type BrandLocationDescriptionEdge {
  """The item at the end of the edge"""
  node: BrandLocationDescription

  """A cursor for use in pagination"""
  cursor: String!
}

"""
## [Description](#description)
The customer-facing version of the name that best represents the business.

## [Data Sources](#data-sources)
The brand name is derived from:
- Publicly available business data and listings
- Privately verified business information

## [Methodology](#methodology)
- Enigma uses high quality data sources to get the best representation of a
business name. Within those data sources, Enigma ranks by dataset quality and
frequency to determine the most likely name the business is referred to by.
- Persons: Agents/providers/business owners available in our data asset that are
branded as the business will use their person name as the brand name. The
company that employs the agents/providers will also have their own brand name
and an affiliated relationship with the agents/providers.
- Sub-brands/Franchises: Businesses that operate multiple other businesses, or
franchisers that are operated by multiple franchise locations available in our
data asset will be referred to by different brand names and have affiliated
brand relationships.
"""
type BrandName implements MathFunctions {
  """
  The customer-facing version of the name that best represents the business.

  This is generated by combining and ranking the business names from scraped data sources.

  """
  name: String
  nameFullTextSearchVector: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalBrandId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type BrandNameConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandNameEdge]!
}

"""A Relay edge containing a `BrandName` and its cursor."""
type BrandNameEdge {
  """The item at the end of the edge"""
  node: BrandName

  """A cursor for use in pagination"""
  cursor: String!
}

type BrandOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandOperatingLocationEdge]!
}

"""A Relay edge containing a `BrandOperatingLocation` and its cursor."""
type BrandOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  brandOperatesAtOperatingLocationId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalBrandOperatesAtOperatingLocationId: String
}

"""
## [Description](#description)
Warnings and issues related to the revenue of this brand.
"""
type BrandRevenueQuality implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The reason for the revenue quality issue.

  The reasons signify the following:
  - **REVENUE_DECREASE_TO_0_PCT_LOCATION_OPEN** (HIGH severity): Brand revenue
  drops to zero and at least 1 operating location is currently open.
  - **REVENUE_DECREASE_TO_20_PCT_LOCATION_OPEN** (HIGH severity): Brand revenue
  drops to 20% of the median revenue over the past 12 months and at least 1
  operating location is currently open.
  - **REVENUE_INCREASE_TO_250_PCT_IN_LAST_18M** (HIGH severity): Brand revenue
  increases to 250% of the median revenue for 3 months in the past 18 months.
  - **REVENUE_INCREASE_TO_250_PCT_ALL_TIME** (HIGH severity): Brand revenue
  increases to 250% of the median revenue for 3 months at any point in its
  revenue history.

  - **REVENUE_DECREASE_TO_0_PCT_LOCATION_UNKNOWN** (MEDIUM severity): Brand
  revenue drops to zero and the latest operating location operating status is stale.
  - **REVENUE_DECREASE_TO_20_PCT_LOCATION_UNKNOWN** (MEDIUM severity): Brand
  revenue drops to 20% of the median revenue over the past 12 months and the
  latest operating location operating status is stale.

  """
  issueReason: String

  """
  The severity of the revenue quality issue.

  """
  issueSeverity: String

  """
  A description of the revenue quality issue.

  """
  issueDescription: String
  internalId: String
  internalBrandId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type BrandRevenueQualityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandRevenueQualityEdge]!
}

"""A Relay edge containing a `BrandRevenueQuality` and its cursor."""
type BrandRevenueQualityEdge {
  """The item at the end of the edge"""
  node: BrandRevenueQuality

  """A cursor for use in pagination"""
  cursor: String!
}

type BrandTieBreakerMetadata {
  enigmaIdExists: RankMetadata
  websiteExists: RankMetadata
  operatingLocationCount: RankMetadata
}

type BrandWebsiteConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [BrandWebsiteEdge]!
}

"""A Relay edge containing a `BrandWebsite` and its cursor."""
type BrandWebsiteEdge {
  """The item at the end of the edge"""
  node: Website

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  brandOperatesWebsiteWebsiteId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalBrandOperatesWebsiteWebsiteId: String
}

type CancelListMaterialization {
  listMaterialization: ListMaterialization
}

input CancelListMaterializationInput {
  id: ID!
}

type ColumnCount {
  fullyQualifiedName: String!
  count: Int!
}

type ColumnMapping {
  columnName: String!
  searchField: ListSearchField!
}

input ColumnMappingInput {
  columnName: String!
  searchField: ListSearchField!
}

input Conditions {
  filter: JSON
  orderBy: [String]
  limit: Int
  pageToken: String
}

input ConnectionConditions {
  filter: JSON
  orderBy: [String]
}

type CreateList {
  list: List
  search: SearchUnion
}

input CreateListInput {
  name: String
  listType: ListType = LIST_GENERATION
  description: String
  searchInput: ListSearchInputInput = null
  fileFormat: String = "PARQUET"
  aliases: [FieldAliasInput]
  columnOrdering: [String]
  columnMapping: [ColumnMappingInput]
  inputFileUri: String
}

type CreateListMaterialization {
  listMaterialization: ListMaterialization
}

input CreateListMaterializationInput {
  listId: ID!
}

type CreateSuggestion {
  suggestion: Suggestion
}

"""
The `Date` scalar type represents a Date
value as specified by
[iso8601](https://en.wikipedia.org/wiki/ISO_8601).
"""
scalar Date

"""
The `DateTime` scalar type represents a DateTime
value as specified by
[iso8601](https://en.wikipedia.org/wiki/ISO_8601).
"""
scalar DateTime

type DeleteList {
  id: ID!
}

input DeleteListInput {
  id: ID!
}

"""
## [Description](#description)
An email address for the business or a person associated with the business.
"""
type EmailAddress implements MathFunctions {
  """
  The email address which consists of a user name, @ symbol, sub domain (optional) and domain.

  """
  emailAddress: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalEmailAddressId: String
  roles(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): EmailAddressRoleConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type EmailAddressRoleConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [EmailAddressRoleEdge]!
}

"""A Relay edge containing a `EmailAddressRole` and its cursor."""
type EmailAddressRoleEdge {
  """The item at the end of the edge"""
  node: Role

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  roleIsAssociatedWithEmailAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRoleIsAssociatedWithEmailAddressId: String
}

input EnrichmentInput {
  entityType: EntityType = null
  output: OutputSpec!
  sourceId: String!
  provider: EnrichmentProvider = null
  scoreThreshold: Float
}

"""An enumeration."""
enum EnrichmentProvider {
  ZOOMINFO
  SEARCH
}

interface Entity {
  id: ID!
  searchMetadata: Searchmetadata
}

input EntityIdentifier {
  id: String!
  type: EntityType!
}

"""An enumeration."""
enum EntityType {
  BRAND
  OPERATING_LOCATION
  LEGAL_ENTITY
}

type ExtendedSchema {
  types: [ExtendedSchemaType]
  projections: [ExtendedSchemaProjection]
  dataAssetMetadata: [ExtendedSchemaDataAsset]
}

type ExtendedSchemaDataAsset {
  namespace: String
  name: String
  value: String
  description: String
}

type ExtendedSchemaProjection {
  entity: String
  name: String
  label: String
  description: String
  fields: JSON
  path: JSON
  filter: JSON
  aggregation: JSON
}

type ExtendedSchemaType {
  name: String
  label: String
  description: String
  descriptionSimplified: String
  pricingTier: String
  fields: [ExtendedSchemaTypeField]
}

type ExtendedSchemaTypeField {
  name: String
  label: String
  description: String
  descriptionSimplified: String
  pricingTier: String
}

type ExternalMutation {
  createList(input: CreateListInput!): CreateList
  updateList(input: UpdateListInput!): UpdateList
  deleteList(input: DeleteListInput!): DeleteList
  createListMaterialization(input: CreateListMaterializationInput!): CreateListMaterialization
  cancelListMaterialization(input: CancelListMaterializationInput!): CancelListMaterialization
  updateListMaterialization(input: UpdateListMaterializationInput!): UpdateListMaterialization
  createSuggestion(suggestion: SuggestionInput!): CreateSuggestion
}

type FieldAlias {
  fullyQualifiedName: String!
  aliasName: String!
}

input FieldAliasInput {
  fullyQualifiedName: String!
  aliasName: String!
}

input GetListMaterializationInput {
  id: ID!
}

"""
## [Description](#description)
The industry within which the business operates.

Multiple distinct classification systems have been created to describe a businesses activity (e.g. NAICS, GICS, MCC, etc.).
Each classification system has advantages and drawbacks.  Rather than selecting
one, our approach is to provide multiple different classifications for each business.
We represent this as follows
* industry_type indicates the classification system (e.g. NAICS)
* industry_code is the code of a particular industry within a particular classification system
* industry_desc is the human readable description for the industry_code

For example, give an example of how NAICS would look.

Many of the traditional classification systems such as NAICS and GICS were
designed for statistical purposes by government or industry organizations.
While useful for many purposes, we've received feedback that for certain use
cases and business types these classifications systems lack the expressiveness
and detail to understand a businesses activity.
(for example, NAICS will be unhelpful in distinguishing between indian
restaurants and hamburger restaurants).  To address these limitations, we also
provide a non-hierarchical enigma_industry_description that provides a more
colloquial indication of the businesses primary activity.

## [Data Sources](#data-sources)
Industry data is derived from a variety of sources:
* company websites
* industry association memberships
* card transaction data
"""
type Industry implements MathFunctions {
  """
  Human-readable description of the industry.

  For industries with an industry_type that is an industry classification
  system, this will be the description corresponding to industry_code, provided
  by the developer of the industry classification system.

  """
  industryDesc: String

  """
  The numeric value of the industry code.  This field only contains a value for
  certain industry classification systems (The industry_type indicates the
  industry classification system).  For all other classification system, this field is null.

  """
  industryCode: String

  """
  The classification system used.  The *industry_type* determines the set of industry_code and industry_desc values.

    The industry_types we currently support are:
    - naics_2017_code
    - naics_2022_code
    - sic_code
    - mcc_code
    - enigma_industry_description

    The *enigma_industry_description* is a non-hierarchical, colloquial
  classification that often expresses dimensions of a business that are
  unavailable in standard industry classification systems (e.g. the style of
  food offered by a restaurant).
  description_simplified: The industry classification system used. Valid values
  are naics_2017_code, naics_2022_code, sic_code, mcc_code, and
  enigma_industry_description.

  """
  industryType: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalIndustryId: String
  brands(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): IndustryBrandConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type IndustryBrandConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [IndustryBrandEdge]!
}

"""A Relay edge containing a `IndustryBrand` and its cursor."""
type IndustryBrandEdge {
  """The item at the end of the edge"""
  node: Brand

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  brandDoesBusinessWithinIndustryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalBrandDoesBusinessWithinIndustryId: String
}

scalar JSON

"""
Allows use of a JSON String for input / output from the GraphQL schema.

Use of this type is *not recommended* as you lose the benefits of having a defined, static
schema (one of the key benefits of GraphQL).
"""
scalar JSONString

type LegalEntity implements MathFunctions & Entity {
  id: ID!
  internalId: String
  enigmaId: String
  tieBreakerMetadata: LegalEntityTieBreakerMetadata
  searchMetadata: Searchmetadata
  brands(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityBrandConnection
  names(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityNameConnection
  roles(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityRoleConnection
  persons(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityPersonConnection
  registeredEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityRegisteredEntityConnection
  tins(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityTinConnection
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityOperatingLocationConnection
  isFlaggedByWatchlistEntries(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityIsFlaggedByWatchlistEntryConnection
  appearsOnWatchlistEntries(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityAppearsOnWatchlistEntryConnection
  addresses(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityAddressConnection
  types(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityTypeConnection
  bankruptcies(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): LegalEntityBankruptcyConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type LegalEntityAddressConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityAddressEdge]!
}

"""A Relay edge containing a `LegalEntityAddress` and its cursor."""
type LegalEntityAddressEdge {
  """The item at the end of the edge"""
  node: Address

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityReceivesMailAtAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityReceivesMailAtAddressId: String
}

type LegalEntityAppearsOnWatchlistEntryConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityAppearsOnWatchlistEntryEdge]!
}

"""
A Relay edge containing a `LegalEntityAppearsOnWatchlistEntry` and its cursor.
"""
type LegalEntityAppearsOnWatchlistEntryEdge {
  """The item at the end of the edge"""
  node: WatchlistEntry

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityAppearsOnWatchlistEntryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityAppearsOnWatchlistEntryId: String
}

"""
## [Description](#description)
The details of the bankruptcy filing (chapter_type, filing date and case number etc.) a legal entity has ever filed.
All bankruptcy cases are handled in federal courts under rules outlined in the U.S. Bankruptcy Code.
"""
type LegalEntityBankruptcy implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The debtor's name on the filing.

  """
  debtorName: String

  """
  In a bankruptcy case, a trustee, appointed by the United States Trustee
  Program, oversees the process, ensuring fair and equitable distribution of
  assets, and may sell non-exempt property to repay creditors, depending on the
  chapter of bankruptcy.

  """
  trustee: String

  """
  Name of the bankruptcy court judge presiding over the case.

  """
  judge: String

  """
  The date the bankruptcy was filed.

  """
  filingDate: Date

  """
  There are different types of bankruptcies, which are usually referred to by their chapter in the U.S. Bankruptcy Code.
  - Individuals may file Chapter 7 or Chapter 13 bankruptcy, depending on the specifics of their situation.
  - Municipalities—cities, towns, villages, taxing districts, municipal
  utilities, and school districts may file under Chapter 9 to reorganize.
  - Businesses may file bankruptcy under Chapter 7 to liquidate or Chapter 11 to reorganize.
  - Chapter 12 provides debt relief to family farmers and fishermen.
  - Bankruptcy filings that involve parties from more than one country are filed under Chapter 15.

  """
  chapterType: String

  """
  For example, the first digit in the case number "2:14-bk-12345" represents the
  district court number, "14" means it was filed in year 2024, "bk" means
  bankruptcy case, and "12345" is the sequence number.

  """
  caseNumber: String

  """
  A voluntary filing is initiated by the debtor, while an involuntary filing is
  initiated by creditors who believe the debtor is unable to pay their debts.

  """
  petition: String

  """
  Date when the case was entered.

  """
  entryDate: Date

  """
  Date when the case was converted from chapter 11 to chapter 7.

  """
  dateConverted: Date

  """
  Date when the case was dismissed from court.

  """
  dateDismissed: Date

  """
  Final docket entry date, bankruptcy case closed.

  """
  dateTerminated: Date

  """
  Court enters the date when the plan is fulfilled and debtor has completed plan repayments.

  """
  debtorDischargedDate: Date

  """
  Date when the plan was confirmed.

  """
  planConfirmedDate: Date
  internalId: String
  internalLegalEntityId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type LegalEntityBankruptcyConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityBankruptcyEdge]!
}

"""A Relay edge containing a `LegalEntityBankruptcy` and its cursor."""
type LegalEntityBankruptcyEdge {
  """The item at the end of the edge"""
  node: LegalEntityBankruptcy

  """A cursor for use in pagination"""
  cursor: String!
}

type LegalEntityBrandConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityBrandEdge]!
}

"""A Relay edge containing a `LegalEntityBrand` and its cursor."""
type LegalEntityBrandEdge {
  """The item at the end of the edge"""
  node: Brand

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityDoesBusinessAsBrandId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityDoesBusinessAsBrandId: String
}

type LegalEntityIsFlaggedByWatchlistEntryConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityIsFlaggedByWatchlistEntryEdge]!
}

"""
A Relay edge containing a `LegalEntityIsFlaggedByWatchlistEntry` and its cursor.
"""
type LegalEntityIsFlaggedByWatchlistEntryEdge {
  """The item at the end of the edge"""
  node: WatchlistEntry

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityIsFlaggedByWatchlistEntryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  confidence: Float
  confidenceFields: String
  internalId: String
  internalLegalEntityIsFlaggedByWatchlistEntryId: String
}

"""
## [Description](#description)
These are entities which U.S. law recognizes as having an identity and rights.
They can be either natural persons, or artificial entities such as businesses and governmental bodies.
"""
type LegalEntityName implements MathFunctions {
  """
  The legal entity's name.

  """
  name: String
  nameFullTextSearchVector: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The legal form of the entity. This can either be "Person", for natural
  persons, or for business entities can be one of the following:

  - Co-operative
  - Corporation
  - General Partnership
  - Limited Cooperative Association
  - Limited Liability Company
  - Limited Partnership
  - Non-profit Co-operative
  - Non-profit Corporation
  - Non-profit Limited Liability Company
  - Non-profit Limited Partnership
  - Non-stock Co-operative
  - Non-stock Corporation
  - Person
  - Professional Corporation
  - Professional Limited Liability Company
  - Professional Limited Partnership
  - Sole Proprietorship
  - Unincorporated Non-profit Association
  - Unknown

  """
  legalEntityType: String
  internalId: String
  internalLegalEntityId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type LegalEntityNameConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityNameEdge]!
}

"""A Relay edge containing a `LegalEntityName` and its cursor."""
type LegalEntityNameEdge {
  """The item at the end of the edge"""
  node: LegalEntityName

  """A cursor for use in pagination"""
  cursor: String!
}

type LegalEntityOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityOperatingLocationEdge]!
}

"""
A Relay edge containing a `LegalEntityOperatingLocation` and its cursor.
"""
type LegalEntityOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityOwnsLocationOperatingLocationId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityOwnsLocationOperatingLocationId: String
}

type LegalEntityPersonConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityPersonEdge]!
}

"""A Relay edge containing a `LegalEntityPerson` and its cursor."""
type LegalEntityPersonEdge {
  """The item at the end of the edge"""
  node: Person

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  personIsInstanceOfLegalEntityId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalPersonIsInstanceOfLegalEntityId: String
}

type LegalEntityRegisteredEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityRegisteredEntityEdge]!
}

"""
A Relay edge containing a `LegalEntityRegisteredEntity` and its cursor.
"""
type LegalEntityRegisteredEntityEdge {
  """The item at the end of the edge"""
  node: RegisteredEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  registeredEntityIsInstanceOfLegalEntityId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRegisteredEntityIsInstanceOfLegalEntityId: String
}

type LegalEntityRoleConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityRoleEdge]!
}

"""A Relay edge containing a `LegalEntityRole` and its cursor."""
type LegalEntityRoleEdge {
  """The item at the end of the edge"""
  node: Role

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityPerformsRoleId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityPerformsRoleId: String
}

type LegalEntityTieBreakerMetadata {
  enigmaIdExists: RankMetadata
}

type LegalEntityTinConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityTinEdge]!
}

"""A Relay edge containing a `LegalEntityTin` and its cursor."""
type LegalEntityTinEdge {
  """The item at the end of the edge"""
  node: Tin

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityFilesTaxesUsingTinId: UUID
  rank: Int
  verificationStatus: String
  verificationResult: String
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalLegalEntityFilesTaxesUsingTinId: String
}

"""
## [Description](#description)
These are entities which U.S. law recognizes as having an identity and rights.
They can be either natural persons, or artificial entities such as businesses and governmental bodies.
"""
type LegalEntityType implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The legal form of the entity. This can either be "Person", for natural
  persons, or for business entities can be one of the following:

  - Co-operative
  - Corporation
  - General Partnership
  - Limited Cooperative Association
  - Limited Liability Company
  - Limited Partnership
  - Non-profit Co-operative
  - Non-profit Corporation
  - Non-profit Limited Liability Company
  - Non-profit Limited Partnership
  - Non-stock Co-operative
  - Non-stock Corporation
  - Person
  - Professional Corporation
  - Professional Limited Liability Company
  - Professional Limited Partnership
  - Sole Proprietorship
  - Unincorporated Non-profit Association
  - Unknown

  """
  legalEntityType: String
  internalId: String
  internalLegalEntityId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type LegalEntityTypeConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [LegalEntityTypeEdge]!
}

"""A Relay edge containing a `LegalEntityType` and its cursor."""
type LegalEntityTypeEdge {
  """The item at the end of the edge"""
  node: LegalEntityType

  """A cursor for use in pagination"""
  cursor: String!
}

type List {
  id: ID!
  listType: ListType
  name: String
  description: String
  searchInput: ListSearchInput
  createdTimestamp: DateTime!
  updatedTimestamp: DateTime!
  materializations(before: String, after: String, first: Int, last: Int): ListMaterializationConnection
  fileFormat: String
  inputFileUri: String
  columnCounts: [ColumnCount]
  fieldAliases: [FieldAlias]
  columnOrdering: [String]
  columnMapping: [ColumnMapping]
}

type ListConditions {
  filter: JSON
  orderBy: [String]
  limit: Int
}

input ListConditionsInput {
  filter: JSON
  orderBy: [String]
  limit: Int
}

type ListConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [ListEdge]!
}

"""A Relay edge containing a `List` and its cursor."""
type ListEdge {
  """The item at the end of the edge"""
  node: List

  """A cursor for use in pagination"""
  cursor: String!
}

type ListMaterialization {
  id: ID!
  listId: ID!
  createdTimestamp: DateTime!
  status: String!
  updatedTimestamp: DateTime!
  searchInput: ListSearchInput
  metrics(before: String, after: String, first: Int, last: Int): ListMaterializationMetricConnection
  billingEventDetails(before: String, after: String, first: Int, last: Int): ListMaterializationBillingEventDetailConnection
  fieldAliases: [FieldAlias]
  columnOrdering: [String]
  columnCounts: [ColumnCount]
  columnMapping: [ColumnMapping]
  inputFileUri: String
  listType: ListType
  resourceUri: String
  progressPercentComplete: Int
  progressMessage: String
}

type ListMaterializationBillingEventDetail {
  id: ID!
  listMaterializationId: ID!
  pricingTier: String!
  quantity: Int!
  entityType: String!
}

type ListMaterializationBillingEventDetailConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [ListMaterializationBillingEventDetailEdge]!
}

"""
A Relay edge containing a `ListMaterializationBillingEventDetail` and its cursor.
"""
type ListMaterializationBillingEventDetailEdge {
  """The item at the end of the edge"""
  node: ListMaterializationBillingEventDetail

  """A cursor for use in pagination"""
  cursor: String!
}

type ListMaterializationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [ListMaterializationEdge]!
}

"""A Relay edge containing a `ListMaterialization` and its cursor."""
type ListMaterializationEdge {
  """The item at the end of the edge"""
  node: ListMaterialization

  """A cursor for use in pagination"""
  cursor: String!
}

type ListMaterializationMetric {
  metricName: String!
  columnName: String
  metricValue: JSON
}

type ListMaterializationMetricConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [ListMaterializationMetricEdge]!
}

"""A Relay edge containing a `ListMaterializationMetric` and its cursor."""
type ListMaterializationMetricEdge {
  """The item at the end of the edge"""
  node: ListMaterializationMetric

  """A cursor for use in pagination"""
  cursor: String!
}

"""An enumeration."""
enum ListSearchField {
  NAME
  PERSON_FIRST_NAME
  PERSON_LAST_NAME
  WEBSITE
  ADDRESS_STREET1
  ADDRESS_STREET2
  ADDRESS_CITY
  ADDRESS_STATE
  ADDRESS_POSTAL_CODE
}

type ListSearchInput {
  entityType: EntityType!
  conditions: ListConditions
  prompt: String
  query: String
}

input ListSearchInputInput {
  entityType: EntityType = null
  conditions: ListConditionsInput = null
  prompt: String
  matchThreshold: Float
}

"""An enumeration."""
enum ListType {
  LIST_GENERATION
  ENRICHMENT
}

type MatchedMetadata {
  matched: String
}

interface MathFunctions {
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocation implements MathFunctions & Entity {
  operatingLocationCache(conditions: Conditions): [OperatingLocationCache]
  internalId: String
  enigmaId: String
  id: ID!
  tieBreakerMetadata: OperatingLocationTieBreakerMetadata
  searchMetadata: Searchmetadata
  names(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationNameConnection
  addresses(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationAddressConnection
  phoneNumbers(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationPhoneNumberConnection
  brands(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationBrandConnection
  roles(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationRoleConnection
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationLegalEntityConnection
  operatingStatuses(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationOperatingStatusConnection
  technologiesUseds(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationTechnologiesUsedConnection
  websites(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationWebsiteConnection
  reviewSummaries(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationReviewSummaryConnection
  isMarketables(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationIsMarketableConnection
  locationTypes(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationLocationTypeConnection
  ranks(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationRankConnection
  revenueQualities(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationRevenueQualityConnection
  cardTransactions(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): OperatingLocationCardTransactionConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationAddressConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationAddressEdge]!
}

"""A Relay edge containing a `OperatingLocationAddress` and its cursor."""
type OperatingLocationAddressEdge {
  """The item at the end of the edge"""
  node: Address

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationOperatesAtAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationOperatesAtAddressId: String
}

type OperatingLocationBrandConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationBrandEdge]!
}

"""A Relay edge containing a `OperatingLocationBrand` and its cursor."""
type OperatingLocationBrandEdge {
  """The item at the end of the edge"""
  node: Brand

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  brandOperatesAtOperatingLocationId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalBrandOperatesAtOperatingLocationId: String
}

type OperatingLocationCache {
  dummyColumn: String
  operatingLocationId: UUID!
  brandId: UUID
  latitude: Float
  longitude: Float
  websiteHttpStatusCode: Float
  latest12mCardRevenueRaw: Float
  latest12mCardRevenueProjected: Float
  latest12mYoyGrowthRaw: Float
  latest12mYoyGrowthProjected: Float
  latest12mCardTransactionsRaw: Float
  latest12mCardTransactionsProjected: Float
  websiteTechnologiesUsed: JSONString
  reviewCountAvg: Float
  name: String
  streetAddress1: String
  streetAddress2: String
  city: String
  state: String
  zip: String
  fullAddress: String
  website: String
  websiteAvailability: String
  websiteFirstObservedDate: String
  websiteLastObservedDate: String
  websiteFaviconUrl: String
  operatingStatus: String
  primaryBrandNaicsIndustry: String
  primaryBrandEnigmaIndustry: String
  rankPosition: Int
  rankCohortSize: Int
  phoneNumber: String
  hasRolePhoneNumber: Boolean
  hasRoleEmailAddress: Boolean
}

"""
## [Description](#description)
Contains quantitative information about the card transactions processed by the operating location.

## [Data Sources](#data-sources)
The card transaction data is derived from a panel of around a third of all U.S. credit card transactions.
"""
type OperatingLocationCardTransaction implements MathFunctions {
  """
  This field indicates the type of quantity represented in the record.

  It may contain the following values:
  - **avg_transaction_size**: The record is the average transaction size in dollars for the location for that time period.
  - **has_transactions**: The record is a 1 if the location had any transactions in the time period, and 0 otherwise.
  - **refunds_amount**: The record is the total amount of refunds in dollars for the location for that time period.
  - **card_transactions_count**: The record is the total number of card transactions for the location for that time period.
  - **card_revenue_amount**: The record is the total sales amount in dollars for the location for that time period.
  - **card_customers_average_daily_count**: The record is the average number of
  unique daily customers for the location for that time period.
  - **card_revenue_yoy_growth**: The record is the ratio of the location's
  current period's revenue to the period one year prior's revenue.
  - **card_revenue_prior_period_growth**: The record is the ratio of the
  location's current period's revenue to the previous period's revenue.

  """
  quantityType: String

  """
  This field indicates the length of the time period represented in the record.

  It may contain the following values:
  - **1m**: One month.
  - **3m**: Three months.
  - **12m**: Twelve months.

  """
  period: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  This field contains the raw value of the quantity specified in quantity_type.
  In cases where the underlying raw data is based on fewer than a threshold
  number of transactions required by the data provider for compliance reasons,
  this number may be null for all quantity_types except for "has_transactions".

  """
  rawQuantity: Float

  """
  This field contains the projected value for the quantity specified in quantity
  type. In cases where the underlying raw data is based on fewer than a
  threshold number of transactions required by the data provider for compliance
  reasons, this number may be null for all quantity_types except for
  "has_transactions".

  For quantity_types of ["avg_transaction_size",
  "card_revenue_prior_period_growth", "has_transactions",
  "card_revenue_yoy_growth"], this is usually the same as raw_quantity. In cases
  where the underlying raw data is based on fewer than a threshold number of
  transactions required by the merchant for compliance reasons, these numbers may not align.

  For quantity_types of ["refunds_amount", "card_transactions_count",
  "card_revenue_amount", "card_customers_average_daily_count"],
  projected_quantity is raw_quantity scaled up by a multiple that approximates
  the proportion of total card transactions the Enigma panel captures for the
  given location and time period. That multiple is based on features of the
  location, including geography, industry, and size, that are predictive of the
  proportion of transactions the panel includes.

  """
  projectedQuantity: Float

  """
  This field contains the date that begins the period for the record.

  """
  periodStartDate: Date

  """
  This field contains the date that ends the period for the record.

  """
  periodEndDate: Date
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationCardTransactionConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationCardTransactionEdge]!
}

"""
A Relay edge containing a `OperatingLocationCardTransaction` and its cursor.
"""
type OperatingLocationCardTransactionEdge {
  """The item at the end of the edge"""
  node: OperatingLocationCardTransaction

  """A cursor for use in pagination"""
  cursor: String!
}

"""
## [Description](#description)
Contains a boolean value indicating whether the operating location is marketable.

## [Data Sources](#data-sources)
An operating location is considered marketable if it meets certain criteria,
like whether it has an open status with recent data, revenue in the last 12
months, or reviews in the last 12 months.
"""
type OperatingLocationIsMarketable implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  This field contains a boolean value indicating whether the operating location is marketable.

  """
  isMarketable: Boolean
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationIsMarketableConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationIsMarketableEdge]!
}

"""
A Relay edge containing a `OperatingLocationIsMarketable` and its cursor.
"""
type OperatingLocationIsMarketableEdge {
  """The item at the end of the edge"""
  node: OperatingLocationIsMarketable

  """A cursor for use in pagination"""
  cursor: String!
}

type OperatingLocationLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationLegalEntityEdge]!
}

"""
A Relay edge containing a `OperatingLocationLegalEntity` and its cursor.
"""
type OperatingLocationLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityOwnsLocationOperatingLocationId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityOwnsLocationOperatingLocationId: String
}

"""
## [Description](#description)
The location type of the operating location--eg. retail, office, etc.

As an example, an operating location for Target at an address where a person can
go and shop would have location_type "retail".

An operating location for Target where a Target employee would go to work would have location_type = "office".
"""
type OperatingLocationLocationType implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The location type of the operating location.

  """
  locationType: String
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationLocationTypeConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationLocationTypeEdge]!
}

"""
A Relay edge containing a `OperatingLocationLocationType` and its cursor.
"""
type OperatingLocationLocationTypeEdge {
  """The item at the end of the edge"""
  node: OperatingLocationLocationType

  """A cursor for use in pagination"""
  cursor: String!
}

"""
## [Description](#description)
The name of the operating location.

An operating location is a place where business is conducted under a brand.
Most often is at a specific address.  If an address cannot be identified, a
phone number is considered sufficient.

An operating locations often have names that are distinct from the brand name.
Operating location names may indicate something distinct about that location.

As an example, the operating location name "Target - Crossgates Mall" indicates
both the brand "Target" and the location name "Crossgates Mall".
"""
type OperatingLocationName implements MathFunctions {
  nameFullTextSearchVector: String

  """
  The name of the operating location.

  """
  name: String!
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationNameConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationNameEdge]!
}

"""A Relay edge containing a `OperatingLocationName` and its cursor."""
type OperatingLocationNameEdge {
  """The item at the end of the edge"""
  node: OperatingLocationName

  """A cursor for use in pagination"""
  cursor: String!
}

"""
## [Description](#description)
Indicates whether a location is actively functioning ("Open"), out of operation
("Temporarily Closed", "Closed"), or of uncertain status ("Unknown").

## [Time Series](#time-series)
We maintain the operating status as a time series.  Each entry in the time
series represents an unbroken period of time where we observed the same
operating status.
The *rank* property indicates the order of the time series and
*first_observed_date* and *last_observed_date* indicate the beginning and end of the period.
- **Rank = 0**: Reflects the most recent Enigma, validated status observation.
- **Higher ranks (1, 2, etc.)**: Represent older, previously recorded statuses,
preserved for reference and limited historical tracking.

This structure lets you understand
* how the operating status has changed over time (e.g. temporary closures or seasonality)
* a lower bound for how long the business has been operating
* when a specific location has closed (this can be particularly helpful for
evaluating openings and closings in businesses with multiple locations)

## [Data Sources](#data-sources)
The operating status data is derived from:
- Publicly available business data and listings (Enigma observes the operating
status at least every three months, however, in many cases we are taking more
frequent observations)
- Privately verified business information

## [Operating Status Values](#operating-status-values)
- **Open**: Verified as open and functional through credible evidence or manual validation.
- **Temporarily Closed**: Trusted data indicates the business has temporarily
ceased operations, or the business is manually verified as temporarily closed.
- **Closed**: Trusted data indicates the business has ceased operations, or the business is manually verified as closed.
- **Unknown**: There is incomplete or insufficient information available to label the location as either Open or Closed.
"""
type OperatingLocationOperatingStatus implements MathFunctions {
  """
  This field reflects the operational state of the brand at this address during
  the time period shown. It may contain the following values: [Open, Closed,
  Temporarily Closed, Unknown].

  The statuses signify the following:
  - **Open**: Verified open and functional based on the latest checks.
  - **Temporarily Closed**: Verified as temporarily closed.
  - **Closed**: Verified no longer operating.
  - **Unknown**: Insufficient or unreliable data to determine a definitive status.

  """
  operatingStatus: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationOperatingStatusConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationOperatingStatusEdge]!
}

"""
A Relay edge containing a `OperatingLocationOperatingStatus` and its cursor.
"""
type OperatingLocationOperatingStatusEdge {
  """The item at the end of the edge"""
  node: OperatingLocationOperatingStatus

  """A cursor for use in pagination"""
  cursor: String!
}

type OperatingLocationPhoneNumberConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationPhoneNumberEdge]!
}

"""
A Relay edge containing a `OperatingLocationPhoneNumber` and its cursor.
"""
type OperatingLocationPhoneNumberEdge {
  """The item at the end of the edge"""
  node: PhoneNumber

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationCanBeCalledAtPhoneNumberId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationCanBeCalledAtPhoneNumberId: String
}

"""
## [Description](#description)
Indicates how the card revenue of this operating location compares to other
operating locations of the same enigma industry within the geographical area.

For example, if Joe's Pizza has a position of 5 and cohort size of 17, this
means, of all the pizza restaurants near Joe's Pizza, four locations have higher
card revenue and twelve locations have lower card revenue.

The geographic area is defined as the H3 index (resolution 4) of the address of the operating location.

There are a few reasons why an operating location does not have an operating location rank
* we're unable to determine the card revenue for the operating location
* fewer than ten operating locations with card revenue exist nearby within the
same industry (too few businesses to form a cohort)
"""
type OperatingLocationRank implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The quantity we're using to determine the ranking within a cohort.  At
  present, ranks will always be based on card_revenue.

  """
  quantityType: String

  """
  The period we're using to determine the ranking within a cohort.  At present,
  ranks will always be based on the most recent 12m for which revenue is available.

  """
  period: String

  """
  The absolute position of the operating location relative to its cohort. So if
  Joe's Pizza is ranked 5 out of 17 for area pizza restaurants, the position will equal 5.

  """
  position: Int

  """
  The number of operating locations in the cohort. For our Joe's Pizza example (5 of 17), the cohort size is 17.

  """
  cohortSize: Int

  """
  The date on which the *period* begins.  So if *period_start_date* is
  2024-01-15 and period is 12m, this means the 12m period we're using to rank
  the operating location began on Jan 15, 2024.

  """
  periodStartDate: Date

  """
  The date on which the *period* ends.  So if *period_end_date* is 2025-01-15
  and period is 12m, this means the 12m period we're using to rank the operating
  location ends on Jan 15, 2025.

  """
  periodEndDate: Date
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationRankConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationRankEdge]!
}

"""A Relay edge containing a `OperatingLocationRank` and its cursor."""
type OperatingLocationRankEdge {
  """The item at the end of the edge"""
  node: OperatingLocationRank

  """A cursor for use in pagination"""
  cursor: String!
}

"""
## [Description](#description)
Warnings and issues related to the revenue of this operating location.
"""
type OperatingLocationRevenueQuality implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The reason for the revenue quality issue.

  The reasons signify the following:
  - **OVER_100X_REVENUE_AND_20M_ANNUAL_REVENUE_EXTRAPOLATION** (HIGH severity):
  100x and $20M annual revenue extrapolated by our models from raw revenue sources.
  - **OVER_100X_REVENUE_EXTRAPOLATION** (HIGH severity): 100x revenue extrapolated by our models from raw revenue sources.
  - **OVER_20M_ANNUAL_REVENUE_EXTRAPOLATION** (HIGH severity): $20M annual
  revenue extrapolated by our models from raw revenue sources.
  - **REVENUE_DECREASE_TO_0_PCT_LOCATION_OPEN** (HIGH severity): Revenue drops
  to zero and location status is currently open.
  - **REVENUE_DECREASE_TO_20_PCT_LOCATION_OPEN** (HIGH severity): Revenue drop
  to 20% of the median revenue over the past 12 months and location status is
  currently open.
  - **CLOSED_BUT_STILL_HAVE_POSITIVE_REVENUE** (HIGH severity): Operating
  location is identified as Closed or Temporarily Closed for over 2 months but
  still has positive revenue.
  - **12M_REVENUE_LOWER_THAN_5K** (HIGH severity): 12m revenue <$5K for
  operating location that is card-accepting, mostly offline, not newly open.
  - **REVENUE_INCREASE_TO_250_PCT_IN_LAST_18M** (HIGH severity): Revenue
  increase to 250% of the median revenue for 3 months in the past 18 months.
  - **REVENUE_INCREASE_TO_250_PCT_ALL_TIME** (HIGH severity): Revenue increase
  to 250% of the median revenue for 3 months at any point in its revenue history.
  - **GREATER_THAN_10X_INTERQUARTILE_RANGE_ABOVE_Q3_WITHIN_BRAND** (HIGH
  severity): Operating location revenue in the last 12 months is 10x IQR over
  p75 of operating locations within brand.

  - **GREATER_THAN_5X_INTERQUARTILE_RANGE_ABOVE_Q3_WITHIN_BRAND** (MEDIUM
  severity): Operating location revenue in the last 12 months is 5x IQR over p75
  of operating locations within brand.
  - **OVERLY_HIGH_PCT_OF_BRAND_REV** (MEDIUM severity): Operating location
  contributes very high portion of revenue for the brand.
    - >10% brand revenue for brands with >= 100 open operating locations
    - >30% brand revenue for brands with >= 10 open operating locations
    - >50% brand revenue for brands with >= 4 open operating locations
  - **REVENUE_DECREASE_TO_0_PCT_LOCATION_UNKNOWN** (MEDIUM severity): Revenue
  drop to zero and location status is currently unknown.
  - **REVENUE_DECREASE_TO_20_PCT_LOCATION_UNKNOWN** (MEDIUM severity): Revenue
  drop to 20% of the median revenue over the past 12 months and location status
  is currently unknown.
  - **EXCEED_P99_WITHIN_4_DIGIT_NAICS** (MEDIUM severity): Operating location
  revenue is greater than 99th percentile revenue within its 4-digit naics code in last 12m.

  """
  issueReason: String

  """
  The severity of the revenue quality issue.

  """
  issueSeverity: String

  """
  A description of the revenue quality issue.

  """
  issueDescription: String
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationRevenueQualityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationRevenueQualityEdge]!
}

"""
A Relay edge containing a `OperatingLocationRevenueQuality` and its cursor.
"""
type OperatingLocationRevenueQualityEdge {
  """The item at the end of the edge"""
  node: OperatingLocationRevenueQuality

  """A cursor for use in pagination"""
  cursor: String!
}

type OperatingLocationReviewSummaryConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationReviewSummaryEdge]!
}

"""
A Relay edge containing a `OperatingLocationReviewSummary` and its cursor.
"""
type OperatingLocationReviewSummaryEdge {
  """The item at the end of the edge"""
  node: ReviewSummary

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationIsSubjectOfReviewSummaryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationIsSubjectOfReviewSummaryId: String
}

type OperatingLocationRoleConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationRoleEdge]!
}

"""A Relay edge containing a `OperatingLocationRole` and its cursor."""
type OperatingLocationRoleEdge {
  """The item at the end of the edge"""
  node: Role

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  roleIsPerformedAtOperatingLocationId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRoleIsPerformedAtOperatingLocationId: String
}

"""
## [Description](#description)
Indicates third-party technologies being used at a particular operating location.

## [Time Structure](#time-structure)

This attribute also includes a historical component through the **rank** property:

- **Rank = 0**: Reflects the most recent Enigma, validated observation of a technology being used at a location.
- **Higher ranks (1, 2, etc.)**: Represent older, previously recorded periods of
usage, preserved for reference and limited historical tracking.

Maintaining multiple ranks helps you see how a location's technology usage may
have changed over time, such as switching from one payment provider to another.

## [Data Sources](#data-sources)

Technologies are determined by parsing merchant identifiers from credit card transaction data.

## [Methodology](#methodology)

This data is sourced from private vendors that we independently verify for accuracy.
Currently we provide information only for payments-related technologies.

We currently identify Clover, Paypal, Shopify, Square, Stripe, and Toast.
"""
type OperatingLocationTechnologiesUsed implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  This field represents the specific third-party technology being used by the location.

  """
  technology: String

  """
  This field represents the category of the third-party technology being used by
  the location. An example would be "payments"

  """
  category: String
  internalId: String
  internalOperatingLocationId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type OperatingLocationTechnologiesUsedConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationTechnologiesUsedEdge]!
}

"""
A Relay edge containing a `OperatingLocationTechnologiesUsed` and its cursor.
"""
type OperatingLocationTechnologiesUsedEdge {
  """The item at the end of the edge"""
  node: OperatingLocationTechnologiesUsed

  """A cursor for use in pagination"""
  cursor: String!
}

type OperatingLocationTieBreakerMetadata {
  enigmaIdExists: RankMetadata
  operatingStatus: RankMetadata
}

type OperatingLocationWebsiteConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [OperatingLocationWebsiteEdge]!
}

"""A Relay edge containing a `OperatingLocationWebsite` and its cursor."""
type OperatingLocationWebsiteEdge {
  """The item at the end of the edge"""
  node: Website

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationOperatesWebsiteWebsiteId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationOperatesWebsiteWebsiteId: String
}

"""An enumeration."""
enum OutputFormat {
  PARQUET
  CSV
}

input OutputSpec {
  filename: String
  format: OutputFormat = null
}

"""
The Relay compliant `PageInfo` type, containing data necessary to paginate this connection.
"""
type PageInfo {
  """When paginating forwards, are there more items?"""
  hasNextPage: Boolean!

  """When paginating backwards, are there more items?"""
  hasPreviousPage: Boolean!

  """When paginating backwards, the cursor to continue."""
  startCursor: String

  """When paginating forwards, the cursor to continue."""
  endCursor: String
}

"""
## [Description](#description)
Persons, who may be associated with a business as an owner, officer or contact.
"""
type Person implements MathFunctions {
  """
  The person's first name.

  """
  firstName: String

  """
  The person's last name.

  """
  lastName: String

  """
  The person's full name.

  """
  fullName: String

  """
  The person's date of birth.

  """
  dateOfBirth: Date
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalPersonId: String
  fullNameFullTextSearchVector: String
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): PersonLegalEntityConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

input PersonInput {
  firstName: String
  lastName: String
  dateOfBirth: String
  address: AddressInput = null
  tin: TinInput = null
}

type PersonLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [PersonLegalEntityEdge]!
}

"""A Relay edge containing a `PersonLegalEntity` and its cursor."""
type PersonLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  personIsInstanceOfLegalEntityId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalPersonIsInstanceOfLegalEntityId: String
}

"""The phone number for a particular business entity."""
type PhoneNumber implements MathFunctions {
  """
  Twelve-digit string representation of the complete phone number (NANP compliant).

  The first characters is a plus sign.  The remaining eleven digits are always
  numbers.  These are the components based on the character index:
  - 0-1: "+1"
  - 2-4: area_code
  - 5-7: exchange_number
  - 8-11: line_number

  The phone number must have a valid U.S. area_code to be included.

  For example, the phone number "+19175362876" has the following components:
  - +1: the prefix
  - 917: the area_code
  - 536: the exchange_number
  - 2876: the line number

  """
  phoneNumber: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalPhoneNumberId: String
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): PhoneNumberOperatingLocationConnection
  roles(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): PhoneNumberRoleConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type PhoneNumberOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [PhoneNumberOperatingLocationEdge]!
}

"""
A Relay edge containing a `PhoneNumberOperatingLocation` and its cursor.
"""
type PhoneNumberOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationCanBeCalledAtPhoneNumberId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationCanBeCalledAtPhoneNumberId: String
}

type PhoneNumberRoleConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [PhoneNumberRoleEdge]!
}

"""A Relay edge containing a `PhoneNumberRole` and its cursor."""
type PhoneNumberRoleEdge {
  """The item at the end of the edge"""
  node: Role

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  roleIsAssociatedWithPhoneNumberId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRoleIsAssociatedWithPhoneNumberId: String
}

type Query {
  backgroundTask(id: String!): BackgroundTask
  search(searchInput: SearchInput!): [SearchUnion]
  aggregate(searchInput: SearchInput!): AggregateResult
  enrich(enrichmentInput: EnrichmentInput!): [SearchUnion]
  account: Account
  searchLists(input: SearchListsInput): ListConnection @deprecated(reason: "Renamed to lists")
  lists(input: SearchListsInput): ListConnection
  getListMaterialization(input: GetListMaterializationInput!): ListMaterialization @deprecated(reason: "Renamed to listMaterialization")
  listMaterialization(input: GetListMaterializationInput!): ListMaterialization
  _schemaExtended: ExtendedSchema
}

type RankMetadata {
  rank: Int
}

"""
## [Description](#description)
Businesses which have become legal entities by registering with a U.S. Secretary of State (SoS).

## [Data sources](#data-sources)
Each state's SoS is the ultimate source of truth for these records.

## [Methodology](#methodology)
A business may form in one state ("domestic registration"), and register with
other states to conduct business there ("foreign registration").
We join these records together to represent the single entity they constitute.
"""
type RegisteredEntity implements MathFunctions {
  """
  This is the standardized name of the entity, derived from the name as listed on the entity's registration.

  """
  name: String
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The standardized legal form of the entity, e.g. "Corporation", "LLC", etc.

  The possible values are:
  - Limited Partnership
  - Limited Liability Company
  - Corporation
  - Professional Limited Liability Company
  - Professional Corporation
  - Non-profit Corporation
  - Sole Proprietorship
  - Non-profit Limited Partnership
  - Non-stock Corporation
  - Non-profit Limited Liability Company
  - Professional Limited Partnership
  - Non-profit Co-operative
  - Non-stock Co-operative
  - Co-operative
  - Unknown
  - Unincorporated Non-profit Association
  - General Partnership
  - Limited Cooperative Association

  """
  registeredEntityType: String

  """
  The earliest non-null issue_date from the entity's registrations, formatted YYYY-MM-DD.

  """
  formationDate: Date

  """
  The year (YYYY) of the earliest non-null issue_date from the entity's registrations.

  """
  formationYear: Int
  internalId: String
  internalRegisteredEntityId: String
  nameFullTextSearchVector: String
  registrations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RegisteredEntityRegistrationConnection
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RegisteredEntityLegalEntityConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type RegisteredEntityLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RegisteredEntityLegalEntityEdge]!
}

"""
A Relay edge containing a `RegisteredEntityLegalEntity` and its cursor.
"""
type RegisteredEntityLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  registeredEntityIsInstanceOfLegalEntityId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRegisteredEntityIsInstanceOfLegalEntityId: String
}

type RegisteredEntityRegistrationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RegisteredEntityRegistrationEdge]!
}

"""
A Relay edge containing a `RegisteredEntityRegistration` and its cursor.
"""
type RegisteredEntityRegistrationEdge {
  """The item at the end of the edge"""
  node: Registration

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  registrationRegisteredRegisteredEntityId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRegistrationRegisteredRegisteredEntityId: String
}

"""
## [Description](#description)
Business registrations filed with a Secretary of State (or equivalent) in a U.S. state or territory.
These registrations either create a legal entity in that state ("domestic"
registrations) or allow an existing entity to do business in that state
("foreign" registrations). They are a source of truth about that business.
"""
type Registration implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The legal form of the registered entity, as given by the regististering jurisdiction's Secretary of State.

  """
  registrationType: String

  """
  The registration's expiration, if any.

  """
  expirationDate: Date

  """
  The US state where the registration was filed.

  """
  registrationState: String

  """
  `foreign` if the registration is for any state other than the business's home state. otherwise, `domestic`.

  """
  jurisdictionType: String

  """
  Two-letter abbreviation for the state jurisdiction of the business.

  """
  homeJurisdictionState: String

  """
  Business name as on the registration filing.

  """
  registeredName: String

  """
  File number of the registration filing.

  """
  fileNumber: String

  """
  Issue date of the registration filing, formatted YYYY/MM/DD.

  """
  issueDate: Date

  """
  Status field indicating whether the registration is active or inactive.

  """
  status: String

  """
  If available from the state, a normalized sub-status for the business.
  Possible values are: [good_standing, not_good_standing, pending_active,
  pending_inactive, unknown, null]

  The sub-status values signify the following:
  - good_standing - The business is active and in good standing.
  - not_good_standing - Non-compliant behavior, e.g. missing annual filing payments.
  - pending_active - In the process of becoming truly active.
  - pending_inactive - Businesses that are active, but are pending an inactive status.
  - unknown - The filing status from the state is not clearly in good or bad standing.
  - null - The filing status is inactive or there is no sub-status provided by the state.

  """
  subStatus: String

  """
  If available, the official filing status message provided by the state.

  """
  statusDetail: String
  internalId: String
  internalRegistrationId: String
  addresses(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RegistrationAddressConnection
  roles(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RegistrationRoleConnection
  registeredEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RegistrationRegisteredEntityConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type RegistrationAddressConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RegistrationAddressEdge]!
}

"""A Relay edge containing a `RegistrationAddress` and its cursor."""
type RegistrationAddressEdge {
  """The item at the end of the edge"""
  node: Address

  """A cursor for use in pagination"""
  cursor: String!
  registrationRecordedAddressId: UUID
  addressType: String
  rank: Int
  id: ID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalRegistrationRecordedAddressId: String
}

type RegistrationRegisteredEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RegistrationRegisteredEntityEdge]!
}

"""
A Relay edge containing a `RegistrationRegisteredEntity` and its cursor.
"""
type RegistrationRegisteredEntityEdge {
  """The item at the end of the edge"""
  node: RegisteredEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  registrationRegisteredRegisteredEntityId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRegistrationRegisteredRegisteredEntityId: String
}

type RegistrationRoleConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RegistrationRoleEdge]!
}

"""A Relay edge containing a `RegistrationRole` and its cursor."""
type RegistrationRoleEdge {
  """The item at the end of the edge"""
  node: Role

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  registrationRecordedRoleId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRegistrationRecordedRoleId: String
}

"""
## [Description](#description)
Summary of publicly available customer reviews for this entity.

## [Time Structure](#time-structure)

The review summary is a time series.

- **Rank = 0**: The most recent review summary has rank 0

- **Higher ranks (1, 2, etc.)**: Represent review summaries from earlier periods in time.

Healthy businesses will have a steadily increasing number of reviews overtime.
You can calculate the "review velocity" by measuring the difference in
review_count between time periods.  The review velocity may be a useful
indicator of business health.

## [Data Sources](#data-sources)

The status data is derived from:

- Actual customer reviews about business locations that are publicly available

## [Methodology](#methodology)

Sourced from publicly available customer reviews of locations.  This data is
updated at least every months for each location.
For simplicity, individual reviews are aggregated to provide an overview of a location.
It's possible for reviews to be removed or edited after some time, so it's possible you may
see the number of reviews *decrease* for a location at one point in time.
"""
type ReviewSummary implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The number of reviews submitted for a location.

  """
  reviewCount: String

  """
  The average rating of the reviews for a location.
  The average rating is the weighted average of reviews submitted by customers during the life of the location

  """
  reviewScoreAvg: String

  """
  The date of the earliest available review (from a sample of one hundred reviews).

  """
  firstReviewDate: Date

  """
  The date of the latest available review.
  Because up to three months may elapse before we refresh the reviews, more
  reviews may be submitted after this date that aren't reflected in our data.
  So a lag may develop which is removed at least every three months.

  """
  lastReviewDate: Date
  internalId: String
  internalReviewSummaryId: String
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): ReviewSummaryOperatingLocationConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type ReviewSummaryOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [ReviewSummaryOperatingLocationEdge]!
}

"""
A Relay edge containing a `ReviewSummaryOperatingLocation` and its cursor.
"""
type ReviewSummaryOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationIsSubjectOfReviewSummaryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationIsSubjectOfReviewSummaryId: String
}

"""
## [Description These are roles which people (and other legal entities) hold at U.S. businesses.](#description-these-are-roles-which-people-and-other-legal-entities-hold-at-us-businesses)
"""
type Role implements MathFunctions {
  externalId: JSON
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  A job title observed in our datasets of roles and employee contact details.

  """
  jobTitle: String

  """
  A standardized job description for this role, e.g. "Accounting", "Contracts", etc.

  """
  jobFunction: String

  """
  The management level for this role.

  """
  managementLevel: String
  externalUrls: JSON
  internalId: String
  internalRoleId: String
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RoleOperatingLocationConnection
  phoneNumbers(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RolePhoneNumberConnection
  emailAddresses(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RoleEmailAddressConnection
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RoleLegalEntityConnection
  registrations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): RoleRegistrationConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type RoleEmailAddressConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RoleEmailAddressEdge]!
}

"""A Relay edge containing a `RoleEmailAddress` and its cursor."""
type RoleEmailAddressEdge {
  """The item at the end of the edge"""
  node: EmailAddress

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  roleIsAssociatedWithEmailAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRoleIsAssociatedWithEmailAddressId: String
}

type RoleLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RoleLegalEntityEdge]!
}

"""A Relay edge containing a `RoleLegalEntity` and its cursor."""
type RoleLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityPerformsRoleId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityPerformsRoleId: String
}

type RoleOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RoleOperatingLocationEdge]!
}

"""A Relay edge containing a `RoleOperatingLocation` and its cursor."""
type RoleOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  roleIsPerformedAtOperatingLocationId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRoleIsPerformedAtOperatingLocationId: String
}

type RolePhoneNumberConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RolePhoneNumberEdge]!
}

"""A Relay edge containing a `RolePhoneNumber` and its cursor."""
type RolePhoneNumberEdge {
  """The item at the end of the edge"""
  node: PhoneNumber

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  roleIsAssociatedWithPhoneNumberId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRoleIsAssociatedWithPhoneNumberId: String
}

type RoleRegistrationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [RoleRegistrationEdge]!
}

"""A Relay edge containing a `RoleRegistration` and its cursor."""
type RoleRegistrationEdge {
  """The item at the end of the edge"""
  node: Registration

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  registrationRecordedRoleId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalRegistrationRecordedRoleId: String
}

input SearchInput {
  prompt: String
  id: String
  name: String
  address: AddressInput = null
  addresses: [AddressInput]
  person: PersonInput = null
  phoneNumber: String
  website: String
  conditions: Conditions = null
  tin: TinInput = null
  matchThreshold: Float
  entityType: EntityType = null
  engine: String
  output: OutputSpec = null

  """S3 path to parquet file containing internal_id column for filtering"""
  enrichmentIdsS3Path: String
}

input SearchListsInput {
  id: ID
  name: String
  conditions: ConnectionConditions = null
  first: Int
  after: String
  last: Int
  before: String
}

type Searchmetadata {
  website: AttributeMetadata
  phoneNumber: AttributeMetadata
  fullTextName: AttributeMetadata
  trigramName: AttributeMetadata
  embedding: AttributeMetadata
  prompt: AttributeMetadata
  address: RankMetadata
  addressStreet1: MatchedMetadata
  addressStreet2: MatchedMetadata
  addressCity: MatchedMetadata
  addressState: MatchedMetadata
  addressPostalCode: MatchedMetadata
}

union SearchUnion = LegalEntity | Brand | OperatingLocation

type Suggestion {
  id: UUID!
  revision: ID!
  apiKeyId: String!
  dataAssetVersion: String!
  payload: JSONString!
  createdTimestamp: DateTime
  requestId: String!
  suggestedByEmail: String
  lastModifiedByEmail: String
  status: String!
}

input SuggestionInput {
  suggestedByEmail: String
  payload: JSON = null
  status: SuggestionStatusEnum = null
  suggestedValue: JSON
  ancestorIdentifier: [EntityIdentifier]
  suggestedEntityIdentifier: EntityIdentifier = null
  field: String
}

enum SuggestionStatusEnum {
  APPROVED
  REJECTED
  PENDING_REVIEW
}

"""
## [Description](#description)
Taxpayer Identification Number (TIN). Identification number used by the Internal
Revenue Service (IRS) in the administration of tax laws.
"""
type Tin implements MathFunctions {
  id: UUID!

  """
  Taxpayer Identification Number (TIN). Identification number used by the
  Internal Revenue Service (IRS) in the administration of tax laws.

  """
  tin: String

  """
  Type of TIN. One of [SSN, EIN, ITIN, ATIN and PTIN].

  """
  tinType: String

  """
  The possible values are * invalid - The TIN is invalid. * not_issued - The TIN
  has not been issued by IRS. * issued - The TIN is valid and issued by IRS. *
  null - The validity has not not been confirmed.
  """
  validity: String
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalTinId: String
  legalEntities(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): TinLegalEntityConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

input TinInput {
  tin: String
  tinType: TinType = null
}

type TinLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [TinLegalEntityEdge]!
}

"""A Relay edge containing a `TinLegalEntity` and its cursor."""
type TinLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityFilesTaxesUsingTinId: UUID
  rank: Int
  verificationStatus: String
  verificationResult: String
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalLegalEntityFilesTaxesUsingTinId: String
}

"""An enumeration."""
enum TinType {
  EIN
  SSN
  ITIN
  TIN
}

type UpdateList {
  list: List
  search: SearchUnion
}

input UpdateListInput {
  id: ID!
  name: String
  description: String
  searchInput: ListSearchInputInput = null
  aliases: [FieldAliasInput]
  columnOrdering: [String]
  columnMapping: [ColumnMappingInput]
}

type UpdateListMaterialization {
  listMaterialization: ListMaterialization
}

input UpdateListMaterializationInput {
  id: ID!
  status: String
}

"""
Leverages the internal Python implementation of UUID (uuid.UUID) to provide native UUID objects
in fields, resolvers and input.
"""
scalar UUID

"""
## [Description](#description)
Watchlist entities draw from the following publications of the Office of Foreign Assets Control (OFAC):
* Specially Designated Nationals and Blocked Persons List (SDN)
* Consolidated Sanctions List (Non-SDN): this includes the Foreign Sanctions
Evaders List (FSE), Sectoral Sanctions Identifications List (SSI), Palestinian
Legislative Council List (PLC), List of Foreign Financial Institutions Subject
to Correspondent Account or Payable-Through Account Sanctions (CAPTA), Non-SDN
Menu-Based Sanctions List (NS-MBS), and the Non-SDN Chinese Military-Industrial
Complex Companies List (NS-CMIC).
"""
type WatchlistEntry implements MathFunctions {
  id: UUID!

  """
  Name of the watchlist, including SDN and Non-SDN.

  """
  watchlistName: String
  firstObservedDate: String
  lastObservedDate: String
  internalId: String
  internalWatchlistEntryId: String
  legalEntitiesIsFlaggedBy(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WatchlistEntryIsFlaggedByLegalEntityConnection
  legalEntitiesAppearsOn(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WatchlistEntryAppearsOnLegalEntityConnection
  addresses(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WatchlistEntryAddressConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type WatchlistEntryAddressConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WatchlistEntryAddressEdge]!
}

"""A Relay edge containing a `WatchlistEntryAddress` and its cursor."""
type WatchlistEntryAddressEdge {
  """The item at the end of the edge"""
  node: Address

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  addressAppearsOnWatchlistEntryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalAddressAppearsOnWatchlistEntryId: String
}

type WatchlistEntryAppearsOnLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WatchlistEntryAppearsOnLegalEntityEdge]!
}

"""
A Relay edge containing a `WatchlistEntryAppearsOnLegalEntity` and its cursor.
"""
type WatchlistEntryAppearsOnLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityAppearsOnWatchlistEntryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityAppearsOnWatchlistEntryId: String
}

type WatchlistEntryIsFlaggedByLegalEntityConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WatchlistEntryIsFlaggedByLegalEntityEdge]!
}

"""
A Relay edge containing a `WatchlistEntryIsFlaggedByLegalEntity` and its cursor.
"""
type WatchlistEntryIsFlaggedByLegalEntityEdge {
  """The item at the end of the edge"""
  node: LegalEntity

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  legalEntityIsFlaggedByWatchlistEntryId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  confidence: Float
  confidenceFields: String
  internalId: String
  internalLegalEntityIsFlaggedByWatchlistEntryId: String
}

"""
## [Description](#description)

A website associated with a business.
"""
type Website implements MathFunctions {
  """
  The complete url of the website including protocol, subdomain and path

  """
  website: String
  firstObservedDate: String
  id: UUID!
  lastObservedDate: String

  """
  The subdomain component of the website (e.g. "documentation" in
  "https://documentation.enigma.com/getting_started/introduction")

  """
  subdomain: String

  """
  The subdomain component of the website (e.g. "enigma" in "https://documentation.enigma.com/getting_started/introduction")

  """
  domain: String

  """
  The top_level_domain (a.k.a. tld) component of the website (e.g. "com" in
  "https://documentation.enigma.com/getting_started/introduction")

  """
  topLevelDomain: String

  """
  The path component of the website (e.g. "getting_started/introduction" in
  "https://documentation.enigma.com/getting_started/introduction")

  """
  path: String

  """
  The fragment component of the website (e.g. "getting_started/introduction" in
  "https://documentation.enigma.com/getting_started/introduction")

  """
  fragment: String
  internalId: String
  internalWebsiteId: String
  brands(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WebsiteBrandConnection
  operatingLocations(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WebsiteOperatingLocationConnection
  websiteContents(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WebsiteWebsiteContentConnection
  technologiesUseds(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): WebsiteTechnologiesUsedConnection
  onlinePresences(first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions): WebsiteOnlinePresenceConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type WebsiteBrandConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WebsiteBrandEdge]!
}

"""A Relay edge containing a `WebsiteBrand` and its cursor."""
type WebsiteBrandEdge {
  """The item at the end of the edge"""
  node: Brand

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  brandOperatesWebsiteWebsiteId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalBrandOperatesWebsiteWebsiteId: String
}

"""
## [Description](#description)
The state of the website at a particular time.

We make a request to each website in our database at least every ninety days.
Each *website_content* object represents what we learned on one of those requests.

## [Time Structure](#time-structure)

This attribute has a historical dimension which is represented by the **rank** property:
- **Rank = 0**: Data from the most recent website request.
- **Higher ranks (1, 2, etc.)**: Data from earlier website requests (higher ranks represent earlier requests)

This structure allows us to answer questions such as
- when did this website become unavailable and begin returning 404 errors?
- when did this website switch it's favicon (which may indicate a rebranding or acquisition)?
"""
type WebsiteContent implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  The HTTP status code returned by the request (e.g. 200, 404, etc.)

  """
  httpStatusCode: String

  """
  The url from which the website's favicon was served.

  """
  faviconUrl: String

  """
  A binary representation of the website's favicon that was returned from the HTTP request.

  """
  faviconImage: String
  websiteAvailability: String
  internalId: String
  internalWebsiteContentId: String
  websites(first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions): WebsiteContentWebsiteConnection
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type WebsiteContentWebsiteConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WebsiteContentWebsiteEdge]!
}

"""A Relay edge containing a `WebsiteContentWebsite` and its cursor."""
type WebsiteContentWebsiteEdge {
  """The item at the end of the edge"""
  node: Website

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  websiteServesWebsiteContentId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalWebsiteServesWebsiteContentId: String
}

"""
## [Description](#description)
Indicates whether a website is an e-commerce website that sells products directly online.

Enigma analyzes a variety of key indicators that suggest online shopping capabilities to identify e-commerce websites.

## [Time Structure](#time-structure)

This attribute does not include time series data and always reflects the most current status.

## [Data Sources](#data-sources)

The data is derived from actual business websites that are publicly available.
"""
type WebsiteOnlinePresence implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  Includes two values:
  - **Yes**: Strong indications suggests that the website is an e-commerce website selling products directly online.
  - **null**: Insufficient indications or lack of information prevents us from making a determination.

  """
  hasOnlineSales: String
  internalId: String
  internalWebsiteId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type WebsiteOnlinePresenceConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WebsiteOnlinePresenceEdge]!
}

"""A Relay edge containing a `WebsiteOnlinePresence` and its cursor."""
type WebsiteOnlinePresenceEdge {
  """The item at the end of the edge"""
  node: WebsiteOnlinePresence

  """A cursor for use in pagination"""
  cursor: String!
}

type WebsiteOperatingLocationConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WebsiteOperatingLocationEdge]!
}

"""A Relay edge containing a `WebsiteOperatingLocation` and its cursor."""
type WebsiteOperatingLocationEdge {
  """The item at the end of the edge"""
  node: OperatingLocation

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  operatingLocationOperatesWebsiteWebsiteId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalOperatingLocationOperatesWebsiteWebsiteId: String
}

"""
## [Description](#description)
Indicates third-party technologies used by a website.

## [Time Structure](#time-structure)

This attribute also includes a historical component through the **rank** property:

- **Rank = 0**: Reflects the most recent Enigma, validated observation of a technology being used on a website.
- **Higher ranks (1, 2, etc.)**: Represent older, previously recorded periods of
usage, preserved for reference and limited historical tracking.

Maintaining multiple ranks helps you see how a website's technology usage may
have changed over time, such as switching from one payment provider to another.

## [Data Sources](#data-sources)

Technologies are determined by scraping a website and identifying resources within the website content.

## [Methodology](#methodology)

This data is sourced from private vendors that we independently verify for accuracy.
Currently we provide information only for payments-related technologies.

We currently identify Adyen, Braintree, PayPal, Shopify, and Stripe.
"""
type WebsiteTechnologiesUsed implements MathFunctions {
  id: UUID!
  firstObservedDate: String
  lastObservedDate: String

  """
  This field represents the specific third-party technology being used by the website.

  """
  technology: String

  """
  This field represents the category of the third-party technology being used by the website. An example would be "payments"

  """
  category: String
  internalId: String
  internalWebsiteId: String
  count(field: String!, conditions: Conditions): Int
  sum(field: String!, conditions: Conditions): Int
  min(field: String!, conditions: Conditions): Int
  max(field: String!, conditions: Conditions): Int
  avg(field: String!, conditions: Conditions): Float
  collect(field: String!, separator: String, conditions: Conditions): String
  minDateTime(field: String!, conditions: Conditions): DateTime
  maxDateTime(field: String!, conditions: Conditions): DateTime
}

type WebsiteTechnologiesUsedConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WebsiteTechnologiesUsedEdge]!
}

"""A Relay edge containing a `WebsiteTechnologiesUsed` and its cursor."""
type WebsiteTechnologiesUsedEdge {
  """The item at the end of the edge"""
  node: WebsiteTechnologiesUsed

  """A cursor for use in pagination"""
  cursor: String!
}

type WebsiteWebsiteContentConnection {
  """Pagination data for this connection."""
  pageInfo: PageInfo!

  """Contains the nodes in this connection."""
  edges: [WebsiteWebsiteContentEdge]!
}

"""A Relay edge containing a `WebsiteWebsiteContent` and its cursor."""
type WebsiteWebsiteContentEdge {
  """The item at the end of the edge"""
  node: WebsiteContent

  """A cursor for use in pagination"""
  cursor: String!
  id: ID
  websiteServesWebsiteContentId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalWebsiteServesWebsiteContentId: String
}
```

## Queries

### Search

The `search` query is for discovering and retrieving entities from Enigma data.

#### Request Parameters

##### SearchInput

`SearchInput` is a required input field for the search query. This table describes the input fields in `SearchInput` :

| **Input Field** | **Description** | **Example** 
| `prompt` | A description of the business. The description should contain only attributes of the business, such as "fast food", "pizza restaurant", "bar", "mexican restaurant in new york" etc. This input field is only supported for the entity type ( `entityType` ) `BRAND` so `entityType` must equal `BRAND` . This field must not be used in conjunction with `id` , `name` , `website` , and `address` . | - "fast food"
- "pizza" 
| `id` | The ID of the entity. Takes precedence over all other input fields. `id` should be used in conjunction with `entityType` to specify which entity this ID belongs to. | 2daa02e4-f887-40f5-8bd2-c00764b91e76 
| `name` | The name of the business. | McDonald's 
| `address` | The various components of an address to filter by:
- `id` (optional): ID of the address
- `street1` (optional): the first part of a street address (e.g. 123 Main St.)
- `street2` (optional): the second part of a street address (e.g. Fl 8)
- `city` (optional): the city name
- `state` (optional): the two letter state abbreviation
- `postalCode` (optional): the ZIP code | `{ "street1": "123 Main St.", "street2": "Apt. 8", "city": "NEW YORK", "state": "NY", "postalCode": "10013" }` 
| `addresses` | A list of `addresses` . Either `address` or `addresses` can be specified, not both. This input field is only supported for `aggregate` . | `[{ "street1": "123 Main St.", "street2": "Apt. 8", "city": "New York", "state": "NY", "postalCode": "10013" }, { "street1": "456 Main St.", "city": "New York", "state": "NY", "postalCode": "10013" }]` 
| `person` | A person's information to search by, such as:
- `firstName` (optional)
- `lastName` (optional)
- `dateOfBirth` (optional): date of birth in ISO 8601 date format (i.e. YYYY-MM-DD)
- `address` (optional)
- `tin` (optional): the TIN of the person. The inner `tin` number (9-digit string) is required. If provided, `firstName` and `lastName` must also be specified. | `{ "firstName": "John", "lastName": "Doe", "dateOfBirth": "1980-01-01", "address": { "street1": "123 Main St.", "city": "New York", "state": "NY", "postalCode": "10013" }, "tin": { "tin": "123456789", "tinType": "SSN" } }` 
| `phoneNumber` | A 10-digit U.S. phone number in the format ########## (e.g. 1234567890) or ###-###- # (e.g. 123-456-7890) | - 1234567890
- 123-456-7890 
| `website` | A website (Can search by just website) | - enigma.com
- [www.enigma.com](http://www.enigma.com)
- [https://www.enigma.com/](https://www.enigma.com/) 
| `conditions` | Conditions to customize the result by, including:
- `filter` (optional): a JSON object to specify filtering of attributes
- `orderBy` (optional): a list of attributes and sort ordering
- `limit` (optional): an integer to limit the top-level result by
- `pageToken` (optional): a numeric offset represented as a string to start returning results from (e.g. a `pageToken` of "8" would indicate to start from the eighth element of the resulting list). | `{ filter: { AND: [ {EQ: ["field1", 123] }, {EQ: ["field2", "abc"] }, ] }, orderBy: ["field1 asc", "field2 desc"], limit: 3, pageToken: "3" }` 
| `tin` | The TIN of the business. The `name` field must also be provided. | `{ "tin": "123456789", "tinType": "TIN" }` 
| `matchThreshold` | The confidence threshold the result must meet (0.0 - 1.0). | - 0.0
- 0.8
- 1.0 
| `entityType` | The entity type to search for. Defaults to `BRAND` . | - `BRAND`
- `LEGAL_ENTITY`
- `OPERATING_LOCATION` 
| `output` | Specifies the result should be a background task instead of an immediate result. Configuration includes:
- `filename` (required): the name of the resulting file
- `format` (optional): the format of the resulting file
- `s3Path` (optional): the AWS S3 path of the resulting file. If `format` is `CSV` , the AWS S3 path must be a unique path to the CSV file. If `format` is `PARQUET` , the AWS S3 path must be a directory. | - `{ "filename": "my_csv", "format": "CSV", "s3Path": "s3://bucket/path/to/my_csv.csv" }`
- `{ "filename": "my_parquet", "format": "PARQUET", "s3Path": "s3://bucket/path/to/my/parquet/" }` 

#### Conditions and ConnectionConditions

[`Conditions`](/reference/graphql_api/inputs/conditions) and [`ConnectionConditions`](/reference/graphql_api/inputs/connection-conditions) is used for filtering and ordering data in connection-based (i.e. list-based) queries. It provides a standardized way to apply conditions to lists, particularly useful for pagination and data filtering. The following can be specified as conditions:

1. `filter`
2. `orderBy`

##### Filter

`filter` is a JSON object containing filtering criteria. It supports complex filtering options including logical operators and field comparisons. See the table below on what is supported:

| **Operator** | **Desc** | **Number of Arguments** | **Examples** 
| `EQ` | Equals comparison | 2 | `filter: { EQ: ["name", "McDonald's"] }` 
| `NE` | Not equals comparison | 2 | `filter: { NE: ["state", "NY"] }` 
| `GT` | Greater than | 2 | `filter: { GT: ["firstObservedDate", "2025-01-01"] }` 
| `GTE` | Greater than or equal | 2 | `filter: { GTE: ["firstObservedDate", "2025-01-01"] }` 
| `LT` | Less than | 2 | `filter: { LT: ["firstObservedDate", "2025-01-01"] }` 
| `LTE` | Less than or equal | 2 | `filter: { LTE: ["firstObservedDate", "2025-01-01"] }` 
| `IN` | Value is in a list | 2 | `filter: { IN: ["operatingStatus", ["Open", "Closed"]] }` 
| `NOT_IN` | Value is not in a list | 2 | `filter: { NOT_IN: ["operatingStatus", ["Open", "Closed"]] }` 
| `LIKE` | Case-sensitive string matching. Use `%` inside the pattern string as in SQL | 2 | `filter: { LIKE: ["name", "%Pizza%"] }` 
| `ILIKE` | Case-insensitive string matching. Use `%` inside the pattern string as in SQL | 2 | `filter: { ILIKE: ["name", "%PiZza%"] }` 
| `AND` | Logical AND operation | ≥2 | `filter: { AND: [ expr1, expr2, ...] } filter: { AND: [ {EQ: ["name", "McDonald's"] }, {NE: ["state", "NY"]] }` 
| `OR` | Logical OR operation | ≥2 | `filter: { OR: [ expr1, expr2, ...] } filter: { OR: [ {EQ: ["name", "McDonald's"] }, {EQ: ["state", "NY"]] }` 
| `NOT` | Logical Negation | 1 | `filter: { NOT: [ expr ] }filter: { NOT: [ {EQ: ["name", "McDonald's"] } ]}` 
| `ADD` | Addition | 2 | `filter: { ADD: [ "monthlySales", 123 ] }` 
| `SUB` | Subtraction | 2 | `filter: { SUB: [ "monthlySales", 123 ] }` 
| `MUL` | Multiplication | 2 | `filter: { MUL: [ "monthlySales", 12 ] }` 
| `DIV` | Division | 2 | `filter: { MUL: [ "annualSales", 12 ] }` 
| `HAS` | Checks if value is present | 1 | `filter: { HAS: ["roles.emailAddresses"] }` 

###### Example

Request
```graphql
query Search {
        search(searchInput: { name: "McDonald's", entityType: OPERATING_LOCATION }) {
            ... on OperatingLocation {
                addresses {
                    edges {
                        node {
                            fullAddress
                        }
                    }
                }
                cardTransactions(
                    conditions: {
                        filter: {
                            AND: [
                                { EQ: ["period", "1m"] },
                                { EQ: ["quantity_type", "card_revenue_amount"] }
                            ]
                        }
                    }
                ) {
                    edges {
                        node {
                            quantityType
                            projectedQuantity
                            rawQuantity
                            periodStartDate
                            periodEndDate
                            period
                        }
                    }
                }
                names {
                    edges {
                        node {
                            name
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "225 MARY GRUBBS HWY WALTON KY 41094"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 188939,
                                    "rawQuantity": 67375,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 198123,
                                    "rawQuantity": 68809,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 187506,
                                    "rawQuantity": 65938,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "2502 SE DELAWARE AVE ANKENY IA 50021"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 117712,
                                    "rawQuantity": 36313,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 125336,
                                    "rawQuantity": 36407,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 122000,
                                    "rawQuantity": 35474,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "DEKALB IL 60115"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": []
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "2642 SANTA ROSA AVE SANTA ROSA CA 95407"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 151212,
                                    "rawQuantity": 41109,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 160633,
                                    "rawQuantity": 41802,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 159208,
                                    "rawQuantity": 42807,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "1717 W BATTLEFIELD ST SPRINGFIELD MO 65807"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 231018,
                                    "rawQuantity": 65062,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 243734,
                                    "rawQuantity": 68490,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 234450,
                                    "rawQuantity": 65714,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "550 COURTHOUSE RD GULFPORT MS 39507"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 48371,
                                    "rawQuantity": 11942,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 51520,
                                    "rawQuantity": 11620,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 52035,
                                    "rawQuantity": 11263,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "808 S COLUMBIA DR WEST COLUMBIA TX 77486"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 146039,
                                    "rawQuantity": 35715,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 175843,
                                    "rawQuantity": 41151,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 156760,
                                    "rawQuantity": 39294,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "10260 GRIFFIN RD FORT LAUDERDALE FL 33328"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 277587,
                                    "rawQuantity": 84323,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 296827,
                                    "rawQuantity": 88822,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 281555,
                                    "rawQuantity": 87665,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "2080 CROWELL RD N STE A COVINGTON GA 30014"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 124874,
                                    "rawQuantity": 34977,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 138962,
                                    "rawQuantity": 37023,
                                    "periodStartDate": "2025-05-01",
                                    "periodEndDate": "2025-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 130421,
                                    "rawQuantity": 36720,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "fullAddress": "1200 N LACROSSE ST RAPID CITY SD 57701"
                                }
                            }
                        ]
                    },
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 308110,
                                    "rawQuantity": 110039,
                                    "periodStartDate": "2021-06-01",
                                    "periodEndDate": "2021-06-30",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 274141,
                                    "rawQuantity": 97907,
                                    "periodStartDate": "2021-05-01",
                                    "periodEndDate": "2021-05-31",
                                    "period": "1m"
                                }
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 237229,
                                    "rawQuantity": 84725,
                                    "periodStartDate": "2021-04-01",
                                    "periodEndDate": "2021-04-30",
                                    "period": "1m"
                                }
                            }
                        ]
                    },
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

###### Filtering by Field Paths

Filtering is applied from the top level downward. Filtering of attributes associated with an entity (e.g. Mexican restaurant brands, grocery store brands in New York, etc.) must always be applied to the top-level entity.

When referencing nested fields (i.e. attributes) from top-level entities, we use dot notation.

For example, if we wanted to access and filter on brands' operating locations' status, the filter is `operatingLocations.operatingStatuses.operatingStatus` . This nested field path was constructed from the following logic based on the GraphQL schema:

1. We know that `search` returns `SearchUnion` (i.e. `Brand | OperatingLocation | LegalEntity` ).
2. We are interested in `Brand` .
3. From `Brand` , we are interested in the field `operatingLocations` of the type `BrandOperatingLocationConnection` because we want to filter on brands' operating locations.
4. `BrandOperatingLocationConnection` is a Connection object based on [Relay](https://relay.dev/graphql/connections.htm) . In `BrandOperatingLocationConnection` , we are interested in the nodes of type `OperatingLocation` .
5. In `OperatingLocation` , we are interested in the field `operatingStatuses` of the type `OperatingLocationOperatingStatusConnection` .
6. `OperatingLocationOperatingStatusConnection` is a Connection object based on [Relay](https://relay.dev/graphql/connections.htm) . In `OperatingLocationOperatingStatusConnection` , we are interested in the nodes of type `OperatingLocationOperatingStatus` .
7. In `OperatingLocationOperatingStatus` , we are interested in the field `operatingStatus` of type `String` .
8. Finally, from traversing the GraphQL schema starting from `Brand` , we get the filter `operatingLocations.operatingStatuses.operatingStatus` .

###### Examples

1. Filtering by a brand's operating locations' status is accessed by `operatingLocations.operatingStatuses.operatingStatus` .
2. Filtering by a brand's operating locations' state address is accessed by `operatingLocations.addresses.state` .
3. Filtering by a brand's industry type and industry code is accessed by `industries.industryType` and `industries.industryCode` respectively.
4. Filtering by a period of card transactions is accessed by `cardTransactions.period` .

###### Walk-through Example

Let's break down an example request to illustrate this:

Example
```graphql
query Search {
        search(
            searchInput: {
                prompt: "indian"
                conditions: {
                    # This filter is equivalent to filtering the entities of "BRAND" by their associated "industries"
                    # attributes (i.e. industry type and industry description) and "operatingLocations" attributes
                    # (i.e. the city of the operating location's address and the state of the operating location's
                    # address). It is analagous to this SQL WHERE clause: "WHERE industries.industryType =
                    # 'enigma_industry_description' AND industries.industryDesc ILIKE '%indian%' AND
                    # operatingLocations.addresses.city = 'FREMONT' AND operatingLocations.addresses.state = 'CA'".
                    # What this filter means is to find brands that have an industry description with the term "indian"
                    # in its Enigma industry description and has at least one operating location in Fremont, CA.
                    filter: {
                        AND: [
                            { EQ: ["industries.industryType", "enigma_industry_description"] }
                            { ILIKE: ["industries.industryDesc", "%indian%"] }
                            { EQ: ["operatingLocations.addresses.city", "FREMONT"] }
                            { EQ: ["operatingLocations.addresses.state", "CA"] }
                        ]
                    }
                    # Return a maximum of three results. This is analagous to "LIMIT 3" in SQL.
                    limit: 3
                    # Sort the result by the Brand's name in lexicographical order. This is analagous to "ORDER BY names.name ASC" in SQL.
                    orderBy: ["names.name ASC"]
                }
                entityType: BRAND
            }
        ) {
            ... on Brand {
                names(first: 1) {
                    edges {
                        node {
                            name
                        }
                    }
                }
                industries {
                    edges {
                        node {
                            industryType
                            industryDesc
                            industryCode
                            lastObservedDate
                        }
                    }
                }
                operatingLocations(
                    conditions: {
                        # This filter further filters the result from the filter above by displaying only the operating locations in Fremont, CA.
                        filter: {
                            AND: [{ EQ: ["addresses.city", "FREMONT"] }, { EQ: ["addresses.state", "CA"] }]
                        }
                    }
                ) {
                    edges {
                        node {
                            addresses {
                                edges {
                                    node {
                                        fullAddress
                                    }
                                }
                            }
                            operatingStatuses {
                                edges {
                                    node {
                                        operatingStatus
                                        lastObservedDate
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```

In this example, we are asking to find Indian businesses with at least one operating location in Fremont, CA. Among a brand's operating locations, we are only interested in the ones with an address in Fremont, CA.

To filter for Indian businesses with at least one operating location in Fremont, CA, we set the following `filter` :

```text
{
    AND: [
        { EQ: ["industries.industryType", "enigma_industry_description"] }
        { ILIKE: ["industries.industryDesc", "%indian%"] }
        { EQ: ["operatingLocations.addresses.city", "FREMONT"] }
        { EQ: ["operatingLocations.addresses.state", "CA"] }
    ]
}
```

This filter means we want only brands that have an industry type of `enigma_industry_description` with an industry description with the word `indian` in it. In addition, the brand should also have at least one operating location in the city of `Fremont` and the `state` of `CA` .

We further filter the list of operating locations at the `OperatingLocation` entity level to retrieve only addresses in Fremont, CA by setting this filter:

```text
{
    AND: [
        { EQ: ["addresses.city", "FREMONT"] }
        { EQ: ["addresses.state", "CA"] }
    ]
}
```

##### OrderBy

`orderBy` is a list of sort expressions that define how results should be ordered. Each string follows the format: `<field_name> [ASC|DESC]`

The ordering pertains to the requested field only. In the example below, the names will be returned in descending order:

Request
```graphql
query Search {
        search(
            searchInput: {
                name: "pizza"
                entityType: BRAND
                address: { city: "NEW YORK", state: "NY" }
            }
        ) {
            ... on Brand {
                names(conditions: { orderBy: ["name DESC"] }) {
                    edges {
                        node {
                            name
                        }
                    }
                }

            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "PIZZA HUT EXPRESS"
                                }
                            },
                            {
                                "node": {
                                    "name": "PIZZA HUT"
                                }
                            },
                            {
                                "node": {
                                    "name": "CENTER PIZZA"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

Multiple ordering patterns are also possible:

Request
```graphql
query Search {
        search(
            searchInput: {
                name: "pizza"
                entityType: OPERATING_LOCATION
                address: { state: "NEW YORK" }
            }
        ) {
            ... on OperatingLocation {
                addresses
                (conditions: { orderBy: ["streetAddress1 ASC", "city ASC"] }) {
                    edges {
                        node {
                            streetAddress1
                            city
                        }
                    }
                }

            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "streetAddress1": "364 7TH AVE",
                                    "city": "BRONX"
                                }
                            }
                        ]
                    }
                },
                {
                    "addresses": {
                        "edges": [
                            {
                                "node": {
                                    "streetAddress1": "921 E 174TH ST",
                                    "city": "NEW YORK"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

Multiple `orderBy` s can also be specified:

Request
```graphql
query Search {
        search(
            searchInput: {
                name: "pizza"
                entityType: BRAND
                address: { city: "NEW YORK", state: "NY" }
            }
        ) {
            ... on Brand {
                names(conditions: { orderBy: ["name desc"] }) {
                    edges {
                        node {
                            name
                        }
                    }
                }
                operatingLocations(conditions:{orderBy: ["addresses.city asc"]}) {
                    edges {
                        node {
                            addresses {
                                edges {
                                    node {
                                        city
                                        state
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```

#### Math Functions

Math functions (i.e. [`NodeFunctions`](/reference/graphql_api/interfaces/node-functions) ) provides aggregate mathematical operations on related data. It allows you to perform calculations like counting, summing, finding minimum/maximum values, and collecting values from related entities.

Here is a table of available math functions:

| **Function** | **Return Type** | **Description** | **Parameters** 
| `count` | Int | Counts the number of related records | - `field` (required)
- `conditions` (optional) 
| `sum` | Int | Sums numeric values from related records | - `field` (required)
- `conditions` (optional) 
| `min` | Int | Finds the minimum numeric value | - `field` (required)
- `conditions` (optional) 
| `max` | Int | Finds the maximum numeric value | - `field` (required)
- `conditions` (optional) 
| `avg` | Float | Calculates the average of numeric values | - `field` (required)
- `conditions` (optional) 
| `collect` | String | Collects values into a concatenated string | - `field` (required)
- `conditions` (optional)
- `separator` (optional) 
| `minDateTime` | DateTime | Finds the minimum datetime value | - `field` (required)
- `conditions` (optional) 
| `maxDateTime` | DateTime | Finds the maximum datetime value | - `field` (required)
- `conditions` (optional) 

##### Parameters

- `field` (required)
- Type: `String`
- Description: The path to the field to apply the math function
- Examples
- `websites` : Count all related websites
- `names.rank` : Sum the rank values of related names
- `operatingLocations.brands.id` : Count brands within operating locations
- `conditions` (optional)
- Type: [`Conditions`](https://documentation.enigma.com/reference/graphql_api/inputs/conditions)
- Description: Conditions in which to apply for the input of the math function
- Properties:
- `filter` (optional): a JSON object to specify filtering of attributes
- `orderBy` (optional): a list of attributes and sort ordering
- `limit` (optional): an integer to limit the top-level result by
- `pageToken` (optional): a numeric offset represented as a string to start returning results from (e.g. a `pageToken` of "8" would indicate to start from the eighth element of the resulting list).
- `separator` (optional) (only for the `collect` math function)
- Type: `String`
- Description: A separator when joining values (e.g. ",", ";", "|", etc.)
- Default: "," (i.e. comma)

##### Examples

###### Count

Count the number of names and websites for the brand "McDonald's".

Request
```graphql
query Search {
      search(searchInput: { name: "McDonald's", entityType: BRAND }) {
    	  ... on Brand {
    		  id
    	    websitesCount: count(field: "websites")
    	    namesCount: count(field: "names")
        }
      }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "id": "2daa02e4-f887-40f5-8bd2-c00764b91e76",
                    "websitesCount": 14482,
                    "namesCount": 3
                }
            ]
        }
    }
```

###### Sum

Get the total number of reviews for McDonald's operating locations.

Request
```graphql
query Search {
      search(searchInput: { name: "McDonald's", entityType: OPERATING_LOCATION }) {
        ... on OperatingLocation {
            totalReviews: sum(field: "reviewSummaries.reviewCount")
        }
      }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "totalReviews": 16323
                },
                {
                    "totalReviews": 20660
                },
                {
                    "totalReviews": 1427
                },
                {
                    "totalReviews": 23860
                },
                {
                    "totalReviews": 18539
                },
                {
                    "totalReviews": 11330
                },
                {
                    "totalReviews": 20853
                },
                {
                    "totalReviews": 11339
                },
                {
                    "totalReviews": 33452
                },
                {
                    "totalReviews": 1725
                }
            ]
        }
    }
```

###### Min/Max

Get the minimum, maximum, and average number of reviews for McDonald's operating locations.

Request
```graphql
query Search {
        search(searchInput: { name: "McDonald's", entityType: OPERATING_LOCATION }) {
            ... on OperatingLocation {
                minReviewCount: min(field: "reviewSummaries.reviewCount")
                maxReviewCount: max(field: "reviewSummaries.reviewCount")
                avgReviewCount: avg(field: "reviewSummaries.reviewCount")

            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "minReviewCount": 641,
                    "maxReviewCount": 1017,
                    "avgReviewCount": 859.1052631578947
                },
                {
                    "minReviewCount": 1491,
                    "maxReviewCount": 1896,
                    "avgReviewCount": 1721.6666666666667
                },
                {
                    "minReviewCount": 124,
                    "maxReviewCount": 269,
                    "avgReviewCount": 203.85714285714286
                },
                {
                    "minReviewCount": 1469,
                    "maxReviewCount": 1852,
                    "avgReviewCount": 1704.2857142857142
                },
                {
                    "minReviewCount": 1908,
                    "maxReviewCount": 2173,
                    "avgReviewCount": 2059.8888888888887
                },
                {
                    "minReviewCount": 930,
                    "maxReviewCount": 1140,
                    "avgReviewCount": 1030
                },
                {
                    "minReviewCount": 918,
                    "maxReviewCount": 1121,
                    "avgReviewCount": 1042.65
                },
                {
                    "minReviewCount": 750,
                    "maxReviewCount": 923,
                    "avgReviewCount": 872.2307692307693
                },
                {
                    "minReviewCount": 1556,
                    "maxReviewCount": 2018,
                    "avgReviewCount": 1858.4444444444443
                },
                {
                    "minReviewCount": 428,
                    "maxReviewCount": 435,
                    "avgReviewCount": 431.25
                }
            ]
        }
    }
```

###### MinDateTime/MaxDateTime

Get the first and last observed date for McDonald's operating locations.

Request
```graphql
query Search {
        search(searchInput: { name: "McDonald's", entityType: OPERATING_LOCATION }) {
            ... on OperatingLocation {
                firstObservedDateTime: minDateTime(field: "addresses.firstObservedDate")
                lastObservedDateTime: maxDateTime(field: "addresses.lastObservedDate")
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-08-16T09:59:51"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-08-13T07:29:01"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-08-19T00:00:00"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-08-14T08:38:52"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-06-30T07:00:00"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-08-06T14:12:59"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-08-08T22:59:39"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-07-09T00:00:00"
                },
                {
                    "firstObservedDateTime": "2020-07-04T01:00:00",
                    "lastObservedDateTime": "2025-07-16T22:13:52"
                },
                {
                    "firstObservedDateTime": "2015-05-15T08:28:06",
                    "lastObservedDateTime": "2025-07-18T08:46:04"
                }
            ]
        }
    }
```

###### Collect

Get the collection of Enigma industry descriptions of McDonald's operating locations.

Note: `collect` must be output to a file (i.e. `output` in `SearchInput` must be specified).

Request
```graphql
query Search {
        search(
            searchInput: {
                address: { city: "NEW YORK", state: "NY" }
                entityType: OPERATING_LOCATION
                output: { filename: "09edc744-e3ca-415b-8b5a-4a8149f3167b" }
            }
        ) {
            ... on OperatingLocation {
                addresses(first: 1) {
                    edges {
                        node {
                            fullAddress
                        }
                    }
                }
                brands(first: 1) {
                    edges {
                        node {
                            names(first: 1) {
                                edges {
                                    node {
                                        name
                                    }
                                }
                            }
                            brandIndustries: collect(
                                field: "industries.industryDesc"
                                separator: ","
                                conditions: {
                                    filter: {
                                        EQ: ["industryType", "enigma_industry_description"]
                                    }
                                }
                            )
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "extensions": {
            "backgroundTasks": [
                {
                    "id": "849e8c2f-2562-4fc0-8359-826f20ce36cf",
                    "status": "SUCCESS",
                    "result": ["<URL_TO_RESULT_FILE>"]
                }
            ]
        },
        "data": {
            "search": null
        }
    }
```

#### Pagination

The Enigma's GraphQL schema implements cursor-based pagination following the [Relay Connection specification](https://relay.dev/graphql/connections.htm) .

##### Core Concepts

###### Connection Pattern

All paginated queries return a `Connection` object that contains:

- `edges` : Array of edge objects containing the actual data
- `pageInfo` : Metadata about the current page and navigation options

###### Edge Structure

Each edge contains:

- `node` : The actual data object
- `cursor` : A string representing the position in the result set

###### PageInfo Structure

The `pageInfo` object provides:

- `hasNextPage` : Boolean indicating if more results are available after the current page
- `hasPreviousPage` : Boolean indicating if results exist before the current page
- `startCursor` : Cursor for the first item in the current page
- `endCursor` : Cursor for the last item in the current page

##### Pagination Parameters

###### Forward Pagination

- `first` : Number of items to return from the beginning
- `after` : Cursor to start after (exclusive)

###### Backward Pagination

- `last` : Number of items to return from the end
- `before` : Cursor to end before (exclusive)

##### Pagination Validation Rules

- Cannot specify both `first` and `last` in the same query
- `after` requires `first` to be specified
- `before` requires `last` to be specified
- All pagination parameters must be >= 0

##### Examples

This example searches the next eight card transactions for McDonald's operating locations after the node with cursor `eyJpZHgiOjd9` .

Request
```graphql
query Search {
        search(searchInput: { name: "McDonald's", entityType: OPERATING_LOCATION }) {
            ... on OperatingLocation {
                cardTransactions(first: 8, after: "eyJpZHgiOjd9") {
                    edges {
                        node {
                            quantityType
                            projectedQuantity
                            rawQuantity
                            periodStartDate
                            periodEndDate
                            period
                        }
                        cursor
                    }
                    pageInfo {
                        hasNextPage
                        hasPreviousPage
                        startCursor
                        endCursor
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "cardTransactions": {
                        "edges": [
                            {
                                "node": {
                                    "quantityType": "avg_transaction_size",
                                    "projectedQuantity": 12,
                                    "rawQuantity": 12,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                },
                                "cursor": "eyJpZHgiOjh9"
                            },
                            {
                                "node": {
                                    "quantityType": "refunds_amount",
                                    "projectedQuantity": -125,
                                    "rawQuantity": -44,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                },
                                "cursor": "eyJpZHgiOjl9"
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_prior_period_growth",
                                    "projectedQuantity": 0.0061,
                                    "rawQuantity": 0.0124,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "3m"
                                },
                                "cursor": "eyJpZHgiOjEwfQ=="
                            },
                            {
                                "node": {
                                    "quantityType": "card_customers_average_daily_count",
                                    "projectedQuantity": 516,
                                    "rawQuantity": 184,
                                    "periodStartDate": "2025-06-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "1m"
                                },
                                "cursor": "eyJpZHgiOjExfQ=="
                            },
                            {
                                "node": {
                                    "quantityType": "refunds_amount",
                                    "projectedQuantity": -1357,
                                    "rawQuantity": -472,
                                    "periodStartDate": "2024-07-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "12m"
                                },
                                "cursor": "eyJpZHgiOjEyfQ=="
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_prior_period_growth",
                                    "projectedQuantity": 0.0023,
                                    "rawQuantity": 0.0022,
                                    "periodStartDate": "2024-07-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "12m"
                                },
                                "cursor": "eyJpZHgiOjEzfQ=="
                            },
                            {
                                "node": {
                                    "quantityType": "card_customers_average_daily_count",
                                    "projectedQuantity": 521,
                                    "rawQuantity": 183,
                                    "periodStartDate": "2025-04-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "3m"
                                },
                                "cursor": "eyJpZHgiOjE0fQ=="
                            },
                            {
                                "node": {
                                    "quantityType": "card_revenue_amount",
                                    "projectedQuantity": 2216172,
                                    "rawQuantity": 769903,
                                    "periodStartDate": "2024-07-01",
                                    "periodEndDate": "2025-06-30",
                                    "period": "12m"
                                },
                                "cursor": "eyJpZHgiOjE1fQ=="
                            }
                        ],
                        "pageInfo": {
                            "hasNextPage": true,
                            "hasPreviousPage": true,
                            "startCursor": "eyJpZHgiOjh9",
                            "endCursor": "eyJpZHgiOjE1fQ=="
                        }
                    }
                }
            ]
        }
    }
```

#### Usage

The `search` query supports four main search patterns:

1. Text Search
2. Lookup
3. Prompt Search
4. Segmentation

##### Text Search

Text search uses the business name, person information (e.g. first name, last name, etc.), and/or address to make a search against Enigma's business data.

###### Example

Request
```graphql
query Search {
        search(
            searchInput: {
                name: "Enigma"
                person: {firstName: "Joe", lastName: "Smith"}
                entityType: BRAND
                address: {city: "NEW YORK", state:"NY"}
            }
        ) {
            ... on Brand {
                id
                names {
                    edges {
                        node {
                            name
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "id": "5f53e079-c66a-487e-8a9d-08efc39652ee",
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "ENIGMA TECHNOLOGIES"
                                }
                            },
                            {
                                "node": {
                                    "name": "ENIGMA TECHNOLOGIES, INC."
                                }
                            },
                            {
                                "node": {
                                    "name": "ENIGMA COMPUTER SOLUTION"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

##### Lookup

Lookup uses a entity's unique ID to search Enigma's business data.

###### Example

Request
```graphql
query Search {
        search(
            searchInput: {
                id: "5f53e079-c66a-487e-8a9d-08efc39652ee"
            }
        ) {
            ... on Brand {
                id
                names {
                    edges {
                        node {
                            name
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "id": "5f53e079-c66a-487e-8a9d-08efc39652ee",
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "ENIGMA TECHNOLOGIES"
                                }
                            },
                            {
                                "node": {
                                    "name": "ENIGMA TECHNOLOGIES, INC."
                                }
                            },
                            {
                                "node": {
                                    "name": "ENIGMA COMPUTER SOLUTION"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

##### Prompt Search

Prompt search uses natural language (e.g. "grocery stores in New York) to search against Enigma's business data.

###### Example

Request
```graphql
query Search {
        search(
            searchInput: {
                prompt: "Mexican restaurants"
                entityType: BRAND
                conditions: {limit: 3}

            }
        ) {
            ... on Brand {
                names {
                    edges {
                        node {
                            name
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "TAQUERIA CDMX"
                                }
                            }
                        ]
                    }
                },
                {
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "DON TEQUILAS MEXICAN GRILL & CANTINA"
                                }
                            }
                        ]
                    }
                },
                {
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "ANGIE'S COCINA"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

##### Segmentation

Segmentation searches resulting in a large dataset should be performed asynchronously. This is particularly useful for comprehensive data analysis. To output the results of a search as a file, specify the `output` parameter in the input. The system will create a background task instead of returning immediate results.

###### Example

Request
```graphql
query Search {
        search(
            searchInput: {
                prompt: "Mexican restaurants"
                entityType: OPERATING_LOCATION
                output: { filename: "mexican_resuaturants_search_query_1" }
            }
        ) {
            ... on OperatingLocation {
                addresses(first: 1) {
                    edges {
                        node {
                            fullAddress
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "extensions": {
            "backgroundTasks": [
                {
                    "id": "849e8c2f-2562-4fc0-8359-826f20ce36cf",
                    "status": "SUCCESS",
                    "result": ["<URL_TO_RESULT_FILE>"]
                }
            ]
        },
        "data": {
            "search": null
        }
    }
```

Segmentation searches will return a `202 Accepted` response status code. The response will include an ID associated with the result.

Example Response
```json
# Below is a the response of search query request which was deemed to return a very large response.

    # Response code: 202
    # Response body:
    {
        "extensions": {
    	      "backgroundTasks": [
    	          {
    	              "id": "285b6f06-c532-4969-bcfd-cdd82f5de373",
    	              "status": "PROCESSING"
    	          }
            ]
        },
        "data": {
    		    # note how "data.search" is not populated, but
    		    # extensions.backgroundTasks: [...] is.
    				# This allows the flexibility for Engima's GraphQL api to return certain data if available,
    				# and provide addtional data for the request in the future via background_tasks
            "search": null
        }
    }
```

To check the status of the result after receiving a `202 Accepted` response, make a request to the `backgroundTask` GraphQL query.

Polling Status Example Request
```graphql
# Use this query to poll for result
    query BackgroundTask {
        backgroundTask(id: "285b6f06-c532-4969-bcfd-cdd82f5de373") {
            status
            result
        }
    }
```

Polling Status Example Response
```json
# Example of a successful completion of a background task
    {
        "data": {
            "backgroundTask": {
                "id": "285b6f06-c532-4969-bcfd-cdd82f5de373",
                "status": "SUCCESS",
                "result": [
                    "https://S3_PRESIGNED_DOWNLOAD_URL_HERE"
                ]
            }
        }
    }
```

Here is a table listing the possible values for `status` :

| **Status** | **Desc** | **Terminal State** 
| `PROCESSING` | Background task is currently executing | No 
| `CANCELLED` | Background task execution aborted/cancelled. No results will ever be available | Yes 
| `FAILED` | Background task execution failed after possible re-tries. No results will ever be available | Yes 
| `SUCCESS` | Background task execution succeeded. Results are immediately available | Yes 

#### Best Practices and Useful Information

Keep in mind the following best practices and information:

- The entity types available are:
- **Brand** : A customer-facing business identity
- **Legal Entity** : How a business is recognized by governments, such as registrations
- **Operating Location** : A physical business location with an address
- `search` requests must have either `id` , `name` , or `website` specified; otherwise, specify `prompt` with `output`
- Set input fields inline over using GraphQL variables.

#### Common Use Cases

The following are common use cases to use the `search` query for:

- Find businesses by industry, location, or name
- Look up specific companies by ID
- Generate market research datasets
- Discover competitors in specific markets
- Find businesses with specific characteristics (revenue, size, etc.)

#### Use Case Examples

##### How do I find for the brand "McDonald's" and the addresses that it's currently operating from in Albany, NY

Request
```graphql
query Search {
        search(
            searchInput: { name: "McDonald's", entityType: BRAND, conditions: { limit: 1 } }
        ) {
            ... on Brand {
                id
                names(first: 1) {
                    edges {
                        node {
                            name
                        }
                    }
                }
                operatingLocations(
                    conditions: {
                        filter: {
                            AND: [
                                { EQ: ["addresses.city", "ALBANY"] }
                                { EQ: ["addresses.state", "NY"] }
                                { EQ: ["operatingStatuses.operatingStatus", "Open"] }
                            ]
                        }
                    }
                ) {
                    edges {
                        node {
                            names(first: 1) {
                                edges {
                                    node {
                                        name
                                    }
                                }
                            }
                            addresses(first: 1) {
                                edges {
                                    node {
                                        fullAddress
                                        city
                                        state
                                        zip
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "id": "2daa02e4-f887-40f5-8bd2-c00764b91e76",
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    },
                    "operatingLocations": {
                        "edges": [
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "106 WOLF RD ALBANY NY 12205",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12205"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "ALBANY NY 12220",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12220"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "161 WASHINGTON EXT AVE ALBANY NY 12205",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12205"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "256 OSBORNE RD ALBANY NY 12211",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12211"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "1814 CENTRAL AVE ALBANY NY 12205",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12205"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "31 HOLLAND AVE ALBANY NY 12209",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12209"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "1602 WESTERN AVE ALBANY NY 12203",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12203"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "391 CENTRAL AVE ALBANY NY 12206",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12206"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "1006 CENTRAL AVE ALBANY NY 12205",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12205"
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

##### For McDonald's in Albany, NY find the subset that were operating on Jan 1, 2024

Request
```graphql
query Search {
        search(
            searchInput: { name: "McDonald's", entityType: BRAND, conditions: { limit: 1 } }
        ) {
            ... on Brand {
                id
                names(first: 1) {
                    edges {
                        node {
                            name
                        }
                    }
                }
                operatingLocations(
                    conditions: {
                        filter: {
                            AND: [
                                { EQ: ["operatingLocationCache.city", "ALBANY"] },
                                { EQ: ["operatingLocationCache.state", "NY"] },
                                { EQ: ["operatingStatuses.operatingStatus", "Open"] },
                                {LTE: ["operatingStatuses.lastObservedDate", "2024-01-01"]}
                            ]
                        }
                    }
                ) {
                    edges {
                        node {
                            names(first: 1) {
                                edges {
                                    node {
                                        name
                                    }
                                }
                            }
                            addresses(first: 1) {
                                edges {
                                    node {
                                        fullAddress
                                        city
                                        state
                                        zip
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
        "data": {
            "search": [
                {
                    "id": "2daa02e4-f887-40f5-8bd2-c00764b91e76",
                    "names": {
                        "edges": [
                            {
                                "node": {
                                    "name": "MCDONALD'S"
                                }
                            }
                        ]
                    },
                    "operatingLocations": {
                        "edges": [
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "ALBANY NY 12220",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12220"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "256 OSBORNE RD ALBANY NY 12211",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12211"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "31 HOLLAND AVE ALBANY NY 12209",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12209"
                                                }
                                            }
                                        ]
                                    }
                                }
                            },
                            {
                                "node": {
                                    "names": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "name": "MCDONALD'S"
                                                }
                                            }
                                        ]
                                    },
                                    "addresses": {
                                        "edges": [
                                            {
                                                "node": {
                                                    "fullAddress": "391 CENTRAL AVE ALBANY NY 12206",
                                                    "city": "ALBANY",
                                                    "state": "NY",
                                                    "zip": "12206"
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
```

##### Find the brands of grocery stores that have open operating locations in Oakland, CA from at least January 1, 2025.

Find the brands of grocery stores that have open operating locations in Oakland, CA from at least January 1, 2025. In addition, retrieve their 12-month revenue from card transactions for the brand and for each operating location.

Request
```graphql
query Search {
        search(
            searchInput: {
                prompt: "grocery"
                conditions: {
                    filter: {
                        AND: [
                            { EQ: ["operatingLocations.addresses.city", "OAKLAND"] }
                            { EQ: ["operatingLocations.addresses.state", "CA"] }
                            { EQ: ["operatingLocations.operatingStatuses.operatingStatus", "Open"] }
                            { EQ: ["industries.industryType", "enigma_industry_description"] }
                            { EQ: ["industries.industryDesc", "grocery store"] }
                            { GTE: ["operatingLocations.operatingStatuses.lastObservedDate", "2025-01-01"] }
                        ]
                    }
                    limit: 6
                }
            }
        ) {
            ... on Brand {
                names(first: 1) {
                    edges {
                        node {
                            name
                        }
                    }
                }
                cardTransactions(
                    first: 1
                    conditions: {
                        filter: {
                            AND: [
                                { EQ: ["period", "12m"] }
                                { EQ: ["quantityType", "card_revenue_amount"] }
                                { IS_NULL: ["platformBrandId"] }
                            ]
                        }
                    }
                ) {
                    edges {
                        node {
                            periodStartDate
                            periodEndDate
                            projectedQuantity
                            quantityType
                        }
                    }
                }
                operatingLocations(
                    conditions: {
                        filter: {
                            AND: [
                                { EQ: ["addresses.city", "OAKLAND"] }
                                { EQ: ["addresses.state", "CA"] }
                            ]
                        }
                    }
                ) {
                    edges {
                        node {
                            addresses {
                                edges {
                                    node {
                                        fullAddress
                                    }
                                }
                            }
                            cardTransactions(
                                first: 1
                                conditions: {
                                    filter: {
                                        AND: [
                                            { EQ: ["quantityType", "card_revenue_amount"] }
                                            { EQ: ["period", "12m"] }
                                        ]
                                    }
                                }
                            ) {
                                edges {
                                    node {
                                        periodStartDate
                                        periodEndDate
                                        projectedQuantity
                                        quantityType
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
```

Response
```json
{
    "data": {
        "search": [
            {
                "names": {
                    "edges": [
                        {
                            "node": {
                                "name": "GROCERY OUTLET"
                            }
                        }
                    ]
                },
                "cardTransactions": {
                    "edges": [
                        {
                            "node": {
                                "periodStartDate": "2024-07-01",
                                "periodEndDate": "2025-06-30",
                                "projectedQuantity": 2421436736,
                                "quantityType": "card_revenue_amount"
                            }
                        }
                    ]
                },
                "operatingLocations": {
                    "edges": [
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "2900 BROADWAY OAKLAND CA 94611"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 11132967,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            },
            {
                "names": {
                    "edges": [
                        {
                            "node": {
                                "name": "GOOD EGGS"
                            }
                        }
                    ]
                },
                "cardTransactions": {
                    "edges": [
                        {
                            "node": {
                                "periodStartDate": "2024-07-01",
                                "periodEndDate": "2025-06-30",
                                "projectedQuantity": 37727432,
                                "quantityType": "card_revenue_amount"
                            }
                        }
                    ]
                },
                "operatingLocations": {
                    "edges": [
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "2000 MARITIME ST UNIT 200 OAKLAND CA 94607"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 76490,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            },
            {
                "names": {
                    "edges": [
                        {
                            "node": {
                                "name": "SPROUTS FARMERS MARKET"
                            }
                        }
                    ]
                },
                "cardTransactions": {
                    "edges": [
                        {
                            "node": {
                                "periodStartDate": "2024-07-01",
                                "periodEndDate": "2025-06-30",
                                "projectedQuantity": 5175564388,
                                "quantityType": "card_revenue_amount"
                            }
                        }
                    ]
                },
                "operatingLocations": {
                    "edges": [
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "3035 BROADWAY OAKLAND CA 94611"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 12291,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            },
            {
                "names": {
                    "edges": [
                        {
                            "node": {
                                "name": "LUCKY"
                            }
                        }
                    ]
                },
                "cardTransactions": {
                    "edges": [
                        {
                            "node": {
                                "periodStartDate": "2024-07-01",
                                "periodEndDate": "2025-06-30",
                                "projectedQuantity": 950412098,
                                "quantityType": "card_revenue_amount"
                            }
                        }
                    ]
                },
                "operatingLocations": {
                    "edges": [
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "1963 MOUNTAIN BLVD OAKLAND CA 94611"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 11039316,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        },
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "247 E 18TH ST OAKLAND CA 94606"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 26016316,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            },
            {
                "names": {
                    "edges": [
                        {
                            "node": {
                                "name": "RANCHO MARKET AND PRODUCE"
                            }
                        }
                    ]
                },
                "cardTransactions": {
                    "edges": [
                        {
                            "node": {
                                "periodStartDate": "2024-07-01",
                                "periodEndDate": "2025-06-30",
                                "projectedQuantity": 758726,
                                "quantityType": "card_revenue_amount"
                            }
                        }
                    ]
                },
                "operatingLocations": {
                    "edges": [
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "1950 FRUITVALE AVE OAKLAND CA 94601"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 756392,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            },
            {
                "names": {
                    "edges": [
                        {
                            "node": {
                                "name": "FOODMAXX"
                            }
                        }
                    ]
                },
                "cardTransactions": {
                    "edges": [
                        {
                            "node": {
                                "periodStartDate": "2024-07-01",
                                "periodEndDate": "2025-06-30",
                                "projectedQuantity": 744588112,
                                "quantityType": "card_revenue_amount"
                            }
                        }
                    ]
                },
                "operatingLocations": {
                    "edges": [
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "3000 E 9TH ST OAKLAND CA 94601"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 12269307,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        },
                        {
                            "node": {
                                "addresses": {
                                    "edges": [
                                        {
                                            "node": {
                                                "fullAddress": "10950 INTERNATIONAL BLVD OAKLAND CA 94603"
                                            }
                                        }
                                    ]
                                },
                                "cardTransactions": {
                                    "edges": [
                                        {
                                            "node": {
                                                "periodStartDate": "2024-07-01",
                                                "periodEndDate": "2025-06-30",
                                                "projectedQuantity": 12518666,
                                                "quantityType": "card_revenue_amount"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

### Aggregation

The `aggregate` query is for getting the count of operating locations as well as their associated brands or legal entities, rather than retrieving detailed entity information.

#### Request Parameters

##### SearchInput

The `aggregate` query only supports the `entityType``OPERATING_LOCATION` .

For `conditions` , the only filter `aggregate` supports is:

```json
{
    "filter": {"EQ": ["operatingStatuses.operatingStatus", "Open"] }
}
```

indicating a filter for open operating locations.

#### Count

The `field` input in `count` only accepts the following:

- `brand`
Example
```graphql
query Aggregate {
            aggregate(
                searchInput: {
                    entityType: OPERATING_LOCATION,
                    address: {
                        city: "NEW YORK",
                        state: "NY"
                    }
                }
            ) {
                brandsCount: count(field: "brand")
            }
        }
```

- `operatingLocation`
Example
```graphql
query Aggregate {
            aggregate(
                searchInput: {
                    entityType: OPERATING_LOCATION,
                    address: {
                        city: "NEW YORK",
                        state: "NY"
                   }
                }
            ) {
                operatingLocationsCount: count(field: "operatingLocation")
            }
        }
```

- `operatingLocation`
legalEntity
```graphql
query Aggregate {
            aggregate(
                searchInput: {
                    entityType: OPERATING_LOCATION,
                    address: {
                        city: "ALBANY",
                        state: "NY"
                   }
               }
            ) {
                legalEntitiesCount: count(field: "legalEntity")
            }
        }
```

#### Common Use Cases

The following are common use cases to use the `aggregate` query:

- Count the total brands particular to a certain area
- Count the total brands of operating locations matching your criteria
- Count the total operating locations matching your criteria
- Count the total open operating locations matching your criteria
- Count the legal entities of operating locations matching your criteria

#### Examples

Use the `aggregate` query in any case in which you want the count of operating locations that match a certain criteria, such as:

- "How many tech companies with operating locations are there in San Francisco?"
- "Count all open operating locations in New York."

## Need Help?

- Reach out to us at [support@enigma.com](mailto:support@enigma.com)