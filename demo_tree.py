# Дерево
class TreeNode:                                                 # Класс дерево
    def __init__(self, value):                                  # Конструктор
        self.value = value                                      # Создание значения узла древа
        self.left = None                                        # Указатель левого поддерева
        self.right = None                                       # Указатель правого поддерева

    def insert_left(self, value):                               # Функция добавления левого поддерева
        self.left = TreeNode(value)                             # Создание левого поддерева
        return self.left                                        # Возвращаем левое поддерево

    def insert_right(self, value):                              # Функция добавления правого поддерева
        self.right = TreeNode(value)                            # Создание правого поддерева
        return self.right                                       # Возвращаем правое поддерево

# Пример работы с деревом
root = TreeNode(1)                                              # Создаем корень со значением 1
root.insert_left(2)                                             # Добавляем левое поддерево со значением 2
root.insert_right(3)                                            # Добавляем правое поддерево со значением 3
root.left.insert_left(4)                                        # Добавляем левое поддерево (4) левому поддереву
root.left.insert_right(5)                                       # Добавляем правое поддерево (5) левому поддереву

print("Корень дерева:", root.value)                             # Выводим корень
print("Левое поддерево корня:", root.left.value)                # Выводим левое поддерево
print("Правое поддерево корня:", root.right.value)              # Выводим правое поддерево