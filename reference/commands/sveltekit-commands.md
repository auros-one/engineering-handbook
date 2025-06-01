# SvelteKit Commands Reference

Essential SvelteKit commands extracted from existing project patterns and workflows.

## Development Setup

### Dependency Management
```bash
# Install all dependencies including dev dependencies
npm install --include=dev

# Install specific package
npm install <package-name>
npm install -D <dev-package-name>  # Development dependency
```

### Environment Setup
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with required values
# Common variables:
# - API URLs
# - Authentication keys
# - Feature flags
```

## Development Server

### Local Development
```bash
# Start development server
npm run dev

# Usually runs on http://localhost:5173 or similar
# Check package.json scripts for exact configuration
```

## Type Safety and API Integration

### Type Synchronization
```bash
# Sync backend API types to frontend
npm run sync-types

# Important: Wait 5-10 seconds after backend changes
# If it fails, wait 5 seconds and retry
# If persistent failures, check backend with pytest
```

### Type Checking
```bash
# Run Svelte type checking
npm run check

# Watch mode for continuous checking
npm run check:watch
```

## Code Quality

### Linting
```bash
# Run ESLint
npm run lint

# Fix auto-fixable issues
npm run lint:fix
```

### Formatting
```bash
# Format with Prettier (if configured)
npm run format

# Check formatting
npm run format:check
```

## Testing

### Unit Tests
```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run specific test file
npm run test -- <test-file>
```

### End-to-End Tests
```bash
# Run Playwright tests (if configured)
npm run test:e2e

# Run e2e tests in headed mode
npm run test:e2e:headed
```

## Build and Production

### Building
```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

### Static Analysis
```bash
# Check for unused exports
npm run check:unused

# Bundle analysis (if configured)
npm run analyze
```

## Development Utilities

### Package Management
```bash
# Check for outdated packages
npm outdated

# Update packages
npm update

# Audit for vulnerabilities
npm audit
npm audit fix
```

### Development Scripts
Common project-specific scripts (check package.json):
```bash
# Generate types from backend
npm run sync-types

# Start with specific configuration
npm run dev:local
npm run dev:staging

# Database or backend integration
npm run setup:dev
```

## SvelteKit Specific

### Page and Component Generation
```bash
# SvelteKit doesn't have built-in generators
# Check if project has custom scripts:
npm run generate:page
npm run generate:component
```

### Routing and Navigation
- File-based routing in `src/routes/`
- `+page.svelte` for pages
- `+layout.svelte` for layouts
- `+page.server.ts` for server-side logic
- `+page.ts` for client-side logic

## Debugging

### Development Tools
- Svelte DevTools browser extension
- SvelteKit debug logs (`DEBUG=vite:* npm run dev`)
- Network tab for API call inspection

### Common Debug Commands
```bash
# Verbose development mode
DEBUG=vite:* npm run dev

# Check SvelteKit version and config
npx svelte-kit --version
npx svelte-kit --help
```

## Integration with Backend

### API Client Setup
- Generated TypeScript client from OpenAPI schema
- TanStack Query for data fetching and caching
- Automatic authentication middleware
- Toast notifications for user feedback

### Common Patterns
```bash
# After backend API changes:
1. npm run sync-types
2. npm run check  # Verify types
3. npm run dev    # Test integration
```