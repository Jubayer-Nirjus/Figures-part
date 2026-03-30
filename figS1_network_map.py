"""
Supplementary Fig. S1 — Evidence network map
Animal journal: 300 DPI TIFF
Bipartite: AI model families (left) ↔ welfare outcome categories (right)
Absent domain explicitly marked with X
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
})

DARK  = '#1B3F6E'
MID   = '#2E75B6'
LIGHT = '#9DC3E6'
ORANGE= '#C55A11'
PURPLE= '#7030A0'

fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# AI nodes (left, x=2)
ai_nodes = [
    (2, 8.5, 'YOLO family',            13, DARK),
    (2, 7.0, 'CNN\n(transfer learning)', 4, MID),
    (2, 5.5, 'Other deep\nlearning',     7, MID),
    (2, 4.0, 'Classical ML',             3, LIGHT),
    (2, 2.5, 'Pose estimation',          1, LIGHT),
    (2, 1.2, 'RNN / optical\nflow',      1, LIGHT),
]

# Welfare outcome nodes (right, x=8)
wo_nodes = [
    (8, 9.0, 'Behavioural\nmeasures',    26, DARK,   True),
    (8, 7.5, 'Activity\npatterns',        15, MID,    True),
    (8, 6.2, 'Posture /\nlying',          11, MID,    True),
    (8, 5.0, 'Feeding /\nrumination',      6, MID,    True),
    (8, 3.8, 'Social\nbehaviour',          5, LIGHT,  True),
    (8, 2.7, 'Stress-related\nbehaviour',  3, PURPLE, True),
    (8, 1.5, 'Lameness /\ndisease',        2, ORANGE, True),
    (8, 0.5, 'Pain / affective\nstate \u2715 ABSENT', 0, '#CCCCCC', False),
]

# Edges (ai_idx, wo_idx, weight)
edges = [
    (0,0,12),(0,1,10),(0,2,8),(0,3,4),(0,4,3),(0,5,2),
    (1,0,4), (1,1,3), (1,2,2),
    (2,0,6), (2,1,5), (2,2,3),(2,3,2),
    (3,0,3), (3,1,2),
    (4,2,1),
    (5,1,1),
]

for ai_i, wo_i, weight in edges:
    x1, y1 = ai_nodes[ai_i][0], ai_nodes[ai_i][1]
    x2, y2 = wo_nodes[wo_i][0], wo_nodes[wo_i][1]
    lw = max(0.5, weight * 0.32)
    alpha = min(0.72, 0.18 + weight * 0.045)
    ax.plot([x1+0.45, x2-0.45], [y1, y2],
            color='#2E75B6', lw=lw, alpha=alpha, zorder=1)
    if weight >= 5:
        mx = (x1+0.45 + x2-0.45)/2
        my = (y1 + y2)/2
        ax.text(mx, my+0.14, str(weight),
                fontsize=7, ha='center', color='#1B3F6E', fontweight='bold')

# Draw AI nodes
for x, y, label, n, color in ai_nodes:
    sz = max(400, n * 110)
    ax.scatter(x, y, s=sz, c=color, zorder=3,
               edgecolors='white', linewidths=1.5, alpha=0.9)
    ax.text(x - 0.55, y, label, fontsize=9, ha='right', va='center',
            fontweight='bold', color='#1a1a1a')
    ax.text(x + 0.52, y - 0.38, f'n={n}', fontsize=7.5,
            ha='left', va='top', color='#555555')

# Draw welfare outcome nodes
for x, y, label, n, color, pres in wo_nodes:
    if not pres:
        ax.scatter(x, y, s=200, c=color, zorder=3,
                   edgecolors='#c0392b', linewidths=2.5, alpha=0.6, marker='X')
        ax.text(x + 0.58, y, label, fontsize=9, ha='left', va='center',
                color='#c0392b', style='italic')
    else:
        sz = max(350, n * 75)
        ax.scatter(x, y, s=sz, c=color, zorder=3,
                   edgecolors='white', linewidths=1.5, alpha=0.88)
        ax.text(x + 0.58, y, label, fontsize=9, ha='left', va='center',
                fontweight='bold', color='#1a1a1a')
        ax.text(x + 0.55, y - 0.4, f'n={n}', fontsize=7.5,
                ha='left', va='top', color='#555555')

# Headers
for hx, htxt in [(2, 'AI model families'), (8, 'Welfare outcome categories')]:
    ax.text(hx, 9.75, htxt, fontsize=11, fontweight='bold', ha='center',
            color=DARK,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#DEEAF1',
                      edgecolor=DARK, alpha=0.85))

ax.text(5, 0.08,
        'Edge label = number of co-occurring studies  |  Node size = frequency of occurrence  |  \u2715 = absent from all studies',
        fontsize=8, ha='center', va='bottom', color='#555555', style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#F5F5F5',
                  edgecolor='#CCCCCC'))

ax.set_title(
    'Supplementary Fig. S1. Evidence network map: AI model families and welfare outcome\n'
    'categories across included studies (n = 28). Edge labels show co-occurrence frequency\n'
    '(studies in which that model family\u2013welfare outcome combination co-occurred).\n'
    '\u2715 indicates outcomes absent from all included studies.',
    fontsize=10, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('./figures/FigS1_network_map.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig S1 saved")
