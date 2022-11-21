
# Import Dependencies os and csv
import os
import csv

# File to the path to get the election data from the resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# open the csv file in read mode
with open(csvpath, 'r', encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

      # What are the headers of the csv file
    csv_header = next(csvreader)
    print(f"This is the header: {csv_header}")

    # create a candidate list
    candidate_list = [
    "Charles Casper Stockham",
    "Diana DeGette",
    "Raymon Anthony Doane"]
   
     # creating empty lists to store the ballot id and candidate name
    ballot = []
    candidate = []

    # Add the ballot id's through into the ballot list
    # Add the candidate names to the candidate list
    for row in csvreader:
        ballot.append(row[0])
        candidate.append(row[2])
    
    # Find the total amount of votes in the file    
    total_votes = (len(ballot))
    
    # Count how many votes each candidate got
    count_a = candidate.count(candidate_list[0])
    count_b = candidate.count(candidate_list[1])
    count_c = candidate.count(candidate_list[2])

    # Comvert the amount of votes to a percentage with three deceimal places
    # To determine the winner of the election
    ccs_perc = format((count_a / total_votes) * 100, '.3f')
    dd_perc = format((count_b / total_votes) * 100, '.3f')
    rad_perc = format((count_c / total_votes) * 100, '.3f')

# the output path to write the analysis text file in the Analysis folder
output_path = os.path.join('Analysis', 'analysis.txt')

# open the textfile in write mode
with open(output_path, 'w') as textfile:
    # active the text writer
    
    #  Write the output that I wish to see on the text file
    textfile.write(f"Election Results\n")
    textfile.write(f"---------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"---------------------\n")
    textfile.write(f"{candidate_list[0]}: {ccs_perc}% ({count_a})\n")
    textfile.write(f"{candidate_list[1]}: {dd_perc}% ({count_b})\n")
    textfile.write(f"{candidate_list[2]}: {rad_perc}% ({count_c})\n")
    textfile.write(f"---------------------\n")
    textfile.write(f"Winner: {candidate_list[1]}\n")
