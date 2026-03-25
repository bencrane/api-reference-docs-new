# Call Analysis Documentation

## Overview

The call analysis feature performs automated summaries and quality assessments once conversations conclude. "Call analysis automatically summarizes and evaluates every call for insights and quality control." Processing typically finishes within seconds using Claude Sonnet, with GPT-4o as a backup option.

The system performs three main functions:
- Summarize conversations
- Extract structured information
- Evaluate call outcomes

Results appear in call dashboards and remain accessible through APIs, with customization available through the `analysisPlan` configuration.

## Customization Options

### Summary Prompt
Creates concise call summaries stored in `call.analysis.summary`. The default instruction asks analysts to "Summarize the call in 2-3 sentences, if applicable." Users can replace or disable this component using JSON configuration.

### Structured Data Prompt
Extracts specific information from conversations and stores results in `call.analysis.structuredData`. The baseline prompt requests data extraction "per the JSON Schema."

### Structured Data Schema
Defines output format using JSON Schema syntax, allowing custom field definitions with type specifications and required parameters.

### Success Evaluation Prompt
Determines call success based on assistant objectives inferred from system instructions, stored in `call.analysis.successEvaluation`.

### Success Evaluation Rubric
Provides scoring frameworks including:
- NumericScale (1-10)
- DescriptiveScale (Excellent/Good/Fair/Poor)
- Checklist format
- Matrix grid
- PercentageScale (0-100%)
- LikertScale
- AutomaticRubric
- PassFail (binary)

### Combined Configuration
Users can merge prompts with rubrics for comprehensive evaluation guidance.

## Results Access

Completed analyses attach to call records, viewable through dashboards or API retrieval, including summaries, extracted data, and success evaluations.
