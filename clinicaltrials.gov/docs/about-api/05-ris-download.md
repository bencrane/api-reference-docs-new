# RIS Download

The information represented below outlines the tag names included in a RIS download and the corresponding data fields used for their content.

| Tag Name | Description | Included Data Fields |
|----------|-------------|---------------------|
| TY | Type of reference | Always "DBASE" |
| DP | Database provider | Always "National Library of Medicine (US)" |
| PP | Publishing place | Always "Bethesda (MD)" |
| ID | Unique identifier of content | [NCTId](https://clinicaltrials.gov/data-api/about-api/study-data-structure#NCTId) |
| U1 | Secondary ID and Secondary ID type | [SecondaryId](https://clinicaltrials.gov/data-api/about-api/study-data-structure#SecondaryId), [SecondaryIdType](https://clinicaltrials.gov/data-api/about-api/study-data-structure#SecondaryIdType) |
| AB | Brief Summary | [BriefSummary](https://clinicaltrials.gov/data-api/about-api/study-data-structure#BriefSummary) |
| AN | National Clinical Trial (NCT) identification number | [NCTId](https://clinicaltrials.gov/data-api/about-api/study-data-structure#NCTId) |
| SF | Subfile/database | Always "ClinicalTrials.gov" |
| ST | Short title | [BriefTitle](https://clinicaltrials.gov/data-api/about-api/study-data-structure#BriefTitle), [Acronym](https://clinicaltrials.gov/data-api/about-api/study-data-structure#Acronym) |
| TI | Official title | [OfficialTitle](https://clinicaltrials.gov/data-api/about-api/study-data-structure#OfficialTitle) |
| Y1 | First submitted date | [StudyFirstSubmitDate](https://clinicaltrials.gov/data-api/about-api/study-data-structure#StudyFirstSubmitDate) |
| Y2 | Study start date | [StartDate](https://clinicaltrials.gov/data-api/about-api/study-data-structure#StartDate) |
| A2 | Investigator(s) | [CollaboratorName](https://clinicaltrials.gov/data-api/about-api/study-data-structure#CollaboratorName) |
| C1 | Sponsor/organization | [LeadSponsorName](https://clinicaltrials.gov/data-api/about-api/study-data-structure#LeadSponsorName) |
| C2 | Overall status | [OverallStatus](https://clinicaltrials.gov/data-api/about-api/study-data-structure#OverallStatus) |
| C3 | Last update posted date | [LastUpdatePostDate](https://clinicaltrials.gov/data-api/about-api/study-data-structure#LastUpdatePostDate) |
| C4 | Last update submitted date | [LastUpdateSubmitDate](https://clinicaltrials.gov/data-api/about-api/study-data-structure#LastUpdateSubmitDate) |
| C5 | Study type | [StudyType](https://clinicaltrials.gov/data-api/about-api/study-data-structure#StudyType), [ExpAccTypeIndividual](https://clinicaltrials.gov/data-api/about-api/study-data-structure#ExpAccTypeIndividual), [ExpAccTypeIntermediate](https://clinicaltrials.gov/data-api/about-api/study-data-structure#ExpAccTypeIntermediate), [ExpAccTypeTreatment](https://clinicaltrials.gov/data-api/about-api/study-data-structure#ExpAccTypeTreatment), [PatientRegistry](https://clinicaltrials.gov/data-api/about-api/study-data-structure#PatientRegistry) |
| C6 | Has results | [HasResults](https://clinicaltrials.gov/data-api/about-api/study-data-structure#HasResults), [SubmissionInfo](https://clinicaltrials.gov/data-api/about-api/study-data-structure#SubmissionInfo) |
| C7 | Study documents | [LargeDocHasProtocol](https://clinicaltrials.gov/data-api/about-api/study-data-structure#LargeDocHasProtocol), [LargeDocHasSAP](https://clinicaltrials.gov/data-api/about-api/study-data-structure#LargeDocHasSAP), [LargeDocHasICF](https://clinicaltrials.gov/data-api/about-api/study-data-structure#LargeDocHasICF) |
| C8 | Central contact | [CentralContactName](https://clinicaltrials.gov/data-api/about-api/study-data-structure#CentralContactName), [CentralContactRole](https://clinicaltrials.gov/data-api/about-api/study-data-structure#CentralContactRole), [CentralContactPhone](https://clinicaltrials.gov/data-api/about-api/study-data-structure#CentralContactPhone), [CentralContactPhoneExt](https://clinicaltrials.gov/data-api/about-api/study-data-structure#CentralContactPhoneExt), [CentralContactEMail](https://clinicaltrials.gov/data-api/about-api/study-data-structure#CentralContactEMail) |
| RD | Retrieved date | |
| UR | Study URL | [NCTId](https://clinicaltrials.gov/data-api/about-api/study-data-structure#NCTId) |

---

*Last updated on June 05, 2024*
