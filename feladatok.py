import random

def fel1():
    szam:int=int(input("Kérek egy páratlan számot: "))
    while(szam%2==0):
        szam:int=int(input("Kérek egy páratlan számot: "))
    print(szam)
    
def fel2():
    
    i:int=0
    db:int=0
    while(i<7):
        szam:int=int(random.random()*96)+5
        print(szam)
        if(szam%5==0):
            db+=1
        i+=1
    print(f"A számok között {db} db 5-tel osztható volt!")
    
def fel3(text, betu):
    
    i:int=0
    hossz=len(text)

    while(hossz[i]==betu):
        i+=1
        print(f": A szövegben {betu} db 'a' betű van")
        
    