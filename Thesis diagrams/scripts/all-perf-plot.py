import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['LED64', 'LED128', 'Present80', 'Present128', 'Piccolo80', 'Piccolo128']
implementation_types = ['Table', 'Vperm', 'Bitslice']

# Performance data (cycles per byte)
performance_data = np.array([
    [128.9, 73.8, 38.42],
    [187.5, 112.8, 50.54],
    [222.8, 130.2, 40.3],
    [225.04, 133.8, 45.54],
    [156.2, 71.94, 34.3],
    [201.1, 89.1, 36.5]
])

# Separate performance data into arrays for Table, Vperm, and Bitslice
table_data = performance_data[:, 0::3].flatten()
vperm_data = performance_data[:, 1::3].flatten()
bitslice_data = performance_data[:, 2::3].flatten()

# Plotting
bar_width = 0.25
bar_positions = np.arange(len(algorithms))

fig, ax = plt.subplots(figsize=(12, 8))

# Performance bars for Table
bars_table = ax.bar(
    bar_positions - bar_width,
    table_data,
    width=bar_width,
    label='Table',
    color='lightblue'
)

# Performance bars for Vperm
bars_vperm = ax.bar(
    bar_positions,
    vperm_data,
    width=bar_width,
    label='Vperm',
    color='lightgreen'
)

# Performance bars for Bitslice
bars_bitslice = ax.bar(
    bar_positions + bar_width,
    bitslice_data,
    width=bar_width,
    label='Bitslice',
    color='lightcoral'
)

# Customizing the plot
ax.set_xticks(bar_positions)
ax.set_xticklabels(algorithms)
ax.set_xlabel('Algorithms')
ax.set_ylabel('Performance (Cycles per Byte)')
ax.legend()
ax.grid(axis='y')
ax.set_title('Performance Comparison for LED, PRESENT, Piccolo across different Implementation Types')

# Show the plot
plt.tight_layout()
plt.show()

