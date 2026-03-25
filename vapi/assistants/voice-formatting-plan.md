# Voice Formatting Plan

## Overview

The system automatically converts raw language model text into speech-friendly format through a process called **Voice Input Formatted**, which is active by default. This transformation handles number expansion, abbreviation clarification, and phone number spacing to improve TTS naturalness.

## Processing Workflow

The formatter executes 14 sequential transformation steps:

1. **removeAngleBracketContent** - Strips `<...>` tags except `<break>`, `<spell>`, or `<< >>`
2. **removeMarkdownSymbols** - Eliminates markdown characters like underscores and backticks
3. **removePhrasesInAsterisks** - Removes asterisk-wrapped text (disabled by default)
4. **replaceNewLinesWithPeriods** - Changes `\n` to periods for smoother delivery
5. **replaceColonsWithPeriods** - Converts colons to periods
6. **formatAcronyms** - Converts known acronyms to lowercase format
7. **formatDollarAmounts** - Transforms "$42.50" to "forty two dollars and fifty cents"
8. **formatEmails** - Changes "@" to "at" and "." to "dot"
9. **formatDates** - Converts date strings to spoken format
10. **formatTimes** - Simplifies time expressions
11. **formatDistances/Units/Percentages/PhoneNumbers** - Expands measurements and contact info
12. **formatNumbers** - Handles years, large numbers, decimals, and negatives
13. **removeAsterisks** - Eliminates remaining asterisk characters
14. **Applying Replacements** - Executes custom user-defined substitutions

## Customization Options

**Disabling:** Set `voice.chunkPlan.formatPlan.enabled = false`

**Number Cutoff:** Controls digit reading threshold (default: 2025)

**Custom Replacements:** Two types available—
- Exact matches: `{ type: 'exact', key: 'hello', value: 'hi' }`
- Pattern-based: `{ type: 'regex', regex: '\b[a-zA-Z]{5}\b', value: 'hi' }`

Currently, only replacements and the number cutoff are configurable.

## Key Takeaway

Voice formatting enhances TTS clarity through targeted transformations while remaining fully customizable or disableable based on your requirements.
