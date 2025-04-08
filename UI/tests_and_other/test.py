import matplotlib.pyplot as plt

# Создание данных для графиков
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Создание первого графика
plt.subplot(2, 1, 1) # указываем 2 строки, 1 столбец, выбираем первое место
plt.plot(x, y1)
plt.title('График 1')

# Создание второго графика
plt.subplot(2, 1, 2) # указываем 2 строки, 1 столбец, выбираем второе место
plt.plot(x, y2)
plt.title('График 2')

plt.show()
