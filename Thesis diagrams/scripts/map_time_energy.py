import re
from datetime import datetime, time
import csv

def is_time_in_range(check_time_str, start_time_str, end_time_str) -> bool:
    # Convert string representations to datetime.time objects
    check_time = datetime.strptime(check_time_str, "%H:%M:%S").time()
    start_time = datetime.strptime(start_time_str, "%H:%M:%S").time()
    end_time = datetime.strptime(end_time_str, "%H:%M:%S").time()

     # Check if check_time is in the range [start_time, end_time]
    return start_time < check_time <= end_time

def extract_file_data() -> list:
  cipher_pattern = r"Cipher Name:\s+(?P<ciphername>[A-z]+)(?P<bitsize>\d+)\s+Implementation:\s+(?P<implementation>\w+)\s+Start Time:\s\d{4}-\d{0,2}-\d{0,2}\s(?P<starttime>\d{2}:\d{2}:\d{2})\s+End\sTime:\s\d{4}-\d{0,2}-\d{0,2}\s(?P<endtime>\d{2}:\d{2}:\d{2})"

  time_file = open("data/formatted_execution_timelog.txt", "r")
  energy_file = open("data/2new_all_data.csv", "r")

  time_data = []
  for line in time_file:
    if not line:
      continue
    matches = re.findall(cipher_pattern, line)    
    if len(matches) != 0:
      matches = matches[0]
      new_row = {"cipher": matches[0], "bitsize": matches[1], "implementation": matches[2], "starttime": matches[3], "endtime": matches[4]}
      time_data.append(new_row)

  energy_pattern = r'\d{4}-\d{2}-\d{2}\s(?P<time>\d{2}:\d{2}:\d{2}),(?P<jouls>[\d.]+)?'
  energy_data = []
  for line in energy_file:
    matches = re.findall(energy_pattern, line)
    if len(matches) != 0:
      matches = matches[0]
      new_row = {"time": matches[0], "joules": matches[1]}
      energy_data.append(new_row)

  time_file.close()
  energy_file.close()

  return time_data, energy_data

def main():
  time_data, energy_data = extract_file_data()
  # print(time_data, energy_data)
  mapped_file = open("data/3new_mapped.csv", 'a', newline='')
  # Create a CSV writer object
  csv_writer = csv.writer(mapped_file)
 
  first_round = True
  data_to_write = []
  for cipher in time_data:
    # print("cipher start time:", cipher["starttime"],"cipher end time:",cipher["endtime"])
    for row in energy_data:
      # print("\n row time:",row["time"])
      output = ''
      result = is_time_in_range(row["time"], cipher["starttime"], cipher["endtime"])
    
      if not result and not first_round:
        continue
    
      if result:
        output = [row["time"],row["joules"],cipher["cipher"],cipher["bitsize"],cipher["implementation"]]
      
      else:
        output = [row["time"],row["joules"],'','' ,'']
  
      if len(output) > 0:
        data_to_write.append(output)
    first_round = False  

  # Sort the data based on the values in the first column
  sorted_data = sorted(data_to_write, key=lambda x: x[0])
  # for row in sorted_data:
    # print(row,"\n")
  csv_writer.writerows(sorted_data)  
  print("Done!")
  mapped_file.close()

main()