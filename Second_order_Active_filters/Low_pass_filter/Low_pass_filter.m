clear all;
clc;
pkg load control;

f_corte = 100e3;
Sigmas = [.8659, .7072, .6516, .6179, .5789, .5228, .4431, .3833];
C_1 = 22e-9;

for n = 1:1:8
  Sigma = Sigmas(n);
  R = 1/(C_1*Sigma*2*pi*f_corte);
  C_2 = 1/(4*(pi^2)*(f_corte^2)*(R^2)*C_1);
  W = 1/sqrt(C_1*C_2*(R^2)*4*(pi^2));

  A = 2/(C_1*R);
  B = 1/(C_1*C_2*R^2);
  num = [0 0 B];
  den = [1 A B];
  w = logspace(0, 8, 1000);


  figure(n)
  bode(tf(num, den), w);
  title(['Sigma = ', num2str(Sigma)])
  saveas(gcf, ['P_bajas',num2str(n),'.png'])

end 
disp(W)