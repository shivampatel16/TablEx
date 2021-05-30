import xml.etree.ElementTree as ET
import re
import string
import glob
import os
import subprocess

# Splitting 'myEdited XMLs' into train and test
# After executing this, rename 'myEdited XMLs' to 'myEdited XMLs 1'

os.chdir("/home/shivam/Desktop/myEdited XMLs/")
subprocess.call(['mkdir', '/home/shivam/Desktop/myEdited XMLs 2/'])
directory = "/home/shivam/Desktop/myEdited XMLs/"
file_name = glob.glob(directory+'*.xml')

# 'myEdited XMLs 1' -> Contains train data
# 'myEdited XMLs 2' -> Contains test data

run_count = 1
papers_added_to_myGenerated_text_file = 0

# Creating 'myGenerated Text.txt'
for fname in file_name:
    print("Run Count =  ", run_count)
    run_count = run_count + 1
    print(fname)
    
    if run_count <= 4568:
        source_folder = fname
        destination_folder = "/home/shivam/Desktop/myEdited XMLs 2/"
        subprocess.call(['mv', source_folder, destination_folder])
    else:
        break    