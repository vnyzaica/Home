file = open('file.txt') #Можно довабить ,"a+" и тогда файл создаться
z = file.read()
print (z)
file.close()
x=int(1)
while x > 0 :
    file = open('file.txt','a+')
    print('Ты всегда можешь закончить. Нажми ctrl + c')
    x += 1
    name = input('Введите имя')
    family = input('Введите фамилию')
    old = input('Введите возраст')
    file.write(name)
    file.write(family)
    file.write(old)
    file.write("        ")
    file.close()
    