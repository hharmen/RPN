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
