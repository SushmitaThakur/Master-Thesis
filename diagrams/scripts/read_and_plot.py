import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import re

file_path = 'led.csv'


# Read data from CSV file
data = pd.read_csv(file_path)


# print ("hello")

# Plotting the graph
# x_values = data['Time']
# y_values = data['Joules']

# plt.plot(x_values, y_values)
# plt.xlabel('Time')
# plt.ylabel('Energy Consumed (in joules)')
# plt.title('Crypto-lib: All Ciphers')
# plt.grid(True)
# plt.show()

# To Do: read the time in mins:seconds only in the time column

results = pd.DataFrame(data, columns=['Time', 'Package Joules Consumed'])

# SNS needs the column values to be numeric to be able to plot the graph
# results['Time'] = pd.to_datetime(results['Time']).dt.time
# results['Time'] = pd.to_numeric(results['Time'])


# Define a regular expression pattern to match the date part
pattern = r"\d{4}-\d{2}-\d{2}\s"

# Apply re.sub to the 'Time' column
results['Time'] = results['Time'].apply(lambda x: re.sub(pattern, "", x))


print(results)

sns.set(style="whitegrid")

plot = sns.lineplot(data=results, x="Time", y="Package Joules Consumed") 
plot.set(xlabel='Time', ylabel='Energy Consumed (in joules)')
# plot.set(title="Crypto-lib: All Ciphers")
plot.set_xticks(results['Time'], rotation=90, fontsize=8)
plot.set(title="Crypto-lib: 3_LED")
fig = plot.get_figure()

# Get current date and time
current_datetime = datetime.now()
# Format and print the current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# fig.savefig("./plots/AllCiphers-{time}.png".format(time=formatted_datetime)) 
fig.savefig("./plots/3_LEDCiphers-{time}.png".format(time=formatted_datetime)) 
