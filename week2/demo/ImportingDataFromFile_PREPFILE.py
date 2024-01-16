#Week 2 Day 1: Importing Data from a File

#YOU MUST IMPORT THE CSV LIBRARY IN ORDER FOR FILES TO BE ACCESSED

#CSV: Comma Separated Values
#RECORDS: rows of the file, different types of data all belonging together
#FIELDS: columns of the file, sets of data (all data in a column is the same "type" ie names, ages, salaries, email addresses, etc)

#BASE PROGRAM CODE-------------------------------------------------------------------

#STEP 1: import csv library so we can read the file
import csv 

#you should ALWAYS have a total records var for your first few attempts at file reading
total_records = 0

#holds all salaries in file for total print at end
total_salaries = 0

#prnt header -- at the end, once everything else is running accurately
print(f"{'NAME':10} \t{'AGE':3} \t${'SALARY':10}")
print("-----------------------------------------------------")


#STEP 2: CONNNECT TO THE FILE LOCATION
#right-click the text/csv file in folder view --> "Properties" to find the file location
#these file locations are cAsE sEnSiTiVe & space/special character sensitive so DOUBLE CHECK THEM!
#flip all '\' to '/'
with open("week2/demo/example.csv") as csvfile:
    #notice ':' everything must be INDENTED now (until we're ready to "close" the file)

    #STEP 3: ALLOW THE FILE TO BE READ BY OUR PROGRAM
    file = csv.reader(csvfile)
    
    #now the file we have connected is known in the program as 'file'
    #file has several records, each record has several fields

    #below is a FOR loop
    #for loops are loops -- continually repeated sequence of code
    #they continue NOT based on a CONDITION but on a RANGE
    #range: '0 - 10', 'a - f'
    
    #STEP 4: ACTUALLY READ/PROCESS THE FILE DATA, ONE RECORD AT A TIME
    for rec in file:
        
        #print(rec)
        #print entire record of file, we are seeing this as a list
                    #lists can hold multiple points of data at once
                    #in order to specify a data point over another, we need to know its POSITION IN THE LIST
                    
        #print all the data for each record as VALUES no LIST PIECES
        print(f"{rec[0]} \t{rec[1]} \t${rec[2]}")
        
        #print only the names in the file -- specify position of data in list
        #print(f"{rec[0]}"")
        
        #add feild width to ensure colu
        
        #print only the names 
        
        #update record count
        total_records += 1 #total_records = total_records + 1 
        
        #update the total salary
        total_salaries += float(rec[2])
        
print(f"\nTOTAL RECORDS: {total_records} | TOTAL SALARIES: $ {total_salaries:.2f}")

        #notice the ':' everything in the for loop must be INDENTED
        #RANGE: for each record in the file, do the following
        #rec is a variable that is initialized the the for loop range
        #           on line 35

        #SHORTHAND VERSION of: total_records = total_records + 1

                    #print entire record of file. we are seeing this as a LIST
                    #lists can hold multiple points of data at once
                    #in order to specify a data point over another, we need to know its POSITION IN THE LIST

        #print only the names in the file -- specify position of data in lit
            

            

        #add all salaries to total_salary -- REMEMBER: all data entering a Python program is treated as a STRING unless cast otherwise
        


        
        
        #add field width to ensure columns stay aligned

 

#print final values: total records processed and total salary of all employees in file