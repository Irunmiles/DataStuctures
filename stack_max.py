#https://stepik.org/lesson/41234/step/4

import sys

class Stack:
    def __init__(self):
        self._cup = []
        self._cup_max = []
        self._max = -float('inf')

    def push_it(self, element):
        self._cup.append(element)
        if element > self._max:
            self._cup_max.append(element)
            self._max = element
        else:
            self._cup_max.append(self._max)

    def pop_it(self):
        if self._cup != []:
            self._cup_max.pop()
            if self._cup_max != []:
                self._max = self._cup_max[-1]
            else:
                self._max = -float('inf')
            return self._cup.pop()
        else:
            return None

    def max_it(self):
        return self._max

my_stack = Stack()
n = int(next(sys.stdin))
for command in sys.stdin:
    if command.startswith('push'):
        _, num = command.split()
        my_stack.push_it(int(num))
    if command.startswith('pop'):
        my_stack.pop_it()
    if command.startswith('max'):
        res = my_stack.max_it()
        if res != -float('inf'):
            print(res)
        else:
            print('None')

