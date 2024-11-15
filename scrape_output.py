import re
import sys

# Check if the input file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python parse_perf_output.py <input_file>")
    sys.exit(1)

# Get the input file from the command-line argument
input_file = sys.argv[1]

# Initialize lists to store extracted values
time_elapsed_list = []
branch_misses_list = []
branch_misses_percent_list = []
branches_list = []
instructions_list = []

# Define regular expressions to match the required lines
time_elapsed_pattern = re.compile(r'(\d+\.\d+) seconds time elapsed')
branch_misses_pattern = re.compile(r'([\d,]+)\s+branch-misses\s+#\s+(\d+\.\d+)% of all branches')
branches_pattern = re.compile(r'([\d,]+)\s+branches\s+#')
instructions_pattern = re.compile(r'([\d,]+)\s+instructions\s+#')

# Read the input file
with open(input_file, 'r') as file:
    for line in file:
        # Extract seconds time elapsed
        time_elapsed_match = time_elapsed_pattern.search(line)
        if time_elapsed_match:
            time_elapsed_list.append(time_elapsed_match.group(1))

        # Extract branch misses and their percentage
        branch_misses_match = branch_misses_pattern.search(line)
        if branch_misses_match:
            branch_misses_list.append(branch_misses_match.group(1))
            branch_misses_percent_list.append(branch_misses_match.group(2))

        # Extract branches
        branches_match = branches_pattern.search(line)
        if branches_match:
            branches_list.append(branches_match.group(1))

        instructions_match = instructions_pattern.search(line)
        if instructions_match:
            instructions_list.append(instructions_match.group(1))

# Print the columns of each statistic
print("Seconds Time Elapsed:")
for time_elapsed in time_elapsed_list:
    print(time_elapsed)

print("\nBranch Misses:")
for branch_misses in branch_misses_list:
    print(branch_misses)

print("\nBranch Misses Percentage:")
for branch_misses_percent in branch_misses_percent_list:
    print(branch_misses_percent+"%")

print("\nBranches:")
for branches in branches_list:
    print(branches)

print("\nInstructions:")
for instructions in instructions_list:
    print(instructions)

import csv
data = zip(time_elapsed_list,branches_list,branch_misses_list,branch_misses_percent_list)

csv_file =input_file.split("/")[-1].split(".")[0] + ".csv"

print("\n\nSaving to "+input_file.split("/")[-1].split(".")[0]+".csv")

with open(csv_file, "w") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)