"""
Fig. 8 — Temporal evolution of AI modelling approaches by publication period
Animal journal: 300 DPI TIFF, 100% stacked bar, small-n caution annotation
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
GREEN = '#70AD47'
ORANGE= '#C55A11'

fig, ax = plt.subplots(figsize=(10, 6))

periods = [
    'Before 2020\n(n = 2)\n\u26a0 n too small\nfor reliable %',
    '2020\u20132022\n(n = 5)',
    '2023\u20132025\n(n = 21)'
]

# Proportions per period (%)
dl     = [50,  80,  76]
cml    = [50,   0,   8]
hybrid = [ 0,   0,  16]
trad   = [ 0,  20,   0]

x = np.arange(3)
w = 0.55

p1 = ax.bar(x, dl,     color=DARK,   width=w, label='Deep learning',   alpha=0.92)
p2 = ax.bar(x, cml,    color=ORANGE, width=w, label='Classical ML',    alpha=0.92,
            bottom=dl)
p3 = ax.bar(x, hybrid, color=LIGHT,  width=w, label='Hybrid',          alpha=0.92,
            bottom=[a+b for a,b in zip(dl,cml)])
p4 = ax.bar(x, trad,   color=GREEN,  width=w, label='Traditional CV',  alpha=0.92,
            bottom=[a+b+c for a,b,c in zip(dl,cml,hybrid)])

def label_seg(patches, vals, bottoms):
    for patch, val, bot in zip(patches, vals, bottoms):
        if val > 0:
            ax.text(patch.get_x() + patch.get_width()/2,
                    bot + val/2,
                    f'{val}%', ha='center', va='center',
                    fontsize=10, fontweight='bold', color='white')

label_seg(p1, dl,     [0, 0, 0])
label_seg(p2, cml,    dl)
label_seg(p3, hybrid, [a+b for a,b in zip(dl,cml)])
label_seg(p4, trad,   [a+b+c for a,b,c in zip(dl,cml,hybrid)])

ax.set_xticks(x)
ax.set_xticklabels(periods, fontsize=10)
ax.set_ylabel('Proportion of studies within period (%)', fontsize=12, labelpad=6)
ax.set_ylim(0, 115)
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=6, loc='upper right', framealpha=0.9, edgecolor='#cccccc')

ax.set_title(
    'Fig. 8. Temporal evolution of AI modelling approaches by publication period\n'
    '(100% stacked bar; cross-tabulation; n = 28).\n'
    'Caution: the \u2018before 2020\u2019 period contains only 2 studies; '
    'proportional values are illustrative only.',
    fontsize=10, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('./figures/Fig08_temporal_evolution.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 8 saved")
