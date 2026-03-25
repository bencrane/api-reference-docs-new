# Scorecard Quickstart Documentation

## Overview

The documentation explains how to create scorecards that automatically grade calls based on structured outputs. As stated, scorecards "compute objective quality metrics from the call's structured outputs after the call ends."

## Key Components

**What Scorecards Do:**
Scorecards perform three primary functions: they evaluate outputs against defined metrics, allocate points when conditions are satisfied, and enable filtering calls by scorecard metrics.

**Timing:** Scorecards are generated after call completion, typically within seconds, and appear in `call.artifact.scorecards`.

**Data Source:** Scorecards reference "structured outputs attached to the assistant (`artifactPlan.structuredOutputIds`)" and work exclusively with number, integer, or boolean data types.

## Implementation Steps

The quickstart covers four main steps:

1. **Create a scorecard** via API with metrics that reference structured output IDs and conditions
2. **Attach to an assistant** by patching the assistant with scorecard IDs
3. **Run a call** using the configured assistant
4. **Retrieve scores** from the call response after waiting a few seconds

## Technical Details

**Supported Comparators:** `=`, `!=`, `>`, `<`, `>=`, `<=` (boolean metrics support only `=`)

**Point Allocation:** All metric conditions must sum to 100 points total

**Response Structure:** Scorecards return `score`, `scoreNormalized`, and `metricPoints` indicating "points awarded per structured output."

## Advanced Features

The documentation includes patterns for multiple scorecards and transient inline scorecards for testing without saving permanent scorecard definitions.
