
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
    count_a = candidate.count('Charles Casper Stockham')
    count_b = candidate.count('Diana DeGette')
    count_c = candidate.count('Raymon Anthony Doane')

    # Comvert the amount of votes to a percentage with three deceimal places
    # To determine the winner of the election
    ccs_perc = format((count_a / total_votes) * 100, '.3f')
    dd_perc = format((count_b / total_votes) * 100, '.3f')
    rad_perc = format((count_c / total_votes) * 100, '.3f')

# the output path to write the analysis text file in the Analysis folder
output_path = os.path.join('Analysis', 'analysis.txt')

# open the textfile in write mode
with open(output_path, 'w', encoding='utf-8') as textfile:
    # active the text writer
    txtwriter = csv.writer(textfile)
    
    #  Write the output that I wish to see on the text file
    txtwriter.writerow("Election Results")
    txtwriter.writerow("---------------------")
    txtwriter.writerow(f"Total Votes: {total_votes}")
    txtwriter.writerow("---------------------")
    txtwriter.writerow(f"Charles Casper Stockham: {ccs_perc}% ({count_a})")
    txtwriter.writerow(f"Diana DeGette: {dd_perc}% ({count_b})")
    txtwriter.writerow(f"Raymon Anthony Doane: {rad_perc}% ({count_c})")
    txtwriter.writerow("---------------------")
    txtwriter.writerow("Winner: Diana DeGette")
