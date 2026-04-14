# Accessing ClinicalTrials.gov Data in the HL7 FHIR Format

ClinicalTrials.gov study data can now be viewed or downloaded in the format known as the Health Level Seven International (HL7) Fast Healthcare Interoperability Resources (FHIR) standard. The FHIR standard is a standard that allows sharing and reuse of scientific data.

> HL7 and FHIR are the registered trademarks of Health Level Seven International. Use of these trademarks does not constitute an endorsement by HL7.

## What is FHIR?

JavaScript Object Notation (JSON) is an open-access standard for storing and transmitting data represented as attribute value pairs in human-readable text. FHIR is JSON-structured data that conforms to the FHIR standard.

## Why is FHIR important for clinical trial data exchange?

FHIR is widely used in electronic health records in the United States. This means clinical trial data in FHIR can be more easily used in clinical decision support and other health care applications.

FHIR is important because it allows interoperability between systems and reduces waste. FHIR also makes the data Findable, Accessible, Interoperable, and Reusable. These are known as the [FAIR Principles](https://www.go-fair.org/fair-principles/) for scientific data management.

## How can I use ClinicalTrials.gov data in FHIR standard?

As applications develop, you will be able to use the ClinicalTrials.gov data in FHIR for:

- Finding relevant trials for individual patients
- Finding patients matching trial eligibility criteria
- Extracting results data for meta-analyses
- Extracting study characteristics for evidence synthesis

## How can I access the ClinicalTrials.gov data in FHIR standard?

On the study record, you can click **Download** on the action bar and select **FHIR** as the format for downloading.

The study record can be downloaded directly in FHIR, or the study can be viewed in human-readable outline form on the [FEvIR Platform](https://fevir.net/).

## What is a FHIR Resource?

FHIR represents data in discrete packets of information called Resources. FHIR Resources have a defined structure including data, metadata, and human-readable text.

## What is a ResearchStudy Resource?

A ResearchStudy Resource is the FHIR Resource best suited to represent a ClinicalTrials.gov study record. FHIR Resources containing related data can be referenced or contained in the ResearchStudy Resource.

## What version of FHIR supports ClinicalTrials.gov data export?

ClinicalTrials.gov data is converted to FHIR version 6 (R6), which allows scientific data to be represented with Citation, Evidence, and EvidenceVariable Resources. These resources along with Composition, Practitioner, PractitionerRole, Organization, Location, and Group Resources can be used to express ClinicalTrials.gov data.

Release notes for the ClinicalTrials.gov-to-FEvIR Converter can be found at [Computable Publishing ClinicalTrials.gov-to-FEvIR Converter](https://computablepublishing.com/toolnotes/).
