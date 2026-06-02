"""
Fig. 2 — Species distribution: bar chart + species-by-year stacked bar
Animal journal: 300 DPI TIFF, Arial, clean two-panel layout
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Font updated to Arial as per journal guidelines, ensuring crisp alignment
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#333333',
})

DARK  = '#1B3F6E'
MID   = '#2E75B6'
LIGHT = '#9DC3E6'
ORANGE= '#C55A11'

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# ── Panel (a): species totals ──────────────────────────────────────────────
ax = axes[0]
species = ['Cattle', 'Sheep /\nLambs', 'Goats', 'Cattle\n& Pig']
counts  = [20, 6, 1, 1]
pcts    = [71, 21, 4, 4]
colors  = [DARK, MID, LIGHT, ORANGE]

bars = ax.barh(species, counts, color=colors, height=0.55,
               edgecolor='white', linewidth=0.5)
for bar, n, pct in zip(bars, counts, pcts):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            f'n = {n}  ({pct}%)', va='center', fontsize=10.5,
            fontweight='bold', color='#222222')

ax.set_xlabel('Number of included studies', fontsize=11, labelpad=6)
ax.set_xlim(0, 26)
ax.xaxis.grid(True, linestyle='--', alpha=0.35)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_title('(a) Species distribution of included studies (n = 28)',
             fontsize=11, pad=8, loc='left')

# ── Panel (b): species by year ─────────────────────────────────────────────
ax2 = axes[1]
years = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
cattle = [1,0,0,1,0,2,1,2,3,7,3]
sheep  = [0,0,0,0,0,0,0,0,1,3,2]
goat   = [0,0,0,0,0,0,0,0,0,1,0]
other  = [0,0,0,0,0,0,0,0,0,1,0]

b1 = ax2.bar(years, cattle, color=DARK,   width=0.6, label='Cattle',      alpha=0.92)
b2 = ax2.bar(years, sheep,  color=MID,    width=0.6, label='Sheep/Lambs', alpha=0.92,
             bottom=cattle)
b3 = ax2.bar(years, goat,   color=LIGHT,  width=0.6, label='Goats',       alpha=0.92,
             bottom=[c+s for c,s in zip(cattle,sheep)])
b4 = ax2.bar(years, other,  color=ORANGE, width=0.6, label='Cattle & Pig',alpha=0.92,
             bottom=[c+s+g for c,s,g in zip(cattle,sheep,goat)])

# labelpad increased to 15 to prevent overlap with rotated tick labels
ax2.set_xlabel('Publication year', fontsize=11, labelpad=15)
ax2.set_ylabel('Number of studies', fontsize=11, labelpad=6)
ax2.set_xticks(years)
ax2.set_xticklabels([str(y) for y in years], fontsize=9, rotation=45, ha='right')
ax2.set_ylim(0, 15)
ax2.yaxis.grid(True, linestyle='--', alpha=0.35)
ax2.set_axisbelow(True)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.legend(fontsize=9, loc='upper left', framealpha=0.9, edgecolor='#cccccc')
ax2.set_title('(b) Species representation by publication year',
              fontsize=11, pad=8, loc='left')

fig.suptitle(
    'Fig. 2. Species distribution of included studies (n = 28).\n'
    '(a) Total studies per species. (b) Species representation across publication years.',
    fontsize=10, fontweight='bold', y=1.04, ha='center')

# Adjust layout to accommodate the increased labelpad smoothly
plt.tight_layout()
plt.subplots_adjust(bottom=0.18)

plt.savefig('./figures/Fig02_species_distribution.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 2 saved with layout and font updates successfully!")