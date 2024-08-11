import datetime
import matplotlib.pyplot as plt

# Data for GIFT64 and GIFT128 (averages)
configurations = ['Basic', 'Level-1', 'Level-2', 'Level-3', 'March Native', 'Function Inlining', 'Loop Vectorization', 'Loop Unrolling']

gift64_averages = [17.6, 16.7, 14.6, 16.2, 17.6, 16.5, 16.9, 16.4]
gift128_averages = [21.2, 16.4, 22.3, 23.6, 26.0, 28.5, 18.2, 26.9]

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(configurations, gift64_averages, marker='o', label='GIFT64')
plt.plot(configurations, gift128_averages, marker='o', label='GIFT128')

plt.title('Average Energy Consumption for GIFT64 and GIFT128 Across Compiler Configurations')
plt.xlabel('Compiler Configurations')
plt.ylabel('Average Energy Consumption (joules)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()

fig = plt.get_figure()

# Get current date and time
current_datetime = datetime.now()
# Format and print the current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# fig.savefig("./plots/AllCiphers-{time}.png".format(time=formatted_datetime)) 
fig.savefig("./plots/gift-{time}.png".format(time=formatted_datetime)) 