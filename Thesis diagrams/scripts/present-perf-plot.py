import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['Present80', 'Present128']
implementation_types = ['Table', 'Vperm', 'Bitslice']

# Energy consumption data (joules)
energy_data = np.array([
    [23.2, 22.2, 21],
    [20.1, 23.7, 23.2]
])

# Performance data (cycles per byte)
performance_data = np.array([
    [222.8, 130.2, 40.3],
    [225.04, 133.8, 45.54]
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
ax1.set_xlabel('Present Algorithms')
ax1.set_ylabel('Energy Consumption (joules)', color='black')
ax2.set_ylabel('Performance (Cycles per Byte)', color='black')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.set_title('Energy and Performance Comparison for Present Algorithms and Implementation Types')

# Show the plot
plt.tight_layout()
plt.show()
