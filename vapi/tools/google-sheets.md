# Google Sheets Integration Documentation

## Overview
The Vapi Google Sheets integration enables assistants to add new rows to spreadsheets during phone calls. Currently, it supports writing data only—not reading or modifying existing content.

## Prerequisites
- Active Google Sheets account
- Access to Vapi Dashboard
- An existing Vapi assistant
- A prepared Google Sheet ready for data entry

## Setup Process

### Step 1: Connect Your Google Account
Navigate to the Vapi Dashboard, locate Providers Keys > Tools Provider > Google Sheets, and authorize Vapi's access to your Google Sheets through the connection popup.

### Step 2: Create the Tool
In Dashboard > Tools, create a new Google Sheets tool by:
- Selecting the Add Row option
- Naming it descriptively
- Entering required configuration: `spreadsheetId` and `range`

To find your spreadsheet ID, open the sheet in a browser and extract the ID from the URL structure.

### Step 3: Integrate with Your Assistant
Go to your assistant's Tools tab and select your newly created Google Sheets tool from the dropdown, then publish changes.

## Tool Parameters
The tool requires three fields:
- **spreadsheetId**: The unique identifier from your sheet's URL
- **range**: Target location (sheet name or specific range like "Sheet1!A:Z")
- **values**: Array containing the new row's data

## Usage Example
The documentation provides a customer feedback assistant configuration that collects ratings, comments, and improvement suggestions, then appends them as rows to a feedback spreadsheet.

## Key Recommendations
- Validate data formatting before submission
- Implement fallback responses for potential failures
- Confirm user intent prior to adding data
- Understand your spreadsheet's column structure
