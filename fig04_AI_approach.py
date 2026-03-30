"""
Fig. 4 — AI modelling approaches across included studies
Animal journal: 300 DPI TIFF, multi-select note, clean bar chart
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#333333',
})

DARK  = '#1B3F6E'
MID   = '#2E75B6'
LIGHT = '#9DC3E6'
ORANGE= '#C55A11'

fig, ax = plt.subplots(figsize=(9, 5.5))

cats   = ['Deep Learning', 'Hybrid', 'Classical ML', 'Traditional CV']
counts = [24, 4, 3, 1]
pcts   = [86, 14, 11, 4]
colors = [DARK, MID, LIGHT, ORANGE]

bars = ax.bar(cats, counts, color=colors, width=0.55,
              edgecolor='white', linewidth=0.5)
for bar, n, pct in zip(bars, counts, pcts):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.25,
            f'n = {n}\n({pct}%)',
            ha='center', va='bottom', fontsize=10.5,
            fontweight='bold', color='#1a1a1a')

ax.set_ylabel('Number of included studies', fontsize=12, labelpad=6)
ax.set_ylim(0, 30)
ax.yaxis.grid(True, linestyle='--', alpha=0.35)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.text(0.99, 0.97,
        'Multi-select; sum of percentages exceeds 100%',
        transform=ax.transAxes, fontsize=8.5,
        ha='right', va='top', color='#555555', style='italic')

ax.set_title(
    'Fig. 4. Distribution of AI modelling approaches across included studies (n = 28).\n'
    'Categories are multi-select; percentages relative to n = 28.\n'
    'DL = deep learning; Classical ML = classical machine learning;\n'
    'Traditional CV = rule-based computer vision without machine learning.',
    fontsize=10, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('./figures/Fig04_AI_approach.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 4 saved")
