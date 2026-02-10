# Tailwind CSS — Compressed AGENTS.md Knowledge

## Quick Reference
| Area | Key Concepts |
|---|---|
| Utility-First | Compose styles from atomic classes, avoid custom CSS |
| Responsive | Mobile-first breakpoints: sm, md, lg, xl, 2xl |
| States | hover:, focus:, active:, disabled:, group-hover:, peer-* |
| Dark Mode | dark: variant, class or media strategy |
| Components | @apply extraction, CVA pattern, component libraries |
| Config | tailwind.config.ts, theme extension, custom utilities, plugins |

## Tailwind v4 vs v3
| Feature | v3 | v4 |
|---|---|---|
| Config | tailwind.config.js | CSS-based @theme directive |
| Content paths | content: ['./src/**/*.tsx'] | Auto-detection or @source |
| Theme | theme.extend in config | @theme { --color-primary: #xxx } |
| Plugins | JS plugins | CSS @plugin or JS |
| Import | @tailwind base/components/utilities | @import "tailwindcss" |

## Core Utility Patterns
### Layout
| Class Pattern | Purpose |
|---|---|
| flex / grid | Display type |
| flex-col / flex-row | Flex direction |
| items-center justify-between | Alignment |
| grid-cols-{n} gap-{n} | Grid columns and gap |
| w-full max-w-{size} mx-auto | Centered container |
| h-screen min-h-dvh | Full viewport height |
| fixed absolute relative sticky | Positioning |
| z-{n} | z-index layering |
| overflow-hidden overflow-auto | Overflow behavior |

### Spacing
```
p-{n} — padding all sides       | px-{n} py-{n} — horizontal/vertical
m-{n} — margin all sides        | mx-auto — center horizontally
space-x-{n} — horizontal gap    | space-y-{n} — vertical gap
gap-{n} — flex/grid gap          | Scale: 0,0.5,1,1.5,2,2.5,3,3.5,4,5,6,8,10,12,16,20,24...
```

### Typography
| Class | Purpose |
|---|---|
| text-{size} | Font size: xs, sm, base, lg, xl, 2xl...9xl |
| font-{weight} | thin, light, normal, medium, semibold, bold, extrabold |
| leading-{n} | Line height: tight, snug, normal, relaxed, loose |
| tracking-{n} | Letter spacing: tighter, tight, normal, wide, wider |
| text-{color}-{shade} | Color: text-gray-900, text-blue-500 |
| truncate | Overflow ellipsis (single line) |
| line-clamp-{n} | Multi-line truncation |

### Colors
```
Pattern: {property}-{color}-{shade}
Properties: text, bg, border, ring, shadow, accent, fill, stroke
Colors: slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green,
        emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose
Shades: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950
Special: transparent, current, inherit, white, black
```

## Responsive Design
```
Mobile-first: no prefix = all sizes, then override upward
sm: 640px | md: 768px | lg: 1024px | xl: 1280px | 2xl: 1536px
```

| Pattern | Effect |
|---|---|
| flex flex-col md:flex-row | Stack on mobile, row on desktop |
| hidden md:block | Hidden on mobile, visible on md+ |
| text-sm md:text-base lg:text-lg | Scale text by breakpoint |
| grid-cols-1 md:grid-cols-2 lg:grid-cols-3 | Responsive grid |
| w-full md:w-1/2 lg:w-1/3 | Responsive widths |
| p-4 md:p-6 lg:p-8 | Responsive padding |

### Container Queries (v3.2+)
```html
<div class="@container">
  <div class="@md:flex-row flex-col">
    <!-- Responds to container width, not viewport -->
  </div>
</div>
```

## State Variants
| Variant | Trigger |
|---|---|
| hover: | Mouse over |
| focus: | Focused (tab or click) |
| focus-visible: | Keyboard focus only |
| active: | Mouse pressed |
| disabled: | Disabled element |
| first: / last: | First/last child |
| odd: / even: | Odd/even children |
| group-hover: | Parent with class="group" hovered |
| peer-checked: | Sibling with class="peer" checked |
| data-[state=open]: | Custom data attribute |
| aria-[selected=true]: | ARIA attribute |

### Group & Peer Pattern
```html
<div class="group">
  <span class="group-hover:text-blue-500">Hover parent to style me</span>
</div>

<input class="peer" type="checkbox" />
<label class="peer-checked:font-bold">Styled when checkbox checked</label>
```

## Dark Mode
```html
<!-- Class strategy (recommended for toggles) -->
<html class="dark">
  <div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">

<!-- tailwind.config -->
darkMode: 'class' | 'media' | ['variant', '.dark-mode']
```

| Pattern | Light | Dark |
|---|---|---|
| Background | bg-white | dark:bg-gray-900 |
| Text | text-gray-900 | dark:text-gray-100 |
| Border | border-gray-200 | dark:border-gray-700 |
| Card | bg-gray-50 | dark:bg-gray-800 |
| Muted text | text-gray-500 | dark:text-gray-400 |

## Component Extraction Patterns
### CVA (Class Variance Authority) — Recommended
```typescript
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils';

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline: 'border border-input bg-background hover:bg-accent',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: { variant: 'default', size: 'default' },
  }
);

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>,
  VariantProps<typeof buttonVariants> {}

function Button({ className, variant, size, ...props }: ButtonProps) {
  return <button className={cn(buttonVariants({ variant, size, className }))} {...props} />;
}
```

### cn() Utility (tailwind-merge + clsx)
```typescript
import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
// Handles: conditional classes, merging conflicts, array/object syntax
// cn('px-4 py-2', conditional && 'bg-blue-500', 'px-6') → 'py-2 px-6 bg-blue-500'
```

## Common Layout Patterns
```html
<!-- Centered page content -->
<main class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

<!-- Sticky header + scrollable content -->
<div class="flex h-screen flex-col">
  <header class="sticky top-0 z-50 border-b bg-white">...</header>
  <main class="flex-1 overflow-auto">...</main>
</div>

<!-- Sidebar layout -->
<div class="flex h-screen">
  <aside class="w-64 shrink-0 border-r">...</aside>
  <main class="flex-1 overflow-auto">...</main>
</div>

<!-- Card grid -->
<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
  <div class="rounded-lg border bg-card p-6 shadow-sm">...</div>
</div>

<!-- Full-bleed hero -->
<section class="relative flex min-h-[60vh] items-center justify-center bg-gradient-to-br from-blue-600 to-purple-700 text-white">
```

## Animation & Transitions
| Class | Effect |
|---|---|
| transition | Default transition (color, bg, border, shadow, opacity, transform) |
| transition-all | Transition all properties |
| duration-{ms} | Duration: 75, 100, 150, 200, 300, 500, 700, 1000 |
| ease-in / ease-out / ease-in-out | Timing function |
| animate-spin | Continuous rotation |
| animate-ping | Radar ping effect |
| animate-pulse | Fade in/out |
| animate-bounce | Bounce |

## Tailwind + shadcn/ui
```
CSS variables approach: define design tokens as CSS vars
bg-background, text-foreground, bg-primary, etc. map to CSS vars
Theming: swap CSS var values for different themes
Install: npx shadcn@latest init → adds components to your project (not node_modules)
```

## Best Practices
| Practice | Rationale |
|---|---|
| Use cn() for conditional classes | Prevents class conflicts, clean API |
| Extract components, not @apply | Components > utility extraction |
| Mobile-first responsive | Match Tailwind's min-width breakpoints |
| Use design tokens | Consistent spacing, colors via theme |
| Avoid arbitrary values | Prefer theme scale; [#hex] only for brand colors |
| Purge safelist sparingly | Dynamic classes need safelist or full class names |
| Group related utilities | Order: layout → sizing → spacing → typography → visual |
