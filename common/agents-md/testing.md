# Testing — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Unit Tests | Isolated functions, pure logic, fast, no dependencies |
| Integration | Multiple modules together, API routes, DB queries |
| E2E | Full user flows, browser automation, real environment |
| Mocking | Stubs, spies, fakes, dependency injection |
| Fixtures | Test data factories, seeding, cleanup |
| Coverage | Line, branch, function, statement — targets and reporting |

## Testing Pyramid & Strategy
```
        /  E2E  \        Few: critical user journeys (5-10%)
       /----------\
      / Integration \    Some: API routes, DB, services (20-30%)
     /----------------\
    /    Unit Tests     \  Many: pure functions, utils, hooks (60-70%)
```

| Test Type | Speed | Scope | Tools |
|---|---|---|---|
| Unit | <10ms | Single function/module | Vitest, Jest |
| Integration | <500ms | Multiple modules, API | Vitest + supertest, MSW |
| E2E | 2-30s | Full browser flow | Playwright, Cypress |
| Component | <200ms | Rendered component | Testing Library + Vitest |

## Vitest Setup (Recommended)
```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom', // or 'node' for API tests
    globals: true,
    setupFiles: ['./tests/setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'tests/', '**/*.d.ts', '**/*.config.*'],
      thresholds: { branches: 80, functions: 80, lines: 80, statements: 80 },
    },
    include: ['**/*.{test,spec}.{ts,tsx}'],
  },
  resolve: { alias: { '@': '/src' } },
});
```

### Setup File
```typescript
// tests/setup.ts
import '@testing-library/jest-dom/vitest';
import { cleanup } from '@testing-library/react';
import { afterEach, vi } from 'vitest';

afterEach(() => { cleanup(); });

// Global mocks
vi.mock('next/navigation', () => ({
  useRouter: () => ({ push: vi.fn(), replace: vi.fn(), back: vi.fn() }),
  useSearchParams: () => new URLSearchParams(),
  usePathname: () => '/',
}));
```

## Unit Testing Patterns
### Pure Function Testing
```typescript
import { describe, it, expect } from 'vitest';

describe('calculateTotal', () => {
  it('sums line items with tax', () => {
    const items = [{ price: 100, qty: 2 }, { price: 50, qty: 1 }];
    expect(calculateTotal(items, 0.1)).toBe(275); // (200+50)*1.1
  });

  it('returns 0 for empty cart', () => {
    expect(calculateTotal([], 0.1)).toBe(0);
  });

  it('throws on negative prices', () => {
    expect(() => calculateTotal([{ price: -1, qty: 1 }], 0)).toThrow('Invalid price');
  });
});
```

### Test Organization — AAA Pattern
```typescript
it('creates a user with hashed password', async () => {
  // Arrange
  const input = { email: 'test@example.com', password: 'secure123' };

  // Act
  const user = await createUser(input);

  // Assert
  expect(user.email).toBe('test@example.com');
  expect(user.password).not.toBe('secure123'); // hashed
  expect(user.id).toBeDefined();
});
```

## Component Testing (React Testing Library)
```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

describe('LoginForm', () => {
  it('submits with email and password', async () => {
    const onSubmit = vi.fn();
    const user = userEvent.setup();

    render(<LoginForm onSubmit={onSubmit} />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123',
      });
    });
  });

  it('shows validation error for invalid email', async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={vi.fn()} />);

    await user.type(screen.getByLabelText(/email/i), 'invalid');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    expect(screen.getByText(/valid email/i)).toBeInTheDocument();
  });
});
```

### Query Priority (Testing Library)
| Priority | Queries | Use When |
|---|---|---|
| 1 (best) | getByRole, getByLabelText | Accessible elements |
| 2 | getByPlaceholderText, getByText | Visible text |
| 3 | getByDisplayValue, getByAltText | Form values, images |
| 4 (last) | getByTestId | No semantic query possible |

## Mocking
### Function Mocking
```typescript
import { vi, describe, it, expect } from 'vitest';

// Mock a module
vi.mock('@/lib/db', () => ({
  db: { user: { findUnique: vi.fn(), create: vi.fn() } },
}));

// Spy on existing function
const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

// Mock implementation
const mockFetch = vi.fn().mockResolvedValue({ ok: true, json: () => ({ data: [] }) });

// Mock return values per test
it('handles not found', async () => {
  vi.mocked(db.user.findUnique).mockResolvedValueOnce(null);
  const result = await getUser('nonexistent');
  expect(result).toBeNull();
});
```

### MSW (Mock Service Worker) — API Mocking
```typescript
import { setupServer } from 'msw/node';
import { http, HttpResponse } from 'msw';

const server = setupServer(
  http.get('/api/users', () => HttpResponse.json([{ id: '1', name: 'Test' }])),
  http.post('/api/users', async ({ request }) => {
    const body = await request.json();
    return HttpResponse.json({ id: '2', ...body }, { status: 201 });
  }),
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

it('handles server error', async () => {
  server.use(http.get('/api/users', () => HttpResponse.json(null, { status: 500 })));
  // test error handling
});
```

## E2E Testing (Playwright)
```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  use: { baseURL: 'http://localhost:3000', trace: 'on-first-retry' },
  webServer: { command: 'npm run dev', port: 3000, reuseExistingServer: !process.env.CI },
});
```

### E2E Test Pattern
```typescript
import { test, expect } from '@playwright/test';

test.describe('checkout flow', () => {
  test('completes purchase', async ({ page }) => {
    await page.goto('/products');
    await page.getByRole('button', { name: 'Add to cart' }).first().click();
    await page.getByRole('link', { name: 'Cart' }).click();
    await expect(page.getByText('1 item')).toBeVisible();
    await page.getByRole('button', { name: 'Checkout' }).click();
    await page.getByLabel('Email').fill('test@example.com');
    await page.getByRole('button', { name: 'Pay' }).click();
    await expect(page).toHaveURL(/\/confirmation/);
    await expect(page.getByText('Order confirmed')).toBeVisible();
  });
});
```

## Fixtures & Factories
```typescript
// tests/factories.ts
import { faker } from '@faker-js/faker';

export function buildUser(overrides?: Partial<User>): User {
  return {
    id: faker.string.uuid(),
    email: faker.internet.email(),
    name: faker.person.fullName(),
    createdAt: faker.date.recent(),
    ...overrides,
  };
}

export function buildPost(overrides?: Partial<Post>): Post {
  return {
    id: faker.string.uuid(),
    title: faker.lorem.sentence(),
    content: faker.lorem.paragraphs(3),
    authorId: faker.string.uuid(),
    published: true,
    ...overrides,
  };
}
```

## Coverage
```
Run: vitest run --coverage
Reports: text (terminal), html (detailed), json (CI), lcov (tools)
```

| Metric | Target | Meaning |
|---|---|---|
| Statements | 80%+ | Individual statements executed |
| Branches | 80%+ | if/else/switch paths taken |
| Functions | 80%+ | Functions called |
| Lines | 80%+ | Source lines executed |

### What to Cover vs Skip
```
COVER: Business logic, utilities, data transforms, hooks, API handlers, validation
SKIP: Config files, type declarations, third-party wrappers, generated code
Focus on: Branch coverage — tests that exercise edge cases and error paths
```

## Best Practices
| Practice | Rationale |
|---|---|
| Test behavior, not implementation | Refactoring shouldn't break tests |
| One assertion per concept | Clear failure messages |
| Descriptive test names | it('returns null when user not found') |
| Avoid test interdependence | Each test sets up its own state |
| Use factories, not fixtures | Generate unique data per test |
| Mock at boundaries | HTTP, DB, file system — not internal modules |
| Prefer userEvent over fireEvent | Simulates real user behavior |
| Test error paths | Happy path + edge cases + errors |
| Run in CI | Every PR must pass all tests |
| Snapshot sparingly | Only for stable, small outputs |
