

def even_number(l:list):
    listeven=[l[i] for i in range(len(l)) if l[i] %2 ==0]
    return listeven

liste=[] 
n = int(input("number of ints to enter:  "))
for i in range (n):
    x=int(input("enter no: \n")) 
    liste.insert(i,x)
    i+=1
print(even_number(liste))