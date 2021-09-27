import pandas as pd
import csv
from pprint import pprint
import pdb
# import pdb
import os
# using groupby() + map() + itemgetter() + sum() 
from itertools import groupby 
from operator import itemgetter 
from collections import defaultdict

path = "C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method3/weightfile"

for filename in os.listdir(path):

    with open(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method3/weightfile/{}".format(filename), newline='') as csv_file:
        reader = csv.reader(line.replace('  ', ',') for line in csv_file)
        my_list = list(reader)
    for element in my_list:
        while ("" in element):
            element.remove('')
    list1 = []
    list2 = []
    for element in my_list:
        k = 0
        listnested = []
        for i in element:
            if k == 1:
                # print()
                listnested.append(i)
                # print(i)
            else:
                list1.append(i)
                k = 1
        list2.append(listnested)

    dictfinal = dict(zip(list1, list2))
    # print(dictfinal)
    #for crude rate
    with open('cdc(agegroups).csv', 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        result = {tuple(row[2:4]): row[7] for row in reader}
        # resultmain= {tuple(row[1:7]): row[7] for row in reader}
    
        # resultall={tuple(row[2:7]): row[7] for row in reader}
    result1 = dict(result)
    # print( result)  
    #dict with all the results
    # resultall=dict(resultall)
    # print(resultall)
    #for death
    with open('cdc(agegroups).csv', 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        #the dict with both pop and death of a county(almost all the entries) in input file
        resultdeath = {tuple(row[2:4]): row[5] for row in reader}
        # resultmain= {tuple(row[1:7]): row[7] for row in reader}
        #the dict with both pop and death of a county(almost all the entries)
        # resultall={tuple(row[2:7]): row[7] for row in reader}
    resultdeath1  = dict(resultdeath)
    #dict with all the results
    # resultall=dict(resultall)
    # print(resultall)
    #for population 
    with open('cdc(agegroups).csv', 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        #the dict with both pop and death of a county(almost all the entries) in input file
        resultpopulation = {tuple(row[2:4]): row[6] for row in reader}
        # resultmain= {tuple(row[1:7]): row[7] for row in reader}
        #the dict with both pop and death of a county(almost all the entries)
        # resultall={tuple(row[2:7]): row[7] for row in reader}
    resultpopulation1  = dict(resultpopulation)


    with open('cdc(agegroups).csv', 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        resultmain = {tuple(row[0:7]): row[7] for row in reader}
    # print(resultmain)

    #for crude rate
    for keys in result:
        if keys[0] in dictfinal:
            # if result[keys] != 'Suppressed':
                # print(result[keys])
            result[keys] = dictfinal[keys[0]]
    # print(result1)


    #for death
    for keys in resultdeath :
        if keys[0] in dictfinal:
            # if result[keys] != 'Suppressed':
                # print(result[keys])
            resultdeath[keys] = dictfinal[keys[0]]
    # resultmaindeath=result.copy()
    # resultmaindeath = copy.deepcopy(result)
    #for population
    for keys in resultpopulation:
        if keys[0] in dictfinal:
            # if result[keys] != 'Suppressed':
                # print(result[keys])
            resultpopulation[keys] = dictfinal[keys[0]]
    # resultmainpopulation=copy.deepcopy(result)


    #for crude rate
    for keys in result:
        firstelement = keys[0]
        # print(firstelement)
        # print(firstelement)
        secondelement = keys[1]
        # print(secondelement)

        if isinstance(result[keys], list):
            newlist = []
            totalint = 0
            sum = 0
            for element in result[keys]:           
                tar_tup = (element, secondelement)
                res = tar_tup in result1
                if res == True:
                    newlist.append(result1[(element, secondelement)])
                    #add newlist death
                    # print(newlist)
                # if no entry in csv file cdc(agegroup) for that adjacency list, we remove the element
                else:
                    result[keys].remove(element)
            result[keys] = newlist
            # print( result[keys])

    #for death
    for keys in resultdeath:
        firstelement = keys[0]
        # print(firstelement)
        # print(firstelement)
        secondelement = keys[1]
        # print(secondelement)

        if isinstance(resultdeath[keys], list):
            newlist = []
            totalint = 0
            sum = 0
            for element in resultdeath[keys]:           
                tar_tup = (element, secondelement)
                res = tar_tup in resultdeath1
                if res == True:
                    newlist.append(resultdeath1[(element, secondelement)])
                    #add newlist death
                    # print(newlist)
                # if no entry in csv file cdc(agegroup) for that adjacency list, we remove the element
                else:
                    resultdeath[keys].remove(element)
            resultdeath[keys] = newlist
            # print( result[keys])

    #for population
    for keys in resultpopulation:
        firstelement = keys[0]
        # print(firstelement)
        # print(firstelement)
        secondelement = keys[1]
        # print(secondelement)

        if isinstance(resultpopulation[keys], list):
            newlist = []
            totalint = 0
            sum = 0
            for element in resultpopulation[keys]:           
                tar_tup = (element, secondelement)
                res = tar_tup in resultpopulation1
                if res == True:
                    newlist.append(resultpopulation1[(element, secondelement)])
                    #add newlist death
                    # print(newlist)
                # if no entry in csv file cdc(agegroup) for that adjacency list, we remove the element
                else:
                    resultpopulation[keys].remove(element)
            resultpopulation[keys] = newlist
            # print( result[keys])

    # print(resultpopulation)

    #for crude rate      
    for keys in result:
        len=0
        for element in result[keys]:
            len=len+1
        dummy=0
        totalelement = 0
        sum = 0
        # print(result[keys])
        if isinstance(result[keys], list):
            # length=len(result[keys])
            # print(length)
            totalelement = 0
            sum = 0
            for element in result[keys]:
                try:
                    dummy=dummy+1    
                    val=float(element)
                    totalelement = totalelement + 1
                    sum = sum + val
                    if dummy==len and sum>0:
                        result[keys]=sum/totalelement
                        #   print(result[keys]) 
                #   print(element)
                except ValueError:
                    if dummy==len and sum>0:
                        result[keys]=sum/totalelement
                        #   print (result[keys])
                    elif dummy==len and sum==0:
                        def most_frequent(List): 
                            counter = 0
                            num = List[0] 
                            for i in List: 
                                curr_frequency = List.count(i) 
                                if(curr_frequency> counter): 
                                    counter = curr_frequency 
                                    num = i 
                            return num 
                        result[keys]=most_frequent(result[keys])
                        # print (result[keys])
    
    x = filename.split(".")

    #file with cdc repoted column
    outputfilename= x[0] +'output'+ '.csv'
    # print(outputfilename)
    # cdcreportedfilename=filename+
    #cdc reporteddeat_column
    with open(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method3/inputfile/{}".format(outputfilename), 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        resultcdcreporteddeath = {tuple(row[1:3]): row[5] for row in reader}
        # resultmain= {tuple(row[1:7]): row[7] for row in reader}
    
        # resultall={tuple(row[2:7]): row[7] for row in reader}
    resultcdcreporteddeath1 = dict(resultcdcreporteddeath)
    # print(resultcdcreporteddeath1)


    #cdc reporteddeat_column
    with open(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method3/inputfile/{}".format(outputfilename), 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        resultpopofcounty = {tuple(row[1:3]): row[6] for row in reader}
        # resultmain= {tuple(row[1:7]): row[7] for row in reader}
    
        # resultall={tuple(row[2:7]): row[7] for row in reader}
    resultpopofcounty1 = dict(resultpopofcounty)
    # print(resultcdcreporteddeath1)



    k=0
    #new crude rate
    dictcruderate={}
    for keys in resultcdcreporteddeath1:
        
        if resultcdcreporteddeath[keys]=='Suppressed' or resultcdcreporteddeath[keys]=='Unreliable' or resultcdcreporteddeath[keys]=='Not available':
            if keys in resultdeath and keys in resultpopulation:
                deathlist=[]
                poplist=[]

                k=k+1
                # print(resultdeath[keys])
                # print(resultpopulation[keys])
                # if (len(resultdeath[keys])==len(resultpopulation[keys])):
                # if isinstance(resultdeath[keys], list)==True:
                #     print(len(resultdeath))
                # print('ol')
                countdeath = 0
                # for x in resultdeath[keys]: 
                if isinstance(resultdeath[keys], list): 
                        for val in resultdeath[keys]: 
                            countdeath += 1 
                # print(countdeath) 
                countpop=0
                if isinstance(resultpopulation[keys], list): 
                        for val in resultpopulation[keys]:
                            countpop += 1 
                # print(countpop) 
                #if list of pop and list of death ae equal
                if (countdeath==countpop):
                    # k=k+1
                    # print("same length")
                    # print(resultdeath[keys])
                    # print(resultpopulation[keys])
                    if isinstance(resultdeath[keys], list): 
                        #  print(resultdeath[keys])
                        #  print(resultpopulation[keys])
                        #while list is not empty
                        while resultdeath[keys]!=None: 
                            
                            if resultdeath[keys][0]=='Suppressed' or resultdeath[keys][0]=='Not available':
                                del resultdeath[keys][0]
                                del resultpopulation[keys][0]
                                # print(val)
                                # print(resultdeath[keys])
                                # print(resultpopulation[keys])
                                #if list is empty
                                if not resultdeath[keys]:
                                    break



                            else:
                                # print(val)

                                deathlist.append(resultdeath[keys][0])
                                # print(resultpopulation[keys])

                                poplist.append(resultpopulation[keys][0])
                                del resultdeath[keys][0]
                                del resultpopulation[keys][0]
                                # print(resultdeath[keys])
                                # print(resultpopulation[keys])
                                #if list is empty
                                if not resultdeath[keys]:
                                        break
                            
                        #the new list without including the suppressed cases for adjacent counties

                    # print(deathlist)
                    # print(poplist)
                    d=0
                    p=0
                    #how to convert all element of deathlist to int
                    for ele in deathlist:
                        d=d+int(ele)
                    # death_list = list(map(int, deathlist)) 
                    #summing up elements of deathlist
                    # d=sum(death_list)
                    # print(d)
                    #how to convert all element of poplist to int
                    for ele in poplist:
                        p=p+int(ele)
                    # pop_list = list(map(int, poplist)) 
                    #summing up elements of poplist
                    # p=sum(pop_list)
                    # print(p)
                    #new crude rate calc= death of adj county/pop of adj county
                    if d==0:
                        cruderate= resultcdcreporteddeath[keys]
                    #    print(cruderate)
                    else:
                        cruderate=float(d/p)
                    # print(cruderate)
                    # print(keys)
                        dictcruderate[keys]=cruderate
                    
                    

                    


                            
                            #   print(val) 

                else:
                    print("list length not same")
            else:
                # k=k+1
                print('exception')
                
    # print(dictcruderate)
    #method3(pop+local risk column calculation)
    # print(resultpopofcounty1)

    # print(dictcruderate)
    newdictmethod3={}

    # calculating the new column for method3(pop+local risk column calculation)
    for keys in resultcdcreporteddeath1:   

        if resultcdcreporteddeath[keys]=='Suppressed' or resultcdcreporteddeath[keys]=='Unreliable' or resultcdcreporteddeath[keys]=='Not available':
            value=keys
            for keys in dictcruderate:
                if keys==value:
                    #new val can be changed t not available
                    if dictcruderate[keys]=='Suppressed' or dictcruderate[keys]=='Unreliable':
                        newval=dictcruderate[keys]
                        newdictmethod3[keys]=newval
                    elif dictcruderate[keys]=='Not available':                      
                        newdictmethod3[keys]='Not available'
                    else:
                            valuecruderate=float(dictcruderate[keys])
                            # print(valuecruderate)
                            for keys in resultpopofcounty1:
                            

                                if keys==value:
                                    if resultpopofcounty1[keys]=='Suppressed' or resultpopofcounty1[keys]=='Not available':
                                        #can be changed to not avaalable
                                        newval=resultpopofcounty1[keys]
                                        newdictmethod3[keys]=newval
                                    else:
                                        valuepop=int(resultpopofcounty1[keys])
                                        # print(valuecruderate)
                                        # print(valuepop)
                                        newval=float(valuecruderate*valuepop)
                                        newdictmethod3[keys]=newval
                                        # print(newdictmethod3)
    print(newdictmethod3)

    newcolumnlist=[]
    #making a new column
    for keys in resultcdcreporteddeath1:  
        if resultcdcreporteddeath1[keys]=='Not available':
            newcolumnlist.append('Not available')
        
        else:
            if resultcdcreporteddeath[keys]=='Suppressed' or resultcdcreporteddeath[keys]=='Unreliable' or resultcdcreporteddeath[keys]=='Not available':
                if keys in newdictmethod3:
                    #  print("blah")
                    newcolumnlist.append(newdictmethod3[keys])
                
                # if resultcdcreporteddeath[keys]=='Not available'
                else:
                    #if the key is not present, the val is assumed 0
                    newcolumnlist.append(0)
            

            else:
                newcolumnlist.append(resultcdcreporteddeath[keys])
    #pandas dataframe to read the csv 
    df1= pd.read_csv(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method3/inputfile/{}".format(outputfilename))

    df1['Method3(Pop+local risk)']=newcolumnlist

    df1.to_csv('CDC_Reported_Death(Method3(Pop+local risk))(without error).csv', mode = 'w', index=False)            

    #list to keep the difference column
    listdiffmethod3=[]
    df1= pd.read_csv("CDC_Reported_Death(Method3(Pop+local risk))(without error).csv")  
    s=0    
    with open("CDC_Reported_Death(Method3(Pop+local risk))(without error).csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # reader = csv.reader(infh)
        next(csv_reader)  # skip the header row
        for lines in csv_reader:
            try:
                float(lines[9])
                float(lines[4])
                print(lines[9])
                print(lines[9])
                diff=float(lines[9])-float(lines[4])
                print(diff)
                listdiffmethod3.append(diff)
                s=s+1

            except ValueError:
                diff='Not available'
                print ("Not a float")
                listdiffmethod3.append(diff)
                s=s+1

    print(s)
        # if (isinstance(lines[4], float))==True and (isinstance(lines[8], float))==True:
        #     diff=float(lines[8])-float(lines[4])
        #     listdiffmethod3.append(diff)

        # else:
        #     diff='Not available'
        #     listdiffmethod3.append(diff)

    # pnt(listdiffmethod3)
    print(listdiffmethod3)
    df1['Error(Method3(Pop+local_risk))']=listdiffmethod3


    # x = filename.split(".")
    # outputfilename= x[0]+'output(Method1)'+'.csv'
    #write updated column
    x = filename.split(".")
    outputfilemethod3=x[0]+'(Method3)'+'.csv'
    df1.to_csv(outputfilemethod3, mode = 'w', index=False)
    os.remove('CDC_Reported_Death(Method3(Pop+local risk))(without error).csv')


        # print(resultfinal)
    countycodelist = df1['County Code'].tolist()
    death_cdcreported = df1['CDCDeaths'].tolist()
        
    nest=[]
    # if len(countycodelist)==len(death_cdcreported):
        # print('same')
    counter=0
    for i in countycodelist: 
      
    # incrementing counter 
        counter = counter + 1
        
    while(counter != 0): 
           
        nest.append((countycodelist[0], death_cdcreported[0]))
        del countycodelist[0]
        del death_cdcreported[0]
        counter=counter-1
        # print(nest)
        
    dictkey={}
    for keys in nest:
        val1=keys[0]
        val2=keys[1]
        lu=[]
        n=0
        for keys in nest:
               
            if keys[0]==val1:
                if keys[1]=='Suppressed':
                    lu.append(keys[1]) 
                     
                n=n+1

                if n==5:
                    break                   
            dictkey[val1]=lu
    print(dictkey)
        
        # for keys in dictkey:
        #     print(keys)
        #     dictkey[keys].count('Suppressed')

    for keys in dictkey:
        dictkey[keys]=dictkey[keys].count('Suppressed')

    print(dictkey)



    with open(outputfilemethod3 , 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
            # result = {row[1]: row[7] for row in reader}
        resultfinal= {tuple(row[0:11]): row[10] for row in reader}

    with open(outputfilemethod3, mode='w', newline='') as csv_file:
        fieldnames = ['County','County Code', 'Ten-Year Age Groups','Ten-Year Age Groups Code','Sim_Deaths','CDCDeaths','CDCPopulation', 'SimCrude Rate','CDCCrudeRate', 'Method3(Pop+local risk)', 'Error(Method3(Pop+local_risk))']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for keys in resultfinal:
            code=keys[1]
            method=keys[9]
            error=keys[10]

            if keys[5]=='Suppressed':
                for ele in dictkey:
                    if str(ele)==code:
                        if dictkey[ele]==1:
                            method=keys[4]
                            error=0
                            break         
            writer.writerow({'County': keys[0], 'County Code': keys[1],
                                                'Ten-Year Age Groups': keys[2], 'Ten-Year Age Groups Code': keys[3], 'Sim_Deaths':keys[4],
                                                'CDCDeaths': keys[5], 'CDCPopulation': keys[6],
                                                'SimCrude Rate': keys[7], 'CDCCrudeRate': keys[8], 'Method3(Pop+local risk)': method, 'Error(Method3(Pop+local_risk))': error})




