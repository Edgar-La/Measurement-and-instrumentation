clear all;
clc;

f_corte=1e3;
C_1=22e-9;
Zetas = [.8659, .7072, .6516, .6179, .5789, .5228, .4431, .3833];
Respuestas = {'Bessel' ; 'Butterworth'; 'Chebyshev (0.1-dB peak)'; 'Chebyshev (0.25-dB peak)'; 'Chebyshev (0.5-dB peak)'; 'Chebyshev (1-dB peak)'; 'Chebyshev (2-dB peak)'; 'Chebyshev (3-dB peak)'};

for n=1:1:8
    Zeta=Zetas(n);
    %--------------------------------------------------------------------%
    %Clase
    R_s=1/(C_1*2*pi*f_corte*Zeta);
    C_2=1/((R_s^2)*C_1*(2*pi*f_corte)^2);

    a=1/((R_s^2)*C_1*C_2);
    b=2/(R_s*C_1);
    numc=[a];
    denc=[1 b a];
    %--------------------------------------------------------------------%
    %Literatura:
    %Se escogen los valores de la tabla para C1'' y C2''.
    Capacitores_1 = [.9066, 1.414, 1.638, 1.778, 1.949, 2.218, 2.672, 3.103];
    C_1_b = Capacitores_1(n);
    Capacitores_2 = [.6799, .7071, .6955, .6789, .6533, .6061, .5246, .4558];
    C_2_b = Capacitores_2(n);
    %Definimos el valor de R y de la frecuencia de corte
    R= 1e3;
    Wo = f_corte*2*pi();

    %Aplicamos las ecuaciones que nos indica la bibliografia para encontrar C1 y C2
    C1 = (C_1_b/Wo)/R;
    C2 = (C_2_b/Wo)/R;

    A = C1*C2*R^2;
    B = C2*2*R;
    num = [0 0 1];
    den = [A B 1];
    %------------------------------------------------------------------%
    w=logspace(0,8,100);
    [Mag,Fase,w]=bode(num,den,w);
    %Agregar Magnitud en decibeles
    MagdB = 20*log10(Mag);

    %Graficas
    figure (n)

    hold on
    bode(numc,denc,w)
    bode(num,den,w)
    grid on 

    Respuesta = string(Respuestas(n,1));
    title(['Filtro Activo Pasa Bajas de 2do Orden. Respuesta tipo: ', Respuesta]);
    legend('Clase','Literatura')
    str = {['Zeta= ',num2str(Zetas(n))],''};
    text(10,50,str)
    hold off
    saveas(gcf, ['P_bajas_comparacion_',num2str(n),'.png'])
end