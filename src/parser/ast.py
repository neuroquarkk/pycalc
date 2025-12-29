from abc import ABC, abstractmethod
from dataclasses import dataclass


class ASTNode(ABC):
    """Base class for all AST nodes"""

    @abstractmethod
    def __repr__(self) -> str:
        pass


@dataclass
class NumberNode(ASTNode):
    value: float | int

    def __repr__(self) -> str:
        return f"Number({self.value})"


@dataclass
class BinaryOpNode(ASTNode):
    operator: str
    left: ASTNode
    right: ASTNode

    def __repr__(self) -> str:
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"


@dataclass
class UnaryOpNode(ASTNode):
    operator: str
    operand: ASTNode

    def __repr__(self) -> str:
        return f"UnaryOp({self.operator}, {self.operand})"
