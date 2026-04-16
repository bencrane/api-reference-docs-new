> Source: https://documentation.enigma.com/reference/data/entities/review-summary/

--- BEGIN UNTRUSTED EXTERNAL CONTENT (source: https://documentation.enigma.com/reference/data/entities/review-summary/) ---
Skip to main contentOverviewData AttributeGraphQL APIConsoleWebsiteLinkedIn← Back to DocsData ReferencePrimary EntitiesBrandOperating LocationLegal EntityPersonSupporting EntitiesAddressEmail AddressIndustryPhone NumberRegistered EntityRegistrationReview SummaryRoleTaxpayer Identification Number (TIN)Watchlist EntryWebsiteWebsite ContentRelationshipsSupporting EntitiesReview SummaryOn this pageReview Summary
A summary of publicly available customer reviews for a business location. Review summaries
are a time series: rank 0 is the most recent summary, with higher ranks representing earlier
periods. Enigma refreshes review data at least every three months per location.
Review velocity—the change in review count between periods—can be used as an indicator
of business health. Note that individual reviews may be removed or edited over time, so
review counts can occasionally decrease between periods.
GraphQL type: ReviewSummary
ExampleThe 4.2-star average across 1,200 Google reviews for a Starbucks location is a Review Summary entity aggregating public customer feedback.
Available from: Operating Location
Summary of publicly available customer reviews for this entity.
Pricing tier: Plus
FieldNameTypeDescriptionReview Countreview_countThe number of reviews submitted for a location.Review Score Averagereview_score_avgThe average rating of the reviews for a location. The average rating is the weighted average of reviews submitted by customers during the life of the locationFirst Review Datefirst_review_dateThe date of the earliest available review (from a sample of one hundred reviews).Last Review Datelast_review_dateThe date of the latest available review. Because up to three months may elapse before we refresh the reviews, more reviews may be submitted after this date that aren't reflected in our data. So a lag may develop which is removed at least every three months.IDidlongFirst Observed Datefirst_observed_datestringLast Observed Datelast_observed_datestring
Relationships​
Review Summary connects to other entities in the Enigma graph:
DirectionRelationshipTarget Entity←is subject ofOperating Location
View all relationships →Last updated on Apr 6, 2026PreviousRegistrationNextRoleRelationships
--- END UNTRUSTED EXTERNAL CONTENT ---
