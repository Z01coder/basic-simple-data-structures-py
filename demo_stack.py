# Реализация стека
class Stack:                                                        # Класс стек
    def __init__(self):                                             # Конструктор
        self.stack = []                                             # Стек

    def push(self, item):                                           # Функция добавления элемента
        self.stack.append(item)                                     # Добавляем элемент в стек

    def pop(self):                                                  # Функция удаления элемента
        return self.stack.pop() if not self.is_empty() else None    # Удаляем элемент из стека

    def peek(self):                                                 # Функция получения верхнего элемента
        return self.stack[-1] if not self.is_empty() else None      # Вернуть верхний элемент

    def is_empty(self):                                             # Функция проверки пустого стека
        return len(self.stack) == 0                                 # Проверяем пуст ли стек

# Пример работы со стеком
stack = Stack()                                                     # Создаем экземпляр стека
stack.push(1)                                                       # Добавляем элементы
stack.push(2)
stack.push(3)
print("Стек после добавления элементов:", stack.stack)              # Выводим стек
print("Верхний элемент стека:", stack.peek())                       # Выводим верхний элемент
stack.pop()                                                         # Удаляем верхний элемент
print("Стек после удаления элемента:", stack.stack)                 # Снова выводим стек