import numpy as np
from src.utils.grapher import discrete_plotter
import matplotlib.pyplot as plt

def dft(x):
    """
    Implementación propia de la DFT.
    x : señal de entrada (array 1D)
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def run():
    # Parámetros
    fs = 256  # frecuencia de muestreo
    T = 6     # duración en segundos
    N = fs * T
    t = np.arange(N) / fs

    # Señal original
    f1, f2 = 8, 20
    x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

    # Ruido (señal de 50 Hz, por ejemplo)
    ruido = 0.8 * np.sin(2*np.pi*50*t)
    x_ruido = x + ruido

    # DFT
    X = dft(x)
    Xr = dft(x_ruido)

    # Frecuencias
    freqs = np.arange(N) * fs / N

    # Graficar señal original
    discrete_plotter(t, x, "Señal original")
    plt.figure()
    plt.stem(freqs[:N//2], np.abs(X[:N//2]))
    plt.title("Espectro señal original")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X[k]|")

    # Graficar señal con ruido
    discrete_plotter(t, x_ruido, "Señal con ruido")
    plt.figure()
    plt.stem(freqs[:N//2], np.abs(Xr[:N//2]))
    plt.title("Espectro señal con ruido")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X[k]|")

    plt.show()
