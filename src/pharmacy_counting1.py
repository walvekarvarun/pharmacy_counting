#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:02:25 2019

@author: varunwalvekar
"""

from collections import defaultdict
from argparse import ArgumentParser

#Function to read input file, calculateresult and write result in outputfile
def process_data(inputfile,outputfile):
    # creating data_dict : key(drugname) and value(list of all membernames and drugamount)
    data_dict = defaultdict(list)
    with open(inputfile,'r') as input:
        for line in input:
            line = line.strip()
            line_data = line.split(',')
            try:
                #memberid = int(line_data[0].strip('\"'))
                memberlname = str(line_data[1])
                memberfname = str(line_data[2])
                membername = (memberfname + ' ' + memberlname)
                drugname = str(line_data[3].strip('\"'))
                drugamount = float(line_data[4])
            # Ignore rows which do not have a number as drugamount
            except ValueError:
                continue
            #Ignore rows which do not have all 5 values(missing values too should be comma seperated)
            except IndexError:
                continue
            details = (membername,drugamount)
            data_dict[drugname].append(details)
    
    # creating a new default dictionary to store result
    drugcost_dict = defaultdict(list)
    # loop to calculate total drug cost and number of prescribers
    for key,values in data_dict.items():
        drugcost = 0
        for idx in range(0,len(values)):
            drugcost = drugcost + int(values[idx][1])
            drugcost_dict[key] = [drugcost,len(values)] 
    
    # sorting and writing result to output file having drugname,num_prescriber,total_cost  
    with open(outputfile, 'w') as output:
        output.write("%s,%s,%s\n"%('drug_name','num_prescriber','total_cost'))
        for idx in sorted(drugcost_dict, key=drugcost_dict.get, reverse=True):
            output.write("%s,%s,%s\n"%(idx,drugcost_dict[idx][1],drugcost_dict[idx][0]))

#  main function to parse           
def main():
    parser = ArgumentParser(description='Parse input output')
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()
    process_data(args.input,args.output)
    

if __name__ == "__main__":
	main()




	
	
	
	
