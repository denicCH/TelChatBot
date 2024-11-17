from collections import deque
from typing import List


class Queue_U:
    def __init__(self, items: List | None = None):
        # Инициализация очереди с использованием deque
        self.queue = deque()
        if items is not None:
            self.enqueue(*items)

    def enqueue(self, *items):
        """Добавляет несколько элементов в конец очереди."""
        self.queue.extend(items)


    def delqueue(self):
        """Удаляет элемент из начала очереди и возвращает его.
        Если очередь пуста, возвращает None."""
        if not self.is_empty():
            item = self.queue.popleft()
            print(f"Элемент {item} удален из очереди.")
            return item
        else:
            print("Очередь пуста.")
            return None

    def dequeue_n(self, n):
        """Удаляет и возвращает первые n элементов очереди.
        Если элементов меньше, чем n, возвращает все доступные элементы."""
        removed_elements = []
        for _ in range(min(n, len(self.queue))):  # Ограничиваем количество итераций длиной очереди
            removed_elements.append(self.queue.popleft())  # Удаляем и добавляем в результат
        return removed_elements

    def peek(self):
        """Возвращает элемент из начала очереди без удаления.
        Если очередь пуста, возвращает None."""
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Очередь пуста.")
            return None

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.queue) == 0

    def size(self):
        """Возвращает размер очереди."""
        return len(self.queue)

    def display(self):
        """Печатает текущее состояние очереди."""
        print("Состояние очереди:", list(self.queue))



