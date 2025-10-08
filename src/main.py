import src.calculate
import sys


def main() -> None:

    expression = sys.stdin.readline()
    result = src.calculate.calculate_rpn(expression)

    print(*result)


if __name__ == "__main__":
    main()
