# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:52:43 2021

@author: 孫亞瑄
"""

f=open("IMDB-Movie-Data.csv","r")
list_f=f.read()
list_f=list_f.split("\n")
for i in range(1,len(list_f)-1):
    list_f[i]=list_f[i].split(",")
    list_f[i][4]=list_f[i][4].split("|")
    list_f[i][2]=list_f[i][2].split("|")
    for j in range(len(list_f[i][4])):
        if list_f[i][4][j][0]==" ":
            list_f[i][4][j]=list_f[i][4][j][1:]
    if list_f[i][9]=="":
        list_f[i][9]=0


#Q1
list_rating=[]
for i in range(1,len(list_f)-1):
    if list_f[i][5]=="2016":
        list_rating.append("%s:%f" %(list_f[i][1],float(list_f[i][7])))
    if len(list_rating)>=3:
        break
print("Q1:Top-3 movies with the highest ratings in 2016?")
for i in list_rating:
    print(i)
print("")


#Q2
dict_revenue={}
for i in range(1,len(list_f)-1):
    for j in list_f[i][4]:
        if j not in dict_revenue:
            dict_revenue[j]=0
        dict_revenue[j]+=(float(list_f[i][9])/len(list_f[i][4]))
max_ar_person=""
max_ar=0
for i in dict_revenue:
    if dict_revenue[i] > max_ar:
        max_ar=dict_revenue[i]
        max_ar_person=i
print("Q2:The actor generating the highest average revenue?")
print(max_ar_person+":"+str(max_ar))
print("")

#Q3
ar_ew=0
ar_t=0
for i in range(1,len(list_f)-1):
    for j in list_f[i][4]:
        if j=="Emma Watson":
            ar_ew+=float(list_f[i][7])
            ar_t+=1
print("Q3:The average rating of Emma Watson’s movies?")
print(ar_ew/ar_t)
print("")


#Q4
dict_dir={}
for i in range(1,len(list_f)-1):
    if list_f[i][3] not in dict_dir:
        dict_dir[list_f[i][3]]=[]
    for j in list_f[i][4]:
        if j not in dict_dir[list_f[i][3]]:
            dict_dir[list_f[i][3]].append(j)
for i in dict_dir:
    dict_dir[i]=len(dict_dir[i])
dir_max=0
list_dir=[]
for i in dict_dir:
    if dict_dir[i]>dir_max:
        dir_max=dict_dir[i]
while True:
    for i in dict_dir:
        if dict_dir[i]==dir_max:
            list_dir.append("%s:%d" %(i,dict_dir[i]))
    if len(list_dir)>=3:
        break
    else:
        dir_max-=1
print("Q4:Top-3 directors who collaborate with the most actors?")
for i in list_dir:
    print(i)
print("")


#Q5
dict_actor={}
for i in range(1,len(list_f)-1):
    for j in list_f[i][4]:
        if j not in dict_actor:
            dict_actor[j]=[]
        for k in list_f[i][2]:
            if k not in dict_actor[j]:
                dict_actor[j].append(k)
for i in dict_actor:
    dict_actor[i]=len(dict_actor[i])
act_max=0
list_act=[]
for i in dict_actor:
    if dict_actor[i]>act_max:
        act_max=dict_actor[i]
while True:
    for i in dict_actor:
        if dict_actor[i]==act_max:
            list_act.append("%s:%d" %(i,dict_actor[i]))
    if len(list_act)>=2:
        break
    else:
        act_max-=1
print("Q5:Top-2 actors playing in the most genres of movies?")
for i in list_act:
    print(i)
print("")


#Q6
dict_actor1={}
for i in range(1,len(list_f)-1):
    for j in list_f[i][4]:
        if j not in dict_actor1:
            dict_actor1[j]=[0,3000]
        if int(list_f[i][5])>dict_actor1[j][0]:
            dict_actor1[j][0]=int(list_f[i][5])
        if int(list_f[i][5])<dict_actor1[j][1]:
            dict_actor1[j][1]=int(list_f[i][5])
for i in dict_actor1:
    dict_actor1[i]=dict_actor1[i][0]-dict_actor1[i][1]
gap_max=0
gap_actor=[]
for i in dict_actor1:
    if dict_actor1[i]>gap_max:
        gap_max=dict_actor1[i]
for i in dict_actor1:
    if dict_actor1[i]==gap_max:
        gap_actor.append(i)
print("Q6:Top-3 actors whose movies lead to the largest maximum gap of years?")
print(gap_actor)
print("")


#Q7      
list_relation=["Johnny Depp"]
for i in list_relation:
        for j in range(1,len(list_f)-1):
            if i in list_f[j][4]:
                for k in list_f[j][4]:
                    if k not in list_relation:
                        list_relation.append(k)
print("Q7:Find all actors who collaborate with Johnny Depp in direct and indirect ways")
print(list_relation)




        

