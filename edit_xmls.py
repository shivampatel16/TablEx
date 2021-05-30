import xml.etree.ElementTree as ET
import re
import string
import glob
import os
import subprocess

os.chdir("/home/shivam/Desktop/myGenerated XMLs/")
subprocess.call(['mkdir', '/home/shivam/Desktop/myEdited XMLs/'])
directory = "/home/shivam/Desktop/myGenerated XMLs/"
file_name = glob.glob(directory+'*.xml')

run_count = 1

# Editing generated XML files
for fname in file_name:
    print("Run Count =  ", run_count)
    run_count = run_count + 1        
    print(fname)
    fn = fname.split('/')
    _xml = fn[-1]
    print(_xml)
    
    tree = ET.parse(_xml)
    root = tree.getroot()

    this_is_start_of_table_once = 0    
    this_is_end_of_table_once = 0
    
    for page in root:
        for text in page:
            k = 0
            while k < len(text):
                if text[k].tag == 'TOKEN':   
                    # The following 4 'if' conditions are for removing consecutive #THIS#IS#START#OF#TABLE#'s or
                    # consecutive #THIS#IS#END#OF#TABLE#'s (consecutive as in each table has 2 or more such 
                    # tokens of similar type added together due to errors)
                    
                    if this_is_start_of_table_once == 1 and text[k].text == "#THIS#IS#START#OF#TABLE#":
                        text.remove(text[k])
                        continue
                    if this_is_end_of_table_once == 1 and text[k].text == "#THIS#IS#END#OF#TABLE#":
                        text.remove(text[k])
                        continue
                    if text[k].text == "#THIS#IS#START#OF#TABLE#":
                        this_is_end_of_table_once = 0
                        this_is_start_of_table_once = 1
                    if text[k].text == "#THIS#IS#END#OF#TABLE#":
                        this_is_start_of_table_once = 0
                        this_is_end_of_table_once = 1       
                k = k + 1
                    
    make_tag_type_T = 0
    table_number = 0
    
    # Adding attributes 'tag_type' and 'table_number' to each XML tag
    for page in root:
        for text in page:
            k = 0
            while k < len(text):
                if text[k].tag == 'TOKEN':
                                         
                    if make_tag_type_T == 0 or text[k].text == "#THIS#IS#END#OF#TABLE#":
                        text[k].set('tag_type','NT')
                        text[k].set('table_number', str(0))
                    elif make_tag_type_T == 1:
                        text[k].set('tag_type','T')
                        text[k].set('table_number', str(table_number))
                    
                    if text[k].text == "#THIS#IS#END#OF#TABLE#":
                        make_tag_type_T = 0
                    elif text[k].text == "#THIS#IS#START#OF#TABLE#":
                        make_tag_type_T = 1
                        table_number = table_number + 1                     
                k = k + 1    
    tree.write("/home/shivam/Desktop/myEdited XMLs/" + _xml)    