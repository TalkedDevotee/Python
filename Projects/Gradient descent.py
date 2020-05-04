import numpy as np
import matplotlib.pyplot as pl
from prettytable import PrettyTable

# Основная функция
def func(x, y):
    return np.tan(y) + (np.abs(x) ** (1 / y))

# Диффиренциал по переменной x
def df_x(x, y):
    return (np.abs(x) ** ((1 / y) - 1)) / y

# Дифференциал по переменной y
def df_y(x, y):
    return (1 / (np.cos(y) ** 2)) - (((np.abs(x) ** (1 / y)) * np.log(x)) / (np.abs(y) ** 2))

# Градиентный спуск
def grad(x, y, Lambda, epoches, plot_2d, x_3d, y_3d, dir):
    th = ['x', 'y', 'dx', 'dy', 'function']
    table = PrettyTable(th)
    for epoch in range(epoches):
        dx, dy, f = df_x(x, y), df_y(x, y), func(x, y)
        td = ["{x0:.4f}".format(x0=x), "{y0:.4f}".format(y0=y), "{dx0:.4f}".format(dx0=dx), "{dy0:.4f}".format(dy0=dy), "{f0:.4f}".format(f0=f)]
        td_data = td[:]

        while td_data:
            table.add_row(td_data[:10])
            td_data = td_data[10:]

        x -= Lambda * dx * dir
        y -= Lambda * dy * dir

        plot_2d.append(f)
        x_3d.append(x)
        y_3d.append(y)

    print(table)

# Ввод переменных x и y
x = float(input("Введите x: "))
y = float(input("Введите y: "))
Lambda = float(input("Введите лямбду: "))
epoches = int(input("Введите количество эпох: "))

# Создаем массивы по f(x, y) для 2D графика (точки максимума/минимума)
plot_max = []
plot_min = []

# Создаем массивы коордиант для создания 3D графика
x_max, y_max = [], []
x_min, y_min = [], []
print("\t\t\t\tНахождение максимума")
grad(x, y, Lambda, epoches, plot_max, x_max, y_max, -1)
print()
print("\t\t\t\tНахождение минимума")
grad(x, y, Lambda, epoches, plot_min, x_min, y_min, 1)

# График 2D
pl.plot(plot_max, label='max')
pl.plot(plot_min, label='min')
pl.xlabel("Количество эпохов")
pl.ylabel("f(x, y)")
pl.title('f(x, y) = tan(y) + pow(x, 1/y)')
pl.legend()
pl.grid()

# График 3D
x_max, y_max = np.meshgrid(x_max, y_max)
x_min, y_min = np.meshgrid(x_min, y_min)

fig = pl.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('X', fontsize=10)
ax.set_ylabel('Y', fontsize=10)
ax.set_zlabel('f(x, y)', fontsize=10)
ax.set_title('Точки максимума')
ax.plot_surface(x_max, y_max, func(x_max, y_max), cmap='Blues', alpha=0.8)
ax.view_init(35, 30)

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_xlabel('X', fontsize=10)
ax.set_ylabel('Y', fontsize=10)
ax.set_zlabel('f(x, y)', fontsize=10)
ax.set_title('Точки минимума')
ax.plot_surface(x_min, y_min, func(x_min, y_min), cmap='Oranges', alpha=0.8)
ax.view_init(35, 30)
pl.show()