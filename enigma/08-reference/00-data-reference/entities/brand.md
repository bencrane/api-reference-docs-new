> Source: https://documentation.enigma.com/reference/data/entities/brand/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/brand/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandBrandAddressReviewsIndustryTechnologies UsedCard TransactionsOperating LocationsLegal EntitiesRegistrationsRegistrations - PeopleContactsOperating LocationLegal EntityPersonSupporting EntitiesRelationshipsPrimary EntitiesBrandOn this pageBrand
The customer-facing identity of a business—the name and presence under which it engages
with customers. A brand represents a distinct commercial identity and may operate across
multiple physical locations and websites. A single legal entity may do business under one
or more brands (for example, a franchisor operating under multiple trade names), and a brand may
be backed by one or more legal entities.
GraphQL type: Brand
ExampleStarbucks is a brand. It has thousands of operating locations, is owned by Starbucks Corporation (a legal entity), and is classified in the food service industry.
Other Attributes​
Additional attributes available on this Brand that are not part of the standard attribute groups.
Brand Activity​
Identifies businesses that engage in activities with a high compliance risk.
Pricing tier: Plus
FieldNameTypeDescriptionActivity Typeactivity_typestringThe type of high-risk activity associated with the business.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
A summary of where a brand operates geographically, showing either the top states for brands with multiple locations or the specific city and state for brands with a single location.
Pricing tier: Core
FieldNameTypeDescriptionLocation Descriptionlocation_descriptionstringA text description of where a brand operates, showing either the top states for multi-location brands or the specific city and state for single-location brands.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Warnings and issues related to the revenue of this brand.
Pricing tier: Plus
FieldNameTypeDescriptionIssue Reasonissue_reasonstringThe reason for the revenue quality issue. The reasons signify the following: - REVENUE_DECREASE_TO_0_PCT_LOCATION_OPEN (HIGH severity): Brand revenue drops to zero and at least 1 operating location is currently open. - REVENUE_DECREASE_TO_20_PCT_LOCATION_OPEN (HIGH severity): Brand revenue drops to 20% of the median revenue over the past 12 months and at least 1 operating location is currently open. - REVENUE_INCREASE_TO_250_PCT_IN_LAST_18M (HIGH severity): Brand revenue increases to 250% of the median revenue for 3 months in the past 18 months. - REVENUE_INCREASE_TO_250_PCT_ALL_TIME (HIGH severity): Brand revenue increases to 250% of the median revenue for 3 months at any point in its revenue history. - REVENUE_DECREASE_TO_0_PCT_LOCATION_UNKNOWN (MEDIUM severity): Brand revenue drops to zero and the latest operating location operating status is stale. - REVENUE_DECREASE_TO_20_PCT_LOCATION_UNKNOWN (MEDIUM severity): Brand revenue drops to 20% of the median revenue over the past 12 months and the latest operating location operating status is stale.Issue Severityissue_severitystringThe severity of the revenue quality issue.Issue Descriptionissue_descriptionstringA description of the revenue quality issue.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Brand Data​
Attributes and metrics directly available on a Brand entity.
ReviewsPlusSummary of publicly available customer reviews for this entity.View MetricsIndustryCoreThe industry within which the business operates.View FieldsTechnologies UsedPremiumIndicates third-party technologies being used at a particular operating location.View MetricsCard TransactionsPlusContains quantitative information about the card transactions processed by the brand.View MetricsOperating LocationsView FieldsLegal EntitiesPremiumBusinesses which have become legal entities by registering with a U.S. Secretary of State (SoS).View Metrics
Also available: ID (.id), Name (.name), Is Marketable (.isMarketable).
Connected Data​
Data accessed through Brand's relationships to other entities. These fields are available when querying a Brand but live on connected entities.
AddressLinks a brand to the operating locations where it conducts business.View FieldsRegistrationsLinks a legal entity to the brands it operates under.View FieldsRegistrations - PeopleLinks a legal entity to the brands it operates under.View FieldsContactsLinks a legal entity to the brands it operates under.View Fields
Also available: Phone (via operating location), Website (via website), Online Presence (via website).
Relationships​
Brand connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity→does business withinIndustry→is affiliated withBrand→operates atOperating Location→operates websiteWebsite←does business asLegal Entity←is performed atRole
View all relationships →Last updated on Apr 6, 2026PreviousData ReferenceNextBrandOther AttributesBrand ActivityBrand DataConnected DataRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---
