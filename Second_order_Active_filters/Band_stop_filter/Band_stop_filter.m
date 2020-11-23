clear all;
clc;

fc=10e3;
Q= [2, 4, 6, 8, 10];
wo=2*pi()*fc;

Rin=10e3;
R1 = (2*Rin);
R2 = (2*Rin);
R3 = (2*Rin);
R=Rin;
R4 = R;
R5 = R;
hold on
for n=1:1:5   
    C2= 2*Q(n)/(pi()*fc*R);
    C1= 1/((2*pi()*fc*R)^2*(C2));

    A=R4+R5-((R2*R3)/R1);
    B=1/(R4*R5*C1*C2);
    C=(R3+R4+R5)/(R4*R5*C2);

    num=[1 A B];
    den=[1 C B];


    w=logspace(0, 8, 1000);  
    [Mag,Phase,w]=bode(num,den,w);
    MagdB=20*log10(Mag);


    bode(num,den,w)
end
grid on
title('Filtro Activo Rechaza-Banda de 2do Orden')
legend('Q1=2','Q2=4','Q3=6','Q4=8','Q5=10')
hold off
saveas(gcf, ['R_banda.png'])