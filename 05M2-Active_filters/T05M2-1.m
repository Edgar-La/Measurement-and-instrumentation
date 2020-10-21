%Programa 5-7

pkg load control
clear all
clc
%clf


num = [25];
den = [1 6 25];
t = 0:0.005:5;
[y,x,t] = step(tf(num,den),t);
r=1; while y(r)<1.0001; r = r+1;end;
tiempo_subida = (r-1)*0.005

[ymax,tp] = max(y);
tiempo_pico = (tp-1)*0.005

sobreelongacion_max = ymax-1

s = 1001;
while y(s)>0.98 && y(s)<1.02;
  s=s-1;
end;
tiempo_asentamiento = (s-1)*0.005