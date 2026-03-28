# assistant-ui Documentation Reference

Canonical local copy of the [assistant-ui](https://www.assistant-ui.com) documentation, sourced directly from the [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) GitHub repository.

**Source commit:** `6554892`
**Extracted:** 2026-03-28

## Structure

```
docs/
  index.mdx                     # Introduction
  architecture.mdx               # System architecture
  cli.mdx                        # CLI tool
  devtools.mdx                   # Developer tools
  installation.mdx               # Setup instructions
  llm.mdx                        # Agent skills / LLM integration
  react-compatibility.mdx        # React version compatibility

  primitives/                    # Unstyled, accessible React components (13 files)
  ui/                            # Pre-styled shadow/ui components (27 files)
  runtimes/                      # Backend integrations (24 files)
    ai-sdk/                        AI SDK v4/v5/v6
    mastra/                        Mastra framework
    custom/                        Custom runtimes (local, external store, thread list)
    langgraph/                     LangGraph + tutorial
    google-adk/                    Google ADK
    a2a/                           Agent-to-Agent
  cloud/                         # Assistant Cloud service (5 files)
  guides/                        # Implementation guides (15 files)
  copilots/                      # Building copilots (7 files)
  utilities/                     # Utility libraries (2 files)
  api-reference/                 # Full API reference (~33 files)
    context-providers/             AssistantRuntimeProvider, TextMessagePartProvider
    primitives/                    All primitive component APIs
    runtimes/                      Runtime hook APIs
    integrations/                  Vercel AI SDK, Data Stream, Hook Form
  migrations/                    # Version migration guides (5 files)
  react-native/                  # React Native docs (6 files)
  ink/                           # Ink/terminal docs (6 files)
```

**Total:** 146 MDX files, 22 meta.json navigation files, 6 tutorial images

## File format

Files are raw MDX (Markdown + JSX) with YAML frontmatter:

```mdx
---
title: ComposerPrimitive
description: Primitives for the text input, send button, and attachments.
---

Content with code blocks, TypeTable components, etc.
```

Custom JSX components used in the docs:
- `<Callout>` — info/warning callouts
- `<TypeTable>` — prop/type tables
- `<ParametersTable>` — function parameter tables
- `<InstallCommand>` — package install commands
- `<Tabs>` / `<Tab>` — tabbed content
- `<Steps>` / `<Step>` — step-by-step guides
- `<SourceLink>` — links to source code

## Programmatic access

`manifest.json` contains a machine-readable index of all 146 documents with paths, titles, descriptions, source URLs, and section groupings.

## Navigation ordering

Each directory contains a `meta.json` file that defines the sidebar ordering used on the live site.
