# Invite Multiple Users

## Endpoint Overview

The POST endpoint at `https://api.elevenlabs.io/v1/workspace/invites/add-bulk` enables bulk email invitations to join a workspace.

## Key Functionality

This endpoint "sends email invitations to join your workspace to the provided emails" and requires verified domain email addresses. New users will be prompted to create accounts, while existing users can accept invites to gain workspace access using available seats.

## Permission Requirements

Only workspace members possessing the `WORKSPACE_MEMBERS_INVITE` permission can call this endpoint.

## Request Parameters

The request body accepts:
- **emails** (required): Array of email addresses to invite
- **seat_type** (optional): One of `workspace_admin`, `workspace_member`, or `workspace_lite_member`
- **group_ids** (optional): Array of group identifiers for the user

## Response

On success, the API returns a response object with a `status` field containing "ok" if the request succeeded.

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the basic invitation creation pattern with email arrays.

## API Server Locations

The service is accessible via multiple regional endpoints including standard US, EU residency, and India residency servers.
