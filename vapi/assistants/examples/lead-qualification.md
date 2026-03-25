# Lead Qualification Assistant Documentation

## Overview

This guide explains how to build an outbound sales assistant using Vapi that qualifies prospects and schedules meetings. The system captures BANT qualification data, handles objections, updates CRM records, and manages calendar bookings.

## Key Capabilities

The assistant can:
- Gather Budget, Authority, Need, and Timeline information
- Handle prospect objections professionally
- Log call outcomes with structured data
- Schedule meetings on integrated calendars
- Update CRM systems with qualified lead status

## Prerequisites

You'll need:
- A Vapi account (dashboard.vapi.ai)
- CRM or spreadsheet data for prospects
- Calendar system access (Google Calendar or alternative)

## Implementation Steps

### 1. Sample Data Preparation

The documentation provides downloadable CSV files:
- **leads.csv** - Prospect contact information
- **products.csv** - Product/service details
- **call_outcomes.csv** - Call result tracking

Files can be uploaded via the Vapi dashboard or programmatically using the TypeScript Server SDK.

### 2. Sales Tools Configuration

Create function tools for:
- Lead lookup and retrieval
- Qualification scoring based on BANT criteria
- CRM record updates
- Meeting scheduling

### 3. Assistant Setup

**System Prompt Foundation:**
"You are an outbound SDR. Goals: get permission, qualify with BANT, schedule a meeting, and log the outcome. Keep responses brief and professional."

**Key Elements:**
- Clear opening message requesting conversation permission
- Structured output capture for all qualification fields
- Tool integration for CRM and calendar operations

### 4. Initiating Calls

The SDK supports both web-based and phone outbound calls, with sample code provided in TypeScript, Python, and cURL formats.

### 5. Testing & Scaling

After setup, test with real phone numbers and consider CRM integration, calendar connectivity, and escalation workflows for complex deals.
