# Граф
class Graph:                                                                    # Класс граф
    def __init__(self):                                                         # Конструктор
        self.adjacency_list = {}                                                # Словарь для хранения списка смежности

    def add_vertex(self, vertex):                                               # Функция добавления вершины
        if vertex not in self.adjacency_list:                                   # Если вершины нет в списке
            self.adjacency_list[vertex] = []                                    # То создаем список смежности

    def add_edge(self, vertex1, vertex2):                                       # Функция добавления ребра
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:   # Если вершины есть в списке
            self.adjacency_list[vertex1].append(vertex2)                        # То добавляем ребро
            self.adjacency_list[vertex2].append(vertex1)                        # Второе ребро, чтобы получился неориентированный граф

    def display(self):                                                          # Функция вывода
        for vertex, edges in self.adjacency_list.items():                       # Проходим по всем вершинам
            print(f"{vertex}: {edges}")                                         # Выводим список смежности

# Пример работы с графом
graph = Graph()                                                                 # Создаем экземпляр графа
for vertex in range(1, 5):                                                      # Добавляем вершины
    graph.add_vertex(vertex)                                                    # Добавляем вершину

graph.add_edge(1, 2)                                              # Добавляем ребра
graph.add_edge(1, 3)
graph.add_edge(3, 4)
print("Граф:")                                                                  # Выводим надпись сначала
graph.display()                                                                 # Теперь выводим сам граф