import functools


def log(filename=""):
    '''Декоратор должен автоматически логировать начало и конец выполнения функции'''
    def log_decorator(func):
        @functools.wraps(func)
        def wrappers(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message_result = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as filelog:
                        filelog.write(f"{message_result}\n")
                else:
                    print(message_result)
                return result
            except Exception as e:
                message_result = f"{func.__name__} : {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as filelog:
                        filelog.write(f"{message_result}\n")
                else:
                    print(message_result)
                return None

        return wrappers

    return log_decorator


if "__main__" == __name__:

    filename = "test.log"
    filename = ""

    @log(filename)
    def sss(a: int, b: int) -> int:
        return a / b

    print(sss(3, 0))
