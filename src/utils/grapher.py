import matplotlib.pyplot as plt

def discrete_plotter(t, x, title="Señal discreta"):
    plt.figure()
    plt.plot(t, x, marker="o", markersize=2, linestyle="-")
    plt.title(title)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
