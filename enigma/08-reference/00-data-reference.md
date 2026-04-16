# Enigma Data Reference

> https://documentation.enigma.com/reference/data/

## Overview

Enigma models U.S. businesses as "a graph of interconnected **entities** — brands, locations, legal structures, and people" powered by `graph-model-1`. Each entity contains attributes (observed facts), derived metrics (computed aggregations), and relationships to other entities.

## Primary Entities

### Brand
The customer-facing identity of a business representing "the name and presence under which it engages with customers."

**Schema fields:** name, address (fullAddress, streetAddress1, streetAddress2), website, phone

### Operating Location
A specific place where business occurs under a brand, typically at a physical address.

**Schema fields:** name, address (fullAddress, streetAddress1, streetAddress2), website, phone

### Legal Entity
"An entity which U.S. law recognizes as having an identity and rights, including both natural persons and artificial entities such as businesses."

### Person
A natural person associated with a business as owner, officer, or contact.

## Supporting Entities

These four primary entities connect to supporting entities including: Address, Email Address, Industry, Phone Number, Registered Entity, Registration, Review Summary, Role, Taxpayer Identification Number (TIN), Watchlist Entry, Website, and Website Content.

## Data Types Available

| Type | Description | Example |
|------|-------------|---------|
| **Attributes** | Observed facts about the entity | Brand name, operating status, address |
| **Derived Metrics** | Computed aggregations from source data | 12-month card revenue, YoY growth |
| **On-Demand Attributes** | AI-powered values computed at query time | Custom brand analysis |

Attributes are grouped into categories like "Card Transactions," "Industry," or "Contacts."

## Entity Connections

"Entities are linked by typed relationships — for example, a Brand _operates at_ an Operating Location, or a Legal Entity _owns_ a Brand."

---

## Sub-pages

- [Brand](/reference/data/entities/brand/)
- [Operating Location](/reference/data/entities/operating-location/)
- [Legal Entity](/reference/data/entities/legal-entity/)
- [Person](/reference/data/entities/person/)
- [Supporting Entities](/reference/data/entities/address/)
- [Relationships](/reference/data/relationships/)
