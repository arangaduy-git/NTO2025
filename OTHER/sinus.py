s = '8, 9, 11, 13, 14, 15, 15, 15, 14, 13, 12, 10, 8, 7, 5, 3, 2, 1, 0, 0, 0, 1, 2, 4, 6'
s = s.split(', ')
A = []
for el in s:
    A.append((4 - len(str(bin(int(el)))[2:])) * '0' + str(bin(int(el)))[2:])
for el in A:
    print('{', end='')
    for j in range(len(el)):
        if j != 3:
            print(el[j], end=', ')
        else:
            print(el[j], end='')

    print('}, ', end='')






# import math
#
# import matplotlib.pyplot as plt
#
# y = [9, 10, 11, 12, 13, 14, 15, 15, 15, 15, 14, 13, 12, 11, 9, 8, 6, 5, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 6, 8]
# x = range(len(y))
#
# plt.plot(x, y)
#
# # [0; 2p]
# for i in range(25):
#     print(round((math.sin(math.pi * 2 * i / 25) + 1) * 7.5), end=', ')
#
# plt.show()
