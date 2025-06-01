# SvelteKit Frontend Behavior Guidelines

Apply when implementing frontend features with SvelteKit - includes patterns for API queries, mutations, state management, and component design.

## Core Principles

This project uses Django for the backend and SvelteKit for the frontend. Maintain consistency with existing project patterns and best practices.

## End-to-End Feature Implementation

### 1. Sync Backend Types

- Run `npm run sync-types` to sync backend types with frontend
- **Important timing considerations:**
  - If backend was just updated, wait 5-10 seconds for dev server restart
  - If sync-types fails, wait 5 seconds and retry
  - If issues persist, run `pytest` in backend to check for errors
  - If tests pass but sync-types fails, stop and ask for help

### 2. Analyze Existing Code

- Inspect existing frontend code organization
- Determine where new scope/feature fits
- Study existing UI/UX design and styling patterns

### 3. Implementation Planning

- Reason about best implementation approach
- Consider code organization and UI/UX consistency
- Plan component structure and data flow

### 4. Development

- Create or update frontend code following existing patterns
- Use established component and styling conventions

### 5. Quality Checks

- Run type checking: `npm run check`
- Run linting: `npm run lint`

## API Integration Patterns

### Frontend Query Pattern (TanStack Query + OpenAPI-Fetch)

**Key concepts:**
- TanStack Query provides data fetching and caching
- OpenAPI-Fetch generates TypeScript client from backend API
- Generated types are in `project/lib/api/backend-api-schema.d.ts`
- Authentication middleware is automatically added (grep for 'createClient')

**Query Implementation:**
```svelte
<script lang="ts">
    import type { components } from '$lib/api/backend-api-schema';
    import { createQuery, useQueryClient } from '@tanstack/svelte-query';
    import { apiClient } from '$lib/api';
    import Spinner from '$lib/components/loading/Spinner.svelte';

    // Type definitions
    type ResponseType = components['schemas']['YourSchemaType'];
    type ErrorType = Error;

    // Query client for cache management
    const queryClient = useQueryClient();

    // Create query
    const query = createQuery<ResponseType, ErrorType>({
        queryKey: ['uniqueKey', optionalId],
        queryFn: async () => {
            const { data, error } = await apiClient.GET('/your/endpoint/', {
                params: {
                    path: { id: optionalId },
                    query: { page: pageNumber }
                }
            });

            if (error) throw new Error(error);
            if (!data) throw new Error('No data returned');
            return data;
        },
        staleTime: 5 * 60 * 1000,
        cacheTime: 10 * 60 * 1000,
        enabled: Boolean(optionalId),
        retry: 3,
    });

    // Reactive access
    $: data = $query.data;
    $: isLoading = $query.isPending;
    $: error = $query.error;
</script>
```

**Mutation Implementation:**
```svelte
<script lang="ts">
    import { createMutation, useQueryClient } from '@tanstack/svelte-query';
    import toast from 'svelte-french-toast';

    const mutation = createMutation({
        mutationFn: async ({ id, data }) => {
            const { data: responseData, error } = await apiClient.POST('/endpoint/{id}/', {
                params: { path: { id } },
                body: data
            });

            if (error) {
                toast.error(error.error || 'An error occurred');
                throw new Error(error.error || 'An error occurred');
            }
            return responseData;
        },
        onSuccess: async () => {
            toast.success('Operation successful!');
            await queryClient.invalidateQueries({ queryKey: ['yourKey'] });
        },
        onError: () => {
            toast.error('Operation failed');
        }
    });
</script>
```

## State Management (Svelte 5 Runes)

### Reactive State
```javascript
// Basic reactive state
let count = $state<number>(0);
let user = $state<User>({ name: 'Alice', age: 30 });

// Computed values
let doubled = $derived<number>(count * 2);
let isEven = $derived<boolean>(count % 2 === 0);

// Effects
$effect(() => {
    console.log(`Count changed to ${count}`);
    return () => console.log('Cleanup');
});
```

### Component Props
```javascript
interface Props {
    message: string;
    count?: number;
}

let { message, count = 0 }: Props = $props<Props>();
let { value = $bindable<string>('') } = $props();
```

## Consistency Guidelines

Before creating new files:

1. **Inspect existing files** to understand project structure
2. **Follow established patterns** for component organization
3. **Match existing styling** and UI conventions
4. **Use consistent naming** and file structure patterns

**Example:** When creating new views or components, first examine existing implementations to maintain project consistency.