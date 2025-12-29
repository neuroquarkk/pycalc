from typing import Dict, List
from error.errors import LexerError
from .tokens import Token, TokenType


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None

    def __advance(self) -> None:
        self.pos += 1
        self.current_char = (
            self.text[self.pos] if self.pos < len(self.text) else None
        )

    def __skip_whitespace(self) -> None:
        while self.current_char and self.current_char.isspace():
            self.__advance()

    def __read_number(self) -> Token:
        start_pos = self.pos
        num_str = ""
        has_dot = False

        while self.current_char and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            if self.current_char == ".":
                if has_dot:
                    raise LexerError(
                        "Multiple decimal points in number", self.pos
                    )
                has_dot = True
            num_str += self.current_char
            self.__advance()

        value = float(num_str) if has_dot else int(num_str)
        return Token(TokenType.NUMBER, value, start_pos)

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []

        while self.current_char:
            if self.current_char.isspace():
                self.__skip_whitespace()
                continue

            if self.current_char.isdigit():
                tokens.append(self.__read_number())
                continue

            token_map: Dict[str, TokenType] = {
                "+": TokenType.PLUS,
                "-": TokenType.MINUS,
                "*": TokenType.MULTIPLY,
                "/": TokenType.DIVIDE,
                "(": TokenType.LPAREN,
                ")": TokenType.RPAREN,
            }

            if self.current_char in token_map:
                token = Token(token_map[self.current_char], None, self.pos)
                tokens.append(token)
                self.__advance()
            else:
                raise LexerError(
                    f"Unexpected character '{self.current_char}'", self.pos
                )

        tokens.append(Token(TokenType.EOF, None, self.pos))
        return tokens
