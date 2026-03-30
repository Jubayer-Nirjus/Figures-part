"""
Fig. 1 — Annual and cumulative publication trend
Animal journal: 300 DPI TIFF, Arial font, no top/right spine, clean layout
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#333333',
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
})

years   = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
annual  = [1,   0,   0,   1,   0,   2,   1,   2,   4,  12,   5]
cumul   = [1,   1,   1,   2,   2,   4,   5,   7,  11,  23,  28]

DARK  = '#1B3F6E'
ORANGE= '#C55A11'

fig, ax1 = plt.subplots(figsize=(11, 6))

bars = ax1.bar(years, annual, color=DARK, width=0.6, alpha=0.92, zorder=3)
for bar, val in zip(bars, annual):
    if val > 0:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.18,
                 str(val), ha='center', va='bottom', fontsize=10,
                 fontweight='bold', color=DARK)

ax1.set_xlabel('Publication year', fontsize=12, labelpad=8)
ax1.set_ylabel('Annual number of studies', fontsize=12, color=DARK, labelpad=8)
ax1.tick_params(axis='y', labelcolor=DARK)
ax1.set_xticks(years)
ax1.set_xticklabels([str(y) for y in years], fontsize=10)
ax1.set_ylim(0, 15)
ax1.yaxis.grid(True, linestyle='--', alpha=0.35, zorder=0)
ax1.set_axisbelow(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Rapid growth shading
ax1.axvspan(2022.7, 2025.4, alpha=0.06, color='green', zorder=0)
ax1.text(2024.0, 13.8,
         'Rapid growth\nphase (2023–2025)',
         ha='center', fontsize=8.5, color='#1a5c1a', style='italic')

ax2 = ax1.twinx()
ax2.plot(years, cumul, color=ORANGE, marker='o', linewidth=2.2,
         markersize=5.5, zorder=4)
ax2.set_ylabel('Cumulative studies (n)', fontsize=12, color=ORANGE, labelpad=8)
ax2.tick_params(axis='y', labelcolor=ORANGE)
ax2.set_ylim(0, 34)
ax2.spines['top'].set_visible(False)

h1 = mpatches.Patch(color=DARK,   label='Annual publications')
h2 = plt.Line2D([0],[0], color=ORANGE, marker='o', linewidth=2,
                markersize=5, label='Cumulative total')
ax1.legend(handles=[h1, h2], loc='upper left', fontsize=10, framealpha=0.9,
           edgecolor='#cccccc')

fig.suptitle(
    'Fig. 1. Annual and cumulative publication counts for studies applying computer\n'
    'vision and machine learning to welfare monitoring of farmed ruminant species\n'
    '(cattle, sheep, and goats), 2015–2025 (n = 28 included studies).',
    fontsize=10, fontweight='bold', y=1.02, ha='center')

plt.tight_layout()
plt.savefig('./figures/Fig01_publication_trend.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 1 saved")
