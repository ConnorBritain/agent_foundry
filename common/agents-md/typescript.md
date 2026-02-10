# TypeScript — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Strict Mode | strict: true, noUncheckedIndexedAccess, exactOptionalPropertyTypes |
| Generics | Constraints, defaults, inference, conditional types |
| Utility Types | Partial, Required, Pick, Omit, Record, Extract, Exclude |
| Discriminated Unions | Tagged unions, exhaustive matching, type narrowing |
| Type Guards | typeof, instanceof, in, custom predicates, assertion functions |
| Advanced | Template literals, mapped types, infer, satisfies, const assertions |

## tsconfig.json — Recommended Strict Settings
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true,
    "forceConsistentCasingInFileNames": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "moduleResolution": "bundler",
    "module": "ESNext",
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "skipLibCheck": true,
    "resolveJsonModule": true
  }
}
```

| Flag | Effect |
|---|---|
| strict | Enables all strict checks (strictNullChecks, strictFunctionTypes, etc.) |
| noUncheckedIndexedAccess | array[0] returns T \| undefined, not T |
| exactOptionalPropertyTypes | Distinguishes between missing and undefined properties |
| verbatimModuleSyntax | Forces explicit type imports: import type { X } from 'y' |

## Generics
### Basics & Constraints
```typescript
// Basic generic function
function identity<T>(value: T): T { return value; }

// Constraint: T must have a length property
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

// Multiple type params with constraint relationship
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// Default type parameter
function createArray<T = string>(length: number, value: T): T[] {
  return Array(length).fill(value);
}
```

### Generic Patterns
```typescript
// Generic interface
interface Repository<T extends { id: string }> {
  findById(id: string): Promise<T | null>;
  findMany(filter: Partial<T>): Promise<T[]>;
  create(data: Omit<T, 'id'>): Promise<T>;
  update(id: string, data: Partial<Omit<T, 'id'>>): Promise<T>;
  delete(id: string): Promise<void>;
}

// Generic factory
function createFetcher<TResponse>(url: string) {
  return async (params?: Record<string, string>): Promise<TResponse> => {
    const query = params ? '?' + new URLSearchParams(params) : '';
    const res = await fetch(url + query);
    return res.json();
  };
}
const getUsers = createFetcher<User[]>('/api/users');
```

## Utility Types
| Type | Effect | Example |
|---|---|---|
| Partial<T> | All props optional | Partial<User> → { name?: string; age?: number } |
| Required<T> | All props required | Required<Config> → removes all ? |
| Readonly<T> | All props readonly | Readonly<State> → immutable |
| Pick<T, K> | Subset of props | Pick<User, 'name' \| 'email'> |
| Omit<T, K> | Exclude props | Omit<User, 'password'> |
| Record<K, V> | Key-value map | Record<string, number> |
| Extract<T, U> | Extract matching | Extract<'a' \| 'b' \| 'c', 'a' \| 'c'> → 'a' \| 'c' |
| Exclude<T, U> | Remove matching | Exclude<'a' \| 'b' \| 'c', 'a'> → 'b' \| 'c' |
| NonNullable<T> | Remove null/undef | NonNullable<string \| null> → string |
| ReturnType<T> | Function return type | ReturnType<typeof fn> |
| Parameters<T> | Function param types | Parameters<typeof fn> → [string, number] |
| Awaited<T> | Unwrap Promise | Awaited<Promise<string>> → string |

## Discriminated Unions
```typescript
// Tagged/discriminated union — ALWAYS use a literal type discriminant
type Result<T> =
  | { success: true; data: T }
  | { success: false; error: string };

function handleResult(result: Result<User>) {
  if (result.success) {
    console.log(result.data); // narrowed: { success: true; data: User }
  } else {
    console.error(result.error); // narrowed: { success: false; error: string }
  }
}

// Complex discriminated union
type Action =
  | { type: 'SET_USER'; payload: User }
  | { type: 'SET_ERROR'; payload: string }
  | { type: 'RESET' };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'SET_USER': return { ...state, user: action.payload }; // payload: User
    case 'SET_ERROR': return { ...state, error: action.payload }; // payload: string
    case 'RESET': return initialState;
    default: {
      const _exhaustive: never = action; // compile error if case missed
      return state;
    }
  }
}
```

## Type Guards & Narrowing
```typescript
// typeof narrowing
function process(value: string | number) {
  if (typeof value === 'string') { /* string */ } else { /* number */ }
}

// in operator narrowing
function handle(event: MouseEvent | KeyboardEvent) {
  if ('key' in event) { /* KeyboardEvent */ } else { /* MouseEvent */ }
}

// Custom type guard (type predicate)
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null && 'id' in value && 'email' in value;
}

// Assertion function
function assertNonNull<T>(value: T | null | undefined, msg?: string): asserts value is T {
  if (value == null) throw new Error(msg ?? 'Expected non-null value');
}
```

## satisfies Operator
```typescript
// Validates type without widening — preserves literal types
const palette = {
  red: [255, 0, 0],
  green: '#00ff00',
  blue: [0, 0, 255],
} satisfies Record<string, string | number[]>;

// palette.green is string (not string | number[])
palette.green.toUpperCase(); // OK — type is narrowed

// vs type annotation which widens:
const palette2: Record<string, string | number[]> = { ... };
palette2.green.toUpperCase(); // ERROR — type is string | number[]
```

## const Assertions & as const
```typescript
// as const makes everything readonly and literal
const ROUTES = {
  HOME: '/',
  ABOUT: '/about',
  CONTACT: '/contact',
} as const;
// type: { readonly HOME: '/'; readonly ABOUT: '/about'; readonly CONTACT: '/contact' }

type Route = typeof ROUTES[keyof typeof ROUTES]; // '/' | '/about' | '/contact'

// Const type parameter (TS 5.0+)
function createRoute<const T extends string>(path: T): { path: T } {
  return { path };
}
const route = createRoute('/api/users'); // type: { path: '/api/users' } not { path: string }
```

## Mapped Types
```typescript
// Basic mapped type
type Optional<T> = { [K in keyof T]?: T[K] };

// With remapping (as clause)
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
// { getName: () => string; getAge: () => number }

// Conditional mapped type
type ReadonlyExceptId<T> = {
  [K in keyof T]: K extends 'id' ? T[K] : Readonly<T[K]>;
};
```

## Template Literal Types
```typescript
type EventName = `on${Capitalize<'click' | 'focus' | 'blur'>}`;
// 'onClick' | 'onFocus' | 'onBlur'

type HTTPMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
type APIRoute = `/api/${string}`;
type Endpoint = `${HTTPMethod} ${APIRoute}`;
// 'GET /api/...' | 'POST /api/...' | etc.

// Infer from template literal
type ExtractParam<T extends string> = T extends `${string}:${infer Param}/${infer Rest}`
  ? Param | ExtractParam<Rest>
  : T extends `${string}:${infer Param}`
  ? Param
  : never;

type Params = ExtractParam<'/users/:id/posts/:postId'>; // 'id' | 'postId'
```

## Conditional Types & infer
```typescript
// Basic conditional
type IsString<T> = T extends string ? true : false;

// infer keyword — extract types within conditional
type ArrayElement<T> = T extends (infer E)[] ? E : never;
type UnpackPromise<T> = T extends Promise<infer R> ? UnpackPromise<R> : T;

// Function return type extraction
type GetReturn<T> = T extends (...args: any[]) => infer R ? R : never;

// Distributive conditional types
type ToArray<T> = T extends any ? T[] : never;
type Result = ToArray<string | number>; // string[] | number[] (distributed)
type NoDistribute<T> = [T] extends [any] ? T[] : never;
type Result2 = NoDistribute<string | number>; // (string | number)[] (not distributed)
```

## Common Patterns
| Pattern | Implementation |
|---|---|
| Branded types | type USD = number & { __brand: 'USD' } |
| Builder pattern | Method chaining with generics accumulating type info |
| Zod inference | type User = z.infer<typeof userSchema> |
| Event map | interface Events { click: MouseEvent; key: KeyboardEvent } |
| Safe indexing | Map<string, T>.get() returns T \| undefined |
| Exhaustive switch | default: never check ensures all cases handled |
| Type-safe env | declare namespace NodeJS { interface ProcessEnv { DB_URL: string } } |

## Performance Tips
```
1. Prefer interfaces over type aliases for object types (faster incremental compilation)
2. Avoid deep recursive conditional types (TS depth limit: ~50)
3. Use project references for monorepo (tsconfig composite + references)
4. skipLibCheck: true to skip .d.ts checking (faster builds)
5. isolatedModules: true required for SWC/esbuild transpilation
6. Use type-only imports: import type { X } to reduce bundle size
```
