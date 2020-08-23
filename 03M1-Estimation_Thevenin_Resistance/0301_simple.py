import os
os.system('clear')

print('Please type the nominal values for the componentes:\n\n')

Vs = float(input('Vs = '))
R1 = float(input('R1 = '))
R2 = float(input('R2 = '))
R3 = float(input('R3 = '))
R4 = float(input('R4 = '))

Vo = (Vs*R3*(R2+R4))/(R3*(-R1-R2+R4)-R2*(3*R2+2*R1)-R4*(R1+R2))
Isc = (-1*Vs*(R2+R4))/(R2*(2*R1+3*R2+R4)+R1*R4)
Rth = Vo/Isc
Rth_ = (-R3*(R2*(2*R1+3*R2+R4)+R1*R4))/(R3*(-R1-R2+R4)-R2*(3*R2+2*R1)-R4*(R1+R2))


print('\n\nVo = ' + str(Vo))
print('Isc = ' + str(Isc))
print('Thevenin resistance is Rth = ' + str(Rth))