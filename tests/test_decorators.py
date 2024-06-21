import pytest
from src.decorators import log


@log()
def add(x, y):
    """
    Функция сложения двух чисел.

    Args:
        x (int): Первое число.
        y (int): Второе число.

    Returns:
        int: Сумма x и y.
    """
    return x + y


@log()
def divide(x, y):
    """
    Функция деления двух чисел.

    Args:
        x (int): Делимое.
        y (int): Делитель.

    Returns:
        float: Результат деления x на y.

    Raises:
        ZeroDivisionError: Если y равен нулю.
    """
    return x / y


def test_log_function_call_and_result(capsys):
    """
    Тестирование логирования успешного вызова функции.

    Args:
        capsys: Фикстура для захвата вывода.
    """
    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.err.strip()


def test_log_function_error(capsys):
    """
    Тестирование логирования ошибки вызова функции.

    Args:
        capsys: Фикстура для захвата вывода.
    """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    expected_output = "divide error: division by zero. Inputs: (1, 0), {}"
    assert expected_output in captured.err.strip()


def test_log_to_file(tmp_path):
    """
    Тестирование логирования вызова функции и ошибки в файл.

    Args:
        tmp_path: Фикстура для создания временного пути.
    """
    log_filename = tmp_path / "test_log.txt"

    @log(filename=str(log_filename))
    def add_to_file(x, y):
        """
        Функция сложения двух чисел с логированием в файл.

        Args:
            x (int): Первое число.
            y (int): Второе число.

        Returns:
            int: Сумма x и y.
        """
        return x + y

    @log(filename=str(log_filename))
    def divide_to_file(x, y):
        """
        Функция деления двух чисел с логированием в файл.

        Args:
            x (int): Делимое.
            y (int): Делитель.

        Returns:
            float: Результат деления x на y.

        Raises:
            ZeroDivisionError: Если y равен нулю.
        """
        return x / y

    # Test function call
    add_to_file(4, 2)
    with open(log_filename, "r") as f:
        log_content = f.read()
        assert "add_to_file ok" in log_content

    # Test function error
    try:
        divide_to_file(1, 0)
    except ZeroDivisionError:
        pass  # Catch the error so we can check the log file

    with open(log_filename, "r") as f:
        log_content = f.read()
        expected_output = "divide_to_file error: division by zero. Inputs: (1, 0), {}"
        assert expected_output in log_content
