# -----------------------------------------------------------------------------
# Copyright (C) 2026 Salvador de la Torre Gonzalez
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import os

import matplotlib.pyplot as plt
import pandas as pd

# Set global font sizes
plt.rcParams.update({
    'font.size': 16,
    'axes.titlesize': 20,
    'axes.labelsize': 18,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 14,
    'figure.titlesize': 22
})

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'out', 'datos_finales.csv')
OUT_DIR = os.path.join(BASE_DIR, 'plots')
days = 30.1  # Maximum time to plot (None to plot everything)

os.makedirs(OUT_DIR, exist_ok=True)

df = pd.read_csv(CSV_PATH)
df.columns = df.columns.str.strip()  # The CSV header has leading spaces in some columns
print("Columns:", list(df.columns))
if days is not None:
    df = df[df['total_days'] <= days]
t = df['total_days']

COLORS = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']


def finish(ax, title, xlabel='Time (days)', ylabel=None, filename=None, legend_axes=None):
    ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    ax.set_title(title)
    handles, labels = [], []
    for a in (legend_axes or [ax]):
        h, l = a.get_legend_handles_labels()
        handles += h
        labels += l
    ax.legend(handles, labels, loc='best')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    if filename:
        plt.savefig(os.path.join(OUT_DIR, filename), dpi=300, bbox_inches='tight')
    plt.show()


# --- Tumor & alive CART cells ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, df['num_tumor_cells'], color='red', linewidth=2, label='Tumor Cells')
ax.plot(t, df['num_alive_cart'], color='green', linewidth=2, label='Alive CART Cells')
finish(ax, 'Tumor & Alive CART Cells Over Time', ylabel='Number of Cells', filename='num_cells.png')

# --- Tumor cell types: absolute numbers ---
cell_types = [
    ('tumor_cells_type1', 'Type 1'),
    ('tumor_cells_type2', 'Type 2'),
    ('tumor_cells_type3', 'Type 3'),
    ('tumor_cells_type4', 'Type 4'),
    ('tumor_cells_type5_dead', 'Type 5 (Dead)')
]

fig, ax = plt.subplots(figsize=(12, 7))
for color, (col, label) in zip(COLORS, cell_types):
    ax.plot(t, df[col], color=color, linewidth=2, label=f'{label} (Abs)')
finish(ax, 'Absolute Number of Each Tumor Cell Type Over Time', ylabel='Number of Cells',
       filename='type_of_cells_absolute_numbers.png')

# --- Tumor cell types: percentage ---
fig, ax = plt.subplots(figsize=(12, 7))
for color, (col, label) in zip(COLORS, cell_types):
    ax.plot(t, 100 * df[col] / df['num_tumor_cells'], color=color, linewidth=2, label=f'{label} (%)')
finish(ax, 'Percentage of Each Tumor Cell Type Over Time', ylabel='Percentage of Tumor Cells (%)',
       filename='type_of_cells_porcentage_populations.png')

# --- Oncoprotein & oxygen (twin axes) ---
fig, ax_onco = plt.subplots(figsize=(10, 6))
ax_oxy = ax_onco.twinx()
ax_onco.plot(t, df['average_oncoprotein'], color='#e41a1c', linewidth=2, label='Oncoprotein')
ax_oxy.plot(t, df['average_level_of_oxygen_cancer_cells'], color='#377eb8', linewidth=2, label='Oxygen')
ax_onco.set_ylabel('Average Oncoprotein Level', color='#e41a1c')
ax_oxy.set_ylabel('Average Oxygen Level', color='#377eb8')
ax_onco.tick_params(axis='y', labelcolor='#e41a1c')
ax_oxy.tick_params(axis='y', labelcolor='#377eb8')
finish(ax_onco, 'Average Oncoprotein & Oxygen Levels Over Time',
       filename='oncoprotein_and_oxygen.png', legend_axes=[ax_onco, ax_oxy])

# --- Tumor cells & tumor radius (twin axes) ---
fig, ax_cells = plt.subplots(figsize=(10, 6))
ax_radius = ax_cells.twinx()
ax_cells.plot(t, df['num_tumor_cells'], color='red', linewidth=2, label='Tumor Cells')
ax_radius.plot(t, df['tumor_radius'], color='purple', linewidth=2, label='Tumor Radius')
ax_cells.set_ylabel('Number of Tumor Cells', color='red')
ax_radius.set_ylabel('Tumor Radius', color='purple')
ax_cells.tick_params(axis='y', labelcolor='red')
ax_radius.tick_params(axis='y', labelcolor='purple')
finish(ax_cells, 'Tumor Cells and Tumor Radius Over Time',
       filename='num_cells_and_tumor_radius.png', legend_axes=[ax_cells, ax_radius])

print(f"Plots saved in '{OUT_DIR}'")

