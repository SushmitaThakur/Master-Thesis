import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['LED64', 'LED128', 'Present80', 'Present128', 'Piccolo80', 'Piccolo128']
implementation_types = ['Table', 'Vperm', 'Bitslice']

# Energy consumption data (watts)
energy_data = np.array([
    [20.2, 23.6, 22.1],
    [22.8, 23.9, 23.1],
    [23.2, 22.2, 21],
    [20.1, 23.7, 23.2],
    [20.7, 24, 21.4],
    [23.8, 21.6, 22.9]
])

# Performance data (cycles per byte)
performance_data = np.array([
    [128.9, 73.8, 38.42],
    [187.5, 112.8, 50.54],
    [222.8, 130.2, 40.3],
    [225.04, 133.8, 45.54],
    [156.2, 71.94, 34.3],
    [201.1, 89.1, 36.5]
])

# Plotting
bar_width = 0.35
bar_positions_energy = np.arange(len(algorithms))
bar_positions_performance = bar_positions_energy + bar_width

fig, ax1 = plt.subplots(figsize=(15, 10))

# Energy consumption bars
colors_energy = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
for i, algo_data in enumerate(energy_data.T):
    bars_energy = ax1.bar(
        bar_positions_energy + i * bar_width,
        algo_data,
        width=bar_width,
        label=f'{implementation_types[i]}',
        color=colors_energy[i],
        edgecolor='black'  # Add black borders for better visibility
    )

# Performance bars
colors_performance = ['#d62728', '#9467bd', '#8c564b']  # Red, Purple, Brown
ax2 = ax1.twinx()  # Create a second y-axis sharing the same x-axis
for i, algo_data in enumerate(performance_data.T):
    bars_performance = ax2.bar(
        bar_positions_performance + i * bar_width,
        algo_data,
        width=bar_width,
        label=f'{implementation_types[i]}',
        color=colors_performance[i],
        hatch='//',
        edgecolor='black'  # Add black borders for better visibility
    )

# Customizing the plot
ax1.set_xticks(bar_positions_energy + (len(implementation_types) - 1) * bar_width / 2)
ax1.set_xticklabels(algorithms, rotation=45, ha='right')
ax1.set_xlabel('Algorithms')
ax1.set_ylabel('Energy Consumption (watts)', color='black')
ax2.set_ylabel('Performance (Cycles per Byte)', color='black')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.tight_layout()
plt.show()
