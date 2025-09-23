import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def simulate_trajectory(num_steps=1000, dt=0.01, accel_scale=1.0):
    """
    Simuliert eine 2D-Trajektorie mit zufälliger Beschleunigung.
    Gibt Positionen (x, y) und Geschwindigkeiten v zurück.
    """
    # Arrays anlegen
    pos = np.zeros((num_steps, 2))
    vel = np.zeros((num_steps, 2))

    # Startbedingungen zufällig
    pos[0] = np.random.randn(2) * 5
    vel[0] = np.random.randn(2)

    for i in range(1, num_steps):
        # zufällige Beschleunigung
        a = np.random.randn(2) * accel_scale
        # Integration
        vel[i] = vel[i - 1] + a * dt
        pos[i] = pos[i - 1] + vel[i] * dt

    # Geschwindigkeitsbeträge
    speed = np.linalg.norm(vel, axis=1)
    return pos[:, 0], pos[:, 1], speed


def plot_colored_trajectories(n_traj=5, **sim_kwargs):
    """
    Simuliert n_traj Trajektorien und plottet sie farblich nach Geschwindigkeit.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    for _ in range(n_traj):
        x, y, v = simulate_trajectory(**sim_kwargs)  # hier fühgst du die Positione und GEschwindigkeiten der Partikel ein. Die musst du aus den dump files extrahieren.
        # Die Struktur der Dumpfiles kannst du dir im Internet anschauen. Einen Code zum auslesen existiert unter /utilities_postprocessing/Evaluate_particle_flow.py

        # Punkte zu Liniensegmenten verbinden
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        # LineCollection mit Colormap
        lc = LineCollection(segments, cmap='rainbow',
                            norm=plt.Normalize(vmin=v.min(), vmax=v.max()))
        lc.set_array(v[:-1])  # Farbe nach Geschwindigkeit
        lc.set_linewidth(2)
        ax.add_collection(lc)

    ax.autoscale()
    ax.set_aspect('equal', 'datalim')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Partikeltrajektorien eingefärbt nach Geschwindigkeit')

    # Farbskala
    cbar = fig.colorbar(lc, ax=ax)
    cbar.set_label('Geschwindigkeit')

    plt.show()


if __name__ == "__main__":
    # Beispielaufruf: 5 Trajektorien, 2000 Schritte, dt=0.005
    plot_colored_trajectories(n_traj=5, num_steps=2000, dt=0.005, accel_scale=2.0)
