from typing import Optional
from lexer.tokens import Token


class PyCalcError(Exception):
    """Base exception for all PyCalc errors"""

    pass


class LexerError(PyCalcError):
    """Raised when lexical analysis fail"""

    def __init__(self, message: str, position: Optional[int] = None):
        self.position = position
        super().__init__(
            f"Lexer error at position {position}: {message}"
            if position
            else message
        )


class ParserError(PyCalcError):
    """Raised when parsing fail"""

    def __init__(self, message: str, token: Optional[Token] = None):
        self.token = token
        super().__init__(
            f"Parser error at {token}: {message}" if token else message
        )


class EvaluatorError(PyCalcError):
    """Raised when evaluation fail"""

    pass
