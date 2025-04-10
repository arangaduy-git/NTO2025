from collections import deque
import serial
import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation

npoints = 30
x = deque([0], maxlen=npoints)
y = deque([0], maxlen=npoints)
fig, ax = plt.subplots()
ser = serial.Serial('COM4', 115200)
[line] = ax.step(x, y)


def get_int(line):
    line = line.rstrip().split('|')
    A = []
    for i in range(len(line)):
        ch = ''
        for j in range(len(line[i])):
            if line[i][j] in '0123456789':
                ch += line[i][j]
        if ch == '':
            ch = -10
        A.append(int(ch))
    return A


def update(frame):
    try:
        line_received = ser.readline().decode("utf-8")
        inted = get_int(line_received)[0]
        print(inted)
        x.append(x[-1] + 1)  # update data
        y.append(inted)

        line.set_xdata(x)  # update plot data
        line.set_ydata(y)

        ax.relim()  # update axes limits
        ax.autoscale_view(True, True, True)
    except:
        print('error')
    return line, ax


ani = animation.FuncAnimation(fig, func=update, interval=1)
plt.show()
