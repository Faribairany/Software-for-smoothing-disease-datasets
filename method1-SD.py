import pandas as pd
import csv
from pprint import pprint
import pdb
import numpy as np
import os
import re

with open('(meanabsoluteerror+std)(method1).csv', mode='w', newline='') as csv_file:
            fieldnames = ['Filename','Mean Error(Method1)', 'Standard Deviation(Method1)']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
path = "C:/Users/Fariba Afrin Irany/Desktop/study/methods(SD included)/method1/inputfile"
# C:\Users\Fariba Afrin Irany\Desktop\Tiwaripaper\methods(SD included)\method1\inputfile
# C:\Users\Fariba Afrin Irany\Desktop\Tiwaripaper\Methods\method1\inputfile
for filename in os.listdir(path):

 

    df1 = pd.read_csv(r"C:/Users/Fariba Afrin Irany/Desktop/study/methods(SD included)/method1/inputfile/{}".format(filename))

    listdiffmethod1=df1['Error(Method1(Pop Only))'].tolist()

    #updated column that CDC reports and will add to the csv
    # df1.to_csv('CDC_Reported_Death(Method1(Pop Only)).csv', mode = 'w', index=False)

    totalno=0

    #contains the the value which are neither 0 nor Not available
    newlist=[]
    for element in listdiffmethod1:
        try:
            # print(element)
            element=int(float(element))
            if element<0:
                element=element*(-1)
          
            newlist.append(element)
        except:
            totalno=totalno+1

    #to add all the element of newlist to get the total error
    print(newlist)
    sum=0

    #total error
    for ele in newlist: 
    
       
        sum = sum + (float(ele))

    print(sum)

    #number of element in the list
    # totalno=len(newlist)-totalno
    print(totalno)

   

    #avergeerror
    avgerror=float(sum)/len(newlist)

    # print(avgerror)
    # print(newlist)



    std=np.std(newlist)

    # print(std)
    #will change the name of the filename 
    x = filename.split("_")
    # y=int("".join(itertools.takewhile(str.isdigit, filename)))
    p= re.search('\d+', filename).group()
    outputfilename= x[0]+ p +'.csv'
    # print(p)
    # print(outputfilename)
    # fields=[CDC_Reported_Death(Method2(Pop+Risk)output).csv,avgerror,std]
    with open('(meanabsoluteerror+std)(method1).csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([outputfilename, avgerror, std])
