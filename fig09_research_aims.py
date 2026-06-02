"""
Fig. 9 — Classification of primary research aims (multi-select)
Animal journal: 300 DPI TIFF
Key: dashed separator line between development and validation aims
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Updated font to Arial as per journal formatting guidelines
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#333333',
})

DARK  = '#1B3F6E'
MID   = '#2E75B6'
LIGHT = '#9DC3E6'

aims   = [
    'Develop a new AI model',
    'Improve existing model',
    'Real-time implementation',
    'Validate existing system',
    'Proof-of-concept',
    'Commercial evaluation',
    'Compare algorithms',
    'Dataset creation',
    'Behaviour prediction',
    'Edge / embedded\ndeployment',
    'Early disease\ndetection',
    'Precision farm\noptimisation',
]
counts = [25, 7, 7, 6, 5, 4, 4, 3, 2, 2, 1, 1]

colors = [DARK if c >= 5 else MID if c >= 3 else LIGHT for c in counts]

fig, ax = plt.subplots(figsize=(12, 7.5))
y = np.arange(len(aims))
bars = ax.barh(y, counts, color=colors, height=0.62,
               edgecolor='white', linewidth=0.5)

for bar, n in zip(bars, counts):
    ax.text(bar.get_width() + 0.2,
            bar.get_y() + bar.get_height()/2,
            f'n = {n}', va='center', fontsize=9,
            fontweight='bold', color='#222222')

ax.set_yticks(y)
ax.set_yticklabels(aims, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel('Number of studies (multi-select; total tags > n = 28)',
              fontsize=10, labelpad=8)
ax.set_xlim(0, 31)
ax.xaxis.grid(True, linestyle='--', alpha=0.35)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Development vs validation separator line and annotation positioning optimized
ax.axhline(y=2.5, color='#c0392b', linestyle='--', linewidth=1.3, alpha=0.8)
ax.annotate('Model-development aims \u25b2',
            xy=(26, 0.8), fontsize=9, color=DARK,
            ha='center', va='bottom', style='italic', fontweight='bold')
ax.annotate('\u25bc Model-validation / translation aims',
            xy=(6, 3.4), fontsize=9, color='#c0392b',
            ha='left', va='top', style='italic', fontweight='bold')
ax.text(30.5, 3.8, '89% vs 21%\ndev./val.\nimbalance',
        fontsize=8.5, ha='right', va='center', color='#c0392b', style='italic', fontweight='bold')

ax.set_title(
    'Fig. 9. Classification of primary research aims across included studies (n = 28; multi-select).\n'
    'Dashed line separates model-development aims (above) from model-validation aims (below).\n'
    'PoC = proof-of-concept; CE = commercial evaluation.',
    fontsize=10, fontweight='bold', pad=15)

# Tight layout and margin padding configuration
plt.tight_layout()
plt.subplots_adjust(left=0.22)

plt.savefig('./figures/Fig09_research_aims.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 9 saved successfully with font and alignment fixes!")