import re
import sys

# Check if the input file is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python parse_branching_output.py <input_file>")
    sys.exit(1)

# Get the input file from the command-line argument
input_file = sys.argv[1]

# Initialize lists to store extracted values
time_taken_list = []
branches_list = []
branch_accuracy_list = []
branch_miss_list = []
total_ins_list = []

# Define regular expressions to match the required lines
time_taken_pattern = re.compile(r'Time taken \(Branching\): (\d+) usec')
branches_pattern = re.compile(r'Branches = ([\d,]+)')
branch_accuracy_pattern = re.compile(r'branch accuracy:(\d+\.\d+)')
branch_miss_pattern = re.compile(r'Cond br mspredictd = (\d+)')
total_ins_pattern = re.compile(r'Instr completed = (\d+)')

# Read the input file
with open(input_file, 'r') as file:
    for line in file:
        # Extract time taken
        time_taken_match = time_taken_pattern.search(line)
        if time_taken_match:
            time_taken_list.append(time_taken_match.group(1))

        # Extract branches
        branches_match = branches_pattern.search(line)
        if branches_match:
            branches_list.append(branches_match.group(1))

        # Extract branch accuracy
        branch_accuracy_match = branch_accuracy_pattern.search(line)
        if branch_accuracy_match:
            branch_accuracy_list.append(branch_accuracy_match.group(1))

        # Extract branch misses
        branch_miss_match = branch_miss_pattern.search(line)
        if branch_miss_match:
            branch_miss_list.append(branch_miss_match.group(1))

        total_ins_match = total_ins_pattern.search(line)
        if total_ins_match:
            total_ins_list.append(total_ins_match.group(1))

# Print the columns of each statistic
print("Time Taken (usec):")
for time_taken in time_taken_list:
    print(time_taken)

print("\nBranches:")
for branches in branches_list:
    print(branches)

print("\nBranch Accuracy:")
for branch_accuracy in branch_accuracy_list:
    print(branch_accuracy)

print("\nBranch Miss:")
for branch_miss in branch_miss_list:
    print(branch_miss)

print("\nTotal Instructions:")
for total_ins in total_ins_list:
    print(total_ins)

import csv
data = zip(time_taken_list,branches_list,branch_miss_list,branch_accuracy_list)

csv_file =input_file.split("/")[-1].split(".")[0] + ".csv"

print("\n\nSaving to "+input_file.split("/")[-1].split(".")[0]+".csv")

with open(csv_file, "w") as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
