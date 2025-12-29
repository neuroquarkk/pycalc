from error.errors import PyCalcError
from evaluator.evaluator import Evaluator
from lexer.lexer import Lexer
from parser.parser import Parser
import math


def evaluate(exp: str) -> float:
    lexer = Lexer(exp)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    evaluator = Evaluator()
    result = evaluator.evaluate(ast)

    return result


def internal():
    print("=" * 70)
    print("Internal Pipeline Demonstration")
    print("=" * 70)
    print()

    expr = "3 + 4 * 2"
    print(f"Expression: {expr}\n")

    lexer = Lexer(expr)
    tokens = lexer.tokenize()
    print("Tokens:")
    for token in tokens:
        print(f"  {token}")
    print()

    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST:\n  {ast}")
    print()

    evaluator = Evaluator()
    result = evaluator.evaluate(ast)
    print(f"Result: {result}")
    print()


def demo():
    test_cases = [
        "42",
        "3 + 5",
        "10 - 3 * 2",
        "(10 - 3) * 2",
        "2.5 * 4",
        "100 / 5 / 2",
        "-5 + 3",
        "-(3 + 2) * 4",
        "2 + 3 * 4 - 5 / 2",
        "((2 + 3) * (4 - 1)) / 3",
    ]

    print(
        f"{'Expression':<30} | {'Expected':<10} | {'Actual':<10} | {'Status'}"
    )
    print("-" * 70)

    passed = 0
    failed = 0

    for expr in test_cases:
        try:
            expected = float(eval(expr))
            actual = evaluate(expr)
            is_correct = math.isclose(actual, expected, rel_tol=1e-9)

            status = "PASS" if is_correct else "FAIL"
            if is_correct:
                passed += 1
            else:
                failed += 1

            print(f"{expr:<30} | {expected:<10} | {actual:<10} | {status}")

        except PyCalcError as e:
            print(f"{expr:<30} | {'Error':<10} | {'Error':<10} | {e}")
            failed += 1

    print("-" * 70)
    print(f"Test Suite Completed: {passed} Passed, {failed} Failed")


if __name__ == "__main__":
    demo()
