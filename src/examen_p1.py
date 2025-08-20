import numpy as np
import matplotlib.pyplot as plt
from .utils.grapher import continuous_plotter, discrete_plotter


def dft(x: np.ndarray) -> np.ndarray:
    """DFT implementada a mano (sin usar numpy.fft)."""
    x = np.asarray(x, dtype=complex)
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    return W @ x


def generate_signal(fc=8.0, fm=0.5, m=0.5, fs=256.0, duration=8.0):
    """
    Genera la señal:
    x(t) = [1 + m*cos(2π*fm*t)] * sin(2π*fc*t)

    Parámetros:
        fc: frecuencia portadora
        fm: frecuencia del modulador
        m: índice de modulación
        fs: frecuencia de muestreo
        duration: duración de la señal en segundos
    Devuelve: t, x, fs
    """
    t = np.arange(0, duration, 1 / fs)
    x = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)
    return t, x, fs


def analyze(x: np.ndarray, fs: float):
    """Aplica DFT, calcula espectro y picos principales."""
    N = len(x)
    X = dft(x)
    freqs = np.arange(N) * fs / N

    # Espectro de amplitud de un solo lado
    mag = np.abs(X) / N
    half = N // 2
    freqs_s = freqs[: half + 1]
    amp_s = mag[: half + 1] * 2
    amp_s[0] = mag[0]  # DC no se duplica

    # Resolución en frecuencia
    df = fs / N

    # Picos más altos
    idx_sorted = np.argsort(amp_s)[::-1]
    peaks = []
    for idx in idx_sorted:
        f = freqs_s[idx]
        a = amp_s[idx]
        if f == 0:
            continue
        if all(abs(f - p[0]) > df / 2 for p in peaks):
            peaks.append((f, a))
        if len(peaks) >= 5:
            break

    return {"N": N, "df": df, "freqs": freqs_s, "amp": amp_s, "peaks": peaks}


def run():
    """Ejecuta la práctica completa."""
    # Parámetros de la señal
    fc, fm, m = 8.0, 0.5, 0.5
    fs, duration = 256.0, 8.0

    t, x, fs = generate_signal(fc, fm, m, fs, duration)
    res = analyze(x, fs)

    print(f"N = {res['N']}")
    print(f"Δf = {res['df']:.6f} Hz")
    print("Picos espectrales principales (Hz, amplitud aprox.):")
    for f, a in res["peaks"][:3]:
        print(f"  {f:.3f} Hz -> {a:.4f}")

    # Gráficas
    continuous_plotter(t, x, "x(t) = [1 + m cos(2πfmt)] sin(2πfct)")
    discrete_plotter(res["freqs"], res["amp"], "Espectro de amplitud (un solo lado)")
    plt.show()

