# Advanced Eval Testing - Complete Documentation

## Overview

This comprehensive guide covers evaluation strategies for production AI agents, including testing approaches, performance optimization, maintenance techniques, and troubleshooting methods.

## Testing Strategies

### Smoke Tests

Quick validation checks that confirm basic functionality. These should run first to catch obvious issues before expensive test suites execute.

**Key characteristics:**
- Minimal validation (any response acceptable)
- Fast execution (1-2 conversation turns)
- Run before detailed test suites
- Exit early if validation fails

**When to use:** After configuration changes, during development, or as health checks in monitoring systems.

### Regression Tests

Ensure that bug fixes remain stable and features continue functioning after updates.

**Best practices:**
- Name tests after the bugs they prevent
- Include ticket/issue numbers in descriptions
- Add regression tests when fixing bugs
- Run full regression suite before major releases
- Archive tests only when features are removed

### Edge Case Testing

Test boundary conditions and unusual inputs systematically.

**Common edge cases:**
- Empty or minimal input
- Very long input (character limits)
- Special characters and unicode
- Ambiguous or unclear requests
- Rapid conversation changes

**Categories to test:**
- Input boundaries
- Data format validation
- Conversation patterns
- Timing scenarios

## Testing Patterns

### Happy Path Testing

Validates ideal user journeys where everything proceeds correctly.

**Structure:**
1. User provides clear, complete information
2. Assistant responds appropriately
3. Tools execute successfully
4. Conversation completes with desired outcome

### Error Handling Testing

Tests how the assistant manages failures gracefully, including:
- Tool/API failures
- Invalid user input
- Timeout scenarios
- Rate limit errors
- Permission/authorization issues

### Boundary Testing

Tests system limits and thresholds, such as:
- Maximum conversation length
- Rate limits under stress
- Data size boundaries
- Resource constraints

## Validation Approach Selection

**Exact Match:** Use for critical business data, tool call validation, compliance-required wording, or status messages.

**Regex:** Use for responses with variable data, pattern matching, flexible phrasing with keywords, or multiple acceptable outputs.

**AI Judge:** Use for semantic meaning, tone evaluation, contextual appropriateness, complex criteria, or helpfulness assessment.

## Best Practices

### Evaluation Design Principles

- **Single responsibility:** Each evaluation tests one specific behavior
- **Clear naming:** Use descriptive names explaining what's tested
- **Comprehensive descriptions:** Document why tests exist and what they validate
- **Maintainable complexity:** Keep evaluations focused (5-10 turns maximum)

### Performance Optimization

1. Use exit-on-failure for early critical steps
2. Run critical tests first
3. Keep conversations focused and concise
4. Batch related tests together
5. Optimize AI judge prompts for speed and cost

**Performance comparison:**
| Judge Type | Speed | Cost | Use Case |
|---|---|---|---|
| Exact | Fast | Low | Critical exact matches |
| Regex | Fast | Low | Pattern matching |
| AI (GPT-3.5) | Medium | Medium | Simple semantic checks |
| AI (GPT-4) | Slower | Higher | Complex evaluation |

### Maintenance Strategies

**Version control evaluations** alongside your codebase in organized directories.

**Regular review cycle:**
- Weekly: Review failed tests
- Monthly: Audit test coverage
- Quarterly: Refactor and optimize

**Update tests when:**
- Assistant prompts or behavior change intentionally
- New features are added
- Bugs are fixed
- User feedback reveals edge cases
- Business requirements evolve

### CI/CD Integration

Automate evaluation runs in deployment pipelines to validate changes before production release.

**Advanced patterns include:**
- Staging environment validation
- Parallel test execution
- Quality gates with pass rate thresholds
- Scheduled regression runs

## Advanced Troubleshooting

### Debugging Failed Evaluations

**Step-by-step process:**
1. Examine the specific failure reason provided
2. Review complete conversation transcript
3. Compare expected versus actual behavior
4. Test validation logic separately
5. Reproduce the issue manually

### Common Failure Patterns

- **Exact match failures:** Switch to regex or AI judge for flexibility
- **Tool call mismatches:** Check argument types and field presence
- **AI judge inconsistency:** Make criteria more specific and explicit
- **Test timeouts:** Check assistant configuration and tool accessibility
- **Regex pattern failures:** Verify escaped special characters

### Debugging Tools

- Use structured logging to track executions systematically
- Isolate variables when tests fail inconsistently
- Build complexity gradually with progressive validation
- Run evaluations multiple times to detect inconsistent behavior

## Status and Error Codes

| Status | Reason | Meaning | Action |
|---|---|---|---|
| ended | mockConversation.done | Test completed normally | Check results for pass/fail |
| ended | assistant-error | Assistant configuration error | Fix setup and re-run |
| ended | pipeline-error-* | Provider API error | Check provider status |
| running | - | Test in progress | Wait or check timeout |
| queued | - | Test waiting to start | Should start soon |

## Next Steps

- Return to quickstart guide for basic evaluation setup
- Learn assistant building and configuration
- Build custom tools and test behavior
- Review complete API documentation for evaluations

---

**Summary:** This guide provides comprehensive strategies for building robust test suites through strategic smoke tests, regression validation, and edge case coverage. Success requires choosing appropriate validation methods, optimizing performance through early exits and parallel execution, and maintaining test quality through regular reviews and CI/CD automation.
