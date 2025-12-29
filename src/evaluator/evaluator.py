from error.errors import EvaluatorError
from parser.ast import ASTNode, BinaryOpNode, NumberNode, UnaryOpNode


class Evaluator:
    def evaluate(self, node: ASTNode) -> float:
        """Evaluate an AST node and return its value"""
        if isinstance(node, NumberNode):
            return self.__eval_number(node)
        if isinstance(node, BinaryOpNode):
            return self.__eval_binary_op(node)
        if isinstance(node, UnaryOpNode):
            return self.__eval_unary_op(node)
        else:
            raise EvaluatorError(f"Unknown node type: {type(node)}")

    def __eval_number(self, node: NumberNode) -> float:
        return float(node.value)

    def __eval_binary_op(self, node: BinaryOpNode) -> float:
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)

        if node.operator == "+":
            return left + right
        elif node.operator == "-":
            return left - right
        elif node.operator == "*":
            return left * right
        elif node.operator == "/":
            if right == 0:
                raise EvaluatorError("Division by zero")
            return left / right
        else:
            raise EvaluatorError(f"Unknown operator: {node.operator}")

    def __eval_unary_op(self, node: UnaryOpNode) -> float:
        operand = self.evaluate(node.operand)

        if node.operator == "+":
            return operand
        elif node.operator == "-":
            return -operand
        else:
            raise EvaluatorError(f"Unknown unary operator: {node.operator}")
