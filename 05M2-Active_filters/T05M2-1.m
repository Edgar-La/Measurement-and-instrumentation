graphics_toolkit('gnuplot')
pkg load control
clear all
clc
clf
s = tf('s');

C1 = 300e-9;
C2 = 120e-12;
R = 1000;
RA = 3000;
RB = 2000;


%Parte 1
p1_1 = 1/(C1*C2*R^2);
p1_2 = (2/(R*C1));
p1_3 = 1/(C1*C2*R^2);

g1 = p1_1/(s**2 + s*p1_2 + p1_3);

%Parte 2
p2_1 = p1_1*(1+(RB/RA));
p2_2 = p1_2 - ((1/R*C2)*(RB/RA));
p2_3 = p1_3;

g2 = p2_1/(s**2 + s*p2_2 + p2_3);



x = input('Grafica 1 o 2: ');
if (x == 1)
  step(g1)
elseif (x == 2)
  step(g2)
endif