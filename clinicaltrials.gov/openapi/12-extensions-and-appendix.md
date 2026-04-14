# OpenAPI 3.0.3 -- Specification Extensions, Revision History, and References

Source: https://spec.openapis.org/oas/v3.0.3 (20 February 2020)

---

## Section 4.8: Specification Extensions

While the OpenAPI Specification tries to accommodate most use cases, additional data can be added to extend the specification at certain points.

The extensions properties are implemented as patterned fields that are always prefixed by `x-`.

### Patterned Field

| Field Pattern | Type | Description |
|---------------|------|-------------|
| `^x-` | Any | Allows extensions to the OpenAPI Schema. The field name MUST begin with `x-`, for example, `x-internal-id`. The value can be `null`, a primitive, an array or an object. Can have any valid JSON format value. |

### Tooling Considerations

The extensions may or may not be supported by the available tooling, but those may be extended as well to add requested support (if tools are internal or open-sourced).

### Objects That Support Specification Extensions

The following objects in the specification each include the statement "This object MAY be extended with Specification Extensions":

1. **OpenAPI Object** (Section 4.7.1)
2. **Info Object** (Section 4.7.2)
3. **Contact Object** (Section 4.7.3)
4. **License Object** (Section 4.7.4)
5. **Server Object** (Section 4.7.5)
6. **Server Variable Object** (Section 4.7.6)
7. **Components Object** (Section 4.7.7)
8. **Paths Object** (Section 4.7.8)
9. **Path Item Object** (Section 4.7.9)
10. **Operation Object** (Section 4.7.10)
11. **External Documentation Object** (Section 4.7.11)
12. **Parameter Object** (Section 4.7.12)
13. **Request Body Object** (Section 4.7.13)
14. **Media Type Object** (Section 4.7.14)
15. **Encoding Object** (Section 4.7.15)
16. **Responses Object** (Section 4.7.16)
17. **Response Object** (Section 4.7.17)
18. **Callback Object** (Section 4.7.18)
19. **Example Object** (Section 4.7.19)
20. **Link Object** (Section 4.7.20)
21. **Tag Object** (Section 4.7.22)
22. **Schema Object** (Section 4.7.24)
23. **XML Object** (Section 4.7.26)
24. **Security Scheme Object** (Section 4.7.27)
25. **OAuth Flows Object** (Section 4.7.28)
26. **OAuth Flow Object** (Section 4.7.29)

Objects that do NOT explicitly declare extension support:

- **Header Object** (Section 4.7.21) -- follows the structure of the Parameter Object (which does support extensions), but does not independently declare "This object MAY be extended with Specification Extensions"
- **Reference Object** (Section 4.7.23)
- **Discriminator Object** (Section 4.7.25)
- **Security Requirement Object** (Section 4.7.30)

---

## Section 4.9: Security Filtering

Some objects in the OpenAPI Specification MAY be declared and remain empty, or be completely removed, even though they are inherently the core of the API documentation.

The reasoning is to allow an additional layer of access control over the documentation. While not part of the specification itself, certain libraries MAY choose to allow access to parts of the documentation based on some form of authentication/authorization.

Two examples:

1. **The Paths Object MAY be empty.** It may be counterintuitive, but this may tell the viewer that they got to the right place, but can't access any documentation. They'd still have access to the Info Object which may contain additional information regarding authentication.

2. **The Path Item Object MAY be empty.** In this case, the viewer will be aware that the path exists, but will not be able to see any of its operations or parameters. This is different from hiding the path itself from the Paths Object, because the user will be aware of its existence. This allows the documentation provider to finely control what the viewer can see.

---

## Appendix A: Revision History

| Version | Date | Notes |
|---------|------|-------|
| 3.0.3 | 2020-02-20 | Patch release of the OpenAPI Specification 3.0.3 |
| 3.0.2 | 2018-10-08 | Patch release of the OpenAPI Specification 3.0.2 |
| 3.0.1 | 2017-12-06 | Patch release of the OpenAPI Specification 3.0.1 |
| 3.0.0 | 2017-07-26 | Release of the OpenAPI Specification 3.0.0 |
| 3.0.0-rc2 | 2017-06-16 | rc2 of the 3.0 specification |
| 3.0.0-rc1 | 2017-04-27 | rc1 of the 3.0 specification |
| 3.0.0-rc0 | 2017-02-28 | Implementer's Draft of the 3.0 specification |
| 2.0 | 2015-12-31 | Donation of Swagger 2.0 to the OpenAPI Initiative |
| 2.0 | 2014-09-08 | Release of Swagger 2.0 |
| 1.2 | 2014-03-14 | Initial release of the formal document. |
| 1.1 | 2012-08-22 | Release of Swagger 1.1 |
| 1.0 | 2011-08-10 | First release of the Swagger Specification |

---

## Section B: References

### B.1 Normative References

**[ABNF]**
Augmented BNF for Syntax Specifications: ABNF. D. Crocker, Ed.; P. Overell. IETF. January 2008. Internet Standard.
URL: https://www.rfc-editor.org/rfc/rfc5234

**[CommonMark]**
CommonMark Spec.
URL: https://spec.commonmark.org/

**[CommonMark-0.27]**
CommonMark Spec, Version 0.27. John MacFarlane. 18 November 2016.
URL: https://spec.commonmark.org/0.27/

**[IANA-HTTP-AUTHSCHEMES]**
Hypertext Transfer Protocol (HTTP) Authentication Scheme Registry. IANA.
URL: https://www.iana.org/assignments/http-authschemes/

**[IANA-HTTP-STATUS-CODES]**
Hypertext Transfer Protocol (HTTP) Status Code Registry. IANA.
URL: https://www.iana.org/assignments/http-status-codes/

**[JSON-Reference]**
JSON Reference. Paul Bryan; Kris Zyp. Internet Engineering Task Force (IETF). 16 September 2012. Internet-Draft.
URL: https://datatracker.ietf.org/doc/html/draft-pbryan-zyp-json-ref-03

**[JSON-Schema-05]**
JSON Schema: A Media Type for Describing JSON Documents. Draft 5. Austin Wright. Internet Engineering Task Force (IETF). 13 October 2016. Internet-Draft.
URL: https://datatracker.ietf.org/doc/html/draft-wright-json-schema-00

**[JSON-Schema-Validation-05]**
JSON Schema Validation: A Vocabulary for Structural Validation of JSON. Draft 5. Austin Wright; G. Luff. Internet Engineering Task Force (IETF). 13 October 2016. Internet-Draft.
URL: https://datatracker.ietf.org/doc/html/draft-wright-json-schema-validation-00

**[RFC1866]**
Hypertext Markup Language - 2.0. T. Berners-Lee; D. Connolly. IETF. November 1995. Historic.
URL: https://www.rfc-editor.org/rfc/rfc1866

**[RFC2119]**
Key words for use in RFCs to Indicate Requirement Levels. S. Bradner. IETF. March 1997. Best Current Practice.
URL: https://www.rfc-editor.org/rfc/rfc2119

**[RFC3339]**
Date and Time on the Internet: Timestamps. G. Klyne; C. Newman. IETF. July 2002. Proposed Standard.
URL: https://www.rfc-editor.org/rfc/rfc3339

**[RFC3986]**
Uniform Resource Identifier (URI): Generic Syntax. T. Berners-Lee; R. Fielding; L. Masinter. IETF. January 2005. Internet Standard.
URL: https://www.rfc-editor.org/rfc/rfc3986

**[RFC6570]**
URI Template. J. Gregorio; R. Fielding; M. Hadley; M. Nottingham; D. Orchard. IETF. March 2012. Proposed Standard.
URL: https://www.rfc-editor.org/rfc/rfc6570

**[RFC6749]**
The OAuth 2.0 Authorization Framework. D. Hardt, Ed. IETF. October 2012. Proposed Standard.
URL: https://www.rfc-editor.org/rfc/rfc6749

**[RFC6838]**
Media Type Specifications and Registration Procedures. N. Freed; J. Klensin; T. Hansen. IETF. January 2013. Best Current Practice.
URL: https://www.rfc-editor.org/rfc/rfc6838

**[RFC6901]**
JavaScript Object Notation (JSON) Pointer. P. Bryan, Ed.; K. Zyp; M. Nottingham, Ed. IETF. April 2013. Proposed Standard.
URL: https://www.rfc-editor.org/rfc/rfc6901

**[RFC7159]**
The JavaScript Object Notation (JSON) Data Interchange Format. T. Bray, Ed. IETF. March 2014. Proposed Standard.
URL: https://www.rfc-editor.org/rfc/rfc7159

**[RFC7230]**
Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing. R. Fielding, Ed.; J. Reschke, Ed. IETF. June 2014. Proposed Standard.
URL: https://httpwg.org/specs/rfc7230.html

**[RFC7231]**
Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. R. Fielding, Ed.; J. Reschke, Ed. IETF. June 2014. Proposed Standard.
URL: https://httpwg.org/specs/rfc7231.html

**[RFC7235]**
Hypertext Transfer Protocol (HTTP/1.1): Authentication. R. Fielding, Ed.; J. Reschke, Ed. IETF. June 2014. Proposed Standard.
URL: https://httpwg.org/specs/rfc7235.html

**[RFC8174]**
Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words. B. Leiba. IETF. May 2017. Best Current Practice.
URL: https://www.rfc-editor.org/rfc/rfc8174

**[YAML]**
YAML Ain't Markup Language (YAML) Version 1.2. Oren Ben-Kiki; Clark Evans; Ingy dot Net. 1 October 2009.
URL: http://yaml.org/spec/1.2/spec.html
