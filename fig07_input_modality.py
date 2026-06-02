"""
Fig. 7 — Input modality distribution
Animal journal: 300 DPI TIFF, annotation box for absent modalities
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Font updated to Arial as per journal formatting rules
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
GRAY  = '#808080'

fig, ax = plt.subplots(figsize=(10, 5.5))

# Refined labels to make them cleaner and professionally spaced
cats   = ['Video /\ncamera (RGB)', 'Multi-sensor\nfusion', 'Still images\n(RGB)',
          'Accelerometer', 'RFID']
counts = [22, 5, 4, 2, 1]
pcts   = [79, 18, 14, 7, 4]
colors = [DARK, MID, LIGHT, ORANGE, GRAY]

bars = ax.bar(cats, counts, color=colors, width=0.55,
              edgecolor='white', linewidth=0.5)
for bar, n, pct in zip(bars, counts, pcts):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.25,
            f'n = {n}\n({pct}%)',
            ha='center', va='bottom', fontsize=10.5,
            fontweight='bold', color='#1a1a1a')

ax.set_ylabel('Number of included studies', fontsize=12, labelpad=6)
ax.set_ylim(0, 28)
ax.yaxis.grid(True, linestyle='--', alpha=0.35)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Shifted down slightly to guarantee no collision with multi-line title parameters
ax.text(0.99, 0.91,
        'Note: No included study used thermal,\n'
        'depth, or hyperspectral imaging\n'
        'as a primary modality.',
        transform=ax.transAxes, fontsize=8.5,
        ha='right', va='top', color='#c0392b', style='italic',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#FFF5F5',
                  edgecolor='#c0392b', alpha=0.85))

ax.set_title(
    'Fig. 7. Distribution of primary input modalities across included studies (n = 28).\n'
    'All included studies used standard RGB imaging only. Multi-sensor fusion = camera\n'
    'combined with accelerometer or RFID.',
    fontsize=10, fontweight='bold', pad=15)

# Layout padding optimization
plt.tight_layout()
plt.savefig('./figures/Fig07_input_modality.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 7 saved successfully with layout adjustments!")