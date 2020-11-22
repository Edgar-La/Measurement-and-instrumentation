clear all;
clc;

f_corte=1e3;
C=22e-9;
Zetas = [.8659, .7072, .6516, .6179, .5789, .5228, .4431, .3833];
Respuestas = {'Bessel' ; 'Butterworth'; 'Chebyshev (0.1-dB peak)'; 'Chebyshev (0.25-dB peak)'; 'Chebyshev (0.5-dB peak)'; 'Chebyshev (1-dB peak)'; 'Chebyshev (2-dB peak)'; 'Chebyshev (3-dB peak)'};

for n=1:1:8
    %Obtenemos los valores de R1 y R2
    wo=2*pi()*f_corte;
    Zeta=Zetas(n);
    R2_c = 1/(Zeta*wo*C);
    R1_c = 1/((wo^2)*R2_c*(C^2));

    %Funcion de transferencia
    Ac=2/(C*R2_c);
    Bc=1/(R1_c*R2_c*(C^2));
    numc=[1 0 0];
    denc=[1 Ac Bc];

    %Diseño de  Literatura:
    %---------------------------------------------------------------------%
    %Tomamos los valores de R1' y R2' del cuadro 2
    Resistencias_1 = [1.103, .7072, .6105, .5624, .5131, .4509, .3743, .3223];
    Resistencias_2 = [1.471, 1.414, 1.438, 1.473, 1.531, 1.650, 1.906, 2.194];

    c = 1/wo;
    K = 1/(wo*c);
    R1 = K*Resistencias_1(n);
    R2 = K*Resistencias_2(n);

    %Funcion de transferencia
    A = 2/(R2*c);
    B = 1/(R1*R2*c^2);
    num = [1 0 0];
    den = [1 A B];

    %---------------------------------------------------------------------%

    w=logspace(0, 8, 1000);   
    [Mag,Fase,w]=bode(num,den,w);
    MagdB=20*log10(Mag); 

    %---------------------------------------------------------------------%
    %Graficamos: 
    figure (n)
    hold on
    bode(numc,denc,w)
    bode(num,den,w)
    grid on 

    Respuesta = string(Respuestas(n,1));
    title(['Filtro Activo Pasa Altas de 2do Orden. Respuesta tipo: ', Respuesta]);
    legend('Clase','Literatura')
    str = {['Zeta= ', num2str(Zetas(n))],''};
    text(10,50,str)
    hold off
    saveas(gcf, ['P_altas_comparacion_',num2str(n),'.png'])
end