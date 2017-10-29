import csv

file_to_load = "election_data_2.csv"
file_to_output = "election_data_2.txt"

Candidates=[]

with open(file_to_load, newline="") as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")

    next(csv_reader, None)

    for row in csv_reader:
        Candidates.append(row[2]) 


total_votes=len(Candidates)
cand_list=set(Candidates)
cand_list=[i for i in cand_list]
vote_counts=[Candidates.count(i) for i in cand_list]
vote_percent= [((Candidates.count(i)/total_votes)*100) for i in cand_list]
vote_percent= [round(i,3) for i in vote_percent]

max_vote=max(vote_counts)


mx,idx = max( (vote_counts[i],i) for i in range(len(vote_counts)) )

wins=cand_list[idx]
        
    
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes) )
print('-------------------------')

cand_num=0
for i in cand_list:
    print(i + ': ' + str(vote_percent[cand_num])+'% '+ '(' + str(vote_counts[cand_num]) + ')' )
    cand_num+=1

print('-------------------------')

print('Winner: ' + str(wins)) 

print('-------------------------')

text_file = open("Output.txt", "w")
text_file.write('Election Results'+'\n')
text_file.write('-------------------------'+'\n')
text_file.write('Total Votes: ' + str(total_votes)+'\n')
text_file.write('-------------------------'+'\n')
cand_num=0
for i in cand_list:
    text_file.write(i + ': ' + str(vote_percent[cand_num])+'% '+ '(' + str(vote_counts[cand_num]) + ')'+'\n')
    cand_num+=1
text_file.write('-------------------------'+'\n')
text_file.write('Winner: ' + str(wins)+'\n') 
text_file.close()