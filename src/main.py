import calculate
import sys


def main() -> None:

    expression = sys.stdin.read()
    result = calculate.calculate_rpn(expression)

    print(*result)


if __name__ == "__main__":
    main()
