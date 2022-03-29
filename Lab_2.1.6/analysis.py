import numpy as np
import matplotlib.pyplot as plt

delta_P = [4, 3.6, 3.24, 2.82, 2.4]

#T = 20 C
delta_T = [-3.47, -3.07, -2.61, -2.14, -1.67]

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += delta_T[i]/5
    x_av += delta_P[i]/5
    y_square_av += delta_T[i]**2/5
    x_square_av += delta_P[i]**2/5
    xy_av += delta_T[i]*delta_P[i]/5
k = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_k = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - k**2)/5)
a = y_av - k*x_av

test = [-3.49, -3.04, -2.63, -2.15, -1.67]

plt.plot(delta_P, delta_T, 'g^')
plt.plot(delta_P, test, 'red')
plt.title('$dT/dP, T = 20 ^{\circ}C$')
plt.ylabel('$dT$', rotation = 0, labelpad = 10, fontsize = 13)
plt.xlabel('$dP$', rotation = 0, labelpad = 2, fontsize = 13)
plt.grid(True)
#plt.savefig('graph_20', dpi = 600)
#plt.show()

#T = 30 C

delta_T = [-3.66, -3.17, -2.75, -2.31, -1.92]
y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += delta_T[i]/5
    x_av += delta_P[i]/5
    y_square_av += delta_T[i]**2/5
    x_square_av += delta_P[i]**2/5
    xy_av += delta_T[i]*delta_P[i]/5
k = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_k = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - k**2)/5)
a = y_av - k*x_av

test = [-3.62, -3.18, -2.7924939442874446, -2.34, -1.88]

plt.plot(delta_P, delta_T, 'r^')
plt.plot(delta_P, test, 'green')
plt.title('$dT/dP, T = 30 ^{\circ}C$')
plt.ylabel('$dT$', rotation = 0, labelpad = 10, fontsize = 13)
plt.xlabel('$dP$', rotation = 0, labelpad = 2, fontsize = 13)
plt.grid(True)
#plt.savefig('graph_30', dpi = 600)
#plt.show()

#T = 40 C
delta_T = [-3.27, -2.81, -2.43, -1.97, -1.61]

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(5):
    y_av += delta_T[i]/5
    x_av += delta_P[i]/5
    y_square_av += delta_T[i]**2/5
    x_square_av += delta_P[i]**2/5
    xy_av += delta_T[i]*delta_P[i]/5
k = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_k = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - k**2)/5)
a = y_av - k*x_av

test = [-3.24, -2.82, -2.45, -2.01, -1.57]

plt.plot(delta_P, delta_T, 'b^')
plt.plot(delta_P, test, 'orange')
plt.title('$dT/dP, T = 40 ^{\circ}C$')
plt.ylabel('$dT$', rotation = 0, labelpad = 10, fontsize = 13)
plt.xlabel('$dP$', rotation = 0, labelpad = 2, fontsize = 13)
plt.grid(True)
#plt.savefig('graph_40', dpi = 600)
#plt.show()

a1 = 8.31*(-0.05)*40*293*303/(20*98000)
b1 = 40*(-1.09*303 + 1.14*293)/10/98000
a2 = 8.31*(-0.046)*40*313*303/(20*98000)
b2 = 40*(-1.044*313 + 1.09*303)/10/98000
print(b1, b2, a1, a2)
print(2*a1/(8.31*b1))
print(2*a2/(8.31*b2))