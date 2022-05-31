import asyncio
import inspect

from unittest.mock import AsyncMock


if __name__ == "__main__":
    mock = AsyncMock()
    print(asyncio.iscoroutinefunction(mock))

    print(inspect.isawaitable(mock()))
