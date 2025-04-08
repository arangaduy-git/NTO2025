import random
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation

npoints = 52  # кол-во точек на графике
x = deque([0], maxlen=npoints)
y_signal_unfiltered = deque([0], maxlen=npoints)
y_signal_filtered = deque([0], maxlen=npoints)

fig, (plot_unfiltered, plot_filtered) = plt.subplots(ncols=2, sharey=True, figsize=(11, 5))
plot_unfiltered.set_title('До фильтрации')
plot_filtered.set_title('После фильтрации')
plot_unfiltered.set(xlabel='Время', ylabel='Напряжение')
plot_filtered.set(xlabel='Время')
[line_unfiltered] = plot_unfiltered.step(x, y_signal_unfiltered)
[line_filtered] = plot_filtered.step(x, y_signal_filtered)


def update(dy):
    x.append(x[-1] + 0.1)  # update data
    y_signal_unfiltered.append(dy)
    y_signal_filtered.append(-dy)

    line_unfiltered.set_xdata(x)  # update plot data
    line_unfiltered.set_ydata(y_signal_unfiltered)

    line_filtered.set_xdata(x)  # update plot data
    line_filtered.set_ydata(y_signal_filtered)

    plt.yticks(np.arange(-2, 2 + 0.5, 0.5), minor=False)
    plot_unfiltered.relim()  # update axes limits
    plot_filtered.relim()
    plot_unfiltered.autoscale_view(False, True, False)
    plot_filtered.autoscale_view(False, True, False)
    return line_unfiltered, plot_unfiltered, plot_filtered


def data_gen():
    while True:
        yield random.random() * 3 - 1.5


ani = animation.FuncAnimation(fig, update, data_gen, interval=0.01)
plt.show()
