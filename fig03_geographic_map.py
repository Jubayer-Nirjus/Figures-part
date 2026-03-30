"""
Fig. 3 — Geographic distribution: proper world map using matplotlib basemap approach
Animal journal: 300 DPI TIFF, standard cartographic style
NOTE: Uses simplified continent polygons drawn with matplotlib patches.
For production, replace with geopandas shapefile if available.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.linewidth': 0.6,
})

DARK   = '#1B3F6E'
MID    = '#2E75B6'
LIGHT  = '#9DC3E6'
LAND   = '#D4E6C3'
OCEAN  = '#E8F4FD'
BORDER = '#aaaaaa'

fig, ax = plt.subplots(figsize=(16, 9), facecolor=OCEAN)
ax.set_facecolor(OCEAN)

# Simplified continent polygons (approximate bounding shapes)
from matplotlib.patches import FancyBboxPatch, Polygon

continent_data = [
    # (x, y, width, height, label)
    (-170, 15, 115, 75, 'North\nAmerica'),
    (-82,  -56, 50, 70, 'South\nAmerica'),
    (-25,  35,  55, 35, 'Europe'),
    (-20,  -36, 70, 74, 'Africa'),
    (25,   0,   150,75, 'Asia'),
    (110,  -48, 60, 40, 'Oceania'),
]
for (x, y, w, h, lbl) in continent_data:
    rect = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=3",
                           facecolor=LAND, edgecolor=BORDER,
                           linewidth=0.5, zorder=1)
    ax.add_patch(rect)

# Country data: (lon, lat, n_studies, label, label_offset_x, label_offset_y)
countries = [
    (-100, 40,  4, 'USA\nn = 4',              6,  2),
    ( -80,-15,  2, 'Brazil\nn = 2',            5, -5),
    (-100, 23,  1, 'Mexico\nn = 1',            5, -5),
    ( -65, 50,  2, 'Canada\nn = 2',            5,  2),
    (  12, 42,  4, 'Italy\nn = 4',             5,  2),
    (  10, 51,  1, 'Germany\nn = 1',            5,  2),
    (  -4, 40,  1, 'Spain\nn = 1',             -8,-5),
    (  16, 47,  1, 'Austria /\nHungary n = 1',-18,-7),
    (  18, 61,  1, 'Sweden\nn = 1',            5,  2),
    (  28, 64,  1, 'Finland\nn = 1',           5,  2),
    (  35, 39,  1, 'Turkey\nn = 1',            5, -5),
    ( 104, 35,  7, 'China\nn = 7',             5,  3),
    ( 128, 36,  3, 'South Korea\nn = 3',        5, -5),
    ( 110,  4,  1, 'Malaysia\nn = 1',           5, -5),
    ( 117, -5,  1, 'Indonesia\nn = 1',          5, -7),
]

def bubble_size(n):
    return {1: 80, 2: 200, 3: 350, 4: 480, 7: 900}.get(n, n * 120)

def bubble_color(n):
    if n >= 4: return DARK
    if n >= 2: return MID
    return LIGHT

for lon, lat, n, label, ox, oy in countries:
    ax.scatter(lon, lat, s=bubble_size(n), c=bubble_color(n),
               alpha=0.88, edgecolors='white', linewidths=1.2, zorder=5)
    ax.annotate(label, (lon, lat),
                xytext=(lon + ox, lat + oy),
                fontsize=7.5, ha='left', va='center', color='#111111',
                arrowprops=dict(arrowstyle='-', color='#888888', lw=0.6),
                zorder=6)

# Zero-study regions
zero_regions = [
    ( 78,  22, 'South Asia\n(0 studies)'),
    ( 22, -12, 'Sub-Saharan Africa\n(0 studies)'),
    (120, -25, 'Southeast Asia /\nOceania (0 studies)'),
]
for lx, ly, lbl in zero_regions:
    ax.text(lx, ly, lbl, fontsize=8.5, color='#c0392b',
            ha='center', style='italic', alpha=0.85, zorder=6)

ax.set_xlim(-175, 185)
ax.set_ylim(-65, 85)
ax.set_xlabel('Longitude', fontsize=10)
ax.set_ylabel('Latitude', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.2, color='#999999')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend
l1 = mpatches.Patch(facecolor=DARK,   label='\u22654 studies')
l2 = mpatches.Patch(facecolor=MID,    label='2\u20133 studies')
l3 = mpatches.Patch(facecolor=LIGHT,  label='1 study')
l4 = mpatches.Patch(facecolor='#c0392b', alpha=0.35,
                    label='0 studies (region label in red)')
ax.legend(handles=[l1, l2, l3, l4],
          title='Studies per country', title_fontsize=9,
          fontsize=9, loc='lower left', framealpha=0.92,
          edgecolor='#cccccc')

ax.set_title(
    'Fig. 3. Geographic distribution of included studies by country of institutional affiliation (n = 28).\n'
    'Bubble size proportional to number of studies per country. Multi-country collaborations disaggregated.\n'
    'Red italic labels indicate regions with zero representation despite hosting the largest global ruminant '
    'populations (FAO, 2023).',
    fontsize=10, fontweight='bold', pad=10, loc='center')

plt.tight_layout()
plt.savefig('./figures/Fig03_geographic_map.tiff',
            format='tiff', dpi=300, bbox_inches='tight', facecolor=OCEAN)
plt.close()
print("Fig 3 saved")
