# Voice Testing Documentation

## Overview
The page describes an automated testing platform that "enable[s] you to test your AI voice agents through simulated phone conversations." The system pairs a user's voice agent with a testing agent on actual phone calls to evaluate performance.

## How It Works
The testing process follows four steps: simulation (the testing agent calls the user's agent), conversation (both AIs interact naturally), recording (calls are documented and transcribed), and assessment (transcripts are evaluated against user-defined criteria using an LLM).

## Key Advantages
The platform offers three main benefits: realistic testing through genuine phone interactions, quality evaluation of voice characteristics like clarity and tone, and comprehensive verification that the entire voice infrastructure functions properly.

## Setup Instructions
Users can integrate voice tests into Test Suites by navigating to the Test tab, selecting Test Suites, creating or editing a suite, choosing Voice as the test type, and defining scripts and success metrics.

## Important Constraints
The documentation notes that "Voice tests require more time to execute compared to chat tests" and that "Each test consumes calling minutes from your account." Additionally, individual calls are capped at 15 minutes maximum.
