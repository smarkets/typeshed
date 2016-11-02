from types import ModuleType
from typing import Any

def monkey_patch(os: bool = ...,
                 select: bool = ...,
                 socket: bool = ...,
                 thread: bool = ...,
                 time: bool = ...,
                 psycopg: bool = ...,
                 MySQLdb: bool = ...,
                 builtins: bool = ...,
                 subprocess: bool = ...,
                 __builtin__: bool = ...,
                 all: bool = ...) -> None: ...


# module should be of type ModuleType but mypy doesn't understand it:
# https://github.com/python/mypy/issues/1498
def is_monkey_patched(module: Any) -> bool: ...

def original(modname: str) -> Any: ...
