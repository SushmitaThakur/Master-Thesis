import matplotlib.pyplot as plt
import numpy as np

# Data
algorithms = ['LED64', 'LED128', 'Present80', 'Present128', 'Piccolo80', 'Piccolo128', 'AES128', 'AES192', 'AES256']
implementation_types = ['Table(basic for AES)', 'Vperm(tiny for AES)', 'Bitslice']

# Energy consumption data (watts)
energy_data = np.array([
    [20.2, 23.6, 22.1],
    [22.8, 23.9, 23.1],
    [23.2, 22.2, 21],
    [20.1, 23.7, 23.2],
    [20.7, 24, 21.4],
    [23.8, 21.6, 22.9],
    [27, 18.1, 21.3],
    [29.8, 18.3, np.nan],  # np.nan for missing data in AES192
    [27.7, 19.3, np.nan]   # np.nan for missing data in AES256
])

# Plotting
bar_width = 0.2
bar_positions = np.arange(len(algorithms))

fig, ax = plt.subplots(figsize=(15, 8))

# Energy consumption bars with better colors
colors = ['lightblue', 'lightgreen', 'lightcoral']  
for i, algo_data in enumerate(energy_data.T):
    bars = ax.bar(
        bar_positions + i * bar_width,
        algo_data,
        width=bar_width,
        label=f'{implementation_types[i]}',
        color=colors[i],
        edgecolor='black'  # Add black borders for better visibility
    )

# Customizing the plot
ax.set_xticks(bar_positions + (len(implementation_types) - 1) * bar_width / 2)
ax.set_xticklabels(algorithms, rotation=45, ha='right')
ax.set_xlabel('Algorithms')
ax.set_ylabel('Energy Consumption (joules)')
ax.legend()
ax.grid(axis='y')
ax.set_title('Energy Consumption for Different Algorithms and Implementation Types')

# Show the plot
plt.tight_layout()
plt.show()