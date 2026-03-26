# Rudder AI Reviewer FAQ Beta

Answers to frequently asked questions about Rudder AI Reviewer.

* * *

  * __less than a minute

  * 


This guide answers frequently asked questions about Rudder AI Reviewer.

### Does Rudder AI Reviewer block PR merging?

No. It is advisory only — it posts recommendations as PR comments but does not block merges. You can optionally configure GitHub branch protection rules to require issue resolution.

### Is my source code stored by RudderStack?

No. Only code diffs (changed lines) are sent for analysis. They are processed in-memory and discarded. No source code is stored by RudderStack or its AI provider.

### Is my code used to train AI models?

No. Your code is never used for model training.

### Does it work with private repositories?

Yes. It works with both public and private GitHub repositories.

### What happens if no SDK is detected?

The action exits gracefully with a warning status and message. No review comment is posted.

### I’m seeing false positives. What should I do?

Report specific examples to [RudderStack support](<mailto:support@rudderstack.com>) with the PR link and an explanation of why the flagged issue is incorrect. Rudder AI is actively tuned based on feedback.