# Rate Limits | DiscoLike API

## Overview

Rate limits are measured in requests per minute and scale by subscription plan:

| Plan | Multiplier |
|------|-----------|
| Starter | 1x |
| Pro | 2x |
| Team | 3x |
| Company | 5x |
| Enterprise | 10x |

## Limits by Endpoint

**2 req/min base:** `/segment`

**5 req/min base:** `/discover`, `/match`, `/append`

**10 req/min base:** `/bizdata`, `/history`, `/score`, `/growth`, `/metrics`, `/vendors`, `/publiclink`, `/subsidiaries`, `/redirects`

For example, `/discover` allows 5 req/min on Starter, 10 on Pro, 15 on Team, 25 on Company, 50 on Enterprise.

---

**Navigation:**
- Previous: [Authentication](/v1/docs/api/access/)
- Next: [Append](/v1/docs/api/endpoints/append/)
