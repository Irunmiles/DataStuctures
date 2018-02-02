import sys

class FLQueue:
    def __init__(self, size):
        self._max_size = size
        self._curr_size = 0
        self._data = []

    def push(self, x):
        self._data.insert(0, x)
        self._curr_size += 1

    def pop(self):
        self._curr_size -= 1
        return self._data.pop()

    def first_out(self):
        return self._data[-1]

    def last_out(self):
        return self._data[0]

    def is_full(self):
        return self._curr_size == self._max_size

    def is_empty(self):
        return self._curr_size == 0

size, n = map(int, next(sys.stdin).split())
queue = FLQueue(size)
for i in range(n):
    arrival, duration = map(int, next(sys.stdin).split())
    if not queue.is_empty():
        if queue.first_out() <= arrival:
            t = max(queue.last_out(), arrival)
            print(t)
            queue.pop() 
            queue.push(t + duration)
        else:
            if not queue.is_full():
                t = queue.last_out()
                print(t)
                queue.push(t + duration)
            else:
                print(-1)
    else:
        print(arrival)
        queue.push(arrival + duration)

