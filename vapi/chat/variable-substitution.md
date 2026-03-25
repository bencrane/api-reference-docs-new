# Variable Substitution in Sessions

## Overview

The documentation explains that when using the Chat API with sessions, variables are replaced at session creation and "baked into" the stored assistant configuration. Once substituted, template placeholders no longer exist in the session.

The system uses LiquidJS for variable substitution, supporting the `{{ }}` syntax with access to filters and conditionals beyond simple replacement.

## Key Mechanics

**At session creation:** The system processes your assistant's template variables (like `"Hello {{name}}"`), substitutes all placeholders using LiquidJS, stores the pre-substituted assistant, and saves original variable values in session metadata.

**At chat creation:** The system loads the pre-substituted assistant. Since no `{{ }}` placeholders remain, any new variable values passed in the chat request have no effect on already-substituted text.

## Important Behaviors

Variables persist across all chats within a session once set during creation. However, passing new `variableValues` in subsequent chat requests won't override the session's pre-substituted assistant because the template placeholders no longer exist.

To use different variable values mid-session, you must provide a fresh template containing `{{ }}` placeholders along with the new values in your chat request.

## Best Practices

For consistent variables throughout a session, set `assistantOverrides.variableValues` during session creation, then use subsequent requests with only the `sessionId` and `input`.

For different variables per conversation, consider: avoiding sessions entirely, overriding with fresh templates, or creating separate sessions for each unique variable context.
