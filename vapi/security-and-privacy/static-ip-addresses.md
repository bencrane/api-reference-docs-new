# Static IP Addresses

## Introduction to Vapi static IP addresses

Vapi facilitates static IP addresses for outbound HTTP requests. When this feature is activated, all HTTP requests from Vapi to your server will come from a consistent set of IP addresses, enabling you to implement strict firewall rules and network security policies.

## Why use static IP addresses

Static IP addresses enhance your infrastructure's security by enabling you to:

* **Control network access** - Restrict incoming traffic to only trusted sources
* **Simplify firewall rules** - Define precise IP based access controls
* **Meet compliance requirements** - Satisfy security policies that mandate IP whitelisting
* **Audit traffic sources** - Verify that requests are genuinely from Vapi's infrastructure

## Vapi's static IP addresses

When static IP addressing is enabled, all webhook requests from Vapi will originate from the following CIDR block:

* `167.150.224.0/23`

## Enabling static IP addresses

You can enable static IP addressing through the server object

### Example

```json
{
  "serverUrl": "https://your-server.example.com/webhook",
  "staticIpAddressesEnabled": true
}
```

⚠️ **Warning**: "Always test static IP configuration in a staging environment before deploying to production to avoid service disruptions."

## Need help?

If you have questions about static IP addressing, contact the support team at [support@vapi.ai](mailto:support@vapi.ai).
