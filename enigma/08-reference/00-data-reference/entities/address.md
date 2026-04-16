> Source: https://documentation.enigma.com/reference/data/entities/address/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/address/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesAddressOn this pageAddress
A physical street address for the business. Addresses conform to the standards provided by
USPS Publication 28 where possible.
If information is available, we indicate the specific street address and unit, meaning that
two units in the same building appear as two distinct addresses. Otherwise, the address may
be a postal code or city/state rather than a complete street address.
GraphQL type: Address
ExampleThe address 1912 Pike Pl, Seattle, WA 98101 is an Address entity linked to the original Starbucks operating location.
Available from: Legal Entity, Operating Location
A physical street address for the business.
Pricing tier: Core
FieldNameTypeDescriptionCitystandardized_component__cityThe city where this address is located.Countystandardized_component__countyThe county where this address is located.Metropolitan Statistical Areastandardized_msaThe Metropolitan/Micropolitan Statistical Area where this address is located.Combined Statistical Areastandardized_csaThe Combined Statistical Area where this address is located.Statestandardized_component__state_abbrThe two-letter abbreviation of the U.S. state or territory.Full Addressstandardized_full_addressThe complete address including street address, unit, city, state and ZIP code.Latitudestandardized_latitudeThe approximate latitude (decimal form) of the street address.Longitudestandardized_longitudeThe approximate longitude (decimal form) of the street address.H3 Indexstandardized_h3_index_res_10The h3 index (resolution 10) for geo-hashing applications.Street Address 1standardized_street_addressThe main street address with number, name, and directionals using USPS standards.Street Address 2standardized_sub_addressAdditional address information like unit, suite or floor number using USPS abbreviations.ZIP Codestandardized_component__zip_fiveThe current five-digit U.S. postal code of the address.Countrystandardized_country_nameThe three-digit ISO3 country code, null typically indicates USA.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Address Deliverability​
The delivery properties of an address.
Pricing tier: Plus
FieldNameTypeDescriptionDeliverabledeliverablestringVirtualvirtualstringResidential Delivery Indicatorstandardized_rdiIndicator showing if USPS identifies the address as Residential or Commercial.Delivery Typerecord_typeThe type of mail delivery for this address.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Address connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity→appears onWatchlist Entry←receives mail atLegal Entity←operates atOperating Location←recordedRegistration
View all relationships →Last updated on Apr 6, 2026PreviousPersonNextEmail AddressAddress DeliverabilityRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---
