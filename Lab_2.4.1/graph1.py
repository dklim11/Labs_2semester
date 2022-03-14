import numpy as np
import matplotlib.pyplot as plt

P1 = [2919.2, 3264.2, 3582.7, 3967.5, 4387, 4856.5, 5334.2, 5865, 6475.4, 7191.9, 7948.3, 8744.4]
T1 = [294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316]

P2 = [3304, 3622.5, 4020.6, 4471.7, 4949.4, 5480.2, 6024.2, 6647.9, 7351.1, 8107.5, 8744.4]
T2 = [296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316]

P3 = [7.98, 8.09, 8.18, 8.29, 8.39, 8.49, 8.58, 8.68, 8.78, 8.88, 8.98, 9.08]
T3 = [0.003401, 0.003378, 0.003356, 0.003333, 0.003311, 0.0032895, 0.003268, 0.003247, 0.003226, 0.0032051, 0.003185, 0.003164]

P4 = [8.1, 8.2, 8.3, 8.4, 8.51, 8.6, 8.7, 8.8, 8.9, 9, 9.08]
T4 = [0.003378, 0.003356, 0.003333, 0.003311, 0.003289, 0.003268, 0.003247, 0.003226, 0.0032051, 0.003185, 0.003165]

#heating
y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(0, 12):
    y_av += P1[i]/12
    x_av += T1[i]/12
    y_square_av += P1[i]**2/12
    x_square_av += T1[i]**2/12
    xy_av += P1[i]*T1[i]/12

b1 = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b1 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b1**2)/12)

#cooling
y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(0, 11):
    y_av += P2[i]/11
    x_av += T2[i]/11
    y_square_av += P2[i]**2/11
    x_square_av += T2[i]**2/11
    xy_av += P2[i]*T2[i]/11

b2 = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b2 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b2**2)/11)

b0 = (b1 + b2)/2 #average coefficient in the first case
delta_b0 = (delta_b1+delta_b2)/2

print(8.31*x_av/y_av*np.sqrt(4*(b0*0.1)**2 + (b0*x_av*13596*9.8*0.01*0.01/y_av)**2 + (x_av*delta_b0)**2))
print(1427*1000/46)

#heating - logarifmic approach
y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(0, 12):
    y_av += P3[i]/12
    x_av += T3[i]/12
    y_square_av += P3[i]**2/12
    x_square_av += T3[i]**2/12
    xy_av += P3[i]*T3[i]/12

b3 = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b3 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b3**2)/12)

#cooling - logarifmic approach
y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(0, 11):
    y_av += P4[i]/11
    x_av += T4[i]/11
    y_square_av += P4[i]**2/11
    x_square_av += T4[i]**2/11
    xy_av += P4[i]*T4[i]/11

b4 = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b4 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b4**2)/11)

b5 = (b3 + b4)/2 #average coefficient in the first case
delta_b5 = (delta_b3+delta_b4)/2
print(3891/834500)

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('P-T coordinates')
#plt.title('lnP-1/T coordinates')
#plt.plot(T1, P1, label = r'$heating$') #1
#plt.plot(T2, P2, label = r'$cooling$') #2
plt.plot(T3, P3, label = r'$heating$') #3
plt.plot(T4, P4, label = r'$cooling$') #4
p1, v1 = np.polyfit(T1, P1, 1, cov = True)
p2, v2 = np.polyfit(T2, P2, 1, cov = True)
p3, v3 = np.polyfit(T3, P3, 1, cov = True)
p4, v4 = np.polyfit(T4, P4, 1, cov = True)
#plt.plot(T1, np.poly1d(p1)(T1), label = 'heat_approx') #1
#plt.plot(T2, np.poly1d(p2)(T2), label = 'cool_approx') #2
#plt.plot(T3, np.poly1d(p3)(T3), label = 'heat_approx') #3
#plt.plot(T4, np.poly1d(p4)(T4), label = 'cool_approx') #4
plt.legend(loc = 'best', fontsize = 10)
plt.grid(True)
plt.savefig('log_graphs.png', dpi = 600)
#plt.show()