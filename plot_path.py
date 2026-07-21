#!/usr/bin/env python3
"""
Jacobian Conjecture Counterexample (Alpoge, July 20 2026)
Visualization: path through the three preimages of (-1/4, 0, 0)

Top panel:  input coordinates (x, y, z) along a curve connecting the preimages
Bottom panel: output values (F1, F2, F3) — all three hit (-1/4, 0, 0) simultaneously
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def F(x, y, z):
    u = 1 + x * y
    F1 = u**3 * z + y**2 * u * (4 + 3 * x * y)
    F2 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    F3 = 2 * x - 3 * x**2 * y - x**3 * z
    return F1, F2, F3


fig, (ax_top, ax_bot) = plt.subplots(
    2, 1, figsize=(14, 10), height_ratios=[1, 1.3],
    gridspec_kw={'hspace': 0.35},
)
fig.suptitle(
    'Path through the three preimages of (−1/4, 0, 0)',
    fontsize=14, fontweight='bold', y=0.97,
)

# Parametrize a curve through (0,0,-1/4), (1,-3/2,13/2), (-1,3/2,13/2)
t = np.linspace(-1.8, 1.8, 1000)
y_path = -1.5 * t
z_path = -0.25 + (27.0 / 4.0) * t**2

# --- Top panel: input coordinates ---
ax_top.set_title('INPUT: source coordinates (x, y, z) along the path',
                 fontsize=12, fontweight='bold')
ax_top.plot(t, t, '-', color='steelblue', linewidth=2.5, label='x')
ax_top.plot(t, y_path, '-', color='crimson', linewidth=2.5, label='y = −3x/2')
ax_top.plot(t, z_path, '-', color='forestgreen', linewidth=2.5,
            label='z = −1/4 + 27x²/4')

for xp in [-1, 0, 1]:
    ax_top.axvline(x=xp, color='gray', linestyle=':', alpha=0.5)
    yp = -1.5 * xp
    zp = -0.25 + 6.75 * xp**2
    ax_top.plot(xp, xp, 'o', color='steelblue', markersize=9,
                markeredgecolor='black', zorder=5)
    ax_top.plot(xp, yp, 'o', color='crimson', markersize=9,
                markeredgecolor='black', zorder=5)
    ax_top.plot(xp, zp, 'o', color='forestgreen', markersize=9,
                markeredgecolor='black', zorder=5)

ax_top.annotate('(−1, 3/2, 13/2)', xy=(-1, -1), xytext=(-1.6, -4),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'),
                bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow'))
ax_top.annotate('(0, 0, −1/4)', xy=(0, 0), xytext=(0.5, -4),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'),
                bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow'))
ax_top.annotate('(1, −3/2, 13/2)', xy=(1, 1), xytext=(1.6, -4),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'),
                bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow'))

ax_top.set_xlabel('x (path parameter)', fontsize=11)
ax_top.set_ylabel('Coordinate value', fontsize=11)
ax_top.legend(fontsize=10, loc='upper center')
ax_top.grid(True, alpha=0.2)
ax_top.set_ylim(-6, 10)

# --- Bottom panel: output values ---
ax_bot.set_title('OUTPUT: F(x, y, z) = (F₁, F₂, F₃) along the same path',
                 fontsize=12, fontweight='bold')

f1_path, f2_path, f3_path = F(t, y_path, z_path)

ax_bot.plot(t, f1_path, '-', color='steelblue', linewidth=2.5, label='F₁')
ax_bot.plot(t, f2_path, '-', color='crimson', linewidth=2.5, label='F₂')
ax_bot.plot(t, f3_path, '-', color='forestgreen', linewidth=2.5, label='F₃')

ax_bot.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

for xp in [-1, 0, 1]:
    ax_bot.axvline(x=xp, color='gray', linestyle=':', alpha=0.5)
    yp = -1.5 * xp
    zp = -0.25 + 6.75 * xp**2
    f1v, f2v, f3v = F(xp, yp, zp)
    ax_bot.plot(xp, f1v, 'o', color='steelblue', markersize=12,
                markeredgecolor='black', markeredgewidth=1.5, zorder=6)
    ax_bot.plot(xp, f2v, 'X', color='crimson', markersize=12,
                markeredgecolor='black', markeredgewidth=0.5, zorder=6)
    ax_bot.plot(xp, f3v, '^', color='forestgreen', markersize=11,
                markeredgecolor='black', markeredgewidth=1, zorder=6)

ax_bot.plot([], [], 'o', color='steelblue', markersize=8,
            markeredgecolor='black', label='F₁ = −1/4')
ax_bot.plot([], [], 'X', color='crimson', markersize=8,
            markeredgecolor='black', label='F₂ = 0')
ax_bot.plot([], [], '^', color='forestgreen', markersize=8,
            markeredgecolor='black', label='F₃ = 0')

ax_bot.set_xlabel('x (path parameter)', fontsize=11)
ax_bot.set_ylabel('Output value', fontsize=11)
ax_bot.legend(fontsize=10, loc='upper center', ncol=3)
ax_bot.grid(True, alpha=0.2)
ax_bot.set_ylim(-5, 7)

plt.savefig('visualization_path.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("Saved visualization_path.png")
