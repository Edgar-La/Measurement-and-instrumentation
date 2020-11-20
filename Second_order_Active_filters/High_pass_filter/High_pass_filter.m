clear all;
clc;
pkg load control;

f_corte = 1e3;
Sigmas = [.8659, .7072, .6516, .6179, .5789, .5228, .4431, .3833];
C = 22e-9;

for n = 1:1:8
  Sigma = Sigmas(n);
  R_2 = 1/(C*Sigma*2*pi*f_corte);
  R_1 = 1/((C^2)*R_2*(4*pi^2)*(f_corte^2));
  W = 1/sqrt(R_1*R_2*(C^2)*4*(pi^2));

  A = 2/(C*R_2);
  B = 1/(R_1*R_2*C^2);
  num = [1 0 0];
  den = [1 A B];
  w = logspace(0, 8, 1000);


  figure(n)
  bode(tf(num, den), w);
  title(['Sigma = ', num2str(Sigma)])
  saveas(gcf, ['P_altas',num2str(n),'.png'])

end 
%disp(f_corte)
%disp(Sigma)
%disp(C)
%disp(R_1)
%disp(R_2)
%disp(W)