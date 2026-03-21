# Taxpayer Identification Number (TIN)

## Description
A Taxpayer Identification Number (TIN) is a unique identification number for a business that is used by the Internal Revenue Service (IRS). TIN verification is a critical component of Know Your Business (KYB) regulations, validating that a business's tax identification number matches IRS records.

## Tier
Premium

## Applies To
- Legal Entity

## TIN Types

The IRS recognizes five categories:
- **Employer Identification Number (EIN)** - Primary focus
- Social Security Number (SSN)
- Individual Taxpayer Identification Number (ITIN)
- Taxpayer Identification Number for Pending U.S. Adoptions (ATIN)
- Preparer Taxpayer Identification Number (PTIN)

## Focus
Enigma primarily handles entities with EINs. Federal Government mandates EINs for all legal entities with employees. EINs are permanent and never reissued.

## Verification Process
- EIN must be submitted as a 9-digit string
- Business names exceeding 40 characters are truncated for IRS submission

## Possible Response Outcomes

| Status | Result | Meaning |
|--------|--------|---------|
| Success | TIN_verified | TIN and name match IRS records |
| Failure | Error | Invalid TIN format |
| Failure | Not_completed | IRS temporarily unavailable or duplicate request pending |
| Failure | TIN_not_verified | Data doesn't match IRS records or number not currently issued |

## Failure Recovery
- Verify EIN directly with business
- IRS can be down for minutes to several hours
- Alternative: request business documentation

## Access Requirements
Optional add-on requiring sales team activation. Implementation involves passing `tin_verification` in the `attrs` parameter with a 9-digit string in the `tin` field via the KYB endpoint.

## Data Source
Internal Revenue Service (IRS)

## Sources
- https://documentation.enigma.com/v1/reference/attributes/kyb-and-identity-attributes/tax-identification-number-tin
- https://developers.enigma.com/docs/tax-identification-number-tin
