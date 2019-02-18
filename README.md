The Entire Source code is written in Python.
The Source Code is titled pharmacy_counting.py and is located in the src folder.

Comments about the Code:
The input file is read line by line and the following contents are stored in pythons defaultdictionary.
1. Drug Name is stored as key
2. A combination of firstname + lastname , drugamount is stored as value.

Since default dictionary is used for each key(drugname) all the combinations of firstname+lastname,drugamount are stored as values pointing to the key.

Key assumptions made here are:
1. The Drugamount should be a number(either integer or float). If a String is encountered then that record is skipped.
2. All 5 values, seperated by commas must be present for each record.  (id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost) 
If there less than 5 values, then that record is skipped and not read: 
Eg of a record that will be read  : 123,smith,john,prazolam,1000
Eg of a record that will be read  : 123,,john,prazolam,1000
Eg of a record that will NOT be read : 123,john,prazolam,1000

Upon storing the key values, the total number of prescribers and the total drug cost are then calculated and stored in a new defaultdictionary

Each key value combination of this defaultdictionary is sorted by totaldrugcost in decending order, and if a tie, then by the drugname in ascending order and written to an outputfile.

The main function consists of an argumentparser which reads the inputfile passed as an argument in commandline and produces and output file in the outputfile argument specified.

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


