'''cons of Singleton usage:
1. Singletons introduce a global state into an application, which can lead to code that is hard to understand and maintain.
Global state can create hidden dependencies and make it difficult to track down the cause of bugs.

2. Singletons can make unit testing difficult. Since they control their own lifecycle, it can be hard to reset their
state between tests, leading to unpredictable test results and making tests dependent on execution order.

3. If a Singleton is not implemented with thread safety in mind, it can lead to concurrency issues in multi-threaded
applications. Ensuring thread safety often adds complexity to the implementation.

4. Violation of Single Responsibility Principle:
By controlling both the instantiation and the global access point, a Singleton can violate the
Single Responsibility Principle, one of the SOLID principles of object-oriented design.

5. Lack of Scalability:
Singletons can become a bottleneck in applications where multiple instances would be beneficial for performance or
scalability reasons, such as in a distributed system.
...

'''
from typing import List


# class Logger:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     def __init__(self):
#         self.log_book = []
#
#     def add_log(self, message):
#         self.log_book.append(message)
#
#     def print_logs(self):
#         print(*self.log_book, sep='\n')
#
#
# logger1 = Logger()
# logger2 = Logger()
#
# logger1.add_log("Message added from the logger1.")
# logger1.print_logs()
# print('________________________________________________________________________')
# logger2.add_log("This is another log message added from the logger2.")
# logger2.print_logs()
#
# print(logger1 is logger2)


# object pool

class Reusable:
    def test(self):
        print(f"Using object {id(self)}")


class ReusablePool:

    def __init__(self, size):
        self.size = size
        self.free: List[Reusable] = []
        self.in_use: List[Reusable] = []
        for _ in range(0, size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        assert len(self.free) > 0
        reusable_inst = self.free[0]
        self.free.remove(reusable_inst)
        self.in_use.append(reusable_inst)
        return reusable_inst

    def release(self, reusable_inst: Reusable):
        self.in_use.remove(reusable_inst)
        self.free.append(reusable_inst)


pool = ReusablePool(2)
r = pool.acquire()
r2 = pool.acquire()

r.test()
r2.test()

pool.release(r2)
r3 = pool.acquire()
r3.test()
