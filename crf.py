import subprocess
from itertools import combinations
import random
import os

os.chdir("/home/shivam/Desktop/IITGN_Final/")

template_features_list = ['U00:%x[0,0]',
                          'U01:%x[-1,0]/%x[0,0]',
                          'U02:%x[-1,0]/%x[0,0]/%x[1,0]',
                          'U03:%x[-2,2]',
                          'U04:%x[-1,2]',
                          'U05:%x[0,2]',
                          'U06:%x[1,2]',
                          'U07:%x[2,2]',
                          'U08:%x[-1,2]/%x[0,2]/%x[1,2]',
                          'U09:%x[-2,2]/%x[-1,2]/%x[0,2]/%x[1,2]/%x[2,2]',
                          'U10:%x[-1,5]',
                          'U11:%x[0,5]',
                          'U12:%x[1,5]',
                          'U13:%x[-1,6]',
                          'U14:%x[0,6]',
                          'U15:%x[1,6]',
                          'U16:%x[-1,7]',
                          'U17:%x[0,7]',
                          'U18:%x[1,7]',
                          'U19:%x[-1,10]',
                          'U20:%x[0,10]',
                          'U21:%x[1,10]',
                          'U22:%x[-1,11]',
                          'U23:%x[0,11]',
                          'U24:%x[1,11]',
                          'U25:%x[-1,12]',
                          'U26:%x[0,12]',
                          'U27:%x[1,12]',
                          'U28:%x[-1,13]',
                          'U29:%x[0,13]',
                          'U30:%x[1,13]']

# Running over various combinations of features in the tamplate_feature_list 
for j in range(1,len(template_features_list) + 1):
    acc_list = []
    feature_list = []

    template_features_comb = combinations(template_features_list, j)
    a = list(template_features_comb)
    random.shuffle(a)
    random_comb = a[:100]

    for i in list(random_comb):
        file1 = open("/home/shivam/Desktop/IITGN_Final/template","w")
        for feature in i:
            file1.write(feature + "\n")
        print("\n")
        file1.close()
        
        subprocess.call(["crf_learn", "template", "bbb.data", "model"])
        subprocess.call("crf_test -m model train_edited.data > output.data", shell=True)    
        result = subprocess.check_output(["python", "accuracy.py", "output.data"])
        modified_result = result[:-2]
        acc_list.append(float(modified_result))
        feature_list.append(i)

    print(acc_list)
    print("\n\n")
    print(feature_list)
    print("\n\n")
    print("Max Accuracy: ", max(acc_list))
    max_acc_index = acc_list.index(max(acc_list))
    print(feature_list[max_acc_index])