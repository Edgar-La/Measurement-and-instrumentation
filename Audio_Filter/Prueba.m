% Filtro pasa-banda
% Edgar Lara
clear all; close all; clc;
%pkg load signal;

sec = 2; flow_ = 400; fhigh_ = 800;
% Grabar audio y reproducirlo
%Fs = 44100;
%MyVoice = audiorecorder(Fs,16,1);
%disp('Grabando...');
%recordblocking(MyVoice,sec);
%disp('Grabado');
%play(MyVoice);
%y = getaudiodata(MyVoice,'double');
 
% Abrir audio y reproducirlo

Audios = {'Grabacion.wav'; 'Campana_1.wav'; 'Campana_2.wav'; 'Chasquidos.wav';  'Dedos_purados.wav';
				'Esferas_Newton.wav'; 'Escribir.wav';  'Guitarra_1.wav'; 'Guitarra_2.wav'; 'Toc_Toc.wav'};
[y,Fs] = audioread(Audios{1});
sound(y.*50,Fs);
 
% Datos necesarios de la se�al
%y = getaudiodata(MyVoice,'double');
Longy = length(y);
Diftime= sec/Longy;
time=0:Diftime:sec-Diftime;

%-------------------------------------------------------------------------
% FFT de la se�al de audio (RADIOGRAF�A DE LA SE�AL)
AudioAnalysis = 2^(nextpow2(Longy));   %NUMERO DE MUESTRAS
AudiOriginal = fft(y,AudioAnalysis);      %Aplicamos la FFT
f1=Fs*((-AudioAnalysis/2):(AudioAnalysis/2-1))/AudioAnalysis;
AudiOrg=fftshift(AudiOriginal);         %ordenar de mayor a menor las fft

%Calculo de la magnitud
b1=2.*abs(AudiOrg);
logY1=b1.^2;

%Calculo de la fase
PhaseAudio=angle(AudiOrg);
Angle=(180/pi()).*PhaseAudio;

%-------------------------------------------------------------------------
% Frecuencias de corte para an�lisis de la se�al
flow = flow_; %frecuencia baja
fhigh = fhigh_; %frecuencia alta
wclow=flow*1.25*pi;
wchigh=fhigh*1.25*pi;
ffiltro=Longy/max(time);
% Filtro de la se�al de pasa-banda
Long_OriginalSignal = length(Angle);
ffiltro1 = ffiltro*Long_OriginalSignal;
Wnd1=[wclow/ffiltro wchigh/ffiltro];
[f1a,g1a]=butter(4,Wnd1/2,'bandpass');
FilteredSignal= filtfilt(f1a,g1a,y);
sound(FilteredSignal.*50,Fs);

%-------------------------------------------------------------------------
% FFT de la se�al de audio (RADIOGRAF�A DE LA SE�AL -FILTRADA-)
AudioAnalysis2=2^(nextpow2(length(FilteredSignal)));   %NUMERO DE MUESTRAS
AudiOriginal2=fft(FilteredSignal,AudioAnalysis2);      %Aplicamos la FFT
f2=Fs*((-AudioAnalysis2/2):(AudioAnalysis2/2-1))/AudioAnalysis2;
AudiOrg2=fftshift(AudiOriginal2);         %ordenar de mayor a menor las fft
 
%Calculo de la magnitud
b2=2.*abs(AudiOrg2);
logY2=b2.^2;
 
%Calculo de la fase
PhaseAudio2=angle(AudiOrg2);
Angle2=(180/pi()).*PhaseAudio2;

%-------------------------------------------------------------------------
% Grafica la se�al de audio
%figure(1)
%plot(y,'r')
%grid on;
 
%figure(2)
%plot(time,y,'r')
%grid on;

figure(3)
plot(y,'b')
hold on;
plot(FilteredSignal,'r')
grid on;

figure(4)
plot(f1,logY1,'b')
hold on;
plot(f2,logY2,'r')
grid on;
