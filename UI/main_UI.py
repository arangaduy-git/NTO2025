import random
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation

npoints = 52  # кол-во точек на графике
x = deque([0], maxlen=npoints)
y_signal_unfiltered = deque([0], maxlen=npoints)
y_signal_filtered = deque([0], maxlen=npoints)

fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(15, 7))
plot_unfiltered_analog_summer = axs[0][0]
plot_filtered_analog_summer = axs[0][1]
text_info = axs[0][2]
amplitude_frequency_unfiltered_analog_summer = axs[1][0]
amplitude_frequency_filtered_analog_summer = axs[1][1]
output_signal = axs[1][2]

plot_unfiltered_analog_summer.set_title('Аналоговый сумматор до фильтрации')
plot_filtered_analog_summer.set_title('Аналоговый сумматор после фильтрации')
text_info.set_title('Текстовая информация')
amplitude_frequency_unfiltered_analog_summer.set_title('Амплитудно-частотная до фильтрации')
amplitude_frequency_filtered_analog_summer.set_title('Амплитудно-частотная после фильтрации')
output_signal.set_title('Выходной сигнал')


plot_unfiltered_analog_summer.set(xlabel='Время', ylabel='Напряжение')
plot_filtered_analog_summer.set(xlabel='Время', ylabel='Напряжение')
[line_unfiltered_analog_summer] = plot_unfiltered_analog_summer.step(x, y_signal_unfiltered)
[line_filtered_analog_summer] = plot_filtered_analog_summer.step(x, y_signal_filtered)
plt.subplots_adjust(wspace=0.4, hspace=0.6)


def update(dy):
    x.append(x[-1] + 0.1)  # update data
    y_signal_unfiltered.append(dy)
    y_signal_filtered.append(-dy)

    line_unfiltered_analog_summer.set_xdata(x)  # update plot data
    line_unfiltered_analog_summer.set_ydata(y_signal_unfiltered)

    line_filtered_analog_summer.set_xdata(x)  # update plot data
    line_filtered_analog_summer.set_ydata(y_signal_filtered)

    plot_filtered_analog_summer.set_yticks(np.arange(-2, 2 + 0.5, 0.5))
    plot_unfiltered_analog_summer.set_yticks(np.arange(-2, 2 + 0.5, 0.5))

    text_info.clear()
    text_info.set_yticks([])
    text_info.set_xticks([])
    text_info.text(0.1, 0.77, f'Коэффициент пульсации: {round(dy, 3)}', fontsize=10)
    text_info.text(0.1, 0.57, f'Сила тока: {round(dy, 3)}А', fontsize=10)
    text_info.text(0.1, 0.37, f'Напряжение: {round(dy, 3)}В', fontsize=10)
    text_info.text(0.1, 0.17, f'Мгновенная мощность: {round(dy, 3)}Вт', fontsize=10)

    plot_unfiltered_analog_summer.relim()
    plot_filtered_analog_summer.relim()

    plot_unfiltered_analog_summer.autoscale_view(False, True, False)
    plot_filtered_analog_summer.autoscale_view(False, True, False)

    return line_unfiltered_analog_summer, plot_unfiltered_analog_summer, plot_filtered_analog_summer


def data_gen():
    while True:
        yield random.random() * 3 - 1.5


ani = animation.FuncAnimation(fig, update, data_gen, interval=0.2)
plt.show()
