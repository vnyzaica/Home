#coding:utf-8
f = open('document.txt', "w")

lst = [
    ["name family 1", 20],
    ["name family 2", 25],
    ["name family 3", 19],
    ["name family 4", 12],
    ["name family 5", 16],
    ["name family 6", 34],
    ["name family 7", 76],
]
for i in range(0, len(lst), 1):

   print("name " + lst[i][0] + " how_old " + str(lst[i][1]))
s = 0
q =int(len(lst[0]))
w =int(len(lst[1]))
e =int(len(lst[2]))
r =int(len(lst[3]))
t =int(len(lst[4]))
y =int(len(lst[5]))
u =int(len(lst[6]))

if q > 15:
    s +=1
if w > 15:
    s +=1
if e > 15:
    s +=1
if r > 15:
    s +=1
if t > 15:
    s +=1
if y > 15:
    s +=1
if u > 15:
    s +=1
q = lst[1][-1]
print (q)
print (s)

f.write(str(x) + '\n' + str(x))

f = open('document.txt', "w")

f.close()



