# Rudder AI Reviewer Beta

Automatically review pull requests for RudderStack SDK instrumentation issues using AI-powered analysis.

* * *

  * __3 minute read

  * 


This guide explains how Rudder AI Reviewer works and how you can use it to review your pull requests for SDK instrumentation issues.

## Overview

**Rudder AI Reviewer** is a GitHub Action that analyzes code changes in your pull requests to detect problems like missing event properties, naming convention violations, and best practice issues. It then posts actionable feedback with suggested fixes directly on your PRs.

> ![success](/docs/images/tick.svg)
> 
> Rudder AI Reviewer catches instrumentation issues before they reach production — like missing event properties, inconsistent event naming, deprecated API usage, potential PII exposure, and more.

## Supported SDKs

  * [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) — via `npm` package or CDN `<script>` tag


> ![announcement](/docs/images/announcement.svg)
> 
> Support for mobile SDKs (iOS, Android) and additional platforms is coming soon.

## What it reviews

The AI reviewer analyzes your RudderStack SDK instrumentation changes and provides feedback across multiple categories:

  * **Tracking plan violations** : Deviations from your defined Tracking Plan
  * **Missing events** : Important user actions that aren’t being tracked
  * **Best practice issues** : Improvements to follow RudderStack SDK best practices
  * **Security concerns** : Potential PII exposure or other security issues in your instrumentation
  * **Performance issues** : Potential performance bottlenecks in your instrumentation
  * **Deprecated API usage** : Usage of deprecated APIs in your instrumentation that are no longer supported
  * **Incorrect property usage** : Usage of incorrect properties in your instrumentation that are not supported by the SDK


## How it works

When a pull request is opened or updated, Rudder AI Reviewer runs through the following pipeline:

  1. **PR change detection** : Fetches changed files via the GitHub API and parses the unified diffs to extract added, modified, and removed lines.
  2. **SDK detection** : Extracts the SDK version by scanning `package.json` and lock files for `@rudderstack/analytics-js`, or parsing the HTML/JS files for RudderStack CDN script tags.
  3. **Framework detection** : Identifies the frontend framework from `package.json` dependencies — this helps the AI provide framework-specific recommendations.
  4. **AI analysis** : Sends a review payload containing PR metadata, code diffs, SDK info, and framework info to RudderStack’s AI review service over HTTPS. Rudder AI analyzes the instrumentation changes and returns a structured review.
  5. **Comment posting** : Posts two types of comments on the PR — a **summary comment** with the overall assessment and **inline review comments** on specific code lines with suggested fixes.


Note that:

  * Each time the action runs, the summary comment is updated with the latest analysis.
  * For inline review comments, the AI attempts to avoid posting duplicate comments. However, if new changes are introduced, additional inline comments may be generated.
  * Only code diffs (changed lines) are sent for analysis — **not** your entire codebase.


> ![info](/docs/images/info.svg)
> 
> No source code is stored by RudderStack or its AI provider. See [Rudder AI Reviewer Security](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/security/>) for more details.

## See more

  * [Rudder AI Reviewer Setup Guide](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/get-started/>)
  * [Rudder AI Reviewer Security](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/security/>)
  * [Rudder AI Reviewer FAQ](<https://www.rudderstack.com/docs/ai-features/rudder-ai-reviewer/faq/>)