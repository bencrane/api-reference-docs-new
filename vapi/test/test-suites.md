# Test Suites Documentation

## Overview

The Test Suites feature provides end-to-end automation for evaluating AI voice agents. According to the documentation, this system "simulates an AI tester that interacts with your voice agent by following a pre-defined script." The platform then uses an LLM to assess whether interactions met defined objectives.

## Key Setup Steps

The creation process involves five main stages:

1. **Initialization**: Access the Test tab and create a new Test Suite
2. **Configuration**: Enter suite details and assign a phone number with an assistant
3. **Test Case Addition**: Add up to 50 individual test cases
4. **Case Setup**: Define scripts, test type (Chat or Voice), evaluation rubrics, and attempt counts
5. **Execution**: Run tests and review results with pass/fail indicators

## How Testing Works

The workflow follows this sequence: simulation of agent interactions, transcript capture, automated LLM evaluation against success criteria, and detailed results display. Each test case shows attempts made, the model's reasoning, full transcripts, and configured parameters.

## Practical Examples Provided

The documentation includes three scenarios: billing support (simple structured script), account inquiries (free-form approach), and appointment scheduling (detailed personality-based script). Each demonstrates varying complexity levels for tailoring tests to specific needs.

## Cost

"Test calls cost you the same as regular calls," so testing is not complimentary.
