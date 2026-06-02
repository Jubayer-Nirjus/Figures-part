"""
Fig. PRISMA — Study Selection Flow Diagram (2020 Guidelines)
Animal journal: 300 DPI TIFF / PNG
Enhanced layout to prevent overlaps with dual-column database layout
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Consistent Journal Typography Settings
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 10,
    'axes.linewidth': 0.8,
})

# Premium Color Palette matching other manuscript figures
DARK_BLUE   = '#1B3F6E'
MID_BLUE    = '#2E75B6'
LIGHT_BLUE  = '#F4F8FA'
BORDER_CLR  = '#2E75B6'
TEXT_MAIN   = '#1A1A1A'
TEXT_MUTED  = '#444444'

# Expanded figsize height to 17 to give structural breathing room
fig, ax = plt.subplots(figsize=(13, 17))
ax.set_xlim(0, 13)
ax.set_ylim(0, 17)
ax.axis('off')

# Helper function to draw clean PRISMA boxes
def draw_box(ax, x, y, w, h, facecolor=LIGHT_BLUE, edgecolor=BORDER_CLR, linewidth=1.5):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                  facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth, zorder=3)
    ax.add_patch(rect)

# Helper function for side header panels
def draw_side_header(ax, x, y, w, h, text):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                  facecolor=DARK_BLUE, edgecolor=DARK_BLUE, zorder=3)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, color='white', fontsize=11, fontweight='bold',
            ha='center', va='center', rotation=90)

# Helper function for perfect directional flow arrows
def draw_arrow(ax, x1, y1, x2, y2, arrow_type='down'):
    if arrow_type == 'down':
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), zorder=2,
                    arrowprops=dict(arrowstyle="-|>", color=MID_BLUE, lw=1.8, 
                                    mutation_scale=12, shrinkA=0, shrinkB=0))
    elif arrow_type == 'right':
        ax.plot([x1, x2, x2], [y1, y1, y2+0.1], color=MID_BLUE, lw=1.8, zorder=2)
        ax.annotate('', xy=(x2, y2), xytext=(x2, y2+0.12), zorder=2,
                    arrowprops=dict(arrowstyle="-|>", color=MID_BLUE, lw=1.8, 
                                    mutation_scale=12, shrinkA=0, shrinkB=0))

# ==========================================
# 1. SIDE SECTOR HEADER PANELS (Left Margin)
# ==========================================
draw_side_header(ax, 0.2, 12.0, 0.5, 4.2, 'Identification')
draw_side_header(ax, 0.2, 3.8,  0.5, 7.6, 'Screening')
draw_side_header(ax, 0.2, 1.2,  0.5, 2.0, 'Included')

# ==========================================
# 2. DATA BOXES & MULTI-COLUMN TEXT CONTENT
# ==========================================

# --- IDENTIFICATION STAGE ---
# Box 1: Databases - Re-engineered into Two Clean Columns to eliminate vertical overflow
b1_x, b1_y, b1_w, b1_h = 1.2, 12.2, 5.0, 3.8
draw_box(ax, b1_x, b1_y, b1_w, b1_h)
ax.text(b1_x + 0.2, b1_y + b1_h - 0.4, "Studies from databases/registers (n = 3129)", 
        color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')

# Left Column Databases
db_left = [
    "Scopus (n = 2413)", "IEEE Xplore (n = 384)", "PubMed (n = 121)", 
    "Web of Science (n = 79)", "Google Scholar (n = 48)", 
    "ACM Digital Library (n = 30)", "PsycINFO (n = 11)"
]
y_offset = b1_y + b1_h - 0.8
for db in db_left:
    ax.text(b1_x + 0.3, y_offset, f"• {db}", color=TEXT_MUTED, fontsize=9.5, va='center')
    y_offset -= 0.4

# Right Column Databases
db_right = [
    "Embase (n = 9)", "CINAHL (n = 8)", "CENTRAL (n = 8)", 
    "MEDLINE (n = 8)", "ClinicalTrials.gov (n = 7)", 
    "Citation searching (n = 2)", "WHO (n = 1)"
]
y_offset = b1_y + b1_h - 0.8
for db in db_right:
    ax.text(b1_x + 2.7, y_offset, f"• {db}", color=TEXT_MUTED, fontsize=9.5, va='center')
    y_offset -= 0.4

# Box 2: Duplicate Removal Box
b2_x, b2_y, b2_w, b2_h = 7.0, 12.6, 5.2, 2.2
draw_box(ax, b2_x, b2_y, b2_w, b2_h)
ax.text(b2_x + 0.2, b2_y + b2_h - 0.35, "References removed (n = 239)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')
rep_texts = [
    "Duplicates identified manually (n = 11)",
    "Duplicates identified by Covidence (n = 228)",
    "Marked ineligible by automation tools (n = 0)"
]
y_offset = b2_y + b2_h - 0.8
for txt in rep_texts:
    ax.text(b2_x + 0.4, y_offset, f"• {txt}", color=TEXT_MUTED, fontsize=9.5, va='center')
    y_offset -= 0.45


# --- SCREENING STAGE (Perfect spacing matrix applied) ---

# Screened
draw_box(ax, 1.2, 10.2, 3.8, 0.8)
ax.text(1.4, 10.6, "Studies screened\n(n = 2672)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')

draw_box(ax, 7.0, 10.2, 3.8, 0.8)
ax.text(7.2, 10.6, "Studies excluded\n(n = 2547)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')

# Retrieval
draw_box(ax, 1.2, 8.6, 3.8, 0.8)
ax.text(1.4, 9.0, "Studies sought for retrieval\n(n = 125)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')

draw_box(ax, 7.0, 8.6, 3.8, 0.8)
ax.text(7.2, 9.0, "Studies not retrieved\n(n = 0)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')

# Eligibility
draw_box(ax, 1.2, 7.0, 3.8, 0.8)
ax.text(1.4, 7.4, "Studies assessed for eligibility\n(n = 125)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')

# Box: Re-refined Exclusions Box (Spaced safely down below)
b_exc_x, b_exc_y, b_exc_w, b_exc_h = 6.0, 3.8, 6.2, 2.6
draw_box(ax, b_exc_x, b_exc_y, b_exc_w, b_exc_h)
ax.text(b_exc_x + 0.3, b_exc_y + b_exc_h - 0.4, "Studies excluded (n = 97)", color=TEXT_MAIN, fontsize=10.5, fontweight='bold', va='center')
exclusions_list = [
    "No primary CV/ML sensor infrastructure (n = 47)",
    "Outside scope of target species/metrics (n = 36)",
    "Ineligible deployment contexts (n = 11)",
    "Non-primary research / Review articles (n = 3)",
    "No English translation available (n = 0)"
]
y_offset = b_exc_y + b_exc_h - 0.85
for items in exclusions_list:
    ax.text(b_exc_x + 0.5, y_offset, f"▪ {items}", color=TEXT_MUTED, fontsize=9.5, va='center')
    y_offset -= 0.4


# --- INCLUDED STAGE ---
draw_box(ax, 1.2, 1.8, 3.8, 0.8)
ax.text(1.4, 2.2, "Studies included in review\n(n = 28)", color=TEXT_MAIN, fontsize=11, fontweight='bold', va='center')


# ==========================================
# 3. ROUTING ARROWS AND CONNECTORS
# ==========================================
# Identification connectors
draw_arrow(ax, 3.7, 12.2, 3.7, 11.1)
draw_arrow(ax, 6.2, 14.1, 7.0, 13.7, arrow_type='right')

# Screening connectors
draw_arrow(ax, 3.1, 10.2, 3.1, 9.5)
draw_arrow(ax, 5.0, 10.6, 7.0, 10.6, arrow_type='right')

draw_arrow(ax, 3.1, 8.6, 3.1, 7.9)
draw_arrow(ax, 5.0, 9.0, 7.0, 9.0, arrow_type='right')

# Main pipeline and full exclusion connector routing
draw_arrow(ax, 3.1, 7.0, 3.1, 2.7)
draw_arrow(ax, 5.0, 7.4, 6.0, 5.1, arrow_type='right')


# Caption text block placement at the absolute base
ax.text(6.5, 0.5, 
        "Fig. PRISMA. Flow diagram mapping the systematic study identification, screening, eligibility,\n"
        "and inclusion process following the PRISMA 2020 guidelines. Final evidence base stabilized at n = 28.",
        fontsize=10, fontweight='bold', ha='center', style='italic', color='#222222')

plt.tight_layout()

# Save as high-res 300 DPI publication quality TIFF image
plt.savefig('./figures/Fig_PRISMA_flowchart.tiff', format='tiff', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("PRISMA Flowchart generated successfully with optimized dual-column layout and zero overlaps!")