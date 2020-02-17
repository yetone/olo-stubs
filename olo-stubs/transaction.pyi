from typing import TypeVar

T = TypeVar('T')


class Transaction:
    def __enter__(self) -> Transaction: ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def __call__(self, func: T) -> T: ...
