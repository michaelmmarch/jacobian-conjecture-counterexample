#!/usr/bin/env python3
"""
Jacobian Conjecture Counterexample (Alpoge, July 20 2026)
Visualization: interactive 3D isosurfaces (exports to HTML via plotly)

Open the output HTML file in a browser to rotate, zoom, and toggle surfaces.
"""

import numpy as np
import plotly.graph_objects as go
from skimage import measure


def F(x, y, z):
    u = 1 + x * y
    F1 = u**3 * z + y**2 * u * (4 + 3 * x * y)
    F2 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    F3 = 2 * x - 3 * x**2 * y - x**3 * z
    return F1, F2, F3


n = 100
x_vol = np.linspace(-1.8, 1.8, n)
y_vol = np.linspace(-2.5, 2.5, n)
z_vol = np.linspace(-1, 8, n)
Xv, Yv, Zv = np.meshgrid(x_vol, y_vol, z_vol, indexing='ij')
F1v, F2v, F3v = F(Xv, Yv, Zv)

fig = go.Figure()


def add_isosurface(volume, level, x, y, z, color, name, opacity=0.3):
    try:
        verts, faces, _, _ = measure.marching_cubes(
            volume - level, 0,
            spacing=(x[1] - x[0], y[1] - y[0], z[1] - z[0]),
        )
        verts[:, 0] += x[0]
        verts[:, 1] += y[0]
        verts[:, 2] += z[0]
        fig.add_trace(go.Mesh3d(
            x=verts[:, 0], y=verts[:, 1], z=verts[:, 2],
            i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
            color=color, opacity=opacity, name=name,
            showlegend=True, flatshading=True,
        ))
        print(f"  {name}: {len(verts)} vertices")
    except Exception as e:
        print(f"  Skipping {name}: {e}")


print("Computing isosurfaces...")
add_isosurface(F1v, -0.25, x_vol, y_vol, z_vol, 'steelblue', 'F₁ = −1/4', 0.3)
add_isosurface(F2v, 0.0, x_vol, y_vol, z_vol, 'crimson', 'F₂ = 0', 0.25)
add_isosurface(F3v, 0.0, x_vol, y_vol, z_vol, 'forestgreen', 'F₃ = 0', 0.25)

preimages = [(0, 0, -0.25), (1, -1.5, 6.5), (-1, 1.5, 6.5)]
labels = ['(0, 0, −1/4)', '(1, −3/2, 13/2)', '(−1, 3/2, 13/2)']

fig.add_trace(go.Scatter3d(
    x=[p[0] for p in preimages],
    y=[p[1] for p in preimages],
    z=[p[2] for p in preimages],
    mode='markers+text',
    marker=dict(size=8, color='gold', line=dict(color='black', width=2)),
    text=labels,
    textposition='top center',
    textfont=dict(size=10),
    name='Preimage points',
    showlegend=True,
))

fig.update_layout(
    title=dict(
        text='Isosurfaces in source space: F₁ = −1/4, F₂ = 0, F₃ = 0<br>'
             '<sub>Gold dots = the three preimages of (−1/4, 0, 0). '
             'Rotate to explore. Toggle surfaces in the legend.</sub>',
        font=dict(size=16),
    ),
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z',
        aspectmode='manual',
        aspectratio=dict(x=1, y=1.2, z=2),
    ),
    legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.8)'),
    width=1000,
    height=800,
)

fig.write_html('isosurfaces_interactive.html', include_plotlyjs=True)
print("Saved isosurfaces_interactive.html")
