import xml.etree.ElementTree as ET
import re
import string
import glob
import os
import subprocess

os.chdir("/home/shivam/Desktop/myEdited XMLs 1/")
directory = "/home/shivam/Desktop/myEdited XMLs 1/"
file_name = glob.glob(directory+'*.xml')
run_count = 1
papers_added_to_myGenerated_text_file = 0

for fname in file_name:
    print("Run Count =  ", run_count)
    run_count = run_count + 1       
    print(fname)
    fn = fname.split('/')
    _xml = fn[-1]
    print(_xml)
    
    tree = ET.parse(_xml)
    root = tree.getroot()
    
    # Selected XML attributes for extracting tabular text
    attributes_allowed = ['angle', 'base', 'bold', 'font-color', 'font-size', 'height',
                          'id', 'italic', 'rotation', 'sid', 'width', 'x', 'y']

    a = []   # a = token_sequence_from_pdf2xml = pdf2xml_tool(input_pdf) -> List of tokens with their properties
    at = {}  # tokens in 'a'
    
    columns_in_template_file_check = 0
    count = 0

    for page in root:
        for text in page:
            for token in text:
                if token.tag == 'TOKEN':
                    count = count + 1
                    at = {}
                    for i in sorted (token.attrib):
                        if i in attributes_allowed:
                            at.update( {i : token.attrib[i]} )
                        if i == 'tag_type':
                            tag_type_store = token.attrib[i]
                        if i == 'table_number':
                            table_number_store = token.attrib[i]
                                                        
                    at.update( {'table_number' : table_number_store} )
                    at.update( {'tag_type' : tag_type_store} )
                    
                    if len(at) != 15:
                        columns_in_template_file_check = 1
                        
                    if token.text:
                        token.text = token.text.strip()
                        token_text = token.text.replace(" ", "")
                        a.append({token_text : at})  
                    else:
                        a.append({token.text : at})
                       
    if columns_in_template_file_check == 0:
        papers_added_to_myGenerated_text_file = papers_added_to_myGenerated_text_file + 1
        print("papers_added_to_myGenerated_text_file = ", papers_added_to_myGenerated_text_file)
        
        with open("/home/shivam/Desktop/myEdited XMLs 1/train.data", "a") as myfile:
            for i in a:
                for key, value in i.items():
                    to_add = str(key) + " "
                    myfile.write(to_add.rstrip("\n"))
                    for key2, value2 in value.items():
                        to_add = str(value2) + " "
                        myfile.write(to_add.rstrip("\n"))
                myfile.write("\n")
    subprocess.call(['rm','-r', fname])
	
os.chdir("/home/shivam/Desktop/myEdited XMLs 1/")

with open("train.data", "r", encoding = "utf8") as f:
    with open("train_edited.data", "w", encoding = "utf8") as f1:
        for line in f:
            if len(line.split()) == 16:
                f1.write(line)