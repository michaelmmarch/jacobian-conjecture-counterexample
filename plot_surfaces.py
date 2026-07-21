#!/usr/bin/env python3
"""
Jacobian Conjecture Counterexample (Alpoge, July 20 2026)
Visualization: isosurfaces and component surfaces in source space

Panel 1: F1 as surface over (x,y) at fixed z
Panel 2: F2 as surface over (x,y) at fixed z
Panel 3: contours of F1=-1/4, F2=0, F3=0 in (x,y) plane
Panel 4: isosurfaces of all three conditions in 3D (x,y,z) space
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure
import matplotlib.patches as mpatches


def F(x, y, z):
    u = 1 + x * y
    F1 = u**3 * z + y**2 * u * (4 + 3 * x * y)
    F2 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    F3 = 2 * x - 3 * x**2 * y - x**3 * z
    return F1, F2, F3


fig = plt.figure(figsize=(18, 14))
fig.suptitle("Visualizing the polynomial map in 2D and 3D input space",
             fontsize=15, fontweight='bold', y=0.97)

x_range = np.linspace(-1.5, 1.5, 200)
y_range = np.linspace(-2.5, 2.5, 200)
X, Y = np.meshgrid(x_range, y_range)
F1s, F2s, F3s = F(X, Y, -0.25)

# ── Panel 1: F1 as surface over (x,y) ───────────────────────────────────
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.set_title('F₁(x, y) as surface at z = −1/4', fontsize=11, fontweight='bold')

F1_clipped = np.clip(F1s, -5, 5)
ax1.plot_surface(X, Y, F1_clipped, cmap='RdBu_r', alpha=0.7, vmin=-3, vmax=3,
                 rstride=4, cstride=4, edgecolor='none')

xx, yy = np.meshgrid([-1.5, 1.5], [-2.5, 2.5])
ax1.plot_surface(xx, yy, np.full_like(xx, -0.25), alpha=0.2, color='gold')

ax1.plot([0], [0], [-0.25], 'o', color='steelblue', markersize=10,
         markeredgecolor='black', markeredgewidth=1.5, zorder=10)
ax1.set_xlabel('x', fontsize=10)
ax1.set_ylabel('y', fontsize=10)
ax1.set_zlabel('F₁', fontsize=10)
ax1.set_zlim(-5, 5)

# ── Panel 2: F2 as surface over (x,y) ───────────────────────────────────
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.set_title('F₂(x, y) as surface at z = −1/4', fontsize=11, fontweight='bold')

F2_clipped = np.clip(F2s, -5, 5)
ax2.plot_surface(X, Y, F2_clipped, cmap='RdBu_r', alpha=0.7, vmin=-3, vmax=3,
                 rstride=4, cstride=4, edgecolor='none')

ax2.plot_surface(xx, yy, np.full_like(xx, 0.0), alpha=0.2, color='lime')

ax2.plot([0], [0], [0], 'X', color='crimson', markersize=10,
         markeredgecolor='black', markeredgewidth=0.5, zorder=10)
ax2.set_xlabel('x', fontsize=10)
ax2.set_ylabel('y', fontsize=10)
ax2.set_zlabel('F₂', fontsize=10)
ax2.set_zlim(-5, 5)

# ── Panel 3: contours on (x,y) plane ────────────────────────────────────
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('Contours in (x, y) at z = −1/4:\nwhere each component hits its target value',
              fontsize=11, fontweight='bold')

ax3.contour(X, Y, F1s, levels=[-0.25], colors='steelblue', linewidths=2.5)
ax3.contour(X, Y, F2s, levels=[0], colors='crimson', linewidths=2.5, linestyles='--')
ax3.contour(X, Y, F3s, levels=[0], colors='forestgreen', linewidths=2.5, linestyles=':')

ax3.plot(0, 0, 'o', color='steelblue', markersize=12,
         markeredgecolor='black', markeredgewidth=1.5, zorder=10)
ax3.plot(0, 0, 'X', color='crimson', markersize=12,
         markeredgecolor='black', markeredgewidth=0.5, zorder=11)
ax3.plot(0, 0, '^', color='forestgreen', markersize=10,
         markeredgecolor='black', markeredgewidth=1, zorder=12)

ax3.plot([], [], '-', color='steelblue', linewidth=2.5, label='F₁ = −1/4')
ax3.plot([], [], '--', color='crimson', linewidth=2.5, label='F₂ = 0')
ax3.plot([], [], ':', color='forestgreen', linewidth=2.5, label='F₃ = 0')
ax3.legend(fontsize=9, loc='upper right')
ax3.set_xlabel('x', fontsize=11)
ax3.set_ylabel('y', fontsize=11)
ax3.grid(True, alpha=0.2)
ax3.set_aspect('equal')
ax3.text(0.02, 0.02,
         'Preimages = points where ALL THREE\ncontours intersect (only (0,0) in this z-slice)',
         transform=ax3.transAxes, fontsize=8, va='bottom',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

# ── Panel 4: isosurfaces in (x,y,z) space ───────────────────────────────
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.set_title('Isosurfaces in source (x, y, z) space:\nthree surfaces, three intersection points',
              fontsize=11, fontweight='bold')

n = 80
x_vol = np.linspace(-1.8, 1.8, n)
y_vol = np.linspace(-2.5, 2.5, n)
z_vol = np.linspace(-1, 8, n)
Xv, Yv, Zv = np.meshgrid(x_vol, y_vol, z_vol, indexing='ij')
F1v, F2v, F3v = F(Xv, Yv, Zv)


def plot_isosurface(ax, volume, level, x, y, z, color, alpha, label):
    try:
        verts, faces, _, _ = measure.marching_cubes(
            volume - level, 0,
            spacing=(x[1] - x[0], y[1] - y[0], z[1] - z[0]),
        )
        verts[:, 0] += x[0]
        verts[:, 1] += y[0]
        verts[:, 2] += z[0]
        ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                        color=color, alpha=alpha, edgecolor='none', shade=True)
    except Exception:
        pass


print("Computing isosurfaces...")
plot_isosurface(ax4, F1v, -0.25, x_vol, y_vol, z_vol, 'steelblue', 0.25, 'F₁=-1/4')
plot_isosurface(ax4, F2v, 0.0, x_vol, y_vol, z_vol, 'crimson', 0.2, 'F₂=0')
plot_isosurface(ax4, F3v, 0.0, x_vol, y_vol, z_vol, 'forestgreen', 0.2, 'F₃=0')

preimages = [(0, 0, -0.25), (1, -1.5, 6.5), (-1, 1.5, 6.5)]
for px, py, pz in preimages:
    ax4.plot([px], [py], [pz], 'o', color='gold', markersize=12,
             markeredgecolor='black', markeredgewidth=2, zorder=20)

ax4.legend(handles=[
    mpatches.Patch(color='steelblue', alpha=0.4, label='F₁ = −1/4'),
    mpatches.Patch(color='crimson', alpha=0.4, label='F₂ = 0'),
    mpatches.Patch(color='forestgreen', alpha=0.4, label='F₃ = 0'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gold',
               markersize=10, markeredgecolor='black', label='Preimage points'),
], fontsize=8, loc='upper left')

ax4.set_xlabel('x', fontsize=10)
ax4.set_ylabel('y', fontsize=10)
ax4.set_zlabel('z', fontsize=10)

plt.savefig('visualization_surfaces.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved visualization_surfaces.png")
