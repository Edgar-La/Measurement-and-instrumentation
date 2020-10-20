import scipy.signal as sig
import matplotlib.pyplot as plt

C1 = 300*10**-9;
C2 = 120*10**-12;
R = 1000;
RA = 3000;
RB = 2000;

num = (1/(C1*C2*R**2))#*(1+(RB/RA));
den1 = (2/(R*C1))#-((1/(R*C2))*(RB/RA));
den2 = 1/(C1*C2*R**2);

#filt = sig.lti((1, 0), (1, 0.2, 1))
filt = sig.lti((0, num), (1, den1, den2))
plt.plot(*filt.step())
plt.title('Respuesta a un impulso solitario')
plt.show()
