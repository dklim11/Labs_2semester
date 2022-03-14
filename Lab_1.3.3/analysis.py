import numpy as np
import matplotlib.pyplot as plt

#3.9
P_lam = [19.6, 39.2, 58.9, 78.5, 98.1, 117.7, 137.3]
t_lam = [214, 110, 70, 55.5, 43, 36.6, 31.9]
sigma_t_lam = [1, 1, 1, 1, 1, 1, 1]
Q_lam = [0.012, 0.023, 0.036, 0.045, 0.058, 0.068, 0.078]

P_tur = [157, 235.4, 314, 392.4, 470.9, 549.4, 627.8, 706.3]
t_tur = [28.6, 24.3, 21.8, 19.5, 17.8, 16.3, 15.5, 14.4]
sigma_t_tur = [1, 1, 1, 1, 1, 1, 1]
Q_tur = [0.087, 0.103, 0.115, 0.128, 0.14, 0.153, 0.161, 0.174]

#5.25
P_lam_2 = [9.8, 19.6, 29.4, 39.2, 49, 58.9, 62.8]
t_lam_2 = [163.3, 65.8, 44.8, 33.8, 26.8, 22.5, 21.5]
sigma_t_lam_2 = [1, 1, 1, 1, 1, 1, 1]
Q_lam_2 = [0.015, 0.038, 0.056, 0.074, 0.093, 0.111, 0.116]

P_tur_2 = [68.7, 98.1, 127.5,  157, 186.4, 215.8, 274.7, 294.3]
t_tur_2 = [20.4, 17.9, 16.2, 14.8, 13.7, 12.3, 11, 9.25]
sigma_t_tur_2 = [1, 1, 1, 1, 1, 1, 1, 1]
Q_tur_2 = [0.123, 0.14, 0.154, 0.169, 0.182, 0.203, 0.227, 0.27]

y_av = 0
x_av = 0
x_square_av = 0
y_square_av = 0
xy_av = 0
for i in range(7):
    y_av += P_lam_2[i]/7
    x_av += Q_lam_2[i]/7
    y_square_av += P_lam_2[i]**2/7
    x_square_av += Q_lam_2[i]**2/7
    xy_av += P_lam_2[i]*Q_lam_2[i]/7
b = (xy_av - x_av*y_av)/(x_square_av - x_av**2)
delta_b = np.sqrt(((y_square_av - y_av**2)/(x_square_av - x_av**2) - b**2)/7)

#print((P_lam_2[4]-P_lam_2[3])/(Q_lam_2[4] - Q_lam_2[3]))

#plt.plot(Q2, P2, 'g^')
#plt.ylabel('$P, Па$')
#plt.xlabel('$Q, m^3/s$')
#plt.grid(True)
#plt.savefig('relation_d_1.png')
#plt.show()

#print(3.1415*1769000*(3.9*0.001)**4/64)
#print(3.1415*527000*(5.25*0.001)**4/64)
#print(3.1415*(0.001*3.9)**3*np.sqrt((1769000*0.0001)**2 + (3.9*0.001*669000/4)**2 + (3.9*0.001*1769000*0.01/4)**2)/16)
#print(3.1415*(0.001*3.9)**3*np.sqrt((526000*0.0001)**2 + (3.9*0.001*199000/4)**2 + (3.9*0.001*527000*0.01/4)**2)/16)
#print(2*1.3*0.078*100000/(1000*3.1415*1.8*3.9*0.001))

x = [30, 40, 50]
y = [49, 62, 78]
plt.plot(x, y, 'green')
plt.title('$\delta P(length)$')
plt.grid(True)
plt.savefig('check_d1', dpi = 600)
plt.show()
