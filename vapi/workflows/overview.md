# Workflows Overview Documentation

## Page Summary

This documentation page introduces Vapi's Workflows feature—a visual builder for creating conversation flows—while noting that the platform now recommends **Assistants** or **Squads** for new projects.

## Key Content Points

**Deprecation Notice**: The page includes a prominent warning stating that the product team has "found that current AI systems aren't yet capable of acting as truly autonomous agents" that can maintain context awareness across workflow nodes. The Squads pattern is presented as the preferred alternative.

**Core Capabilities**: Workflows enable developers to design conversation flows using nodes and edges, supporting:
- Visual prototyping of multi-turn conversations
- Complex branching logic for call centers and support scenarios
- Multilingual conversation paths
- AI-based and logical conditions for routing decisions

**Node Types**: The documentation describes six node varieties:
1. **Conversation Node** (default) – main building block with configurable prompts, models, and variable extraction
2. **API Request Node** – HTTP calls to external services
3. **Transfer Call Node** – routing to human agents or phone numbers
4. **End Call Node** – conversation termination
5. **Tool Node** – integration with pre-built tools
6. **Global Node** – accessible from anywhere for escalation

**Conditions**: Edges between nodes support plain-language AI conditions, variable-based logical conditions, or combined expressions using operators.

**Best Practices**: The guide emphasizes planning workflows beforehand, using focused prompts, testing all paths, and monitoring performance over time.
