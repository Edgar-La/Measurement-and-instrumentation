clear all; close all; clc;

fs = 44100;
MyVoice = audiorecorder(fs,16,1);
sec=2;
% Grabar audio
disp('Grabando...');
recordblocking(MyVoice,sec);
disp('Grabado');
 
% Reproduce audio
play(MyVoice);
 
%Store data in double-precision array.
y = getaudiodata(MyVoice,'double');
Longy = length(y);
Diftime= sec/Longy;
Freq=1/Diftime;
time=0:Diftime:sec-Diftime;
Longtime=length(time);
disp(Diftime)
disp(sec-Diftime)
% Gráficas
figure(1)
plot(y,'r')
grid on;
 
figure(2)
plot(time,y,'r')
grid on;