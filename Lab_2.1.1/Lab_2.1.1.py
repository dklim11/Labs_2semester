import numpy as np
import matplotlib.pyplot as plt

#first expenditure
T1 = [1.13, 1.6, 2.11, 2.73, 3.49]
IU1 = [0.30051, 0.41935, 0.56408, 0.72706, 0.9186]

m = 0.234

for i in range(5):
    T1[i] *= m

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += IU1[i]/5
    x_av += T1[i]/5
    y_square_av += IU1[i]**2/5
    x_square_av += T1[i]**2/5
    xy_av += T1[i]*IU1[i]/5

k = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_k = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - k**2)/5)
a = y_av - k*x_av
delta_a = delta_k*np.sqrt(x_square_av - x_av**2)

test1 = [0]*5

for i in range(5):
    test1[i] = k*T1[i] + a

#second expenditure
T2 = [2.24, 3.32, 4.47, 5.95, 7.32]
IU2 = [0.30647, 0.42061, 0.56238, 0.72858, 0.91418]

m = 0.102

for i in range(5):
    T2[i] *= m

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += IU2[i]/5
    x_av += T2[i]/5
    y_square_av += IU2[i]**2/5
    x_square_av += T2[i]**2/5
    xy_av += T2[i]*IU2[i]/5

k = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_k = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - k**2)/5)
a = y_av - k*x_av
delta_a = delta_k*np.sqrt(x_square_av - x_av**2)

test2 = [0]*5

for i in range(5):
    test2[i] = k*T2[i] + a

#third expenditure
T3 = [1.52, 2.26, 3.07, 3.93, 5.01]
IU3 = [0.29873, 0.42042, 0.5652, 0.73042, 0.91817]

m = 0.161

for i in range(5):
    T3[i] *= m

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += IU3[i]/5
    x_av += T3[i]/5
    y_square_av += IU3[i]**2/5
    x_square_av += T3[i]**2/5
    xy_av += T3[i]*IU3[i]/5

k = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_k = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - k**2)/5)
a = y_av - k*x_av
delta_a = delta_k*np.sqrt(x_square_av - x_av**2)

test3 = [0]*5

for i in range(5):
    test3[i] = k*T3[i] + a

#plt.plot(T1, IU1, 'g^')
plt.plot(T1, test1, 'blue', label = 'first')
#plt.plot(T2, IU2, 'g^')
plt.plot(T2, test2, 'green', label = 'second')
#plt.plot(T3, IU3, 'g^')
plt.plot(T3, test3, 'red', label = 'third')
plt.legend()
plt.title('$IU(mdT)$')
plt.ylabel('$IU$', rotation = 0, labelpad = 10, fontsize = 13)
plt.xlabel('$mdT$', rotation = 0, labelpad = 2, fontsize = 13)
plt.grid(True)
plt.savefig('comparison', dpi = 600)
plt.show()