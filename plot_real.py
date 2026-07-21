#!/usr/bin/env python3
"""
Jacobian Conjecture Counterexample (Alpoge, July 20 2026)
Visualization: four views of the actual polynomial map's folding behavior

Panel 1 (3D): three preimage curves in source space
Panel 2: grid deformation showing folding in target space
Panel 3: source plane color-coded by F1 value with contours
Panel 4: 1D cross-section through all three preimages
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def F(x, y, z):
    u = 1 + x * y
    F1 = u**3 * z + y**2 * u * (4 + 3 * x * y)
    F2 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    F3 = 2 * x - 3 * x**2 * y - x**3 * z
    return F1, F2, F3


fig = plt.figure(figsize=(18, 16))
fig.suptitle("The actual polynomial map: how the sheets fold",
             fontsize=15, fontweight='bold', y=0.97)

preimages = [(0, 0, -0.25), (1, -1.5, 6.5), (-1, 1.5, 6.5)]

# ── Panel 1: three preimage curves in 3D source space ──────────────────────
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.set_title('Three preimage curves in source (x, y, z)\n'
              'All map to the same line in the target',
              fontsize=11, fontweight='bold')

a_vals = np.linspace(-2.5, -0.02, 500)

ax1.plot(np.zeros_like(a_vals), np.zeros_like(a_vals), a_vals,
         '-', color='steelblue', linewidth=2.5, label='Branch 1: (0, 0, a)')

x2 = 1.0 / (2 * np.sqrt(-a_vals))
y2 = -3.0 * np.sqrt(-a_vals)
z2 = -26.0 * a_vals
mask = (np.abs(x2) < 5) & (np.abs(y2) < 10) & (np.abs(z2) < 70)
ax1.plot(x2[mask], y2[mask], z2[mask],
         '-', color='crimson', linewidth=2.5, label='Branch 2: (+x)')

x3 = -1.0 / (2 * np.sqrt(-a_vals))
y3 = 3.0 * np.sqrt(-a_vals)
z3 = -26.0 * a_vals
ax1.plot(x3[mask], y3[mask], z3[mask],
         '-', color='forestgreen', linewidth=2.5, label='Branch 3: (−x)')

for px, py, pz in preimages:
    ax1.plot([px], [py], [pz], 'o', color='steelblue', markersize=10,
             markeredgecolor='black', markeredgewidth=1.5, zorder=10)
    ax1.plot([px], [py], [pz], 'X', color='crimson', markersize=10,
             markeredgecolor='black', markeredgewidth=0.5, zorder=11)
    ax1.plot([px], [py], [pz], '^', color='forestgreen', markersize=9,
             markeredgecolor='black', markeredgewidth=1, zorder=12)

ax1.set_xlabel('x', fontsize=10)
ax1.set_ylabel('y', fontsize=10)
ax1.set_zlabel('z', fontsize=10)
ax1.legend(fontsize=8, loc='upper left')

# ── Panel 2: grid deformation ──────────────────────────────────────────────
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('Source grid (x, y) at z = −0.25\nmapped through (F₁, F₂)',
              fontsize=11, fontweight='bold')

z_fixed = -0.25
n_lines = 25

for x_val in np.linspace(-1.5, 1.5, n_lines):
    y_range = np.linspace(-2.5, 2.5, 300)
    f1, f2, _ = F(x_val, y_range, z_fixed)
    ok = (np.abs(f1) < 8) & (np.abs(f2) < 8)
    ax2.plot(np.where(ok, f1, np.nan), np.where(ok, f2, np.nan),
             '-', color='steelblue', alpha=0.4, linewidth=0.7)

for y_val in np.linspace(-2.5, 2.5, n_lines):
    x_range = np.linspace(-1.5, 1.5, 300)
    f1, f2, _ = F(x_range, y_val, z_fixed)
    ok = (np.abs(f1) < 8) & (np.abs(f2) < 8)
    ax2.plot(np.where(ok, f1, np.nan), np.where(ok, f2, np.nan),
             '-', color='crimson', alpha=0.4, linewidth=0.7)

ax2.plot(-0.25, 0, 'o', color='steelblue', markersize=14,
         markeredgecolor='black', markeredgewidth=1.5, zorder=10)
ax2.plot(-0.25, 0, 'X', color='crimson', markersize=14,
         markeredgecolor='black', markeredgewidth=0.5, zorder=11)
ax2.plot(-0.25, 0, '^', color='forestgreen', markersize=12,
         markeredgecolor='black', markeredgewidth=1, zorder=12)

ax2.set_xlabel('F₁', fontsize=11)
ax2.set_ylabel('F₂', fontsize=11)
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.grid(True, alpha=0.15)
ax2.set_aspect('equal')
ax2.plot([], [], 'o', color='steelblue', markersize=8,
         markeredgecolor='black', label='F₁ = −1/4')
ax2.plot([], [], 'X', color='crimson', markersize=8,
         markeredgecolor='black', label='F₂ = 0')
ax2.plot([], [], '^', color='forestgreen', markersize=8,
         markeredgecolor='black', label='F₃ = 0')
ax2.legend(fontsize=8, loc='upper right')

# ── Panel 3: source heatmap ───────────────────────────────────────────────
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('The folding: source grid colored by\nwhich sheet covers a target region',
              fontsize=11, fontweight='bold')

X, Y = np.meshgrid(np.linspace(-1.8, 1.8, 400), np.linspace(-3, 3, 400))
F1g, F2g, _ = F(X, Y, -0.25)

im = ax3.pcolormesh(X, Y, F1g, cmap='RdBu_r', vmin=-3, vmax=3,
                    shading='auto', rasterized=True)
plt.colorbar(im, ax=ax3, label='F₁ value', shrink=0.8)
ax3.contour(X, Y, F1g, levels=[-0.25], colors='gold', linewidths=2)
ax3.contour(X, Y, F2g, levels=[0], colors='lime', linewidths=1.5, linestyles='--')

ax3.plot(0, 0, 'o', color='steelblue', markersize=12,
         markeredgecolor='black', markeredgewidth=1.5, zorder=10)
ax3.plot(0, 0, 'X', color='crimson', markersize=12,
         markeredgecolor='black', markeredgewidth=0.5, zorder=11)
ax3.plot(0, 0, '^', color='forestgreen', markersize=10,
         markeredgecolor='black', markeredgewidth=1, zorder=12)

ax3.set_xlabel('x (source)', fontsize=11)
ax3.set_ylabel('y (source)', fontsize=11)
ax3.text(0.02, 0.02,
         'Gold contour: F₁ = −1/4\nDashed green: F₂ = 0\nIntersections = preimages',
         transform=ax3.transAxes, fontsize=8, va='bottom',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# ── Panel 4: 1D cross-section ─────────────────────────────────────────────
ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title('1D cross-section along a path\nthrough all three preimages',
              fontsize=11, fontweight='bold')

t = np.linspace(-1.8, 1.8, 1000)
y_path = -1.5 * t
z_path = -0.25 + (27.0 / 4.0) * t**2
f1p, f2p, f3p = F(t, y_path, z_path)

ax4.plot(t, f1p, '-', color='steelblue', linewidth=2.5, label='F₁')
ax4.plot(t, f2p, '-', color='crimson', linewidth=2.5, label='F₂')
ax4.plot(t, f3p, '-', color='forestgreen', linewidth=2.5, label='F₃')
ax4.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

for xp in [-1, 0, 1]:
    ax4.axvline(x=xp, color='gray', linestyle=':', alpha=0.5)
    yp = -1.5 * xp
    zp = -0.25 + 6.75 * xp**2
    f1v, f2v, f3v = F(xp, yp, zp)
    ax4.plot(xp, f1v, 'o', color='steelblue', markersize=12,
             markeredgecolor='black', markeredgewidth=1.5, zorder=6)
    ax4.plot(xp, f2v, 'X', color='crimson', markersize=12,
             markeredgecolor='black', markeredgewidth=0.5, zorder=6)
    ax4.plot(xp, f3v, '^', color='forestgreen', markersize=11,
             markeredgecolor='black', markeredgewidth=1, zorder=6)

ax4.plot([], [], 'o', color='steelblue', markersize=8,
         markeredgecolor='black', label='F₁ = −1/4')
ax4.plot([], [], 'X', color='crimson', markersize=8,
         markeredgecolor='black', label='F₂ = 0')
ax4.plot([], [], '^', color='forestgreen', markersize=8,
         markeredgecolor='black', label='F₃ = 0')

ax4.set_xlabel('x (parameter along path through 3 preimages)', fontsize=10)
ax4.set_ylabel('Component values', fontsize=10)
ax4.legend(fontsize=8, loc='upper center', ncol=3)
ax4.grid(True, alpha=0.2)
ax4.set_ylim(-5, 7)

plt.savefig('visualization_real.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved visualization_real.png")
