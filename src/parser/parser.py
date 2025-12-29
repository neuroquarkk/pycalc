from typing import List
from error.errors import ParserError
from lexer.tokens import Token, TokenType
from .ast import ASTNode, BinaryOpNode, NumberNode, UnaryOpNode


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None

    def __advance(self) -> None:
        self.pos += 1
        self.current_token = (
            self.tokens[self.pos] if self.pos < len(self.tokens) else None
        )

    def __expect(self, token_type: TokenType) -> Token:
        """Consume token of expected value or raise error"""
        if not self.current_token or self.current_token.type != token_type:
            raise ParserError(f"Expected {token_type.name}", self.current_token)
        token = self.current_token
        self.__advance()
        return token

    def __expression(self) -> ASTNode:
        node = self.__term()

        while self.current_token and self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            op = "+" if self.current_token.type == TokenType.PLUS else "-"
            self.__advance()
            node = BinaryOpNode(op, node, self.__term())

        return node

    def __term(self) -> ASTNode:
        """Parse Multiplication and division"""
        node = self.factor()

        while self.current_token and self.current_token.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
        ):
            op = "*" if self.current_token.type == TokenType.MULTIPLY else "/"
            self.__advance()
            node = BinaryOpNode(op, node, self.factor())

        return node

    def factor(self) -> ASTNode:
        """Parse unary operators and primary expressions"""
        if self.current_token and self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
        ):
            op = "+" if self.current_token.type == TokenType.PLUS else "-"
            self.__advance()
            return UnaryOpNode(op, self.factor())

        return self.primary()

    def primary(self) -> ASTNode:
        """Parse numbers and parenthesized expressions"""
        token = self.current_token

        if token and token.type == TokenType.NUMBER:
            self.__advance()
            return NumberNode(token.value)

        if token and token.type == TokenType.LPAREN:
            self.__advance()
            node = self.__expression()
            self.__expect(TokenType.RPAREN)
            return node

        raise ParserError("Expected Number or '('", token)

    def parse(self) -> ASTNode:
        """Parse tokens into AST"""
        if not self.tokens or (
            self.current_token and self.current_token.type == TokenType.EOF
        ):
            raise ParserError("Empty expression")

        ast = self.__expression()

        if self.current_token and self.current_token.type != TokenType.EOF:
            raise ParserError(
                "Unexpected token after expression", self.current_token
            )

        return ast
