import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from calculate import calculate_rpn
import rpn_errors



class TestRPNCalculatorSuccess:
    """Тесты успешных вычислений для функции calculate_rpn"""

    def test_addition(self) -> None:
        """Тест сложения"""
        assert calculate_rpn("1 2 +") == [3]

    def test_subtraction(self) -> None:
        """Тест вычитания"""
        assert calculate_rpn("5 3 -") == [2]

    def test_multiplication(self) -> None:
        """Тест умножения"""
        assert calculate_rpn("2 3 *") == [6]

    def test_division(self) -> None:
        """Тест деления"""
        assert calculate_rpn("10 2 /") == [5.0]

    def test_not_simple_expression(self) -> None:
        """Тест сложного выражения"""
        assert calculate_rpn("5 1 2 + 4 * + 3 -") == [14]

    def test_unary_minus(self) -> None:
        """Тест унарного минуса"""
        assert calculate_rpn("5 ~") == [-5]

    def test_unary_plus(self) -> None:
        """Тест унарного плюса"""
        assert calculate_rpn("5 $") == [5]

    def test_integer_division(self) -> None:
        """Тест целочисленного деления"""
        assert calculate_rpn("7 2 //") == [3]

    def test_modulo_operation(self) -> None:
        """Тест операции modulo"""
        assert calculate_rpn("7 3 %") == [1]

    def test_power_operation(self) -> None:
        """Тест операции возведения в степень"""
        assert calculate_rpn("2 3 **") == [8]

    def test_empty_expression(self) -> None:
        """Тест пустого выражения"""
        assert calculate_rpn("") == []

    def test_only_numbers(self) -> None:
        """Тест выражения только с числами"""
        assert calculate_rpn("1 2 3") == [1, 2, 3]

    def test_simple_brackets(self) -> None:
        """Тест простых скобок"""
        assert calculate_rpn("( 1 2 + )") == [3]

    def test_nested_brackets(self) -> None:
        """Тест вложенных скобок"""
        assert calculate_rpn("( ( 1 2 + ) 3 * )") == [9]

    def test_more_brackets(self) -> None:
        """Тест нескольких скобочных выражений"""
        assert calculate_rpn("( 1 2 + ) ( 3 4 + ) *") == [21]

    def test_brackets_with_unary(self) -> None:
        """Тест скобок с унарными операциями"""
        assert calculate_rpn("( 5 ~ ) 2 *") == [-10]

    def test_not_simple_brackets_expression(self) -> None:
        """Тест сложного выражения со скобками"""
        assert calculate_rpn("1 ( 2 3 + ) 4 ( 5 6 * ) + * +") == [171]

    def test_negative_numbers(self) -> None:
        """Тест отрицательных чисел"""
        assert calculate_rpn("-5 3 +") == [-2]

    def test_decimal_numbers(self) -> None:
        """Тест дробных чисел"""
        assert calculate_rpn("1.5 2.5 +") == [4.0]

    def test_zero_operations(self) -> None:
        """Тест операций с нулем"""
        assert calculate_rpn("0 5 +") == [5]

    def test_multiple_unary_operations(self) -> None:
        """Тест нескольких унарных операций подряд"""
        assert calculate_rpn("1 $ $ 2 ~ ~ 3 ~ ~ ~") == [1, 2, -3]

    def test_complex_operator_sequence(self) -> None:
        """Тест сложной последовательности операторов"""
        assert calculate_rpn("1 2 3 + * 4 - 5 $ +") == [6]

    def test_mixed_number_types(self) -> None:
        """Тест смешанных типов чисел (int и float)"""
        assert calculate_rpn("1 2.5 3 + *") == [5.5]

    def test_whitespace_handling(self) -> None:
        """Тест обработки лишних пробелов"""
        assert calculate_rpn("  1   2   +   ") == [3]




class TestRPNCalculatorErrors:
    """Тесты обработки ошибок"""

    def test_division_by_zero(self) -> None:
        """Тест деления на ноль"""
        with pytest.raises(rpn_errors.DivisionByZeroError):
            calculate_rpn("1 0 /")

    def test_integer_division_by_zero(self) -> None:
        """Тест целочисленного деления на ноль"""
        with pytest.raises(rpn_errors.DivisionByZeroError):
            calculate_rpn("1 0 //")

    def test_modulo_by_zero(self) -> None:
        """Тест c остатком деления на ноль"""
        with pytest.raises(rpn_errors.DivisionByZeroError):
            calculate_rpn("1 0 %")

    def test_stack_underflow_binary(self) -> None:
        """Тест недостатка операторов для бинарной операции"""
        with pytest.raises(rpn_errors.StackUnderflowError):
            calculate_rpn("1 +")

    def test_stack_underflow_unary(self) -> None:
        """Тест недостатка операторов для унарной операции"""
        with pytest.raises(rpn_errors.StackUnderflowError):
            calculate_rpn("~")

    def test_invalid_token(self) -> None:
        """Тест неизвестного символа"""
        with pytest.raises(rpn_errors.InputError):
            calculate_rpn("1 2 b52")

    def test_unmatched_closing_bracket(self) -> None:
        """Тест лишней закрывающей скобки"""
        with pytest.raises(rpn_errors.BracketsError):
            calculate_rpn("1 2 + )")

    def test_unmatched_opening_bracket(self) -> None:
        """Тест незакрытой открывающей скобки"""
        with pytest.raises(rpn_errors.BracketsError):
            calculate_rpn("( 1 2 +")

    def test_incorrect_bracket_sequence(self) -> None:
        """Тест неправильной последовательности скобок"""
        with pytest.raises(rpn_errors.BracketsError):
            calculate_rpn(") (")

    def test_operation_in_brackets_without_numbers(self) -> None:
        """Тест операции в скобках без чисел"""
        with pytest.raises(rpn_errors.StackUnderflowError):
            calculate_rpn("( + )")
