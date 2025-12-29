from error.errors import EvaluatorError
from parser.ast import (
    ASTNode,
    BinaryOpNode,
    ConstantNode,
    FunctionCallNode,
    NumberNode,
    UnaryOpNode,
)
import math


class Evaluator:
    CONSTANTS = {
        "pi": math.pi,
        "e": math.e,
    }

    def evaluate(self, node: ASTNode) -> float:
        """Evaluate an AST node and return its value"""
        if isinstance(node, NumberNode):
            return self.__eval_number(node)
        if isinstance(node, BinaryOpNode):
            return self.__eval_binary_op(node)
        if isinstance(node, UnaryOpNode):
            return self.__eval_unary_op(node)
        if isinstance(node, ConstantNode):
            return self.__eval_constant(node)
        if isinstance(node, FunctionCallNode):
            return self.__eval_function_call(node)
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

    def __eval_constant(self, node: ConstantNode) -> float:
        if node.name not in self.CONSTANTS:
            raise EvaluatorError(f"Unknown constant: {node.name}")
        return self.CONSTANTS[node.name]

    def __eval_function_call(self, node: FunctionCallNode) -> float:
        args = [self.evaluate(arg) for arg in node.args]

        try:
            if node.name == "abs":
                return abs(args[0])
            elif node.name == "sqrt":
                if args[0] < 0:
                    raise EvaluatorError(
                        "Cannot take square root of negative number"
                    )
                return math.sqrt(args[0])
            elif node.name == "pow":
                return math.pow(args[0], args[1])
            elif node.name == "min":
                return min(args)
            elif node.name == "max":
                return max(args)
            elif node.name == "round":
                if len(args) == 1:
                    return round(args[0])
                else:
                    return round(args[0], int(args[1]))
            elif node.name == "sin":
                return math.sin(args[0])
            elif node.name == "cos":
                return math.cos(args[0])
            elif node.name == "tan":
                return math.tan(args[0])
            else:
                raise EvaluatorError(f"Unknown function: {node.name}")
        except (ValueError, OverflowError) as e:
            raise EvaluatorError(f"Math error in {node.name}: {str(e)}")
