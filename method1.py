import pandas as pd
import csv
from pprint import pprint
import pdb
import os
path = "C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method1/inputfile"

# C:\Users\Fariba Afrin Irany\Desktop\Tiwaripaper\Methods\method1\inputfile
for filename in os.listdir(path):
    df1= pd.read_csv(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method1/inputfile/{}".format(filename))
    # with open('CDC_Reported_Death.csv', 'r') as infh:
    #     reader = csv.reader(infh)
    #     next(reader)  # skip the header row
    #     resultmain = {tuple(row[0:7]): row[8] for row in reader}
    # # print(resultmain)
    #readings rows in a tuple
    with open(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method1/inputfile/{}".format(filename), 'r') as infh:
        reader = csv.reader(infh)
        next(reader)  # skip the header row
        result = {tuple(row[0:7]): row[5] for row in reader}
        # resultmain= {tuple(row[1:7]): row[7] for row in reader}
    result1 = dict(result)
    # print(result1)
    listcounty=[]
    listdeath=[]
    listpop=[]
    listcdcdeath=[]
    #variable to put all elements of a county for all age group in a list
    s=0
    sumdeath=[]
    listvalfinal=[]
    sumpop=[]
    #variable to check if there is any suppressed or unreliable in cdc death list
    q=0
    #list of summed death and population first element death and second element pop
    finallist=[]
    #put similar counties in a list and also the death, population and cdc death in list
    for key in result:
        s=s+1
        # print(key)

        if(s<6):
            if str(result[key]).isdigit()==False:
                if str(key[4]).isdigit()==True and str(key[6]).isdigit()==True:
                    listcounty.append(key[0])
                    listdeath.append(key[4])
                    listpop.append(key[6])
                    listcdcdeath.append(result[key])
        if s==5 and len(listcdcdeath)!=0:
                s=0
                #if dissimilar county in list
        
                if ((len(set( listcounty))) == 1):
                    # print('ok')
                    # print(listcounty)
                    # print(listcdcdeath)
                    for element in listcdcdeath:
                        if element.isdigit()==False:
                            q=1
                            break
                            # print("ok")
                    #putty the element which can be converted to integer in another list for addingfor death and pop column
                    if q==1:
                        for element in listdeath:
                            if str(element).isdigit()==True:
                                sumdeath.append(element)
                        for element in listpop:
                            if str(element).isdigit()==True:
                                sumpop.append(element)
                        q=0
                            # s=0
                            #converting all element of new list to integer for addition
                        for i in range(0, len(sumdeath)): 
                            sumdeath[i] = int(sumdeath[i]) 
                        for i in range(0, len(sumpop)): 
                            sumpop[i] = int(sumpop[i]) 
                            
                        death=0
                        pop=0
                        for ele in range(0, len(sumdeath)): 
                            death = death + sumdeath[ele]   
                        for ele in range(0, len(sumpop)): 
                            pop = pop + sumpop[ele]            
                        
                        finallist.append(death)
                        finallist.append(pop)
                        #tuple
                        resultmain = [listcounty[0],death,pop]
                        # print(resultmain)
                        #list of tuple containing county, total death and total pop
                        listvalfinal.append(resultmain)
                        # listvalfinal.append(Dict[listcounty[0]]=finallist)
                        # print(Dict)
                        
                        # print(death)
                        # print(pop)
                            

            


                        listcounty.clear()
                        listdeath.clear()
                        listpop.clear()
                        listcdcdeath.clear()
                        sumdeath.clear()
                        sumpop.clear()
                        finallist.clear()
                        

                    else:
                        # print('all values in cdc death column is integer')  
                        listcounty.clear()
                        listdeath.clear()
                        listpop.clear()
                        listcdcdeath.clear()
                        
                        
                    
                else:
                    # print('problem in input file, data for some age group is missing')
                    s=0
                
        elif s==5 and len(listcdcdeath)==0:
            s=0



    print(listvalfinal)  
   
    
    # print(listvalfinal)
    # print(result1)
    #list of element which will be the new column for method1
    method1list=[]
    #this variable is used to remove the element from listvalfinal as there are duplicate coun ty
    m=0
    #the cdcoutfile kept in dict where cdcdeath is the result[key] and others are values


    for keys in result1:
        m=m+1
        #first column of csv
        # print(keys[0])
        #if integer then keep same
        # print(result1[keys])
        if str(result1[keys]).isdigit()==True:
            method1list.append(result1[keys])
            # print(result1[keys])
            # if suppressed or unreliable then estimate
        
        
        elif (str(keys[4]).isdigit()==False or str(keys[6]).isdigit()==False):
            #listval =(county, totaldeath,totalpop)
            # print(result1[keys])
            method1list.append(result1[keys])
        
        else:
        
            for element in listvalfinal:
                if element[0]==keys[0]:
                    #keys[5] is the pop of the county, element[2] is the total pop and element[1] is the death
                    val=(int(keys[6])/element[2])*element[1]
                    # print(val)
                    method1list.append(val)
                    # print(keys[2])
                
                    break
                


                


    # print(method1list)
    #add the new column with method1 in the outputfile
    df1['Method1(Pop Only)']=method1list

     # num=num+1
    x = filename.split(".")
    outputfilename= x[0]+'(Method1)'+'.csv'
    print(outputfilename)
    #list to keep the difference column
    listdiffmethod1=[]
    df1.to_csv(outputfilename, mode = 'w', index=False)



  #to adjust the method1 column basing on cdc death column
   # print(adjusterror)

    cdcdeathlist=df1['CDCDeaths'].tolist()
    method2list = df1['Method1(Pop Only)'].tolist()
    # errorcdc=df1['Error(Method2(Pop+risk)'].tolist()

    #to correct method coluumn basing on the cdcdeathcolumn
    cdcdeathvallist=[]
    methodvallist=[]
    # errorvallist=[]


    for i,j in zip( cdcdeathlist,method2list):
            if i=='Suppressed' or i=='Not available':
               methodvallist.append(j)
            else:
                methodvallist.append('N/A')
        #    print (i,j)
    
    if len(cdcdeathlist)==len(method2list):
         print('same length')

    df1['Method1(Pop Only)'] =  methodvallist

    # df1['Error(Method2(Pop+Risk))'] =  method2error

    # #updated column that CDC reports and will add to the csv
    df1.to_csv(outputfilename, mode='w', index=False)





    with open(r"C:/Users/Fariba Afrin Irany/Desktop/study/Methods/method1/{}".format(outputfilename), "r") as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
        #  csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    # csvreader.next() also works in Python 2.
         next(csv_reader)
         for lines in csv_reader:
            #  next(csv_reader)
            #  csv_reader.next()
            #  lines = csv_reader.readlines()[1:]
             if str(lines[5]).isdigit()==True or str(lines[5]).isdigit()=='Not available':
                 
                 listdiffmethod1.append('N/A')
             else:
                try:
                      diff= float(lines[9])-float(lines[4])
                      listdiffmethod1.append(diff)
                except:

                  
                    listdiffmethod1.append('N/A')

    print(listdiffmethod1)
    df1['Error(Method1(Pop Only))']=listdiffmethod1
    df1.to_csv(outputfilename, mode='w', index=False)

    #making the suppressed value equla to the death value for all counties where only one age is suppressed, as methods are not really contributing towards it
