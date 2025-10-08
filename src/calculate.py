import src.rpn_errors
import src.constants
from src.stack_operations import (pop, push)

def calculate_rpn(input_expression : str) -> list[float]:
    """
    Вычисляет результат Входного выражения, который записан в обратной польской записи
    :input_expression: Выражение, записанное в обратной польской записи
    :return: Возвращает список (стек) чисел
    """
    stack: list[float | int] = []
    token_counter = [[0, 0, 0]] #Для отслеживания количества операторов и чисел, чтобы не применяли бинарную операцию к менее чем двум числам (можно было бы обойтись без этого, если бы не бессмысленные скобки)
    #([количество чисел в подксобочном выражении, количество бинарных операций в подскобочном выражении, количество унарных операций в подскобочном выражении])
    brackets_counter = [0, 0] #Для отслеживания правильной расстановки скобок (количество открывающих, количество закрывающих)
    input_num: float | None | int = None
    for i in input_expression.split():
        try:
            input_num = int(i)
        except ValueError:
            try:
                input_num = float(i)
            except ValueError:
                input_num = None
        match input_num:
            case None:
                match i:
                    case operator if operator in src.constants.BINARY_OPERATIONS:
                        try:
                            num1 = pop(stack)
                            num2 = pop(stack)
                            push(stack, src.constants.operations[i](num2, num1))
                            token_counter[-1][1] += 1

                        except IndexError:
                            raise src.rpn_errors.StackUnderflowError("Нехватка чисел для вычисления, сликшом много операторов ХВАТИТ СПАМИТЬ ЭТИМИ ОПЕРАТОРАМИ")
                        except ZeroDivisionError:
                            raise src.rpn_errors.DivisionByZeroError("ТЫ ЗАБЫЛ, ЧТО НА 0 ДЕЛИТЬ НЕЛЬЗЯ! ИДИ ЛУЧШЕ У БИТЮКОВА СПРОСИ ПОЧЕМУ НЕЛЬЗЯ")

                    case operator if operator in src.constants.UNARY_OPERATIONS:
                        try:
                            num1 = pop(stack)
                            push(stack, src.constants.operations[i](num1))
                            token_counter[-1][2] += 1
                            print(token_counter)
                        except IndexError:
                            raise src.rpn_errors.StackUnderflowError("Нехватка чисел для вычисления, сликшом много операторов ХВАТИТ СПАМИТЬ ЭТИМИ ОПЕРАТОРАМИ")
                    case "(":
                        brackets_counter[0] += 1
                        token_counter[-1][0] += 1 #бинарная операция может быть вместе с числом и скобочным выражением или вместе только скобочными выражениями
                        token_counter.append([0, 0, 0])
                    case ")":
                        if brackets_counter[0] <= brackets_counter[1]:
                            raise src.rpn_errors.BracketsError("Неправильное написание скобок, НЕФИГ БЫЛО ИХ ВООБЩЕ ИСПОЛЬЗОВАТЬ В РПН")
                        token_counter.pop()
                        brackets_counter[1] += 1
                    case _:
                        raise src.rpn_errors.InputError(f"Неизвестный символ {i} ОБ КЛАВИАТУРУ УДАРИЛСЯ?")
            case _:
                stack.append(input_num)
                token_counter[-1][0] += 1
        count_numbers, count_binary_operators, count_unary_operators = token_counter[-1]
        if ((token_counter[-1][0] == 0 and (token_counter[-1][1] > 0 or token_counter[-1][1] > 0)) or \
        (token_counter[-1][0] <= token_counter[-1][1])) and \
              (token_counter[-1] != [0, 0, 0]):
            raise src.rpn_errors.StackUnderflowError("Нехватка чисел для вычисления, сликшом много операторов ХВАТИТ СПАМИТЬ ЭТИМИ ОПЕРАТОРАМИ")

    if brackets_counter[0] != brackets_counter[1]:
        raise src.rpn_errors.BracketsError("Неправильное написание скобок, НЕФИГ БЫЛО ИХ ВООБЩЕ ИСПОЛЬЗОВАТЬ В РПН")
    return stack
