


def arithmetic (a,b,c):
    if c == "+":
        x = a+b
    else:
        if c == "*" :
            x = a * b
        else: 
            if c == "-":
                x = a-b
            else:
                if c == "/":
                    x = a/b
                else:
        	        print("Неизвастная операция")
    print(x)
x = int(0)	
a = int(input("Введите число 1"))
b = int(input("Введите число 2"))
c = input("Введите знак")

arithmetic(a,b,c)
print(x)


    