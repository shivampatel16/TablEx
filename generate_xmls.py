import glob
import subprocess
import os

os.chdir("/home/shivam/Desktop/myGenerated PDFs/")
directory = "/home/shivam/Desktop/myGenerated PDFs/"
file_name = glob.glob(directory+'*.pdf')
subprocess.call(['mkdir', '/home/shivam/Desktop/myCompleted PDFs/'])
subprocess.call(['mkdir', '/home/shivam/Desktop/myGenerated XMLs/'])

run_count = 1

# Creating XML file for each generated PDF
for fname in file_name:
    print("Run Count =  ", run_count)
    run_count = run_count + 1
    print(fname)
    fn = fname.split('/')
    
    _pdf = fn[-1]
    print(_pdf)
    fn = fn[-1][:-4]
    print(fn)
    
    subprocess.call("./pdftoxml.linux64.exe.1.2_7 -noImage -noImageInline " + _pdf + " "+fn+".xml", shell=True)
    source_folder = directory + fn + ".xml"
    destination_folder = "/home/shivam/Desktop/myGenerated XMLs/"
    subprocess.call(['mv', source_folder, destination_folder])
    
    source_folder = directory + fn + ".pdf"
    destination_folder = "/home/shivam/Desktop/myCompleted PDFs/"
    subprocess.call(['mv', source_folder, destination_folder])