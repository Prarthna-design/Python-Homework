import os
import csv

#create path for the filename
output_csv = os.path.join("Resources", "election_data.csv")

print(output_csv)

# total no of votes cast 

print('----------------------')
voter_data = []
voter_list = []
count_votes = {}
#open file, read and print header

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        voter_data.append(row[0])
        candidate = row[2]
        if candidate not in voter_list:
            voter_list.append(candidate)
        if candidate not in count_votes:
            count_votes[candidate] = 1
        else: 
            count_votes[candidate] = count_votes[candidate] +1
    # print(count_votes)

TotalVotes = len(voter_list)
winner = max(TotalVotes.values())
percent = ''
for y in voter_list:
    percent += f'{y}: {TotalVotes[y]/(TotalVotes))*100}% \n'


mult = ''' print '''
putput = (f''' 
Election Restults
------------------------------
Total Votes: {TotalVotes}
--------------------------------
{candidate}: {percent}% ({TotalVotes})
--------------------------------------
Winner: {winner}
---------------------------------
''')
print(output)



