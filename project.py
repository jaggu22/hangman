from random import randint
def fetchdata(fo):
 """RETURNS A LIST WITH DICTINORIES OF NAMES AND HINTS
                                  ZEROTH DICT SERVES AS INDEX TO OTHER DICTS"""
 l=[{}]
 j=0
 f=open(fo,"r")
 for i in f:
   if(i[0]=='@'):
    j+=1
    k=i[1:-1]
    l[0][k]=j
    l.append({})
   elif(i[0]=='~'):
     key=i[1:-1]
     l[j][key]=[]
   else:
     l[j][key].append(i[0:-1])
 f.close()
 return(l) 
#-------------------------------------------fetching data-----------------------

def guess(n,word,hints):
    a=n
    guessed=""
    for i in word:
       print('_',end=' ')
    while(a>0):
     print("\nYou have {} trails".format(a))
     if(a<len(hints) and a!=n):
      print("Here is a hint\n",hints.pop())
     entry=input("\n Enter your guess:")
     entry=entry[:len(word)]
     d=False
     for i in entry:
      if(i in word and i not in guessed):
       guessed+=i
       d=True
     if(d and entry!=word):
      print("You missed\nBut you moved a step forward")
     a-=1
     for i in word:
      if(i in guessed):
       print(i,end=' ')
      else:
       print('_',end=' ')
     if(entry==word):
      print("\nYou win Congratulations")
      return(1)
    print("The trials are over")
    print("You lost\t Try again")
    return(0)

def start_game(d,level):
    word=list(d.keys())
    word=word[randint(0,len(word)-1)]
    n=len(word)
    n=round(n/level)+1
    guess(n,word,d[word])

l=fetchdata("pp.txt")
start_game(l[1],2)
