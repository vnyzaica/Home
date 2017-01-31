#coding : utf - 8
import random
import time
Ap = {"one":"X","two":"X","three":"X"}
Bp = {"one":"X","two":"X","three":"X"}
Cp = {"one":"X","two":"X","three":"X"}
A = {"one":"0","two":"0","three":"0"}
B = {"one":"0","two":"0","three":"0"}
C = {"one":"0","two":"0","three":"0"}

A["one"]=random.randint(0,1)
A["two"]=random.randint(0,1)
A["three"]=random.randint(0,1)
B["one"]=random.randint(0,1)
B["two"]=random.randint(0,1)
B["three"]=random.randint(0,1)
C["one"]=random.randint(0,1)
C["two"]=random.randint(0,1)
C["three"]=random.randint(0,1)
def pole():
    print(Ap["one"],Ap["two"],Ap["three"])
    print(Bp["one"],Bp["two"],Bp["three"])
    print(Cp["one"],Cp["two"],Cp["three"])
def lose():
    print("Lose")
    print('''
 
 _________Oooo_
__oooO___(___)_
_(___)____)__/_
_\__(____(__/__
__\__)_________

 
''')
    time.sleep(10)
    exit(0)
def goA():
    if g == "1":
        if A["one"]==1:
            lose()
        else:
            Ap["one"] = 0
    if g == "2":
        if A["two"]== 1:
            lose()
        else:
            Ap["two"] = 0
    if g == "3": 
        if A["three"]== 1:
            lose()
        else:
            Ap["three"] = 0
def goB():
    if g == "1":
        if B["one"]==1:
            lose()
        else:
            Bp["one"] = 0
    if g == "2":
        if B["two"]== 1:
            lose()
        else:
            Bp["two"] = 0
    if g == "3": 
        if B["three"]== 1 :
            lose()
        else:
            Bp["three"] = 0

def goC():
    if g == "1":
        if C["one"]==1:
            lose()
        else:
            Cp["one"] = 0
    if g == "2":
        if C["two"]== 1:
            lose()
        else:
            Cp["two"] = 0
    if g == "3": 
        if C["three"]== 1:
            lose()
        else:
            Cp["three"] = 0
x=("a")
z=int("8")

while z != 0 :

    x = input("Write right coordinats  ")
        
    f = (x[0])
    g = (x[1])
    if f == "A":
        goA()
    elif f == "B":
    
        goB()
    else:
    
        goC()
    pole()
    z = z-1


