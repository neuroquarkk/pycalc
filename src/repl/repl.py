from typing import Optional
from evaluator.evaluator import Evaluator
from lexer.lexer import Lexer
from parser.parser import Parser
from error.errors import PyCalcError


class REPL:
    def __init__(self):
        self.evaluator = Evaluator()
        self.history = []
        self.running = True

    def __evaluate_expression(self, expression: str) -> Optional[float]:
        if not expression.strip():
            return None

        lexer = Lexer(expression)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        result = self.evaluator.evaluate(ast)

        return result

    def __print_banner(self) -> None:
        print("=" * 70)
        print("PyCalc")
        print("=" * 70)
        print("Type expressions to evaluate them")
        print(
            "Commands: 'exit' or 'quit' to exit, 'history' to view history, 'clear' to clear history"
        )
        print("=" * 70)
        print()

    def __handle_command(self, command: str) -> bool:
        command = command.strip().lower()

        if command in ("exit", "quit", "q"):
            self.running = False
            return True

        if command == "history":
            if not self.history:
                print("No history yet")
            else:
                print("\nExpression history")
                print("-" * 50)
                for i, (expr, result) in enumerate(self.history, 1):
                    print(f"{i:3}. {expr:<30} = {result}")
                print("-" * 50)
            return True

        if command == "clear":
            self.history.clear()
            print("History cleared")
            return True

        if command == "help":
            print("\nAvailable commands:")
            print("  exit, quit, q  - Exit the calculator")
            print("  history        - Show calculation history")
            print("  clear          - Clear history")
            print("  help           - Show this help message")
            print("\nSupported operations:")
            print("  +, -, *, /     - Basic arithmetic")
            print("  ( )            - Grouping")
            print("  +x, -x         - Unary Operators")
            return True

        return False

    def run(self) -> None:
        self.__print_banner()

        while self.running:
            try:
                expression = input(">>> ").strip()

                if not expression:
                    continue

                if self.__handle_command(expression):
                    continue

                result = self.__evaluate_expression(expression)
                if result is not None:
                    print(f"= {result}")
                    self.history.append((expression, result))

            except PyCalcError as e:
                print(f"Error: {e}")

            except KeyboardInterrupt:
                print("\n\nType 'exit' to quit")

            except EOFError:
                break

            except Exception as e:
                print(f"Unexpected error: {e}")
