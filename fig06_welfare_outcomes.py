"""
Fig. 6 — Welfare outcome categories mapped to Five Domains Model
Animal journal: 300 DPI TIFF
Key fix: absent domains shown explicitly in grey with red italic 'not addressed' label
Five Domains colour-coding: each bar coloured by domain assignment
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Updated font to Arial as per journal formatting guidelines
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#333333',
})

# Five Domains colours
DOM_COLORS = {
    'Behavioural Interactions': '#1B3F6E',
    'Health':                   '#C55A11',
    'Mental State':              '#7030A0',
    'Nutrition':                 '#375623',
    'Physical Environment':      '#808080',
}

# (label, count, domain, is_present)
rows = [
    ('Behavioural measures\n(primary welfare outcome)',   26, 'Behavioural Interactions', True),
    ('Activity patterns',                                  15, 'Behavioural Interactions', True),
    ('Posture / lying / standing',                         11, 'Behavioural Interactions', True),
    ('Feeding / rumination behaviour',                      6, 'Behavioural Interactions', True),
    ('Social behaviour',                                    5, 'Behavioural Interactions', True),
    ('Stress-related behaviour',                            3, 'Mental State',             True),
    ('Lameness / gait (Health)',                            1, 'Health',                   True),
    ('Disease / health indicators',                         1, 'Health',                   True),
    ('Pain / nociception — FAU-based\n(Mental State)',      0, 'Mental State',             False),
    ('Affective state / fear\n(Mental State)',               0, 'Mental State',             False),
    ('Body condition score\n(Health)',                       0, 'Health',                   False),
    ('Thermal comfort /\nenvironment (Physical Env.)',       0, 'Physical Environment',     False),
    ('Feed / water access\n(Nutrition)',                     0, 'Nutrition',                False),
]

labels  = [r[0] for r in rows]
counts  = [r[1] for r in rows]
domains = [r[2] for r in rows]
present = [r[3] for r in rows]

bar_colors = [DOM_COLORS[d] if p else '#CCCCCC'
              for d, p in zip(domains, present)]

fig, ax = plt.subplots(figsize=(14, 9.5))
y = np.arange(len(labels))

bars = ax.barh(y, counts, color=bar_colors, height=0.65,
               edgecolor='white', linewidth=0.5)

for i, (bar, n, p) in enumerate(zip(bars, counts, present)):
    if n > 0:
        ax.text(bar.get_width() + 0.3,
                bar.get_y() + bar.get_height()/2,
                f'n = {n}  ({round(n/28*100)}%)',
                va='center', fontsize=9.5,
                fontweight='bold', color='#111111')
    else:
        ax.text(0.4, bar.get_y() + bar.get_height()/2,
                'Not addressed in any included study',
                va='center', fontsize=9,
                color='#c0392b', style='italic')

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel('Number of included studies (multi-select; n = 28 total)',
              fontsize=10, labelpad=8)
ax.set_xlim(0, 34)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Gap separator line: Positioned text cleanly to avoid collision with lines
ax.axhline(y=7.5, color='#c0392b', linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(33.5, 7.1, 'Evidence\ngap below',
        fontsize=8, color='#c0392b', ha='right', va='bottom', style='italic', fontweight='bold')

# Domain legend
legend_patches = [
    mpatches.Patch(facecolor=DOM_COLORS[d], label=d, alpha=0.88)
    for d in DOM_COLORS
]
legend_patches.append(
    mpatches.Patch(facecolor='#CCCCCC', alpha=0.6,
                   label='Not addressed in any study'))
ax.legend(handles=legend_patches,
          title='Five Domains Model domain',
          title_fontsize=9, fontsize=8.5,
          loc='lower right', framealpha=0.92,
          edgecolor='#cccccc')

ax.set_title(
    'Fig. 6. Welfare outcome categories across included studies (n = 28),\n'
    'colour-coded by Five Domains Model domain (Mellor, 2017).\n'
    'Grey bars indicate outcomes absent from all included studies. See Table 3.',
    fontsize=10, fontweight='bold', pad=15)

# Expanded left margin layout adjustment for long multiline labels
plt.tight_layout()
plt.subplots_adjust(left=0.32)

plt.savefig('./figures/Fig06_welfare_outcomes.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig 6 saved successfully with updated font and clean spacing layout!")