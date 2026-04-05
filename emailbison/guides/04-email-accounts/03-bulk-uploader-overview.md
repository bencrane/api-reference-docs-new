# Bulk Uploader Tool Overview

**URL:** https://docs.emailbison.com/email-accounts/bulk-uploader-tool/overview

The EmailBison team provides executables for uploading Microsoft accounts to EmailBison on Windows, macOS, and Linux. The latest version of the tool can be downloaded from the download links (Windows, macOS, Linux).

**Using the tool:** In the zip file you downloaded, you will find instructions on using the tool in how_to_use.txt.

**Issues and FAQs:**

Common Issues When Launching:
- **'bulk_uploader' not opened OR cannot be opened because it is from an unidentified developer** - This is a common macOS issue. To fix this, follow the short steps from Apple.
- **'bulk_uploader' is damaged and can't be opened. You should move it to the Bin** - This is a common issue with macOS GateKeeper quarantining files downloaded from unknown sources. To fix this, enter the following in your terminal: `xattr -c path/to/emailbison_bulk_uploader`
- **Windows protected your PC** - This is a common issue due to default settings on Microsoft SmartScreen. To fix this, click on More info -> Run anyway.
- **Search for app in the Store?** - Microsoft blocks .exe files downloaded from the internet. To fix this, right click the program, click on properties, towards the end, there's a Security: label with an Unblock checkbox, check it and press OK.

Common Issues While Using the Script:
- Set-up Issues: Most set-up issues are self-reporting and the issue will be shown in your terminal. Common issues include: Not having config.txt in the same place as the program; Not populating config.txt; Providing the wrong URL or wrong credentials in config.txt; Your CSV headers are not "name, email, password".
- **Need Admin Approval:** Manual Resolution: Refer to the help article to resolve this manually. Automatic resolution: For each different tenant in the CSV, include 1 account with the "Cloud Applications Admin" role. Include a "use_as_admin" column, mark the row this account is in as true. The bulk uploader will now login to the admin marked accounts first, and attempt to accept permissions tenant-wide.

**Advanced Usage:**
The walkthrough above is enough for most use-cases. However, the bulk uploader tool can be fine-tuned to specific needs with flags. Flags are arguments you pass in the command line.

**Flags available:**

| Flag | Type | Description | Default | Example |
|------|------|-------------|---------|---------|
| non-interactive | boolean | Disable all prompts and inputs. --csv-file flag required with this flag | false | --non-interactive |
| browsers | integer | How many browsers to spawn concurrently | 6, min: 1, max: 16 | --browsers 4 |
| no-headless | boolean | spawns visible browsers. Use --browsers 1 with this flag | false | --no-headless |
| timeout | integer | How long, in seconds, before treating the email as a fail and moving on | 75, min: 30, max: 180 | --timeout 180 |
| tag | string | What to tag this batch of emails (will create tag if it doesn't exist) | "" | --tag "batch 1" |
| skip-connected-accounts | boolean | If account exists on EmailBison, and is in a "connected" state, skip it | false | --skip-connected-accounts |
| config-file | string | Use a custom config file | "config.txt" | --config-file "../configs/workspace4.txt" |
| csv-file | string | A path to the csv file to use, to skip the file picker prompt | "" | --csv-file "../files/accounts.csv" |
| throttle | boolean | Use recommended throttling to avoid issues of the script signing in to accounts too fast | false | --throttle |
| driver | string | The technology that controls the browsers. Either "rod" or "chromedp" | "rod" | --driver rod |
