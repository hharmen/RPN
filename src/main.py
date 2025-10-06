import calculate


def main() -> None:

    expression = input()
    result = calculate.calculate_rpn(expression)

    print(*result)


if __name__ == "__main__":
    main()
