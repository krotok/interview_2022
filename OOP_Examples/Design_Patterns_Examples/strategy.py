#Применяется когда нужно легко выбрать одно из возможных действиий
#1. Выбрать алгоритм сортировки
#2. Выбрать способ оплаты
#3. Выбрать подключиться к реальному сетвису или к тестовому МОК
#4. Выбрать маршрут навигавции
#5. Выбрать формат воода или выводаданных
#6. Выбрать Алгоритм авторизации:токены, Basic Auth, cookie
#7. Выбрать путь для навигатора: красивый или короткий или быстрый

##############################
class SortStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Bubble Sort")

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Quick Sort")

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data):
        self.strategy.sort(data)

sorter = Sorter(QuickSort())
sorter.sort([1, 2, 3])  # Quick Sort



