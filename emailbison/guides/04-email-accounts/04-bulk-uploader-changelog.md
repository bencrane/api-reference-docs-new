# Bulk Uploader Tool Changelog

**URL:** https://docs.emailbison.com/email-accounts/bulk-uploader-tool/changelog

**v2.1.1 - February 2026 - EmailGuard Compatibility; Tagging Fix:**
- Updated EmailGuard mode to work on new layout.
- Added new flag --emailguard-prompt-login and the equivalent advanced option. Intended for advanced usage, in almost all cases this should be left as false / no.
- Fixed issue causing email tagging to not correctly trigger.

**v2.1.0 - January 2026 - Support for Admin Consent Prompt:**
- This update is required for the new EmailBison "Admin Consent Prompt" Option. Backwards compatibility is maintained.
- You can now provide an optional use_as_admin column in your CSV file, which will cause the uploader to check "Admin Consent Prompt" on the EmailBison Page.
- Fixed issue with workspace name not being read properly.
- Stability Improvements.

**v2.0.4 - November 2025 - Minor maintenance patch.**

**v2.0.3 - September 2025 - Minor enhancements:**
- The tool has better selectors for the EmailBison connect page. This update is needed in cases where the layout has changed.
- Fixed an issue where the tool would say the API key is not correct for the workspace, when it is.

**v2.0.2 - September 2025 - Minor enhancements:**
- Will now stop on wrong Microsoft username in rod driver.
- Will now display account timeouts ("context deadline exceeded") as failures.
- Explained the "context deadline exceeded" error.

**v2.0.1 - September 2025 - Minor bug fixes:**
- Fixed edge case in rod driver where microsoft password page would time out.
- The average time per account display was rounded, it now displays with 2 decimal places.
- Fixed wording for --help flag output.

**v2.0.0 - September 2025 - GUI Overhaul. New Driver. Flag Options in GUI:**
What's new:
- Brand-new user interface! The interface looks more pleasing, offers more functionality, and is easier to use.
- You can now set any flag option directly from the GUI just by following the prompts, you can skip learning how to launch the tool from the terminal and pass flags!
- Users who choose to use flags have not been forgotten. Interaction flags have been deprecated for a more intuitive --non-interactive flag! This flag removes all input prompts and allows you to integrate the tool with your other automations painlessly.
- Only failures will now be printed to the terminal, and to supplement this, you will have a running count of processed accounts, successful accounts, and failed accounts.
- The output CSV file will now only include failures. This allows you to re-run only failed accounts without an API key, by running the tool again on the output file.
- A new "driver" (the tech that controls the browsers) has been introduced, with promising internal testing. The new driver is selected by default. Users can opt for the old driver either from the GUI or by passing in a --driver flag.

Deprecated features and flags:
- The "reconnect existing accounts" prompt and flag have both been removed. This setting has been replaced by the "skip connected accounts if they exist" setting.
- Removed flags: --skip-api-key-warning, --skip-workspace-prompt, --connect-existing-accounts
- Renamed flag: --connect-disconnected-accounts-only => --skip-connected-accounts (changed to boolean, false by default)

Bug fixes:
- Fixed Ctrl+C behaviour.
- Fixed incomplete CSV output, and accounts not being tagged, if the tool is stopped before processing all accounts.
- Fixed a case where failures on accounts would have an empty message.
- Fixed dragging a CSV file on the tool causing issues if flags were passed.
- Fixed edge case where user was still prompted when the non-interactive flags were passed.

**v1.1.0 - August 2025 - V2 support. New features. Improved success rate:**
- The tool is updated to work on the EmailBison v2 beta! The tool will auto detect if it should run on v1 or v2 EmailBison, or EmailGuard.
- New feature: only process accounts that are "not connected" on EmailBison (requires API key).
- New feature (beta): You can now drop csv files directly into the executable instead of picking from the file picker.
- Many bug fixes, resulting in much higher success rate.
- Tested with --browsers 20, when RAM was fully used and macbook had to use swap for all new browsers, 100% success rate.
- Better error messages all around.
- New flags added: csv-file, skip-workspace-prompt, skip-api-key-warning, connect-existing-accounts, connect-disconnected-accounts-only, force-bison-v1, force-bison-v2.
