import serial

ser = serial.Serial('COM3', 115200)


def get_int(line):
    ch = ''
    for i in range(len(line)):
        if line[i] in '0123456789':
            ch += line[i]
    if ch == '':
        return None
    return int(ch)


while True:
    line = ser.readline().decode("utf-8")
    # line = ser.readline().decode("utf-8").replace('\n', '').replace('\r', '')
    print(get_int(line))