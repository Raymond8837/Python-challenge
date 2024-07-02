import os
import csv
from pathlib import Path

# set path
csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_votes = {}

#  read CSV file
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    header = next(csvreader)
    
    for row in csvreader:
        # total vote
        total_votes += 1
        
        # number of votes for candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# calculate the % and find out the winner
winner = ""
winner_votes = 0

results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# print outcome
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# export to folder "Analysis"
output_path = Path("Analysis", "election_results.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for result in results:
        txtfile.write(result + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
