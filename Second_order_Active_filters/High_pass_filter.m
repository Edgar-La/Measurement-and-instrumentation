clear all;
clc;
pkg load control;

f_corte = 1e3;
Sigma = sqrt(2)/2;
C_1 = 22e-9;

R = 1/(C_1*Sigma*2*pi*f_corte);
C_2 = 1/(4*(pi^2)*(f_corte^2)*(R^2)*C_1);

w = sqrt(1/(C_1*C_2*R^2))/(2*pi)

disp(f_corte)
disp(Sigma)
disp(R)
disp(C_1)
disp(C_2)
disp(w)