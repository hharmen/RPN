import rpn_errors
import constants

def push(st: list[float], x: float) -> None:
    """
    Кладет элемент в стек
    :st: Стек
    :x: Элемент, который кладет в стек
    """
    st.append(x)

def pop(st: list[float]) -> float:
    """
    Достает из стека верхний элемент
    :st: Стек
    :return: Верхний элемент стека
    """
    if is_empty(st):
        raise IndexError("pop from empty stack")
    return st.pop()

def is_empty(st: list[float]) -> bool:
    """
    Проверяет не пустой ли стек
    :st: Стек
    :return: Возвращает булевый ответ
    """
    return not st






def calculate_rpn(input_expression : str) -> list[float]:
    """
    Вычисляет результат Входного выражения, который записан в обратной польской записи
    :input_expression: Выражение, записанное в обратной польской записи
    :return: Возвращает список (стек) чисел
    """
    stack: list[float] = []
    token_counter = [[0, 0, 0]] #Для отслеживания количества операторов и чисел, чтобы не применяли бинарную операцию к менее чем двум числам (можно было бы обойтись без этого, если бы не бессмысленные скобки)
    #([количество чисел в подксобочном выражении, количество бинарных операций в подскобочном выражении, количество унарных операций в подскобочном выражении])
    brackets_counter = [0, 0] #Для отслеживания правильной расстановки скобок (количество открывающих, количество закрывающих)
    for i in input_expression.split():
        try:
            input_num = float(i)
        except ValueError:
            input_num = None
        if input_num is None:
            if i in constants.BINARY_OPERATIONS:
                try:
                    num1 = pop(stack)
                    num2 = pop(stack)
                    push(stack, constants.operations[i](num2, num1))
                    token_counter[-1][1] += 1

                except IndexError:
                    raise rpn_errors.StackUnderflowError("Нехватка чисел для вычисления, сликшом много операторов")
                except ZeroDivisionError:
                    raise rpn_errors.DivisionByZeroError("ТЫ ЗАБЫЛ, ЧТО НА 0 ДЕЛИТЬ НЕЛЬЗЯ! ИДИ ЛУЧШЕ У БИТЮКОВА СПРОСИ ПОЧЕМУ НЕЛЬЗЯ")


            elif i in constants.UNARY_OPERATIONS:
                try:
                    num1 = pop(stack)
                    push(stack, constants.operations[i](num1))
                    token_counter[-1][2] += 1
                    print(token_counter)
                except IndexError:
                    raise rpn_errors.StackUnderflowError("Нехватка чисел для вычисления, сликшом много операторов")

            elif i == "(":
                brackets_counter[0] += 1
                token_counter[-1][0] += 1
                token_counter.append([0, 0, 0])


            elif i == ")":
                token_counter.pop()
                brackets_counter[1] += 1
        else:
            stack.append(input_num)
            token_counter[-1][0] += 1

        count_numbers, count_binary_operators, count_unary_operators = token_counter[-1]

        if (brackets_counter[0] < brackets_counter[1]):
            raise rpn_errors.BracketsError("Неправильное написание скобок")

        if ((token_counter[-1][0] == 0 and (token_counter[-1][1] > 0 or token_counter[-1][1] > 0)) or \
        (token_counter[-1][0] <= token_counter[-1][1])) and \
              (token_counter[-1] != [0, 0, 0]):
            raise rpn_errors.StackUnderflowError("Нехватка чисел для вычисления, сликшом много операторов")

    return stack
