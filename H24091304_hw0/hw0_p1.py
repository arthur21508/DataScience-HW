# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:08:19 2021

@author: 孫亞瑄
"""
def sym(a,b):
    if a=="+" and b=="+":
        return "+"
    elif a=="+" and b=="-":
        return "-"
    elif a=="-" and b=="+":
        return "-"
    elif a=="-" and b=="-":
        return "+"
    
    

def mul(items):
    items.append([])
    for i in items[0]:
        for j in items[1]:
            coef=sym(i[0][0],j[0][0])+str(int(i[0][1:])*int(j[0][1:]))
            value=i[1]+j[1]
            items[-1].append([coef,value])
    del items[0]
    del items[0]
    
    if len(items)!=1:
        mul(items)



poly=input("Input the polymials:")
poly=poly.replace("(",")")
poly=poly.replace("*","")
poly=poly.replace("^","")
poly=poly.split(")")
for i in poly:
    if i=="":
        poly.remove(i)
for i in range(len(poly)):
    if poly[i][0]!="-":
        poly[i]="+"+poly[i]

items=[]
for i in range(len(poly)):
    items.append([])
for i in range(len(poly)):
    start=0
    for j in range(1,len(poly[i])):
        if poly[i][j]=="+" or poly[i][j]=="-":
            items[i].append(poly[i][start:j])
            start=j
    items[i].append(poly[i][start:])
for i in items:
    for j in range(len(i)):
        if i[j][1].isdigit()==False:
            i[j]=i[j][0]+"1"+i[j][1:]
for i in items:
    for j in range(len(i)):
        for k in range(len(i[j])):
            if i[j][k].isalpha():
                i[j]=i[j][:k]+","+i[j][k:]
                i[j]=i[j].split(",")
                break
for i in items:
    for j in range(len(i)):
        if isinstance(i[j],str):
            i[j]=[i[j],""]
for i in items:
    for j in i:
        for k in range(10000):
            if k<len(j[1]) and j[1][k].isalpha() and k+1<len(j[1]) and j[1][k+1].isdigit():
                for l in range(10000):
                    if k+1+l<len(j[1]) and j[1][k+1+l].isdigit()==False:
                        j[1]=j[1][:k]+j[1][k]*int(j[1][k+1:k+1+l])+j[1][k+1+l:]
                        break
                    elif k+1+l==len(j[1])-1:
                        j[1]=j[1][:k]+j[1][k]*int(j[1][k+1:])
                        break

mul(items)
items=items[0]

set_alpha=set()
for i in items:
    for j in i[1]:
        set_alpha.add(j)
list_alpha=[]
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if i in set_alpha:
        list_alpha.append(i)
for i in list_alpha:
    for j in range(len(items)):
        times=items[j][1].count(i)
        items[j][1]=items[j][1].replace(i,"")
        if times!=0 and times!=1:
            items[j][1]+=i+"^"+str(times)
        elif times==1:
            items[j][1]+=i
set_items=set()
dict_items={}
result=[]
for i in items:
    set_items.add(i[1])
for i in set_items:
    dict_items[i]=0
for i in items:
    if i[0][0]=="+":
        dict_items[i[1]]+=int(i[0][1:])
    elif i[0][0]=="-":
        dict_items[i[1]]-=int(i[0][1:])
for i in dict_items:
    dict_items[i]=str(dict_items[i])
    if dict_items[i][0]!="-":
        dict_items[i]="+"+dict_items[i]
    if dict_items[i]=="+1":
        dict_items[i]="+"
    elif dict_items[i]=="-1":
        dict_items[i]="-"
    else:
        dict_items[i]+="*"

output=""
for i in dict_items:
    output+=dict_items[i]+i
if output[0]=="+":
    output=output[1:]

print("Output result:",output)




