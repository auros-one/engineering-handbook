# Test Isolation & Async Tests

## The Golden Rule

**Never use `sync_to_async()` to call fixtures or create database records in async tests.**

It breaks Django's transaction isolation because `sync_to_async` runs on a different thread pool with a different database connection.

## How pytest-django Transaction Isolation Works

```
Test starts → Transaction begins → Test runs → Transaction rolls back
```

All database operations must happen on the **same connection** to be rolled back.

## What Breaks Isolation

```python
# ❌ BAD: sync_to_async breaks transaction isolation
@pytest.mark.django_db
class TestSomething:
    @pytest.mark.asyncio
    async def test_foo(self, my_factory):
        obj = await sync_to_async(my_factory)()  # Different connection!
        await some_async_function(obj)           # Data persists after test!
```

The `sync_to_async` call executes on a thread pool worker with its own DB connection, outside the test's transaction.

## The Fix: Sync Tests with async_to_sync

```python
# ✅ GOOD: Sync test calling async function
from asgiref.sync import async_to_sync

@pytest.mark.django_db
class TestSomething:
    def _run_async(self, coro):
        async def _wrapper():
            return await coro
        return async_to_sync(_wrapper)()

    def test_foo(self, my_factory):
        obj = my_factory()  # Sync call, same connection
        result = self._run_async(some_async_function(obj))
        assert result.something == expected
```

## When Async Tests Are Fine

Async tests without `@pytest.mark.django_db` are fine:

```python
# ✅ GOOD: No database interaction
class TestPureLogic:
    @pytest.mark.asyncio
    async def test_generate(self):
        with patch("some.external.service") as mock:
            result = await generator.generate("text")
            assert result.field == "value"
```

## Quick Reference

| Pattern | Safe? | Why |
|---------|-------|-----|
| `@pytest.mark.asyncio` + `sync_to_async(fixture)()` + `@pytest.mark.django_db` | ❌ | Different DB connection |
| Sync test + `async_to_sync(async_func)()` + `@pytest.mark.django_db` | ✅ | Same DB connection |
| `@pytest.mark.asyncio` without `@pytest.mark.django_db` | ✅ | No DB to isolate |
| `@pytest.mark.django_db(transaction=True)` | ⚠️ | Works but slower, may cause flush errors |

## Debugging Test Pollution

1. Run failing test alone → passes? It's pollution
2. Binary search: run half the tests before it → still fails? Polluter is in that half
3. Look for `sync_to_async` + `@pytest.mark.django_db` combo
4. Check if tests create records that match queries in other tests
