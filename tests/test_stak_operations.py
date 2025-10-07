import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from stack_operations import push, pop, is_empty


class TestPush:
    """Тесты для функции push"""

    def test_push_one_element(self) -> None:
        """Добвление одного элемента в стек"""
        stack: list[float] = []
        push(stack, 5.0)
        assert stack == [5.0]

    def test_push_more_elements(self) -> None:
        """Добавление нескольких элементов в стек"""
        stack: list[float] = []
        push(stack, 1.0)
        push(stack, 2)
        push(stack, 3)
        assert stack == [1.0, 2, 3]

    def test_push_negative_number(self) -> None:
        """Добавление отрицательного числа"""
        stack: list[float] = []
        push(stack, -10.5)
        assert stack == [-10.5]

    def test_push_negative_zero_positive_number(self) -> None:
        """Добавление отрицательного числа вместе с положительными и нулем"""
        stack: list[float] = []
        push(stack, -11.5)
        push(stack, 12)
        push(stack, 5.9)
        push(stack, 0)
        push(stack, -1)
        assert stack == [-11.5, 12, 5.9, 0, -1]

class TestPop:
    """Тесты для функции pop"""

    def test_pop_more_element(self) -> None:
        """Удаление нескольких элементов"""
        stack: list[float] = [1, 2, -1, -1.5, 5.9]

        assert pop(stack) == 5.9
        assert stack == [1, 2, -1, -1.5]

        assert pop(stack) == -1.5
        assert stack == [1, 2, -1]

        assert pop(stack) == -1
        assert stack == [1, 2]

        assert pop(stack) == 2
        assert stack == [1]

    def test_pop_one_element(self) -> None:
        """Удаление одного элемента"""
        stack: list[float] = [1, 3]

        assert pop(stack) == 3
        assert stack == [1]

    def test_pop_empty_stack(self) -> None:
        """Удаление из пустого стека (ожидается ошибка)"""
        stack: list[float] = []

        with pytest.raises(IndexError, match="pop from empty stack"):
            pop(stack)

class TestIsEmpty:
    """Тесты для функции is_empty"""

    def test_empty_stack(self) -> None:
        """Проверка пустого стека"""
        stack: list[float] = []
        assert is_empty(stack) is True

    def test_not_empty_stack(self) -> None:
        """Проверка не пустого стека"""
        stack: list[float] = [1, 2, 3.0]
        assert is_empty(stack) is False
