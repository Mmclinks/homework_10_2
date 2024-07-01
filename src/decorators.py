import functools
import logging
from typing import Any, Callable, Dict, Optional, Tuple


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызова функции и ее результата.

    Логирует вызов функции и ее результат в файл или в консоль.
    Если вызов функции закончился ошибкой, записывает сообщение об ошибке и входные параметры функции.

    Args:
        filename (Optional[str]): Путь к файлу для записи логов. Если не задан, логи выводятся в консоль.

    Returns:
        Callable: Обернутая функция с логированием.
    """

    def decorator_log(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Декоратор для обертывания функции логированием.

        Args:
            func (Callable): Функция для обертывания.

        Returns:
            Callable: Обернутая функция с логированием.
        """

        @functools.wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            """
            Обертка для выполнения логики логирования.

            Args:
                *args: Позиционные аргументы для оборачиваемой функции.
                **kwargs: Именованные аргументы для оборачиваемой функции.

            Returns:
                Результат выполнения оборачиваемой функции.

            Raises:
                Exception: Исключение, возникшее при выполнении оборачиваемой функции.
            """
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(message)s')

            handler: logging.Handler
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()

        return wrapper

    return decorator_log
