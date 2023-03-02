import random

pt1=0
pt2=0

for i in range(0,5):
    person1=input("enter  rock or paper or scissor: ")
    person2=random.choice(["rock","paper","scissor"])
    if(person1=="rock" and person2=="paper"):
        pt2=pt2+1
    
    elif(person1=="rock" and person2=="scissor"):
        pt1=pt1+1
    
    elif(person1=="rock" and person2=="rock"):
        pt1=0
        pt2=0
        
    elif(person1=="paper" and person2=="rock"):
        pt1=pt1+1
        
    elif(person1=="paper" and person2=="scissor"):
        pt2=pt2+1
        
    elif(person1=="paper" and person2=="paper"):
        pt1=0
        pt2=0
    
    elif(person1=="scissor" and person2=="rock"):
        pt2=pt2+1
    
    elif(person1=="scissor" and person2=="paper"):
        pt1=pt1+1
        
    elif(person1=="scissor" and person2=="scissor"):
        pt1=0
        pt2=0
    
    
    print(person1)
    print(person2)
    print(pt1)
    print(pt2)
        
        
if(pt1>pt2):
    print("person 1 is winner")
elif(pt2>pt1):
    print("person 2 is winner")
else:
    print("it is a draw")
        