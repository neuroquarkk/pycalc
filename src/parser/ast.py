from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


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


@dataclass
class ConstantNode(ASTNode):
    name: str

    def __repr__(self) -> str:
        return f"Constant({self.name})"


@dataclass
class FunctionCallNode(ASTNode):
    name: str
    args: List[ASTNode]

    def __repr__(self) -> str:
        arg_str = ", ".join(str(arg) for arg in self.args)
        return f"Functioncall({self.name}, [{arg_str}])"
