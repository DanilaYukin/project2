from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор который логирует функцию и ее результат в файл или консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok\n"

            except Exception as e:
                result = None
                log_message = f"my_function error: {e}. Inputs {args}, {kwargs} \n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                raise
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def function(x, y):
    return x / y


if __name__ == "__main__":
    print(function(2, 0))
