#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:21:05 2020

@author: zeronp
"""

import json 
import csv 
import os

file_name = 'top_500_instagram_influencers.json'      #file to read from 
csv_file_name = 'top_500_instagram_influencers.csv'   #file to be written to

dummy_file = file_name + '.bak' 
with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
    # Write given line to the dummy file
    write_obj.write('{"Influencers": [' + '\n')
    
    # Read lines from original file one by one and append them to the dummy file
    for line in read_obj:
        write_obj.write(line)
    write_obj.write("{ }]}")
# remove original file
os.remove(file_name)
# Rename dummy file as the original file
os.rename(dummy_file, file_name)
  
# Opening JSON file and loading the data 
# into the variable data 
with open(file_name) as json_file: 
    data = json.load(json_file) 
  
dj_data = data['Influencers'] 

# now we will open a file for writing 
data_file = open(csv_file_name, 'w') 

# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 

headers = ['rank','grade','name','psots/media','followers','following']
csv_writer.writerow(headers) 
for r in dj_data: 
    # Writing data of CSV file 
    csv_writer.writerow(r.values()) 
  
data_file.close() 