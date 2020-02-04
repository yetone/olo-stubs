from typing import TypeVar, Type, Any, Optional, List, ClassVar, overload

from .expression import BinaryExpression
from .query import Query

T = TypeVar('T')
M = TypeVar('M', bound='Model')


class ModelMeta(type):
    @property
    def query(cls: Type[T]) -> Query[T]: ...


class Model(metaclass=ModelMeta):

    AES_KEY: ClassVar[str]
    __table_name__: str

    def __init__(self, **kwargs: Any) -> None: ...

    @classmethod
    def get(cls: Type[M], ident: Any, *kwargs: Any) -> Optional[M]: ...

    @classmethod
    def get_multi(cls: Type[M], idents: List[T], filter_none: bool = False) -> List[Optional[M]]: ...

    @classmethod
    def gets(cls: Type[M], idents: List[T], filter_none: bool = False) -> List[Optional[M]]: ...

    @classmethod
    def get_by(cls: Type[M], *expressions: BinaryExpression, **expression_dict: Any) -> Optional[M]: ...

    @classmethod
    def get_multi_by(cls: Type[M], *expressions: BinaryExpression, **expression_dict: Any) -> List[M]: ...

    @classmethod
    def gets_by(cls: Type[M], *expressions: BinaryExpression, **expression_dict: Any) -> List[M]: ...

    @classmethod
    def create(cls: Type[M], **kwargs: Any) -> M: ...

    # FIXME: return bool
    def update(self, **kwargs: Any) -> Any: ...

    def delete(self, **kwargs: Any) -> bool: ...
