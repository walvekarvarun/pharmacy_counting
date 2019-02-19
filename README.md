The Entire Source code is written in Python.
The Source Code is titled pharmacy_counting.py and is located in the src folder.

# Comments about the Code:

There are 2 functions used-
1. process_data : to read file, calculate and write output.
2. main : to parse the arguments passed in the script.

## DataStructure and Methodology
The input file is read line by line and the following contents are stored in a nested dictionary.
The nested dictonary follows the format {Key : Value}, where Key is Drug name and Value is a Dictionary {key : value},where key is the patient name and value is the drug amount. 
If Patientname is repeated then only the drugamount is updated by adding it to the existing drug amount.

## Key assumptions made here are:
1. The Drugamount should be a number(either integer or float). If a String is encountered then that record is skipped.
2. All 5 values, seperated by commas must be present for each record.  (id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost) 
If there are less than 5 values, then that record is skipped and not read: 
Eg of a record that will be read  : 123,smith,john,prazolam,1000 \n
Eg of a record that will be read  : 123,,john,prazolam,1000 \n
Eg of a record that will NOT be read : 123,john,prazolam,1000 \n

Upon creating the nested dictionary, the total number of patients for that drug and the total amount spent on that drug are calculated and stored in another dictionary - output-dictionary.

Each key value combination of this output-dictionary is sorted by totaldrugcost in decending order, and if a tie, then by the drugname in ascending order and written to an outputfile.

The main function consists of an argumentparser which reads the inputfile passed as an argument in commandline and produces and output file in the outputfile argument specified.

# Repositary Structure

The submission follows the below repositary structure:
1. README.md - Consisting of the methodology followed.
2. input - consisting the input file(itcont.txt) having ~24 million records.
3. output - consisting of the output file(top_cost_drug.txt) for the above input file.
4. src - consists of the sourcecode
5. run.sh - shell script to run the above sourcecode and read the inputargument and outputargument
6. insight_testsuite - consists of the following items:
a. tests folder : including the original test provided, there are 5 other tests which have been run and executed successfully. the foldername specifies the test conducted.
b. run-tests.sh : shell script to run the tests.
c. results.txt : output of the tests which have been run
d. temp : temporary folder created while running the tests

