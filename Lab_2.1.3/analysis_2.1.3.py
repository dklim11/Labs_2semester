import matplotlib.pyplot as plt
import numpy as np

#air, frequency
delta_f = [320.2, 575.2, 917.2, 1197.2, 1477.2]
k = [1, 2, 3, 4, 5]

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += delta_f[i]/5
    x_av += k[i]/5
    y_square_av += delta_f[i]**2/5
    x_square_av += k[i]**2/5
    xy_av += delta_f[i]*k[i]/5

b = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b**2)/5) + b*0.002*np.sqrt((1/x_av)**2+(1/x_av/y_av)+(1/x_square_av)+(1/xy_av))
a = y_av - b*x_av

test = [310.2, 603.8, 897, 1191, 1484.6]

#plt.plot(k, delta_f, 'g^')
#plt.plot(k, test, 'red')
#plt.ylabel('$f_k$', rotation = 0, labelpad = 10, fontsize = 13)
#plt.xlabel('$k$', rotation = 0, labelpad = 2, fontsize = 13)
#plt.grid(True)
#plt.show()

#CO_2, freq

delta_f = [250, 480, 730, 940, 1180, 1420]
k = [1, 2, 3, 4, 5, 6]

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(6):
    y_av += delta_f[i]/6
    x_av += k[i]/6
    y_square_av += delta_f[i]**2/6
    x_square_av += k[i]**2/6
    xy_av += delta_f[i]*k[i]/6

b = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b**2)/6) + b*0.002*np.sqrt((1/x_av)**2+(1/x_av/y_av)+(1/x_square_av)+(1/xy_av))
a = y_av - b*x_av

test = [250.8, 483.6, 716.8, 949.9, 1183, 1416.2]

#plt.plot(k, delta_f, 'b^')
#plt.plot(k, test, 'green')
#plt.ylabel('$f_k$', rotation = 0, labelpad = 10, fontsize = 13)
#plt.xlabel('$k$', rotation = 0, labelpad = 2, fontsize = 13)
#plt.grid(True)
#plt.show()

#air, tube

k = [1, 2, 3, 4]
l_1 = [0.043, 0.087, 0.13, 0.176]
l_2 = [0.038, 0.079, 0.119, 0.159]
l_3 = [0.034, 0.07, 0.107, 0.142, 0.18]
l_4 = [0.033, 0.068, 0.1, 0.134, 0.168, 0.202]

f1 = 3900
f2 = 4300
f3 = 4783
f4 = 5100

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(4):
    y_av += l_1[i]/4
    x_av += k[i]/4
    y_square_av += l_1[i]**2/4
    x_square_av += k[i]**2/4
    xy_av += l_1[i]*k[i]/4

b = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b**2)/4) + b*0.002*np.sqrt((1/x_av)**2+(1/x_av/y_av)+(1/x_square_av)+(1/xy_av))
a = y_av - b*x_av

#co2, tube
k = [1, 2, 3, 4, 5, 6, 7]
l_1 = [0.051, 0.103, 0.154, 0.207]
l_2 = [0.042, 0.085, 0.129, 0.171]
l_3 = [0.039, 0.078, 0.114, 0.15]
l_4 = [0.031, 0.05, 0.092, 0.121, 0.154, 0.183, 0.213]

f1 = 2577
f2 = 3100
f3 = 3546
f4 = 4420

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(7):
    y_av += l_4[i]/7
    x_av += k[i]/7
    y_square_av += l_4[i]**2/7
    x_square_av += k[i]**2/7
    xy_av += l_4[i]*k[i]/7

b = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b**2)/7) + b*0.002*np.sqrt((1/x_av)**2+(1/x_av/y_av)+(1/x_square_av)+(1/xy_av))
a = y_av - b*x_av

test = [0]*7

for i in range(7):
    test[i] = a + b*k[i]

print(b, delta_b)
print(2*b*f4, 2*np.sqrt((f4*delta_b)**2 + (10*b)**2))

plt.plot(k, l_4, 'b^')
plt.plot(k, test, 'green')
plt.ylabel('$L_k$', rotation = 0, labelpad = 10, fontsize = 13)
plt.xlabel('$k$', rotation = 0, labelpad = 2, fontsize = 13)
plt.grid(True)
plt.show()