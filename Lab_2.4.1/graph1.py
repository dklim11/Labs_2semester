import numpy as np
import matplotlib.pyplot as plt

P1 = [215.6*13.54, 241.08*13.54, 264.6*13.54, 293.02*13.54, 324*13.54, 358.68*13.54, 393.96*13.54, 433.16*13.54, 478.24*13.54, 531.16*13.54, 587.02*13.54, 645.82*13.54]
T1 = [294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316]

P2 = [244.02*13.54, 267.54*13.54, 296.94*13.54, 330.26*13.54, 365.54*13.54, 404.74*13.54, 444.92*13.54, 490.98*13.54, 542.92*13.54, 598.78*13.54, 645.82*13.54]
T2 = [296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316]

P3 = [np.log(215.6*13.54), np.log(241.08*13.54), np.log(264.6*13.54), np.log(293.02*13.54), np.log(324*13.54), np.log(358.68*13.54), np.log(393.96*13.54), np.log(433.16*13.54), np.log(478.24*13.54), np.log(531.16*13.54), np.log(587.02*13.54), np.log(645.82*13.54)]
T3 = [1/294, 1/296, 1/298, 1/300, 1/302, 1/304, 1/306, 1/308, 1/310, 1/312, 1/314, 1/316]

P4 = [np.log(244.02*13.54), np.log(267.54*13.54), np.log(296.94*13.54), np.log(330.26*13.54), np.log(365.54*13.54), np.log(404.74*13.54), np.log(444.92*13.54), np.log(490.98*13.54), np.log(542.92*13.54), np.log(598.78*13.54), np.log(645.82*13.54)]
T4 = [1/296, 1/298, 1/300, 1/302, 1/304, 1/306, 1/308, 1/310, 1/312, 1/314, 1/316]

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
delta_b1 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b1)/12)

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
delta_b2 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b2)/11)

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
delta_b3 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b3)/12)

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
delta_b4 = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b4)/11)
#print(b4, " ", delta_b4)

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('P-T coordinates')
#plt.title('lnP-1/T coordinates')
#plt.plot(T1, P1, label = r'$heating$') #1
#plt.plot(T2, P2, label = r'$cooling$') #2
#plt.plot(T3, P3, label = r'$heating$') #3
#plt.plot(T4, P4, label = r'$cooling$') #4
p1, v1 = np.polyfit(T1, P1, 1, cov = True)
p2, v2 = np.polyfit(T2, P2, 1, cov = True)
p3, v3 = np.polyfit(T3, P3, 1, cov = True)
p4, v4 = np.polyfit(T4, P4, 1, cov = True)
#plt.plot(T1, np.poly1d(p1)(T1), label = 'heat_approx') #1
#plt.plot(T2, np.poly1d(p2)(T2), label = 'cool_approx') #2
plt.plot(T3, np.poly1d(p3)(T3), label = 'heat_approx') #3
plt.plot(T4, np.poly1d(p4)(T4), label = 'cool_approx') #4
plt.legend(loc = 'best', fontsize = 10)
plt.grid(True)
#plt.savefig('log_approximations.png', dpi = 600)
plt.show()

#print(b1, " ", delta_b1)
#print(b2, " ", delta_b2)
#print(b3, " ", delta_b3)
#print(b4, " ", delta_b4)

b0 = (b1 + b2)/2 #average coefficient in the first case
delta_b0 = (delta_b1+delta_b2)/2
print(b0, " ", delta_b0)
#267.83791195816264   79.63512112945219 (dP/dT)

delta_p = 13540*9.8*0.001
delta_L1 = 8.31*T1[0]/P1[0]*np.sqrt(4*(b0*0.1)**2 + (T1[0]*b0*delta_p/P1[0])**2 + (T1[0]*delta_b0)**2)
#print(delta_L1)

b5 = (b3 + b4)/2 #average coefficient in the second case
delta_b5 = (delta_b3 + delta_b4)/2
print(b5, " ", delta_b5)
#-4619.487583588178   1363.6247878882282 (d(lnP)/d(1/T))
