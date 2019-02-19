#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 05:52:09 2019

@author: varunwalvekar
"""

from argparse import ArgumentParser
from collections import defaultdict

# function to read input file, calculateresult and write result in outputfile
def process_data(input_file, output_file):
    multiple_drug_nested_dict = {} # nesteddictionary - key(drugname) value(dictionary of patients and drugamount)
    with open(input_file,'r') as inpt:
        for line in inpt:
            line = line.strip() 
            line_data = line.split(',')
            try:
                patient_id = line_data[0]
                patient_ln = str(line_data[1])
                patient_fn = str(line_data[2])
                patientname = (patient_ln + patient_fn)
                drug_name =  str(line_data[3].strip('\"'))
                drug_expense =  float(line_data[4])
            # Ignore rows which do not have a number as drugamount
            except ValueError: 
                continue
            #Ignore rows which do not have all 5 values(missing values too should be comma seperated)
            except IndexError:
                continue
            # check for conditions and add key,value to the multiple_nested_dictionary
            if drug_name in multiple_drug_nested_dict:
                single_drug_dict = multiple_drug_nested_dict[drug_name]	
				# Check to see unique patient names, and, total drug cost
                if patientname in single_drug_dict:
                    existing_expense = single_drug_dict[patientname]
                    single_drug_dict[patientname] = existing_expense + drug_expense
                else:
                    single_drug_dict[patientname] = drug_expense
            else:
                single_drug_dict = {}
                single_drug_dict[patientname] = drug_expense
                multiple_drug_nested_dict[drug_name] = single_drug_dict
                
    #create a defaultdictionary to store the output
    output_dict = defaultdict(list)	
    with open(output_file, 'w') as output:
        #write the header
        output.write("%s,%s,%s\n"%('drug_name','num_prescriber','total_cost'))
    # Calculate the total unique patients and sum of drug cost
        for drug in multiple_drug_nested_dict:
            drug_cost = 0
            unique_patients = 0
            single_drug_dict = multiple_drug_nested_dict[drug]
            for patient_id in single_drug_dict:
                unique_patients += 1
                drug_cost += int(single_drug_dict[patient_id])
            output_dict[drug] = [drug_cost,unique_patients]
        for idx in sorted(output_dict, key=output_dict.get, reverse=True):
            output.write("%s,%s,%s\n"%(idx,output_dict[idx][1],output_dict[idx][0]))


#  main function to parse  
def main():
    parser = ArgumentParser(description='Parse input output')
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    process_data(args.input,args.output)
        
        
if __name__ == "__main__":
	main()