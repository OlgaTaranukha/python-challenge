# Homework Python PyBank
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
            datafile = open(output_file, "w", newline="\n")

            # Write in the rows of results
            datafile.writelines("%s\n" % l for l in list)
    
        except:
            print("Something went wrong when writing to the resulting file")
        finally:
            datafile.close()

# Lists to store data
date = []
profit_losses = []
average_changes = []

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, newline='') as csv_budget:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csv_budget, delimiter=',')  
    
    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Add date
        date.append(row[0])
    
        # Add profit_losses
        profit_losses.append(int(row[1]))
               
    # Add average changes
    for n in range(1,len(profit_losses)):  
        average_changes.append(profit_losses[n]-profit_losses[n-1])

    # The total number of months included in the dataset  
    total_num_months = len(date)

    # The net total amount of "Profit/Losses" over the entire period
    total_amount = sum(profit_losses)

    # The average of the changes in "Profit/Losses" over the entire period
    average_change = round(sum(average_changes)/len(average_changes),2)
    
    # The greatest increase in profits (date and amount) over the entire period
    max_profit = max(average_changes)
    
    # The greatest decrease in losses (date and amount) over the entire period
    max_loss = min(average_changes)

    # create list of results
    result_list = []
    
    result_list.append("Financial Analysis".center(30," "))
    result_list.append("".ljust(30,"-")) 
    result_list.append("Total Months: %d" %(total_num_months))
    result_list.append("Total : $%d" %(total_amount))
    result_list.append("Average  Change: $%.2f" %(average_change))
    result_list.append("Greatest Increase in Profits: %s ($%d)" %(date[average_changes.index(max_profit)+1],max_profit))
    result_list.append("Greatest Decrease in Profits: %s ($%d)" %(date[average_changes.index(max_loss)+1],max_loss))    
    
    # print results on Terminal
    result_output(result_list,"")

    # write results in the file
    result_output(result_list,"budget_final.txt")