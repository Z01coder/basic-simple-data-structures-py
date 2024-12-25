# Реализация очереди
from collections import deque                                           # Импортируем deque для удобства работы с очередью

class Queue:                                                            # Класс очередь
    def __init__(self):                                                 # Конструктор
        self.queue = deque()

    def enqueue(self, item):                                            # Функция добавления элемента
        self.queue.append(item)                                         # Добавляем элемент в очередь

    def dequeue(self):                                                  # Функция удаления элемента
        return self.queue.popleft() if not self.is_empty() else None    # Удаляем элемент из очереди

    def is_empty(self):                                                 # Функция проверки пустой очереди
        return len(self.queue) == 0                                     # Проверяем пуста ли очередь

# Пример работы с очередью
queue = Queue()                                                         # Создаем экземпляр очереди
queue.enqueue(1)                                                        # Добавляем элементы
queue.enqueue(2)
queue.enqueue(3)
print("Очередь после добавления элементов:", list(queue.queue))         # Выводим очередь
queue.dequeue()                                                         # Удаляем элемент
print("Очередь после удаления элемента:", list(queue.queue))            # Снова выводим очередь