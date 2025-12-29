from enum import Enum, auto
from dataclasses import dataclass
from typing import Any


class TokenType(Enum):
    # Literals
    NUMBER = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    # Grouping
    LPAREN = auto()
    RPAREN = auto()

    # Special
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: Any
    position: int

    def __repr__(self) -> str:
        if self.value is not None:
            return f"Token({self.type.name}, {self.value}, pos={self.position})"
        return f"Token({self.type.name}, pos={self.position})"
