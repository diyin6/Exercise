#! /usr/bin/env python
# -*-coding:utf-8 -*-

class Fib:
    def __init__(self):
        self._a = 1
        self._b = 1
    def __iter__(self):
        return self
    def next(self):
        if self._a > 300:
            raise StopIteration('终止了')
        self._a,self._b=self._b,self._a + self._b
        return self._a

f1 = Fib()

print next(f1)
print next(f1)


for i in f1:
    print(i)