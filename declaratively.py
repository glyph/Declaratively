"""
Enforced declarative specification of module-level code objects.
"""

from __future__ import annotations

__version__ = '0.0.1'

from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Generic, TypeVar, List, Sequence, Callable, MutableMapping, Tuple, Optional, Iterator

import inspect

DeclaredType = TypeVar("DeclaredType")
SpecifiedType = TypeVar("SpecifiedType")
NamespaceType = TypeVar("NamespaceType")


@dataclass
class Declarer(Generic[SpecifiedType, DeclaredType, NamespaceType]):

    _collection: DeclarationCollection
    namespace: str
    _namespaceObject: NamespaceType
    _declarations: List[Tuple[SpecifiedType, DeclaredType]]

    def declare(self, specification: SpecifiedType) -> DeclaredType:
        declaration = self._collection._specificationToDeclaration(
            self.namespace, self._namespaceObject, specification
        )
        self._declarations.append((specification, declaration))
        return declaration


@dataclass
class _NamespaceRecord(Generic[NamespaceType, SpecifiedType, DeclaredType]):
    _namespace: str
    _namespaceObject: NamespaceType
    _declarations: Sequence[Tuple[SpecifiedType, DeclaredType]]


class AlreadyDeclared(Exception):
    """
    The namespace already had a declaration applied.
    """


@dataclass
class DeclarationCollection(Generic[NamespaceType, SpecifiedType, DeclaredType]):

    _name: str
    _specificationToDeclaration: Callable[
        [str, NamespaceType, SpecifiedType], DeclaredType
    ]
    _namespaceFactory: Callable[[str], NamespaceType]
    _declarationNamespaces: MutableMapping[
        str, _NamespaceRecord[NamespaceType, SpecifiedType, DeclaredType]
    ] = field(default_factory=dict)

    @contextmanager
    def declarations(
        self, group: Optional[NamespaceType] = None, namespace: Optional[str] = None
    ) -> Iterator[Declarer[SpecifiedType, DeclaredType, NamespaceType]]:
        if namespace is None:
            namespace = inspect.currentframe().f_globals['__name__']
        if namespace in self._declarationNamespaces:
            raise AlreadyDeclared(
                f"Already declared {self._name} for namespace {namespace}"
            )
        if group is None:
            group = self._namespaceFactory(namespace)
        declarations: List[Tuple[SpecifiedType, DeclaredType]] = []
        self._declarationNamespaces[namespace] = _NamespaceRecord(
            namespace, group, declarations
        )
        declarer = Declarer(self, namespace, group, declarations)
        yield declarer
