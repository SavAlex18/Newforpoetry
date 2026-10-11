import functools

def log(filename=''):
    def log_decorator(func):
        @functools.wraps(func)
        def wrappers(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message_result = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding='utf-8') as filelog:
                        filelog.write(f"{message_result}\n")
                else:
                    print(message_result)
                return result

            except Exception as e:
                message_result = f"{func.__name__} : {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding='utf-8') as filelog:
                        filelog.write(f"{message_result}\n")
                else:
                    print(message_result)
                return message_result
        return wrappers
    return log_decorator


# filename = 'aa.log'
# @log(filename)
# def sss(a: int, b: int) -> int:
#     return a / b
#
# print(sss(3, 0))

# from functools import wraps
# import pytest
#
# def new_with_psrsm(word_len = 8, symb = '.'):
#     def trunc_txt(ffunc):
#         def inner(*args, **kwargs):
#             result = ffunc(*args, **kwargs)
#             if type(result) == str:
#                 l_result = result.split(' ')
#                 ll = ' '.join([ x[:word_len] + symb if len(x) > word_len else x for x in l_result ])
#                 return ll
#             else:
#                 return None
#         return inner
#     return trunc_txt
#
#
# #if "__main__" == __name__:
#
# @new_with_psrsm()
# def func():
#     return "weasdfasdf asdfad fasdfadf fdsasdfd fsdfasdf asdfadf"
#
#
# # print(func())
#
# def test_new_with_psrsm():
#     assert func() == 'weasdfas. asdfad fasdfadf fdsasdfd fsdfasdf asdfadf'
#
#
# def test_new_ehds():
#     @new_with_psrsm(word_len = 3, symb = '!!')
#     def func():
#         return "weasdfasdf asdfad fasdfadf fdsasdfd fsdfasdf asdfadf"
#
#     assert func() == 'wea!! asd!! fas!! fds!! fsd!! asd!!'

# def check_that_args_is(predicate, error_message):
#     def wrapper(function):
#         @wraps(function)
#         def inner(arg):
#             if not predicate(arg):
#                 raise ValueError(error_message)
#             return function(arg)
#         return inner
#     return wrapper
#
#
# def predicate_is_int(x):
#     return type(x) == int
#
#
# def predicate_is_positive(x):
#     return x > 0
#
#
# @check_that_args_is(predicate_is_int, 'Значение должно быть целым числом!')
# @check_that_args_is(predicate_is_positive, 'Число должно быть положительным')
# def square(x):
#     """Возведение числа в квадрат """
#     return x * x
#
#
# if __name__ == '__main__':
#     with pytest.raises(ValueError, match='Число должно быть положительным'):
#         square(-3)
#
#
# #    print(help(square))
# #    print(square(3))
# #    print(square('3'))
#
#
#
#
# # def logs(func):
# #     def wrapper(*args, **kwargs):
# #         pass
# #     return wrapper

