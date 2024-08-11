import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['LED64', 'LED128', 'Present80', 'Present128', 'Piccolo80', 'Piccolo128']
table_values = [20.2, 22.8, 23.2, 20.1, 20.7, 23.8]
vperm_values = [23.6, 23.9, 22.2, 23.7, 24, 21.6]
bitslice_values = [22.1, 23.1, 21, 23.2, 21.4, 22.9]

# Plotting
bar_width = 0.1
bar_positions = np.arange(len(algorithms))

fig, ax = plt.subplots(figsize=(10, 6))

bars_table = ax.bar(bar_positions - bar_width, table_values, bar_width, label='Table', color='lightblue')
bars_vperm = ax.bar(bar_positions, vperm_values, bar_width, label='Vperm', color='lightgreen')
bars_bitslice = ax.bar(bar_positions + bar_width, bitslice_values, bar_width, label='Bitslice', color='lightcoral')


# Customizing the plot
ax.set_xticks(bar_positions)
ax.set_xticklabels(algorithms)
ax.set_xlabel('Algorithms')
ax.set_ylabel('Energy Consumption (watts)')
ax.legend()
ax.grid(axis='y')
ax.set_title('Energy Consumption for Different Algorithms and Implementation Types')

# Show the plot
plt.tight_layout()
plt.show()
