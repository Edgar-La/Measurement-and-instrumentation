clear all
%clc
%clf
%pkg load control

%Definir componentes
fprintf('\nDiseño Filtro pasa-bajas 2do orden\n\n')
fc = input('Introduce frecuencia de corte(fc):  ');
Sigma = input('Introduce el valor de sigma:  ');
C = input('Introdce valor de Capacitor 1 (C1): ');

wc = 2*pi*fc;

R2 = 1/(C*Sigma*2*pi*fc);
R1 = 1/((C^2)*R2*((2*pi)^2)*(fc^2));

fprintf('Capacitor (C): %6.3d\n', C);
fprintf('Resistor 1 (R1): %6.3d\n', R1);
fprintf('Resistor 2 (R2): %6.3d\n', R2);

%Funcion de transferencia
A = 2/(C*R2);
B = 1/(R1*R2*C^2);
fc = (sqrt(B))/(2*pi);
fprintf('Frecuencia de corte %6.2f\n', fc);

%Funcion de transferencia
num = [1 0 0];
den = [1 A B];
w = logspace(0, 8, 1000);
[Mag, Fase, w] = bode(tf(num,den), w);
%bode(tf(num, den), w);
MagdB = 20*log10(Mag);    %Poner la magnitud en decibeles

figure(1)
bode(tf(num, den), w);

figure(2)
semilogx(w, MagdB)
%grid on;