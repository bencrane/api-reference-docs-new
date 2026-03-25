# Transient vs Permanent Configurations

## Overview

The documentation contrasts two approaches for configuring Vapi assistants. "Choose between **transient** (inline) and **permanent** (stored) configurations to optimize your Vapi implementation for flexibility, reusability, and management needs."

## Key Differences

| Aspect | Transient | Permanent |
|--------|-----------|-----------|
| **Definition** | Complete JSON in API request | ID reference to stored configuration |
| **Storage** | Exists only during API call | Stored on Vapi servers |
| **Reusability** | Defined per request | Reusable across multiple calls |
| **Dashboard access** | Not visible | Visible and manageable |
| **Best for** | Dynamic, personalized scenarios | Shared, reusable setups |

## When to Use Transient Configurations

Transient configurations suit:
- **Dynamic personalization:** Embedding customer-specific data directly in system messages
- **A/B testing:** Experimenting with different setups without permanent storage
- **Temporary campaigns:** Short-term, event-specific assistants
- **Development testing:** Rapid prototyping without managing stored configs

The documentation notes that "transient configurations exist only during the API call and cannot be managed through the dashboard or reused across calls."

## When to Use Permanent Configurations

Permanent configurations work best for:
- **Shared resources:** Team collaboration across departments
- **Dashboard management:** Non-technical user configuration
- **Reusable setups:** Consistent workflows across calls
- **Version control:** Tracking configuration changes

## Mixed Approach

The guide demonstrates combining both types—referencing stored assistants while embedding dynamic configurations for specific scenarios like specialized support roles.

## Best Practices Summary

**Use transient for:** Customer-specific data, testing, personalization, and prototyping

**Use permanent for:** Multi-team access, dashboard management, consistency requirements, and change tracking
