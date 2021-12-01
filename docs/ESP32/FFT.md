

## 摘要

在本文中将以$x(t)=A\cos(2\pi ft+\phi)$的傅里叶变换为例介绍Matlab中如何进行傅里叶变换，主要介绍以下内容：

 1. 用数字方式（离散时间）描述信号$x(t)$
 2. 利用傅里叶变换将离散信号$x[n]$变换到频域$X[k]$
 3. 提取频域信号$X[k]$的幅值和相位谱，及功率谱
 4. 由频域信号恢复出时域信号

## 离散时间域表示

考虑一个正弦波$x(t)=A\cos(2\pi ft+\phi)$，其中$A=4$, $f=2\text{Hz}$，$\phi=\pi/4$(即$30^{\circ}$)。即：

\begin{equation}\label{eq:xt}
x(t)=4cos(2\pi 2t+\pi/4)
\end{equation}

为将时域连续信号（模拟信号）$x(t)$存储到计算机中，我们需对其进行采样，根据Nyquist采样定律，采样频率一般需要大于信号频率的两倍。

下面看看这采样频率为8和32的情形

    A=4;
    f=2;
    phi=pi/4;
    duration=2;
    fs=4*f;
    t=0:1/fs:duration-1/fs;
    x=A*cos(2*pi*f*t+phi);
    figure('Position',[500 300 400 300])
    subplot(2,1,1)
    plot(t,x)
    hold on
    stem(t,x,':.','color',[0.5 0.5 0.5])
    ylabel('fs=8')
    hold off
    fs=16*f;
    t=0:1/fs:duration-1/fs;
    x=A*cos(2*pi*f*t+phi);
    subplot(2,1,2)
    plot(t,x)
    hold on
    stem(t,x,':.','color',[0.5 0.5 0.5])
    xlabel('time(s)')
    ylabel('fs=32')

得到的结果如下图

![离散结果](http://www.mekesim.com/usr/uploads/2016/09/2469517740.png)

从图中可以看到当采样频率$fs=8$时，已经看不出原始信号的形状了，我们也可以认为是一个方波信号。不过即便如此频率信息还是保留了。当采样频率$fs=32$时，能够较好地描述原始信号的形状。

## 利用傅立叶变换到频域

傅立叶变换得到的结果为复数$X=X_{re} + j X_{im}$。Matlab提供的**X = fft(x,N)**函数可以进行快速离散傅立叶变换，变换长度N必须足够大，否则在变换过程中会丢失有用信息，如果不指定N，则默认以x的数据长度作为N的值。

    N = 32;  % Transform length, FFT size
    X=fft(x,N);
    ff = fs*(0:N-1)/N;
    subplot(3,1,2)
    stem(ff,abs(X)/N,'.');

下面看看N分别取8, 32, 128情形下的结果：
![FFT结果](http://www.mekesim.com/usr/uploads/2016/09/2682705478.png)

 - N=8，频率信息失真 
 - N=32，校准确地获得频率信息 
 - N=128，？？

注意到，即使中间那幅图正确的得到了频率分量，但是怎么会有一个$f=30\text{Hz}$的分量，这又是什么鬼？
其实可以只取前面一半的数据X(1: N/2)，并将幅值$\times 2$，即可得到单边谱。如果想要得到和理论教程中一样的结果，可以将频率搬移，得到复频率的那一半。正负频率的结果是对称的哦。Matlab已经提供了函数**fftshift**进行此操作。

另外也可以根据傅立叶变换结果计算信号的功率谱

    X = fftshift(fft(x,N))/N;
    stem(ff,abs(X),'.'); %magnitudes vs frequencies
    xlabel('Frequency (Hz)'); 
    ylabel('Amplitude |X[N]|');
    power=X.*conj(X);
    stem(ff,power,'.')
    xlabel('Frequency (Hz)'); 
    ylabel('Power');

![幅值谱和功率谱](http://www.mekesim.com/usr/uploads/2016/09/3131700564.png)

相位谱

如果直接用angle(X)读取幅值信息，发现结果比较混乱。

    subplot(2,1,1)
    plot(ff,angle(X)*180/pi); %magnitudes vs frequencies
    X2=X;%store the FFT results in another array
    %detect noise (very small numbers (eps)) and ignore them
    threshold = max(abs(X))/10000; %tolerance threshold
    X2(abs(X)<threshold) = 0; %maskout values that are below the threshold
    phase=unwrap(angle(X2))*180/pi; %phase information
    subplot(2,1,2)
    stem(ff,phase,'.'); %phase vs frequencies

![相位谱](http://www.mekesim.com/usr/uploads/2016/09/3930432017.png)