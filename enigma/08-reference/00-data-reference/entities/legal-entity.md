> Source: https://documentation.enigma.com/reference/data/entities/legal-entity/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/legal-entity/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityLegal EntityPersonSupporting EntitiesRelationshipsPrimary EntitiesLegal EntityOn this pageLegal Entity
An entity which U.S. law recognizes as having an identity and rights. Legal entities can be
either natural persons or registered entities such as businesses and governmental bodies.
A legal entity may be associated with one or more registered entities (the legal entities that are registered with individual
states), and may do business under one or more brands. Legal entities may also file
taxes using a TIN, hold roles at other businesses, and appear on government watchlists.
GraphQL type: LegalEntity
ExampleStarbucks Corporation is a legal entity — the registered corporate structure that owns the Starbucks brand and in which shareholders own equity.
Bankruptcy​
The bankruptcy filing of the legal entity.
Pricing tier: Premium
FieldNameTypeDescriptionDebtor Namedebtor_namestringThe debtor's name on the filing.TrusteetrusteestringThe trustee on the filing.JudgejudgestringName of the bankruptcy court judge presiding over the case.Filing Datefiling_datedateThe date the bankruptcy was filed.Chapter Typechapter_typestringBankruptcy petition type, i.e, reorgainzation for 11, liqidation for 7, etc.Case Numbercase_numberstringThe full US District Court docket number for bankruptcy case.PetitionpetitionstringNature of petition, i.e, "voluntary" or "involuntary".Entry Dateentry_datedateDate when the case was entered.Date Converteddate_converteddateDate when the case was converted from chapter 11 to chapter 7.Date Dismisseddate_dismisseddateDate when the case was dismissed from court.Date Terminateddate_terminateddateFinal docket entry date, bankruptcy case closed.Debtor Discharged Datedebtor_discharged_datedateCourt enters the date when the plan is fulfilled and debtor has completed plan repayments.Plan Confirmed Dateplan_confirmed_datedateDate when the plan was confirmed.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Name​
A legal entity is an entity which U.S. law recognizes as having an identity and rights.
Pricing tier: Free
FieldNameTypeDescriptionNamenamestringThe legal entity's name.Legal Entity Typelegal_entity_typestringThe legal form of the entity. This can either be "Person", for natural persons, or for business entities one of a number of legal forms.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Type​
A legal entity is an entity which U.S. law recognizes as having an identity and rights.
Pricing tier: Free
FieldNameTypeDescriptionLegal Entity Typelegal_entity_typestringThe legal form of the entity. This can either be "Person", for natural persons, or for business entities one of a number of legal forms.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Legal Entity connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity→appears onWatchlist Entry→does business asBrand→files taxes usingTaxpayer Identification Number (TIN)→is flagged byWatchlist Entry→ownsLegal Entity→owns locationOperating Location→performsRole→receives mail atAddress←is instance ofPerson←is instance ofRegistered Entity
View all relationships →Last updated on Apr 6, 2026PreviousBrand - Card TransactionsNextLegal EntityBankruptcyNameTypeRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---
