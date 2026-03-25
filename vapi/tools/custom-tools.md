# Custom Tools Documentation

## Overview
The Vapi platform enables developers to build custom tools for their assistants. The documentation recommends using the dashboard's Tools section for ease of use, though API configuration is available for advanced users.

## Dashboard Tool Creation

### Initial Setup
To create tools, users should navigate to the Vapi Dashboard, access the Tools section from the sidebar, and select "Create Tool."

### Configuration Steps
The dashboard guides users through several configuration phases:

**Basic Information:**
- Tool Type: Select "Function" for custom integrations
- Tool Name: Provide a descriptive identifier
- Description: Explain the tool's functionality

**Technical Settings:**
- Function Name: The identifier (e.g., `get_weather`)
- Parameters: Define expected inputs
- Server URL: Specify the hosted endpoint

**Communication Setup:**
Users can customize assistant messages during tool execution, including status updates for request initiation, completion, failures, and delays.

**Advanced Options:**
- Asynchronous execution mode
- Response timeout configuration
- Error handling strategies

## Weather Tool Example

A practical demonstration uses weather lookup functionality:
- Function identifier: `get_weather`
- Required parameter: location (string)
- API endpoint: OpenWeatherMap's weather service
- Note: Users must obtain their own API key from the service provider

## Integration Methods

### Dashboard Integration
Tools integrate into assistants through the Assistants section, where users can add tools via a dropdown selector.

### Workflow Integration
Custom tools automatically appear in workflow builders as selectable Tool Nodes.

### CLI Management
The Vapi CLI provides commands for listing, retrieving, creating, testing, and deleting tools. Local testing requires a tunneling service and the `vapi listen` command.

## API Approach

Developers preferring programmatic control can create tools using REST API calls with proper authentication headers and JSON payloads containing function specifications and server URLs.

## Request/Response Protocol

### Incoming Request Format
Vapi sends tool call requests containing:
- Timestamp information
- Tool call identifiers
- Function name and arguments
- Complete tool definition and assistant context

### Required Response Format
Servers must return JSON with this structure: "results array containing objects with toolCallId and result fields." Each response object maps to a corresponding request using the unique identifier.

**Example Response:**
```json
{
  "results": [
    {
      "toolCallId": "call_VaJOd8ZeZgWCEHDYomyCPfwN",
      "result": "San Francisco's weather is 62°C, partly cloudy."
    }
  ]
}
```

## Key Implementation Notes

Users should ensure servers are publicly accessible, properly handle incoming requests, and format responses correctly. The documentation emphasizes matching toolCallId values between requests and responses for proper context preservation.
