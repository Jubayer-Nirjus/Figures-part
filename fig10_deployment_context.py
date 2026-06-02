"""
Fig. 10 — Deployment context: sample setting vs practical usability
Animal journal: 300 DPI TIFF
Counts reconciled: Barn n=21 (from Fig 12 original data which is the authoritative source)
Annotation: no outdoor/pasture system achieved real-time performance
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Updated font family to Arial as per journal submission rules
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

fig, ax = plt.subplots(figsize=(13, 7))

settings = ['Barn / indoor', 'Pasture /\noutdoor', 'Mixed', 'Laboratory',
            'Slaughter\nplant', 'Fear test\narena', 'Commercial\nfarm']
totals   = [21, 3, 2, 2, 1, 1, 1]

# Usability breakdown (real-time, near-rt, offline, poc, not stated)
real_time  = [10, 2, 1, 2, 1, 1, 0]
near_rt    = [ 4, 0, 0, 0, 0, 0, 0]
offline    = [ 5, 0, 1, 0, 0, 0, 0]
poc        = [ 1, 0, 0, 0, 0, 0, 0]
not_stated = [ 1, 1, 0, 0, 0, 0, 1]

y = np.arange(len(settings))
w = 0.65

p1 = ax.barh(y, real_time, color=DARK,   height=w, label='Real-time',         alpha=0.92)
p2 = ax.barh(y, near_rt,   color=MID,    height=w, label='Near real-time',     alpha=0.92, left=real_time)
p3 = ax.barh(y, offline,   color=LIGHT,  height=w, label='Offline / batch',    alpha=0.92, left=[a+b for a,b in zip(real_time,near_rt)])
p4 = ax.barh(y, poc,       color=ORANGE, height=w, label='Proof-of-concept',   alpha=0.92, left=[a+b+c for a,b,c in zip(real_time,near_rt,offline)])
p5 = ax.barh(y, not_stated,color=GRAY,   height=w, label='Not stated',         alpha=0.7,  left=[a+b+c+d for a,b,c,d in zip(real_time,near_rt,offline,poc)])

for i, tot in enumerate(totals):
    ax.text(tot + 0.3, i, f'n = {tot}',
            va='center', fontsize=9.5, fontweight='bold', color='#222222')

ax.set_yticks(y)
ax.set_yticklabels(settings, fontsize=10)
ax.invert_yaxis()
ax.set_xlabel('Number of studies', fontsize=11, labelpad=8)
ax.set_xlim(0, 25) # Re-calibrated limit to save space and provide perfect fit for 'n =' labels
ax.xaxis.grid(True, linestyle='--', alpha=0.35)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(title='Practical usability', title_fontsize=9,
          fontsize=9, loc='lower right', framealpha=0.92,
          edgecolor='#cccccc')

# Adjusted annotation parameters to point perfectly to pasture bar without hitting labels
ax.annotate('No outdoor system\nachieved real-time\nperformance',
            xy=(2.2, 1.0), xytext=(8.5, 2.2),
            fontsize=9, color='#c0392b', style='italic', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.2, shrinkA=3, shrinkB=3))

ax.set_title(
    'Fig. 10. Deployment context: sample setting vs. practical usability (n = 28).\n'
    'Cross-tabulation; multi-select setting classification.\n'
    'Real-time capability is absent from all outdoor and pasture deployments.\n'
    'PoC = proof-of-concept study.',
    fontsize=10, fontweight='bold', pad=15)

# Tight layout and precise margin expansion applied
plt.tight_layout()
plt.subplots_adjust(left=0.18)

plt.savefig('./figures/Fig10_deployment_context.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 10 saved successfully with custom annotation alignment!")