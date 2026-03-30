"""
Supplementary Fig. S2 — Evidence landscape bubble chart
Animal journal: 300 DPI TIFF
x = year, y = species, colour = model family, size = performance tier
Diamond marker for studies with no reported performance metric
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
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
ORANGE= '#C55A11'
GREEN = '#2E7D32'
PURPLE= '#7030A0'
TEAL  = '#00695C'

# Model family codes: 0=YOLO, 1=CNN-TL, 2=OtherDL, 3=ClassML, 4=CNNcustom, 5=Pose, 6=RNN
# Species y: Cattle=3, Sheep/Lambs=2, Goats=1, Cattle&Pig=0
# Perf tier: 0=not reported, 1=<85%, 2=85-94%, 3=>=95%
studies = [
    (2015,3,2,3),(2018,3,3,4),(2020,3,0,2),(2020,3,3,4),
    (2021,3,0,2),(2022,3,2,1),(2022,2,2,0),(2023,3,0,2),
    (2023,2,3,4),(2023,2,2,1),(2023,3,3,5),(2024,3,3,0),
    (2024,0,3,0),(2024,2,3,0),(2024,2,3,0),(2024,3,0,2),
    (2024,3,0,3),(2024,3,2,3),(2024,3,3,0),(2024,3,3,0),
    (2024,3,3,0),(2024,1,3,0),(2024,3,3,0),(2025,3,3,0),
    (2025,3,3,2),(2025,2,2,6),(2025,3,0,0),(2025,3,3,2),
]

model_colors = {0:DARK,1:MID,2:LIGHT,3:ORANGE,4:GREEN,5:PURPLE,6:TEAL}
model_labels = {
    0:'YOLO family',1:'CNN (transfer learning)',2:'Other deep learning',
    3:'Classical ML',4:'CNN (custom)',5:'Pose estimation',6:'RNN / optical flow'
}
tier_sizes = {0:80, 1:160, 2:380, 3:640}
tier_labels = {0:'Not reported',1:'<85%',2:'85\u201394%',3:'\u226595%'}

fig, ax = plt.subplots(figsize=(15, 8))

np.random.seed(42)
for year, sp_y, perf, model in studies:
    jx = np.random.uniform(-0.12, 0.12)
    jy = np.random.uniform(-0.10, 0.10)
    marker = 'D' if perf == 0 else 'o'
    ax.scatter(year+jx, sp_y+jy,
               s=tier_sizes[perf],
               c=model_colors[model],
               alpha=0.82, edgecolors='white', linewidths=1.2,
               marker=marker, zorder=3)

ax.set_xlabel('Publication year', fontsize=12, labelpad=8)
ax.set_xlim(2014, 2026)
ax.set_xticks(range(2015, 2026))
ax.set_xticklabels([str(y) for y in range(2015, 2026)], fontsize=10)

sp_labels = {0:'Cattle\n& Pig', 1:'Goats', 2:'Sheep /\nLambs', 3:'Cattle'}
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels([sp_labels[i] for i in [0,1,2,3]],
                   fontsize=11, fontweight='bold')
ax.set_ylim(-0.65, 3.85)
ax.xaxis.grid(True, linestyle='--', alpha=0.22)
ax.yaxis.grid(True, linestyle='--', alpha=0.22)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Horizontal species separators
for yv in [0.5, 1.5, 2.5]:
    ax.axhline(yv, color='#CCCCCC', linewidth=0.8, zorder=0)

# Legend: model family
model_handles = [
    mpatches.Patch(facecolor=model_colors[i], label=model_labels[i], alpha=0.85)
    for i in sorted(model_labels)
]
leg1 = ax.legend(handles=model_handles,
                 title='AI model family', title_fontsize=9,
                 fontsize=8.5, loc='upper left',
                 framealpha=0.92, edgecolor='#cccccc')
ax.add_artist(leg1)

# Legend: performance tier (size)
tier_handles = [
    mlines.Line2D([],[],marker='o', color='w', markerfacecolor='#595959',
                  markersize=np.sqrt(tier_sizes[t]/np.pi)*1.9,
                  label=tier_labels[t])
    for t in [0, 1, 2, 3]
]
tier_handles.append(
    mlines.Line2D([],[],marker='D', color='w', markerfacecolor='#595959',
                  markersize=8, label='\u25c6 = performance not reported'))
ax.legend(handles=tier_handles,
          title='Best performance metric tier', title_fontsize=9,
          fontsize=8.5, loc='upper right',
          framealpha=0.92, edgecolor='#cccccc')

ax.set_title(
    'Supplementary Fig. S2. Evidence landscape bubble chart for included studies (n = 28).\n'
    'x-axis = publication year; y-axis = target species; bubble colour = AI model family;\n'
    'bubble size = best performance tier (\u226485%, 85\u201394%, \u226595%); '
    '\u25c6 = performance not reported. Slight jitter applied for readability.',
    fontsize=10, fontweight='bold', pad=12)

plt.tight_layout()
plt.savefig('./figures/FigS2_bubble_landscape.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("Fig S2 saved")
