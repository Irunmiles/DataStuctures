#https://stepik.org/lesson/41234/step/5

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

#--- --- ---

class Queue:
    def __init__(self):
        self.left_cup = Stack()
        self.right_cup = Stack()

    def push_left(self, element):
        self.left_cup.push_it(element)


    def pop_right(self):
        if self.right_cup._cup == []:
            for i in range(len(self.left_cup._cup)):
                curr = self.left_cup.pop_it()
                self.right_cup.push_it(curr)
        return self.right_cup.pop_it()

    def get_max(self):
        return max(self.left_cup._max, self.right_cup._max)

#--- --- ---

import sys

n = int(next(sys.stdin))
data = [int(num) for num in next(sys.stdin).split()]
m = int(next(sys.stdin))

window = Queue()
for i in range(m):
    window.push_left(data[i])

res = [window.get_max()]
for i in range(m, n):
    window.push_left(data[i])
    window.pop_right()
    res.append(window.get_max())
print(*res)
