import matplotlib
matplotlib.use("TkAgg")  # <-- добавь это

import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Пример алгоритма (O(n^2))
def my_algorithm(data):
    total = 0
    for i in data:
        for j in data:
            total += i * j
    return total

# Замер времени выполнения
def measure_time(func, sizes):
    times = []
    for n in sizes:
        data = list(range(n))
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
        print(f"n={n:<6} time={end - start:.6f} сек")
    return np.array(times)

# Потенциальные функции сложности
def O_n(x, a): return a * x
def O_nlogn(x, a): return a * x * np.log2(x)
def O_n2(x, a): return a * x**2

# Основной запуск
sizes = np.array([100, 200, 400, 800])
times = measure_time(my_algorithm, sizes)

# Подгонка каждой функции
popt_n, _ = curve_fit(O_n, sizes, times)
popt_nlogn, _ = curve_fit(O_nlogn, sizes, times)
popt_n2, _ = curve_fit(O_n2, sizes, times)

# Построение графика
plt.plot(sizes, times, 'o', label='Замеренные данные')
plt.plot(sizes, O_n(sizes, *popt_n), label='O(n)')
plt.plot(sizes, O_nlogn(sizes, *popt_nlogn), label='O(n log n)')
plt.plot(sizes, O_n2(sizes, *popt_n2), label='O(n^2)')

plt.xlabel("Размер входных данных (n)")
plt.ylabel("Время выполнения (сек)")
plt.title("Эмпирическая оценка сложности алгоритма")
plt.legend()
plt.grid(True)
plt.show()
