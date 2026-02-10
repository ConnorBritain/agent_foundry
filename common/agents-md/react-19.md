# React 19 — Compressed AGENTS.md Knowledge

## Quick Reference
| Feature | Status | Key Change |
|---|---|---|
| Server Components | Stable | Default in App Router, async components, zero client JS |
| Server Actions | Stable | "use server" functions, form handling, mutations |
| use() hook | New | Unwrap promises/context in render, replaces some useEffect |
| useActionState | New | Form action state management, replaces useFormState |
| useOptimistic | New | Optimistic UI updates during async actions |
| useFormStatus | Stable | Pending state for form submissions |
| ref as prop | New | No more forwardRef needed — ref is a regular prop |
| Document metadata | New | <title>, <meta>, <link> in components hoist to <head> |
| Stylesheet support | New | Precedence-based CSS loading |
| Preloading APIs | New | preload(), preinit(), prefetchDNS(), preconnect() |

## Server Components (RSC)
```
DEFAULT in Next.js App Router — no directive needed
Run on server only → no useState, useEffect, event handlers
Can: await data, access DB, read fs, use secrets
Cannot: use hooks (except use()), attach event listeners, access browser APIs
```

| Pattern | Server Component | Client Component |
|---|---|---|
| Directive | none (default) | "use client" at top of file |
| Data fetching | async/await directly | useEffect + fetch or library |
| State | none | useState, useReducer |
| Interactivity | none | onClick, onChange, etc. |
| Rendering | server only | server pre-render + client hydration |

### Composition Pattern
```tsx
// Server Component (default) — fetches data
async function UserProfile({ userId }: { userId: string }) {
  const user = await db.user.findUnique({ where: { id: userId } });
  return (
    <div>
      <h1>{user.name}</h1>
      <EditButton user={user} /> {/* Client Component */}
    </div>
  );
}

// Client Component — handles interactivity
"use client";
function EditButton({ user }: { user: User }) {
  const [editing, setEditing] = useState(false);
  return <button onClick={() => setEditing(true)}>Edit</button>;
}
```

### Key Rules
```
Server Components CAN import Client Components
Client Components CANNOT import Server Components (pass as children instead)
Props from Server → Client must be serializable (no functions, Date → string)
Client boundary: "use client" marks the boundary — everything imported is client
```

## Server Actions
```
"use server" — marks a function as a server action
Can be defined: inline in server component OR in separate "use server" file
Called from: form action prop, onClick, useEffect, or direct invocation
Automatic: serialization, CSRF protection, progressive enhancement
```

### Form Action Pattern
```tsx
// actions.ts
"use server";
export async function createPost(formData: FormData) {
  const title = formData.get("title") as string;
  const post = await db.post.create({ data: { title } });
  revalidatePath("/posts");
  redirect(`/posts/${post.id}`);
}

// page.tsx (Server Component)
import { createPost } from "./actions";
export default function NewPost() {
  return (
    <form action={createPost}>
      <input name="title" required />
      <button type="submit">Create</button>
    </form>
  );
}
```

### useActionState (replaces useFormState)
```tsx
"use client";
import { useActionState } from "react";
import { createPost } from "./actions";

function PostForm() {
  const [state, formAction, isPending] = useActionState(createPost, { error: null });
  return (
    <form action={formAction}>
      <input name="title" required />
      {state.error && <p className="error">{state.error}</p>}
      <button disabled={isPending}>{isPending ? "Creating..." : "Create"}</button>
    </form>
  );
}
```

### useOptimistic
```tsx
"use client";
import { useOptimistic } from "react";

function TodoList({ todos, addTodo }: Props) {
  const [optimisticTodos, addOptimistic] = useOptimistic(
    todos,
    (state, newTodo: Todo) => [...state, { ...newTodo, pending: true }]
  );

  async function handleAdd(formData: FormData) {
    const newTodo = { id: crypto.randomUUID(), text: formData.get("text") as string };
    addOptimistic(newTodo);
    await addTodo(newTodo); // server action
  }

  return (
    <form action={handleAdd}>
      <input name="text" />
      <ul>
        {optimisticTodos.map(todo => (
          <li key={todo.id} style={{ opacity: todo.pending ? 0.5 : 1 }}>{todo.text}</li>
        ))}
      </ul>
    </form>
  );
}
```

## use() Hook
```
Unwrap promises and context during render
REPLACES: some useEffect data-fetching patterns
Works in: client components (with Suspense for promises) and server components
NOT a hook rule: can be called conditionally (inside if/loops)
```

### Promise Unwrapping
```tsx
import { use, Suspense } from "react";

function UserName({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise); // suspends until resolved
  return <span>{user.name}</span>;
}

// Parent passes the promise (created during render or in server component)
function Page() {
  const userPromise = fetchUser(userId); // start fetch, don't await
  return (
    <Suspense fallback={<Skeleton />}>
      <UserName userPromise={userPromise} />
    </Suspense>
  );
}
```

### Context Reading
```tsx
const theme = use(ThemeContext); // equivalent to useContext(ThemeContext)
// Advantage: can be called conditionally
if (showThemed) {
  const theme = use(ThemeContext); // valid with use(), invalid with useContext()
}
```

## Suspense Patterns
| Pattern | Use Case |
|---|---|
| Data loading | Wrap async component in Suspense with fallback |
| Streaming | Server sends shell, streams content as ready |
| Nested Suspense | Fine-grained loading states per section |
| Error boundary | Pair with ErrorBoundary for error states |

```tsx
<Suspense fallback={<PageSkeleton />}>
  <Header />
  <Suspense fallback={<SidebarSkeleton />}>
    <Sidebar />
  </Suspense>
  <Suspense fallback={<ContentSkeleton />}>
    <MainContent />
  </Suspense>
</Suspense>
```

## ref as Regular Prop (No more forwardRef)
```tsx
// React 19 — ref is just a prop
function Input({ ref, ...props }: { ref?: React.Ref<HTMLInputElement> }) {
  return <input ref={ref} {...props} />;
}
// Usage: <Input ref={myRef} />

// Cleanup function on ref (new in React 19)
<div ref={(node) => {
  // setup
  node.focus();
  // return cleanup function
  return () => { /* cleanup */ };
}} />
```

## Document Metadata
```tsx
// Components can render metadata — hoisted to <head> automatically
function BlogPost({ post }: { post: Post }) {
  return (
    <article>
      <title>{post.title}</title>
      <meta name="description" content={post.excerpt} />
      <link rel="canonical" href={`https://blog.com/${post.slug}`} />
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
}
```

## useFormStatus
```tsx
"use client";
import { useFormStatus } from "react-dom";

function SubmitButton() {
  const { pending, data, method, action } = useFormStatus();
  return <button disabled={pending}>{pending ? "Submitting..." : "Submit"}</button>;
}
// Must be a CHILD of a <form> — does not work in the same component as the form
```

## Migration Notes
| Old Pattern | React 19 Replacement |
|---|---|
| forwardRef(Component) | ref prop directly on component |
| useFormState | useActionState (renamed, added isPending) |
| useEffect for data | use() with Suspense |
| useContext(Ctx) | use(Ctx) — conditional-compatible |
| React.lazy | Still works, but RSC preferred for code splitting |
| string ref | Removed — use callback ref or createRef |
| defaultProps | Use JS default params instead |

## Performance Patterns
```
1. Keep client boundaries small — "use client" only where needed
2. Pass server data as props to client components (serializable only)
3. Use Suspense boundaries to stream and parallelize
4. Colocate data fetching with components that need it (server components)
5. Preload resources: preload('/api/data', { as: 'fetch' })
6. Use React.cache() for request-level deduplication in server components
```
