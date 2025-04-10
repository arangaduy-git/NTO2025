import scipy
import serial
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial('COM4', 115200)
npoints = 256  # кол-во точек на графике
x = deque([0], maxlen=npoints)
y_signal_unfiltered = deque([0], maxlen=npoints)
y_signal_filtered = deque([0], maxlen=npoints)

fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(15, 7))
plot_unfiltered_analog_summer = axs[0][0]
plot_filtered_analog_summer = axs[0][1]
output_signal = axs[0][2]
amplitude_frequency_unfiltered_analog_summer = axs[1][0]
amplitude_frequency_filtered_analog_summer = axs[1][1]
text_info = axs[1][2]

plot_unfiltered_analog_summer.set_title('Аналоговый сумматор до фильтрации')
plot_filtered_analog_summer.set_title('Аналоговый сумматор после фильтрации')
text_info.set_title('Текстовая информация')
amplitude_frequency_unfiltered_analog_summer.set_title('Амплитудно-частотная до фильтрации')
amplitude_frequency_filtered_analog_summer.set_title('Амплитудно-частотная после фильтрации')
output_signal.set_title('Выходной сигнал')


plot_unfiltered_analog_summer.set(xlabel='Время', ylabel='Напряжение')
plot_filtered_analog_summer.set(xlabel='Время', ylabel='Напряжение')
amplitude_frequency_unfiltered_analog_summer.set(xlabel='Частота', ylabel='Амплитуда')
text_info.set_yticks([])
text_info.set_xticks([])
[line_unfiltered_analog_summer] = plot_unfiltered_analog_summer.step(x, y_signal_unfiltered)
[line_filtered_analog_summer] = plot_filtered_analog_summer.step(x, y_signal_filtered)
plt.subplots_adjust(wspace=0.4, hspace=0.6)


def get_ints(line):
    line = line.rstrip().split('|')
    A = []
    for i in range(len(line)):
        ch = ''
        for j in range(len(line[i])):
            if line[i][j] in '0123456789':
                ch += line[i][j]
            if line[i][j] == '.':
                ch += '.'
        if ch == '':
            ch = 0
        A.append(float(ch))
    if len(A) < 3:
        return None
    return A


def fourier(y):
    Fs = 8000
    n = len(y)  # length of the signal
    k = np.arange(n)
    T = n / Fs
    frq = k / T  # two sides frequency range
    frq = frq[range(n // 2)]  # one side frequency range

    Y = scipy.fft.fft(y) / n  # fft computing and normalization
    Y = Y[range(n // 2)]
    return frq, abs(Y)


def update(dy):
    try:
        line_received = ser.readline().decode("utf-8")
        inted = get_ints(line_received)
        if inted:
            x.append(x[-1] + 1)  # update data
            if inted[0] > 5.5:
                print(line_received)
            y_signal_unfiltered.append(inted[0])
            y_signal_filtered.append(inted[1])

            line_unfiltered_analog_summer.set_xdata(x)  # update plot data
            line_unfiltered_analog_summer.set_ydata(y_signal_unfiltered)

            line_filtered_analog_summer.set_xdata(x)  # update plot data
            line_filtered_analog_summer.set_ydata(y_signal_filtered)

            plot_filtered_analog_summer.set_yticks(np.arange(-0.5, 5 + 1, 0.5))
            plot_unfiltered_analog_summer.set_yticks(np.arange(-0.5, 5 + 1, 0.5))

            frq_unfiltered, frq_Y_unfiltered = fourier(y_signal_unfiltered)
            amplitude_frequency_unfiltered_analog_summer.clear()
            amplitude_frequency_unfiltered_analog_summer.set(xlabel='Частота', ylabel='Амплитуда')
            amplitude_frequency_unfiltered_analog_summer.set_title('Амплитудно-частотная до фильтрации')
            amplitude_frequency_unfiltered_analog_summer.plot(frq_unfiltered, frq_Y_unfiltered, 'r')

            frq_filtered, frq_Y_filtered = fourier(y_signal_filtered)
            amplitude_frequency_filtered_analog_summer.clear()
            amplitude_frequency_filtered_analog_summer.set(xlabel='Частота', ylabel='Амплитуда')
            amplitude_frequency_filtered_analog_summer.set_title('Амплитудно-частотная после фильтрации')
            amplitude_frequency_filtered_analog_summer.plot(frq_filtered, frq_Y_filtered, 'r')

            # text_info.clear()
            # text_info.set_yticks([])
            # text_info.set_xticks([])
            # text_info.text(0.1, 0.77, f'Коэффициент пульсации: {round(dy, 3)}', fontsize=10)
            # text_info.text(0.1, 0.57, f'Сила тока: {round(dy, 3)}А', fontsize=10)
            # text_info.text(0.1, 0.37, f'Напряжение: {round(dy, 3)}В', fontsize=10)
            # text_info.text(0.1, 0.17, f'Мгновенная мощность: {round(dy, 3)}Вт', fontsize=10)

            plot_unfiltered_analog_summer.relim()
            plot_filtered_analog_summer.relim()

            plot_unfiltered_analog_summer.autoscale_view(False, True, False)
            plot_filtered_analog_summer.autoscale_view(False, True, False)
        else:
            print('skipped:', line_received)
    except Exception as e:
        print('ERROR:', e)

    return line_unfiltered_analog_summer, plot_unfiltered_analog_summer, plot_filtered_analog_summer


ani = animation.FuncAnimation(fig, func=update, interval=3)
plt.show()