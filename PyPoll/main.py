#
# File main.py
#
# For python-challenge homework "PyPoll"
#
# Author: Phil Lowden (phil@dreamtone.com)
#
# Sample output to terminal and file
#
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

# import os and csv modules
import os
import csv

# define variables

# total number of votes cast
total_votes = 0

# list of candidates who received votes
candidates = {}

# candidate's name in dataset (column three)
name = ""

# most votes
most_votes = 0

# winner's name
winner = ""

# read input file

input_path = os.path.join('Resources','election_data.csv')

with open(input_path,newline='') as input_file:

	input_reader = csv.reader(input_file,delimiter=',')

	# skip header
	next(input_reader)

	# read each row and store columns
	for row in input_reader:
		name = row[2]

		# keep track of total votes
		total_votes += 1

		# increment this candidate's number of votes
		if name in candidates:
			candidates[name] += 1
		else:
			candidates[name] = 1


# construct output as list

output=[]
output.append("Election Results")
output.append("-------------------------")
output.append("Total Votes: " + str(total_votes))
output.append("-------------------------")

for candidate in candidates:
	if total_votes > 0:
		percent = format(candidates[candidate]/total_votes * 100, '.3f')
	output.append(candidate + ": " + str(percent) + "% (" + str(candidates[candidate]) + ")")

	if candidates[candidate] > most_votes:
		most_votes = candidates[candidate]
		winner = candidate

output.append("-------------------------")
output.append("Winner: " + winner)
output.append("-------------------------")

# print to terminal
for line in output:
	print(line)

# open file for writing
out_path  = "PyPoll.txt"

# print to file
with open(out_path, 'w') as out_file:
	for line in output:
		out_file.write("%s\n" % line)


