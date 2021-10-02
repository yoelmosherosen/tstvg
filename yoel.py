import random
def radom():
 li={}
 num=0
 numb=100000000
 for i in range(numb):
      number= random.randint(1,10)
      if li.get(number):
        num = li.get(number)+1
        li[number]=num
      else: li[number]=1  
    
 Percent=(li.get(1)/numb)*100
 print("Number of times 1 was selected from "+str(numb)+" attempts is:"+str(li.get(1))+"  Percent is:",Percent )
    



def image(str,Percent):

    counter=0
    arr=[]
    place_index={}
   
    for i in range(len(str)):
        for j in range(len(str[i])):
            place_index[str[i][j]]=[i,j]
        
    namber_black=(len(place_index.keys())/100)*Percent
    arr=sorted( place_index.keys())

    for i in range(int(namber_black)):
        at=place_index.get(arr[i])
        str[at[0]][at[1]]=0

    for i in range(len(str)):
        for j in range(len(str[i])):  
            if str[i][j]!=0:
               str[i][j]=256

def palindrom(arr):

    lambda j: j<8


    

  
    k= list(filter(lambda k:k[1]<101 ,arr.items()))
    
   
    print(k[0])
    k[0]=3
    print(k[0])
    a=(3,5)
    a[0]=2

gmra={"shimi":99.5,"yoel":0,"sheor":70,"ff":99,"dvid":10}
 
palindrom(gmra) 

        







str=[[7,8],
    [8,88,9],
    [7,912,1000],
    [227,333,765,987]]
 
image(str,10)   