import matplotlib.pyplot as plt

# Data
key_sizes = ['AES-128', 'AES-192', 'AES-256', 'AES-Tiny-128', 'AES-Tiny-192', 'AES-Tiny-256', 'AES-Bitslice-128']
energy_consumption = [27.0, 29.8, 27.7, 18.1, 18.3, 19.3, 21.3]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
line = ax.plot(key_sizes, energy_consumption, marker='o', linestyle='-', color='red')

# Customizing the plot
ax.set_xlabel('AES Variants')
ax.set_ylabel('Energy Consumption (joules)')
ax.set_title('Energy Consumption for Different AES Variants')
ax.grid(axis='y')

# Display the values on top of the line points
for i, val in enumerate(energy_consumption):
    plt.text(i, val, round(val, 1), ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()
