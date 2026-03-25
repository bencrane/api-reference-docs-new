# Code Tool Documentation

## Overview

The Code Tool enables execution of custom TypeScript code within a Vapi assistant's infrastructure, eliminating the need for server setup. As stated in the documentation, it allows you to "Execute custom TypeScript code directly within your assistant without setting up a server."

## Primary Use Cases

Code tools are recommended when you need to:

* Transform or process conversational data
* Make HTTP requests to external APIs
* Perform calculations or business logic
* Bypass webhook server maintenance overhead

## Implementation Basics

### Required Components

Creating a code tool necessitates:

* A descriptive tool name (e.g., `get_customer_data`)
* Clear description explaining the tool's functionality
* TypeScript code for execution
* Input parameter definitions
* Secure environment variable storage

### Accessible Objects

Your code can access two key objects:

* **`args`**: Parameters passed by the assistant
* **`env`**: Environment variables for sensitive data

## Practical Examples

The documentation provides two detailed examples:

**Customer Lookup**: Retrieves customer information via API using environment variables for authentication.

**Order Processing**: A more complex implementation that calculates totals, fetches product details, and creates orders through multiple API calls.

## Technical Constraints

* Maximum execution time: 60 seconds (default: 10 seconds)
* No file system access in isolated environment
* Limited memory allocation
* HTTP/HTTPS requests only

## Integration with Assistants

Once created, code tools integrate via API by updating the assistant configuration with the tool ID.

## Code Tools vs Custom Function Tools

Code Tools excel for quick integrations requiring minimal setup, while Custom Function Tools offer greater control for complex logic and existing infrastructure.
