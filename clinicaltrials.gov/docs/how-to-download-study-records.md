# How to Download Study Records

Learn how to download information about some or all of the studies shown in your search results, or the information from a single study.

This page also references information about the application programming interface (API) for developers and the public-private Clinical Trials Transformation Initiative project.

> **Important note:** Use of ClinicalTrials.gov data is subject to the [Terms and Conditions](https://clinicaltrials.gov/about-site/terms-conditions).

## Download Study Information from the Search Results List

### Open the Download Options

After doing a search, select **Download** in the action bar directly above the list of search results.

A pop-up will open with the title **What would you like to download?**

### Choose a File Format

Select the preferred file format. Three types are available:

- **CSV** (comma separated values)
- **JSON** (javascript object notation)
- **RIS** (research information systems format)

> **Note:** Choosing JSON will present the additional option to **Put each study into a separate file and download them as a zip archive**. Select the checkbox to confirm this option or leave it unselected to download a single `.json` file with all study information.

### Choose the Results to Download

Select one of the following options:

- **All Studies.** The total number of results found in your search. The number will vary based on your specific search.
- **X-selected.** The specific studies you selected on the search results screen. If no studies are selected, you will not be able to pick this option.
  > **Important note:** You must close the *What would you like to download?* pop-up to return to the Search Results and select individual studies from the list. You can close the pop-up by selecting the "X" in the upper right corner or by clicking anywhere outside the pop-up window.
- **Top X-number.** You can specify the exact number of studies to download. The default option is set to the top 10. Click in the box with the number to change it. You can select from the drop-down, enter a number, or use the up/down arrows next to the numbers to increase or decrease the value by increments of 1.

### Choose the Data Fields to Include

Select the data fields to include in your download. The options here will depend on the file format you selected in the previous step.

#### Fields Available with CSV Format

There are nine pre-selected fields: National Clinical Trial (NCT) Number, Study Title, Study URL, Study Status, Conditions, Interventions, Sponsor, Collaborators, and Study Type.

- You can modify these by selecting or de-selecting the checkbox next to each field name.
- You may also use the **Select all/De-select all** options at the top of the list of fields to check or uncheck all the options at once.
- You can select from a total of 30 fields.

#### Fields Available with JSON Format

You may choose one of the following options:

- **All available.** This will include every available data field for each study included in your download.
- **Most popular.** This will include eight pre-selected fields to include in your download. These are: NCT number, Study Title, Study Status, Conditions, Interventions, Sponsor, Collaborators, Study Type. You can modify these by selecting or de-selecting the checkbox next to each field name. You may also use the **Select all/De-select all** options at the top of the list of fields to check or uncheck all the options at once.
- **Custom set.** This is the most advanced download option. You will be able to select every available field you want to download.
  - To expand the options, use the arrow icon next to each section name and select the box next to the field name you wish to include (or un-select to exclude).
  - Please note that each section may contain one or more nested sub-sections that can be expanded/collapsed, and those sub-sections may also have additional, nested sections as well.

#### Fields Available with RIS Format

RIS format is used for downloading data for citations. The [RIS Download](https://clinicaltrials.gov/data-api/about-api/ris-download) page outlines the tag names included in a RIS download and the corresponding data fields used for its content.

### Download Your Results

Click the **Download** button at the bottom of the pop-up and save the file to a location of your choosing, or select **Cancel** to close the pop-up window and return to the Search Results page.

## Download Information from a Single Study

### Open the Download Options

When viewing an individual study record, select **Download** from the action bar above the Study Record tabs.

A pop-up with the title **What would you like to download?** will open with several options.

### Choose a File Format

Select the preferred file format. Four types are available:

- **CSV** (comma separated values)
- **JSON** (javascript object notation)
- **FHIR** (Fast Healthcare Interoperability Resources)
- **RIS** (research information systems format)

> **Note:** Choosing JSON will present the additional option to **Put each study into a separate file and download them as a zip archive**. Select the checkbox to confirm this option or leave it unselected to download a single `.json` file with all study info.

### Choose the Data Fields to Include

Select the data fields to include in your download. The options here will depend on which file format you selected in the previous step.

#### Fields Available with CSV Format

There are nine pre-selected fields: National Clinical Trial (NCT) Number, Study Title, Study URL, Study Status, Conditions, Interventions, Sponsor, Collaborators, and Study Type.

- You can modify these by selecting or de-selecting the checkbox next to each field name.
- You may also use the **Select all/De-select all** options at the top of the list of fields to check or uncheck all the options at once.
- You can select from a total of 30 fields.

#### Fields Available with JSON Format

You may choose the following options:

- **All available.** This will include every data field for each study included in your download.
- **Most popular.** This will include eight pre-selected fields to include in your download. These are: NCT number, Study Title, Study Status, Conditions, Interventions, Sponsor, Collaborators, Study Type. You can modify these by selecting or de-selecting the checkbox next to each field name. You may also use the **Select all/De-select all** options at the top of the list of fields to check or uncheck all the options at once.
- **Custom set.** This is the most advanced download option. You will be able to select every available data field you want to download.
  - To expand the options, use the arrow icon next to each section name and select the box next to the field name you wish to include (or un-select to exclude).
  - Please note that each section may contain one or more nested sub-sections that can be expanded/collapsed; and those sub-sections may also have additional sections nested within as well.

#### FHIR Format

The Fast Healthcare Interoperability Resources (FHIR) format is currently available as part of a pilot project. You can learn more about [Accessing ClinicalTrials.gov Data in the FHIR Format](https://clinicaltrials.gov/data-api/fhir).

#### Fields Available with RIS Format

RIS format is used for downloading data for citations. The [RIS Download](https://clinicaltrials.gov/data-api/about-api/ris-download) page outlines the tag names included in a RIS download and the corresponding data fields used for its content.

## Other Ways to Access Study Information

### ClinicalTrials.gov API

The [ClinicalTrials.gov application programming interface (API)](https://clinicaltrials.gov/data-api/api) provides a toolbox for programmers and other technical users to access publicly available information for all study records posted on ClinicalTrials.gov.

### CTTI Database

The Clinical Trials Transformation Initiative (CTTI) is a public-private partnership. The CTTI Improving Public Access to Aggregate Content (AACT) of ClinicalTrials.gov page provides instructions on accessing the database directly or downloading a static snapshot.

Supporting information, such as a data dictionary, database schema, and a guide for researchers and analysts, are also available on the AACT database page.
