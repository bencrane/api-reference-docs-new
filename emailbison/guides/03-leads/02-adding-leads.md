# Creating a Lead (Adding Leads)

**URL:** https://docs.emailbison.com/leads/creating-a-lead

You can add leads one at a time using the API, or bulk add leads in a CSV file using the UI or the API.

**Adding Single Leads (API):**
You can create a single lead by sending a POST request at the following endpoint: `/api/leads`. The required fields are first_name, last_name, and email. The optional fields are title, company, notes, and custom variables. Custom variables need to be created in advance in each workspace.

Example:
```
curl https://dedi.emailbison.com/api/leads \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@doe.com",
    "title": "Engineer",
    "company": "John Doe Company",
    "notes": "Important client",
    "custom_variables": [
      {
        "name": "phone number",
        "value": "9059999999"
      }
    ]
  }'
```

**Bulk Uploading Leads (API):**
Do not set the content-type header for this request. It will be automatically set to multipart/form-data because of the file included. Bulk upload leads with a POST request to the following endpoint: `/api/leads/bulk/csv`

The request takes the following fields:
- **name** (string, required) - The name of the lead list that will be created
- **csv** (FILE, required) - The CSV file
- **columnsToMap[first_name][]** (string, required) - The name of the CSV header column that corresponds to first_name on EmailBison
- **columnsToMap[last_name][]** (string, required) - The name of the CSV header column that corresponds to last_name on EmailBison
- **columnsToMap[email][]** (string, required) - The name of the CSV header column that corresponds to email on EmailBison
- **columnsToMap[{OTHER}][]** (string) - The remaining fields you would like to map - including custom variables - each getting their own field.

Example:
```
curl https://dedi.emailbison.com/api/leads/bulk/csv \
  --request POST \
  --header 'Content-Type: multipart/form-data' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data "{
    "name":"John Does list",
    "csv":"/Users/Jack/Desktop/list.csv",
    "columnsToMap[0][first_name]":"name",
    "columnsToMap[0][last_name]":"last name",
    "columnsToMap[0][email]":"email",
    "columnsToMap[0][company]":"company name",
    "columnsToMap[0][my_custom_variable]":"my_custom_variable"
  }"
```

**Bulk Uploading Leads (UI):** There is a 50,000 lead limit per CSV file. Navigate to Contacts -> Import New Contacts. You can download and refer to the Sample CSV file on proper formatting.
