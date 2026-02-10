---
skill_name: "testing"
version: "1.0.0"
description: "Writes and manages tests across unit, integration, and e2e levels with coverage targets"
author: "Agent Foundry"
triggers:
  - "when asked to write tests for code"
  - "when asked to improve test coverage"
  - "when asked to set up a testing framework"
  - "when a new feature is built and needs test coverage"
  - "when asked to debug or fix failing tests"
---

# Testing Skill

## Purpose
Write effective tests that verify correctness, prevent regressions, and serve as living documentation. Balance thoroughness with maintainability across the test pyramid.

## Test Writing Workflow

### Step 1: Analyze What to Test
Before writing tests, determine:
- What is the function/component's public API?
- What are the inputs, outputs, and side effects?
- What are the edge cases and error conditions?
- What is the appropriate test level (unit, integration, e2e)?

### Step 2: Select Test Level

| Level | What to Test | Tool |
|---|---|---|
| Unit | Pure functions, utilities, transformations, hooks | Vitest |
| Component | React components, user interactions, rendering | Vitest + Testing Library |
| Integration | API routes, database queries, service layers | Vitest + MSW/supertest |
| E2E | Critical user flows, cross-page journeys | Playwright |

### Decision Matrix
```
Is it a pure function with no dependencies? → Unit test
Is it a React component with user interaction? → Component test
Does it call external services or databases? → Integration test
Is it a critical user journey across pages? → E2E test
Does it involve browser-specific behavior? → E2E test
```

### Step 3: Write Tests Using AAA Pattern
```
Arrange — Set up test data, mocks, and preconditions
Act     — Execute the code under test
Assert  — Verify the expected outcome
```

### Step 4: Cover Edge Cases
For every function/component, test:
- Happy path (normal expected input)
- Empty/null input
- Boundary values (min, max, zero, one)
- Error conditions (invalid input, network failure)
- Concurrent/async behavior (race conditions, timeouts)

## Test Templates

### Unit Test Template
```typescript
import { describe, it, expect } from 'vitest';
import { functionUnderTest } from '@/lib/module';

describe('functionUnderTest', () => {
  // Happy path
  it('returns expected output for valid input', () => {
    const result = functionUnderTest(validInput);
    expect(result).toEqual(expectedOutput);
  });

  // Edge cases
  it('handles empty input', () => {
    expect(functionUnderTest([])).toEqual([]);
  });

  it('handles null values', () => {
    expect(functionUnderTest(null)).toBeNull();
  });

  // Error cases
  it('throws on invalid input', () => {
    expect(() => functionUnderTest(invalidInput)).toThrow('Expected error message');
  });

  // Boundary values
  it('handles maximum allowed value', () => {
    const result = functionUnderTest(MAX_VALUE);
    expect(result).toBeDefined();
  });
});
```

### Component Test Template
```typescript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { Component } from '@/components/Component';

describe('Component', () => {
  it('renders with required props', () => {
    render(<Component title="Test" />);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });

  it('handles user interaction', async () => {
    const onAction = vi.fn();
    const user = userEvent.setup();
    render(<Component onAction={onAction} />);

    await user.click(screen.getByRole('button', { name: /submit/i }));
    expect(onAction).toHaveBeenCalledOnce();
  });

  it('displays loading state', () => {
    render(<Component loading={true} />);
    expect(screen.getByRole('progressbar')).toBeInTheDocument();
  });

  it('displays error state', () => {
    render(<Component error="Something went wrong" />);
    expect(screen.getByText('Something went wrong')).toBeInTheDocument();
  });
});
```

### API Route Test Template
```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { POST } from '@/app/api/resource/route';

describe('POST /api/resource', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('creates resource and returns 201', async () => {
    const request = new Request('http://localhost/api/resource', {
      method: 'POST',
      body: JSON.stringify({ name: 'Test' }),
      headers: { 'Content-Type': 'application/json' },
    });

    const response = await POST(request);
    const data = await response.json();

    expect(response.status).toBe(201);
    expect(data).toHaveProperty('id');
    expect(data.name).toBe('Test');
  });

  it('returns 400 for invalid body', async () => {
    const request = new Request('http://localhost/api/resource', {
      method: 'POST',
      body: JSON.stringify({}), // missing required fields
      headers: { 'Content-Type': 'application/json' },
    });

    const response = await POST(request);
    expect(response.status).toBe(400);
  });

  it('returns 401 for unauthenticated request', async () => {
    // no auth header
    const request = new Request('http://localhost/api/resource', {
      method: 'POST',
      body: JSON.stringify({ name: 'Test' }),
    });

    const response = await POST(request);
    expect(response.status).toBe(401);
  });
});
```

## Coverage Targets

### By Project Phase
| Phase | Line Coverage | Branch Coverage |
|---|---|---|
| MVP / Prototype | 60%+ | 50%+ |
| Production v1 | 80%+ | 75%+ |
| Mature product | 85%+ | 80%+ |
| Critical paths (auth, payments) | 95%+ | 90%+ |

### What to Cover vs Skip
| Always Cover | Skip Coverage |
|---|---|
| Business logic | Config files |
| Validation functions | Type declarations (.d.ts) |
| API route handlers | Generated code |
| Auth/authorization | Third-party wrapper pass-throughs |
| Data transformations | Simple getters/setters |
| Custom hooks | Static constants |
| Error handling paths | Framework boilerplate |

## Mocking Strategy

### When to Mock
| Mock | Don't Mock |
|---|---|
| External HTTP APIs (use MSW) | The code under test |
| Database calls (in unit tests) | Pure utility functions |
| Time/dates (vi.useFakeTimers) | Simple data transformations |
| File system operations | Standard library functions |
| Third-party SDKs | Internal modules (use real ones) |

### Mock Hierarchy (prefer top of list)
1. **Dependency injection** — pass dependencies as parameters
2. **MSW** — intercept network at service worker level
3. **Module mocks** — vi.mock() for module-level replacement
4. **Spies** — vi.spyOn() for observation without replacement

## Test Naming Conventions
```
describe('ModuleName or FunctionName', () => {
  describe('methodName or scenario', () => {
    it('expected behavior when condition', () => {
      // Pattern: "it [does something] when [condition]"
    });
  });
});

// Good names:
it('returns null when user is not found')
it('throws ValidationError when email is invalid')
it('redirects to login when session expires')
it('renders empty state when list has no items')

// Bad names:
it('works')
it('test 1')
it('should handle the case')
```

## Test Maintenance Rules
| Rule | Rationale |
|---|---|
| Test behavior, not implementation | Tests survive refactoring |
| No test interdependence | Each test is isolated and repeatable |
| Remove flaky tests immediately | Fix or delete — flaky tests erode trust |
| Keep test files near source | `component.tsx` → `component.test.tsx` |
| Use factories over fixtures | Dynamic data prevents hidden coupling |
| One concept per test | Clear failure messages |
| Avoid logic in tests | No if/else/loops in test code |

## Running Tests
```bash
# Unit + component tests
pnpm vitest                      # Watch mode
pnpm vitest run                  # Single run
pnpm vitest run --coverage       # With coverage report

# E2E tests
pnpm playwright test             # Run all e2e
pnpm playwright test --ui        # Interactive UI mode
pnpm playwright test --debug     # Debug mode with inspector

# CI pipeline
pnpm vitest run --coverage --reporter=json
pnpm playwright test --reporter=html
```
