# EmailBison Documentation Audit Report

**Date:** 2026-04-05
**Sources audited:**
- API Reference: `dedi.emailbison.com/api/reference` (OpenAPI 3.0.3 spec)
- Guides Site: `docs.emailbison.com` (Mintlify-hosted documentation)
- Local Folder: `emailbison/` in this repository

---

## Summary

| Category | Before | After | Delta |
|----------|--------|-------|-------|
| API reference endpoint files | 145 | 153 | +8 |
| Guides / documentation files | 0 | 47 | +47 |
| New top-level sections | 16 | 18 | +2 |
| **Total files** | **145** | **200** | **+55** |

---

## 1. Missing API Endpoint Files (8 added)

These endpoints existed in the live API reference but had no corresponding file in the local folder.

### 1.1 Campaigns (3 new files)

| File | Endpoint | Method | Path |
|------|----------|--------|------|
| `02-campaigns/22-move-leads-to-campaign.md` | Move leads to another campaign | POST | `/api/campaigns/{campaign_id}/leads/move-to-another-campaign` |
| `02-campaigns/23-bulk-delete-campaigns.md` | Bulk delete campaigns by ID | DELETE | `/api/campaigns/bulk` |
| `02-campaigns/24-delete-campaign.md` | Delete a campaign | DELETE | `/api/campaigns/{campaign_id}` |

**Why these were missing:** The local folder had campaign CRUD for create, read, update, pause, resume, archive, and duplicate, but lacked any delete operations (single or bulk) and the move-leads-between-campaigns endpoint.

### 1.2 Schedules (3 new files)

| File | Endpoint | Method | Path |
|------|----------|--------|------|
| `10-schedules/06-show-sending-schedules.md` | Show sending schedules for all campaigns | GET | `/api/campaigns/sending-schedules` |
| `10-schedules/07-show-sending-schedule-for-campaign.md` | Show sending schedule for a single campaign | GET | `/api/campaigns/{campaign_id}/sending-schedule` |
| `10-schedules/08-create-schedule-from-template.md` | Create campaign schedule from template | POST | `/api/campaigns/{campaign_id}/create-schedule-from-template` |

**Why these were missing:** The local folder had schedule CRUD (get, create, update) and template/timezone lookups, but lacked the "sending schedule" preview endpoints (which show what emails are queued for today/tomorrow/day-after) and the create-from-template shortcut.

### 1.3 Scheduled Emails (2 new files, new section)

| File | Endpoint | Method | Path |
|------|----------|--------|------|
| `17-scheduled-emails/01-get-all-scheduled-emails.md` | Get all scheduled emails | GET | `/api/scheduled-emails` |
| `17-scheduled-emails/02-get-scheduled-email.md` | Get a single scheduled email | GET | `/api/scheduled-emails/{id}` |

**Why these were missing:** The API reference has a standalone "Scheduled Emails" section with top-level endpoints not scoped to a campaign or lead. The local folder previously only had campaign-scoped (`02-campaigns/14-get-scheduled-emails.md`) and lead-scoped (`03-leads/14-get-lead-scheduled-emails.md`) versions. The `17-scheduled-emails/` directory is entirely new.

---

## 2. Missing Guides Documentation (47 files added)

The entire guides site at `docs.emailbison.com` had zero local representation. This content is conceptual documentation, walkthroughs, and workflow guides that supplement the API reference. All 47 pages were extracted and organized under `emailbison/guides/`.

### 2.1 Get Started (5 files)

| File | Source Page |
|------|------------|
| `guides/01-get-started/01-introduction.md` | Introduction to the docs, how to navigate |
| `guides/01-get-started/02-making-api-requests.md` | How to make HTTP requests, testing endpoints |
| `guides/01-get-started/03-notes-and-terminology.md` | Key terms: campaigns, leads, sender emails, sequences, etc. |
| `guides/01-get-started/04-authentication.md` | Bearer token authentication, generating API tokens |
| `guides/01-get-started/05-pagination.md` | Pagination patterns for list endpoints |

### 2.2 Low-Code Tools (14 files)

| File | Source Page |
|------|------------|
| `guides/02-low-code-tools/01-introduction.md` | Overview of low-code integrations (Clay, Zapier, Make) |
| `guides/02-low-code-tools/02-clay-overview.md` | Clay integration overview |
| `guides/02-low-code-tools/03-clay-workspace-setup.md` | Setting up Clay workspace for EmailBison |
| `guides/02-low-code-tools/04-clay-enrichments.md` | Native enrichments overview |
| `guides/02-low-code-tools/05-clay-find-lead.md` | Find Lead enrichment |
| `guides/02-low-code-tools/06-clay-create-or-update-lead.md` | Create or Update Lead enrichment |
| `guides/02-low-code-tools/07-clay-import-leads-to-campaign.md` | Import Lead(s) to Campaign enrichment |
| `guides/02-low-code-tools/08-clay-add-email-to-blocklist.md` | Add Email to Blocklist enrichment |
| `guides/02-low-code-tools/09-clay-add-domain-to-blocklist.md` | Add Domain to Blocklist enrichment |
| `guides/02-low-code-tools/10-clay-remove-email-from-blocklist.md` | Remove Email from Blocklist enrichment |
| `guides/02-low-code-tools/11-clay-remove-domain-from-blocklist.md` | Remove Domain from Blocklist enrichment |
| `guides/02-low-code-tools/12-clay-authenticating.md` | Authenticating Clay requests |
| `guides/02-low-code-tools/13-clay-get-requests.md` | GET requests with Clay (with examples) |
| `guides/02-low-code-tools/14-clay-post-requests.md` | POST requests with Clay (with examples) |

### 2.3 Leads (3 files)

| File | Source Page |
|------|------------|
| `guides/03-leads/01-overview.md` | Leads concepts and data model |
| `guides/03-leads/02-adding-leads.md` | Workflows for adding leads (single, bulk, CSV, upsert) |
| `guides/03-leads/03-custom-variables.md` | Creating and using custom lead variables |

### 2.4 Email Accounts (4 files)

| File | Source Page |
|------|------------|
| `guides/04-email-accounts/01-overview.md` | Sender email concepts and connection types |
| `guides/04-email-accounts/02-adding-sender-emails.md` | Adding email accounts (OAuth, IMAP/SMTP, bulk) |
| `guides/04-email-accounts/03-bulk-uploader-overview.md` | Bulk uploader tool overview |
| `guides/04-email-accounts/04-bulk-uploader-changelog.md` | Bulk uploader tool changelog |

### 2.5 Campaigns (4 files)

| File | Source Page |
|------|------------|
| `guides/05-campaigns/01-overview.md` | Campaign concepts, lifecycle, and statuses |
| `guides/05-campaigns/02-creating-campaigns.md` | Step-by-step campaign creation workflow |
| `guides/05-campaigns/03-adding-leads-to-campaign.md` | Importing and attaching leads to campaigns |
| `guides/05-campaigns/04-adding-removing-sender-emails.md` | Managing sender emails on campaigns |

### 2.6 Tags (4 files)

| File | Source Page |
|------|------------|
| `guides/06-tags/01-overview.md` | Tag system concepts |
| `guides/06-tags/02-creating-tags.md` | Creating tags via API |
| `guides/06-tags/03-attaching-tags.md` | Attaching tags to campaigns, leads, email accounts |
| `guides/06-tags/04-removing-tags.md` | Removing tags from resources |

### 2.7 Master Inbox (4 files)

| File | Source Page |
|------|------------|
| `guides/07-master-inbox/01-overview.md` | Master inbox concepts and reply management |
| `guides/07-master-inbox/02-fetching-replies.md` | Getting replies and campaign emails for a lead |
| `guides/07-master-inbox/03-responding-to-messages.md` | Composing, replying, and forwarding |
| `guides/07-master-inbox/04-attaching-leads-to-untracked-replies.md` | Linking untracked replies to leads |

### 2.8 Workspaces (5 files)

| File | Source Page |
|------|------------|
| `guides/08-workspaces/01-overview.md` | Workspace concepts and multi-tenancy |
| `guides/08-workspaces/02-creating-api-keys.md` | Generating API tokens for workspaces |
| `guides/08-workspaces/03-creating-users.md` | Creating workspace users programmatically |
| `guides/08-workspaces/04-creating-workspaces.md` | Creating new workspaces |
| `guides/08-workspaces/05-inviting-and-accepting-members.md` | Invitation and acceptance flows |

### 2.9 Webhooks (2 files)

| File | Source Page |
|------|------------|
| `guides/09-webhooks/01-overview.md` | Webhook system overview |
| `guides/09-webhooks/02-when-are-webhooks-triggered.md` | Event types and trigger conditions |

### 2.10 Walkthroughs (2 files)

| File | Source Page |
|------|------------|
| `guides/10-walkthroughs/01-creating-template-workspaces.md` | End-to-end walkthrough: creating template workspaces |
| `guides/10-walkthroughs/02-send-slack-message-on-reply.md` | End-to-end walkthrough: Slack notification on campaign reply |

---

## 3. Structural Differences (noted, not changed)

The local folder organizes content differently from the API reference in several places. These are intentional organizational choices, not gaps. Documented here for reference.

| Difference | API Reference | Local Folder |
|------------|---------------|--------------|
| Blacklist grouping | Two sections: "Email Blacklist" and "Domain Blacklist" | Combined `08-blocklist/` folder |
| Inbox naming | "Replies" | `04-inbox/` |
| Email accounts naming | "Email Accounts" | `05-sender-emails/` |
| Schedule location | Nested under "Campaigns" | Separate `10-schedules/` folder |
| Sequence location | Nested under "Campaigns" | Separate `11-sequences/` folder |
| Campaign events | Standalone "Campaign Events" section | Inside `02-campaigns/21-campaign-events-stats.md` |
| Webhook events | Separate "Webhook Events" section | Combined into `09-webhooks/` folder |
| Workspace versions | Two sections: "v1 (deprecated)" and "v1.1" | Merged `16-workspaces/` folder |
| Tags naming | "Custom Tags" | `07-tags/` |
| Variables naming | "Custom Lead Variables" | `14-custom-variables/` |

---

## 4. Items Confirmed as NOT Missing

During the audit, several items initially appeared to be gaps but were confirmed as already covered:

| Apparent Gap | Actually Covered By |
|-------------|---------------------|
| "Import leads by IDs" | `02-campaigns/10-import-leads-to-campaign.md` (uses `/api/campaigns/{id}/leads/attach-leads`) |
| Campaigns v1.1 sequence endpoints | `11-sequences/01-03` (already use `/api/campaigns/v1.1/` paths) |
| "Campaign details" (GET single) | `02-campaigns/03-get-campaign.md` |
| "Import sender emails by ID" | `02-campaigns/16-attach-sender-emails.md` |
| "Get full normalized stats by date" | `02-campaigns/19-stats-by-date.md` |
| "Breakdown of events by date" | `02-campaigns/21-campaign-events-stats.md` |

---

## 5. Final File Inventory

### API Reference Sections (17 sections, 153 files)

| # | Section | Files |
|---|---------|-------|
| 01 | Account Management | 4 |
| 02 | Campaigns | 24 |
| 03 | Leads | 18 |
| 04 | Inbox (Replies) | 14 |
| 05 | Sender Emails (Email Accounts) | 13 |
| 06 | Warmup | 5 |
| 07 | Tags | 10 |
| 08 | Blocklist | 10 |
| 09 | Webhooks | 8 |
| 10 | Schedules | 8 |
| 11 | Sequences | 6 |
| 12 | Reply Templates | 5 |
| 13 | Custom Tracking Domains | 4 |
| 14 | Custom Variables | 2 |
| 15 | Ignore Phrases | 4 |
| 16 | Workspaces | 16 |
| 17 | Scheduled Emails | 2 |

### Guides Sections (10 sections, 47 files)

| # | Section | Files |
|---|---------|-------|
| 01 | Get Started | 5 |
| 02 | Low-Code Tools | 14 |
| 03 | Leads | 3 |
| 04 | Email Accounts | 4 |
| 05 | Campaigns | 4 |
| 06 | Tags | 4 |
| 07 | Master Inbox | 4 |
| 08 | Workspaces | 5 |
| 09 | Webhooks | 2 |
| 10 | Walkthroughs | 2 |
