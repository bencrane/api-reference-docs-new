# Understanding Call Concurrency

## Overview

Vapi's call concurrency feature manages how many simultaneous calls your account can handle. The platform allocates **10 concurrent call slots by default**, with each active call occupying one slot. When capacity is exhausted, incoming calls queue until slots become available.

### Key Learning Objectives

The documentation covers four main areas:
- Default concurrency allocations and adequacy assessment
- Keeping workloads within plan constraints
- Increasing capacity through the Vapi Dashboard
- Monitoring concurrency via API and analytics tools

## Core Concepts

**Inbound vs. Outbound Patterns:**
- Inbound agent services rarely encounter limits unless traffic spikes occur
- Outbound calling campaigns more frequently approach capacity constraints, especially during large-scale operations

The system enforces these limits to maintain platform reliability across all customers.

## Practical Management Strategies

**For outbound campaigns:** Divide large contact lists into batches of 50-100 numbers and execute sequentially to maintain manageable concurrency levels.

**For high-volume operations:** Accounts exceeding 50,000 monthly minutes should explore custom plans or add-on bundles offering flexible capacity expansion.

## Upgrading Capacity

Users can increase reserved call lines directly through the Vapi Dashboard (Settings > Billing > Reserved Concurrency) without support intervention. Changes take effect immediately.

## Monitoring Approaches

**API Method:** The POST /call response includes a `subscriptionLimits` object showing:
- Current concurrency limit
- Remaining available slots
- Whether calls are being blocked

**Analytics Method:** The `/analytics` endpoint reveals historical usage patterns, helping justify capacity increases based on documented demand patterns.
