import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['Piccolo80', 'Piccolo128']
implementation_types = ['Table', 'Vperm', 'Bitslice']

# Energy consumption data (joules)
energy_data = np.array([
    [20.7, 24, 21.4],
    [23.8, 21.6, 22.9]
])

# Performance data (cycles per byte)
performance_data = np.array([
    [156.2, 71.94, 34.3],
    [201.1, 89.1, 36.5]
])

# Plotting
bar_width = 0.4
bar_positions = np.arange(len(algorithms))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Energy consumption bars
bars_energy_table = ax1.bar(bar_positions - bar_width / 2, energy_data[:, 0], bar_width, label='Energy - Table', color='lightblue')
bars_energy_vperm = ax1.bar(bar_positions, energy_data[:, 1], bar_width, label='Energy - Vperm', color='lightgreen')
bars_energy_bitslice = ax1.bar(bar_positions + bar_width / 2, energy_data[:, 2], bar_width, label='Energy - Bitslice', color='lightcoral')

# Creating a second y-axis for performance data
ax2 = ax1.twinx()
bars_performance_table = ax2.bar(bar_positions - bar_width / 2, performance_data[:, 0], bar_width, label='Performance - Table', alpha=0.5, color='blue', hatch='//')
bars_performance_vperm = ax2.bar(bar_positions, performance_data[:, 1], bar_width, label='Performance - Vperm', alpha=0.5, color='green', hatch='//')
bars_performance_bitslice = ax2.bar(bar_positions + bar_width / 2, performance_data[:, 2], bar_width, label='Performance - Bitslice', alpha=0.5, color='red', hatch='//')

# Customizing the plot
ax1.set_xticks(bar_positions)
ax1.set_xticklabels(algorithms)
ax1.set_xlabel('Piccolo Algorithms')
ax1.set_ylabel('Energy Consumption (joules)', color='black')
ax2.set_ylabel('Performance (Cycles per Byte)', color='black')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.set_title('Energy and Performance Comparison for Piccolo Algorithms and Implementation Types')

# Show the plot
plt.tight_layout()
plt.show()
