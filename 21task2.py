

k=[1,1,3,4,5,6,77,77]
l=[]
for i in k:
    if i not in l:
        l.append(i)
print(l)                     


list=[1,2.5,3,4,'hi','hw',True,False,4+6j]
integer_list=[]
float_list=[] 
string_list=[]
complex_list=[]
boolean_list=[]
for i in list:
    if type (i)==int:
        integer_list.append(i)
    elif(type(i)==float):
        float_list.append(i)
    elif(type(i)==str):
        string_list.append(i)
    elif(type(i)==complex):
        complex_list.append(i)
    elif(type(i)==bool):
        boolean_list.append(i)
    print(integer_list,float_list,string_list,complex_list,boolean_list)

