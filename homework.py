#Задание 1
fruits = ['apple', 'banana', 'Apricot']
#if fruits[0][0] == 'a':
    #fruits.remove('apple')
#if fruits[1][0] == 'b':
    #print(fruits[1])
#if fruits[1][0] == 'A':
# (если я правильно поняла, здесь будет fruits[1][0] тк после первого условия слово удаляется из списка и он становится короче. По-другому просто не срабатывает программа, выдавая ошибку
    #fruits.remove('Apricot')
#print(fruits)
#Result['banana']
#if fruits[0][0] == 'a':
    #fruits.pop(0)
#if fruits[1][0] == 'b':
    #print(fruits[1])
#if fruits[1][0] == 'A':
    #fruits.pop(1)
#print(fruits)
#второй вариант
#fruits_new = []
#if fruits[0][0] == 'a':
   # fruits_new.append('apple')
#if fruits[1][0] == 'b':
    #fruits_new.append('banana')
#if fruits[2][0] == 'A':
    #fruits_new.append('Apricot')
#print (fruits_new)
#result ['apple', 'banana', 'Apricot']
#2 задание
#nums = [1, 2, 3, 4]
#number =int(input('Add any number'))
#position = int(input ('State the position of the number'))
#position1= position - 1
#if position > 5:
   # print('Error')
#else:
    #nums.insert(position1, number)
    #print(nums)
#Result Add any number8
#State the position of the number3
#[1, 2, 8, 3, 4]
#Задание 3
#names = ['Sam', 'Erik', 'Kris', 'Sasha', 'Bob', 'Mark']
#del names[1:5]
#print(names)
names = ['Sam', 'Erik', 'Kris', 'Sasha', 'Dan', 'Mark']
length = len(names)
if length == 4:
    del names[1:3]
if length > 4:
    del names[1: length-1]
if length < 4:
    del names[1: length-1]
print(names)
#Results: names = ['Sam', 'Erik', 'Kris', 'Sasha']   ['Sam', 'Sasha']
#names = ['Sam', 'Erik', 'Kris', 'Sasha', 'Dan']  ['Sam', 'Dan']
#names = ['Sam', 'Erik', 'Kris', 'Sasha', 'Dan', 'Mark']  ['Sam', 'Mark']





