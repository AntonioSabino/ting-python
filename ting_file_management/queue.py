class Queue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        return self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        length = len(self._queue)
        if 0 <= index < length:
            return self._queue[index]
        raise IndexError("Index out of range")
