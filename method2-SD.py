import pandas as pd
import csv
from pprint import pprint
import pdb
import os
import re
# using groupby() + map() + itemgetter() + sum()
from itertools import groupby
from operator import itemgetter
from collections import defaultdict
import random
import numpy as np
import csv  
import math
from collections import defaultdict 
with open('(meanabsoluteerror+std)(method2).csv', mode='w', newline='') as csv_file:
            fieldnames = ['Filename','Mean Error(Method2)', 'Standard Deviation(Method2)']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
path = "C:/Users/Fariba Afrin Irany/Desktop/study/methods(SD included)/method2/inputfile"
# C:\Users\Fariba Afrin Irany\Desktop\study\methods(SD included)\method2\inputfile
# C:\Users\Fariba Afrin Irany\Desktop\Tiwaripaper\methods(SD included)\method2\inputfile
#if there is over or underestimation in total death for a state but no place to adjust the value that means all the error are either 0 or unavailable, in that case from the total value of error this value will be substaraced if there if overestimation or added if there is underestimation
for filename in os.listdir(path):

    adjusterror=0
    df1 = pd.read_csv("C:/Users/Fariba Afrin Irany/Desktop/study/methods(SD included)/method2/inputfile/{}".format(filename))

    # stores the method2reportedcolumn column value
    listpopulationmaincdcfile = df1['Method2(Pop+Risk)'].tolist()
    listerror=df1['Error(Method2(Pop+Risk))'].tolist()
    # print(listerror)

    #list to put the updated value method2reportedcolumn 
    method2reportedcolumn=[]
    #list to put the updated value of error
    method2error=[]

    #convert all the values to int
    for val in listpopulationmaincdcfile:

        if val=='Suppressed' or val=='Unreliable' or val=='Not available':
            method2reportedcolumn.append(val)

        else:
                val=int(float(val))
                # print(val)

                method2reportedcolumn.append(val)

    #convert all the errorvalues to int
    for val in listerror:

            try:
                val=int(float(val))
                # print(val)

                method2error.append(val)
            except:
                method2error.append(val)


    # print(method2reportedcolumn)


    df1['Method2(Pop+Risk)'] = method2reportedcolumn

    df1['Error(Method2(Pop+Risk))'] =  method2error
    x = filename.split(".")
    outputfile= x[0]+'(adjusted)'+'.csv'
    # outputfile=filename+'SD'
    # #updated column that CDC reports and will add to the csv
    df1.to_csv(outputfile, mode='w', index=False)
    # df1.to_csv('Error(Method2(Pop+Risk))', mode='w', index=False)

    # os.remove('CDC_Reported_Death_output.csv')
#row[4]=death; row[7]=method2
    with open(outputfile, 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        
        resultmain = {tuple(row[0:4]): row[4] for row in reader}

    #keep a list of suppressed or not available death column
    listkey=[]
    for keys in resultmain:
        if resultmain[keys]=='Suppressed' or resultmain[keys]=='Unreliable' or resultmain[keys]=='Not available':
            # print('ok')
            listkey.append(keys)
    # del resultmain[keys]

    for keys in listkey:
        if keys in resultmain:
            del (resultmain[keys])

    # # putting the total death using key
    # print(resultmain)

    dictdeath={}
    listdeath = []

    for keys in resultmain:
        tupli=[]
        val=resultmain[keys]
        u = keys[0]
        p = keys[0].split()
    #     # print(p[-1])

        l = keys[0].replace(keys[0], p[-1])
         
        # print(keys)

        tupli.append(keys[0])
        tupli.append(keys[1])
        tupli.append(keys[2])
        tupli.append(keys[3])
        # lst = list(keys)
        # print(tupli)
        tupli[0] = l
        # print(tupli[0])
        t = tuple(tupli)
        # print(t)
        keys=t
        #  resultdeath = {tuple(t): row[7] for row in reader}
        dictdeath[t]=val
        #  print(val)
        
        val=int(float(val))
        listdeath.append((l,val))
    # print(listdeath)
        
    # print(dictdeath)
    # print(listdeath)

  
    # print(resdeath)
    # Initialisation of list of tuple 
    # Input = [(1, 13), (1, 190), (3, 25), (1, 12)] 
    d = {x:0 for x, _ in listdeath} 
    
    for name, num in listdeath: d[name] += num 
    
    # print(d.items)
    # using map 
    # Output = (d.items())

    resdeath=[]
    for items in d.items():
        # print(items)
        resdeath.append(items)


    dictdeath = {}
    for element in resdeath:
        dictdeath[element[0]] = element[1]

    with open(outputfile, 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        
        resultmain1 = {tuple(row[0:4]): row[9] for row in reader}
    
    #dict
    with open(outputfile, 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        
        resultmainsup = {tuple(row[0:9]): row[9] for row in reader}

    #a list of tuple where county code is the key and cdc reported death is the value
    resultsup=[]
    for keys in resultmainsup:

        resultsup.append((keys[1],keys[5]))

    res = defaultdict(list) 
    for i, j in resultsup: 
        res[i].append(j) 
    
    res=dict(res)
    print(res)
    
    #the dict where key is the county code and value is the number of sup age group
    supdict={}
    for keys in res:
        # res[keys].count('Suppressed')
        supdict[keys]=res[keys].count('Suppressed')
    print(supdict)


  
    
    
    # printresultsup
     #list of all keys having a suppressed value
    listkey1=[]
    for keys in resultmain1:
        if resultmain1[keys]=='Suppressed' or resultmain1[keys]=='Unreliable' or resultmain1[keys]=='Not available':
            # print('ok')
            listkey1.append(keys)
    # del resultmain[keys]

    for keys in listkey1:
        if keys in resultmain1:
            del (resultmain1[keys])
    # print(listkey1)
    
    dictdeath1={}
    listdeath1 = []

    for keys in resultmain1:
        tupli1=[]
        val=resultmain1[keys]
        u = keys[0]
        p = keys[0].split()
    #     # print(p[-1])

        l = keys[0].replace(keys[0], p[-1])
        tupli1.append(keys[0])
        tupli1.append(keys[1])
        tupli1.append(keys[2])
        tupli1.append(keys[3])
        # tupli1 = list(keys)
        tupli1[0] = l
        t = tuple(tupli1)
        keys=t

        #  resultdeath = {tuple(t): row[7] for row in reader}
        dictdeath1[t]=val
        #  print(val)
        
        val=int(float(val))
        listdeath1.append((l,val))
    print("listdeath1")
    print(listdeath1)
        
    # print(dictdeath)

     # print(dictdeath)
    resdeath1=[]
    d1 = {x:0 for x, _ in listdeath1} 
  
    for name, num in listdeath1: d1[name] += num 

    for items in d1.items():
        print(items)
        resdeath1.append(items)
    # print(resdeath1)

    # resdeath1 = [(key, sum(map(itemgetter(1), ele)))
    #              for key, ele in groupby(sorted(listdeath1, key=itemgetter(0)),
    #                                      key=itemgetter(0))]

    # converting to a dict
    dictdeath1 = {}
    for element in resdeath1:
        dictdeath1[element[0]] = element[1]
    # print('dictdeath1')
    # print(dictdeath1)

    #difference in total death(estimated-real)
    print("resdeath1")
    print(resdeath1)
    diff = {x: dictdeath1[x] - dictdeath[x] for x in dictdeath1 if x in dictdeath}

    print('diff')
    # print(diff)
    print(diff)
    
    
    
    
    
    
    
    
    
    #for adjusting under and overestimation
    
    with open(outputfile, 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row

        
        result = {tuple(row[0:10]): row[9] for row in reader}
    # print(resultmain)
    # dict in python to store the state codes


    dictmain={}
    listmain=[]

    #a list of dict where keys is the state and val is the list of counties which gives over or underestimation for the death
    for keys in result:
        gg=[]
        gg.append(keys[0])
        gg.append(keys[1])
        gg.append(keys[2])
        gg.append(keys[3])
        gg.append(keys[4])
        gg.append(keys[5])
        gg.append(keys[6])
        gg.append(keys[7])
        gg.append(keys[8])
        gg.append(keys[9])
        val=result[keys]
        u = keys[0]
        p = keys[0].split()
    #     # print(p[-1])

        l = keys[0].replace(keys[0], p[-1])
        # lst = list(keys)
        gg[0] = l
        t = tuple(gg)
        keys=t
        #  resultdeath = {tuple(t): row[7] for row in reader}
        dictmain[t]=l

    listdel=[]

    # #removing all elements from list with 0 error
    # for keys in dictmain:
    #     val=2
    #     try:
    #             val=int(float(val))
    #             # print(val)

    #     except:
    #             method2error.append(val)
        
    #     # if keys[9]=='0':
    #     #     listdel.append(keys)
    #     # if keys[9]=='Not available' or keys[9]=='N/A' or :
    #     #     listdel.append(keys)

    # for keys in listdel:
    #     if keys in dictmain:
    #         del (dictmain[keys])
    # # print(dictmain)

    liststate = ["AL", "AK", "AZ",  "AR",  "CA",  "CO","CT", "DE", "DC", "FL", "GA",  "HI",  "ID",  "IL","IN",  "IA",  "KS",  "KY",
            "LA",  "ME",  "MD",  "MA",  "MI",  "MN",
            "MS",  "MO",  "MT", "NE",
            "NV",  "NH",  "NJ",  "NM",  "NY",
            "NC",  "ND",  "OH",
            "OK",  "OR",  "PA",  "RI",  "SC",
            "SD", "TN",  "TX", "UT",  "VT",
            "VA",  "WA",  "WV", "WI", "WY",
            "MH",  "DC"]

    #a dict where keys is the state and value is a list of tuple for all counties for all age group in the state
    dictvalue={}
    for val in liststate:
        listu=[]
        for keys in dictmain:
            if dictmain[keys]==val:
                #  if supdict[keys[1]]
                if keys[5]== 'Suppressed' and supdict[keys[1]]!=1:
                # if keys[5]!='Not available':
                    # if keys[5]== 'Suppressed':
                        listu.append(keys)
            # print(listu)
        dictvalue[val]=listu

    # print(dictvalue)


#reading the file for readjusted of the cases when there is over or underestimation but not place to adjust the death that means all the error are either 0 or not available
    #row[4]=death; row[7]=method2
    with open(outputfile, 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        
        resultadj = {tuple(row[0:3]): row[9] for row in reader}
    
    # print( resultadj)
#    dict with keys (county code, age group) and value=values need to be adjusted
    
    dictoverunder={}
    # print(dictdeath)
    # print(dictdeath1)
    # print(diff)

    for keys in diff:
        #  print(diff[keys])
        #a list
        val=dictvalue.get(keys)
        m=0
        #  print(val)
        if len(val) != 0: 
            if diff[keys]>0:
                for i in range(0, diff[keys]):
                    
                    #  numberList = [111,222,333,444,555]
                    ele=random.choice(val)

                    if (ele[0],ele[1],ele[2]) in dictoverunder:
                        dictoverunder[(ele[0],ele[1], ele[2])]=  dictoverunder[(ele[0],ele[1],ele[2])]+1
                        m=m+1
                    else:
                        dictoverunder[(ele[0],ele[1],ele[2])]=1
                        m=m+1
            elif diff[keys]<0:
                diff[keys]=diff[keys]*(-1)
                for i in range(0, diff[keys]):
                    
                    ele=random.choice(val)

                    if (ele[0],ele[1],ele[2]) in dictoverunder:
                        dictoverunder[(ele[0],ele[1], ele[2])]=  dictoverunder[(ele[0],ele[1],ele[2])]-1
                        m=m+1
                    else:
                        dictoverunder[(ele[0],ele[1],ele[2])]=-1
                        m=m+1
        #the cases where there is over or under estimation but no places to adjust the value
        # if m!=diff[keys]:
        #     list=[]
        #     if diff[keys]!=0:
        #         # print(keys)
        #         # print(diff[keys])
        #         # print("not ok")
        #         adjusterror=adjusterror+diff[keys]
        #         # print(adjusterror)
        
          #for adjusting the over and underestimation of the method column

    #row[4]=death; row[7]=method2
    with open(outputfile, 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        
        resultmethod = {tuple(row[0:3]): row[9] for row in reader}

    # print(resultmethod)


    for keys in resultmethod:
        if resultmethod[keys]!='Not available':

            for val in dictoverunder:
                if val[1]==keys[1] and val[2]==keys[2]:
                    #  print(keys)
                    #  print(type(resultmethod[keys]))
                    #resultmethod[keys] is converted to int
                    valresult=int(float(resultmethod[keys]))
                    #  print(valresult)
                    #  print(dictoverunder[val])
                    #  print('previous')
                    #  print(resultmethod[keys])
                    if dictoverunder[val]>=0:
                        valresult=valresult-dictoverunder[val]
                    elif dictoverunder[val]<=0:
                        valresult=valresult+((dictoverunder[val])*(-1))
                    resultmethod[keys]=valresult
                    #  print('after')

                    #  print(resultmethod[keys])
                    # print(type(valresult))
                    #  print(type(dictoverunder[val]))
                    if type(valresult)!=type(dictoverunder[val]):
                        print('not similar')
                    break 

    # print(resultmethod)
    #put all the values in a list(contains updated value for over and underestimation)
    overunder=[]
    for keys in resultmethod:
        overunder.append(resultmethod[keys])
        

    df1['Method2(Pop+Risk)(adjusted)'] = overunder

    # df1['Error(Method2(Pop+Risk))'] =  method2error

    # #updated column that CDC reports and will add to the csv
    df1.to_csv(outputfile, mode='w', index=False)
   

    df1 = df1.drop('Method2(Pop+Risk)', axis=1)
    df1.to_csv(outputfile, mode='w', index=False)

    df1 = df1.drop('Error(Method2(Pop+Risk))', axis=1)
    df1.to_csv(outputfile, mode='w', index=False)
    #list to keep the difference column


    df1 = df1.drop('Method2(Pop+Risk)(adjusted)', axis=1)
    df1.to_csv(outputfile, mode='w', index=False)
    #list to keep the difference column


    
    df1['Method2(Pop+Risk)'] = overunder

    # df1['Error(Method2(Pop+Risk))'] =  method2error

    # #updated column that CDC reports and will add to the csv
    df1.to_csv(outputfile, mode='w', index=False)


   


     #to adjust the method1 column basing on cdc death column
   # print(adjusterror)

    cdcdeathlist=df1['CDCDeaths'].tolist()
    method2list = df1['Method2(Pop+Risk)'].tolist()
    # errorcdc=df1['Error(Method2(Pop+risk)'].tolist()

    #to correct method column basing on the cdcdeathcolumn
    cdcdeathvallist=[]
    methodvallist=[]
    # errorvallist=[]


    for i,j in zip( cdcdeathlist,method2list):
             if i=='Suppressed':
                methodvallist.append(j)
             
             elif i=='Not available':
                 methodvallist.append('N/A')

             else:
                 methodvallist.append('N/A')
    #     #    print (i,j)
    
    # if len(cdcdeathlist)==len(method2list):
    #      print('same length')

    df1['Method2(Pop+Risk)'] =  methodvallist
    df1.to_csv(outputfile, mode='w', index=False)


    # # errormiscal=df1['CDCDeaths'].tolist()


    listdiffmethod=[]

    s=0 
    # #error column calculation
    with open(outputfile, "r") as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
        #  reader = csv.reader(infh)
         next(csv_reader)  # skip the header row
         for lines in csv_reader:
             try:
                 float(lines[9])
                 float(lines[4])
    #             # print(lines[8])
    #             # print(lines[8])
                 diff=float(lines[9])-float(lines[4])
    #             # print(diff)

                
                 if diff==0.0 and lines[5]=='Suppressed':
                     diff=diff
                 elif diff==0.0:
                      diff='N/A'

                    
                 listdiffmethod.append(diff)
                 s=s+1

             except ValueError:
    #             # if diff
                 diff='N/A'
    #             # print ("Not a float")
                 listdiffmethod.append(diff)
                 s=s+1
    
    
  
    #   #converting all error of listdiffmethod to int
    listerroradj=[]


    for val in listdiffmethod:
       try:
         val=float(val)
         listerroradj.append(val)


       except ValueError:
         listerroradj.append(val)
    #     # pass
    #     # print ("Not a float")


                      

    df1['Error(Method2(Pop+Risk))']=listerroradj
    df1.to_csv(outputfile, mode='w', index=False)


    
    totalno=0

    # #contains the the value which are neither 0 nor Not available
    newlist=[]
    for element in listerroradj:
         try:
             element=float(element)
    #             # print(val)
             if element<0:
                 element=element*(-1)
            
             newlist.append(element)
        
         except:            
              totalno=totalno+1
    # # print(newlist)
    # #to add all the element of newlist to get the total error
    sum=0.0

    # #total error
    for ele in newlist: 
         sum = sum + ele
    # # print(sum)


    # #avergeerror
    # # print(len(newlist))
    avgerror=int(sum)/len(newlist)


  
    std=np.std(newlist)

    # # print(std)

    #    #will change the name of the filename 
    x = filename.split("_")
    # # y=int("".join(itertools.takewhile(str.isdigit, filename)))
    p= re.search('\d+', filename).group()
    outputfilename1= x[0]+ p +'.csv'
    # # print(p)
    # # print(outputfilename1)
    # # fields=[CDC_Reported_Death(Method2(Pop+Risk)output).csv,avgerror,std]
    # # print(avgerror)
    with open('(meanabsoluteerror+std)(method2).csv', 'a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([outputfilename1, avgerror, std])


 







    