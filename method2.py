
import pandas as pd
import csv
from pprint import pprint
import pdb
import os
# using groupby() + map() + itemgetter() + sum() 
from itertools import groupby 
from operator import itemgetter 
from collections import defaultdict
path = "C:/Users/Fariba Afrin Irany/Desktop/study/Methods/Method2/inputfile"

for filename in os.listdir(path):

        # filename=r”C:/Users/Fariba Afrin Irany/Desktop/Tiwaripaper/Methods/method2/inputfile/{}”.format(filename)
        x = filename.split(".")
        outputfilename= x[0]+'(Method2)'+'.csv'
        # print(outputfilename)

        output_file = outputfilename
        cols_to_remove = [1] # Column indexes to be removed (starts at 0)
        cols_to_remove = sorted(cols_to_remove, reverse=True) # Reverse so we remove from the end first
        row_count = 0 # Current amount of rows processed
        with open(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/Method2/inputfile/{}".format(filename), "r") as source:
            reader = csv.reader(source)
            with open(output_file, "w", newline='') as result:
                writer = csv.writer(result)
                for row in reader:
                    row_count += 1
                    # print('\r{0}'.format(row_count), end='') # Print rows processed
                    for col_index in cols_to_remove:
                        del row[col_index]
                    writer.writerow(row)

        #dict in python to store the state codes
        dict={"Alabama":"AL", "Alaska":"AK", "Arizona":"AZ", "Arkansas":"AR", "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
        "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana":"IN", "Iowa": "IA", "Kansas":"KS", "Kentucky":"KY", 
        "Louisiana":"LA", "Maine":"ME", "Maryland":"MD", "Massachusetts":"MA", "Michigan":"MI", "Minnesota":"MN", "Mississippi": "MS", "Missouri":"MO", "Montana":"MT", "Nebraska":"NE",
        "Nevada":"NV", "New Hampshire":"NH", "New Jersey":"NJ","New Mexico":"NM", "New York":"NY","North Carolina":"NC","North Dakota":"ND","Ohio":"OH",
        "Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT",
        "Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY", "Marshall Islands":"MH", "District of Columbia":"DC"}  

        dict1={}
        #list to hold the county code
        list=[]

 

        with open(output_file , 'r') as infh:
            reader = csv.reader(infh)
            next(reader)  # skip the header row
            # result = {row[1]: row[7] for row in reader}
            resultmain= {tuple(row[0:2]): [row[3], row[5]] for row in reader}
            # list.append(result)
        # print(resultmain)
        #keep list of all element that has either population or death value suppressed or unreliable that means any value other than float
        listdel=[]
        for keys in resultmain:
            try:
                float(resultmain[keys][0])
                # print(float(resultmain[keys][0]))
                float(resultmain[keys][1])
                # print(float(resultmain[keys][1]))
            

            except ValueError:
                # print(resultmain[keys])
                listdel.append(keys)
                # print(listdel)
                # print ("Not a float")

        # print(resultmain)
            # if resultmainpop[keys][0]  and resultmainpop[keys][1]==
        #resultmain is the dict which stores 
        # print(resultmain)
        # print(listdel)
        newlist=[]
        for keys in listdel:
            if keys in resultmain:
                del(resultmain[keys])
                # print(resultmain)
                # break
        # print(resultmain)   
                
                # print('"list" is found in ourlist')

        #putting the total death using key
        # dictdeath={}
        listdeath=[]
        for keys in resultmain:
            u=keys[0]
            p=keys[0].split()
            # print(p[-1])
            l=keys[0].replace(keys[0], p[-1])
            m=keys[1]
            # dictdeath[(u,l,m)] = resultmain[keys][0]
            v=l+m
            r=float(resultmain[keys][0])
            # dictpop[(u,l,m)] = 
            listdeath.append((v, r))

        # print(dictpop)
        # print(listdeath)    
        #respop contains the aggrgated value of pop
        # Aggregate values by tuple keys 
        # using groupby() + map() + itemgetter() + sum() 
        resdeath = [(key, sum(map(itemgetter(1), ele))) 
            for key, ele in groupby(sorted(listdeath, key = itemgetter(0)),  
                                                        key = itemgetter(0))] 
        
        # printing result 
        # print(str(resdeath)) 
        #converting to a dict
        dictdeath={}
        for element in resdeath:
            dictdeath[element[0]]=element[1]
        # print(dictdeath)

        #putting the total pop in list using key
        listpopulation=[]
        #resultmain is the dict which stores 
        # print(resultmain)

        for keys in resultmain:
            u=keys[0]
            p=keys[0].split()
            # print(p[-1])
            l=keys[0].replace(keys[0], p[-1])
            m=keys[1]
            v=l+m
            r=float(resultmain[keys][1])
            # dictpop[(u,l,m)] = 
            listpopulation.append((v, r))
            
        # print(dictpop)
        # print(listpopulation)    
        #respop contains the aggrgated value of pop
        # Aggregate values by tuple keys 
        # using groupby() + map() + itemgetter() + sum() 
        respop = [(key, sum(map(itemgetter(1), ele))) 
            for key, ele in groupby(sorted(listpopulation, key = itemgetter(0)),  
                                                        key = itemgetter(0))] 
        
        # printing result 
        # print(str(respop)) 

        #converting to a dict
        dictpop={}
        for element in respop:
         dictpop[element[0]]=element[1]
        # print(dictpop)

        #reading from the file to add a new column state rate
        with open(output_file , 'r') as infh:
            reader = csv.reader(infh)
            next(reader)  # skip the header row
            # result = {row[1]: row[7] for row in reader}
            result= {tuple(row[0:2]): row[5] for row in reader}

        # print(result)

        #cdc file in dict
        dictmainfile={}
        for keys in result:
            u=keys[0]
            p=keys[0].split()
            # print(p[-1])
            l=keys[0].replace(keys[0], p[-1])
            m=keys[1]
            v=l+m
            r=(result[keys][1])
            # dictpop[(u,l,m)] = 
            # listpopulation.append((v, r))
            
            for val in dictpop:
                if val==v:
                    result[keys]=float(dictdeath[val]/dictpop[val])
        # print(result)

        #state rate column
        staterate=[]
        for keys in result:
            staterate.append(result[keys])

        # print(staterate)
        df1= pd.read_csv(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/Method2/inputfile/{}".format(filename))
        # df1['State_rate']=staterate
        #updated column that CDC reports and will add to the csv
        # df1.to_csv('CDC_Reported_Death(Method2(Pop+Risk Only)).csv', mode = 'w', index=False)

        #stores the population column value
        listpopulationmaincdcfile = df1['CDCPopulation'].tolist()

        deathmainfile=df1['CDCDeaths'].tolist()
        # print(deathmainfile)

        os.remove(output_file )

        #checking if length of two list are same or not
        # print(staterate)
        # print(len(staterate))
        # print(len(listpopulationmaincdcfile))
        # print(len(deathmainfile))

        Risk=[]
        # Iterating the index 
        # same as 'for i in range(len(list))' 
        #calculating the new column found by multiplying the 
        while (len(listpopulationmaincdcfile) != 0):
            # if deathmainfile[0]=='Not available':
            #     Risk.append('Not available')
            if str(deathmainfile[0]).isdigit()==True:
                val=deathmainfile[0]
                Risk.append(val)
                # print(listpopulationmaincdcfile[0] )
                # print(deathmainfile[0] )
                # print( staterate[0] )
                del listpopulationmaincdcfile[0] 
                del deathmainfile[0] 
                del staterate[0] 
            elif deathmainfile[0]=='Not available':
                val='Not available'
                Risk.append(val)
                # print(listpopulationmaincdcfile[0] )
                # print(deathmainfile[0] )
                # print( staterate[0] )
                del listpopulationmaincdcfile[0] 
                del deathmainfile[0] 
                del staterate[0] 


        
            else:

                if str(listpopulationmaincdcfile[0]).isdigit()==True:
                    try:
                        # print(listpopulationmaincdcfile[0] )
                        # print(deathmainfile[0] )
                        # print( staterate[0] )
                        float(staterate[0])
                        val=int(listpopulationmaincdcfile[0])*float(staterate[0])
                        Risk.append(val)
                        del listpopulationmaincdcfile[0] 
                        del staterate[0] 
                        del deathmainfile[0] 
                    except:
                        # print(listpopulationmaincdcfile[0] )
                        # print(deathmainfile[0] )
                        # print( staterate[0] )
                        # print('not a float')
                        Risk.append(deathmainfile[0])
                        del listpopulationmaincdcfile[0] 
                        del staterate[0] 
                        del deathmainfile[0] 
                        
                    
                else:
                    Risk.append(deathmainfile[0])
                    del listpopulationmaincdcfile[0] 
                    del staterate[0] 
                    del deathmainfile[0] 
                    
            # print(Risk)

            #listriskContains the statewide rate    

        df1['Method2(Pop+Risk)']=  Risk    
        df1.to_csv(output_file, mode = 'w', index=False)

        #stores method2 column
        # #list to keep the difference column error
        listdiffmethod2=[]
        with open(output_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            reader = csv.reader(csv_reader)
            next(csv_reader)  # skip the header row
            for lines in csv_reader:
                    try:
                        float(lines[9])
                        float(lines[4])
                    
                        diff=float(lines[9])-float(lines[4])
                        # print(diff)
                        if diff==0:
                            listdiffmethod2.append('N/A')
                        else:
                            listdiffmethod2.append(diff)
                

                    except ValueError:
                        diff='N/A'
            #             # print ("Not a float")
                        listdiffmethod2.append(diff)


        df1['Error(Method2(Pop+Risk))']=listdiffmethod2

        # #updated column that CDC reports and will add to the csv
        df1.to_csv(output_file, mode = 'w', index=False)

        #making the suppressed value equla to the death value for all counties where only one age is suppressed, as methods are not really contributing towards it
        # dictcounty={}



    

        # print(resultfinal)
        countycodelist = df1['County Code'].tolist()
        death_cdcreported = df1['CDCDeaths'].tolist()
        
        nest=[]
        
        while (len(countycodelist) != 0): 
           
            nest.append((countycodelist[0], death_cdcreported[0]))
            del countycodelist[0]
            del death_cdcreported[0]
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



        with open(output_file , 'r') as infh:
            reader = csv.reader(infh)
            next(reader)  # skip the header row
            # result = {row[1]: row[7] for row in reader}
            resultfinal= {tuple(row[0:11]): row[10] for row in reader}

        with open(output_file, mode='w', newline='') as csv_file:
            fieldnames = ['County','County Code', 'Ten-Year Age Groups','Ten-Year Age Groups Code','Sim_Deaths','CDCDeaths','CDCPopulation', 'SimCrude Rate','CDCCrudeRate', 'Method2(Pop+Risk)', 'Error(Method2(Pop+Risk))']
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
                    # else:



                

   
                
                # #if the population column is suppressed
                # if sixthelement=='Suppressed':
                writer.writerow({'County': keys[0], 'County Code': keys[1],
                                                'Ten-Year Age Groups': keys[2], 'Ten-Year Age Groups Code': keys[3], 'Sim_Deaths':keys[4],
                                                'CDCDeaths': keys[5], 'CDCPopulation': keys[6],
                                                'SimCrude Rate': keys[7], 'CDCCrudeRate': keys[8], 'Method2(Pop+Risk)': method, 'Error(Method2(Pop+Risk))': error})


