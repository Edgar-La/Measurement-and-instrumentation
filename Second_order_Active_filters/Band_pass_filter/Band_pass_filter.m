%%Filtro Pasa Bajas. 

clear all;
clc;

fc=10e3;
Cap = 10e-8;
Q= [2, 4, 6, 8, 10];
H=10;
wo=2*pi()*fc;

for n=1:1:5
%------------------------------------------------------------------%
%Diseño con el factor Q
R3= (2*Q(n))/(wo*Cap);
R1= (Q(n))/(wo*Cap*H);
R2= (Q(n))/((wo*Cap)*((2*Q(n)^2)-H));
A_Q=(-1)/(R1*Cap);
B_Q=(2/Cap)/(R3);
C_Q=((1/R1)+(1/R2))/(R3*Cap^2);
numQ=[0 A_Q 0];
denQ=[1 B_Q C_Q];

%-----------------------------------------------------------------%
%Diseño sin el factor Q

A_12 = -1/(Cap*R1);
B_12 = 2/(R3*Cap);
C_12 = (4*Q(n)^2)/(Cap^2*(R3^2));
num = [0 A_12 0];
den= [1 B_12 C_12];


%-----------------------------------------------------------------%
w=logspace(0, 8, 1000);   
[Mag,Fase,w]=bode(numQ,denQ,w);
MagdB=20*log10(Mag); 
%-----------------------------------------------------------------%

figure (1)
hold on
bode(numQ,denQ,w)
grid on
title({'Caracterizacion del Filtro Activo Pasa Bandas de Segundo Orden' ; 'Funcion de transferencia con el factor Q'})
legend('Q1=2','Q2=4','Q3=6','Q4=8','Q5=10')
hold off

figure (2)
hold on
bode(num,den,w)
grid on
title({'Caracterizacion del Filtro Activo Pasa Bandas de Segundo Orden' ; 'Funcion de transferencia sin el factor Q'})
legend('Q1=2','Q2=4','Q3=6','Q4=8','Q5=10')
hold off
end

figure(1)
saveas(gcf, ['P_banda_con_Q.png'])
figure(2)
saveas(gcf, ['P_banda_sin_Q.png'])