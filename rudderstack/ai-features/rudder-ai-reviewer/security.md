# Rudder AI Reviewer Security and Data Privacy Beta

Understand Rudder AI Reviewer’s data handling, security model, and privacy guarantees.

* * *

  * __2 minute read

  * 


This guide explains Rudder AI Reviewer’s security model and data privacy guarantees.

## Data sent for analysis

The review payload sent to Rudder AI Reviewer contains the following information:

  * **PR metadata** : PR number, title, branch names, file count, line counts
  * **Code diffs** : Patch content for changed files. It contains the added/removed/modified lines only, not full file contents
  * **Repository metadata** : Owner, name, visibility (public/private), primary language
  * **SDK info** : SDK name, version, installation type (npm or CDN)
  * **Framework info** : Framework name and version


## Data not sent or stored

Rudder AI Reviewer does not send or store the following data:

  * Full source code files
  * Environment variables or secrets
  * Developer personal information
  * Git history or commit contents beyond the PR diff
  * Contents of `.env`, credentials, or other secret files


## AI model provider

Rudder AI Reviewer uses [Amazon Bedrock](<https://aws.amazon.com/bedrock/>) for AI-powered analysis.

Code diffs are processed in-memory and discarded after the review is generated. The AI model does not retain context between reviews.

> ![info](/docs/images/info.svg)
> 
> **No data is used** to train AI models and code diffs are **not stored** by the AI provider.

## Authentication and transport

The action authenticates with Rudder AI using your [workspace-level Service Access Token](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/get-started/#prerequisites>) stored as a GitHub Actions secret.

The workflow also uses **GitHub token** to read PR diffs and post review comments. It is scoped to the current repository and requires `contents: read` and `pull-requests: write` permissions.

All communication uses **HTTPS (TLS 1.2+)** and the action runs on your own GitHub Actions runner. RudderStack **does not host** any infrastructure for the action execution.

## PII detection

Rudder AI Reviewer actively flags potential PII exposure in event properties, for example, raw email addresses, phone numbers, or user names passed as tracking properties. This helps catch compliance issues (GDPR, CCPA, etc.) before code reaches production.

## See more

  * [Rudder AI Reviewer Overview](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/>)
  * [Rudder AI Reviewer Setup Guide](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/get-started/>)
  * [Rudder AI Reviewer FAQ](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/faq/>)