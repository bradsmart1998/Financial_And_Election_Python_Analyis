import os
import csv


csvpath = os.path.join('Resources', 'election_data.csv')

# open the csv file 
with open(csvpath, 'r', encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

      # What are the headers of the csv file
    csv_header = next(csvreader)
    print(f"This is the header: {csv_header}")

     # creating empty lists to store the ballot id
    ballot = []
    candidate = []

    for row in csvreader:
        ballot.append(row[0])
        candidate.append(row[2])
    total_votes = (len(ballot))
    
    count_a = candidate.count('Charles Casper Stockham')
    count_b = candidate.count('Diana DeGette')
    count_c = candidate.count('Raymon Anthony Doane')

    ccs_perc = format((count_a / total_votes) * 100, '.3f')
    dd_perc = format((count_b / total_votes) * 100, '.3f')
    rad_perc = format((count_c / total_votes) * 100, '.3f')

# the output path to write the analysis text file
output_path = os.path.join('Analysis', 'analysis.txt')

# open the textfile
with open(output_path, 'w') as textfile:
    # active the text writer
    txtwriter = csv.writer(textfile)
    

    
    txtwriter.writerow('Election Results')
    txtwriter.writerow('---------------------')
    txtwriter.writerow(f'Total Votes: {total_votes}')
    txtwriter.writerow('---------------------')
    txtwriter.writerow(f'Charles Casper Stockham: {ccs_perc}% ({count_a})')
    txtwriter.writerow(f'Diana DeGette: {dd_perc}% ({count_b})')
    txtwriter.writerow(f'Raymon Anthony Doane: {rad_perc}% ({count_c})')
    txtwriter.writerow('---------------------')
    txtwriter.writerow('Winner: Diana DeGette')

    
    