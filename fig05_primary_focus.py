"""
Fig. 5 — Primary study focus classification (multi-select)
Animal journal: 300 DPI TIFF, horizontal bar, all categories including Hardware
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#333333',
})

DARK  = '#1B3F6E'
MID   = '#2E75B6'
LIGHT = '#9DC3E6'

cats = [
    'Behaviour recognition /\nclassification',
    'Activity monitoring',
    'Methodological /\nalgorithm innovation',
    'Precision livestock\nmanagement',
    'Posture detection',
    'Hardware / device\ndevelopment',
    'Dataset development',
    'Facial expression\nanalysis',
    'Lameness detection',
    'Disease detection',
    'Stress-related\nbehaviour',
    'Social interaction',
]
counts = [22, 6, 6, 5, 5, 4, 2, 2, 1, 1, 1, 1]

colors = [DARK if c >= 5 else MID if c >= 3 else LIGHT for c in counts]

fig, ax = plt.subplots(figsize=(12, 7.5))
y = np.arange(len(cats))
bars = ax.barh(y, counts, color=colors, height=0.62,
               edgecolor='white', linewidth=0.5)
for bar, n in zip(bars, counts):
    ax.text(bar.get_width() + 0.15,
            bar.get_y() + bar.get_height()/2,
            f'n = {n}', va='center', fontsize=9.5,
            fontweight='bold', color='#222222')

ax.set_yticks(y)
ax.set_yticklabels(cats, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel('Number of studies (multi-select; total tags > n = 28)', fontsize=10, labelpad=6)
ax.set_xlim(0, 27)
ax.xaxis.grid(True, linestyle='--', alpha=0.35)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_title(
    'Fig. 5. Primary study focus categories across included studies (n = 28; multi-select).\n'
    'Total tags exceed n = 28 because individual studies address multiple focus areas.',
    fontsize=10, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('./figures/Fig05_primary_focus.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 5 saved")
