# Custom Variables

**URL:** https://docs.emailbison.com/leads/custom-variables

A custom variable is EmailBison's way of attaching any extra information to a lead. Custom Variables need to be created before they can be attached to leads with a custom value for each lead. Note: custom variables are unique per workspace.

**Creating Custom Variables (API):**
You can create a custom variable by submitting a POST request at the following endpoint: `/api/custom-variables`. The only field you can and must provide is name, which is a name for the custom variable.

**Attaching Custom Variables to Leads (API):**
When you are creating or updating a lead - either with a POST or a PUT - you can pass the custom_variables field as an array of objects that contain a name key and a value key. The JSON will look like the following:
```json
"custom_variables": [
  {
    "name": "phone_number",
    "value": "123-456-7890"
  },
  {
    "name": "priority",
    "value": "super-high"
  }
]
```

Note how everything is wrapped in an array identifier [], and each custom variable is wrapped in an object identifier {}.

Example of adding custom variables when updating leads:
```
curl https://dedi.emailbison.com/api/leads \
  --request PUT \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@doe.com",
    "custom_variables": [
      {
        "name": "phone number",
        "value": "9059999999"
      }
    ]
  }'
```

**Attaching Custom Variables to Leads (UI):**
Refer to Leads on uploading a CSV using the UI. Include Custom Variables as columns in the CSV. Once you upload the CSV, the UI will ask you to map your headers. During this step, click on Add custom variable, enter a name for your variable and click the + button. After following the first and second steps, map your custom variables to the CSV headers. For example, map the phone number custom variable to the phone_number CSV header.
