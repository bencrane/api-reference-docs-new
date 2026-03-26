#!/usr/bin/env python3
"""Fetch all Vapi documentation pages and save them as markdown files."""

import subprocess
import json
import os
import time
import re
import sys

BASE_DIR = "/Users/benjamincrane/api-reference-docs-new/vapi"

# All docs URLs organized by section (excluding changelog)
URLS = [
    # 01-quickstart
    "quickstart/introduction",
    "quickstart/phone",
    "quickstart/web",
    "quickstart",
    "how-vapi-works",
    # 02-guides
    "guides",
    "composer",
    "prompting-guide",
    "debugging",
    "faq",
    "resources",
    # 03-assistants
    "assistants/quickstart",
    "assistants/concepts/transient-vs-permanent-configurations",
    "assistants/dynamic-variables",
    "assistants/personalization",
    "assistants/voice-formatting-plan",
    "assistants/flush-syntax",
    "assistants/background-messages",
    "assistants/idle-messages",
    "assistants/assistant-hooks",
    "assistants/pronunciation-dictionaries",
    "assistants/call-analysis",
    "assistants/call-recording",
    "assistants/structured-outputs-quickstart",
    "assistants/structured-outputs-examples",
    # 03-assistants/examples
    "assistants/examples/appointment-scheduling",
    "assistants/examples/lead-qualification",
    "assistants/examples/inbound-support",
    "assistants/examples/voice-widget",
    "assistants/examples/docs-agent",
    "assistants/examples/support-escalation",
    "assistants/examples/multilingual-agent",
    # 04-customization
    "customization/multilingual",
    "customization/speech-configuration",
    "customization/voice-pipeline-configuration",
    "customization/provider-keys",
    "customization/custom-keywords",
    "customization/custom-voices/custom-voice",
    "customization/custom-voices/elevenlabs",
    "customization/custom-voices/playht",
    "customization/custom-transcriber",
    "customization/custom-voices/custom-tts",
    "customization/custom-llm/fine-tuned-openai-models",
    "customization/custom-llm/using-your-server",
    "customization/tool-calling-integration",
    "customization/jwt-authentication",
    # 05-tools
    "tools",
    "tools/default-tools",
    "tools/voicemail-tool",
    "tools/custom-tools",
    "tools/code-tool",
    "tools/client-side-websdk",
    "tools/tool-rejection-plan",
    "tools/static-variables-and-aliases",
    "tools/custom-tools-troubleshooting",
    "tools/google-calendar",
    "tools/google-sheets",
    "tools/slack",
    "tools/go-high-level",
    "tools/encryption",
    "tools/mcp",
    # 06-knowledge-base
    "knowledge-base",
    "knowledge-base/using-query-tool",
    "knowledge-base/custom-knowledge-base",
    "knowledge-base/migrating-from-trieve",
    # 07-squads
    "squads",
    "squads-example",
    "squads/handoff",
    "squads/silent-handoffs",
    "squads/examples/clinic-triage-scheduling-handoff-tool",
    "squads/examples/clinic-triage-scheduling",
    "squads/examples/ecommerce-order-management",
    "squads/examples/property-management",
    "squads/examples/multilingual-support",
    # 08-calls
    "phone-calling",
    "calls/outbound-calling",
    "calls/websocket-transport",
    "calls/call-features",
    "calls/customer-join-timeout",
    "calls/voicemail-detection",
    "call-forwarding",
    "calls/assistant-based-warm-transfer",
    "calls/call-dynamic-transfers",
    "calls/call-handling-with-vapi-and-twilio",
    "phone-calling/in-call-control/transfer-calls/debug-forwarding-drops",
    "calls/call-queue-management",
    "calls/call-concurrency",
    "calls/call-ended-reason",
    "calls/troubleshoot-call-errors",
    # 09-phone-numbers
    "free-telephony",
    "phone-numbers/inbound-sms",
    "phone-numbers/import-twilio",
    "phone-numbers/phone-number-hooks",
    "telnyx",
    # 10-sip
    "advanced/sip",
    "advanced/sip/sip-trunk",
    "advanced/sip/sip-networking",
    "advanced/sip/twilio",
    "advanced/sip/telnyx",
    "advanced/sip/zadarma",
    "advanced/sip/plivo",
    "advanced/sip/amazon-chime",
    "advanced/sip/troubleshoot-sip-trunk-credential-errors",
    # 11-outbound-campaigns
    "outbound-campaigns/quickstart",
    "outbound-campaigns/overview",
    # 12-chat
    "chat/quickstart",
    "chat/streaming",
    "chat/non-streaming",
    "chat/openai-compatibility",
    "chat/session-management",
    "chat/variable-substitution",
    "chat/sms-chat",
    "chat/web-widget",
    # 13-server-url
    "server-url",
    "server-url/setting-server-urls",
    "server-url/events",
    "server-url/spam-call-rejection",
    "server-url/developing-locally",
    "server-url/server-authentication",
    # 14-workflows
    "workflows/quickstart",
    "workflows/overview",
    "workflows/examples/appointment-scheduling",
    "workflows/examples/lead-qualification",
    "workflows/examples/clinic-triage-scheduling",
    "workflows/examples/ecommerce-order-management",
    "workflows/examples/property-management",
    "workflows/examples/multilingual-support",
    # 15-observability
    "observability/evals-quickstart",
    "observability/evals-advanced",
    "observability/simulations-quickstart",
    "observability/simulations-advanced",
    "observability/boards-quickstart",
    "observability/scorecard-quickstart",
    # 16-test
    "test/test-suites",
    "test/chat-testing",
    "test/voice-testing",
    # 17-providers
    "providers/voice/vapi-voices",
    "providers/voice/vapi-voices/legacy-migration",
    "providers/voice/elevenlabs",
    "providers/voice/playht",
    "providers/voice/azure",
    "providers/voice/openai",
    "providers/voice/cartesia",
    "providers/voice/imnt",
    "providers/voice/rimeai",
    "providers/voice/deepgram",
    "providers/voice/inworld",
    "providers/model/openai",
    "providers/model/azure-openai",
    "providers/model/anthropic-bedrock",
    "providers/model/gemini",
    "providers/model/groq",
    "providers/model/deepinfra",
    "providers/model/perplexity",
    "providers/model/togetherai",
    "providers/model/openrouter",
    "providers/transcriber/deepgram",
    "providers/transcriber/google",
    "providers/transcriber/gladia",
    "providers/transcriber/speechmatics",
    "providers/transcriber/talkscriber",
    "providers/transcriber/assembly-ai",
    "providers/cloud/s3",
    "providers/cloud/gcp",
    "providers/cloud/cloudflare",
    "providers/cloud/supabase",
    "providers/observability/langfuse",
    "providers/voiceflow",
    "providers/chat-dash",
    "providers/vapify",
    "providers/voicerr-ai",
    "providers/voiceaiwrapper",
    "providers/sympana-connector",
    # 18-security-and-privacy
    "security-and-privacy/data-flow",
    "security-and-privacy/recording-consent-plan",
    "security-and-privacy/GDPR",
    "security-and-privacy/hipaa",
    "security-and-privacy/pci",
    "security-and-privacy/proxy-server",
    "security-and-privacy/static-ip-addresses",
    "tcpa-consent",
    # 19-enterprise
    "enterprise/plans",
    # 20-ivr
    "ivr-navigation",
    # 21-voice-fallback
    "voice-fallback-plan",
    "customization/transcriber-fallback-plan",
    "openai-realtime",
    # 22-background-speech
    "documentation/assistants/conversation-behavior/background-speech-denoising",
    # 23-cli
    "cli",
    "cli/init",
    "cli/mcp",
    "cli/webhook",
    "cli/auth",
    # 24-sdk
    "sdk/mcp-server",
    # 25-support
    "support",
    "issue-reporting",
    "glossary",
    # 26-api-reference
    "api-reference/assistants/list",
    "api-reference/assistants/create",
    "api-reference/assistants/get",
    "api-reference/assistants/delete",
    "api-reference/assistants/update",
    "api-reference/squads/list",
    "api-reference/squads/create",
    "api-reference/squads/get",
    "api-reference/squads/delete",
    "api-reference/squads/update",
    "api-reference/calls/list",
    "api-reference/calls/create",
    "api-reference/calls/get",
    "api-reference/calls/delete",
    "api-reference/calls/update",
    "api-reference/chats/list",
    "api-reference/chats/create",
    "api-reference/chats/get",
    "api-reference/chats/delete",
    "api-reference/chats/create-response",
    "api-reference/campaigns/campaign-controller-find-all",
    "api-reference/campaigns/campaign-controller-create",
    "api-reference/campaigns/campaign-controller-find-one",
    "api-reference/campaigns/campaign-controller-remove",
    "api-reference/campaigns/campaign-controller-update",
    "api-reference/sessions/list",
    "api-reference/sessions/create",
    "api-reference/sessions/get",
    "api-reference/sessions/delete",
    "api-reference/sessions/update",
    "api-reference/phone-numbers/list",
    "api-reference/phone-numbers/create",
    "api-reference/phone-numbers/get",
    "api-reference/phone-numbers/delete",
    "api-reference/phone-numbers/update",
    "api-reference/tools/list",
    "api-reference/tools/create",
    "api-reference/tools/get",
    "api-reference/tools/delete",
    "api-reference/tools/update",
    "api-reference/tools/tool-controller-test-code-execution",
    "api-reference/tools/tool-controller-mcp-child-tools-discover",
    "api-reference/files/list",
    "api-reference/files/create",
    "api-reference/files/get",
    "api-reference/files/delete",
    "api-reference/files/update",
    "api-reference/structured-outputs/structured-output-controller-find-all",
    "api-reference/structured-outputs/structured-output-controller-create",
    "api-reference/structured-outputs/structured-output-controller-find-one",
    "api-reference/structured-outputs/structured-output-controller-remove",
    "api-reference/structured-outputs/structured-output-controller-update",
    "api-reference/structured-outputs/structured-output-controller-run",
    "api-reference/insight/insight-controller-find-all",
    "api-reference/insight/insight-controller-create",
    "api-reference/insight/insight-controller-find-one",
    "api-reference/insight/insight-controller-remove",
    "api-reference/insight/insight-controller-update",
    "api-reference/insight/insight-controller-run",
    "api-reference/insight/insight-controller-preview",
    "api-reference/eval/eval-controller-get-paginated",
    "api-reference/eval/eval-controller-create",
    "api-reference/eval/eval-controller-get",
    "api-reference/eval/eval-controller-remove",
    "api-reference/eval/eval-controller-update",
    "api-reference/eval/eval-controller-get-run",
    "api-reference/eval/eval-controller-remove-run",
    "api-reference/eval/eval-controller-get-runs-paginated",
    "api-reference/eval/eval-controller-run",
    "api-reference/observability-scorecard/scorecard-controller-get",
    "api-reference/observability-scorecard/scorecard-controller-remove",
    "api-reference/observability-scorecard/scorecard-controller-update",
    "api-reference/observability-scorecard/scorecard-controller-get-paginated",
    "api-reference/observability-scorecard/scorecard-controller-create",
    "api-reference/provider-resources/provider-resource-controller-get-provider-resources-paginated",
    "api-reference/provider-resources/provider-resource-controller-create-provider-resource",
    "api-reference/provider-resources/provider-resource-controller-get-provider-resource",
    "api-reference/provider-resources/provider-resource-controller-delete-provider-resource",
    "api-reference/provider-resources/provider-resource-controller-update-provider-resource",
    "api-reference/analytics/get",
    "api-reference/webhooks/server-message",
    "api-reference/webhooks/client-message",
]

# Map URL paths to local folder/file structure
def url_to_path(url_path):
    """Convert a URL path to a local file path within the vapi folder."""
    parts = url_path.strip("/").split("/")

    # The last part becomes the filename
    filename = parts[-1] + ".md"

    # Everything before becomes the directory path
    if len(parts) > 1:
        dir_path = os.path.join(BASE_DIR, *parts[:-1])
    else:
        dir_path = BASE_DIR

    return os.path.join(dir_path, filename)


def fetch_page(url_path):
    """Fetch a page using curl and return the content."""
    url = f"https://docs.vapi.ai/{url_path}"
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", "30", url],
            capture_output=True, text=True, timeout=35
        )
        return result.stdout
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def html_to_markdown(html_content):
    """Basic HTML to markdown conversion."""
    if not html_content:
        return ""

    # Try to extract main content area
    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)

    # Convert common HTML elements to markdown
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<code>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', content, flags=re.DOTALL)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode HTML entities
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")
    content = content.replace('&nbsp;', ' ')

    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return content


def main():
    total = len(URLS)
    print(f"Fetching {total} Vapi documentation pages...")

    for i, url_path in enumerate(URLS, 1):
        file_path = url_to_path(url_path)

        # Skip if already exists
        if os.path.exists(file_path):
            print(f"[{i}/{total}] SKIP (exists): {url_path}")
            continue

        print(f"[{i}/{total}] Fetching: {url_path}")

        # Create directory
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Fetch and save
        html = fetch_page(url_path)
        if html:
            # Save raw content - we'll use WebFetch for proper conversion
            # For now save what we get
            markdown = html_to_markdown(html)
            with open(file_path, 'w') as f:
                f.write(markdown)
            print(f"  -> Saved: {file_path}")
        else:
            print(f"  -> FAILED: {url_path}")

        # Small delay to be respectful
        time.sleep(0.3)

    print(f"\nDone! Fetched {total} pages.")


if __name__ == "__main__":
    main()
