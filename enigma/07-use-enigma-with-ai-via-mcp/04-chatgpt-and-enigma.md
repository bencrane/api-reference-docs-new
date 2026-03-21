# ChatGPT + Enigma​

URL: https://documentation.enigma.com/guides/ai-mcp/chatgpt

Beta

- ChatGPT's Developer Mode and MCP connector features are currently in beta.
- The Enigma remote MCP server is currently in beta.

Give ChatGPT the power of Enigma comprehensive business intelligence. With Enigma MCP tools, ChatGPT becomes a business research expert, perfect for analysis, due diligence, and strategic decision-making.

## Prerequisites

- An [Enigma account](https://console.enigma.com/register)
- A ChatGPT account that is either:
- An [individual account](https://chatgpt.com/pricing/) on the Pro or Plus plan
- A [Business, Enterprise, and Edu](https://chatgpt.com/pricing/) account with admin, owner, or authorized developer permissions

## Installation

**Individual Account (Pro or Plus plan)**

1. Enable ChatGPT developer mode
- Go to **[Settings → Connectors](https://chatgpt.com/#settings)**
- Scroll down and select **Advanced settings**
- Toggle on **Developer Mode**
2. Go to **[Settings → Connectors](https://chatgpt.com/#settings)**
3. Scroll down and select **Advanced settings**
4. Toggle on **Developer Mode**
5. Add the Enigma connector
- Go to **[Settings → Connectors](https://chatgpt.com/#settings)**
- Select **Create**
- Enter the following information:
- **Name** : Enigma
- **MCP Server URL** : [https://mcp.enigma.com/http](https://mcp.enigma.com/http)
- **Authentication** : OAuth
- Select **Create**
6. Go to **[Settings → Connectors](https://chatgpt.com/#settings)**
7. Select **Create**
8. Enter the following information:
- **Name** : Enigma
- **MCP Server URL** : [https://mcp.enigma.com/http](https://mcp.enigma.com/http)
- **Authentication** : OAuth
9. **Name** : Enigma
10. **MCP Server URL** : [https://mcp.enigma.com/http](https://mcp.enigma.com/http)
11. **Authentication** : OAuth
12. Select **Create**
13. Log in to the Enigma Console and authorize the connector in the new browser window that opens
**Business, Enterprise, and Edu Account (Admin or Authorized Developer)**

1. Enable ChatGPT developer mode
- Go to **Workspace Settings → Permissions & Roles → Connected Data**
- Toggle on **Developer mode / Create custom MCP connectors**
2. Go to **Workspace Settings → Permissions & Roles → Connected Data**
3. Toggle on **Developer mode / Create custom MCP connectors**
4. Add the Enigma connector
- Create a new Connector
- Admins/owners: from Workspace settings, navigate to **Connectors → Connectors → Create** .
- Authorized users: from User settings, navigate to **Apps & Connectors → Create** .
- Configure the connector:
- **Name** : Enigma
- **MCP Server URL** : [https://mcp.enigma.com/http](https://mcp.enigma.com/http)
- **Authentication** : OAuth
- Select **Create**
5. Create a new Connector
- Admins/owners: from Workspace settings, navigate to **Connectors → Connectors → Create** .
- Authorized users: from User settings, navigate to **Apps & Connectors → Create** .
6. Admins/owners: from Workspace settings, navigate to **Connectors → Connectors → Create** .
7. Authorized users: from User settings, navigate to **Apps & Connectors → Create** .
8. Configure the connector:
- **Name** : Enigma
- **MCP Server URL** : [https://mcp.enigma.com/http](https://mcp.enigma.com/http)
- **Authentication** : OAuth
9. **Name** : Enigma
10. **MCP Server URL** : [https://mcp.enigma.com/http](https://mcp.enigma.com/http)
11. **Authentication** : OAuth
12. Select **Create**
13. Log in to the Enigma Console and authorize the connector in the new browser window that opens
14. Go to **Workplace Settings → Connectors** to publish. Review safety warnings (especially for write actions).

## Verify Your Setup

1. Start a new chat and enable the Enigma connector.
- In the bottom left corner of the chat box, select **+ → More → Developer Mode**
- Toggle on the Enigma connector
2. In the bottom left corner of the chat box, select **+ → More → Developer Mode**
3. Toggle on the Enigma connector
4. Ensure that you've selected the a model that supports tool use, such as GPT-5 Thinking.
5. Try an example to verify that the connector is working.
- "Should I invest in fiddlehead bistro in saranac lake NY?""
- "Use only the internal Enigma data to find 2 coffee shops in 10026 with highest revenue as determined by current revenue figures"
6. "Should I invest in fiddlehead bistro in saranac lake NY?""
7. "Use only the internal Enigma data to find 2 coffee shops in 10026 with highest revenue as determined by current revenue figures"

## Troubleshooting

**Connection drops during use?**

- ChatGPT's Developer Mode and MCP connector features are currently in beta. Occasional disconnections may occur
- **Quick fix** : Disable and re-enable the Enigma connector
**Authentication failed?**

- Verify you're logged into [Enigma Console](https://console.enigma.com) in the same browser
- Try the authentication flow again, clear browser cache if needed
**Tools not working as expected?**

- Some business queries require multiple tools working together
- Be specific in your requests (e.g., "Analyze Tacombi's financial performance" vs "Tell me about Tacombi")

## Resources

- [ChatGPT Developer mode](https://platform.openai.com/docs/guides/developer-mode)
- [Developer Mode and full MCP connectors in ChatGPT](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta)