# Homework Python PyPoll 
import os 
import csv

# define function to output the result 
def result_output(list,file_name):
    if len(file_name) == 0:
        # print on Terminal
        print(*list, sep = "\n", end = " ")
    else:
        # write in the txt-file
        
        # Set variable for output file
        output_file = os.path.join(file_name)
        
        try:
            #  Open the output file
            datafile = open(output_file, "wt+", newline="\n")
            

            # Write in the rows of results
            datafile.writelines("%s\n" % l for l in list)
    
        except:
            print("Something went wrong when writing to the resulting file")
        finally:
            datafile.close()

# Lists to store data from csv-file
voters = []
#counties_csv = []
candidates_csv = []

# Lists to store resulting data 
candidate_names = []
candidate_votes = []
candidate_percentages = []

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, newline='') as csv_election:    
    
    # Detect CSV header line
    has_header = csv.Sniffer().has_header(csv_election.read(1024))
    csv_election.seek(0)

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csv_election, delimiter=',') 
    if has_header:
        # Read the header row first 
        csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Add voters ID
        voters.append(int(row[0]))
    
        # Add counties
        #counties_csv.append(row[1])
        
        # Add candidates
        candidates_csv.append(row[2])
               
    # the total number of votes cast
    total_num_votes = len(voters)

    # list of candidates who received votes
    candidate_names = list(set(candidates_csv))

    # calculate number of votes and percentage for each candidate
    for c in candidate_names:
        # the total number of votes the each candidate won
        n = candidates_csv.count(c)
        candidate_votes.append(n)
        
        # the percentage of votes the each candidate won
        p = round(n * 100 / total_num_votes, 3)
        candidate_percentages.append(p)
    
    # create total list of the candidates
    candidates = list(zip(candidate_names, candidate_votes, candidate_percentages))
    
    # sort candidates in the descending order according to the popular vote
    candidates.sort(key=lambda candidate: candidate[1], reverse = True)  
    
    # the winner of the election based on popular vote
    winner = candidates[0][0]  
    
    # create list of results
    result_list = []
    
    result_list.append("Election Results".center(30," "))
    result_list.append("".ljust(30,"-")) 
    result_list.append("Total Votes: %d" %(total_num_votes))
    result_list.append("".ljust(30,"-")) 

    for x in candidates:
        result_list.append("%s: %.3f%% (%d)" %(x[0], x[2], x[1]))    
    
    result_list.append("".ljust(30,"-")) 
    result_list.append("Winner: %s".ljust(30," ") %(winner))
    result_list.append("".ljust(30,"-")) 
    
    # print results on Terminal
    result_output(result_list,"")

    # write results in the file
    result_output(result_list,"election_final.txt")