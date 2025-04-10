import sys
from threading import Thread, Lock
import serial
import time


def serial_com(ser, locker: Lock):
    global last_received
    lines = []
    while True:
        line = ser.readline()
        lines.append(line.decode('utf-8').rstrip())
        if len(lines) > 10:
            lines = lines[-6:-1]
        locker.acquire()
        last_received = lines[-1]
        locker.release()


try:
    serial_port = serial.Serial('COM4', baudrate=115200, timeout=1)
except serial.SerialException as e:
    print("could not open serial port: {}".format(e))
    sys.exit(0)

last_received = ''
lock = Lock()
Thread(target=serial_com, args=(serial_port, lock, )).start()

while True:
    lock.acquire()
    print(last_received)
    lock.release()
    time.sleep(0.5)
