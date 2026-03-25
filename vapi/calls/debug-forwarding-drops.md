# Debug Call Forwarding Drops

## Overview

This guide addresses a specific issue: calls that disconnect immediately after a transfer is initiated. The documentation helps users identify root causes, check logs systematically, analyze provider responses, and fix configuration problems.

## Key Troubleshooting Steps

The guide presents a structured workflow:

1. **Verify forwarding initiation** by checking the `endedReason` field in Vapi's API response. A value of "assistant-forwarded-call" indicates Vapi successfully initiated the transfer.

2. **Review server message settings** – the `serverMessages` configuration should exclude "phone-call-control" unless you're implementing custom transfer logic, as this setting can override Vapi's default behavior.

3. **Confirm call control settings** – `phoneCallProviderBypassEnabled` should be set to `false` for standard Vapi-managed transfers.

4. **Validate transfer compatibility** – certain scenarios aren't supported, including web-to-phone transfers and PSTN-to-SIP forwarding.

5. **Examine provider logs** using the `phoneCallProviderId` in dashboards for Twilio, Vonage, or Telnyx to identify transfer failures.

6. **Analyze SIP packets** (for SIP calls) by downloading PCAP files and filtering for REFER packets in Wireshark.

## Common Issues & Solutions

The documentation identifies frequent problems:

- **Successful forwarding showing but calls still drop**: Check destination number formatting and verify the number is reachable
- **Non-forwarding endedReason values**: Remove conflicting configuration settings
- **Missing SIP REFER packets**: Verify SIP endpoint configuration matches requirements

## When to Escalate

Support should be contacted after completing troubleshooting when provider logs indicate successful transfers but failures persist, or when configuration changes don't resolve the issue.
