# Homework Python PayBank
import os
import csv

# define function to output the result 
def result_output(list,file_name):
    if len(file_name) == 0:
        # print on Terminal
        for s in list:
            print(s)
    else:
        # write in the txt-file
        
        # Set variable for output file
        output_file = os.path.join(file_name)
        
        try:
            #  Open the output file
            datafile = open(output_file, "w+")

            # Write in the rows of results
            # datafile.writelines(list)
            for s in result_list:
                datafile.write(s)
                datafile.write("\n")
    
        except:
            print("Something went wrong when writing to the resulting file")
        finally:
            datafile.close()

# Lists to store data
date = []
profit_losses = []

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

    # The total number of months included in the dataset  
    total_num_months = len(date)

    # The net total amount of "Profit/Losses" over the entire period
    total_amount = sum(profit_losses)

    # The average of the changes in "Profit/Losses" over the entire period
    average_change = round(total_amount/total_num_months,2)
    
    # The greatest increase in profits (date and amount) over the entire period
    max_profit = max(profit_losses)
    
    # The greatest decrease in losses (date and amount) over the entire period
    max_loss = min(profit_losses)

    # create list of results
    result_list = []
    
    result_list.append("Financial Analysis".center(30," "))
    result_list.append("".center(30,"-")) 
    result_list.append("Total Months: %d" %(total_num_months))
    result_list.append("Total : $%d" %(total_amount))
    result_list.append("Average  Change: $%d" %(average_change))
    result_list.append("Greatest Increase in Profits: %s ($%d)" %(date[profit_losses.index(max_profit)],max_profit))
    result_list.append("Greatest Decrease in Profits: %s ($%d)" %(date[profit_losses.index(max_loss)],max_loss))    
    
# print results on Terminal
result_output(result_list,"")

# write results in the file
result_output(result_list,"budget_final.txt")