import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================
# QCD Lattice Gauge Theory
# Advanced Visualization
# ==========================

# Parameters
L = 20
iterations = 500

# Random gauge field
phi = np.random.uniform(0, 2*np.pi, (L, L))

# Dark theme
plt.style.use("dark_background")

# Figure setup
fig, ax = plt.subplots(figsize=(10, 8))

# Initial plaquette calculation
def compute_plaquette(phi):
    return np.cos(
        phi
        - np.roll(phi, 1, axis=0)
        - np.roll(phi, 1, axis=1)
        + np.roll(np.roll(phi, 1, axis=0), 1, axis=1)
    )

plaquette = compute_plaquette(phi)

# Heatmap
im = ax.imshow(
    plaquette,
    cmap="plasma",
    vmin=-1,
    vmax=1,
    animated=True
)

# Colorbar
cbar = plt.colorbar(im)
cbar.set_label("Plaquette Value")

# Grid lines
ax.set_xticks(np.arange(-0.5, L, 1), minor=True)
ax.set_yticks(np.arange(-0.5, L, 1), minor=True)
ax.grid(which="minor", color="white", linestyle="-", linewidth=0.3)

# Labels
ax.set_xlabel("X Lattice Coordinate")
ax.set_ylabel("Y Lattice Coordinate")

# Information panel
info_text = ax.text(
    0.02,
    1.02,
    "",
    transform=ax.transAxes,
    fontsize=10,
    color="white"
)

# Animation update
def update(frame):
    global phi

    # Small Monte Carlo-like fluctuation
    phi += np.random.normal(0, 0.15, (L, L))

    plaquette = compute_plaquette(phi)

    im.set_array(plaquette)

    mean_val = np.mean(plaquette)
    std_val = np.std(plaquette)

    wilson_loop = np.mean(plaquette)

    ax.set_title(
        "QCD Lattice Gauge Theory Simulation",
        fontsize=16
    )

    return [im, info_text]

# Animation
ani = FuncAnimation(
    fig,
    update,
    frames=iterations,
    interval=80,
    blit=True
)

plt.tight_layout()
plt.show()