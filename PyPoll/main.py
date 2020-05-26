# Import Data from CSV file
import os
import csv

# Path of data from CSV file
csvpath = os.path.join('Resources', 'election_data.csv')


# Total Vote Counter
total_votes = 0

# All candidates, candidate votes, winning candidate and win count
all_candidates = []
candidate_votes = {}
candidate_winner = ""
win_count = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath, 'r') as election_data:
    csvreader = csv.DictReader(election_data)

    # For each row
    for row in csvreader:

        # total vote count
        total_votes += 1

        # Candidate name from each row
        candidate_name = row["Candidate"]

        if candidate_name not in all_candidates:

            all_candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the results in the terminal and output the data to text file
output_file = "analysis/election_analysis.txt"
with open(output_file, "w") as text:

    # Print the final vote count
    print(f'Election Results'+'\n')
    print(f'----------------------'+'\n')
    print(f"Total Votes: {total_votes}\n")    
    print(f'----------------------'+'\n')    
    

    # Save the final vote count to the text file
    text.write(f'Election Results'+'\n')
    text.write(f'----------------------'+'\n')
    text.write(f"Total Votes: {total_votes}\n")    
    text.write(f'----------------------'+'\n')

    # Looping through the counts
    for candidate in candidate_votes:

        # Vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > win_count):
            win_count = votes
            candidate_winner = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save to text file
        text.write(voter_output)

    # Print Winner
    winner_output = (
        f"-------------------------\n"
        f"Winner: {candidate_winner}\n"
        f"-------------------------\n")
    print(winner_output)

    # Winning candidate's name to the text file
    text.write(winner_output)
