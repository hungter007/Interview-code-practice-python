# use __new__ for singleton
# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class Myclass(Singleton):
#     a = 1

# use Decorator
# def singleton(cls):
#     instance = {}
#
#     def decorator(*args, **kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
#         return instance[cls]
#     return decorator
#
# @singleton
# class Myclass:
#     a = 1


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("Singleton.__call__　is called")
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            print(cls.__instance)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):
    def __new__(cls, *args):
        print("Spam.__new__ is called")
        return super().__new__(cls)

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Creating spam")


s1 = Spam(1, 2)
